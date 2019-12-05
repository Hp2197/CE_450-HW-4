
def flttn(lst):
    if lst == []:
        return[]
    elif type(lst) != list:
        return[lst]
    else:
        return flttn(lst[0]) + flttn(lst[1:])
