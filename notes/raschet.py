day = 250
dlx = 1.1

week = day * 7 * 0.87
month = day * 30 * 0.67
print('Room 1,2,3')
print('------------')
print(f"Day = {day}")
print(f"Week = {week}")
print(f"Month = {month}")

week_dlx = week * dlx
month_dlx = month * dlx
print('Room Delux')
print('------------')
print(f"Day = {day * dlx}")
print(f"Week = {week * dlx}")
print(f"Month = {month * dlx}")
