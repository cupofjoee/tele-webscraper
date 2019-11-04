import threading
import time
import scraper as sc
from datetime import datetime

data = []

def timer():
    threading.Timer(63, timer).start()
    global data
    start = datetime.now()
    data = sc.fetch_data()
    end = datetime.now()
    runtime  = end - start
    for msg in data:
        print(msg)
    print("Runtime: " + str(runtime))

timer()

# def timer():
#     threading.Timer(4, timer).start()
#     now = datetime.now()
#     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
#     # global data
#     # data = sc.fetch_data()
#     print(dt_string)

# print("hello")
# timer()
# print("world")


# start = datetime.now()
# print(sc.fetch_data())
# end = datetime.now()
# runtime = end - start
# print("runtime: " + str(runtime))