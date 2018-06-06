import time

CITY_DATA = { 'chicago': 'chicago.csv',
			  'new york city': 'new_york_city.csv',
			  'washington': 'washington.csv'}

def get_filters():
    '''
    others
    '''
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
    city_lower = city.lower()
    while city_lower not in CITY_DATA:
        city = input('The Input is wrong! Would you like to see data for Chicago, New York City, or Washington?\n')
        city_lower = city.lower()

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
			  'september', 'october', 'november', 'december', 'all']

    month = input('Which month? ALL, January, February, March, Apirl, May or June\n')
    month_lower = month.lower()
    while month_lower not in months:
        month = input('The Input is wrong! Which month? ALL, January, February, March, Apirl, May or June\n')
        month_lower = month.lower()

    print('-'*40)
    return city, month

city, month = get_filters()
print('the cith is %s' %city)
print('the month is %s\n' %month)

# import adan
