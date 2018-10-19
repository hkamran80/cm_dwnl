# Joy of Tech Comic Downloader

from bs4 import BeautifulSoup
import handycode
import requests

joyoftech_folder = ""

def download_file(url, location, filename=""):
    local_filename = url.split('/')[-1] if filename == "" else filename
    
    r = requests.get(url, stream=True)
    with open(location + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

    return local_filename

if joyoftech_folder != "":
	max_jot_range = int(BeautifulSoup(requests.get("http://joyoftech.com/joyoftech/").text, "html.parser").find_all("img")[1]["src"].split("/")[1:][0].split(".")[:1][0])
	jot_1_range = ["00" + str(r) for r in range(1, 10)]
	jot_2_range = ["0" + str(r) for r in range(10, 100)]
	jot_3_range = [str(r) for r in range(100, max_jot_range+1)]

	jot_range = []
	for r in jot_1_range:
		jot_range.append(r)
	for r in jot_2_range:
		jot_range.append(r)
	for r in jot_3_range:
		jot_range.append(r)

	img_formats = ["png", "jpg", "gif"]

	# ii = Image Index
	for ii in jot_range:
		for i in img_formats:
			link = "http://joyoftech.com/joyoftech/joyimages/{}.{}".format(ii, i)

			print("Trying .{} format".format(i.upper()))

			r = requests.get(link)
			if r.url == link and r.status_code == 200:
				print(link)
				
				download_file(link, joyoftech_folder, filename="{}.{}".format(ii, i))
				break
			else:
				continue
else:
    print("You must set the \"joyoftech_folder\" variable first!")
