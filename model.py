def pad_num(num):
    return ("0" if num < 10 else "") + str(num)


def format_time(seconds):
    days = int(seconds / 86400)
    hours = int(seconds / 3600) % 24
    mins = int(seconds / 60) % 60
    seconds = int(seconds % 60)

    days_string = (str(days) + " day" +
                   ("s " if days != 1 else " ")) if days > 0 else ""
    hours_string = pad_num(hours)
    mins_string = pad_num(mins)
    seconds_string = pad_num(seconds)

    return days_string + hours_string + ":" + mins_string + ":" + seconds_string
