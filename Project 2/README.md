# Disaster Response Pipeline Project

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Go to `app` directory: `cd app`

3. Run your web app: `python run.py`

4. Click the `PREVIEW` button to open the homepage

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

You should install Python 3 and some following packages:

- pandas
- sqlalchemy
- nltk
- sklearn
- plotly
- flask

## Project Motivation<a name="motivation"></a>

In this project, I apply data engineering skills to analyze disaster data from [Appen](https://appen.com/) (formally Figure 8) to build a model for an API that classifies disaster messages.

The data set containing real messages that were sent during disaster events. I created a machine learning pipeline to categorize these events so that I can send the messages to an appropriate disaster relief agency.

I also created a web app where an emergency worker can input a new message and get classification results in several categories. The web app also display visualizations of the data.

![webapp](./images/webapp.png)

![plot1](./images/plot1.png)

![plot2](./images/plot2.png)

![plot3](./images/plot3.png)

## File Descriptions <a name="files"></a>

- :open_file_folder: app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@hunghuynh.11899/what-to-consider-while-buying-an-used-car-c05c47d643d8).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/datasets/thedevastator/uncovering-factors-that-affect-used-car-prices). Otherwise, feel free to use the code here as you would like!
