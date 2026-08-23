# Flight Delay Analysis & Prediction

## Project Overview

This project analyses flight delay patterns using historical flight data and develops a machine learning model to estimate the likelihood of an arrival delay of 15 minutes or more.

The project combines data cleaning, exploratory data analysis, statistical analysis, hypothesis testing, machine learning and an interactive Streamlit application.

## Business Problem

Flight delays can affect passengers, airline operations and scheduling decisions.

The aim of this project is to investigate the main patterns associated with flight delays and provide an interactive tool that can estimate delay risk using scheduled flight information.

## Objectives

- Analyse historical flight delay patterns.
- Compare delay rates between airlines.
- Investigate monthly delay patterns.
- Examine relationships between departure and arrival delays.
- Perform statistical and hypothesis testing.
- Develop a supervised machine learning model for delay prediction.
- Provide an interactive application for exploring results and estimating delay risk.

## Dataset

The project uses the 2018 flight dataset containing flight-level information such as airline, origin airport, destination airport, scheduled departure and arrival times, distance and delay-related variables.

The dataset was cleaned and prepared before analysis.

## Data Preparation

The ETL process included:

1. Loading the source dataset using Python and pandas.
2. Removing cancelled and diverted flights from the delay analysis.
3. Handling missing values in the target variable.
4. Creating a binary `Delayed` target based on `ArrDel15`.
5. Creating time-based features including month, day of week, departure hour and arrival hour.
6. Creating scheduled flight duration from scheduled departure and arrival times.
7. Selecting suitable variables for machine learning.

## Exploratory Data Analysis

The analysis investigates:

- Overall flight delay rates.
- Delay rates by airline.
- Monthly delay patterns.
- Arrival and departure delay statistics.
- Relationships between numerical delay variables.

Visualisations were created to support the analysis and communicate the findings clearly.

## Hypothesis Testing

### Research Question

Does departure delay have a statistically significant relationship with arrival delay?

### Null Hypothesis

There is no statistically significant relationship between departure delay and arrival delay.

### Alternative Hypothesis

There is a statistically significant relationship between departure delay and arrival delay.

A significance level of 0.05 was used to evaluate the result.

## Machine Learning

A supervised classification approach was used to predict whether a flight would experience an arrival delay of 15 minutes or more.

The main model used in the project is Logistic Regression.

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- ROC Curve

A train/test split was used to evaluate model performance on unseen data.

## Interactive Application

A Streamlit application was developed to provide:

- Overall flight delay metrics.
- Airline delay analysis.
- Monthly delay analysis.
- An interactive flight delay prediction tool.

Users can enter scheduled flight information and receive an estimated probability of arrival delay.

## Key Findings

The analysis found an overall flight delay rate of **19.48%** across the flights included in the analysis.

The airline comparison showed substantial variation in delay rates. **Commutair Aka Champlain Enterprises, Inc.** had the highest observed delay rate at **32.07%**, while **Cape Air** had the lowest observed delay rate at **8.94%**.

Monthly analysis also showed variation in delay frequency. **August (Month 8)** recorded the highest delay rate at **24.35%**, while **September (Month 9)** recorded the lowest at **16.65%**.

These results suggest that delay risk is not evenly distributed across airlines or months and that operational planning can benefit from understanding historical patterns.

## Recommendations

Based on the findings, airlines could use historical delay patterns to identify periods with higher operational risk and allocate resources accordingly.

The differences between airline delay rates also suggest that airline-level operational factors should be monitored when planning schedules and managing disruption risk.

The higher delay rate observed in August indicates that this period may require additional operational planning compared with lower-delay periods.

The prediction component can also be used as a supporting tool for identifying flights with a higher estimated delay risk and prioritising proactive communication or operational attention.

## Limitations

- The analysis is based on historical flight data from 2018.
- Historical patterns may not represent current operational conditions.
- The prediction model uses only the variables selected for this project.
- Model predictions should support, rather than replace, operational decision-making.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- PyArrow

## Project Structure

```text
DA-Capstone/
│
├── app/
├── data/
├── docs/
├── notebooks/
├── outputs/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```
