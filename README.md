# Salary_Prediction_Project
## 📌 About the Project

This is an end-to-end machine learning project aimed at creating a web app for predicting an individual's salary.

### 📌 Data Preprocessing and Exploratory Data Analysis 📈 📊 📉 

Every project begins with data collection. We obtained the dataset from the Kaggle site and installed all the required libraries for this project. We performed data preprocessing steps, such as checking for null and duplicate values.

The data didn't contain any null values but had duplicate entries, which we removed. Additionally, we dealt with unwanted values in certain columns, replacing them with "others" as appropriate. We then embarked on Exploratory Data Analysis (EDA) to gain insights from the data. We explored exciting questions, like the distribution of working hours per week, the most demanded degree and education, and the job with the highest working hours. Furthermore, we investigated the average age for each gender. We utilized pie, bar, box, and histogram charts to visualize these insights.

### 📌 Machine Learning Process

We installed the required libraries and converted categorical values into numerical ones using label encoding. Next, we divided the data into dependent and independent variables. After that, we normalized the data using the StandardScaler. The dataset was then split into training and testing sets, with 20% of the data reserved for training. We created a function for the machine learning model and applied various classification algorithms, including logistic regression, Random Forest, and XGBoost. Among these, the Random Forest algorithm achieved an accuracy score of 87%. We saved the model using the Pickle library.

### 📌 Machine Learning Model Deployment

For model deployment, we used Streamlit, a user-friendly web app framework. In the app.py file, we loaded the Pickle files and utilized Streamlit's built-in functions like select boxes and number inputs to take user inputs. We normalized the data as required, used the Pickle model to make predictions, and displayed the results on the Streamlit app. Finally, we deployed the web app on the Streamlit Cloud platform, making it accessible as a website.




Web App: https://salarypredictionproject-2g8cme26awavyozazmas89.streamlit.app/

[![Watch the Video](https://example.com/video-thumbnail.png)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
