# 🚗 Used Car Price Prediction
This project aims to build a Machine Learning model to predict the selling price of used cars. By selecting the most relevant features such as engine size, car weight, horsepower, and drivetrain, the model helps sellers determine a fair and competitive market price.

## 📌 Project Background <br>
In the used car market, pricing is often subjective, leading to:
- Non-competitive pricing, making it difficult to sell vehicles.
- Unfair transactions for both buyers and sellers.
- A lack of transparency in the valuation process.

This project offers a data-driven approach to provide objective and fair price recommendations.

## 🌟 Project Objectives <br>
- Build a regression model to estimate used car prices.
- Select important features using correlation and statistical scoring.
- Minimize prediction error using MAE and R² metrics.
- Deploy the model for real-time price prediction.

## 👥 Target Users <br>
- Used Car Sellers → To determine competitive and fair pricing.
- Used Car Buyers → To assess the fairness of listed prices.

## 📰 Justification <br>
<a href="https://indeks.kompas.com/topik-pilihan/list/8894/harga-mobil-bekas-2024" target="_blank" >Kompas.com – Used Car Prices 2024</a> <br>
<a href="https://www.mocil.id/blog/tren-harga-mobil-bekas-2024-apa-yang-perlu-anda-ketahui" target="_blank" >Mocil.id – Market Trends for 2024</a> <br>
<a href="https://www.suara.com/otomotif/2023/12/11/210056/ini8-faktor-yang-mempengaruhi-harga-jual-mobil-makin-standar-makin-oke" target="_blank" >Suara.com – 8 Factors Affecting Resale Value</a>

## 📂 Dataset Source <br>
<a href="https://www.kaggle.com/datasets/hellbuoy/car-price-prediction/dat">Car Price Prediction - Manish Kumar (Kaggle)</a>

## 🧰 Tools & Technologies Used <br>
- Python → Data processing and model development
- Pandas & NumPy → Data manipulation and numerical operations
- Scikit-Learn & XGBoost → Model building and tuning
- Matplotlib & Seaborn → Data visualization
- Streamlit → Model deployment and web app interface

## ⚙️ Model Pipeline <br>
- Data Cleaning → Handling duplicates, outliers, and missing values
- Feature Selection → Correlation analysis and ANOVA F-test for top features
- Preprocessing → Scaling numeric features, encoding categoricals
- Model Training → Train and evaluate 7 different regressors
- Hyperparameter Tuning → GridSearchCV on the top 3 models
- Model Inference & Evaluation → Final evaluation on test data
- Model Deployment → Export model to .pkl and integrate into Streamlit app

## 📈 Model Evaluation (Final Model: XGBRegressor) <br>
- Train R²: 0.9881
- Test R²: 0.9113
- Train MAE: $630
- Test MAE: $1655

The model generalizes well to unseen data with a high level of accuracy.

## 🧠 Key Insights <br>
The most influential numerical features are `engine size`, `curb weight`, `horsepower`, and `car width`.
Categorical features such as `cylinder number`, `fuel system`, `drivetrain`, `aspiration`, and `car body` also play a significant role in predicting car prices.
Among all tested algorithms, XGBRegressor achieved the best performance after feature selection and hyperparameter tuning.

## 📌 Conclusion <br>
- The final model achieves 91.13% accuracy (R²) on unseen test data.
- The model provides reliable price estimates with low prediction errors (MAE ~$1655).
- Suitable for real-world deployment as a car pricing assistant.

## ✅ Model Strengths & ⚠️ Limitations <br>
**Strengths:** <br>
- High prediction accuracy
- Robust to outliers and non-linear features
- Stable performance across cross-validation folds

**Limitations:** <br>
- Slight overfitting (Train R² > Test R²)
- Complex model, less interpretable
- Requires complete preprocessing before inference

## 💡 Business Recommendations <br>
- Target Toyota models → Highest demand based on dataset distribution.
- Use predictive price range for inventory decisions.
- Develop marketing strategies aligned with predicted price tiers.
- Educate sellers to use key technical specs for better pricing.

## 🚀 Deployment
This project is deployed with **Streamlit** and hosted on Hugging Face:
<a href="https://huggingface.co/spaces/rizkystiawanp/UsedCarPricePrediction" target="_blank">Huggingface</a>