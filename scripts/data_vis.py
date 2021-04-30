#!/usr/bin/python
import sys
import pandas as pd 
import configparser

import matplotlib.pyplot as plt
import pandas
import numpy as np
from pandas.plotting import scatter_matrix

path = "../../../__data/"
config_file = "_config.ini"

# config = configparser.ConfigParser()
# config.read(path + config_file)
# print( config["topsecret.server.com"]['Port'])
dataset_final = ""

def main():
    print("Hello, World!")
    ds_wine = pd.read_csv(path + "winequality-red.csv",sep=';')
    # ds_wine.head(10)
    ds_wine.describe()
    # dataset_csv['alcohol'].describe()
    # ds_wine[ds_wine['alcohol'] > 11.0]
    # ds_wine[ds_wine['alcohol'] > 11.0].count()
    ds_wine[ds_wine['alcohol'] > 11.0].describe()
    # ds_wine[ds_wine['job'] > "Sales"].describe()
    global dataset_final
    dataset_final = ds_wine[['alcohol','chlorides','quality']]

def visualize():
    scatter_matrix(dataset_final)
    plt.show()

def test_matplotlib():
    # Prepare the data
    x = np.linspace(0, 10, 100)
    # Plot the data
    plt.plot(x, x, label='linear')
    # Add a legend
    plt.legend()
    # Show the plot
    plt.show()   

def test_sns():
    from string import ascii_letters
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(style="white")

    # Compute the correlation matrix
    corr = dataset.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

##########################################################################
##########################################################################
# $ python test.py arg1 arg2 arg3
if __name__== "__main__" :
    main()
    # print( 'Number of arguments:' + str(len(sys.argv)) + ' arguments.' )
    # print ( 'Argument List:' + str(sys.argv) )