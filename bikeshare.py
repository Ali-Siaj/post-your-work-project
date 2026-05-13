import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march',
          'april', 'may', 'june']

days = ['all', 'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_name = input(
            "Would you like to see data for Chicago, New York City, or Washington?\n"
        ).lower()

        if city_name in CITY_DATA:
            break
        else:
            print("Invalid city. Please try again.")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "Which month? January, February, March, April, May, June or 'all'?\n"
        ).lower()

        if month in months:
            break
        else:
            print("Invalid month. Please try again.")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input(
            "Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or 'all'?\n"
        ).lower()

        if day in days:
            break
        else:
            print("Invalid day. Please try again.")

    return city_name, month, day


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

    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Most Common Month:",
          df['month'].mode()[0])

    # display the most common day of week
    print("Most Common Day:",
          df['day_of_week'].mode()[0])

    # display the most common start hour
    print("Most Common Hour:",
          df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""


    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station:")
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print("\nMost Common End Station:")
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Trip Combination'] = (
        df['Start Station']
        + " -> "
        + df['End Station']
    )

    print("\nMost Common Trip:")
    print(df['Trip Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""


    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    mean_duration = df['Trip Duration'].mean()

    # display total travel time
    print("Total Travel Time:")
    print(total_duration)

    # display mean travel time
    print("\nAverage Travel Time:")
    print(mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Types:")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:

        print("\nGender Counts:")
        print(df['Gender'].value_counts())

    else:
        print("\nNo gender data available.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        print("\nEarliest Birth Year:")
        print(int(df['Birth Year'].min()))

        print("\nMost Recent Birth Year:")
        print(int(df['Birth Year'].max()))

        print("\nMost Common Birth Year:")
        print(int(df['Birth Year'].mode()[0]))

    else:
        print("\nNo birth year data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data 5 rows at a time."""

    start = 0

    while True:
        show = input("\nWould you like to see 5 rows of raw data? yes/no: ").lower()
        if show.lower() not in ['yes', 'y']:
            break

        print(df.iloc[start:start + 5])
        start += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? yes/no: ').lower()
        if restart.lower() not in ['yes', 'y']:
            break

if __name__ == "__main__":
    main()
# This script analyzes bikeshare data using Python
# Refactored version of bikeshare analysis script