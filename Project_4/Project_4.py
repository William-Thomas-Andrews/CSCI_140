import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



def make_subset(df, region = None, vaccine = None, year = None):

    df_copy = df.copy()    # Makes a copy to manipulate

# Region filter
    if region != None:
        df_copy = df_copy.loc[df_copy['Region'].isin(region)]

# Vaccine filter
    if vaccine != None:
        df_copy = df_copy.loc[df_copy['Vaccine'].isin(vaccine)]

# Year filter
    if year != None:
        df_copy = df_copy.loc[df_copy['Year'].isin(year)]

    return df_copy     # Returns the result



def make_plot (series_object, title = '', bar = True):
    
    plt.title(title)   # Puts the title on the graph

    if bar == True:    # If barplot      
        return sns.barplot(y = series_object.index, x = series_object.values, orient = 'h' ).set_ylabel(series_object.index.name) # returns a barplot

    else:    # If lineplot
        plt.xticks(rotation=90)   
        return sns.lineplot(x = series_object.index, y = series_object.values).set_xlabel(series_object.index.name)  # returns a lineplot
