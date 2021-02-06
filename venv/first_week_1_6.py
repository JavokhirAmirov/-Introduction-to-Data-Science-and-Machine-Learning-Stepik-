import pandas as pd
import numpy as np


# task_1
# df_dota_heroes = pd.read_csv("dota_hero_stats.csv")
# print(df_dota_heroes.groupby('legs', as_index=False).agg({"id": 'count'}))




# task_2
# df_loopa_pupa = pd.read_csv("accountancy.csv")
# print(df_loopa_pupa.groupby(['Type', 'Executor'], as_index=False).agg({"Salary": "mean"}))


# task_3
# df_dota_heroes = pd.read_csv("dota_hero_stats.csv")
# print(df_dota_heroes.groupby(['attack_type', 'primary_attr'], as_index=False).agg({"id": "count"}))


# task_4
# concentrations = pd.read_csv("http://stepik.org/media/attachments/course/4852/algae.csv")
# print(concentrations.groupby('genus')\
#                     .agg({'sucrose': 'mean', 'alanin': 'mean', 'citrate': 'mean', 'glucose': 'mean', 'oleic_acid': 'mean'}))


# task_5
# concentrations = pd.read_csv("http://stepik.org/media/attachments/course/4852/algae.csv")
# print(concentrations.query('genus == "Fucus"')\
#                     .groupby('genus', as_index=False)\
#                     .agg({'alanin': 'min'}).round(2))
# print(concentrations.query('genus == "Fucus"')\
#                     .groupby('genus', as_index=False)\
#                     .agg({'alanin': 'mean'}).round(2))
# print(concentrations.query('genus == "Fucus"')\
#                     .groupby('genus', as_index=False)\
#                     .agg({'alanin': 'max'}).round(2))


# task_6
# concentrations = pd.read_csv("http://stepik.org/media/attachments/course/4852/algae.csv")
# print(concentrations.groupby('group', as_index=False).agg({'genus': 'count'}))


