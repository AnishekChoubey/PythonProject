#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 16:02:57 2025

@author: anish
"""
import marksgen
import namegen
import numpy as np
import pandas as pd
import random


NAME = "Name"
ROLL = "RollNo"
GENDER = "Gender"
RELIGION = "Religion"
YEAR = "ExamYear"
SCHOOL = "SchoolName"

SUBJECTS = ["Maths","English","SST","Science","Hindi"]
SCHOOLS = ["Dehli Public",
           "Angels High",
           "Naman Vidya",
           "Saint Xavier",
           "DAV Public",
           "Vivekandanda Central"];
YEARS = 2021+np.arange(4)
averageStudentCountPerYear = 1000
maxDeltaStudentCount = 100



RELIGION_RATIO = {"Hindu":75,"Muslim":25} #whole number only because of genWeightedList function
GENDER_RATIO = {"Male":60,"Female":40} #same isme bhi


yearPlaceValue = 100000

ROLL_MIN = 10000
ROLL_MAX = 99999

yearNoise = random.randint(1000, 10000-YEARS.max())
def noisedYear(year):
    return year+yearNoise

def genWeightedList(dictionary):
    l = []
    for key,weightage in dictionary.items():
        l.extend([key]*weightage)
    return l
            
#print(genWeightedList(RELIGION_RATIO))


def generation_function(gen_seed):
    random.seed(gen_seed)
    students = []

    df = pd.DataFrame()

    for year in YEARS:
        deltaStudentCount = random.randint(-maxDeltaStudentCount, maxDeltaStudentCount)
        studentsThisYear = []
        for i in range(averageStudentCountPerYear - deltaStudentCount):
            # gender = "Male"
            gender = random.choice(genWeightedList(GENDER_RATIO))

            # religion = "Hindu"
            religion = random.choice(list(RELIGION_RATIO.keys()))
            religion = random.choice(genWeightedList(RELIGION_RATIO))
            school = random.choice(SCHOOLS)
            name = namegen.generateName(random, gender, religion)
            roll = 0  # todo
            student = {
                ROLL: roll,
                NAME: name,
                YEAR: year,
                GENDER: gender,
                RELIGION: religion,
                SCHOOL: school
            }

            # students.append(student)
            studentsThisYear.append(student)

        dfThisYear = pd.DataFrame(studentsThisYear)
        dfThisYear = dfThisYear.sort_values(by=NAME);
        dfThisYear = dfThisYear.reset_index(drop=True)
        for i in range(len(studentsThisYear)):
            dfThisYear.loc[i, ROLL] = (noisedYear(year) * (averageStudentCountPerYear + deltaStudentCount) * 10) + i
            students.append({
                ROLL: dfThisYear.loc[i, ROLL],
                NAME: dfThisYear.loc[i, NAME],
                YEAR: dfThisYear.loc[i, YEAR],
                GENDER: dfThisYear.loc[i, GENDER],
                RELIGION: dfThisYear.loc[i, RELIGION],
                SCHOOL: dfThisYear.loc[i, SCHOOL]

            })

        # df.append(dfThisYear)

        #print(dfThisYear)




    return marksgen.assign_marks(pd.DataFrame(students),SUBJECTS,random);
        # students.append(studentsThisYear)

#generating list with a name of choice

def findWithName(name):
    seed = 0
    while True:
        seed += 1
        print("Check " + str(seed))
        df = generation_function(seed)
        s = df.loc[:, NAME]
        result = s[s.str.startswith(name, na=False)]
        if len(result) > 0:
            return df,seed





#generating list with a name of choice
if __name__ == "__main__":
    df, seed = findWithName('Anishek Choubey')
    CSV_PATH = "adata/a_data_" + str(seed) + ".csv"
    df.to_csv(CSV_PATH, index=False)
    print(df)














