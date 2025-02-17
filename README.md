# Project Name: XGB-BPred: Machine Learning based Antibody Mediated Response Predictor for Infectious Diseases

## Description  
XGB-Pred is a novel, state of the art, machine learning based classifier that can anticipate the antibody mediated immune response of infectious epitopes. 
Identification and prediction of this attribute will play a significant role in the automation of multi epitope vaccine designing, reverse vaccinology, immunoinformatics, reverse vaccinology and antibody engineering.
## Dependencies  
    1- Biopython library (code available in Step2_Biopython.ipynb)
    2- Pfeature package (code available in Step3_Pfeature.ipynb)

## Libraries and Package Requirements  
```
pip install pandas==2.1.4 joblib==1.2.0 numpy==1.26.4 xgboost==2.1.1 scikit-learn==1.5.2
```
## Input File Preparation
```
Step 1: Prepare a text file that contains epitope sequences and extract Biopython features via script "Step2_Biopython.ipynb" given in github repositority
Step 2: Extract peptide features from Pfeature via "Step3_Pfeature.ipynb" given in the github repository
Step 2: Finally employ "File_Preparation_Script.ipynb", which ensures finalized CSV file contains exact 766 features given in the training data and then normalizes the features using min-max scaler
```
## Model Usage
**Step 1:** 
Load the saved model
```
model_path = "XGB_BPred.pkl"  # Update with your actual model path
model = joblib.load(model_path)
```
**Step 2:** Load the CSV data
```
data_path = "Epitopes_scaled.csv"  # Update with your CSV file path
data = pd.read_csv(data_path)
```
**Step 3:** 
Extract epitope sequences and features
```
epitopes = data.iloc[:, 0]  # First column: epitope sequences
features = data.iloc[:, 2:]  # Columns 3 to end: 766 features (exclude label)
```
**Step 4:** 
Make predictions
```
predicted_labels = model.predict(features)  # Predict labels (0 or 1)
```
**Step 5:** Create the result DataFrame
```
result = pd.DataFrame({
    "Epitope": epitopes,
    "Predicted_Label": predicted_labels
})
```
**Step 6:** Save the results to a new CSV file
```
output_path = "predictions_with_epitopes.csv"  # Update with your desired output path
result.to_csv(output_path, index=False)
print(f"Predictions saved to {output_path}")  
```
## Dataset 
Dataset employed in this research was extracted from IEDB and available in Github repository
## Contributors  
Maha Yousaf, Soosung Kang, Sun Choi
## Acknowledgments  
This work was supported by the National Research Foundation of Korea grant (NRF- 2022M3E5F3080873).  
