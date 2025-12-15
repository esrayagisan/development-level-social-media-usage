# development-level-social-media-usage
DSA210 Term Project Repo

# Social Media Usage & Development Indicators Analysis

## Project Summary

This project analyzes whether countries' social media platform preferences
correlate with development indicators.\
Two hypotheses were tested:

-   **H0:** No correlation exists.
-   **H1:** A correlation exists.

The process includes dataset merging, cleaning, Z‑score normalization
using Worldwide averages, correlation analysis, and hypothesis testing.

Code: https://colab.research.google.com/drive/1gaJ-ycMkWCuMxfnKqy5WDlPcy_FaJSgm?usp=sharing

## Motivation

Social media is one of the most influential tools for communication and information sharing in modern societies. However, the intensity of its use may vary across countries depending on their economic conditions. One day I want to build my own social media platform, that's why I try to understand the needs and habbits of societies with different development levels. The findings will help me to understand how development level influences digital behaviors.


## Datasets

-   `monthly_time_spend_by_country.csv`: This dataset is obtained from Datareportal's Instagram, X, Tiktok, LinkedIn, Pinterest Users, Stats, Data & Trends for 2025. I couldn't find the actual dataset so I used the graphs that show monthly time spend data for top 50 countries. I used GenAI to convert these graphs to a merged data table.
Graphs: https://drive.google.com/drive/folders/11Oza-q2oY5u7eKO9wnQlAcZHpx14U2ee?usp=sharing
Extracted dataset: https://drive.google.com/file/d/1XVIsLcXXbefWaH4NlXZDJHGTI9uUGbAo/view?usp=sharing

-   `android_phone_use_by_country.csv`: https://gs.statcounter.com/os-market-share/mobile/worldwide/#quarterly-202404-202404-map
https://drive.google.com/file/d/1Nfg3OeY6cbPBhYDJtB8w0S1-4T789Dl1/view?usp=sharing


-   `development_country.csv`: https://www.kaggle.com/datasets/tarktunataalt/2023-global-country-development-and-prosperity-index
https://drive.google.com/file/d/16qgpEV9k87cOgHd1SqIVORoXSGyxBYmF/view?usp=sharing

## Data Preparation

-   Cleaned `Country_Code`
-   Replaced "-" with NaN
-   Merged datasets on `Country_Code`
-   Restored the `Worldwide` row for Z‑score normalization

## Z‑Score Normalization

Z‑score was computed relative to the Worldwide usage value:

    z = (country_value – worldwide_value) / std(countries_only)

## Correlation & Hypothesis Testing

Pearson and Spearman correlations were computed between: 
- Each social
media platform (Z‑score adjusted)
- Each development indicator

Significant relationships were identified using **p \< 0.05**.

## Outputs

-   Cleaned merged dataset\
-   Z‑score normalized columns\
-   Correlation heatmap\
-   Hypothesis test results\
-   Significant relationships list

## Conclusion

This project provides a standardized comparison of social media usage
patterns across development indicators, accounting for missing data and
dataset bias using normalization techniques.



