# Python Data Analysis

Python scripts for data analysis and simulation, written as part of 1008ENG (Programming and Computing for Engineers) at Griffith University.

## Files

### rainfall_analysis.py
Analysis of 24-hour rainfall data (mm) recorded at Southport, QLD across Jan–Dec 2006.

- Filters invalid readings (-9999)
- Finds maximum rainfall per month
- Calculates mean and standard deviation for any user-specified month
- Finds temperature sensor readings exceeding a threshold (nested loops)
- Visualises monthly average and maximum rainfall with bar charts

**Dataset:** `rainfall_southport_2006.txt`, `temp.dat`

---

### savings_plan.py
Simulates an education savings plan using a while loop.

- Finds smallest N such that sum of cubes exceeds a user-specified limit
- Calculates how long it takes to save $40,000 given a starting balance, monthly contributions, and tiered interest rates
- Plots balance growth over time

---

## Libraries Used
- `numpy`
- `matplotlib`

## How to Run
```bash
python rainfall_analysis.py
python savings_plan.py
```
