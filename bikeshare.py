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

    citydict = { 1: "chicago", 2: "new york city", 3: "washington"}
    monthdict = { 0: "all", 1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6:"june"}
    daydict = { 0: "all", 1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}
    
    while True:
        try:
            cityNo = int(input("Enter a number for city: \n (1) Chicago \n (2) New York City \n (3) Washington \n"))
            city = citydict[cityNo]
            break
        except ValueError:
            print("\n Try Again! Invalid Answer!\n")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            monthNo = int(input("Enter a number for month: \n (0) All \n (1) January \n (2) February \n (3) March \n (4) April \n (5) May \n (6) June \n"))
            month = monthdict[monthNo]
            break
        except ValueError:
            print("\n Try Again! Invalid Answer!\n")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            dayNo = int(input("Enter a number for day: \n (0) All \n (1) Monday \n (2) Tuesday \n (3) Wednesday \n (4) Thursday \n (5) Friday \n (6) Saturday \n (7) Sunday \n"))
            day = daydict[dayNo]
            break
        except ValueError:
            print("\n Try Again! Invalid Answer!\n")
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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month : " + str(common_month))
    
    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    print("The most common day of week : " + str(common_dow))

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour: " + str(common_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The  most commonly used start station: " + str(common_start_station))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The  most commonly used end station: " + str(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' --> ' + df['End Station']
    common_frequent_combination = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip : " + str(common_frequent_combination.split("-->")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time: " + str(total_travel))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time: " + str(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print("No gender info!!!")    

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print("\nEarliest year of birth: " + str(int(earliest)))       
        recent = df['Birth Year'].max()
        print("\nMost recent year of birth: " + str(int(recent)))     
        common_birth = df['Birth Year'].mode()[0]         
        print("\nMost common year of birth: " + str(int(common_birth)))             

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    is_raw_data = input('Do you want to see raw data? Enter y or n.\n')
    number = 0

    while True:
        if is_raw_data.lower() != 'n':    
            print(df.iloc[number : number + 5])           
            number +=5          
            is_raw_data = input('\nDo you want to see raw data? Enter y or n.\n')
        else:
            break

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
