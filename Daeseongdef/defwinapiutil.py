import win32api


def ShellExecute_url(url):
    win32api.ShellExecute(0, 'open', url, '', '', 1)


def ShellExecute_path(path):
    win32api.ShellExecute(0, 'open', path, '', '', 1)


if __name__ == '__main__':
    ShellExecute_url('https://www.naver.com')
    ShellExecute_path('C:\\Windows\\System32\\notepad.exe')
    pass
