# development-level-social-media-usage  
DSA210 Term Project Repository

## Social Media Usage & Development Indicators Analysis

---

## Project Summary

This project investigates the relationship between social media usage patterns
and country-level development indicators. The analysis aims to understand whether
platform-specific usage behaviors correlate with economic, institutional, and
social development measures across countries.

The study follows a structured pipeline including data extraction, cleaning,
exploratory data analysis (EDA), hypothesis testing, normalization, and machine
learning modeling.

**Hypotheses tested:**
- **H0:** There is no correlation between social media usage and development indicators.
- **H1:** There exists a statistically significant correlation between social media usage and development indicators.

---

## Motivation

Social media is one of the most influential tools for communication and
information sharing in modern societies. However, the intensity and nature ofI of
its use may vary across countries depending on their economic and developmental
conditions. Motivated by the long-term goal of building a social media platform,
this project aims to better understand how societies with different development
levels engage with social media. The findings help explain how development
contexts influence digital behaviors and platform preferences.

---

## Datasets

- **`monthly_time_spend_by_country.csv`**  
  Source: Datareportal (2025 platform usage statistics).  
  Since the raw dataset was not publicly available, platform-specific graphs
  showing average monthly time spent for the top 50 countries were extracted and
  converted into tabular format using Generative AI tools.

  - Graphs:  
    https://drive.google.com/drive/folders/11Oza-q2oY5u7eKO9wnQlAcZHpx14U2ee
  - Extracted dataset:  
    https://drive.google.com/file/d/1XVIsLcXXbefWaH4NlXZDJHGTI9uUGbAo

- **`android_phone_use_by_country.csv`**  
  Source: StatCounter Global Stats  
  https://gs.statcounter.com/os-market-share/mobile/worldwide/#quarterly-202404-202404-map  
  Extracted dataset:  
  https://drive.google.com/file/d/1Nfg3OeY6cbPBhYDJtB8w0S1-4T789Dl1

- **`development_country.csv`**  
  Source: Kaggle – 2023 Global Country Development and Prosperity Index  
  https://www.kaggle.com/datasets/tarktunataalt/2023-global-country-development-and-prosperity-index  
  Extracted dataset:  
  https://drive.google.com/file/d/16qgpEV9k87cOgHd1SqIVORoXSGyxBYmF

---

## Data Preparation

- Standardized `Country_Code` values
- Replaced missing values ("-") with NaN
- Merged datasets using `Country_Code`
- Converted all numerical columns to numeric format
- Generated platform-specific normalized usage variables using Android
  penetration rates

The final cleaned dataset is available within the notebook outputs.

---

## Exploratory Data Analysis (EDA)

EDA was conducted to:
- Inspect distributions of social media usage variables
- Analyze correlations between platforms and development indicators
- Identify potential outliers and missing data patterns

Visualizations include correlation heatmaps and scatter plots for each
platform–indicator pair.

---

## Normalization

Social media usage values were normalized using Android phone penetration rates
to control for device accessibility differences across countries.

---

## Correlation & Hypothesis Testing

Pearson (linear) and Spearman (rank-based) correlation analyses were performed
between:
- Each social media platform’s normalized usage
- Each development indicator

Statistical significance was evaluated using **p < 0.05**. Results from both
methods were compared to assess robustness.

---

## Machine Learning

A regression-based machine learning model was applied to evaluate the predictive
power of social media usage on development indicators. The model achieved a low
R² score (~0.097), indicating that social media usage alone has limited
predictive capability and should be interpreted as a complementary signal rather
than a primary determinant.

---

## Results & Interpretation

- Platform-specific patterns were observed across development dimensions
- LinkedIn and Pinterest showed mostly positive associations with institutional
  and quality-of-life indicators
- TikTok and YouTube exhibited more negative associations with governance and
  economic indicators
- ML results supported the statistical findings by highlighting weak standalone
  predictive power

---

## AI Tool Usage

Generative AI tools were used in this project for specific and limited purposes.
These include converting publicly available graphical data into tabular format,
assisting with code debugging, and improving code structure and documentation.
All analytical decisions, hypothesis formulation, statistical testing,
interpretation of results, and conclusions were independently conducted by the
author. AI tools were not used to generate results or automate analysis.




