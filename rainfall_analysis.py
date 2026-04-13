#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 12:54:23 2025

@author: truongvy
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('rainfall_southport_2006.txt')

# Replace -9999 with nan to ignore invalid readings
data = data.astype(float)
data[data == -9999] = np.nan

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#%% Q1 - Maximum rainfall

# (i) Maximum rainfall in January
january = data[:, 0]
max_jan = np.nanmax(january)
print(f"Maximum rainfall in January: {max_jan} mm")

# (ii) Maximum rainfall in each month
print("\nMaximum rainfall per month:")
for i in range(12):
    monthly_data = data[:, i]
    max_val = np.nanmax(monthly_data)
    print(f"  {months[i]}: {max_val} mm")

#%% Q2 - Mean and standard deviation for a user-specified month

month_num = int(input("\nEnter month number (1=Jan, 2=Feb, ..., 12=Dec): "))
month_data = data[:, month_num - 1]
valid_data = month_data[~np.isnan(month_data)]

n = len(valid_data)
mean = np.sum(valid_data) / n
std = np.sqrt(np.sum((valid_data - mean) ** 2) / (n - 1))

print(f"\n{months[month_num - 1]} rainfall statistics:")
print(f"  Mean:               {mean:.2f} mm")
print(f"  Standard deviation: {std:.2f} mm")

#%% Q3 - Temperature readings greater than 85.0 degrees

temp_data = np.loadtxt('temp.dat')
print("\nTemperature readings greater than 85.0°C:")
print(f"{'Hour':<6} {'Sensor':<8} {'Temp (°C)'}")
print("-" * 25)

for i in range(len(temp_data)):
    hour = int(temp_data[i, 0])
    for j in range(1, temp_data.shape[1]):
        if temp_data[i, j] > 85.0:
            print(f"  {hour:<6} {j:<8} {temp_data[i, j]}")

#%% Visualisation - Monthly rainfall summary

monthly_means = []
monthly_max = []

for i in range(12):
    col = data[:, i]
    monthly_means.append(np.nanmean(col))
    monthly_max.append(np.nanmax(col))

x = np.arange(12)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(x, monthly_means, color='steelblue')
axes[0].set_title('Average Daily Rainfall by Month (2006)')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Mean Rainfall (mm)')
axes[0].set_xticks(x)
axes[0].set_xticklabels(months)
axes[0].grid(axis='y', alpha=0.3)

axes[1].bar(x, monthly_max, color='coral')
axes[1].set_title('Maximum Daily Rainfall by Month (2006)')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Max Rainfall (mm)')
axes[1].set_xticks(x)
axes[1].set_xticklabels(months)
axes[1].grid(axis='y', alpha=0.3)

plt.suptitle('Southport Rainfall Analysis 2006')
plt.tight_layout()
plt.show()
