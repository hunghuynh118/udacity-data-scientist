import sys
import pandas as pd
import joblib
from sqlalchemy import create_engine
import nltk
nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier


def load_data(database_filepath):
    """Load data from sqlite database

    Args:
        database_filepath (string): database filepath

    Returns:
        X (dataframe): message data
        Y (dataframe): categories data
    """
    # create engine connecting to database then load the dataset
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql_table('DisasterResponse', engine)

    # create message data and categories data
    category_names = list(df.columns[4:].values)
    X = df.message
    Y = df[category_names]

    return X, Y


def tokenize(text):
    """Preprocess text: tokenize, lemmatize and normalize

    Args:
        text (string): a sentence or paragraph

    Returns:
        list of string: cleaned tokens
    """
    # tokenize text
    tokens = word_tokenize(text)

    # lemmatize and normalize tokens
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """Build a machine learning pipeline to take the message as input 
        and output classification results on 36 categories

    Returns:
        model: a machine learning model
    """
    # build pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(estimator=RandomForestClassifier()))
    ])

    # parameters used in grid search cv to find better parameter
    parameters = {
        'clf__estimator__n_estimators' : [10, 20, 50]
    }

    # create grid search model
    cv = GridSearchCV(pipeline, param_grid=parameters)
    
    return cv


def evaluate_model(model, X_test, Y_test):
    """Evaluate the model and display scores to screen

    Args:
        model (model): a machine learning model
        X_test (dataframe): test message data
        Y_test (dataframe): test categories data
    """
    # predict X_test
    Y_pred = model.predict(X_test)

    # show the precision, recall and f1-score of each category
    for index, column in enumerate(Y_test):
        print('*' * 50 + '\nColumn: ' + column)
        print(classification_report(Y_test[column], Y_pred[:, index]))


def save_model(model, model_filepath):
    """Export model as a pickle file

    Args:
        model (model): a machine learning model
        model_filepath (string): filepath to export model
    """
    joblib.dump(model, open(model_filepath, 'wb'), compress=3)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()