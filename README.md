## Project Overview
  - The Olympics History Data Analysis proejct aims to unconver valuable insights by analyzing historical data related to the olympic games. By exploring this dataset, we will draw data-driven conclusions that provides us an insight on various aspects of Olympic Games throughout history.

## About the dataset
- The data can be obtained or downloaded from https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results. This is a historical dataset provides a comprehensive historical overview, spanning from Athens 1896 to Rio 2016. The dataset was originally obtained from  www.sports-reference.com. The dataset consists information athletes, events, countries, and medals awarded, covering both Summer and Winter Games.
- Athlete_events.csv: Olympic event (athlete-events). The columns are:
ID - Unique number for each athlete
Name - Athlete's name
Sex - M or F
Age - Integer
Height - In centimeters
Weight - In kilograms
Team - Team name
NOC - National Olympic Committee 3-letter code
Games - Year and season
Year - Integer
Season - Summer or Winter
City - Host city
Sport - Sport
Event - Event
Medal - Gold, Silver, Bronze, or NA
- noc_regions.csv: Has all the regional information
  region : region that athlete belong too
  noc : Regional olympic committee
  notes: any notes about the events
  
## Objective:
- The data can be obtained or downloaded from https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results. This is a historical dataset provides a comprehensive historical overview, spanning from Athens 1896 to Rio 2016. The dataset was originally obtained from  www.sports-reference.com .
## Folder Structure:
olympic-history-analysis/
│
├── sql_queries.py
├── create_tables.py
├── etl.py
├── test.ipynb
└── README.md

## Usage

1. **Set up Environment**: Ensure Python and necessary dependencies are installed by running `pip install -r requirements.txt`.
2. **Create Tables**: Execute `create_tables.py` to create the required database tables.
3. **ETL Operations**: Run `etl.py` to perform ETL operations on the data.
4. **Data Analysis**: Utilize `sql_queries.py` for analyzing data through SQL queries and explore data further using `test.ipynb`.





