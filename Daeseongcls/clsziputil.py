import os
import zipfile


class clsziputil:
    def __init__(self):
        pass

    def Zipfile(self, path, zippath):
        zipf = zipfile.ZipFile(zippath, 'w')
        for dirname, subFolders, files in os.walk(path):
            zipf.write(dirname)
            for filename in files:
                zipf.write(os.path.join(dirname, filename))
        zipf.close()

    def UnZipfile(self, path, unzippath):
        zipf = zipfile.ZipFile(path, 'r')
        zipf.extractall(unzippath)


if __name__ == '__main__':
    clsobj = clsziputil()
    clsobj.Zipfile('E:\\a', 'C:\\a.zip')
    clsobj.UnZipfile('C:\\a.zip', 'C:\\')
    pass
