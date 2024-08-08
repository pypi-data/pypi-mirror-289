import os
import pwd
import shutil
import subprocess
from setuptools import Extension, setup
from pathlib import Path
from ...utils.install_utils import download, extract_zip


DALSA_ZIP = "https://mindhive-public.s3.amazonaws.com/dalsa/DALSA.zip"

CURR_DIR = Path(__file__).parent
INSTALL_DIR = Path('/opt/GigeV')


def _install_files():
    bin_dir = INSTALL_DIR / 'DALSA/GigeV/bin'
    installer = bin_dir / 'install.gigev'
    os.chdir(bin_dir)
    os.chmod(installer, 755)
    print('Installing Dalsa...')
    print(subprocess.run([installer], capture_output=True, env={'TDY_INSTALL_MODE': 'Silent'}))


def _build():
    os.chdir(CURR_DIR)
    dalsa_cpp = CURR_DIR / 'cpp/dalsa.cpp'

    setup(
        ext_modules=[
            Extension(
                "dalsa",
                sources=[str(dalsa_cpp)],
                include_dirs=[
                    "/usr/local/include/GigeV/include",
                    "/opt/genicam_v3_0/library/CPP/include",
                ],
                libraries=["GevApi"],
                extra_compile_args=["-Wno-unknown-pragmas"],
                extra_link_args=["-o", "./dalsa.so"]
            ),
        ],
    )
    shutil.move("./dalsa.so", f"{INSTALL_DIR}/dalsa.so")

    # cleanup
    shutil.rmtree(CURR_DIR / 'build')


def _download():
    tmp_dir = Path("/tmp/")
    zip_file = download(DALSA_ZIP, tmp_dir)
    extract_zip(zip_file, INSTALL_DIR)


def main():
    if not pwd.getpwuid(os.getuid())[0] == 'root':
        raise RuntimeError("MVS SDK installer must be run as root")
    _download()
    _install_files()
    _build()


if __name__ == "__main__":
    print('Running Dalsa installer....')
    main()
