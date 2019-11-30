from threading import Timer


class clstimerutil:
    def __init__(self, second, endtime):
        self.counter = 0
        self.second = second
        self.endtime = endtime
        self.timer = None

    def Repeat_timer(self):
        self.counter = self.counter + 1
        print(self.counter)
        # endtime 까지만 반복
        if self.counter < self.endtime:
            self.start_timer()
        else:
            self.cancel()

    def Repeat_timerA(self):
        # 무한 반복
        self.counter = self.counter + 1
        print(self.counter)
        self.start_timer()

    def start_timer(self):
        # self.timer = Timer(self.second, self.Repeat_timerA)
        self.timer = Timer(self.second, self.Repeat_timer)
        self.timer.start()

    def start(self):
        self.start_timer()

    def cancel(self):
        self.timer.cancel()
        del self.timer


if __name__ == '__main__':
    clsobj = clstimerutil(1, 10)
    clsobj.start()
    pass
