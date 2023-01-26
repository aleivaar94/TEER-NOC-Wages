
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white) ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white) 	![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

# Find My NOC Wage App

As a newcomer and international student in Canada I struggled to find reliable salary or wage data to help me plan for life after graduation. Some of the wages I found through well known platforms like Glassdoor were based on salaries in the United States. Furthermore, it didn't provide information of salaries for the same position across different provinces in Canada.

[Findmywage](https://findmywage.streamlit.app/) is an app developed in Streamlit that displays the median, mean, max and minimum wage of occupations per province based on the National Occupation Classification or NOC. The wages come from various sources such as 2016 Census, Labour Force Survey and Employment Insurance survey data.

The National Occupational Classification (NOC) system is a standardized system used in Canada to classify and describe all occupations in the Canadian labor market. The NOC groups together similar occupations based on the tasks, duties, and responsibilities required in the job. The classification is used forworkforce analysis, immigration, and education and training. The NOC is updated every five years to reflect changes in the labor market and economy. The most recent version is the NOC 2021.

The objective of [Findmywage](https://findmywage.streamlit.app/) is to provide reliable and up to date wages for various job positions based on the NOC classification it falls into, so that newcomers and international students in Canada or potential newcomers and international students to Canada can make strategic decisions in case they are planning to move to another province, change careers or decide which province to migrate to. Information is power.


## Demo 

![](https://github.com/aleivaar94/TEER-NOC-Wages/blob/master/assets/app-demo-gif.gif)

## Requirements

```
beautifulsoup4==4.11.1
pandas==1.3.4
requests==2.26.0
selenium==3.141.0
webdriver_manager==3.8.5
numpy==1.20.3
plotly==5.10.0
Pillow==9.4.0
streamlit==1.11.0
```

## Methodology

### Data Collection

Wage data was collected from the [Government of Canada](https://open.canada.ca/data/en/dataset/adad580f-76b0-4502-bd05-20c125de9116).


NOC Codes and titles for each version (2016 and 2021) were also extracted from the Government of Canada [National Occupation Classification](https://noc.esdc.gc.ca/).

Follow the jupyter notebook to see the methodology in detail:

```
TEER-NOC-Code-Extraction.ipynb
```


![](https://github.com/aleivaar94/TEER-NOC-Wages/blob/master/assets/extraction-noc-2016-gif.gif)
<sup>Extracting NOC 2016 codes and titles using BeautifulSoup and Selenium</sup>


![](https://github.com/aleivaar94/TEER-NOC-Wages/blob/master/assets/extraction-noc-2021-gif.gif)
<sup>Extracting NOC 2021 codes and titles using BeautifulSoup and Selenium</sup>


### Data Analysis

Extracted NOC codes and titles of each version (2016 and 2021) were merged.

There are discrepancies between the merged NOC titles of each version. It doesn't necessarily mean that the NOC classification was removed from one version to the other. It could also have a different name corresponding to the same NOC classification. To address this discrepancies, string matching using the `difflib` library was used.

![](https://github.com/aleivaar94/TEER-NOC-Wages/blob/master/assets/string-diff.png)


String matching outputs a numerical value, the closer the value to 1 means it's an identical match. A value at or above 0.5054 provides a match among NOC titles of the different NOC versions.
<br>

![](https://github.com/aleivaar94/TEER-NOC-Wages/blob/master/assets/string-matching.png)


Once the above discrepancies are addressed, the NOC codes from both the 2016 and 2021 versions are merged with the wages data obtained from the Government of Canada. This dataset is used to graph a Choropleth Map using Plotly and develop the Streamlit app.

You can find the Streamlit app code in `noc-dash-streamlit.py`


Follow the jupyter notebook to see the methodology in detail:

```
TEER-NOC-Code-Analysis.ipynb
```

## Workflow
Follow the jupyter notebooks in the order below:

```
1. TEER-NOC-Code-Extraction.ipynb

2. TEER-NOC-Code-Analysis.ipynb
```