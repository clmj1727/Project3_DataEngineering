# Real Estate Housing Market Analysis

## Overview

This project focuses on analyzing housing markets in various cities and states, particularly in the U.S. regions of Texas, North Carolina, and Virginia. By examining key metrics like median sale prices, square footage, inventory, and mortgage prices, we aim to uncover trends in the housing market. The goal is to identify patterns such as price growth, affordability, and the influence of demographic, cultural, and economic factors. We’ll also explore migration trends, investor behavior, and the effects of government policies on housing prices.

## Purpose

This project was chosen because the housing market offers a rich dataset with meaningful insights into the economic and socio-cultural dynamics of different regions. Understanding these factors can help stakeholders—ranging from potential homebuyers to investors—make informed decisions. Through this project, we aim to answer key questions around housing affordability, trends, and regional market comparisons.

## Instructions

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/clmj1727/Project3_DataEngineering.git
    ```

2. Open the main analysis script:
    ```bash
    python housing_analysis.py
    ```
3. Make note to change the file_path route to the file in your directory.
    ```bash
    # Extract latest version of cities housing market dataset from Kaggle 
      path = kagglehub.dataset_download("vincentvaseghi/us-cities-housing-market-data")
    # Print the path to locate the file directory
      print("Path to dataset files:", path)
    # Set the correct path to the directory
      directory_path = "path"
    # check the files under the directory which the dataset is downloaded 
      print("Files in the directory:", os.listdir(directory_path))
    # combine the directory path and the dataset file in to a single file path 
      file_path = os.path.join(directory_path, 'city_market_tracker.tsv000')
    ```
  
5. If you are using the data directly from Kaggle, be sure to download the dataset:
    [US Cities Housing Market Data - Kaggle](https://www.kaggle.com/datasets/vincentvaseghi/us-cities-housing-market-data)


## Ethical Considerations

In this project, we have carefully considered ethical implications related to data privacy and fairness. The data used primarily comes from publicly available sources, ensuring that sensitive personal information is not involved. We have also considered the potential impact of the analysis, especially in the context of housing affordability and the effects of demographic trends on different regions. In this dataset we did not find any sensitive data or identifying demographics. Nonetheless, we aim to present data-driven insights responsibly and avoid reinforcing any biases, particularly when analyzing factors like race, gender, or marital status in the housing market. We have cited the data sources below for transparency and validation.

## Data Sources

- [US Cities Housing Market Data - Kaggle](https://www.kaggle.com/datasets/vincentvaseghi/us-cities-housing-market-data)
- [Redfin US Housing Market](https://www.redfin.com/us-housing-market)
- [Mortgage Rates](https://fred.stlouisfed.org/series/MORTGAGE30US)
- [US Cities Census Data](https://simplemaps.com/data/us-cities)

## Code References

The code within this repository is largely original. However, we have incorporated several external resources for specific tasks:

- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api)
- [MongoDB Documentation](https://www.mongodb.com/docs/)

For any non-original code used in the project, references are clearly cited within the respective scripts and notebooks.

## Future Enhancements

- Expand the analysis to additional states and cities across the U.S.
- Implement predictive models to forecast future housing trends.
- Incorporate additional external data sources like Zillow API for real-time insights.

## Contributing

We welcome contributions from other developers. If you'd like to contribute, please fork the repository, make changes, and submit a pull request.

