# XKCD Daily Comic Downloader

from bs4 import BeautifulSoup
import requests
import re

def download_file(url, location, filename=""):
    local_filename = url.split('/')[-1] if filename == "" else filename
    
    r = requests.get(url, stream=True)
    with open(location + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

    return local_filename

xkcd_page = BeautifulSoup(requests.get("https://xkcd.com").text, "html.parser")
img_src = xkcd_page.select("div#middleContainer > div#comic > img")[0]["src"].replace("//", "https://")
img_num = xkcd_page.select("div#middleContainer")[0].text.split("\n")[20].split(" ")[-1].replace("https://xkcd.com/", "").replace("/", "")
img_ext = img_src.split(".")[-1]

print("Downloading XKCD {}...".format(img_num))

download_file(img_src, "/Users/hkamran/Desktop/Desktop/Images/comics/XKCD/", filename="{}.{}".format(img_num, img_ext))

print("Download completed!")
