#Do not change any of the import lines
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Project_4 import *


#Part 1: Data QC
#Do not change the order of lines
#Maintain the original structures (if there is a lambda, use a lambda etc)
#You can copy and paste in the line
#vaccine.head()
#or from the command line
#print(vaccine.head())
#to view the data frame
#comment these lines out before you turn in your project

##Read in the data
vaccine = pd.read_csv('vaccine_data.csv')

##Assign column names
vaccine = pd.read_csv('vaccine_data.csv', names = ['Region', 'Vaccine', 'Year', 'Percentage'])

##Update region names to replace & with and and remove spaces
vaccine['Region'] = vaccine['Region'].str.replace('&','and').str.replace(' ','_')

##Change type of Year column to a string
vaccine['Year']  = vaccine['Year'].astype('str')
# print(vaccine['Year'].dtypes)

##Create description column
## The mapping variable and its values are correct, please do not change this line
mappings = {'BCG':'tuberculosis', 'DTP1':'diphteria_pertussis_tetanus','DTP3': 'diptheria_pertussis_tetanus',\
'MCV1':'meningococcal_disease','MCV2':'meningococcal_disease','HEPBB':'hepatitis B', 'HEPB3':'hepatitis B',\
'HIB1':'Haeomphilus influenza', 'HIB3':'Haemophilus influenza','IPV1': 'polio','IPV3': 'polio', 'POL3': 'polio','PCV3':'pneumococcal disease', 'RCV1':'rubella',\
'ROTAC':'rotavirus','YFV':'Yellow Fever Virus'}
vaccine['Description'] = vaccine['Vaccine'].map(mappings)



# start changing from here again
##Check the data frame before continuing
# print(vaccine)



##Create a data frame called BCG_2019 that contains the rows for BCG vaccine for 2019
BCG_2019 = make_subset(vaccine, vaccine = ['BCG'], year = ['2019'])



##From the data frame you made, create a Series called BCG2019_Series with Region as the index and Percentage as the values
BCG2019_Series = pd.Series(BCG_2019['Percentage'].tolist(), index = BCG_2019['Region'].tolist())  



##Create a barplot for the percentage outreach (Percentage) of BCG vaccine by region in 2019.
make_plot(BCG2019_Series)



##Create a data frame called DPT1_Years that contains the rows for DTP1 vaccinations in the East Asia and Pacific region
DTP1_Years = make_subset(vaccine, region = ['East_Asia_and_Pacific'], vaccine = ['DTP1'])  



##From the data frame you made, create a Series called DTP1_series that has Year as the index and Percentage as the values  
DTP1_series = pd.Series(DTP1_Years['Percentage'].tolist(), index = DTP1_Years['Year'].tolist())   



##Create a line plot of the data stored in DTP1_series with the title: DTP1 Vaccinations by Year in East Asia and Pacific Region
make_plot(DTP1_series, title = 'DTP1 Vaccinations by Year in East Asia and Pacific Region', bar = False)
# plt.show()
