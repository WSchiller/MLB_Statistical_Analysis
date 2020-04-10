import pandas as pd
import matplotlib.pyplot as plt
import statistics
from numpy import std
import seaborn as sns


# Read in Ricky Henderson player data
df = pd.read_csv('Ricky_Henderson.csv')

# Print Year Runs, SB, and OBP columns
print("-----Ricky Henderson stats by season-----")
print(df[['Year', 'OBP', 'R', 'SB']])

# Get On Base Percentage
obp = df['OBP']

# Get and print avg/sum career stats
obp_avg = statistics.mean(obp)
runs = sum(df['R'])
sb = sum(df['SB'])

print(f"\n-----Ricky Henderson Career Stats-----\nOBP avg: {obp_avg}\nRuns: {runs}\nSB: {sb}\n", end='')

# Get standard deviation
sdev = std(obp)
sdev = round(sdev, 3)
print("Standard Deviation: " + str(sdev))
med = round(statistics.median(obp), 3)
print(f"Median OBP: {med}")

# Sort On Base Percentage
obp = sorted(obp, reverse=False)

# Number of season Ricky Henderson played
num_seasons = len(obp)

# Const Y-coordinates for dotplot
y_coord = [1] * num_seasons

# Dotplot and boxplot of Ricky Henderson's career OBP
sns.boxplot(x=obp)
plt.scatter(obp, y_coord, label='obp', color='g', s=25, marker="o")

# Remove y-axis ticks and label
plt.yticks([])

# Label x-axis
plt.xlabel('OBP')

# Give plot title
plt.title('Ricky Henderson\'s On Base Percentage by Season')

# Legend for obp
plt.legend()

# Display OBP dot plot
plt.show()

# Read in Tim Raines player data
dt = pd.read_csv('Tim_Raines.csv')

# Get On Base Percentage
obp = dt['OBP']

# Get and print avg/sum career stats
obp_avg = statistics.mean(obp)
runs = sum(dt['R'])
sb = sum(dt['SB'])

print(f"\n-----Tim Raines-----\nOBP avg: {obp_avg}\nRuns: {runs}\nSB: {sb}\n", end='')

# Calculate standard deviation
sdev = std(obp)
sdev = round(sdev, 3)
print("Standard Deviation: " + str(sdev))
med = round(statistics.median(obp), 3)
print(f"Median OBP: {med}")


# Sort On Base Percentage
obp = sorted(obp, reverse=False)

# Number of season Tim Raines played
num_seasons = len(obp)

# Const Y-coordinates for dotplot
y_coord = [1] * num_seasons

# Dotplot and boxplot of Tim Raine's career OBP
sns.boxplot(x=obp)
plt.scatter(obp, y_coord, label='obp', color='c', s=25, marker="o")

# Remove y-axis ticks and label
plt.yticks([])

# Label x-axis
plt.xlabel('OBP')

# Give plot title
plt.title('Tim Raines On Base Percentage by Season')

# Legend for obp
plt.legend()

# Display OBP dot plot
plt.show()














