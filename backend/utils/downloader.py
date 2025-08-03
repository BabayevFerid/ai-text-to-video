import requests

def download_file(url: str, path: str) -> str:
    """
    URL-dən faylı yükləyir və qeyd edilən yola saxlayır.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to download file from {url}")
    with open(path, "wb") as f:
        f.write(response.content)
    return path
