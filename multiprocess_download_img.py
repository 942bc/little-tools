import os
import urllib
import multiprocessing


def dload(urls):
    localDir = '/data/17'
    for line in urls:
        line = line.replace("\r\n", "")
        local = os.path.join(localDir, os.path.basename(line)) + ".jpg"
        r = urllib.urlopen(line)
        if r.code == 200:
            f = open(local, "wb")
            f.write(r.read())
            f.close()
        r.close()


if __name__ == "__main__":
    f = open("/data/17.csv", "rb")
    urls = f.readlines()
    size = len(urls) / 8
    for i in range(8):
        list = []
        if i < 7:
            list = urls[i*size:(i+1) * size]
        else:
            list = urls[i*size:]
        p = multiprocessing.Process(target=dload, args=(list,))
        p.start()
