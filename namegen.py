"""
Created on Fri Oct  3 15:43:39 2025

@author: anish
"""


import random
import time
import os



hindu_male_first_names = [
    "Aarav", "Aditya", "Aayush", "Aniket", "Ansh", "Anshul", "Abhishek", "Aman", "Akhil", "Amit",
    "Arjun", "Aryan", "Ashutosh", "Bhavesh", "Chirag", "Deepak", "Dheeraj", "Gaurav", "Harsh", "Himanshu",
    "Ishaan", "Jay", "Jatin", "Karan", "Kartik", "Krishna", "Lakshay", "Lalit", "Manav", "Manish",
    "Mayank", "Mohit", "Naman", "Nikhil", "Nilesh", "Niraj", "Pankaj", "Parth", "Pranav", "Prashant",
    "Raghav", "Rahul", "Raj", "Rajat", "Rakesh", "Ramesh", "Ravi", "Rishabh", "Ritesh", "Rohit",
    "Sachin", "Sagar", "Sandeep", "Sanjay", "Saurabh", "Shaurya", "Sharad", "Shivam", "Shrey", "Shubham",
    "Siddharth", "Sumit", "Sumeet", "Suraj", "Tanmay", "Tarun", "Uday", "Ujjwal", "Varun", "Vikas",
    "Vivek", "Yash", "Yuvraj", "Anirudh", "Bhanu", "Dilip", "Eshan", "Gautam", "Hemant", "Indrajit",
    "Jai", "Kunal", "Lokesh", "Mahesh", "Nikhilesh", "Omkar", "Prateek", "Rajnish", "Ranjit", "Saket",
    "Tejas", "Umesh", "Vikram", "Vipul", "Yatin", "Zubin", "Anand", "Bharat", "Chaitanya", "Devansh"
]
hindu_female_first_names = [
    "Aditi", "Ananya", "Anjali", "Anushka", "Bhavna", "Chitra", "Divya", "Esha", "Gayatri", "Hema",
    "Isha", "Jaya", "Kavya", "Kirti", "Lavanya", "Laxmi", "Madhuri", "Meera", "Neha", "Nisha",
    "Pooja", "Prachi", "Priya", "Radhika", "Rekha", "Sakshi", "Sandhya", "Sarika", "Seema", "Shalini",
    "Shruti", "Simran", "Smita", "Sneha", "Sonia", "Sunita", "Swati", "Tanya", "Usha", "Vandana"
]
muslim_male_first_names = [
    "Ahmed", "Ayaan", "Faizan", "Zaid", "Imran", "Salman", "Rehan", "Arman", "Bilal", "Danish",
    "Ehsan", "Farhan", "Hamza", "Hassan", "Irfan", "Junaid", "Khalid", "Luai", "Mansoor", "Naveed",
    "Omar", "Parvez", "Qasim", "Rafiq", "Saad", "Tariq", "Usman", "Yasir", "Zubair", "Azhar",
    "Basit", "Dawood", "Fahad", "Ghazanfar", "Hafiz", "Ilyas", "Javed", "Kashif", "Luqman", "Moeed",
    "Nadeem", "Owais", "Rashid", "Sami", "Talha", "Umair", "Waqar", "Yousuf", "Zain", "Adeel",
    "Bashir", "Dawood", "Faisal", "Ghaffar", "Haris", "Iqbal", "Jibran", "Kamran", "Latif", "Moin",
    "Noman", "Parvez", "Qadeer", "Riaz", "Sajid", "Taimoor", "Uzair", "Waseem", "Yaqoob", "Zahir",
    "Ahsan", "Babar", "Dawood", "Farooq", "Gulzar", "Hasan", "Iftikhar", "Jamal", "Khalil", "Mahmood",
    "Naseer", "Parvez", "Qamar", "Rashid", "Sarfaraz", "Talib", "Umar", "Wahid", "Yasir", "Zafar",
    "Asim", "Bilal", "Fawad", "Ghulam", "Haroon", "Irfan", "Junaid", "Kashif", "Latif", "Mansoor"
]
muslim_female_first_names = [
    "Aisha", "Fatima", "Zainab", "Amira", "Sara", "Noor", "Hina", "Sadia", "Sumaira", "Nida",
    "Rabia", "Bushra", "Amina", "Kiran", "Maryam", "Sana", "Shazia", "Huma", "Tasneem", "Nusrat",
    "Razia", "Asma", "Dilshad", "Fareeha", "Ghazal", "Hafsa", "Imrana", "Javeria", "Khadija", "Lubna",
    "Mahira", "Naila", "Parveen", "Qurat", "Rihana", "Saba", "Samina", "Tahira", "Wajiha", "Zehra"
]
hindu_surnames = [
    "Sharma", "Verma", "Pandey", "Choudhary", "Tiwari", "Mishra", "Joshi", "Tripathi", "Shukla", "Dubey",
    "Dwivedi", "Awasthi", "Rastogi", "Saxena", "Srivastava", "Bhardwaj", "Trivedi", "Jha", "Yadav", "Sinha",
    "Agrawal", "Goyal", "Jain", "Mahajan", "Gupta", "Bansal", "Malhotra", "Nair", "Chatterjee", "Mukherjee",
    "Bhattacharya", "Banerjee", "Chakraborty", "Dutta", "Sengupta", "Iyer", "Iyengar", "Nambiar", "Menon", "Rao",
    "Reddy", "Naidu", "Patel", "Desai", "Mehta", "Shah", "Thakur", "Rajput", "Solanki", "Chauhan"
]
muslim_surnames = [
    "Khan", "Ansari", "Syed", "Sheikh", "Qureshi", "Malik", "Chaudhry", "Farooqi", "Shaikh", "Abbasi",
    "Awan", "Hashmi", "Rizvi", "Naqvi", "Jafri", "Bukhari", "Siddiqui", "Mirza", "Hussain", "Alvi",
    "Mughal", "Niazi", "Shah", "Pathan", "Faruqi", "Aziz", "Khalil", "Imam", "Sayeed",
    "Khanam", "Mir", "Hakim", "Kazmi", "Lodhi", "Sarwar", "Chishti", "Gilani", "Bari", "Munshi",
    "Soomro", "Qadri", "Shahbaz", "Naqash", "Ansari", "Rana", "Baig", "Durrani", "Taimuri", "Zafar"
]
firstNames = {
    "Male":{"Hindu":hindu_male_first_names, "Muslim":muslim_male_first_names},
    "Female":{"Hindu":hindu_female_first_names, "Muslim":muslim_female_first_names}
    }
surnames = {
    "Hindu":hindu_surnames,
    "Muslim":muslim_surnames
    }
def generateName(gender,religion):
    fNameCandidates = firstNames[gender][religion]
    lNameCandidates = surnames[religion]
    return random.choice(fNameCandidates)+" "+random.choice(lNameCandidates)
    







