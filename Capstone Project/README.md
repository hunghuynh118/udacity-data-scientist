# Starbucks Capstone Project

## Project Overview

This project contains data set simulating customer behavior on the Starbucks rewards mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Some users might not receive any offer during certain weeks.

Not all users receive the same offer, and that is the challenge to solve with this data set.

My task is to combine transaction, demographic and offer data to determine which demographic groups respond best to which offer type. This data set is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products.

## Project Statement

In this project, I need to clean the data set first, then combine them together to answer two business questions:

- Which demographic groups response best to which offer type.
- Whether a customer will complete an offer after viewing it.

## Installations

This project was written in Python, using Jupyter Notebook on Anaconda. The relevant Python packages for this project are as follows:

- pandas
- numpy
- itertools
- matplotlib
- seaborn >= 0.9.0
- sklearn

## File Descriptions

This repo contains 7 files:

- `Starbucks_Capstone_notebook.ipynb`: the notebook file containing all code
- `Starbucks_Capstone_notebook.html`: html version of the notebook file
- `README.md`: this file introduces overall the project
- `master.csv`: the cleaned dataset merged from 3 other datasets
- `data\portfolio.json`: json file containing offer data
- `data\profile.json`: json file containing user data
- `data\transcript.json`: json file containing record log data

## Links for Project:

- Code repository on Github could be found [here](https://github.com/hunghuynh118/udacity-data-scientist/tree/main/Capstone%20Project).

- Blog post report on Medium could be found [here](https://medium.com/@hunghuynh.11899/does-the-starbucks-offers-target-a-specific-customer-group-8cf71d420c22).

## Licensing, Authors, Acknowledgements

Data for this project was provided by Udacity.
