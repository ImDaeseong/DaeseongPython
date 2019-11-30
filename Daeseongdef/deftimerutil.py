import threading

counter = 0
timer = None


def Repeat_timer():
    global counter, timer
    counter = counter + 1
    print(counter)

    if counter < 10:
        timer = threading.Timer(1, Repeat_timer)
        timer.start()
    else:
        timer.cancel()
        del timer


if __name__ == "__main__":
    Repeat_timer()
