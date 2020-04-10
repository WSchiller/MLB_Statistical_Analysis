import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Read in Derek Jeter career playing data
df = pd.read_csv('Derek_Jeter.csv')

# Print career info by season and home runs per season
print("-----Derek Jeter Home Run Totals by Season-----")
print(df[['Year', 'HR']])

# Store year and home run data
year = df['Year']
home_run = df['HR']

# Get number of seasons played. Excluding seasons with less than 100 plate appearances
seasons_played = len(year)

# Sort home run totals in increasing order
home_run = sorted(home_run, reverse=False)

# Calculate y coordinates for dotplot.
y_coord = []
hr_count = 1
for hr in range(0, seasons_played - 1):
    if home_run[hr] == home_run[hr + 1]:  # Duplicate home run total.  Increase y-axis by .1 for plotting.
        y_coord.append(hr_count + .1)
        hr_count += .1
    else:
        hr_count = 1
        y_coord.append(hr_count)
y_coord.append(1)

# Display home runs per season by dot plot
plt.ylim(0, 4)
plt.scatter(home_run, y_coord, label='HR', color='b', s=25, marker="o")
plt.xlabel('Home Runs')
plt.xticks(range(0, 25, 5))
plt.yticks([])
plt.title('Derek Jeter\'s Home Run Totals per Season')
plt.legend()
plt.show()

# ----Linear Regression----

# Define data.
# Input regressors - year(x)
# Output predictor - home runs(y)
home_run = df['HR']
x = np.array(year).reshape((-1, 1))
y = np.array(home_run)

# Create model and fit it
model = LinearRegression().fit(x, y)

# Get results
r_sq = model.score(x, y)
print('coefficient of determination: ', r_sq)
print('intercept: ', model.intercept_)
print('slope:', model.coef_)
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

# Print scatter plot with regression line
plt.xlabel('Year')
plt.ylabel('HR')
plt.scatter(x, y, color='blue')
plt.plot(x, y_pred, color='red', linewidth=2)
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(min(y), max(y)+1, 2.0))
plt.show()
