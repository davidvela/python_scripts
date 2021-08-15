#  get data: 
import pandas as pd 
df = pd.DataFrame({ 
    'Fname':['Harry','Sally','Paul','Abe','June','Mike','Tom'], 
    'Age':[21,34,42,18,24,80,22], 
    'Weight': [180, 130, 200, 140, 176, 142, 210], 
    'Gender':['M','F','M','M','F','M','M'], 
    'State':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
    'Children':[4,1,2,3,0,2,0],
    'Pets':[3,2,2,5,0,1,5] 
}) 
print (df) 



# VISUALIZATION: 
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 
# dataset = pandas.DataFrame(...)
# dataset = dataset.drop_duplicates()
# print(dataset)
# Paste or type your script code here:
import matplotlib.pyplot as plt 
dataset.plot(kind='scatter', x='Age', y='Weight', color='red')
plt.show() 
