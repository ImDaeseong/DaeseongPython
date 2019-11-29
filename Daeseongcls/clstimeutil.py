import datetime


class clstimeutil:
    def __init__(self):
        pass

    def GetFullCurrentDay(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def GetCurrentDay(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")

    def GetCurrentTime(self):
        now = datetime.datetime.now()
        # data = "%d-%d-%d-%d-%d-%d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
        # data = "%d:%d:%d" % (now.hour, now.minute, now.second)
        # print(data)
        return now.strftime("%H:%M:%S")

    def GetToday(self):
        day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        week = datetime.datetime.today().weekday()
        return day[week]

    def GetYear(self):
        now = datetime.datetime.now()
        return now.strftime("%Y")

    def GetMonth(self):
        now = datetime.datetime.now()
        return now.strftime("%m")

    def GetDay(self):
        now = datetime.datetime.now()
        return now.strftime("%d")

    def SetDay(self, nDay):
        now = datetime.datetime.now()
        # data = now + datetime.timedelta(weeks=nDay)
        # data = now + datetime.timedelta(hours=nDay)
        # data = now + datetime.timedelta(minutes=nDay)
        # data = now + datetime.timedelta(seconds=nDay)
        data = now + datetime.timedelta(days=nDay)
        return data.strftime("%Y-%m-%d %H:%M:%S")

    def SetMonth(self, nMonth):
        week = nMonth * 4
        now = datetime.datetime.now()
        data = now + datetime.timedelta(weeks=week)
        return data.strftime("%Y-%m-%d %H:%M:%S")

    def SetYear(self, nYear):
        week = nYear * 52
        now = datetime.datetime.now()
        data = now + datetime.timedelta(weeks=week)
        return data.strftime("%Y-%m-%d %H:%M:%S")

    def ConvertStrToTime(self, sTime):
        typetime = datetime.datetime.strptime(sTime, '%Y-%m-%d %H:%M:%S')
        # print(type(typetime))
        # print(typetime)
        return typetime

    def SubstringTime(self, sStart, sEnd):
        starttime = datetime.datetime.strptime(sStart, '%Y-%m-%d %H:%M:%S')
        endtime = datetime.datetime.strptime(sEnd, '%Y-%m-%d %H:%M:%S')
        day = (endtime - starttime).days  # 날짜
        second = (endtime - starttime).seconds  # 초
        hour = (endtime - starttime).seconds / 3600  # 시간
        # print(day)
        # print(second)
        # print(hour)
        return second


if __name__ == '__main__':
    clsobj = clstimeutil()
    print(clsobj.GetFullCurrentDay())
    print(clsobj.GetCurrentDay())
    print(clsobj.GetCurrentTime())
    print(clsobj.GetToday())
    print(clsobj.GetYear())
    print(clsobj.GetMonth())
    print(clsobj.GetDay())
    print(clsobj.ConvertStrToTime('2019-11-28 12:11:32'))
    print("내일시간:" + clsobj.SetDay(1))
    print("어제일시간:" + clsobj.SetDay(-1))
    print("한달뒤:" + clsobj.SetMonth(1))
    print("한달전:" + clsobj.SetMonth(-1))
    print("일년뒤:" + clsobj.SetYear(1))
    print("일년전:" + clsobj.SetYear(-1))
    print(clsobj.SubstringTime('2019-11-28 14:04:05', '2019-11-29 15:04:05'))

    pass
