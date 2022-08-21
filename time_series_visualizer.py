import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates = ['date'])

# set index column to 'date'
df = df.set_index('date')

# Clean the data by filtering out days when the page views were in the top 2.5% of 
# the dataset or bottom 2.5% of the dataset.
df=df.drop(df[(df['value']<df['value'].quantile(0.025)) | (df['value']>df['value'].quantile(0.975))].index)

def draw_line_plot():
    new_query = df.query("date >= '2016-05-09' & date <= '2019-12-03'")
    # Draw line plot
    fig = sns.lineplot(data=new_query,x="date",y="value")
    fig.set_xlabel("Date")
    fig.set_ylabel("Page Views")
    fig.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Save image and return fig (don't change this part)
    fig.figure.savefig('lineplot.png')
    return fig


def draw_bar_plot():
    df_bar = df.copy()
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()
    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                 'August', 'September', 'October', 'November', 'December']
    # Draw bar plot
    fig = df_bar.plot(kind= 'bar', figsize = (15,10)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page View")
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = sns.boxplot(x = "year", y ="value", data=df_box)

    # Save image and return fig (don't change this part)
    fig.figure.savefig('box_plot.png')
    return fig


print(draw_line_plot())
print(draw_bar_plot())
print(draw_box_plot())