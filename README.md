# Machine Learning Models 

This repository contains code for deploying three machine learning models using Decision Tree, Linear Regression, and Naïve Bayes algorithm. The models predict heart attack risk and insurance charges based on provided datasets.

## Installation

### Prerequisites

- Python: Ensure you have Python installed. If not, you can download it from [python.org](https://www.python.org/downloads/).

1. **Clone the Repository:**
   git clone https://github.com/gourabb8273/Data-Science-With-Python.git
   cd Data-Science-With-Python
2. **Install all dependencies library used in the project**
   pip install numpy
   pip install pandas
   pip install seaborn
   pip install matplotlib
   pip install sklearn or pip install scikit-learn
   pip install flask
   pip install pydotplus
   (use pip3 instead of pip for python 3 version)
   Install [graphviz](https://graphviz.org/download/) to visualize the Decision Tree Plot
 
## Usage

### Problem 1: Heart Attack Prediction

#### Decision Tree Model

The code for predicting heart attack risk using a Decision Tree model can be found in the `heart_risk_predictor_decision_tree_model.ipynb` notebook inside `DecisionTree` folder.

#### Steps

1. **Load and Process Data:**
   - The notebook loads the `US_Heart_Patients.csv` dataset and performs necessary data processing steps.

2. **Split the Data:**
   - The data is split into an 80% training dataset and a 20% test dataset.

3. **Train Decision Tree Model:**
   - The Decision Tree model is trained using the training dataset.

4. **Evaluate Model:**
   - The model is evaluated on the test dataset.

5. **Save Model:**
   - The trained Decision Tree model is saved as a pickle file `decision_tree_model.pkl` inside `DecisionTree` folder for future deployment.
   
#### Execution

Execute the cells in the `heart_risk_predictor_decision_tree_model.ipynb` notebook to perform the entire process, from loading data to saving the trained model.

### Deploying Models in an API

To deploy the Decision Tree model for predicting heart attacks, a Flask API has been implemented which will load the model and predict the heart risk using data requested by API. The code is available in the `DecisionTree/predict_heart_attack.py` file.

#### Execution
To run it use command `python DecisionTree/predict_heart_attack.py`  then hit the end point http://127.0.0.1:5000/heart-attack-risk and pass the required data to get the prediction. (Please verify the port once before invoking)


#### Naïve Bayes Model

The code for predicting heart attack risk using a Decision Tree model can be found in the `heart_risk_predictor_naïve_bayes_model.ipynb` notebook inside `NaïveBayes` folder.

#### Steps

1. **Load and Process Data:**
   - The notebook loads the `US_Heart_Patients.csv` dataset and performs necessary data processing steps.

2. **Split the Data:**
   - The data is split into an 80% training dataset and a 20% test dataset.

3. **Train Decision Tree Model:**
   - The Decision Tree model is trained using the training dataset.

4. **Evaluate Model:**
   - The model is evaluated on the test dataset.

5. **Save Model:**
   - The trained Decision Tree model is saved as a pickle file `naive_bayes_model.pkl` inside `NaïveBayes` folder for future deployment.
   
#### Execution

Execute the cells in the `heart_risk_predictor_naïve_bayes_model.ipynb` notebook to perform the entire process, from loading data to saving the trained model.

#### Deploying Models in an API

To deploy the Decision Tree model for predicting heart attacks, a Flask API has been implemented which will load the model and predict the heart risk using data requested by API. The code is available in the `NaïveBayes/predict_heart_attack.py` file.

#### Execution
To run it use command `python NaïveBayes/predict_heart_attack.py` then hit the end point http://127.0.0.1:5000/heart-attack-risk and pass the required data to get the prediction. (Please verify the port once before invoking)



### Problem 2 : Health Insurance Charge Prediction

#### Linear Regression Model

The code for predicting heart attack risk using a Decision Tree model can be found in the `health_insurance_charge_predictor_linear_regression_model.ipynb` notebook inside `LinearRegression` folder.

#### Steps

1. **Load and Process Data:**
   - The notebook loads the `insurance_data.csv` dataset and performs necessary data processing steps.

2. **Split the Data:**
   - The data is split into an 80% training dataset and a 20% test dataset.

3. **Train Decision Tree Model:**
   - The Decision Tree model is trained using the training dataset.

4. **Evaluate Model:**
   - The model is evaluated on the test dataset.

5. **Save Model:**
   - The trained Decision Tree model is saved as a pickle file `linear_regression_model.pkl` inside `LinearRegression` folder for future deployment.
   
#### Execution

Execute the cells in the `health_insurance_charge_predictor_linear_regression_model.ipynb` notebook to perform the entire process, from loading data to saving the trained model.

### Deploying Models in an API

To deploy the Decision Tree model for predicting heart attacks, a Flask API has been implemented which will load the model and predict the heart risk using data requested by API. The code is available in the `LinearRegression/predict_heart_attack.py` file.

#### Execution
To run it use command `python LinearRegression/predict_heart_attack.py` then hit the end point http://127.0.0.1:5000/insurance-charges and pass the required data to get the prediction. (Please verify the port once before invoking)
