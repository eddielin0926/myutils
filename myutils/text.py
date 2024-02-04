from datetime import datetime


def fpercent(part, whole, point=2):
    return f"{(100 * float(part)/float(whole)):.{point}f}%"


def timestamp(all_hyphen=False):
    if all_hyphen:
        return str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    else:
        return str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def wrap(data):
    return f"[{data[0]}, {data[1]}, ..., {data[-1]}]"
