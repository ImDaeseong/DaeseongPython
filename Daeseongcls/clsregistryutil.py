import winreg


class clsregistryutil(object):
    def __init__(self):
        pass

    def SetregistryString(self, regKey, key, Val):
        try:
            hkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(hkey, key, 0, winreg.REG_SZ, Val)
            hkey.Close()
        except WindowsError:
            print('error SetregistryString')

    def GetregistryString(self, regKey, key):
        hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
        Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
        hkey.Close()
        return Val

    def SetregistryDWord(self, regKey, key, Val):
        try:
            hkey = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(hkey, key, 0, winreg.REG_DWORD, Val)
            hkey.Close()
        except WindowsError:
            print('error SetregistryDWord')

    def GetregistryDWord(self, regKey, key):
        hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
        Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
        hkey.Close()
        return Val

    def DeleteKeyregistry(self, regKey):
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, regKey)
        except WindowsError:
            print('error DeleteKeyregistry')

    def DeleteValueregistry(self, regKey, key):
        try:
            hkey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, regKey, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(hkey, key)
            hkey.Close()
        except WindowsError:
            print('error DeleteValueregistry')

    def SetregistryStringWOW64(self, regKey, key, Val):
        try:
            hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0,
                                      winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(hkey, key, 0, winreg.REG_SZ, Val)
            hkey.Close()
        except WindowsError:
            print('error SetregistryStringWOW64')

    def GetregistryStringWOW64(self, regKey, key):
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
        Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
        hkey.Close()
        return Val

    def SetregistryDWordWOW64(self, regKey, key, Val):
        try:
            hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0,
                                      winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(hkey, key, 0, winreg.REG_DWORD, Val)
            hkey.Close()
        except WindowsError:
            print('error SetregistryDWordWOW64')

    def GetregistryDWordWOW64(self, regKey, key):
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
        Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
        hkey.Close()
        return Val

    def DeleteValueregistryWOW64(self, regKey, key):
        try:
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_WOW64_64KEY | winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(hkey, key)
            hkey.Close()
        except WindowsError:
            print('error DeleteValueregistryWOW64')

    def SetregistryString32(self, regKey, key, Val):
        try:
            hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(hkey, key, 0, winreg.REG_SZ, Val)
            hkey.Close()
        except WindowsError:
            print('error SetregistryString32')

    def GetregistryString32(self, regKey, key):
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
        Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
        hkey.Close()
        return Val

    def SetregistryDWord32(self, regKey, key, Val):
        try:
            hkey = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(hkey, key, 0, winreg.REG_DWORD, Val)
            hkey.Close()
        except WindowsError:
            print('error SetregistryDWord32')

    def GetregistryDWord32(self, regKey, key):
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
        Val = winreg.QueryValueEx(hkey, key)[0]  # Val = winreg.QueryValueEx(hkey, key)
        hkey.Close()
        return Val

    def DeleteKeyregistry32(self, regKey):
        try:
            winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, regKey)
        except WindowsError:
            print('error DeleteKeyregistry32')

    def DeleteValueregistry32(self, regKey, key):
        try:
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, regKey, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(hkey, key)
            hkey.Close()
        except WindowsError:
            print('error DeleteValueregistry32')


if __name__ == '__main__':
    clsobj = clsregistryutil()

    """
    clsobj.SetregistryString32("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = clsobj.GetregistryString32("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    clsobj.SetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = clsobj.GetregistryDWord32("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    clsobj.DeleteValueregistry32("Software\\Daeseong\\Daeseong", "Gamekey1")

    clsobj.DeleteKeyregistry32("Software\\Daeseong\\Daeseong")
    clsobj.DeleteKeyregistry32("Software\\Daeseong")
    """

    """
    clsobj.SetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = clsobj.GetregistryStringWOW64("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    clsobj.SetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = clsobj.GetregistryDWordWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    # clsobj.DeleteValueregistryWOW64("Software\\Daeseong\\Daeseong", "Gamekey1")

    """
    clsobj.SetregistryString("Software\\Daeseong\\Daeseong", "GameList", "3")
    counter = clsobj.GetregistryString("Software\\Daeseong\\Daeseong", "GameList")
    print(counter)

    clsobj.SetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1", 1)
    counter = clsobj.GetregistryDWord("Software\\Daeseong\\Daeseong", "Gamekey1")
    print(counter)
    """

    """
    clsobj.DeleteValueregistry("Software\\Daeseong\\Daeseong", "Gamekey1")
    clsobj.DeleteKeyregistry("Software\\Daeseong\\Daeseong")
    clsobj.DeleteKeyregistry("Software\\Daeseong")
    """

    pass
