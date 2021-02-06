import pandas as pd
import numpy as np

students_performance = pd.read_csv("StudentsPerformance.csv")
titanic = pd.read_csv("titanic.csv")


# task_2
# (students_performance['lunch']=='free/reduced').mean()


# task_3
# print((students_performance['lunch']=='standard').mean())
# print((students_performance['lunch']=='standard').var())

# task_6
# df = pd.read_csv("column_hell.csv")
# selected_columns = df.filter(like="-")
