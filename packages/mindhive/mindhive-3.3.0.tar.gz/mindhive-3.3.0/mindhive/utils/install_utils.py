import os
from urllib.parse import urlparse
from pathlib import Path
import requests
import tarfile
from zipfile import ZipFile


def download(file_url: str, dest: Path) -> Path:
    url = urlparse(file_url)
    filename = os.path.basename(url.path)
    dest.mkdir(parents=True, exist_ok=True)
    download_file = dest / filename

    if os.path.exists(download_file):
        os.unlink(download_file)

    print(f'Downloading {filename}')
    r = requests.get(file_url, allow_redirects=True)
    open(download_file, 'wb').write(r.content)
    return download_file


def extract_zip(zip_file: Path, dest_dir: Path):
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True)
    with ZipFile(zip_file, 'r') as zObject:
        zObject.extractall(path=dest_dir)


def extract_tar(tar_file: Path, dest_dir: Path, extract_flat=False):
    print(f'Extracting {tar_file}')
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True)
    with tarfile.open(tar_file, 'r') as tar:
        if extract_flat:
            for member in tar.getmembers():
                if member.isreg():
                    member.name = os.path.basename(member.name)
                    tar.extract(member, path=dest_dir)
        else:
            tar.extractall(dest_dir)