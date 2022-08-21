import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    dataframe = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = dataframe['Year']
    y = dataframe['CSIRO Adjusted Sea Level']
    fig,ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    first_result = linregress(x,y)
    x_prediction = pd.Series([i for i in range(1880,2051)])
    y_prediction = first_result.slope*x_prediction + first_result.intercept
    plt.plot(x_prediction,y_prediction,"red")
    
    # Create second line of best fit
    df = dataframe.loc[dataframe['Year'] >= 2000]
    X = df['Year']
    Y = df['CSIRO Adjusted Sea Level']
    second_result = linregress(X,Y)
    new_x = pd.Series([i for i in range(2000,2051)])
    new_y = second_result.slope*new_x + second_result.intercept
    plt.plot(new_x,new_y,"green")
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level Predictor')
    ax.set_title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

print(draw_plot())