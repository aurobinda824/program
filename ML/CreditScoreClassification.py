import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os,random

os.chdir("E:\program\ML")
data = pd.read_csv("resources\data\CreditScore.csv")

'''data.info() shows the information about the coulmns'''
'''data.isnull().sum() shows if the dataset has any null values'''
'''data["Credit_Score"].value_counts()    credit score coulumn values'''

data['Credit_Mix'] = data['Credit_Mix'].map({"Standard":1, "Good":2, "Bad":0})
#data.boxplot(by='Credit_Score',column='Credit_Mix' )          for blox plots to check if a given column has any correlation wiht credit score
data['Credit_Score'] = data['Credit_Score'].map({'Standard':1, "Good":2, "Poor":0})

x = np.array(data[['Annual_Income','Monthly_Inhand_Salary','Num_Bank_Accounts','Num_Credit_Card','Interest_Rate','Num_of_Loan','Delay_from_due_date','Num_of_Delayed_Payment','Changed_Credit_Limit','Num_Credit_Inquiries','Outstanding_Debt','Credit_History_Age','Monthly_Balance']])
y = np.array(data['Credit_Score'])
random.shuffle(x)

x_train = x[0:int(len(x)* 0.9)]
x_test = x[int(len(x) * 0.9):]
y_train = y[0:int(len(y)*0.9)]
y_test = y[int(len(y)*0.9):]

