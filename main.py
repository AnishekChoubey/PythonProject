import os
import pandas as pd
import matplotlib.pyplot as plt

from datagen import SUBJECTS

NAME = "Name"
ROLL = "RollNo"
GENDER = "Gender"
RELIGION = "Religion"
YEAR = "ExamYear"
SCHOOL = "SchoolName"

class SelectableData:
    #todo
    def __init__(self,mainDf):
        self.mainDf = mainDf
        self.applied_filters = {

        }
        self.applied_sorting = NAME
        self.applied_sorting_ascending = True

    def get_df(self):
        sdf = self.mainDf
        #print(len(sdf))
        for key, value in self.applied_filters.items():

            if value is not None:
                if len(value) > 0:
                    sdf = pd.concat([sdf[sdf[key] == val] for val in value])

        return sdf.sort_values(by=self.applied_sorting, ascending=self.applied_sorting_ascending)

    def show_selected_data(self):
        sdf = self.get_df()
        printline()
        print("Showing Selected Data:")
        print("Total Count:" + str(len(sdf)))
        print("Applied Filters:", self.applied_filters)
        print("Applied Sorting:" + self.applied_sorting)
        print("Sorting Order:" + ("Ascending" if self.applied_sorting_ascending else "Descending"))
        printline()
        print(sdf.head(6))  # todo pagination
        printline()
        wait4continue()
        return





if __name__ == "__main__":

    df,main_data_path = load_csv(seed=1)

    selectableData = SelectableData(mainDf=df)  # common field for every menu













    home_menu()
    df.to_csv(main_data_path, index=False)
    print("Exiting...")
