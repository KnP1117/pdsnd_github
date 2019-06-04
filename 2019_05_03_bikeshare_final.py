import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    while True:
        try:
            city_name = input(str('Choose city for data analysis.  Choices are: chicago, new york city, washington: '))
            cities = ['chicago', 'new york city', 'washington']
            if city_name in cities:
                city = city_name
                break
        except:
            print('That\'s not a valid entry!')
            continue
    # Provide data filter by month or day or no filter.
    while True:
        try:
            m_d_choice = input('Would you like to filter by: month, day or none? ')
            m_d_options = ['month', 'day', 'none']
            if m_d_choice in  m_d_options:
                m_d_filter = m_d_choice.lower()
                print(m_d_filter)
                break
        except:
           ('That\'s not a valid entry!')
           continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            if m_d_filter == 'none' or m_d_filter == 'day':
                month = 'all'
                break
            elif  m_d_filter != 'day' or m_d_filter != 'none':
                month_name = input('Choose month for data analysis; choices are: january, february, march, april, may, june\n')
                months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
                if month_name in months:
                    month = month_name.lower()
                    break
        except:
            print('That\'s not a valid entry!')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            if m_d_filter == 'none' or m_d_filter == 'month':
                day = 'all'
                break
            elif m_d_filter != 'month' or m_d_filter != 'none':
                day_name = input('Choose day for data analysis: Choices are monday through sunday\n')
                days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                if day_name in days:
                    day = day_name.lower()
                    break
        except:
            print('That\'s not a valid entry')
            continue
    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name
    df['Month Name'] = pd.to_datetime(df['Start Time'], format='%m').dt.month_name()
    df['Hour'] = df['Start Time'].dt.hour
    # input to provide 5 lines of the raw data frame
    while True:
         try:
             see_df = input('Would you like to see 5 lines of the unfiltered dataframe? \nyes or no\n')
             if see_df == 'no':
                 break
             elif see_df == 'yes':
                 print(df.head())
                 break
         except:
            continue
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day of Week'] == day.title()]
    #print(df)
    return df


    #print(df)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    while True:
        try:
            #print('\nCalculating The Most Frequent Times of Travel...\n')
            start_time = time.time()
            see_time_stats = input('\nWould you like to see travel time data?  \nyes or no.\n')
            if see_time_stats == 'no':
                break
            elif see_time_stats == 'yes':
                print('\nCalculating The Most Frequent Times of Travel...\n')
                start_time = time.time()

    # TO DO: display the most common month
                print('The most common month for bikeshare was: \n{}'.format(df['Month Name'].mode()[0]))
    # TO DO: display the most common day of week
                print('The most common day of the week for bikeshare was: \n{}'.format(df['Day of Week'].mode()[0]))
    # TO DO: display the most common start hour
                print('The most common start time hour for bikeshare was: \n{}'.format(df['Hour'].mode()[0]))
                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)
                break
        except:
            continue
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    while True:
        try:
            see_station_stats = input('\nWould you like to see station and trip data? \nyes or no.\n')
            if see_station_stats == 'no':
                break
            elif see_station_stats == 'yes':
                print('\nCalculating The Most Popular Stations and Trip...\n')
                start_time = time.time()

    # TO DO: display most commonly used start station
                print('Most common start station...\n{}'.format(df['Start Station'].mode()[0]))
    # TO DO: display most commonly used end station
                print('Most common end station...\n{}'.format(df['End Station'].mode()[0]))
    # TO DO: display most frequent combination of start station and end station trip
                print('Most common trip...\n{}'.format(df.groupby(['Start Station','End Station']).size().idxmax()))

                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)
                break
        except:
            continue


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    while True:
        try:
            see_trip_dur_stats = input('\nWould you like to see data about trip durations? \nyes or no.\n')
            if see_trip_dur_stats == 'no':
                break
            elif see_trip_dur_stats == 'yes':
                print('\nCalculating Trip Duration...\n')
                start_time = time.time()

    # TO DO: display total travel time
                print('The total of travel time in minutes...\n{}'.format(df['Trip Duration'].sum(0, True) / 60))

    # TO DO: display mean travel time
                print('The average of travel time in minutes...\n{}'.format(df['Trip Duration'].mean(0, True) /60))

                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)
                break
        except:
            continue


def user_stats(df):
    """Displays statistics on bikeshare users."""
    while True:
        try:
            see_user_stats = input('\nWould you like to see data about user statistics? \nyes or no.\n')
            if see_user_stats == 'no':
                break
            elif see_user_stats == 'yes':
                print('\nCalculating User Stats...\n')
                start_time = time.time()

                # TO DO: Display counts of user types
                print('User type counts...\n{}'.format(df['User Type'].value_counts()))

                # TO DO: Display counts of gender
                col = 'Gender'
                if col in df.columns:
                    print(df['Gender'].value_counts())
                else:
                    print('No gender data for Washington!')



                # TO DO: Display earliest, most recent, and most common year of birth
                print('The earliest, most recent, and most common year of birth...')
                col = 'Birth Year'
                if col in df.columns:
                    print(df['Birth Year'].value_counts())
                else:
                    print('No birth year data for Washington!')
                    break

                    print(df['Birth Year'].mode()[0])
                    print(df['Birth Year'].min(0, True))
                    print(df['Birth Year'].max(0, True))

                print("\nThis took %s seconds." % (time.time() - start_time))
                print('-'*40)
                break
        except:
            continue


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
