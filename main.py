import pandas as pd
from time_series_visualizer import draw_line_plot

# Read CSV and parse dates
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Sort by date to ensure line plot is correct
df = df.sort_index()

# Now plot
draw_line_plot(df)
