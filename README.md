# Project Name: XGB-BPred: Machine Learning based Antibody Mediated Response Predictor for Infectious Diseases

## Description  
XGB-Pred is a novel, state of the art, machine learning based classifier that can anticipate the antibody mediated immune response of infectious epitopes. 
Identificattion and prediction of this attribute will play a significant role in the automation of multi epitope vaccine designing, reverse vaccinology, immunoinformatics, reverse vaccinology and antibody engineering.

## Features  
- (List the key features of your project.)  
- (Highlight any unique functionalities.)  

## Installation  
pip install pandas==2.1.4 joblib==1.2.0 numpy==1.26.4 xgboost==2.1.1 scikit-learn==1.5.2
## Usage 
**File Preparation:**
**Step 1:** Prepare your CSV file with epitope features using Biopython and Pfeature with scripts given in the github repository
**Step 2:** Normalize the features using Min-Max scaler
**Step 3:** Ensure your normalized final CSV file should contain epitope sequences and exact same 766 features given in the train, test and external validation test data sets
**Model Usage:**
Step 1: Load the saved model
model_path = "model.pkl"  # Update with your actual model path
model = joblib.load(model_path)
Step 2: Load the CSV data
data_path = "Epitopes_scaled.csv"  # Update with your CSV file path
data = pd.read_csv(data_path)
Step 3: Extract epitope sequences and features
epitopes = data.iloc[:, 0]  # First column: epitope sequences
features = data.iloc[:, 2:]  # Columns 3 to end: 766 features (exclude label)
Step 4: Make predictions
predicted_labels = model.predict(features)  # Predict labels (0 or 1)
Step 5: Create the result DataFrame
result = pd.DataFrame({
    "Epitope": epitopes,
    "Predicted_Label": predicted_labels
})
Step 6: Save the results to a new CSV file
output_path = "predictions_with_epitopes.csv"  # Update with your desired output path
result.to_csv(output_path, index=False)

print(f"Predictions saved to {output_path}")
(Explain how to use the project, including commands, examples, or scripts.)  
## Dependencies  
1- Biopython library (code available in Script 3)
2- Pfeature package (code available in Script 4)
## Dataset 
Dataset employed in this research was extracted from IEDB and available in Github repository
## Contributors  
Maha Yousaf, Soosung Kang, Sun Choi
## Acknowledgments  
(Include any references, funding sources, or credits to other projects.)  
