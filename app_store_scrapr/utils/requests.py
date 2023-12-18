import urllib.error
import urllib.request


def get(url: str, timeout: int = 10) -> str:
    request = urllib.request.Request(url)

    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("UTF-8")
