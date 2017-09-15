time = input()
hh = time[0:2]
mm = time[3:5]
ss = time[6:8]
if time[8:] == "PM" and hh != "12" :
    hh = str(int(hh)+12)
if time[8:] == "AM" and hh == "12" :
    hh = "00"

print("{}:{}:{}".format(hh,mm,ss))