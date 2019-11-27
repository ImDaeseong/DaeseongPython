from Daeseongdef.defStringutil import GetExt, GetFileName, GetOnlyFileName
from Daeseongcls.clsStringutil import clsStringutil
from Daeseongdef.defjsonutil import GetJson, WriteString, WriteJsonString
from Daeseongcls.clsjsonutil import clsjsonutil


def func1():
    print("GetExt: " + GetExt('E:\\Util\\python\\python.png'))
    print("GetFileName: " + GetFileName('E:\\Util\\python\\python-3.8.0.png'))
    print("GetOnlyFileName: " + GetOnlyFileName('E:\\Util\\python\\python-3.8.0.png'))


def func2():
    strobj = clsStringutil('E:\\Util\\python\\python.png')
    print("Get_Ext: " + strobj.Get_Ext())
    print("Get_FileName: " + strobj.Get_FileName())
    print("Get_OnlyFileName: " + strobj.Get_OnlyFileName())


def func3():
    testdata = [
        {'id': '1', 'packagename': 'com.pearlabyss.blackdesertm', 'gametitle': '검은사막 모바일',
         'gamedesc': {'details1': '당신이 진짜로 원했던 모험의 시작', 'details2': '월드클래스 MMORPG “검은사막 모바일”'}},
        {'id': '2', 'packagename': 'com.kakaogames.moonlight', 'gametitle': '달빛조각사',
         'gamedesc': {'details1': "500만 구독자의 게임 판타지 대작 '달빛조각사'", 'details2': '- 5레벨만 달성해도 달빛조각사 이모티콘 100% 지급!'}},
        {'id': '3', 'packagename': 'com.ncsoft.lineagem19', 'gametitle': "리니지M",
         'gamedesc': {'details1': 'PC의 향수! 리니지 본질 그대로 리니지M', 'details2': 'PC리니지와 동일한 아덴월드의 오픈 필드'}},
        {'id': '4', 'packagename': 'com.netmarble.bnsmkr', 'gametitle': '블레이드&소울 레볼루션',
         'gamedesc': {'details1': '원작 감성의 방대한 세계관과 복수 중심의 흥미진진한 스토리', 'details2': 'MMORPG의 필드를 제대로 즐길 수 있는 경공'}},
        {'id': '5', 'packagename': 'com.cjenm.sknights', 'gametitle': '세븐나이츠',
         'gamedesc': {'details1': 'Netmarble롤플레잉', 'details2': '세나의 재탄생, 세븐나이츠: 리부트'}},
        {'id': '6', 'packagename': 'com.google.android.youtube', 'gametitle': 'YouTube',
         'gamedesc': {'details1': 'Google LLC동영상 플레이어/편집기', 'details2': '좋아하는 동영상 빠르게 검색하기'}},
    ]

    WriteString('C:\\game.json', '[')
    i = 0
    for row in testdata:
        WriteJsonString('C:\\game.json', row)
        if i < 5:
            WriteString('C:\\game.json', ',')
        i = i + 1
    WriteString('C:\\game.json', ']')

    game = GetJson('C:\\game.json')
    for i in game:
        print(i['id'], i['packagename'], i['gametitle'], i['gamedesc']['details1'], i['gamedesc']['details2'])
    pass


def func4():
    testdata = [
        {'id': '1', 'packagename': 'com.pearlabyss.blackdesertm', 'gametitle': '검은사막 모바일',
         'gamedesc': {'details1': '당신이 진짜로 원했던 모험의 시작', 'details2': '월드클래스 MMORPG “검은사막 모바일”'}},
        {'id': '2', 'packagename': 'com.kakaogames.moonlight', 'gametitle': '달빛조각사',
         'gamedesc': {'details1': "500만 구독자의 게임 판타지 대작 '달빛조각사'", 'details2': '- 5레벨만 달성해도 달빛조각사 이모티콘 100% 지급!'}},
        {'id': '3', 'packagename': 'com.ncsoft.lineagem19', 'gametitle': "리니지M",
         'gamedesc': {'details1': 'PC의 향수! 리니지 본질 그대로 리니지M', 'details2': 'PC리니지와 동일한 아덴월드의 오픈 필드'}},
        {'id': '4', 'packagename': 'com.netmarble.bnsmkr', 'gametitle': '블레이드&소울 레볼루션',
         'gamedesc': {'details1': '원작 감성의 방대한 세계관과 복수 중심의 흥미진진한 스토리', 'details2': 'MMORPG의 필드를 제대로 즐길 수 있는 경공'}},
        {'id': '5', 'packagename': 'com.cjenm.sknights', 'gametitle': '세븐나이츠',
         'gamedesc': {'details1': 'Netmarble롤플레잉', 'details2': '세나의 재탄생, 세븐나이츠: 리부트'}},
        {'id': '6', 'packagename': 'com.google.android.youtube', 'gametitle': 'YouTube',
         'gamedesc': {'details1': 'Google LLC동영상 플레이어/편집기', 'details2': '좋아하는 동영상 빠르게 검색하기'}},
    ]

    jsonobj = clsjsonutil('C:\\game.json')

    jsonobj.WriteString('[')
    i = 0
    for row in testdata:
        jsonobj.WriteJsonString(row)
        if i < 5:
            jsonobj.WriteString(',')
        i = i + 1
    jsonobj.WriteString(']')

    game = jsonobj.GetJson()
    for i in game:
        print(i['id'], i['packagename'], i['gametitle'], i['gamedesc']['details1'], i['gamedesc']['details2'])


if __name__ == '__main__':
    """
    func1()
    func2()
    func3()
    func4()
    """
