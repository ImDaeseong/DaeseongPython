import configparser


class clsiniutil(object):

    def __init__(self, path):
        self.path = path

    def SetIniSection(self, section):
        config = configparser.ConfigParser()
        config.read(self.path)

        if not config.has_section(section):
            config.add_section(section)
            config.write(open(self.path, 'w'))

    def SetIniValue(self, section, key, val):
        config = configparser.ConfigParser()
        config.read(self.path)
        try:
            config.add_section(section)
        except configparser.DuplicateSectionError:
            pass
        config.set(section, key, val)
        config.write(open(self.path, 'w'))

    def GetIniValue(self, section, key):
        config = configparser.ConfigParser()
        config.read(self.path)
        if config.has_option(section, key):
            return config.get(section, key)
        else:
            return None


if __name__ == '__main__':

    clsobj = clsiniutil('c:\\gameinfo.ini')

    nGameCount = 3
    clsobj.SetIniSection("GameList")
    clsobj.SetIniValue("GameList", "GameCount", str(nGameCount))
    for i in range(nGameCount):
        key = "Gamekey%d" % (i)
        val = "Gamename%d" % (i)
        clsobj.SetIniValue("GameList", key, val)

    nReadCount = clsobj.GetIniValue("GameList", "GameCount")
    nCount = int(nReadCount)
    for i in range(nCount):
        key = "Gamekey%d" % (i)
        val = clsobj.GetIniValue("GameList", key)
        print(val)

    pass
