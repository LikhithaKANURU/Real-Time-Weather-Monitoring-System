# Real-Time Data Processing System for Weather Monitoring

## Objective
This project aims to develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system utilizes data from the [OpenWeatherMap API](https://openweathermap.org/).

## Data Source
The system continuously retrieves weather data from the OpenWeatherMap API. You need to sign up for a free API key to access the data. The API provides various weather parameters, including:

- `main`: Main weather condition (e.g., Rain, Snow, Clear)
- `temp`: Current temperature in Celsius
- `feels_like`: Perceived temperature in Celsius
- `dt`: Time of the data update (Unix timestamp)

## Features
1. **Continuous Data Retrieval**:
   - The system retrieves weather data for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad) at configurable intervals (e.g., every 5 minutes).

2. **Temperature Conversion**:
   - Convert temperature values from Kelvin to Celsius and allow user preference for unit selection.

3. **Rollups and Aggregates**:
   - **Daily Weather Summary**: 
     - Roll up weather data for each day, calculating daily aggregates for average, maximum, and minimum temperatures, as well as the dominant weather condition.
   - **Alerting Thresholds**:
     - Define user-configurable thresholds for temperature or specific weather conditions. Trigger alerts for breaches, displayed on the console or sent via email notifications.

4. **Visualizations**:
   - Implement visualizations to display daily weather summaries, historical trends, and triggered alerts.

## Test Cases
The following test cases will ensure the reliability of the system:

1. **System Setup**: Verify successful connection to the OpenWeatherMap API using a valid API key.
2. **Data Retrieval**: Simulate API calls and ensure the system retrieves and parses weather data correctly.
3. **Temperature Conversion**: Test conversion of temperature values from Kelvin to Celsius (or Fahrenheit).
4. **Daily Weather Summary**: Validate calculations for daily summaries.
5. **Alerting Thresholds**: Test configurations and trigger alerts accurately.

## Bonus Features
- Extend the system to support additional weather parameters (e.g., humidity, wind speed) and incorporate them into rollups/aggregates.
- Retrieve weather forecasts and generate summaries based on predicted conditions.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/weather-monitoring-system.git
   cd weather-monitoring-system
## Key Features
-1.**Data Collection**: Retrieves data at configurable intervals (e.g., every 5 minutes) for major cities like Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
-2.**Temperature Conversion**: Converts temperature data from Kelvin to Celsius or Fahrenheit based on user preference.
-3.**Daily Weather Summaries**: Aggregates daily data to calculate average, maximum, and minimum temperatures and the dominant weather condition.
-4.**Alert System**: Notifies users when user-defined thresholds are breached. Alerts can be triggered for specific temperatures or weather conditions and are displayed on the console or sent via email.
-5.**Visualizations**: Generates charts to show daily summaries, trends, and alert triggers for better data interpretation.

## Getting Started
-1.'Libraries Required'
To run this project, you need to install the following Python libraries:

requests: For making API calls to OpenWeatherMap
matplotlib: For creating visualizations and graphs
smtplib: For sending email alerts (built-in Python library, but requires SMTP configuration)
datetime: For handling date and time operations (standard Python library)
time: For scheduling regular data retrieval (standard Python library)
Install the required libraries with:

bash
Copy code
pip install requests matplotlib
How to Solve the Program
Clone the Repository: First, clone the repository to your local machine.
bash
Copy code
git clone https://github.com/your_username/weather-report.git
cd weather-report
Set Up OpenWeatherMap API Key: Sign up on OpenWeatherMap to get a free API key. Once you have the API key, create a .env file in your project folder and add:
env
Copy code
API_KEY=your_openweathermap_api_key
Configure Email Alerts (Optional): If you wish to receive email alerts, set up an app password for your email account (required by Gmail). Add your email credentials to the .env file:
env
Copy code
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
Run the Program: Execute the main Python script to start collecting and processing weather data.
bash
Copy code
python weather_monitoring.py
How the Program Works
The program fetches weather data at set intervals for each city.
It converts temperatures to the chosen unit (Celsius or Fahrenheit).
Data is processed to calculate daily summaries, including average, max, and min temperatures.
If set thresholds are breached, alerts are sent via console or email.
Visualizations are generated for daily and historical data to facilitate interpretation.
Testing
This project includes several test cases to ensure accurate functionality and reliability:

API Connectivity: Verifies connection to OpenWeatherMap API.
Data Retrieval and Parsing: Ensures data is correctly parsed and structured.
Temperature Conversion: Confirms conversion from Kelvin to Celsius/Fahrenheit.
Daily Summaries: Checks accuracy of calculated daily rollups.
Alert Triggering: Verifies alerts are triggered at correct thresholds.
Bonus Features
Additional Weather Parameters: Includes options for extra data like humidity and wind speed.
Weather Forecast Summaries: Provides insights based on forecasted conditions for better planning.
Contributing
Contributions are welcome! Please see the Contributing Guidelines for instructions on reporting issues, submitting pull requests, and joining discussions.
