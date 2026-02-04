# Car Acceptance Data Visualization
## Overview
This project demonstrates the use of Exploratory Data Analysis (EDA) and data visualization techniques to analyze a car evaluation dataset. The primary objective is to understand how various car attributes-such as price, number of doors, and passenger capacity affect the acceptance-decision of a vehicle.

Data visualization plays a critical role in data mining and machine learning by revealing patterns, trends, and relationships that are not immediately apparent from raw data. The insights derived from this analysis can support feature selection and model design in downstream predictive tasks.

## Dataset
The dataset used in this project is myCarTrainDataset_2024.csv. It consists of categorical and numerical attributes describing different characteristics of cars, along with an acceptance label.

Key attributes include:

price – Categorical feature representing the cost category of the car

doors – Numerical feature indicating the number of doors

persons – Numerical feature representing passenger capacity

accept – Target variable indicating the acceptance class

The dataset is preprocessed and structured, making it suitable for exploratory analysis with minimal data cleaning.

## Structure
The repository is organized to promote clarity and reproducibility:

src/data_visualization.py – Main Python script containing all visualization logic

data/myCarTrainDataset_2024.csv – Dataset used for analysis

visualizations – Folder containing generated plots

README.md – Project documentation

requirements.txt – List of Python dependencies

## Requirements
To run this project locally, ensure Python 3.x is installed along with the following libraries:

Pandas – For data loading, manipulation, and aggregation

Matplotlib – For low-level plotting and customization 

Seaborn – For high-level statistical data visualization

All required packages can be installed using:

pip install -r requirements.txt

## Implementation Details
The implementation follows a systematic exploratory data analysis workflow:

Data Loading: The dataset is loaded using Pandas and inspected to understand its structure and attributes.

Bar Chart Analysis: A bar chart is used to visualize the distribution of acceptance classes across different price categories.

Scatter Plot Visualization: A scatter plot examines the relationship between the number of doors and passenger capacity, with acceptance represented using color and style.

Histogram Analysis: A histogram illustrates the distribution of the number of doors across all vehicles.

Stacked Bar Chart: A stacked bar chart provides a comparative view of acceptance outcomes across price categories.

Pie Chart Representation: A pie chart displays the overall proportion of acceptance classes in the dataset.

These visualizations collectively provide a comprehensive overview of the dataset and support intuitive pattern recognition.

## Results
The exploratory analysis reveals several meaningful insights:

Vehicle acceptance varies significantly across different price categories.
Cars with higher passenger capacity tend to exhibit higher acceptance rates.
The distribution of doors highlights common structural preferences in the dataset.
The acceptance classes are not uniformly distributed, indicating potential class imbalance.
The visual patterns observed through this analysis serve as a strong foundation for subsequent machine learning and classification tasks.

## Academic Context
This project was completed as part of coursework for the Data Mining and Machine Learning module in the Master’s program at the University of Liverpool. It demonstrates practical application of Python-based data analysis and visualization techniques commonly used in data mining and machine learning workflows.
