import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML


heart_failure = pd.read_csv('https://raw.githubusercontent.com/sauravmishra1710/Heart-Failure-Condition-And-Survival-Analysis/master/Data/heart_failure_clinical_records_dataset.csv')

# Understand the features of the data
heart_failure.columns
heart_failure.isnull().sum() # no missing values
heart_failure.head(10)
heart_failure.describe()


################ 
# Classification 
################

# create X and y variables 
X = heart_failure[['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
       'ejection_fraction', 'high_blood_pressure', 'platelets',
       'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time',]]
y = heart_failure["DEATH_EVENT"] # DV that we want to predict

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25) 
X_test

automl = AutoML(results_path="classification/heart-failure", mode="Explain") 
automl.fit(X_train, y_train)

pred = automl.predict(X_test)
pred


### Test the model ###
automl_death = AutoML(results_path="classification/heart-failure")

X_withdeath = heart_failure.sample(25)
X_withoutdeath = X_withdeath.drop(columns=['DEATH_EVENT'])

predict = automl.predict(X_withoutdeath)
predict

values_actual = X_withdeath['DEATH_EVENT'].values.tolist()
values_predicted = predict.tolist()
output = pd.DataFrame({'actual': values_actual, 'predicted': values_predicted})
output



############ 
# Regression 
############

X_without_age = heart_failure.drop(columns=['age']) # all columsn except age
y_age = heart_failure['age'] # DV that we want to predict

automl_regression = AutoML(results_path="regression/heart-failure", mode="Explain")
automl_regression.fit(X_without_age, y_age)

heart_failure['predictions'] = automl_regression.predict(X_without_age)