import os
import pandas as pd


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
            SCHOOL: ["Angels Hingh", "Delhi Public"],
            YEAR: [2022, 2023],
            GENDER: ["Male"],
            RELIGION: ["Hindu"]
        }
        self.applied_sorting = NAME
        self.applied_sorting_ascending = True

    def get_selected_data(self):
        sdf = self.mainDf
        print(len(sdf))
        for key, value in self.applied_filters.items():
            sdf = pd.concat([sdf[sdf[key] == val] for val in value])
        return sdf.sort_values(by=self.applied_sorting, ascending=self.applied_sorting_ascending)

    def show_selected_data(self):
        sdf = self.get_selected_data()
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




def load_csv(seed):
    CSV_PATH = "adata/a_data_" + str(seed) + ".csv"
    return pd.read_csv(CSV_PATH),CSV_PATH


def printline():
    print("-"*25)
def wait4continue(pre_txt ='', txt ="Press ENTER to continue..."):
    input(pre_txt + txt)



def elaborate(df):
    #todo add percentage calc also
    for i in range(len(df)):
        printline()
        for col in df.columns:
            print(col,":",df[col][i])
        printline()


if __name__ == "__main__":

    df,main_data_path = load_csv(seed=1)

    selectableData = SelectableData(mainDf=df)  # common field for every menu

    def home_menu():
        printline()
        while True:
            #todo print a summary of data

            print("HOME MENU Options:")
            print("1.View/Export Data")
            print("2.Visualize/Export Charts")
            print("3.Modify/Insert Data")
            print("4.Delete Data")
            print("5.Exit")
            inp = int(input("Please Choose an option[1-5]:"))
            if inp == 1: view_data_menu()
            elif inp == 2: visualize_data_menu()#todo visualize
            elif inp == 3: modify_data_menu()
            elif inp == 4: delete_data_menu()
            elif inp == 5: return

    def visualize_data_menu():
        printline()
        while True:
            print("VISUALIZE DATA OPTIONS:")
            print("1.Show Selected Data")
            print("2.Apply Filters(By Schools,Year,Gender,Religion)")
            print("3.Apply Sorting(By Name,Percentage)")
            print("4.Show Histogram for Selected Data (On Basis of Marks, Students Count etc.)")
            inp = int(input("Please Choose an option[1-5]:"))
            if inp == 1:selectableData.show_selected_data()
            elif inp == 2:return


    def view_data_menu():

#todo:
        def apply_filters():
            printline()
            print("Available Filters:"+df.columns)
            for col in df.columns:
                print()

            return 0

        def apply_sorting():
            return 0



        def export_selected_data():
            sdf = selectableData.get_selected_data()
            try:
                printline()
                print("Exporting Selected Data:")
                print("Total Count:" + str(len(sdf)))
                print("Applied Filters:", selectableData.applied_filters)
                print("Applied Sorting:" + selectableData.applied_sorting)
                print("Sorting Order:" + ("Ascending" if selectableData.applied_sorting_ascending else "Descending"))
                printline()
                path = input("Please Enter the Path:")
                sdf.to_csv(path, index=False)
                print("Data Exported!")

            except:
                print("Error while exporting!")
                return
            wait4continue()



        def show_data_by_roll_num():
            try:
                roll = int(input("Enter Roll Number:"))
                print(elaborate(df[df[ROLL]==roll]))
                wait4continue()
            finally:
                return




        while True:
            printline()
            print("VIEW DATA MENU Options:")
            print("1.Show Selected Data")
            print("2.Apply Filters(By Schools,Year,Gender,Religion)")
            print("3.Apply Sorting(By Name,Percentage)")
            print("4.Export Selected Data")
            print("5.Show Data by Roll Number")
            print("6.Go Back")
            inp = int(input("Please Choose an option[1-5]:"))
            if inp == 1: selectableData.show_selected_data()
            elif int(inp) == 2: apply_filters()
            elif int(inp) == 3: apply_sorting()
            elif int(inp) == 4: export_selected_data()
            elif int(inp) == 5: show_data_by_roll_num()
            elif int(inp) == 6: return

    def modify_data_menu():#Requires saving data
        try:
            roll = int(input("Please enter the Roll Number to modify/insert:"))
            sdf = df[df[ROLL] == roll]
            for col in sdf.columns:
                if col == ROLL:
                    continue
                print("Please type new "+col+" and press ENTER, Or leave it blank to skip")
                inp = input("New "+col+":")
                if inp.strip():
                    sdf.loc[sdf[ROLL] == roll, col] = inp
                    df.loc[df[ROLL] == roll, col] = inp
            print(elaborate(sdf))
            wait4continue("Data Updated!")
        except:
            wait4continue("Error Updating Data!")

        return 0
    def delete_data_menu():#Requires saving data
        try:
            roll = int(input("Please enter the Roll Number to delete:"))
            sdf = df[df[ROLL] == roll]
            print(elaborate(sdf))
            inp = input("Are your Sure you want to DELETE this data??? [yes/no]")
            if inp.lower() == "yes":
                df.drop(df[df[ROLL] == roll].index, inplace=True)
                print("Data Deleted!")
            else :
                print("Data not deleted!")
            wait4continue()
        except:
            wait4continue("Error!")

        return 0

    home_menu()
    df.to_csv(main_data_path, index=False)
    print("Exiting...")



















