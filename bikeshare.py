import time
import pandas as pd
import numpy as np


CITY_DATA = {'chicago': r'E:\Python\BikeShareData\chicago.csv',
             'new york city': r'E:\Python\BikeShareData\new_york_city.csv',
             'washington': r'E:\Python\BikeShareData\washington.csv'}
MONTHS_DATA = ['january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


# noinspection PyGlobalUndefined
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    global city, day, month

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input("\nWhich city's data you would like to see:-"
                         "\nChicago\nNew York City\nWashington"
                         "\nPlease select one of the above cities.\n").lower()
        except KeyError:
            print("You have entered invalid entry.\n")
            continue

        if city not in CITY_DATA:
            print("\nSorry, looks like You have entered invalid city.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nWhich month you would like to navigate,\n"
                          "January\nFebruary\nMarch\nApril\nMay\nJune\n"
                          "Please select the month, or type 'All' for all months.\n").lower()
        except KeyError:
            print("You have entered invalid entry\n.")
            continue
        if month not in MONTHS_DATA and month != 'all':
            print("\nSorry, looks like You have entered invalid month.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nWhich day you would like to navigate,\n"
                        "Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday\n"
                        "Please select the day or type 'All' for all of the weekdays.\n").lower()
        except KeyError:
            print("You have entered invalid entry\n.")
            continue
        if day not in WEEKDAYS and day != 'all':
            print("\nSorry, looks like You have entered invalid day.")
            continue
        else:
            break

    print("\nThe data you have selected is:\nCity: {}\nMonth: {}\nWeekday: {}\nProceeding your query..."
          "".format(city.title(), month.title(), day.title()))
    print("-" * 40)
    return city, month, day


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent month in 1st half of 2017 is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent day in the week is: ', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = ' From: ' + df['Start Station'] + ' To: ' + df['End Station']
    popular_route = df['route'].mode()[0]
    print('Most most frequent combination of start station and end station trip:\n', popular_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum().sum() // 60
    print('Total travel is:', total_trip_duration, 'Minutes')

    # TO DO: display mean travel time
    average_trip_duration = int(df['Trip Duration'].mean()) // 60
    print('Average trip duration is:', average_trip_duration, 'Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types, '\n')

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('User Gender:\n', user_gender, '\n')
    except KeyError:
        print("Sorry, looks like there is no data available for user gender.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].dropna().min()
        most_recent_year = df['Birth Year'].dropna().max()
        most_common_year = df['Birth Year'].dropna().mode()[0]

        print("The earliest birth year is: {}\n"
              "The most recent  birth year is: {}\n"
              "The most common birth year is: {}"
              "".format(int(earliest_year), int(most_recent_year), int(most_common_year)))

    except KeyError:
        print("Sorry, looks like there is no data available for birth year.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def overall_stats(df):
    """Displays overall Trip Duration statistics ."""

    print('\nCalculating Overall Trip Duration Statistics...\n')
    start_time = time.time()

    # Display overall Trip Duration statistics
    print('Overall trip duration statistics :'
          '\n', df['Trip Duration'].describe().astype(int))

    # Display overall Trip Duration by user type (in hours)
    print('\nTrip Duration by user type (Hours):\n', df.groupby(['User Type'])['Trip Duration'].sum() // 360)

    # Display overall Trip Duration by user type and months (in hours)
    print('\nTrip Duration by user type and month (Hours):'
          '\n', df.groupby(['User Type', 'month'])['Trip Duration'].sum() // 360)

    # Display overall Trip Duration by user type and start station (in hours)
    print('\nTrip Duration by user type and start station (Hours):'
          '\n', df.groupby(['User Type', 'Start Station'])['Trip Duration'].sum() // 360)

    # Display overall Trip Duration by user type and end station (in hours)
    print('\nTrip Duration by user type and end station (Hours):'
          '\n', df.groupby(['User Type', 'End Station'])['Trip Duration'].max() // 360)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def data_row_iteration(df):
    print('\nPreparing first set of data rows...\n')
    start_time = time.time()

    # Show selected data, 5 rows at a time
    selection = input('Would you like to visit the raw data? Enter [Yes/No]\n').lower()

    i = 0
    while True:
        if selection.lower() == 'yes':
            for label, row in df.iterrows():
                print('Row ' + str(label + 1) + ' :   ' + str(row)[10:])
                i += 1
                if i != 0 and i % 5 == 0:
                    selection = input('Would you like to see more data? Enter [Yes/No]\n').lower()
                    if selection != 'yes':
                        if selection not in ['yes', 'no']:
                            selection = input("It seems your entry is invalid."
                                              " Please enter [Yes/No]\n").lower()
                        elif selection == 'no':
                            break
        elif selection == 'no':
            break
        elif selection not in ['yes', 'no']:
            selection = input("It seems your entry is invalid. Please enter [Yes/No]\n").lower()
            continue

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        overall_stats(df)
        data_row_iteration(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Create DataFrame from selected city csv file
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.strftime('%H')

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


if __name__ == "__main__":
    main()