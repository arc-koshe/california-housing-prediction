# Housing Price Prediction

This project is a simple web application that predicts housing prices using a pre-trained machine learning model. The app is built using Streamlit, and it loads a pickled model that includes all necessary preprocessing steps.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Input Features](#input-features)
- [Error Handling](#error-handling)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)

## Overview
This Streamlit web application predicts housing prices based on several input features. The model used in the app is pre-trained and stored in a pickle file. The application includes all necessary preprocessing steps, ensuring that the inputs are correctly processed before making predictions.

## Installation

### Prerequisites
- Python 3.7 or higher
- Streamlit
- Pandas
- Numpy
- Scikit-learn (if you wish to train the model or make modifications)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/arc-koshe/california-housing-prediction
    cd california-housing-prediction
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    conda create -p venv python==3.12
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    streamlit run application.py
    ```

## Usage
1. Open the application in your web browser after running the Streamlit server.
2. Use the sliders and input fields to set the values for the housing features.
3. Click the "Predict" button to see the predicted housing price.

## Model Details
The model used in this application is a Random Forest regression model trained on the California Housing dataset. The model was tuned using Random Search CV to optimize the hyperparameters, ensuring the best possible performance. Other models, such as Linear Regression and Decision Trees, were also tried during the model development process. However, Random Forest provided the lowest Root Mean Squared Error (RMSE), making it the best choice for this prediction task. The model is pickled and loaded in the app, including all preprocessing steps such as feature scaling and encoding.

## Input Features
- **Housing Median Age**: The median age of the houses in the block.
- **Total Rooms**: Total number of rooms in the block.
- **Population**: Population in the block.
- **Median Income**: Median income of the block in tens of thousands of dollars.
- **Ocean Proximity**: Categorical variable indicating the proximity of the block to the ocean.
- **Rooms per House**: The ratio of total rooms to the number of households.
- **Bedrooms Ratio**: The ratio of the number of bedrooms to the total rooms.
- **People per House**: The average number of people per household in the block.

## Error Handling
The application includes error handling for invalid inputs, such as:
- **Infinity/NaN Values**: The app checks for invalid values like infinity or NaN and prompts the user to correct the inputs.
- **Out-of-Range Inputs**: Sliders and input fields have defined ranges to prevent unreasonable inputs.

## Acknowledgements
This project was inspired by the concepts and examples provided in the book **Hands On Machine Learning** by **Aureilen Geron**. The book has been instrumental in understanding machine learning techniques and applying them effectively in real-world scenarios.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.


