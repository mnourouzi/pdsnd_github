import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_LIST = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        city = input('Please pick a city from the following to analyze: chicago, new york city, or washington ').lower()
        while city not in CITY_DATA:
            print('Oops! Seems like you did not provide a valid city, please check your spelling and re-enter.')
            city = input('Please pick a city from the following to analyze: chicago, new york city, or washington ').lower()
        print('You have chosen: ', city.title())

    # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Please pick a month from january to june to analyze or enter "all" to include all available months in your analysis. ').lower()
        while month not in MONTH_LIST:
            print('Oops! Seems like you did not provide a valid input, please check your spelling and re-enter.')
            month = input('Please pick a month from january to june to analyze or enter "all" to include all available months in your analysis. ').lower()
        print('You have chosen: ', month.title())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Please pick a day (monday, tuesday,...,sunday) to analyze or enter "all" to include all days. ').lower()
        while day not in DAY_LIST:
            print('Oops! Seems like you did not provide a valid input, please check your spelling and re-enter.')
            day = input('Please pick a day (monday, tuesday,...,sunday) to analyze or enter "all" to include all days. ').lower()
        print('You have chosen: ', day.title())

    except Exception as e:
        print('An error with your inputs occured: {}'.format(e))
        raise e
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day (if applicable).

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = MONTH_LIST.index(month)
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    try:
        common_month_num = df['month'].mode()[0]
        common_month = MONTH_LIST[common_month_num-1].title()
        print('Most Popular Month: ', common_month)
    except Exception as e:
        print('Couldn\'t calculate the most popular month, as an Error occurred: {}'.format(e))
        raise e
# TO DO: display the most common day of week
    try:
        common_day = df['day'].mode()[0]
        print('Most Popular Day: ', common_day)
    except Exception as e:
        print('Couldn\'t calculate the most popular day, as an Error occurred: {}'.format(e))
        raise e
    # TO DO: display the most common start hour
    try:
        common_hour = df['hour'].mode()[0]
        print('Most Popular Start Hour: ', common_hour)
    except Exception as e:
        print('Couldn\'t calculate the most popular hour, as an Error occurred: {}'.format(e))
        raise e
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    try:
        common_start_station = df['Start Station'].mode()[0]
        print('Most Popular Start Station: ', common_start_station)
    except Exception as e:
        print('Couldn\'t calculate the most popular start station, as an Error occurred: {}'.format(e))
    # TO DO: display most commonly used end station
    try:
        common_end_station = df['End Station'].mode()[0]
        print('Most Popular End Station: ', common_end_station)
    except Exception as e:
        print('Couldn\'t calculate the most popular end station, as an Error occurred: {}'.format(e))

    # TO DO: display most frequent combination of start station and end station trip
    try:
        df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' - ')
        common_trip = df['trip'].mode()[0]
        print('Most Common Trip: ', common_trip)
    except Exception as e:
        print('Couldn\'t calculate the most trip, as an Error occurred: {}'.format(e))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
        total_duration = df['Trip Duration'].sum()
        minute, second = divmod(total_duration, 60)
        hour, minute = divmod(minute, 60)
        print('Total Trip Duration: ', format(hour,","), ' hours', minute, ' minutes and', second, 'seconds')
    except Exception as e:
        print('Couldn\'t calculate total trip duration, as an Error occurred: {}'.format(e))
    # TO DO: display mean travel time
    try:
        average_duration = df['Trip Duration'].mean()
        minute, second = divmod(average_duration, 60)
        hour, minute = divmod(minute, 60)
        print('Average Trip Duration: ', format(hour,","), ' hours', minute, ' minutes and', second, 'seconds')
    except Exception as e:
        print('Couldn\'t calculate the average trip duration, as an Error occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
        print('Below are the user type counts:\n', user_type)
    except Exception as e:
        print('Couldn\'t calculate the user type counts, as an Error occurred: {}'.format(e))
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Below are the gender counts:\n', gender_count)
    except Exception as e:
        print('Couldn\'t calculate the gender counts, as an Error occurred: {}'.format(e))
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth: ', int(earliest_birth_year), '\nMost recent year of birth: ', int(recent_birth_year), '\nMost common year of birth: ', int(common_birth_year))
    except Exception as e:
        print('Couldn\'t calculate the gender counts, as an Error occurred: {}'.format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw date from csv file upon user request."""
    row_index = 0
    display_data = input('Would you like to see the raw data? Yes or No ').lower()
    while True:
        if display_data == 'no':
            return
        if display_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
            display_data = input('Would you like to see more rows of the raw data? Yes or No ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
