#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 17:49:05 2025

@author: truongvy
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Q1 - Find smallest N such that S = sum(i^3) > SL

SL = int(input("Enter the limit SL: "))
N = 0
S = 0

while S <= SL:
    N = N + 1
    S = S + N**3

print(f"Smallest N = {N}, S = {S}")

#%% Q2 - Education savings plan: how long to save $40,000

balance = 800
monthly_contribution = 120
target = 40000
months = 0
balance_history = [balance]

while balance < target:
    if balance < 10000:
        rate = 0.003
    elif balance < 20000:
        rate = 0.004
    elif balance < 30000:
        rate = 0.005
    else:
        rate = 0.006

    balance = balance + balance * rate + monthly_contribution
    months = months + 1
    balance_history.append(balance)

years = months // 12
remaining_months = months % 12
print(f"{years} years and {remaining_months} months to save $40,000")

plt.figure()
plt.plot(balance_history)
plt.axhline(y=target, color='red', linestyle='--', label='Target $40,000')
plt.title('Education Savings Plan')
plt.xlabel('Month')
plt.ylabel('Balance ($)')
plt.legend()
plt.grid(True)
plt.show()
