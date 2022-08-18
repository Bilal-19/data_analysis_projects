import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex']=='Male','age'].mean()
    average_age_men = round(average_age_men,3)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.loc[df['education']=='Bachelors','education']
    percentage_bachelors = round((percentage_bachelors.shape[0]/df.shape[0]) * 100,2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[
        (df['education']=='Bachelors')|
        (df['education']=='Masters')|
        (df['education']=='Doctorate')]
    
    lower_education = df.loc[
        (df['education'] != 'Bachelors') & 
        (df['education'] != 'Masters') & 
        (df['education'] != 'Doctorate')]


    # percentage with salary >50K
    # for percentage = obtain/total * 100
    higher_education_rich = higher_education.loc[higher_education['salary'] == '>50K']
    higher_education_rich = round((higher_education_rich.shape[0]/higher_education.shape[0])*100,2)
    
    lower_education_rich = lower_education.loc[lower_education['salary'] == '>50K']
    lower_education_rich = round((lower_education_rich.shape[0]/lower_education.shape[0])*100,2)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df.loc[df['hours-per-week'],'hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] < df['hours-per-week'].mean()]
    num_min_workers = num_min_workers.loc[num_min_workers['salary'] == '>50K']
    percentage = (num_min_workers.shape[0]/df.shape[0]) * 100
    
    # What country has the highest percentage of people that earn >50K?
    # highest_earning_country --- United States
    # highest_earning_country_percentage --- 7177 
    # for percentage = 7177/sum of highest_earning_country values

    highest_earning_country = df.loc[df['salary'] == '>50K']
    country_distribution = dict(highest_earning_country['native-country'].value_counts())
    highest_earning_country = max(country_distribution,key=country_distribution.get)
    highest_earning_country_percentage = country_distribution[highest_earning_country]/sum(country_distribution.values())
    highest_earning_country_percentage = round((highest_earning_country_percentage*100),2)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = top_IN_occupation[['salary','native-country','occupation']]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race: \n" , race_count) 
        print("\nAverage age of men:", average_age_men)
        print(f"\nPercentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"\nPercentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"\nPercentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"\nMin work time: {min_work_hours} hours/week")
        print("\nCountry with highest percentage of rich:", highest_earning_country)
        print(f"\nHighest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("\nTop occupations in India:\n", top_IN_occupation)

print(calculate_demographic_data(print_data=True))