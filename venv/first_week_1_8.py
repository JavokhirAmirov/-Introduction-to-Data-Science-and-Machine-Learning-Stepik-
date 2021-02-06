import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# task_1
# data = {'type': ['A', 'A', 'B', 'B'], 'value': [10, 14, 12, 23]}
# my_data = pd.DataFrame(data=data)
# print(my_data)


# task_2
# my_stat = pd.read_csv('my_stat.csv')
# subset_1 = my_stat[['V1','V3']].iloc[:10]
# subset_2 = my_stat[['V2','V4']].drop([0,4], axis=0)
# print(my_stat)


# task_3
# my_stat = pd.read_csv('my_stat.csv')
# subset_1 = my_stat.query('V1 > 0 & V3 == "A"')
# subset_2 = my_stat.query('V2 != 10 | V4 >= 1')
# print(subset_2)


# task_4
# my_stat = pd.read_csv('my_stat.csv')
# my_stat['V5'] = my_stat.V1 + my_stat.V4
# my_stat['V6'] = np.log(my_stat.V2)
# print(my_stat)


# task_5
# my_stat = pd.read_csv('my_stat.csv')
# my_stat = my_stat.rename(columns={'V1': 'session_value', 'V2': 'group', 'V3': 'time', 'V4': 'n_users'})
# print(my_stat)


# task_6
# my_stat = pd.read_csv('my_stat_1.csv')
# my_stat = my_stat.fillna(0)
# median_without_negative_values = my_stat.query('n_users >= 0').n_users.median()
# my_stat.loc[my_stat['n_users'] < 0, 'n_users'] = median_without_negative_values
# print(my_stat)


# task_7
# my_stat = pd.read_csv('my_stat_1.csv')
# mean_session_value_data = my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'})
# mean_session_value_data = mean_session_value_data.rename(columns={'session_value': 'mean_session_value'})
# print(mean_session_value_data)
