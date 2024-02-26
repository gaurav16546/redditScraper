import requests
from os import path

home_directory = path.expanduser("~")


def downloadFile(url: str):
    name = url.split("/")[-1]
    print(f"Started downloading {name}")
    response = requests.get(url)
    open(f"./images/{name}", "wb").write(response.content)
    print(f"Finished downloading {name}")
