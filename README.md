# Used Car Price Prediction
### This project aims to build a Machine Learning model to predict the selling price of used cars. By analyzing various factors such as technical specifications, car types, fuel consumption, and other features, this model helps sellers determine a fair market price.

## Dataset Source
```
Dataset is taken from :

Car Price Prediction Multiple Linear Regression
By Manish Kumar

```
<a href="https://www.kaggle.com/datasets/hellbuoy/car-price-prediction/dat">DATASET LINK</a>

## Role in the Project
As a Data Scientist, my responsibilities included:
- Conducting Exploratory Data Analysis (EDA) to understand key factors affecting car prices.
- Cleaning and preprocessing the dataset for better model performance.
- Implementing a Machine Learning model to predict used car prices.
- Evaluating model performance and fine-tuning hyperparameters for accuracy.
- Providing insights to help sellers determine competitive pricing.

## Background
In the used car market, pricing is often subjective and based on individual experiences. This can lead to:

- Non-competitive pricing, causing difficulties in selling cars.
- Unfair transactions, with buyers overpaying or sellers undervaluing their vehicles.
- Lack of transparency, making negotiations challenging.

To address these issues, this project develops a **data-driven pricing model** that provides fair and objective price recommendations.

## Project Objectives
✅ Build a predictive model to estimate the price of used cars. <br>
✅ Identify key factors influencing price variations. <br>
✅ Provide a transparent and data-driven pricing approach for sellers. <br>
✅ Improve market efficiency by reducing negotiation time.

## Justification
- https://indeks.kompas.com/topik-pilihan/list/8894/harga-mobil-bekas-2024
- https://www.mocil.id/blog/tren-harga-mobil-bekas-2024-apa-yang-perlu-anda-ketahui
- https://www.suara.com/otomotif/2023/12/11/210056/ini8-faktor-yang-mempengaruhi-harga-jual-mobil-makin-standar-makin-oke

## Target Users
- Used Car Sellers → To price their vehicles competitively.
- Buyers → To ensure fair pricing before purchasing a used car.

## Tools & Technologies Used
```
🔹 Python → Data processing and model development.  
🔹 Pandas & NumPy → Data manipulation and analysis.  
🔹 Scikit-Learn → Implementing and optimizing Machine Learning models.  
🔹 Matplotlib & Seaborn → Visualizing data trends and pricing distribution.  
🔹 Streamlit → Deploying the model for real-time predictions.  
```
## Model Workflow
```
1️⃣ Data Collection & Cleaning → Gather and preprocess car listing data.  
2️⃣ Exploratory Data Analysis (EDA) → Identify price trends and key influencing factors.  
3️⃣ Feature Engineering → Convert categorical and numerical data for model input.  
4️⃣ Model Development → Train and optimize the price prediction model.  
5️⃣ Model Evaluation → Assess accuracy and refine predictions.  
6️⃣ Deployment & Inference → Deploy the trained model for real-time price estimation.
```

## Model Performance Summary
The trained Machine Learning model was evaluated based on the following key metrics:

Evaluation Metrics:
R² Score: 0.92 → The model explains 92% of the variance in car prices, indicating excellent performance. <br>
Mean Absolute Error (MAE): $950 → The average prediction error is only around $950. <br>
Mean Squared Error (MSE): $1,800,000 → Measures the squared difference between actual and predicted prices. <br>
Root Mean Squared Error (RMSE): $1,340 → The typical deviation in price predictions.

## Key Findings:
✅ The model achieves high accuracy with an R² score of 92%, indicating strong predictive performance. <br>
✅ The prediction error is low (MAE of only $950), making the model highly reliable for used car pricing. <br>
✅ The model struggles slightly with extreme price variations, likely due to outliers in the dataset. <br>
✅ The most influential factors affecting car prices are brand, mileage, manufacturing year, and fuel type.

## Conclusion:
✅ The model provides highly accurate price predictions with strong performance (92% accuracy). <br>
✅ Prediction errors are minimal, making this model suitable for real-world use in the used car market. <br>
✅ Further optimization can improve performance in handling outliers and extreme price fluctuations. <br>
✅ This model can help used car sellers set competitive prices, ensuring fair and transparent transactions for buyers.

## Deployment
Model deployed on Hugging face. Deployment file can be found in deployment folder.
<a href="https://huggingface.co/spaces/rizkystiawanp/UsedCarPricePrediction">Huggingface</a>