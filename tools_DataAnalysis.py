import numpy as n
from matplotlib import pyplot as plt
import pandas as pd

#---------------set display options
pd.set_option('display.width', 100)
pd.set_option('precision',3)

#---------------General Functions ---------------------------------

#returns a dataFrame of a dataset provided via URL
def readCSV(url,names):
    data=pd.read_csv(url,names=names)
    print(data.shape)
    return data

def YNvalidation():
    while True:
        data = input("Would you like to continue? (Y/N)")
        if data.lower() not in ('Y', 'N', 'y', 'n'):
            print('Please input a valid response (Y - for yes or N - for No)')
        else:
            break
    return data

def CorrValidation():
    while True:
        data = input("What type of correlation test would you like to run? (pearson, kendall, spearman)")
        if data.lower() not in ('pearson', 'kendall', 'spearman'):
            print('Please input a valid response (pearson, kendall, spearman)')
        else:
            break
    return data

def integerValidation(inputText):
    while True:
        try:
            number = int(input(inputText))
        except ValueError:
                print("Please enter a valid integer")
                #better try again... Return to the start of the loop
                continue
        else:
            return number
            break


#---------------Data Analysis Functions ----------------------------

#prints a sneek peek of the data with limited number of rows
def sneekPeek(dataFrame, numRows):
    print('---------------Data Snippet Output as Follows ------------------')
    peek=dataFrame.head(numRows)
    print(peek)
#prints a datasets descriptive statistics
def DescriptiveStats(dataFrame):
    print('------------DataFrame DescriptiveStatistics are as Follows:----------')
    description=dataFrame.describe()
    print(description)
#count by class
def classCount(dataFrame,column):
    class_counts = dataFrame.groupby(column).size()
    print('-------------class counts are as follows:-----------------')
    print(class_counts)
#examine data correlations. method : {‘pearson’, ‘kendall’, ‘spearman’}
        # pearson : standard correlation coefficient
        # kendall : Kendall Tau correlation coefficient
        # spearman : Spearman rank correlation
def correlation(dataFrame, method):
    df_return = dataFrame.corr(method=method)
    print('-----------------correlation data ('+str(method)+' method) output as follows:-------------')
    print(df_return)
def skew(dataFrame):
    return_df = dataFrame.skew()
    print('--------------skew data output as follows:----------------')
    print(return_df)
def DataSummary(dataFrame):
    columns = dataFrame.columns
    print('Dataframe dimensions are as follows (rows, columns): '+str(dataFrame.shape))
    print('DataFrame Columns are as follows: '+ str(columns))
    #------------Sneek Peek Rows ----------------------
    numRows=integerValidation('How many rows would you like to examine? (Row Total = ' + str(len(dataFrame))+')')
    sneekPeek(dataFrame,numRows)
    #----------Class Counts ---------------------------
    while True:
        YN = input("Would you like to get a column class count? (Y/N)")
        if YN not in ('Y', 'N','y','n'):
            print("Please input a valid response (Y - for yes or N - for No)")
        elif YN in ('Y','y'):
            while YN in ('Y','y'):
                column = input('What column would you like a classcount for? Recall Columns: '+ str(columns))
                classCount(dataFrame,column)
                YN=YNvalidation()
            break
        else:
            break
    #----------DescriptiveStats-----------------------
    while True:
        YN = input("Would you like to run descriptive statistics? (Y/N)")
        if YN not in ('Y', 'N','y','n'):
            print("Please input a valid response (Y - for yes or N - for No)")
        elif YN in ('Y','y'):
            DescriptiveStats(dataFrame)
            break
        else:
            break
    #----------Correlation --------------------------
    while True:
        YN = input("Would you like to run data correlation? (Y/N)")
        if YN not in ('Y', 'N','y','n'):
            print("Please input a valid response (Y - for yes or N - for No)")
        elif YN in ('Y','y'):
            method=CorrValidation()
            correlation(dataFrame,method)
            break
        else:
            break
    #---------Skew Value ---------------------------
    while True:
        YN = input("Would you like to run data skew analysis? (Y/N)")
        if YN not in ('Y', 'N','y','n'):
            print("Please input a valid response (Y - for yes or N - for No)")
        elif YN in ('Y','y'):
            skew(dataFrame)
            break
        else:
            break
    print('-----------Data Summary Script Complete-------------')
#---------------Data Analysis Functions ----------------------------
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
names = ['age', 'sex', 'cp', 'testbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang','oldpeak','slope','ca','thal','num']
data=readCSV(url,names)

#DataSummary(data)

data.hist()
data.plot(kind='density',subplots=True, layout=(7,2),sharex=False)
plt.show()
