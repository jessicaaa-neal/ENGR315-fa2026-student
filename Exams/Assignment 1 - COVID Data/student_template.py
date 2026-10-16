import sys

"""
Create a program which will provide answers to the questions posed in the assignment description.
We've provided a function which will parse the NYT covid database file (named "us-counties.csv"); 
however, its correct implementation will be up to you. DO NOT MODIFY THIS FUNCTION.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
"""


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information

    ____________________ DO NOT MODIFY THIS FUNCTION ___________________
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

### YOUR CODE HERE ###

# path to the NYT Covid Data file
filepath = 'data/covid/us-counties.csv'

# call function to parse the data
covid_data = parse_nyt_data(filepath)

# variables to store the first dates with positive cases
harrisonburg_first_date=''
rockingham_first_date=''

#iterate through Covid Data
for entry in covid_data:

    # separate information
    date=entry[0]
    county=entry[1]
    state=entry[2]
    cases=entry[4]

    #determine first positive Harrisonburg Case
    if state=='Virginia' and county=='Harrisonburg city' and cases>0:
        if harrisonburg_first_date=='':
            harrisonburg_first_date=date

    #determine first positive Rockingham Case
    if state=='Virginia' and county=='Rockingham' and cases>0:
        if rockingham_first_date == '':
            rockingham_first_date=date

#print question 1 results
print ('Question 1 Answer:')
print('The first positive COVID case in Harrisonburg, VA is', harrisonburg_first_date)
print ('The first positive COVID case in Rockingham, VA is', rockingham_first_date)
print()

# Question 2 variables
harrisonburg_previous_cases=0
rockingham_previous_cases=0

harrisonburg_new_cases=0
rockingham_new_cases=0

harrisonburg_new_date=''
rockingham_new_date=''

# iterate through Covid Data
for entry in covid_data:

    #separate information
    date=entry[0]
    county=entry[1]
    state=entry[2]
    cases=entry[4]

    #check Harrisonburg data
    if state=='Virginia' and county=='Harrisonburg city':

        #calculate new cases
        new_cases=cases-harrisonburg_previous_cases

        #see if this is the most amount of new cases
        if new_cases>harrisonburg_new_cases:
            harrisonburg_new_cases=new_cases
            harrisonburg_new_date=date

        #save the total for next steps
        harrisonburg_previous_cases=cases

    #check Rockingham data
    if state=='Virginia' and county=='Rockingham':

        #calculate new cases
        new_cases=cases-rockingham_previous_cases

        #see if this is the most amount of new cases
        if new_cases>rockingham_new_cases:
            rockingham_new_cases=new_cases
            rockingham_new_date=date

        #save the total for next steps
        rockingham_previous_cases=cases

#print question 2 results
print('Question 2 Answer:')
print('The date with the greatest number of new cases in Harrisonburg is', harrisonburg_new_date)
print('The date with the greatest number of new cases in Rockingham is', rockingham_new_date)
print()

#Question 3 variables
#create lists to store dates and cases
harrisonburg_dates=[]
harrisonburg_daily_cases=[]

rockingham_dates=[]
rockingham_daily_cases=[]

#store previous total number of cases
harrisonburg_previous_cases=0
rockingham_previous_cases=0

#iterate through Covid Data
for entry in covid_data:

    #separate information
    date=entry[0]
    county=entry[1]
    state=entry[2]
    cases=entry[4]

    #Check Harrisonburg data
    if state == 'Virginia' and county =='Harrisonburg city':

        #calculate the amount of new cases
        new_cases=cases-harrisonburg_previous_cases

        #save the information in the list
        harrisonburg_dates.append(date)
        harrisonburg_daily_cases.append(new_cases)

        #save current total
        harrisonburg_previous_cases=cases
    
    #Check Rockingham data
    if state == 'Virginia' and county =='Rockingham':

        #calculate the amount of new cases
        new_cases=cases-rockingham_previous_cases

        #save the information in the list
        rockingham_dates.append(date)
        rockingham_daily_cases.append(new_cases)

        #save current total
        rockingham_previous_cases=cases

#variables to store largest 7 day totals
harrisonburg_seven_day=0
harrisonburg_start_date=''
harrisonburg_end_date=''

rockingham_seven_day=0
rockingham_start_date=''
rockingham_end_date=''

#check each 7 day period in Harrisonburg
for a in range(len(harrisonburg_daily_cases)-6):

    #start the total at 0
    seven_day_total=0

    #add in new cases
    for b in range(7):
        seven_day_total=seven_day_total+harrisonburg_daily_cases[a+b]

    #see if this is the largest total
    if seven_day_total>harrisonburg_seven_day:

        #save it
        harrisonburg_seven_day = seven_day_total

        #save first and last date of the period
        harrisonburg_start_date=harrisonburg_dates[a]
        harrisonburg_end_date=harrisonburg_dates[a+6]

#check each 7 day period in Rockingham
for a in range(len(rockingham_daily_cases)-6):

    #start the total at 0
    seven_day_total=0

    #add in new cases
    for b in range(7):
        seven_day_total=seven_day_total+rockingham_daily_cases[a+b]

    #see if this is the largest total
    if seven_day_total>rockingham_seven_day:

        #save it
        rockingham_seven_day = seven_day_total

        #save first and last date of the period
        rockingham_start_date=rockingham_dates[a]
        rockingham_end_date=rockingham_dates[a+6]


# Print question 3 answers
print('Question 3 Answer:')
print('The worst seven day period in Harrisonburg for new COVID cases is', harrisonburg_start_date, 'to', harrisonburg_end_date)
print('The worst seven day period in Rockingham for new COVID cases is', rockingham_start_date, 'to', rockingham_end_date)






