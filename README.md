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
   - Converts temperature values from Kelvin to Celsius and allows user preference for unit selection.

3. **Rollups and Aggregates**:
   - **Daily Weather Summary**: 
     - Rolls up weather data for each day, calculating daily aggregates for average, maximum, and minimum temperatures, as well as the dominant weather condition.
   - **Alerting Thresholds**:
     - Allows user-configurable thresholds for temperature or specific weather conditions. Alerts are triggered for breaches and displayed on the console or sent via email notifications.

4. **Visualizations**:
   - Implements visualizations to display daily weather summaries, historical trends, and triggered alerts.

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
