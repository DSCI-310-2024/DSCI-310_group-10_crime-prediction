from sklearn.model_selection import train_test_split, cross_validate
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
import pandas as pd
import click

@click.command()
@click.argument('input_path', type=str)
@click.argument('output_path', type=str)
def analysis(input_path, output_path):
    # Read data from the input path
    data = pd.read_csv(input_path)

    X = data.drop(columns=['if_crime'])
    y = data['if_crime']

    perform_analysis(X, y, output_path)

def perform_analysis(X, y, output_path):

    # Perform one-hot encoding with sparse representation
    X_encoded = pd.get_dummies(X, sparse=True)
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=123)  
    
    # Initialize classifiers
    dummy = DummyClassifier()
    lr = LogisticRegression()
    
    # Fit the classifiers
    dummy.fit(X_train, y_train)
    lr.fit(X_train, y_train)
    
    # Evaluate the classifier
    #dummy_results = pd.DataFrame([dummy.score(X_test, y_test)])
    dummy_score = dummy.score(X_test, y_test)  
    dummy_results = pd.DataFrame({'Score': [dummy_score]})
    cv_results_lr = pd.DataFrame(pd.DataFrame(cross_validate(lr, X_train, y_train, return_train_score=True)).mean())

    #Save cross-validation results
    cv_results_lr.to_csv(output_path + '/cross_validation_results.csv', index=True)

    #Save coefficients
    saveDummyScore(dummy_results, output_path)
    saveCoefficients(X_train, lr, output_path)

def saveCoefficients(X_train, lr, output_path):

    viz_df = pd.DataFrame({"features": X_train.columns, "coefficients": lr.coef_[0]})

    viz_df.to_csv(output_path + '/crime_coefficients.csv', index=False)

def saveDummyScore(dummy_results, output_path):

    viz_dummy = pd.DataFrame({"Dummy Classifier": ["Dummy Score"], "Score": [dummy_results]})

    viz_dummy.to_csv(output_path + '/dummy_results.csv', index=False)


if __name__ == '__main__':
    analysis()