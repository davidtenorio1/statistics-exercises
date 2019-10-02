import numpy as np
import pandas as pd


# 1.) How likely is it that you roll doubles when rolling two dice?
n_trials = 1_000_000
n_dice = 2
rolls = np.random.choice([1, 2, 3, 4, 5, 6], n_trials * n_dice).reshape(n_trials, 2)
df = pd.DataFrame(rolls)
doubles = df.mean() == df.mode()
df['rolled_doubles'] = df[0] == df[1]
doubles_probability = df.rolled_doubles.mean()
doubles_probability

# 2.) If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?
n_trials = 1_000_000
n_flips = 8
flips = np.random.choice([0, 1], n_trials * n_flips).reshape(n_trials, n_flips)
df = pd.DataFrame(flips)
df['three_heads'] = df.sum(axis=1) == 3
exactly_three_probability = df.three_heads.mean()
exactly_three_probability
df['more_than_three'] = df.sum(axis=1) > 3
more_than_three_probability = df.more_than_three.mean()
more_than_three_probability

# 3.) There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

n_trials = 1_000_000
n_billboards = 2
drives = np.random.choice(['web1', 'web2', 'web3', 'ds'], n_trials * n_billboards).reshape(n_trials, n_billboards)
df = pd.DataFrame(drives)
df['count'] = (df.values=='ds').sum(axis=1)
df['both_ds'] = df['count'] == 2
ds_probability = df.both_ds.mean()
ds_probability

# 4.) Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?
pop_tarts = np.random.normal(3,1.5,(1_000_000,5))
df = pd.DataFrame(pop_tarts)
df['sum'] = df.sum(axis=1)
df['poptarts_left'] = df['sum'] < 17
poptarts_probability = df.poptarts_left.mean()
poptarts_probability

# 5.) Compare Heights
#Men have an average height of 178 cm and standard deviation of 8cm.
#Women have a mean of 170, sd = 6cm.
#If a man and woman are chosen at random, P(woman taller than man)?
df_men = pd.DataFrame(np.random.normal(178,8,(1_000_000,1)))
df_women = pd.DataFrame(np.random.normal(170,6,(1_000_000,1)))
df_women['woman_taller_than_man'] = df_women > df_men
taller_woman_probability = df_women.woman_taller_than_man.mean()
taller_woman_probability

# 6.) When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 
# What are the odds that after having 50 students download anaconda, no one has an installation issue? 
fifty_data = np.random.random((1_000_000,50))
not_corrupted = fifty_data > (1/250)
df_not_corrupted = pd.DataFrame(not_corrupted)
df_not_corrupted['none_corrupted'] = df_not_corrupted.all(1)
none_corrupted_probability = df_not_corrupted.none_corrupted.mean()
none_corrupted_probability

# 100 students?
hundred_data = np.random.random((1_000_000,100))
not_corrupted = hundred_data > (1/250)
df_not_corrupted = pd.DataFrame(not_corrupted)
df_not_corrupted['none_corrupted'] = df_not_corrupted.all(1)
none_corrupted_probability = df_not_corrupted.none_corrupted.mean()
none_corrupted_probability

# What is the probability that we observe an installation issue within the first 150 students that download anaconda?
first_one_fifty_data = np.random.random((1_000_000,150))
corrupted = first_one_fifty_data < (1/250)
df_corrupted = pd.DataFrame(corrupted)
df_corrupted['at_least_one_corrupted'] = df_corrupted.any(1)
one_corrupted_probability = df_corrupted.at_least_one_corrupted.mean()
one_corrupted_probability

# How likely is it that 450 students all download anaconda without an issue?
four_fifty_data = np.random.random((1_000_000,450))
lucky = four_fifty_data > (1/250)
df_lucky = pd.DataFrame(lucky)
df_lucky['none_corrupted'] = df_lucky.all(1)
no_corrupted_probability = df_lucky.none_corrupted.mean()
no_corrupted_probability

# 7.) There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?
# How likely is it that a food truck will show up sometime this week?
data = np.random.random((1_000_000,3))
ft = data > .7
df_ft = pd.DataFrame(ft)
df_ft['food_truck_present'] = df_ft.any(1)
three_days_missing_probability = df_ft.food_truck_present.mean()
three_days_missing_probability

data2 = np.random.random((1_000_000,7))
ft_present = data2 <= .7
df_ft = pd.DataFrame(ft_present)
df_ft['food_truck_present'] = df_ft.any(1)
once_this_week_probability = df_ft.food_truck_present.mean()
once_this_week_probability

# 8.) If 23 people are in the same room, what are the odds that two of them share a birthday? 
birthdays = np.random.randint(1,365,(1_000_000,23))
df_birthdays = pd.DataFrame(birthdays)
df_birthdays['uniques'] = (df_birthdays.nunique(1))
df_birthdays['same_birthdays'] = df_birthdays.uniques != 23
same_probability = df_birthdays.same_birthdays.mean()

# What if it's 20 people?
birthdays = np.random.randint(1,365,(1_000_000,20))
df_birthdays = pd.DataFrame(birthdays)
df_birthdays['uniques'] = (df_birthdays.nunique(1))
df_birthdays['same_birthdays'] = df_birthdays.uniques != 20
same_probability = df_birthdays.same_birthdays.mean()

# What if it's 40 people?
birthdays = np.random.randint(1,365,(1_000_000,40))
df_birthdays = pd.DataFrame(birthdays)
df_birthdays['uniques'] = (df_birthdays.nunique(1))
df_birthdays['same_birthdays'] = df_birthdays.uniques != 40
same_probability = df_birthdays.same_birthdays.mean()




