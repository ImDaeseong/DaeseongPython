import requests
from requests import get


class clsdownloadutil:
    def __init__(self):
        pass

    def Get_WebPage(self, Url):
        response = requests.get(Url)
        # print(response.status_code)
        # print(response.text)
        # print(type(response))
        # print(type(response.text))
        # print(response.cookies)
        # print(response.content)
        if response.status_code == 200:
            return response.text
        else:
            return ""

    def FileUrl(self, Url):
        if Url.rfind('/') != -1:
            return Url[Url.rfind('/') + 1:]
        else:
            return Url

    def Get_DownloadFile(self, Url):
        path = 'c:\\' + self.FileUrl(Url)
        # print(path)
        with open(path, "wb") as file:
            response = get(Url)
            file.write(response.content)


if __name__ == '__main__':
    obj = clsdownloadutil()
    req = obj.Get_WebPage('https://github.com/ImDaeseong')
    # print(req)
    obj.Get_DownloadFile('http://content.screencast.com/users/JamesMontemagno/folders/Jing/media/23c1dd13-333a-459e-9e23-c3784e7cb434/2016-06-02_1049.png')
    pass
