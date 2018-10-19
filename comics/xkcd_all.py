# XKCD Comic Downloader

from bs4 import BeautifulSoup
import requests

xkcd_folder = ""

def download_file(url, location, filename=""):
    local_filename = url.split('/')[-1] if filename == "" else filename
    
    r = requests.get(url, stream=True)
    with open(location + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

    return local_filename

print("Beginning XKCD comic download...")

if xkcd_folder != "":
    xkcd_page = BeautifulSoup(requests.get("https://xkcd.com").text, "html.parser")
    img_num = xkcd_page.select("div#middleContainer")[0].text.split("\n")[20].split(" ")[-1].replace("https://xkcd.com/", "").replace("/", "")

    for xkcd_imgnum in range(1, int(img_num)+1):
        xkcd_imgnum = str(xkcd_imgnum)

        xkcd_page = BeautifulSoup(requests.get("https://xkcd.com/{}/".format(xkcd_imgnum)).text, "html.parser")
        xkcd_imgsrc = xkcd_page.select("div#middleContainer > div#comic > img")[0]["src"].replace("//", "https://")
        xkcd_imgnum = xkcd_page.select("div#middleContainer")[0].text.split("\n")[20].split(" ")[-1].replace("https://xkcd.com/", "").replace("/", "")
        xkcd_imgext = xkcd_imgsrc.split(".")[-1]

        print("[{}] Downloading XKCD...".format(xkcd_imgnum, img_num))

        download_file(xkcd_imgsrc, xkcd_folder, filename="{}.{}".format(xkcd_imgnum, xkcd_imgext))

        print("[{}] Download completed!".format(xkcd_imgnum))

    print("XKCD comic download complete!")
else:
    print("You must set the \"xkcd_folder\" variable first!")
