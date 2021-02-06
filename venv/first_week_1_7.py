import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# task_1
# df = pd.read_csv('income.csv')
# sns.lineplot(x=df.index, y=df.income)
# plt.show()


# task_2
# with open('dataset_209770_6.txt', 'r') as infile, open('outfile.csv','w') as outfile:
#     for line in infile:
#         outfile.write(line.replace(' ',','))
# df = pd.read_csv('outfile.csv')
# sns.scatterplot(x=df.x, y=df.y)
# plt.show()
###### or
# df = pd.read_csv('dataset_209770_6.txt', sep=" ")
# sns.scatterplot(x=df.x, y=df.y)
# plt.show()


# task_3
# df = pd.read_csv('genome_matrix.csv', index_col=0)
# g = sns.heatmap(data=df, cmap='viridis')
# g.xaxis.set_ticks_position('top')
# g.xaxis.set_tick_params(rotation=90)
# plt.show()


# task_4
# df_heroes = pd.read_csv('dota_hero_stats.csv', index_col=0)
# df_heroes['total_roles'] = df_heroes.roles.str.split().str.len()
# print(df_heroes.total_roles.mode())


# task_5
# df_flowers = pd.read_csv('iris.csv', index_col=0)
# sns.kdeplot(x='sepal length', y='sepal width', data=df_flowers)
# sns.distplot(df_flowers)
# plt.show()
# print(df_flowers)


# task_6
# df_flowers = pd.read_csv('iris.csv', index_col=0)
# sns.violinplot(y='petal length', data=df_flowers, color='purple')
# plt.show()


# task_7
# df_flowers = pd.read_csv('iris.csv', index_col=0)
# sns.pairplot(df_flowers)
# plt.show()

