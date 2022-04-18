def add_time(start, duration, day=""):
    a = start
    a_s = a.split()
    a_s1 = a_s[0].split(":")
    a_s1.append(a_s[1])
    a1 = a_s1  # >>>['6', '30', 'PM']
    #0:00 AM = 00:00, 12:00 PM = 12:00
    h = int(a1[0])
    m = int(a1[1])
    ampm = a1[2]
    
    if ampm == "PM":
        h = h + 12
        ampm = "AM"
        
    b = duration
    b1 = b.split(":")
    h = h + int(b1[0])
    m = m + int(b1[1])

    if m > 59:
        n = m // 60
        h = h + n
        m = m % 60  # minuty očištěné od hodin

    h1 = h // 12
    h = h % 12

    d = h1//2

    if h1 % 2 == 1:
        ampm = "PM"

    if h == 0:
        h = 12

    if d == 1:
        d1 = "(next day)"
    else:
        d1 = f"({d} days later)"
    
    if len(day)>0:
        day = day.lower()
        week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        w = week.index(day)
        w = w + d
        w = w % 7
        day = week[w]
        day = day.capitalize()
        new_time = f"{h}:{m:02d} {ampm}, {day} {d1}"
        if d == 0:
            new_time = f"{h}:{m:02d} {ampm}, {day}"
    else:
        new_time = f"{h}:{m:02d} {ampm} {d1}"
        if d == 0:
            new_time = f"{h}:{m:02d} {ampm}"  
    #print(new_time)
    return new_time
"""
add_time("3:00 PM", "3:10")
add_time("11:30 AM", "2:32", "Monday")
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
add_time("6:30 PM", "205:12")
"""