import win32api


class clswinapiutil:
    def __init__(self):
        pass

    def ShellExecute_url(self, url):
        win32api.ShellExecute(0, 'open', url, '', '', 1)

    def ShellExecute_path(self, path):
        win32api.ShellExecute(0, 'open', path, '', '', 1)


if __name__ == '__main__':
    clsobj = clswinapiutil()
    clsobj.ShellExecute_url('https://www.naver.com')
    clsobj.ShellExecute_path('C:\\Windows\\System32\\notepad.exe')
    pass
