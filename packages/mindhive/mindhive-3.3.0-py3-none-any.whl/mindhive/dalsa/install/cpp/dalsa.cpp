#include "cordef.h"
#include "gevapi.h"
#include "GenApi/GenApi.h"
#include <string.h>
#include <sys/time.h>

using namespace GenApi;

#define CHECK(call) { int _status = call; if (_status) { lastFailedFunc = #call; return _status; } }

#define STR_EQ 0

extern "C" {
    static const int MAX_CAM_COUNT = 32;
    static const int BUFFERS_PER_CAMERA = 100;
    static const int MIN_STREAM_MEMORY_LIMIT = 64 * 1024 * 1024;

    static const int MAX_HZ = 2000;
    static const int LINE_PULSE_US = (1000000 / MAX_HZ) / 10;
    static const int LINE_DEBOUNCE_US = LINE_PULSE_US / 10;

    thread_local const char* lastFailedFunc = "<none>";

    typedef struct {
        GEV_CAMERA_HANDLE handle;
        UINT64 payloadSize;
        PUINT8 buffers[BUFFERS_PER_CAMERA];
    } CameraData;
    CameraData cameras[MAX_CAM_COUNT] = {0};

    GEV_CAMERA_INFO camera_info[MAX_CAM_COUNT] = {0};

    int camCount;

    struct CameraInfo {
        int index;
        UINT32 ipAddr;
        char* serial;
        UINT32 hostInterfaceIdx;
    };

    struct BufferStats {
        UINT32 total;
        UINT32 used;
        UINT32 free;
        UINT32 trashed;
    };

    int get_max_cameras() {
        return MAX_CAM_COUNT;
    }

    const char* get_last_failed_func() {
        return lastFailedFunc;
    }

    int initialize() {
        CHECK(GevApiInitialize());
        GEVLIB_CONFIG_OPTIONS options = {0};
        GevGetLibraryConfigOptions( &options);
        options.logLevel = GEV_LOG_LEVEL_TRACE;
        GevSetLibraryConfigOptions( &options);
        return GEVLIB_OK;
    }

    int get_cameras(CameraInfo pyCameras[], int maxCameras, int *numCameras) {
        if (maxCameras > MAX_CAM_COUNT) {
            lastFailedFunc = "Max camera check";
            return GEVLIB_ERROR_INSUFFICIENT_MEMORY;
        }
        CHECK(GevGetCameraList(camera_info, MAX_CAM_COUNT, &camCount));
        *numCameras = camCount < maxCameras ? camCount : maxCameras;
        for ( int i = 0; i < *numCameras; i++ ) {
            GEV_CAMERA_INFO *cam = &camera_info[i];
            pyCameras[i] = {i, cam->ipAddr, cam->serial, cam->host.ifIndex};
        }
        return GEVLIB_OK;
    }

    int get_float_feature(int camIndex, const char* feature, float* value) {
        CameraData *camera = &cameras[camIndex];
        int type;
        CHECK(GevGetFeatureValue(camera->handle, feature, &type, sizeof(float), value));
        if (type != GENAPI_FLOAT_TYPE) {
            lastFailedFunc = "Checking type";
            return GEVLIB_ERROR_ARG_INVALID;
        }
        return GEVLIB_OK;
    }

    int get_int_feature(int camIndex, const char* feature, int* value) {
        CameraData *camera = &cameras[camIndex];
        int type;
        CHECK(GevGetFeatureValue(camera->handle, feature, &type, sizeof(int), value));
        if (type != GENAPI_INTEGER_TYPE && type != GENAPI_ENUM_TYPE) {
            lastFailedFunc = "Checking type";
            return GEVLIB_ERROR_ARG_INVALID;
        }
        return GEVLIB_OK;
    }

    int get_string_feature(int camIndex, const char* feature, char* value, int string_size) {
        CameraData *camera = &cameras[camIndex];
        int type;
        CHECK(GevGetFeatureValueAsString(camera->handle, feature, &type, string_size, value));
        return GEVLIB_OK;
    }

    int set_float_feature(CameraData *camera, const char* feature, double value) {
        return GevSetFeatureValue(camera->handle, feature, sizeof(value), &value);
    }

    int set_int_feature(CameraData *camera, const char* feature, int value) {
        return GevSetFeatureValue(camera->handle, feature, sizeof(value), &value);
    }

    int set_bool_feature(CameraData *camera, const char* feature, bool value) {
        return GevSetFeatureValue(camera->handle, feature, sizeof(value), &value);
    }

    int set_string_feature(CameraData *camera, const char* feature, const char* value) {
        return GevSetFeatureValueAsString(camera->handle, feature, value);
    }

    int exec_command(CameraData *camera, const char* command, bool wait = true) {
        int cmd = 1;
        int status = GevSetFeatureValue(camera->handle, command, sizeof(cmd), &cmd);

        if (wait && (status == 0)) {
            // Wait for command to complete.
            int done = 0;
            int type;
            do {
                Sleep(20); // Sleep 20ms for polling.
                status = GevGetFeatureValue(camera->handle, command, &type, sizeof(done), &done);
            } while( !done && (status == 0));
        }
        return status;
    }

    int open_camera(int camIndex) {
        CameraData *camera = &cameras[camIndex];
        CHECK(GevOpenCamera(&camera_info[camIndex], GevExclusiveMode, &camera->handle));
        return GEVLIB_OK;
    }

    int config_camera(
        int camIndex,
        bool sync,
        int height,
        float rateHz,
        float exposureMicros,
        float gain,
        bool reverseX,
        int format,
        bool binning,
        const char* calibrationSet,
        int packetSize
    ) {
        CameraData *camera = &cameras[camIndex];

        CHECK(set_float_feature(camera, "AcquisitionLineRate", rateHz));
        CHECK(set_float_feature(camera, "ExposureTime", exposureMicros));

        if (sync) {
            bool master = camIndex == 0;
            CHECK(set_string_feature(camera, "TriggerSelector", "LineStart"));
            CHECK(set_string_feature(camera, "TriggerMode", master ? "Off" : "On"));
            CHECK(set_string_feature(camera, "LineSelector", "Line3"));
            CHECK(set_string_feature(camera, "LineFormat", "RS422"));
            CHECK(set_string_feature(camera, "LineMode", master ? "Output" : "Input"));
            if (master) {
              CHECK(set_string_feature(camera, "outputLineSource", "PulseOnStartofLine"));
              CHECK(set_int_feature(camera, "outputLinePulseDelay", 0));
              CHECK(set_int_feature(camera, "outputLinePulseDuration", LINE_PULSE_US));
            } else {
              CHECK(set_string_feature(camera, "TriggerSource", "Line3"));
              CHECK(set_string_feature(camera, "TriggerActivation", "RisingEdge"));
              CHECK(set_string_feature(camera, "TriggerOverlap", "previousLine"));
              CHECK(set_int_feature(camera, "lineDebouncingPeriod", LINE_DEBOUNCE_US));
              CHECK(set_string_feature(camera, "lineElectricalTermination", "Enabled"));
            }
        } else {
            CHECK(set_string_feature(camera, "TriggerSelector", "LineStart"));
            CHECK(set_string_feature(camera, "TriggerMode", "Off"));
        }

        CHECK(set_float_feature(camera, "sensorLineSpatialCorrection", reverseX ? 0.25 : 0.5));

        int width;
        CHECK(get_int_feature(camIndex, "SensorWidth", &width));
        if (binning) {
            width = width / 2;
        }
        CHECK(set_int_feature(camera, "BinningHorizontal", binning ? 2 : 1));
        CHECK(GevSetImageParameters(camera->handle, width, height, 0, 0, format));

        CHECK(set_string_feature(camera, "GainSelector", "DigitalAll"));
        CHECK(set_float_feature(camera, "Gain", gain));

        if (calibrationSet) {
            CHECK(set_string_feature(camera, "flatfieldCorrectionCurrentActiveSet", calibrationSet));
            CHECK(set_string_feature(camera, "flatfieldCorrectionMode", "Active"));
        } else {
            CHECK(set_string_feature(camera, "flatfieldCorrectionMode", "Off"));
        }

        CHECK(set_bool_feature(camera, "ReverseX", reverseX));
        CHECK(set_string_feature(camera, "sensorScanDirection", reverseX ? "Reverse" : "Forward"));

        UINT32 returnFormat;
        CHECK(GevGetPayloadParameters(camera->handle, &camera->payloadSize, &returnFormat));
        for (int i = 0; i < BUFFERS_PER_CAMERA; i++) {
            camera->buffers[i] = (PUINT8)malloc(camera->payloadSize);
            memset(camera->buffers[i], 0, camera->payloadSize);
        }

        // As per DALSA example but dropped thread affinity, made it worse
        GEV_CAMERA_OPTIONS camOptions = {0};
        CHECK(GevGetCameraInterfaceOptions( camera->handle, &camOptions));
        camOptions.streamFrame_timeout_ms = 1001;
        camOptions.streamNumFramesBuffered = 16;  // Buffer frames internally.
        UINT32 streamMemoryLimitMax = camOptions.streamNumFramesBuffered * camera->payloadSize;
        if (streamMemoryLimitMax < MIN_STREAM_MEMORY_LIMIT) {
            streamMemoryLimitMax = MIN_STREAM_MEMORY_LIMIT;
        }
        camOptions.streamMemoryLimitMax = streamMemoryLimitMax;  // Adjust packet memory buffering limit.
        camOptions.streamPktSize = packetSize;                   // Adjust the GVSP packet size.
        // Add microseconds between packets to pace arrival at NIC.
        // Try and stagger between cameras to avoid slamming switch with them at the same time.
        camOptions.streamPktDelay = 10 * (camIndex + 1);
        CHECK(GevSetCameraInterfaceOptions( camera->handle, &camOptions));

        CHECK(GevInitializeTransfer(camera->handle, SynchronousNextEmpty, camera->payloadSize, BUFFERS_PER_CAMERA, camera->buffers));

        return GEVLIB_OK;
    }

    int set_exposure(int camIndex, float exposureMicros) {
        CameraData *camera = &cameras[camIndex];
        CHECK(set_float_feature(camera, "ExposureTime", exposureMicros));
        return GEVLIB_OK;
    }

    UINT64 _current_epoch_microseconds() {
        struct timeval tv;
        gettimeofday(&tv, nullptr);
        return static_cast<UINT64>(tv.tv_sec) * 1000 * 1000 + tv.tv_usec;
    }

    int start_acquisition(int camIndex, UINT64 start_epoch_microseconds) {
        CameraData *camera = &cameras[camIndex];
        while (_current_epoch_microseconds() < start_epoch_microseconds);
        CHECK(GevStartTransfer(camera->handle, -1));
        return GEVLIB_OK;
    }

    int wait_for_image(int camIndex, GEV_BUFFER_OBJECT **result, BufferStats *stats, int timeoutMillis) {
        *result = nullptr;
        CameraData *camera = &cameras[camIndex];
        int status = GevWaitForNextFrame(camera->handle, result, timeoutMillis);
        *stats = {0};
        GevBufferCyclingMode mode;
        GevQueryTransferStatus(camera->handle, &stats->total, &stats->used, &stats->free, &stats->trashed, &mode);
        if (status) {
          return status;
        }
        return (*result)->status;
    }

    int release_image(int camIndex, GEV_BUFFER_OBJECT *result) {
        if (result) {
            CameraData *camera = &cameras[camIndex];
            GevReleaseImage(camera->handle, result);
        }
        return GEVLIB_OK;
    }

    int start_timed_line_counter(int camIndex, const char* line, const char* detectionLevel, int timerDuration) {
        CameraData *camera = &cameras[camIndex];
        CHECK(set_string_feature(camera, "LineSelector", line));
        CHECK(set_string_feature(camera, "LineFormat", "SingleEnded"));
        CHECK(set_string_feature(camera, "lineDetectionLevel", detectionLevel));
        CHECK(set_int_feature(camera, "lineDebouncingPeriod", 1000));

        CHECK(set_string_feature(camera, "counterSelector", "Counter1"));
        CHECK(set_string_feature(camera, "counterMode", "Off"));
        CHECK(set_string_feature(camera, "counterStartSource", "Timer1End"));
        CHECK(set_string_feature(camera, "counterIncrementalSource", line));
        CHECK(set_string_feature(camera, "counterIncrementalLineActivation", "RisingEdge"));
        CHECK(set_string_feature(camera, "counterResetSource", "Timer1End"));

        CHECK(set_string_feature(camera, "timerSelector", "Timer1"));
        CHECK(set_string_feature(camera, "timerMode", "Off"));
        CHECK(set_string_feature(camera, "timerStartSource", "Timer1End"));
        CHECK(set_int_feature(camera, "timerDuration", timerDuration));

        CHECK(set_string_feature(camera, "counterMode", "Active"));
        CHECK(set_string_feature(camera, "timerMode", "Active"));

        return GEVLIB_OK;
    }

    int get_counter_state(int camIndex, int* count, int* timerDuration) {
        CHECK(get_int_feature(camIndex, "counterValueAtReset", count));
        CHECK(get_int_feature(camIndex, "timerDuration", timerDuration));
        return GEVLIB_OK;
    }

    int start_line_timer(int camIndex, const char* line, const char* detectionLevel, int maxDuration) {
        CameraData *camera = &cameras[camIndex];
        CHECK(set_string_feature(camera, "LineSelector", line));
        CHECK(set_string_feature(camera, "LineFormat", "SingleEnded"));
        CHECK(set_string_feature(camera, "lineDetectionLevel", detectionLevel));
        CHECK(set_int_feature(camera, "lineDebouncingPeriod", 1000));

        CHECK(set_string_feature(camera, "counterSelector", "Counter1"));
        CHECK(set_string_feature(camera, "counterMode", "Off"));
        CHECK(set_string_feature(camera, "counterStartSource", line));
        CHECK(set_string_feature(camera, "counterStartLineActivation", "RisingEdge"));
        CHECK(set_string_feature(camera, "counterIncrementalSource", "InternalClock"));
        CHECK(set_string_feature(camera, "counterResetSource", line));
        CHECK(set_string_feature(camera, "counterResetLineActivation", "RisingEdge"));
        CHECK(set_int_feature(camera, "counterDuration", maxDuration));

        CHECK(set_string_feature(camera, "counterMode", "Active"));
        return GEVLIB_OK;
    }

    int get_timer(int camIndex, int* lastTimerDuration) {
        char status[64] = {0};
        CHECK(get_string_feature(camIndex, "counterStatus", status, sizeof(status)));
        if (strncmp(status, "CounterTriggerWait", sizeof(status)) == STR_EQ) {
            *lastTimerDuration = -1;  // Haven't seen first signal
        } else if (strncmp(status, "CounterActive", sizeof(status)) == STR_EQ) {
            CHECK(get_int_feature(camIndex, "counterValueAtReset", lastTimerDuration));
            if (*lastTimerDuration == 0) {
                *lastTimerDuration = -2;  // Waiting to complete first timing
            }
        } else {
            *lastTimerDuration = -3;  // Hit max or overflowed
        }
        return GEVLIB_OK;
    }

    void stop_acquisition(int camIndex) {
        CameraData *camera = &cameras[camIndex];
        if (camera->handle == NULL) {
            return;
        }
        GevAbortTransfer(camera->handle);
        GevFreeTransfer(camera->handle);
    }

    int reset_camera(int camIndex) {
        CameraData *camera = &cameras[camIndex];
        GevAbortTransfer(camera->handle);
        GevFreeTransfer(camera->handle);
        int status = exec_command(camera, "DeviceReset", false);
        if (status && status != -1) {  // Ignore expected ERROR_GENERIC (-1)
            lastFailedFunc = "exec_command(camera, \"DeviceReset\", false)";
            return status;
        }
        // Following fails as camera is rebooting
        // GevCloseCamera(&camera->handle);
        camera->handle = nullptr;
        return GEVLIB_OK;
    }

    void close_camera(int camIndex) {
        CameraData *camera = &cameras[camIndex];
        if (!camera->handle) {
            return;
        }
        GevAbortTransfer(camera->handle);
        GevFreeTransfer(camera->handle);
        GevCloseCamera(&camera->handle);
        camera->handle = nullptr;
    }

    void teardown() {
        for (int i = 0; i < MAX_CAM_COUNT; i++) {
          close_camera(i);
        }
        GevApiUninitialize();
        _CloseSocketAPI();
    }

    int _max_file_access_length(CameraData *camera) {
        GenApi::CNodeMapRef *node = static_cast<GenApi::CNodeMapRef*>(GevGetFeatureNodeMap(camera->handle));
        if (!node) {
            return 0;
        }
        CIntegerPtr accessLength = node->_GetNode("FileAccessLength");
        return accessLength->GetMax();
    }

    int _download_file(CameraData *camera, const char* fileName, void *data, int dataSize) {
        int file_size;
        int type;

        //========================================================
        // Open the camera file for read access;
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileSelector", fileName));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Open"));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileOpenMode", "Read"));

        CHECK(exec_command(camera, "FileOperationExecute"));

        // Get the file size from the camera.
        CHECK(GevGetFeatureValue(camera->handle, "FileSize", &type, sizeof(file_size), &file_size));

        if (file_size == 0) {
            lastFailedFunc = "file_size == 0";
            return GEVLIB_ERROR_NULL_PTR;
        }
        if (file_size > dataSize) {
            lastFailedFunc = "file_size > dataSize";
            return GEVLIB_ERROR_DATA_OVERFLOW;
        }

        int maxBytes = _max_file_access_length(camera);
        if (!maxBytes) {
            lastFailedFunc = "maxBytes is null";
            return GEVLIB_ERROR_NULL_PTR;
        }

        unsigned char *pBuf = (unsigned char *)data;

        // Read data from the camera (in a loop)
        int byteOffset = 0;
        while (byteOffset < file_size ) {
            int type;
            int bytesRead;
            int bytesToRead = dataSize - byteOffset;
            if (bytesToRead > maxBytes){
                bytesToRead = maxBytes;
            }

            // Set up the read offset in the camera
            CHECK(GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Read"));

            CHECK(GevSetFeatureValue(camera->handle, "FileAccessLength",  sizeof(UINT32), &bytesToRead));
            CHECK(GevSetFeatureValue(camera->handle, "FileAccessOffset", sizeof(UINT32), &byteOffset));

            // Tell the camera to transfer the intended read data.
            CHECK(exec_command(camera, "FileOperationExecute"));

            // Check the success.
            char result[64] = {0};
            CHECK(GevGetFeatureValueAsString(camera->handle, "FileOperationStatus", &type, sizeof(result), result));
            if (strncasecmp(result, "Success", sizeof(result)) != STR_EQ) {
                GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Close");
                exec_command(camera, "FileOperationExecute");
                lastFailedFunc = "_download_file not success";
                return GEVLIB_ERROR_SOFTWARE;
            }
            // Get the number of bytes read.
            CHECK(GevGetFeatureValue(camera->handle, "FileOperationResult", &type, sizeof(bytesRead), &bytesRead));
            // Read the data into the buffer.
            CHECK(GevGetFeatureValue(camera->handle, "FileAccessBuffer", &type, bytesRead, &pBuf[byteOffset]));

            byteOffset += bytesRead;
        }
        return GEVLIB_OK;
    }

    int download_file(int camIndex, const char* fileName, void *data, int dataSize) {
        if (!data) {
            lastFailedFunc = "data == null";
            return GEVLIB_ERROR_NULL_PTR;
        }
        CameraData *camera = &cameras[camIndex];
        int status = _download_file(camera, fileName, data, dataSize);
        // Close the camera file to complete the read access;
        GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Close");
        exec_command(camera, "FileOperationExecute");
        return status;
    }

    int _get_file_size(CameraData *camera, const char* fileName, int* buffer_size) {
        int file_size = 0;
        int type;

        //========================================================
        // Open the camera file for read access;
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileSelector", fileName));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Open"));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileOpenMode", "Read"));

        CHECK(exec_command(camera, "FileOperationExecute"));

        // Get the file size from the camera.
        CHECK(GevGetFeatureValue(camera->handle, "FileSize", &type, sizeof(file_size), &file_size));

        int pad = 0;
        if ((file_size % 4) != 0) {
            pad = 4 - (file_size % 4);  // Multiple of 4 bytes required.
        }

        *buffer_size = file_size + pad;

        return GEVLIB_OK;
    }

    int get_file_size(int camIndex, const char* fileName, int* buffer_size) {
        CameraData *camera = &cameras[camIndex];
        int status = _get_file_size(camera, fileName, buffer_size);

        // Close the camera file to complete the read access;
        GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Close");
        exec_command(camera, "FileOperationExecute");
        return status;
    }

    int _upload_file(CameraData *camera, const char* fileName, void *data, int dataSize) {
        // Open the camera file for write access;
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileSelector", fileName));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Open"));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileOpenMode", "Write"));
        CHECK(GevSetFeatureValueAsString(camera->handle, "FileSelector", fileName));

        CHECK(exec_command(camera, "FileOperationExecute"));

        int maxBytes = _max_file_access_length(camera);
        if (!maxBytes) {
            lastFailedFunc = "maxBytes == 0";
            return GEVLIB_ERROR_NULL_PTR;
        }

        unsigned char *pBuf = (unsigned char *)data;

        // Write data to the camera (in a loop)
        int byteOffset = 0;
        while ( byteOffset < dataSize ) {
            int bytesWritten;
            int type;

            // Set up the write offset in the camera
            CHECK(GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Write"));

            int bytesToWrite = dataSize - byteOffset;
            if (bytesToWrite > maxBytes){
                bytesToWrite = maxBytes;
            }
            CHECK(GevSetFeatureValue(camera->handle, "FileAccessLength",  sizeof(UINT32), &bytesToWrite));
            CHECK(GevSetFeatureValue(camera->handle, "FileAccessOffset", sizeof(UINT32), &byteOffset));

            // Write the data into the camera.
            CHECK(GevSetFeatureValue(camera->handle, "FileAccessBuffer", bytesToWrite, &pBuf[byteOffset]));

            // Tell the camera to transfer the intended read data.
            CHECK(exec_command(camera, "FileOperationExecute"));

            // Check the success.
            char result[64] = {0};
            CHECK(GevGetFeatureValueAsString(camera->handle, "FileOperationStatus", &type, sizeof(result), result));
            if (strncasecmp(result, "Success", sizeof(result)) != STR_EQ) {
                GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Close");
                exec_command(camera, "FileOperationExecute");
                lastFailedFunc = "_upload_file not success";
                return GEVLIB_ERROR_SOFTWARE;
            }


            // Get the number of bytes written.
            CHECK(GevGetFeatureValue(camera->handle, "FileOperationResult", &type, sizeof(bytesWritten), &bytesWritten));

            byteOffset += bytesWritten;
        }
        return GEVLIB_OK;
    }

    int upload_file(int camIndex, const char* fileName, void *data, int dataSize) {
        if (!data) {
            lastFailedFunc = "data == null";
            return GEVLIB_ERROR_NULL_PTR;
        }
        if (dataSize <= 0) {
            lastFailedFunc = "dataSize <= 0";
            return GEVLIB_ERROR_NULL_PTR;
        }
        CameraData *camera = &cameras[camIndex];
        int status = _upload_file(camera, fileName, data, dataSize);

        // Close the camera file to complete the write access;
        GevSetFeatureValueAsString(camera->handle, "FileOperationSelector", "Close");
        exec_command(camera, "FileOperationExecute");
        return status;
    }
}
