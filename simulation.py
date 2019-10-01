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
flips_probability = df.three_heads.mean()
flips_probability

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
n_trials = 10
pop_tarts = np.random.normal()


