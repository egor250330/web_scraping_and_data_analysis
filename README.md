# web_scraping_and_data_analysis
Python Developer Job Market Analysis
A project for collecting Python developer job listings from Djinni and analyzing the most in-demand technologies.

How It Works
Data Collection: The script scrapes Python developer job titles and links from Djinni and saves them in a CSV file.
Data Analysis: A Jupyter Notebook is used to analyze the data and identify the most popular technologies.

How to Run
Clone the repository:

git clone https://github.com/egor250330/web_scraping_and_data_analysis
cd python-job-market-analysis

Install dependencies:

python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

Run the scraping script:

python scrape_jobs.py

Open the Jupyter Notebook for analysis:

jupyter notebook


Results
Job data is saved in the python_developer_jobs.csv file.
Analysis includes graphs of technology popularity.
Example Graph

Technologies Used
requests, BeautifulSoup — for web scraping.
pandas — for data processing.
matplotlib, seaborn — for data visualization.
