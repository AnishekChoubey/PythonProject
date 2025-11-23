import pandas as pd
import numpy as np
import random
import datagen



SUBJECTS = ["Maths","English","SST","Science","Hindi"]

REQUIRED_SIZE = 100

MAX_DELTA_MARKS = 8
MIN_DELTA_MARKS = 5

# Number of students scoring within each 10-mark interval
# Intervals 0–10, 11–20, 21–30, 31–40, 41–50, 51–60, 61–70, 71–80, 81–90, 91–100
AVERAGE_DISTRIBUTION = [0, 0, 0, 3, 7, 15, 23, 27, 18, 7]



def gen_marks(rnd,average,subjects_count = 5):
    marks = []
    current_student_max_delta_marks =   int(rnd.randint(MIN_DELTA_MARKS,MAX_DELTA_MARKS)/2)# int(rnd.randint(MIN_DELTA_MARKS,min(MAX_DELTA_MARKS,100-average))/2)
    for subject in range(subjects_count):
        while True:
            deltaMarks = rnd.randint(0, current_student_max_delta_marks)
            deltaMarks *= -1 if rnd.randint(0, 1) == 0 else 1
            if deltaMarks + average > 100:
                deltaMarks = 100-average - rnd.randint(0, MIN_DELTA_MARKS)+1
            if (deltaMarks not in marks) or random.randint(0, 4) == 3:
                marks.append(deltaMarks)
                break
    return np.array(marks)+average

def generate_averages(rnd,num_students, distribution):
    total_dist = sum(distribution)
    if total_dist == 0:
        raise ValueError("Distribution all zeros")
    scale_factor = num_students / total_dist
    scaled_bins = [round(x * scale_factor) for x in distribution]
    diff = num_students - sum(scaled_bins)
    if diff != 0:
        max_idx = scaled_bins.index(max(scaled_bins))
        scaled_bins[max_idx] += diff
    marks = []
    for i, count in enumerate(scaled_bins):
        low = i * 10
        high = min(low + 10, 100)
        for _ in range(count):
            marks.append(rnd.randint(low, high))

    random.shuffle(marks)
    return marks


def assign_marks(df,subjects,rnd = random):
    all_schools_df = []
    schools = {t: school_df.copy() for t, school_df in df.groupby(datagen.SCHOOL)}
    for school_name, sdf in schools.items():
        averages = generate_averages(rnd, len(sdf), AVERAGE_DISTRIBUTION)
        rows = [gen_marks(rnd, avg, len(subjects)) for avg in averages]
        mdf = pd.DataFrame(rows, columns=subjects)
        combined_df = pd.concat([sdf.reset_index(drop=True), mdf], axis=1)
        all_schools_df.append(combined_df)
    final_df = pd.concat(all_schools_df, ignore_index=True)
    return final_df








#print(generate_averages(random,100,AVERAGE_DISTRIBUTION))
#print(gen_marks(random,88))

