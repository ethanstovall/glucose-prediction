# Glucose Prediction with Dexcom, Garmin, and MyFitnessPal
The work for this project so far has mostly been a cursory exploration of the Dexcom and Garmin data in Jupyter notebooks, so this README serves as the roadmap for the broader application. 
# Overview
This project aims to help individuals with Type 1 diabetes predict high or low blood sugar episodes by analyzing a combination of heart rate, glucose levels, food intake, and insulin administration data. By leveraging real-time data from health-tracking devices and apps, this project aims to provide actionable insights to help users manage their blood sugar levels more effectively.
- Heart Rate Data: Collected from Garmin devices capable of continuous heart rate monitoring, accessed via the Garmin Connect API.
- Blood Glucose Data: Downloaded from the user's Dexcom Clarity account, which tracks continuous glucose monitor (CGM) data.
- Food and Insulin Data: Pulled from MyFitnessPal and Dexcom Clarity, providing records of carbohydrate consumption and insulin doses. Still working on how to incorporate this effectively, as the value of this data is entirely dependent on the accuracy/consistency of user inputs. 
# Key Features
## Federated Login 
The app would provide federated login functionality, allowing users to securely connect using various accounts for the following:
- Dexcom Clarity: Dexcom CGM tracks blood glucose levels.
- Garmin Connect: Garmin device with heart rate monitoring capabilities.
- MyFitnessPal: logs food intake (carbohydrates) and insulin administration, though I think Dexcom Clarity may also offer this.
## Machine Learning Model 
From my reading, a Recurrent Neural Network (RNN) model or Long Short-Term Memory (LSTM) model is ideal for sequential and temporal data like this. These models are good for time series predictions, as they can maintain and use memory of previous states to improve accuracy.
The model will use recent time windows of heart rate, glucose readings, and food/insulin events to predict future blood sugar levels. The model should give higher weight to more recent events when making predictions, but also be aware of older data. With type 1 diabetics, this is important. For example, the soda you drank 5 minutes ago will have a big effect on your blood sugar. But if you also exercised 30 minutes ago, and ate a large meal high in fats 4 hours ago, those factors will also play a major role.
### Feature Engineering
The input features will include heart rate, glucose levels, insulin doses, and food intake, with the possibility of including additional features like exercise intensity or sleep-related data.
### Training
The model will be trained on time series data. My research suggests using a sliding window approach to capture sequential data over a fixed time range (e.g., the last 30 minutes to several hours).
### Target Variable
The target variable for the model will be the future blood glucose level, predicted over short intervals (e.g., 5, 10, 30 minutes into the future). Depending on the predicted blood glucose level, we should be able to make some valuable suggestions for remediation steps. 
## Training Data Pipeline
A background data pipeline will gather, consolidate, and prepare data from the following sources:
- Dexcom Clarity API: Fetches continuous glucose readings.
- Garmin Connect: Collects heart rate data via GarminDB (SQLite database).
- MyFitnessPal API: Tracks food consumption (carbohydrates) and insulin dosage information.
- This data will be used to generate time series datasets that capture key events: heart rate, blood sugar values, food intake, and insulin administration.
A good candidate for this is AWS Lambda; Step Functions as well, depending on how extensive the procedure is.
## Real-Time Blood Sugar Prediction
Once the model is trained on historical data, the app will predict future blood sugar levels based on the most recent input from the data sources.
The model will continuously evaluate recent data and offer pre-emptive suggestions for the user to address potential high or low blood sugar events.
## Remediation Suggestions
The app will provide real-time alerts for potential blood sugar issues, such as impending lows or highs. These alerts will offer practical recommendations, such as:
- Taking an insulin dose to counteract a high.
- Eating a fast-acting carbohydrate to prevent a low.
- Reducing/Increasing exercise intensity to stabilize blood sugar.
# Development Considerations
A cross-platform mobile app (iOS and Android) is the goal, due to the need for real-time monitoring. Most users will want to access the app via their smartphones, as it allows them to get immediate updates and alerts on their glucose levels.
## Framework 
I'll probably use Flutter or React Native (ideal for cross-platform mobile app for iOS and Android).
## Real-Time Data Access
The app will use the same APIs as the training pipeline to pull real-time data from Dexcom Clarity, Garmin Connect, and MyFitnessPal. Users will receive immediate feedback and alerts based on their latest data, but optimization will be essential; we'll need to be able to pull the appropriate window of data to the users device, and relatively quickly. Blood sugar lows can appear quickly and if the user is depending on the app for predicting this, it has to be fast enough.
## Privacy and Security
Since this project may eventually deal with sensitive health data, privacy and security will be considered. All data transfers could be encrypted, and users' login credentials will be handled using OAuth 2.0 for secure authentication with third-party services (Dexcom, Garmin, MyFitnessPal).
## HIPAA Compliance
For future scaling and user acquisition, the app may need to meet HIPAA (Health Insurance Portability and Accountability Act) standards to protect users' personal health information, but I'm not sure yet whether simple blood glucose data, or access to health-related accounts like Dexcom, would indicate a need for HIPAA compliance.
