import pandas as pd
import matplotlib.pyplot as plt

#Constants
NAME = "Name"
ROLL = "RollNo"
GENDER = "Gender"
RELIGION = "Religion"
YEAR = "ExamYear"
SCHOOL = "SchoolName"
SUBJECTS = ["Maths","English","SST","Science","Hindi"]

#Variables
CSV_PATH = "adata/a_data_4.csv"
df,path = pd.read_csv(CSV_PATH),CSV_PATH
applied_filters = {

}
applied_sorting = NAME
applied_sorting_ascending = True


#Static Methods
def printline():
    print('\n\n')
    print("-"*25)

def wait4continue(pre_txt ='',
                  txt ="Press ENTER to continue..."):
    input(pre_txt + txt)

def saveOrContinue(plt):
    wait4continue()
    return



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
        colIndex = int(input
            ("Select [1-" + str(len(l)) + "]:")) - 1
        colLabel = l[colIndex]
        retval = colLabel
        break
    return retval

def elaborate(df):
    for i in range(len(df)):
        printline()
        for col in df.columns:
            print(col,":",df[col][i])
        printline()

def get_df():
    sdf = pd.DataFrame(df,copy=True)
    for key, value in applied_filters.items():
        if value is not None:
            if len(value) > 0:
                sdf = pd.concat([sdf[sdf[key] == val] for val in value])
    return sdf.sort_values(by=applied_sorting,
                           ascending=applied_sorting_ascending)



#Menu Options
def apply_filters():
    while True:
        printline()
        print("1.Select Column")
        print("Leave blank to Go Back")

        inp1 = input("Please Choose an option[1]:")

        if not inp1:
            break

        inp1 = int(inp1)

        selectedColumn = None
        if inp1 == 1:
            l = [ROLL, NAME]
            l.extend(SUBJECTS)
            selectedColumn = selectColumn(df, l)
        else:
            break
        while True:
            printline()
            print("Selected Column:" + selectedColumn)
            print("Currently applied filters:" +
                  str(str(applied_filters[selectedColumn])
                      if selectedColumn in applied_filters
                      else 'None'))
            print("1.Add filter")
            print("2.Clear all filters")
            print("Leave blank to Go Back")
            inp = input("Please Choose an option[1-2]:")

            print("Leave blank to Go Back")
            if not inp:
                break
            inp = int(inp)

            if inp == 1:
                print("Add filter")
                print("#Repeatedly Type FilterValue "
                      "and press Enter for the next value")
                print("#To apply the filter and go back "
                      "- Leave Blank and press Enter when finished")
                i = 0
                while True:
                    i += 1
                    filValue = input("Filter Value " + str(i) + ":")
                    if not filValue.strip():
                        break

                    if selectedColumn not in applied_filters:
                        applied_filters[selectedColumn] = []

                    applied_filters[selectedColumn].append(filValue)
                print("Filters Applied: ",
                      applied_filters[selectedColumn])
                wait4continue()
            elif inp == 2:
                applied_filters.pop(selectedColumn)
                wait4continue("All Filters Removed!")
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
            global applied_sorting_ascending
            applied_sorting_ascending = order == "A"
            break
        global  applied_sorting
        applied_sorting = selectedCol
        wait4continue("Sorting applied!")
        break

    return 0



def export_selected_data():
    sdf = get_df()
    try:
        printline()
        print("Exporting Selected Data:")
        print("Total Count:" + str(len(sdf)))
        print("Applied Filters:", applied_filters)
        print("Applied Sorting:" + applied_sorting)
        print("Sorting Order:" +
              ("Ascending"
               if applied_sorting_ascending else
               "Descending"))
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

def show_selected_data():
    sdf = get_df()
    printline()
    print("Showing Selected Data:")
    print("Total Count:" + str(len(sdf)))
    print("Applied Filters:", applied_filters)
    print("Applied Sorting:" + applied_sorting)
    print("Sorting Order:" +
          ("Ascending"
           if applied_sorting_ascending else
           "Descending"))
    printline()
    print(sdf.head(6))
    printline()
    wait4continue()
    return


#Menus
def home_menu():
    printline()
    while True:
        printline()
        print("HOME MENU Options:")
        print("1.View/Export Data")
        print("2.Visualize/Export Charts")
        print("3.Modify/Insert Data")
        print("4.Delete Data")
        print("5.Exit")

        inp = int(input("Please Choose an option[1-5]:"))
        if inp == 1: view_data_menu()
        elif inp == 2: visualize_data_menu()
        elif inp == 3: modify_data_menu()
        elif inp == 4: delete_data_menu()
        elif inp == 5: return

def view_data_menu():
    while True:
        printline()
        print("VIEW DATA MENU Options:")
        print("1.Show Selected Data")
        print("2.Apply Filters")
        print("3.Apply Sorting")
        print("4.Export Selected Data")
        print("5.Show Data by Roll Number")
        print("Leave blank to Go Back")

        inp = input("Please Choose an option[1-5]:")

        if not inp:
            break
        inp = int(inp)

        if inp == 1:
            show_selected_data()
            wait4continue()
        elif int(inp) == 2: apply_filters()
        elif int(inp) == 3: apply_sorting()
        elif int(inp) == 4: export_selected_data()
        elif int(inp) == 5: show_data_by_roll_num()
        else :return

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

        print("Leave Blank to Go Back")

        inp = input("Please Choose an option[1-9]:")
        if not inp:
            return
        inp = int(inp)

        sdf = get_df()

        if inp == 1:show_selected_data()
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
            plt.plot(avg_per_subject.index,
                     avg_per_subject.values, marker="o")
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

            names = [ str(each[0]).replace(" ", "\n")
                      +'\n'+str(each[2])+''  for each in top10]
            averages = [each[1] for each in top10]


            plt.figure(figsize=(10, 5))
            plt.bar(names, averages, color="green")
            plt.title("Top 10 Students by Average Marks")
            plt.ylabel("Average Marks")
            plt.show()
            saveOrContinue(plt)
        else:return

def modify_data_menu():#Requires saving data
    try:
        roll = int(input("Please enter the Roll Number to modify/insert:"))
        sdf = df[df[ROLL] == roll]
        for col in sdf.columns:
            if col == ROLL:
                continue
            print("Please type new "+col
                  +" and press ENTER, Or leave it blank to skip")
            inp = input("New "+col+":")
            if inp.strip():

                expectedType = sdf[col].dtype

                try:
                    if expectedType == type(98):inp = int(inp)
                    if expectedType == type(98.6):inp = float(inp)
                    if expectedType == type(True):inp = bool(inp)
                except:im = 9

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



#Running the code
home_menu()
df.to_csv(CSV_PATH, index=False)
print("Exiting...")