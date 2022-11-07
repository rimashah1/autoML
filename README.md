# autoML
The dataset used in this repo contains the medical records for patient's who had had heart failure.
1. Details on the study and variables can be found here: https://github.com/sauravmishra1710/Heart-Failure-Condition-And-Survival-Analysis
2. The raw data can be found here https://raw.githubusercontent.com/sauravmishra1710/Heart-Failure-Condition-And-Survival-Analysis/master/Data/heart_failure_clinical_records_dataset.csv

# Experiment 1: Classification
1. Binary Classification Model
2. Dependent variable = If death occurred ("Death event")
3. The best model was the Ensemble. The log loss was 0.328403, which was the lowest of the models. The AUC value was 0.9327, which is the highest of the models.
4. The baseline log loss was 0.628023 and the Ensemble log loss was 0.328403, so the Ensemble model performed better

# Experiment 2: Regression
1. Regression Model
2. Dependent variable = Age. 
3. The best model was the Ensemble. The RMSE was 11.3497, which was the lowest of the models. The AUC value was 0.9327
4. The baseline log loss was 11.3497 and the Ensemble log loss was 11.9538, so the Ensemble model performed slightly better
