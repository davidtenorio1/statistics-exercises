from scipy import stats
from scipy.stats import norm, binom
import numpy as np
import pandas as pd
import env
from env import user, password, host


# 1.) A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.
# What is the probability that no cars drive up in the noon hour?
trials = 100_000
nonzero_cars = np.count_nonzero(np.random.poisson(2,trials))
no_cars_probability = (trials-nonzero_cars) / trials
no_cars_probability

cars_distribution = stats.poisson(2)
cars_distribution.cdf(0) #.135

# What is the probability that 3 or more cars come through the drive through?
three_plus_cars = sum(np.random.poisson(2,trials) >= 3)
three_or_more_probability = three_plus_cars/trials
three_or_more_probability

cars_distribution.sf(2) #.323

# How likely is it that the drive through gets at least 1 car?
one_plus_cars = sum(np.random.poisson(2,trials) >= 1)
one_or_more_probability = one_plus_cars/trials
one_or_more_probability #.862

cars_distribution.sf(0) #.865







# 2.) Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:
# What grade point average is required to be in the top 5% of the graduating class?
a = pd.DataFrame(np.sort(np.random.normal(3,.3,trials)))
r = round((95/100 * (trials + 1)))
a.iloc[[r]] #3.498 

gpa_distribution = norm(3, .3)
gpa_distribution.isf(.05) #3.493

# An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. 
# Would a student with a 2.8 grade point average qualify for this scholarship?
a = pd.DataFrame(np.sort(np.random.normal(3,.3,trials)))
r = round((20/100 * (trials + 1)))
a.iloc[[r]] #2.749

a = pd.DataFrame(np.sort(np.random.normal(3,.3,trials)))
r = round((30/100 * (trials + 1)))
a.iloc[[r]] #2.841

gpa_distribution.ppf(.2) 
gpa_distribution.ppf(.3) 
#bottom 30% = 2.748 through 2.843







# 3.) A marketing website has an average click-through rate of 2%. One day they observe 4326 visitors and 97 click-throughs. How likely is it that this many people or more click through?
data = (sum(np.random.random((4326,trials)) <.02) >= 97).mean() #.140


click_through_distribution = binom(4326, .02)
click_through_distribution.sf(96) #.140







# 4.) You are working on some statistics homework consisting of 100 questions where all of the answers are a probability rounded to the hundreths place. 
# Looking to save time, you put down random probabilities as the answer to each question.
# What is the probability that at least one of your first 60 answers is correct?
sim = ((np.random.random((trials, 60)) <= .01).sum(axis = 1) > 0).mean()

homework_distribution = binom(60,.01)
homework_distribution.sf(0) #.453





# 5.) The codeup staff tends to get upset when the student break area is not cleaned up. 
# Suppose that there's a 3% chance that any one student cleans the break area when they visit it, and, on any given day, about 90% of the 3 active cohorts of 22 students visit the break area. 
# How likely is it that the break area gets cleaned up each day?

avg_num_visits = round(.9 * 3 * 22)
((np.random.random((trials, avg_num_visits)) <= .03).sum(axis=1) > 0).mean() #.834

cleaned_distribution = binom(avg_num_visits, .03)
cleaned_distribution.sf(0) #.834

 # How likely is it that it goes two days without getting cleaned up? 
uncleaned_two_days = (1-(cleaned_distribution.sf(.9))) ** 2
#.027

 # All week?
uncleaned_seven_days = (1-(cleaned_distribution.sf(.9))) ** 7
# 3.44 * 10^-6



# 6.) You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. 
# After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of 15 and standard deviation of 3. 
# If it takes 2 minutes for each person to order, and 10 minutes from ordering to getting your food, what is the likelihood that you have at least 15 minutes left to eat your food before you have to go back to class? 
# Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.

sum(np.random.normal(15,3,trials) <= 17)/trials #.748

line = norm(15,3)
line.cdf(17)
#.748






# 7.) Connect to the employees database and find the average salary of current employees, along with the standard deviation. Model the distribution of employees salaries with a normal distribution and answer the following questions:

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

df = pd.read_sql('select salary from employees join salaries on employees.emp_no = salaries.emp_no where to_date = "9999-01-01"', url)
df.mean() #72,012
df.std() #17,310
salary_distribution = norm(72012,17310)

# What percent of employees earn less than 60,000?
salary_distribution.cdf(60000) #.244
# What percent of employees earn more than 95,000?
salary_distribution.sf(95000) #.092
# What percent of employees earn between 65,000 and 80,000?
salary_distribution.cdf(80000) - salary_distribution.cdf(65000) #.335
# What do the top 5% of employees make?
salary_distribution.isf(.05) #100,484









