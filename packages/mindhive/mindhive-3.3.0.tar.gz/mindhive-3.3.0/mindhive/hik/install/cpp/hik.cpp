#include "MvCameraControl.h"
#include <string.h>
#include <sys/time.h>
#include <chrono>
#include <thread>

#define CHECK(call) { int _status = call; if (_status) { lastFailedFunc = #call; return _status; } }
#define STR_EQ 0
#define MAX_CAM_COUNT 32

extern "C" {
    thread_local const char* lastFailedFunc = "<none>";

    void* handles[MAX_CAM_COUNT] = {0};
    MV_CC_DEVICE_INFO_LIST deviceInfoList = {0};

    struct CameraInfo {
        unsigned int index;
        unsigned int ipAddr;
        unsigned char* serial;
        unsigned int interfaceIp;
    };

    int get_max_cameras() {
        return MAX_CAM_COUNT;
    }

    const char* get_last_failed_func() {
        return lastFailedFunc;
    }

    void* get_handle(int camIndex) {
        if (!handles[camIndex]) {
            int _status = MV_CC_CreateHandle(&handles[camIndex], deviceInfoList.pDeviceInfo[camIndex]);
            if (_status)
                return nullptr;
        }
        return handles[camIndex];
    }

    int get_cameras(CameraInfo pyCameras[], unsigned int maxCameras, unsigned int *numCameras) {
        if (maxCameras > MAX_CAM_COUNT) {
            lastFailedFunc = "maxCameras > MAX_CAM_COUNT";
            return MV_E_NOENOUGH_BUF;
        }
        CHECK(MV_CC_EnumDevices(MV_GIGE_DEVICE, &deviceInfoList));
        if (deviceInfoList.nDeviceNum > maxCameras) {
            return MV_E_NOENOUGH_BUF;
        }
        for ( unsigned int i = 0; i < deviceInfoList.nDeviceNum; i++ ) {
            auto gigeInfo = &deviceInfoList.pDeviceInfo[i]->SpecialInfo.stGigEInfo;
            pyCameras[i] = {i, gigeInfo->nCurrentIp, gigeInfo->chSerialNumber, gigeInfo->nNetExport};
        }
        *numCameras = deviceInfoList.nDeviceNum;
        return MV_OK;
    }

    int get_float_feature(int camIndex, const char* feature, float* value) {
        void* handle = handles[camIndex];
        MVCC_FLOATVALUE floatValue;
        CHECK(MV_CC_GetFloatValue(handle, feature, &floatValue));
        *value = floatValue.fCurValue;
        return MV_OK;
    }

    int get_int_feature(int camIndex, const char* feature, int64_t* value) {
        void* handle = handles[camIndex];
        MVCC_INTVALUE_EX intValue;
        CHECK(MV_CC_GetIntValueEx(handle, feature, &intValue));
        *value = intValue.nCurValue;
        return MV_OK;
    }

    int get_string_feature(int camIndex, const char* feature, char* value, size_t string_size) {
        void* handle = handles[camIndex];
        MVCC_STRINGVALUE strValue;
        CHECK(MV_CC_GetStringValue(handle, feature, &strValue));
        if (strlen(strValue.chCurValue) >= string_size) {
            return MV_E_NOENOUGH_BUF;
        }
        strncpy(value, strValue.chCurValue, string_size);
        return MV_OK;
    }

    int download_all_features(int camIndex, const char* localFilename) {
        void* handle = handles[camIndex];
        CHECK(MV_CC_FeatureSave(handle, localFilename));
        return MV_OK;
    }

    int open_camera(int camIndex) {
        void* handle = get_handle(camIndex);
        CHECK(MV_CC_OpenDevice(handle));
        return MV_OK;
    }

    int config_encoder(
        int camIndex,
        int line = 0,
        int multiplier = 32
    ) {
        void* handle = handles[camIndex];
        // CHECK(MV_CC_SetEnumValueByString(handle, "InputSource", line));
        CHECK(MV_CC_SetEnumValue(handle, "InputSource", line));
        CHECK(MV_CC_SetIntValueEx(handle, "Multiplier", multiplier));
        return MV_OK;
    }

    int config_exposure(
        int camIndex,
        float exposureMicros,
        int preampGain
    ) {
        void* handle = handles[camIndex];
        CHECK(MV_CC_SetFloatValue(handle, "ExposureTime", exposureMicros));
        CHECK(MV_CC_SetEnumValue(handle, "PreampGain", preampGain));
        return MV_OK;
    }

    int _config_network(void* handle, int packetSize) {
        CHECK(MV_CC_SetIntValue(handle,"GevSCPSPacketSize", packetSize));
        CHECK(MV_CC_SetBoolValue(handle, "FrameTimeoutEnable", true));
        CHECK(MV_CC_SetBoolValue(handle, "GevIEEE1588", true));
        CHECK(MV_CC_SetImageNodeNum(handle, 10));
        return MV_OK;
    }

    int config_mono_camera(
        int camIndex,
        int height,
        float rateHz,
        float exposureMicros,
        int preampGain,
        bool reverseX,
        int format,
        bool binning,
        const char* calibrationSet,
        int packetSize
    ) {
        void* handle = handles[camIndex];

        CHECK(MV_CC_SetEnumValue(handle, "PixelFormat", format));

        CHECK(MV_CC_SetBoolValue(handle, "AcquisitionLineRateEnable", true));
        CHECK(MV_CC_SetIntValueEx(handle, "AcquisitionLineRate", rateHz));
        CHECK(MV_CC_SetFloatValue(handle, "ExposureTime", exposureMicros));
        CHECK(MV_CC_SetEnumValue(handle, "BinningHorizontal", binning ? 2 : 1));
        CHECK(MV_CC_SetIntValueEx(handle, "Height", height));

        CHECK(MV_CC_SetEnumValue(handle, "PreampGain", preampGain));

        if (calibrationSet) {
            CHECK(MV_CC_SetEnumValueByString(handle, "PRNUCUserSelector", calibrationSet));
            CHECK(MV_CC_SetBoolValue(handle, "PRNUCUserEnable", true));
        } else {
            CHECK(MV_CC_SetBoolValue(handle, "PRNUCUserEnable", false));
        }
        // Non functional - but doesn't throw an error if we change it
        CHECK(MV_CC_SetBoolValue(handle, "ReverseX", reverseX));

        return _config_network(handle, packetSize);

    }

    int config_color_camera(
        int camIndex,
        int height,
        float rateHz,
        float exposureMicros,
        int preampGain,
        bool reverseX,
        bool reverseScanDirection,
        int format,
        bool binning,
        const char* calibrationSet,
        int redBalanceRatio,
        int greenBalanceRatio,
        int blueBalanceRatio,
        int packetSize
    ) {
        void* handle = handles[camIndex];

        CHECK(MV_CC_SetEnumValue(handle, "PixelFormat", format));
        CHECK(MV_CC_SetEnumValueByString(handle, "BalanceWhiteAuto", "Off"));
        // Set white balance values to match the original cameras, one (L00309833) had different values
        CHECK(MV_CC_SetEnumValueByString(handle, "BalanceRatioSelector", "Red"));
        CHECK(MV_CC_SetIntValueEx(handle, "BalanceRatio", redBalanceRatio));
        CHECK(MV_CC_SetEnumValueByString(handle, "BalanceRatioSelector", "Green"));
        CHECK(MV_CC_SetIntValueEx(handle, "BalanceRatio", greenBalanceRatio));
        CHECK(MV_CC_SetEnumValueByString(handle, "BalanceRatioSelector", "Blue"));
        CHECK(MV_CC_SetIntValueEx(handle, "BalanceRatio", blueBalanceRatio));
        CHECK(MV_CC_SetBoolValue(handle, "CCMEnable", false));
        CHECK(MV_CC_SetBoolValue(handle, "ColorTransformationEnable", false));
        CHECK(MV_CC_SetBoolValue(handle, "AcquisitionLineRateEnable", true));
        CHECK(MV_CC_SetIntValueEx(handle, "AcquisitionLineRate", rateHz));
        CHECK(MV_CC_SetFloatValue(handle, "ExposureTime", exposureMicros));
        CHECK(MV_CC_SetEnumValue(handle, "BinningHorizontal", binning ? 2 : 1));
        // REVISIT: when not binning and reversed, should this be different
        CHECK(MV_CC_SetFloatValue(handle, "LineRateRatio", binning ? 0.5 : 1));
        CHECK(MV_CC_SetIntValueEx(handle, "Height", height));

        CHECK(MV_CC_SetEnumValue(handle, "PreampGain", preampGain));

        if (calibrationSet) {
            CHECK(MV_CC_SetEnumValueByString(handle, "PRNUCUserSelector", calibrationSet));
            CHECK(MV_CC_SetBoolValue(handle, "PRNUCUserEnable", true));
        } else {
            CHECK(MV_CC_SetBoolValue(handle, "PRNUCUserEnable", false));
        }

        CHECK(MV_CC_SetBoolValue(handle, "ReverseX", reverseX));
        CHECK(MV_CC_SetBoolValue(handle, "ReverseScanDirection", reverseScanDirection));

        return _config_network(handle, packetSize);
    }

    int config_dual_line_trigger(int camIndex, int input) {
        void* handle = handles[camIndex];

        CHECK(MV_CC_SetEnumValueByString(handle, "TriggerSelector", "FrameBurstStart"));
        CHECK(MV_CC_SetEnumValueByString(handle, "TriggerMode", "On"));
        CHECK(MV_CC_SetEnumValue(handle, "TriggerSource", input));
        CHECK(MV_CC_SetEnumValueByString(handle, "TriggerActivation", "RisingEdge"));
        CHECK(MV_CC_SetIntValueEx(handle, "AcquisitionBurstFrameCount", 1));
        CHECK(MV_CC_SetEnumValueByString(handle, "TriggerSelector", "LineStart"));
        CHECK(MV_CC_SetEnumValueByString(handle, "TriggerMode", "On"));
        CHECK(MV_CC_SetEnumValue(handle, "TriggerSource", input));
        CHECK(MV_CC_SetEnumValueByString(handle, "TriggerActivation", "AnyEdge"));

        return MV_OK;
    }

    int calibrate(int camIndex, int whiteTarget, int redTarget, int greenTarget, int blueTarget) {
        int status;
        void* handle = handles[camIndex];
        CHECK(MV_CC_SetBoolValue(handle, "PRNUCUserEnable", false));
        CHECK(MV_CC_SetBoolValue(handle, "PRNUCTargetEnable", true));
        status = MV_CC_SetIntValue(handle,"PRNUCTarget", whiteTarget);
        if (status && status != MV_E_GC_ACCESS) {
            lastFailedFunc = "MV_CC_SetIntValue(handle,\"PRNUCTarget\", whiteTarget)";
            return status;
        }
        status = MV_CC_SetIntValue(handle,"PRNUCTargetR", redTarget);
        if (status && status != MV_E_GC_ACCESS) {
            lastFailedFunc = "MV_CC_SetIntValue(handle,\"PRNUCTargetR\", redTarget)";
            return status;
        }
        status = MV_CC_SetIntValue(handle,"PRNUCTargetG", greenTarget);
        if (status && status != MV_E_GC_ACCESS) {
            lastFailedFunc = "MV_CC_SetIntValue(handle,\"PRNUCTargetG\", greenTarget)";
            return status;
        }
        status = MV_CC_SetIntValue(handle,"PRNUCTargetB", blueTarget);
        if (status && status != MV_E_GC_ACCESS) {
            lastFailedFunc = "MV_CC_SetIntValue(handle,\"PRNUCTargetB\", blueTarget)";
            return status;
        }
        CHECK(MV_CC_SetCommandValue(handle, "ActivateShading"));
        return MV_OK;
    }

    int set_calibration_enable(int camIndex, bool enable) {
        void* handle = handles[camIndex];
        CHECK(MV_CC_SetBoolValue(handle, "PRNUCUserEnable", enable));
        return MV_OK;
    }

    int64_t _current_epoch_microseconds() {
        struct timeval tv;
        gettimeofday(&tv, nullptr);
        return static_cast<int64_t>(tv.tv_sec) * 1000 * 1000 + tv.tv_usec;
    }

    int start_acquisition(int camIndex, int64_t start_epoch_microseconds) {
        while (_current_epoch_microseconds() < start_epoch_microseconds);
        CHECK(MV_CC_StartGrabbing(handles[camIndex]));
        return MV_OK;
    }

    int wait_for_image(int camIndex, MV_FRAME_OUT *result, unsigned int timeoutMillis) {
        CHECK(MV_CC_GetImageBuffer(handles[camIndex], result, timeoutMillis));
        return MV_OK;
    }

    int release_image(int camIndex, MV_FRAME_OUT *result) {
        if (result && result->pBufAddr) {
            CHECK(MV_CC_FreeImageBuffer(handles[camIndex], result));
        }
        return MV_OK;
    }

    void stop_acquisition(int camIndex) {
        void* handle = handles[camIndex];
        if (handle == NULL) {
            return;
        }
        MV_CC_StopGrabbing(handle);
    }

    int get_net_metrics(int camIndex, MV_MATCH_INFO_NET_DETECT* pMatchInfoNetDetect) {
        if (!pMatchInfoNetDetect) {
            lastFailedFunc = "get_net_metrics(pMatchInfoNetDetect)";
            return MV_E_PARAMETER;
        }
        void* handle = handles[camIndex];
        MV_ALL_MATCH_INFO allMatchInfo = {0};
        allMatchInfo.nType = MV_MATCH_TYPE_NET_DETECT;
        allMatchInfo.pInfo = pMatchInfoNetDetect;
        allMatchInfo.nInfoSize = sizeof(MV_MATCH_INFO_NET_DETECT);
        memset(allMatchInfo.pInfo, 0, sizeof(MV_MATCH_INFO_NET_DETECT));
        CHECK(MV_CC_GetAllMatchInfo(handle, &allMatchInfo));
        return MV_OK;
    }

    int download_file(int camIndex, const char *devFilename, const char *localFilename) {
        void* handle = handles[camIndex];
        MV_CC_FILE_ACCESS fileAccess = {0};
        fileAccess.pUserFileName = localFilename;
        fileAccess.pDevFileName = devFilename;
        CHECK(MV_CC_FileAccessRead(handle, &fileAccess));
        return MV_OK;
    }

    int upload_file(int camIndex, const char *devFilename, const char *localFilename) {
        void* handle = handles[camIndex];
        MV_CC_FILE_ACCESS fileAccess = {0};
        fileAccess.pUserFileName = localFilename;
        fileAccess.pDevFileName = devFilename;
        CHECK(MV_CC_FileAccessWrite(handle, &fileAccess));
        return MV_OK;
    }

    int set_dhcp_mode(int camIndex) {
        void* handle = get_handle(camIndex);
        CHECK(MV_GIGE_SetIpConfig(handle, MV_IP_CFG_DHCP));
        return MV_OK;
    }

    int set_linklocal_addr(int camIndex) {
        void* handle = get_handle(camIndex);
        CHECK(MV_GIGE_SetIpConfig(handle, MV_IP_CFG_LLA));
        return MV_OK;
    }

    int set_static_ip_addr(int camIndex, unsigned int ipAddr, unsigned int netWorkMask, unsigned int gateway) {
        void* handle = get_handle(camIndex);
        CHECK(MV_GIGE_ForceIpEx(handle, ipAddr, netWorkMask, gateway));
        CHECK(MV_CC_DestroyHandle(handle));
        handle = NULL;

        deviceInfoList.pDeviceInfo[camIndex]->SpecialInfo.stGigEInfo.nCurrentIp = ipAddr;
        deviceInfoList.pDeviceInfo[camIndex]->SpecialInfo.stGigEInfo.nCurrentSubNetMask = netWorkMask;
        deviceInfoList.pDeviceInfo[camIndex]->SpecialInfo.stGigEInfo.nDefultGateWay = gateway;

        CHECK(MV_CC_CreateHandle(&handle, deviceInfoList.pDeviceInfo[camIndex]));
        CHECK(MV_GIGE_SetIpConfig(handle, MV_IP_CFG_STATIC))
        return MV_OK;
    }

    int reset_camera(int camIndex) {
        void* handle = handles[camIndex];
        MV_CC_StopGrabbing(handle);
        CHECK(MV_CC_SetCommandValue(handle, "DeviceReset"));
        return MV_OK;
    }

    void close_camera(int camIndex) {
        void* handle = handles[camIndex];
        if (!handle) {
            return;
        }
        MV_CC_StopGrabbing(handle);
        MV_CC_CloseDevice(handle);
        MV_CC_DestroyHandle(handle);
        handles[camIndex] = nullptr;
    }

    void teardown() {
        for (int i = 0; i < MAX_CAM_COUNT; i++) {
            close_camera(i);
        }
    }
}
