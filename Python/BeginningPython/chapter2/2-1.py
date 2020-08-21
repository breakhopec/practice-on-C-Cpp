# show specific date

def main():
    months = ['', 'January', 'February', 'March', 'April', 
            'May', 'June', 'July', 'August', 'September',
            'October', 'November', 'December']
    days = ['th', 'st', 'nd', 'rd'] + ['th'] * 6

    year = input('input year: ')
    month = input('input month(1-12): ')
    day = input('input day(1-31): ')

    year_name = year
    month_name = months[int(month)]
    day_name = day + days[int(day[-1])]

    print(month_name + ' ' + day_name + ', ' + year_name)

if __name__ == '__main__':
    main()