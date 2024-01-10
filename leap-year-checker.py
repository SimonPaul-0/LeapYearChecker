def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    try:
        year = int(input('Enter the year: '))
        if year > 0:
            if is_leap_year(year):
                print(f'The entered year {year} is a leap year.')
            else:
                print(f'The entered year {year} is not a leap year.')
        else:
            print('Please enter a positive integer for the year.')
    except ValueError:
        print('Invalid input. Please enter a valid integer for the year.')

if __name__ == "__main__":
    main()
