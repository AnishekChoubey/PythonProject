import pandas as pd


NAME = "Name"
ROLL = "RollNo"
GENDER = "Gender"
RELIGION = "Religion"
YEAR = "ExamYear"
SCHOOL = "SchoolName"


seed = 1
CSV_PATH = "adata/a_data_" + str(seed) + ".csv"
df = pd.read_csv(CSV_PATH)
l = ["Angels High"]

df = pd.concat([df[df[SCHOOL]==val] for val in l])
print(df)

applied_filters = {
            SCHOOL:["Angels Hingh","Delhi Public"],
            YEAR:[2022,2023],
            GENDER:["Male"],
            RELIGION:["Hindu"]
        }
applied_sorting = NAME
applied_sorting_ascending = True





