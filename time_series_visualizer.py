# time_series_visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def draw_line_plot(df):
    """Draws a line plot of page views over time."""
    plt.figure(figsize=(12,6))
    plt.plot(df.index, df['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.tight_layout()
    plt.show()

def draw_bar_plot(df):
    """Draws a bar plot of average monthly page views per year."""
    # Copy dataframe and extract year/month
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Create pivot table
    df_pivot = df_bar.groupby(['year','month'])['value'].mean().unstack()

    # Sort months correctly
    months_order = ['January','February','March','April','May','June',
                    'July','August','September','October','November','December']
    df_pivot = df_pivot[months_order]

    # Plot
    df_pivot.plot(kind='bar', figsize=(12,6))
    plt.title("Average Page Views per Month")
    plt.xlabel("Year")
    plt.ylabel("Average Page Views")
    plt.legend(title='Month')
    plt.tight_layout()
    plt.show()

def draw_box_plot(df):
    """Draws box plots for year-wise and month-wise distributions."""
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')  # Jan, Feb, etc.
    months_order = ['Jan','Feb','Mar','Apr','May','Jun',
                    'Jul','Aug','Sep','Oct','Nov','Dec']

    # Year-wise Box Plot
    plt.figure(figsize=(12,6))
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.show()

    # Month-wise Box Plot
    plt.figure(figsize=(12,6))
    sns.boxplot(x='month', y='value', data=df_box, order=months_order)
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    plt.show()
