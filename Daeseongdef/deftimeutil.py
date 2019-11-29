import datetime


def GetFullCurrentDay():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def GetCurrentDay():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")


def GetCurrentTime():
    now = datetime.datetime.now()
    # data = "%d-%d-%d-%d-%d-%d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    # data = "%d:%d:%d" % (now.hour, now.minute, now.second)
    # print(data)
    return now.strftime("%H:%M:%S")


def GetToday():
    day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    week = datetime.datetime.today().weekday()
    return day[week]


def GetYear():
    now = datetime.datetime.now()
    return now.strftime("%Y")


def GetMonth():
    now = datetime.datetime.now()
    return now.strftime("%m")


def GetDay():
    now = datetime.datetime.now()
    return now.strftime("%d")


def SetDay(nDay):
    now = datetime.datetime.now()
    # data = now + datetime.timedelta(weeks=nDay)
    # data = now + datetime.timedelta(hours=nDay)
    # data = now + datetime.timedelta(minutes=nDay)
    # data = now + datetime.timedelta(seconds=nDay)
    data = now + datetime.timedelta(days=nDay)
    return data.strftime("%Y-%m-%d %H:%M:%S")


def SetMonth(nMonth):
    week = nMonth * 4
    now = datetime.datetime.now()
    data = now + datetime.timedelta(weeks=week)
    return data.strftime("%Y-%m-%d %H:%M:%S")


def SetYear(nYear):
    week = nYear * 52
    now = datetime.datetime.now()
    data = now + datetime.timedelta(weeks=week)
    return data.strftime("%Y-%m-%d %H:%M:%S")


def ConvertStrToTime(sTime):
    typetime = datetime.datetime.strptime(sTime, '%Y-%m-%d %H:%M:%S')
    # print(type(typetime))
    # print(typetime)
    return typetime


def SubstringTime(sStart, sEnd):
    starttime = datetime.datetime.strptime(sStart, '%Y-%m-%d %H:%M:%S')
    endtime = datetime.datetime.strptime(sEnd, '%Y-%m-%d %H:%M:%S')
    day = (endtime - starttime).days #날짜
    second = (endtime - starttime).seconds #초
    hour = (endtime - starttime).seconds / 3600  #시간
    # print(day)
    # print(second)
    # print(hour)
    return second


if __name__ == '__main__':
    print(GetFullCurrentDay())
    print(GetCurrentDay())
    print(GetCurrentTime())
    print(GetToday())
    print(GetYear())
    print(GetMonth())
    print(GetDay())
    print(ConvertStrToTime('2019-11-28 12:11:32'))
    print("내일시간:" + SetDay(1))
    print("어제일시간:" + SetDay(-1))
    print("한달뒤:" + SetMonth(1))
    print("한달전:" + SetMonth(-1))
    print("일년뒤:" + SetYear(1))
    print("일년전:" + SetYear(-1))
    print(SubstringTime('2019-11-28 14:04:05', '2019-11-29 15:04:05'))

    pass
