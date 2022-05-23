import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
  
    # What is the average age of men?
    average_age_men = int(df[df['sex'] == 'Male']['age'].mean())
  
    # What is the percentage of people who have a Bachelor's degree?
    a = sum(df[df['education'] == 'Bachelors'].value_counts())
    b = sum(df['education'].value_counts())
    percentage_bachelors = round((a/b)*100 , 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    def edu(title):
        if 'bachelors' in title.lower().split():
            return True
        else:
            return False
        if 'masters' in title.lower().split():
            return True
        else:
            return False
        if 'doctorate' in title.lower().split():
            return True
        else:
            return False
          
    higher_education = sum(df['education'].apply(lambda x:edu(x)))
    lower_education = sum(df['education'].value_counts())

    # percentage with salary >50K
    def salary(money):
        if '>' in money.lower():
            return True
        else:
            return False
    
	  
    total = sum(df[df['salary'].apply(lambda x:salary(x))].value_counts())
      
	  high_ed = sum(ed[ed['salary'].apply(lambda x:salary(x))].value_counts())

    higher_education_rich = round((high_ed/total)*100 , 1)
    lower_education_rich = 100-higher_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = sum(df[df['hours-per-week'] == min_work_hours ].value_counts())

    rich_percentage = round(num_min_workers/total*100 , 1)

    # What country has the highest percentage of people that earn >50K?
	
	  high_salary = df[df['salary'].apply(lambda x:salary(x))]
	  high_salary.drop(high_salary.index[high_salary['native-country'] == '?'], inplace = True)

	  highest_earning_country = high_salary['native-country'].value_counts().head(1).keys()

	  highest_country = high_salary['native-country'].value_counts().head(1)
	  highest_country_total  = sum(high_salary['native-country'].value_counts())
    
	  highest_earning_country_percentage = round(highest_country/highest_country_total)*100 , 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = high_salary[high_salary['native-country'] == 'India']        
    ['occupation'].value_counts().head(1)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: 
        {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
