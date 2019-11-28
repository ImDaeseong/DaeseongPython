import winreg


def SetregistryString(regKey, key, Val):
    try:
        hkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(hkey, key, 0, winreg.REG_SZ, Val)
        hkey.Close()
    except WindowsError:
        print('error SetregistryString')


def GetregistryString(regKey, key):
    hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
    Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
    hkey.Close()
    return Val


def SetregistryDWord(regKey, key, Val):
    try:
        hkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(hkey, key, 0, winreg.REG_DWORD, Val)
        hkey.Close()
    except WindowsError:
        print('error SetregistryDWord')


def GetregistryDWord(regKey, key):
    hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
    Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
    hkey.Close()
    return Val


def DeleteKeyregistry(regKey):
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, regKey)
    except WindowsError:
        print('error DeleteKeyregistry')


def DeleteValueregistry(regKey, key):
    try:
        hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(hkey, key)
        hkey.Close()
    except WindowsError:
        print('error DeleteValueregistry')


def SetregistryStringWOW64(regKey, key, Val):
    try:
        hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(hkey, key, 0, winreg.REG_SZ, Val)
        hkey.Close()
    except WindowsError:
        print('error SetregistryStringWOW64')


def GetregistryStringWOW64(regKey, key):
    hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
    Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
    hkey.Close()
    return Val


def SetregistryDWordWOW64(regKey, key, Val):
    try:
        hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(hkey, key, 0, winreg.REG_DWORD, Val)
        hkey.Close()
    except WindowsError:
        print('error SetregistryDWordWOW64')


def GetregistryDWordWOW64(regKey, key):
    hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
    Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
    hkey.Close()
    return Val


def DeleteValueregistryWOW64(regKey, key):
    try:
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(hkey, key)
        hkey.Close()
    except WindowsError:
        print('error DeleteValueregistryWOW64')


def SetregistryString32(regKey, key, Val):
    try:
        hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(hkey, key, 0, winreg.REG_SZ, Val)
        hkey.Close()
    except WindowsError:
        print('error SetregistryString32')


def GetregistryString32(regKey, key):
    hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
    Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
    hkey.Close()
    return Val


def SetregistryDWord32(regKey, key, Val):
    try:
        hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(hkey, key, 0, winreg.REG_DWORD, Val)
        hkey.Close()
    except WindowsError:
        print('error SetregistryDWord32')


def GetregistryDWord32(regKey, key):
    hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
    Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
    hkey.Close()
    return Val


def DeleteKeyregistry32(regKey):
    try:
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, regKey)
    except WindowsError:
        print('error DeleteKeyregistry32')


def DeleteValueregistry32(regKey, key):
    try:
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(hkey, key)
        hkey.Close()
    except WindowsError:
        print('error DeleteValueregistry32')


if __name__ == '__main__':

    """
    SetregistryString32("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = GetregistryString32("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    SetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = GetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """


    """
    DeleteValueregistry32("Software\\Daeseong\\Daeseong", "Gamekey1")

    DeleteKeyregistry32("Software\\Daeseong\\Daeseong")
    DeleteKeyregistry32("Software\\Daeseong")
    """



    """
    SetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = GetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    SetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = GetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    # DeleteValueregistryWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")

    """
    SetregistryString("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = GetregistryString("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    SetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = GetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    DeleteValueregistry("Software\\Daeseong\\Daeseong", "Gamekey1")

    DeleteKeyregistry("Software\\Daeseong\\Daeseong")
    DeleteKeyregistry("Software\\Daeseong")
    """
    pass
