import os
import pwd
from pathlib import Path
import subprocess
import shutil
from setuptools import Extension, setup
import platform
from ...utils.install_utils import download, extract_tar

# MVS SDK v4.1.2
ARM64_MVS_SDK = "https://mindhive-public.s3.amazonaws.com/mvs/arm64/MvCamCtrlSDK_Runtime-4.1.2_aarch64_20231011.tar.gz"
X86_MVS_SDK = "https://mindhive-public.s3.amazonaws.com/mvs/amd64/MvCamCtrlSDK_Runtime-4.1.2_x86_64_20231011.tar.gz"
 
ARCH = platform.machine()

if ARCH == 'arm64':
    ARCH = 'aarch64'

if ARCH == 'aarch64':
    MVS_SDK_URL = ARM64_MVS_SDK
elif ARCH == 'x86_64':
    MVS_SDK_URL = X86_MVS_SDK
else:
    raise RuntimeError(f'MVS SDK: Unsupported architecture {ARCH}')


CURR_DIR = Path(__file__).parent
INSTALL_DIR = Path('/opt/MVS')


def _install_files():
    shutil.copytree(CURR_DIR / 'include', INSTALL_DIR / 'include', dirs_exist_ok=True)


def _build():
    os.chdir(CURR_DIR)
    hik_cpp = CURR_DIR / 'cpp/hik.cpp'
    include_dir = INSTALL_DIR / 'include'
    lib_dir = INSTALL_DIR / 'lib/64'
    if ARCH == 'aarch64':
        lib_dir = INSTALL_DIR / 'lib/aarch64'

    setup(
        ext_modules=[
            Extension(
                "hik",
                sources=[str(hik_cpp)],
                include_dirs=[str(include_dir)],
                library_dirs=[str(lib_dir)],
                libraries=["MvCameraControl"],
                extra_compile_args=["-Wno-unknown-pragmas"],
                extra_link_args=["-o", "./hik.so"]
            ),
        ],
    )
    shutil.move("./hik.so", f"{INSTALL_DIR}/lib/hik.so")
    # cleanup
    shutil.rmtree(CURR_DIR / 'build')



def _download():
    tmp_dir = Path("/tmp/MVS")

    tar_file = download(MVS_SDK_URL, tmp_dir)

    extract_tar(tar_file, tmp_dir, True)

    # delete old MVS
    if os.path.exists(INSTALL_DIR):
        shutil.rmtree(INSTALL_DIR)

    Path(INSTALL_DIR).mkdir(parents=True)

    # run MVS setup
    os.chdir(tmp_dir)
    print('Installing MVS...')
    print(subprocess.run([f"./setup.sh"], capture_output=True))

    # cleanup
    shutil.rmtree(tmp_dir)


def main():
    if not pwd.getpwuid(os.getuid())[0] == 'root':
        raise RuntimeError("MVS SDK installer must be run as root")
    
    _download()
    _install_files()
    _build()


if __name__ == "__main__":
    print('Running MVS installer....')
    main()

