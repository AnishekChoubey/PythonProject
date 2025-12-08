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
            SCHOOL: ["Angels High", "Delhi Public"],
            YEAR: [2022, 2023],
            GENDER: ["Male"],
            RELIGION: ["Hindu"]
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




def load_csv(seed):
    CSV_PATH = "adata/a_data_" + str(seed) + ".csv"
    return pd.read_csv(CSV_PATH),CSV_PATH


def printline():
    print('\n\n')
    print("-"*25)
def wait4continue(pre_txt ='', txt ="Press ENTER to continue..."):
    input(pre_txt + txt)

def saveOrContinue(plt):
    #todo
    inp = input("Type 'save' to save the figure or Press ENTER to continue...")
    if inp == 'save':
        path = input("Enter the path to save the figure: ")
        try:
            plt.savefig(path)
            plt.close()
            wait4continue('Image saved!')

        except:
            wait4continue('Error saving figure!')


def showListItems(l):
    s = ''
    i = 0
    size = len(l)
    for val in l:
        i+=1
        s += ' '+ str(val)+ (', ' if i < size else '')
    return s
def selectColumn(df, columns_not_allowed = []):
    l = []
    l.extend(df.columns)
    for col in columns_not_allowed:
        try:l.remove(col)
        finally:continue



    for i in range(len(l)):
        print((i + 1), ". ", l[i])
    retval = None
    while True:
        colIndex = int(input("Select [1-" + str(len(l)) + "]:")) - 1
        colLabel = l[colIndex]
        retval = colLabel
        break
    return retval


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
            printline()
            print("HOME MENU Options:")
            print("1.View/Export Data")
            print("2.Visualize/Export Charts")
            print("3.Modify/Insert Data")
            print("4.Delete Data")
            print("5.Exit")
            inp = int(input("Please Choose an option[1-5]:"))#todo gives error if input isnt integer
            if inp == 1: view_data_menu()
            elif inp == 2: visualize_data_menu()#todo visualize
            elif inp == 3: modify_data_menu()
            elif inp == 4: delete_data_menu()
            elif inp == 5: return


    def apply_filters():

        while True:
            printline()

            print("1.Select Column")
            print("2.Go Back")
            inp1 = int(input("Please Choose an option[1-2]:"))
            selectedColumn = None
            if inp1 == 1:
                l = [ROLL, NAME]
                l.extend(SUBJECTS)
                selectedColumn = selectColumn(df, (l))
            else:
                break
            while True:
                printline()
                print("Selected Column:" + selectedColumn)
                print("Currently applied filters:" + str(str(selectableData.applied_filters[
                                                                 selectedColumn]) if selectedColumn in selectableData.applied_filters else 'None'))
                print("1.Add filter")
                print("2.Clear all filters")
                print("3.Go Back")
                inp = int(input("Please Choose an option[1-3]:"))  # todo: non integer value will crash the program
                if inp == 1:
                    print("Add filter")
                    print("#Repeatedly Type FilterValue and press Enter for the next value")
                    print("#To apply the filter and go back - Leave Blank and press Enter when finished")
                    i = 0
                    while True:
                        i += 1
                        filValue = input("Filter Value " + str(i) + ":")
                        if not filValue.strip():
                            break

                        if selectedColumn not in selectableData.applied_filters:
                            selectableData.applied_filters[selectedColumn] = []

                        selectableData.applied_filters[selectedColumn].append(filValue)
                    print("Filters Applied: ", selectableData.applied_filters[selectedColumn])
                    wait4continue()
                elif inp == 2:
                    selectableData.applied_filters.pop(selectedColumn)
                    wait4continue("All Filters Removed!")
                elif inp == 3:
                    break
                else:
                    print("Invalid Choice")

        return 0


    def apply_sorting():
        printline()
        print("Select Column for sorting")
        while True:
            selectedCol = selectColumn(df)
            if selectedCol not in df.columns:
                print("Invalid Column Name")
                continue
            print("Selected Sorting Order For Column:", selectedCol)
            print("A for Ascending, D for Descending")
            while True:
                order = input("[A/D]:")
                if order not in ["A", "D"]:
                    print("Invalid Order")
                    continue
                selectableData.applied_sorting_ascending = order == "A"
                break

            selectableData.applied_sorting = selectedCol
            wait4continue("Sorting applied!")
            break

        return 0


    def visualize_data_menu():
        printline()
        while True:
            printline()
            print("VISUALIZE DATA OPTIONS:")
            print("1.Show Selected Data")
            print("2.Apply Filters")
            print("3.Apply Sorting")

            print("4.Show Histogram - Average Marks over No of Students)")

            print("5.Show LineChart - Average marks per subject")
            print("6.Show LineChart - Average marks per school")

            print("7.Show BarChart - No of Students over Grades(A1,A2,B1...)")

            print("8.Show BarChart - Top 10 Students by Average Marks")
            print("9.Go Back")

            sdf = selectableData.get_df()

            inp = int(input("Please Choose an option[1-9]:"))
            if inp == 1:selectableData.show_selected_data()
            elif inp == 2:apply_filters()
            elif inp == 3:apply_sorting()
            elif inp == 4:
                printline()
                print("Showing Histogram")
                avg = sdf[SUBJECTS].mean(axis=1)

                plt.hist(avg, bins=10, edgecolor='black')
                plt.title("Distribution of Average Marks")
                plt.xlabel("Average Marks")
                plt.ylabel("No of Students")
                plt.show()

                saveOrContinue(plt)

            elif inp == 5:



                avg_per_subject = sdf[SUBJECTS].mean()
                plt.plot(avg_per_subject.index, avg_per_subject.values, marker="o")
                plt.title("Average Marks per Subject")
                plt.ylabel("Average Marks")
                plt.grid(True)
                plt.show()
                saveOrContinue(plt)
            elif inp == 6:
                schools = sdf[SCHOOL].unique()

                school_avg = []
                for school in schools:
                    school_rows = sdf[sdf[SCHOOL] == school]
                    avg = school_rows[SUBJECTS].mean(axis=1).mean()
                    school_avg.append(avg)

                plt.plot(schools, school_avg, marker='o')
                plt.title("Average Marks per School")
                plt.xlabel("School")
                plt.ylabel("Average Marks")
                plt.grid(True)
                plt.show()
                saveOrContinue(plt)
            elif inp == 7:
                bins = [0, 32, 40, 50, 60, 70, 80, 90, 100]
                labels = ["E", "D", "C2", "C1", "B2", "B1", "A2", "A1"]
                counts = {label: 0 for label in labels}
                for i in range(len(sdf)):
                    row = sdf.iloc[i]
                    avg = sum([row[sub] for sub in SUBJECTS]) / len(SUBJECTS)
                    for j in range(len(bins) - 1):
                        if bins[j] <= avg < bins[j + 1]:
                            grade = labels[j]
                            counts[grade] += 1
                            break
                        if avg == 100:
                            counts[labels[-1]] += 1
                            break
                plt.bar(counts.keys(), counts.values(), color="orange")
                plt.title("Number of Students per Grade")
                plt.xlabel("Grade")
                plt.ylabel("Number of Students")
                plt.show()
                saveOrContinue(plt)

            elif inp == 8:
                student_avg = []

                for i in range(len(sdf)):
                    row = sdf.iloc[i]
                    avg = sum([row[sub] for sub in SUBJECTS]) / len(SUBJECTS)
                    student_avg.append((row[NAME], avg,row[ROLL]))
                student_avg.sort(key=lambda x: x[1], reverse=True)

                top10 = student_avg[:10]

                names = [ str(each[0]).replace(" ", "\n")+'\n'+str(each[2])+''  for each in top10]
                averages = [each[1] for each in top10]


                plt.figure(figsize=(10, 5))
                plt.bar(names, averages, color="green")
                plt.title("Top 10 Students by Average Marks")
                plt.ylabel("Average Marks")
                plt.show()
                saveOrContinue(plt)








            else:return


    def view_data_menu():




        def export_selected_data():
            sdf = selectableData.get_df()
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
            print("2.Apply Filters")
            print("3.Apply Sorting")
            print("4.Export Selected Data")
            print("5.Show Data by Roll Number")
            print("6.Go Back")
            inp = int(input("Please Choose an option[1-5]:"))
            if inp == 1:
                selectableData.show_selected_data()
                wait4continue()
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
            inp = input("Are you Sure you want to DELETE this data??? [yes/no]")
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
