hours = 2
minutes_in_hour = 60
interval_minutes = 10
readings = int(minutes_in_hour/interval_minutes)
count = 1
total = 0
average = 0.0

start_ = input('Press enter to start program')

if start_ == "":
    hour = 1
    for x in range(hours):
        print(f'Hour: {hour}')
        hour = hour + 1
        count = 1
        for y in range(readings):
            ph_ = input(f'Reading {count} Enter PH (10-50) ')
            while int(ph_) < 10 or int(ph_) > 50:
                print("ERROR - PH must be an integer from 10 thru 50. Re-Enter")
                ph_ = input(f'Reading {count} Enter PH (10-50) ')
            else:
                count += 1
                total += int(ph_)
        print()
    average = total / 12
    print(f'Average PH: {average:.2f}')
    
