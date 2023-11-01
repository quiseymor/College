month = int(input("Enter month number (1-12): "))
first_day = int(input("Enter the day of the week number (1-7): "))

months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'Оctober', 'November', 'December']

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

print('\t{:>2}'.format(months[month]))
print("Mo Tu We Th Fr Sa Su")

num_days = days_in_month[month]
start_day = (first_day - 1) % 7

for _ in range(start_day):
    print('{:>2}'.format(''), end=' ')
    
for day in range(1, num_days + 1):
    print('{:>2}'.format(day), end=' ')
    if (day + start_day) % 7 == 0:
        print()


