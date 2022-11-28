log_file = open(r"C:\Users\Badger\Desktop\Code\Keylogger\Log\ key_log.txt", "r")
Lines = log_file.readlines()

line = Lines[0]
# Date and time of first log

date = line[:10]
time = line[10:19]
init_date = date
init_time = time

hourly_log = []
for line in Lines:
    if 'Key' in line:
        if 'backspace' in line:
            hourly_log.pop(-1)
        else:
            hourly_log.append(' ')
    # Checks if the date and time is the same with the last line
    elif date == line[:10]:
        if time[1:5] in line:
            hourly_log.append(line[26])
        else:
            # Resets default date and time
            date = line[:10]
            time = line[10:19]
            hourly_log.append('\n' + date + time + '\n')
            hourly_log.append(line[26])

print(init_date + init_time + '\n' + ''.join(hourly_log) + '\n')

with open(r'C:\Users\Badger\Desktop\Code\Keylogger\Log\clean_key_log.txt', 'w') as f:
    f.write(init_date + init_time + '\n' + ''.join(hourly_log) + '\n')

