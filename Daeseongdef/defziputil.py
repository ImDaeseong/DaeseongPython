import os
import zipfile


def Zipfile(path, zippath):
    zipf = zipfile.ZipFile(zippath, 'w')
    for dirname, subFolders, files in os.walk(path):
        zipf.write(dirname)
        for filename in files:
            zipf.write(os.path.join(dirname, filename))
    zipf.close()


def UnZipfile(path, unzippath):
    zipf = zipfile.ZipFile(path, 'r')
    zipf.extractall(unzippath)


if __name__ == '__main__':
    Zipfile('E:\\a', 'C:\\a.zip')
    UnZipfile('C:\\a.zip', 'C:\\')
    pass
