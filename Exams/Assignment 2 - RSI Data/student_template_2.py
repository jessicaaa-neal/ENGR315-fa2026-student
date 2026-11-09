"""
CULMINATING ASSIGNMENT 2: RSI

Create a program which will provide answers to the tasks posed in the assignment description.

For this assignment, you will start from scratch with this blank template.
It is your reponsibility to include all necessary program components in this file.
Your code needs to be successful as well as sufficiently commented/documented to receive full credit.

The relevant data file is named "all_participant_data_rsi.csv" and is located in data > drop-jump.

All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""

# Task 1: Paired T-Test
print("Task 1: Paired T-Test")

# Import pandas to read csv
import pandas as pd

# Load a csv
data=pd.read_csv("../../data/drop-jump/all_participant_data_rsi.csv")

# Print data to ensure it is loaded
print(data.columns)
print()

# Select all force plate measurements
force_plate = data["force_plate_rsi"]

# Select all acceerometer measurements
accelerometer = data["accelerometer_rsi"]

# import functions from scipy
from scipy import stats

# Set level of significance
alpha = 0.05

# Perform a paired t-test comparing the two measurement methods
t_stat, p_value = stats.ttest_rel(force_plate, accelerometer)

# Print the reslts of the paired t-test
print("T-statistic:", t_stat)
print("P-value:", p_value)
print()

# Print the null and alternative hypothesis
print("H0: The mean difference between force plate and accelerometer RSI is zero.")
print("H1: The mean difference between force plate and accelerometer RSI is non-zero.")
print()

# Compare the p-value to the level of significance
if p_value < alpha:
    print("Reject the null hypothesis.")
    print("There is a significant difference between the two methods.")
else:
    print("Fail to reject the null hypothesis")
    print("There is not enough evidence of a significant difference") 

print()

# Task 2: Normal Distribution and Chi2 Goodness of Fit Test
print("Task 2: Normal Distribution and Chi2 Goodness of Fit Test")

# Import Numpy
import numpy as np

# Import normal distribution
from scipy.stats import norm

# Import matplotlib to make graphs
import matplotlib.pyplot as plt

# Fit a normal distribution to the accelerometer data
mean, std_dev = norm.fit(accelerometer)

# Print mean and standard deviation
print ("Mean:", mean)
print ("Standard Deviation:", std_dev)
print ()

# Create x-values accross the accelerometer range
X = np.linspace(accelerometer.min(), accelerometer.max(),200)

# Calculate the normal distribution curve using fitted parameters
normal_curve = norm.pdf(X, mean, std_dev)

# Plot a Histogram
plt.hist(accelerometer, bins=10, density=True, alpha=0.6, label= "Accelerometer Data")

# Plot the fitted normal distribution curve on the histogram
plt.plot(X, normal_curve, label="Fitted Normal Distribution Curve")

# Add chart elements
plt.title ("Accelerometer Normal Distribution Fit")
plt.xlabel("Accelerometer RSI")
plt.ylabel("Probability Density")
plt.legend()

# Display histogram
plt.show()

# Calculate observed frequency using histogram
observed, bin_edges = np.histogram(accelerometer, bins=10)

# Calculate expected frquency using fitted distribution
expected = len(accelerometer)* np.diff(norm.cdf(bin_edges,mean, std_dev))

# Include probability below the smallest value in first bin
expected [0] += len(accelerometer)*norm.cdf(bin_edges[0], mean, std_dev)

# Include probability above the largest value in last bin
expected [-1] += len(accelerometer)*norm.sf(bin_edges[-1], mean, std_dev)

# Print both frequencies
print ("Original Frequencies (10 bins):")
print("Observed frequencies:", observed)
print ("Expected Frequencies:", expected)
print()

# Check if expected frequencies are <5
print ("Checking expected frequencies")
print ("Smallest expected frequency:", expected.min())
print()

# Check if the last expected frequency is below 5
if expected[-1] < 5:
    
    # Explain why the bins are being combined
    print("Last expected frequency is below 5. Combining the last two bins.")

    # Combine the last two bins
    observed[-2] = observed[-2] + observed[-1]
    expected[-2] = expected[-2] + expected[-1]

    # Remove the last bin since it was combined
    observed = observed[:-1]
    expected = expected[:-1]

# Print updated frequencies
print(f"Final Frequencies ({len(observed)} Bins):")
print ("Final observed frequency:", observed)
print ("Final expected frequency:", expected)
print()

# Calculate the degrees of freedom
degrees_freedom = len(observed)-3

# Perform the Chi2 goodness of fit test
chi2_stat, chi2_p = stats.chisquare(observed, expected, ddof=2)

# Print Results
print ("Chi2 Statistic:", chi2_stat)
print ("P-value:", chi2_p)
print ("Degrees of freedom:", degrees_freedom)
print()

# Print the null and alternative hypotheses
print("H0: The accelerometer data follows a normal distribution.")
print("H1: The accelerometer data does not follow a normal distribution.")
print()

# See if the normal distribution is a good fit
if chi2_p < alpha:
    print("Reject the null hypothesis")
    print("The normal distribution is not a good fit for the accelerometer data.")
else:
    print("Fail to reject the null hypothesis")
    print("The normal distribution is a reasonable fit for the accelerometer data")

print()

# Task 3: Participant F and 95% Confidence Intervals
print("Task 3: Participant F and 95% Confidence Intervals")

# Choose only Participant F's trials
participant_f = data[data["trial"].str.startswith("F")]

# Display all columns in DataFrame
pd.set_option("display.max_columns", None)

# Print Participant F's data
print("Participant F Data:")
print(participant_f)
print()

# Choose Participant F's force plate values
f_force_plate = participant_f["force_plate_rsi"]

# Choose Participant F's accelerometer values
f_accelerometer = participant_f["accelerometer_rsi"]

# Set Confidence Level
confidence = 0.95

# Calculate sample sizes
n_force = len(f_force_plate)
n_accel = len(f_accelerometer)

# Calculate confidence interval for force plate
force_ci = stats.t.interval(
    confidence,
    df=n_force-1,
    loc=f_force_plate.mean(),
    scale=stats.sem(f_force_plate)
)

# Calculate confidence interval for accelerometer
accel_ci = stats.t.interval(
    confidence,
    df=n_accel-1,
    loc=f_accelerometer.mean(),
    scale=stats.sem(f_accelerometer)
)

# Print the force plate mean and confidence interval
print("Participant F Force Plate RSI:")
print("Mean:", f_force_plate.mean())
print("95% Confidence Interval:", force_ci)
print()

# Print the accelerometer mean and confidence interval
print("Participant F Accelerometer RSI:")
print("Mean:", f_accelerometer.mean())
print("95% Confidence Interval:", accel_ci)
print()