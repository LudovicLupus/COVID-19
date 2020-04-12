"""
Load CSSE data from github
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
"""

# import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from utility import clean_headers

pd.set_option('display.max_columns', None)

# Raw csv link address from github (single url)
CSV_URL = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-22-2020.csv'

DAILY_REPORTS_URL = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'
RAW_GITHUB_PREFIX = 'https://raw.githubusercontent.com'

def get_daily_report_links():
    # create response object
    r = requests.get(DAILY_REPORTS_URL)

    # create BeautifulSoup object
    soup = BeautifulSoup(r.content, 'lxml')

    # find all links on web-page
    links = soup.find_all('a')

    # Concatenating raw github prefix with href attribute's ending in '.csv'
    report_links = [RAW_GITHUB_PREFIX + link['href'] for link in links
                    if link['href'].endswith('.csv')]

    # Cleaning link by removing '/blob' from string
    report_links = [link.replace('/blob', '') for link in report_links]

    print(f"First Link: {report_links[0]}")
    print(f"Number of report Links: {len(report_links)}")

    return report_links

report_links = get_daily_report_links()

# fields = {}
# for link in report_links:
#     for field in list(pd.read_csv(link, index_col=0, parse_dates=[0]).columns):
#         field = field.strip()
#         field = field.lower()
#         field = field.replace('/', '_')
#         field = field.replace(' ', '_')
#         fields[field] = fields.get(field, 0) + 1

fields_trimmed = {'country_region': 79,
                  'last_update': 79,
                  'confirmed': 79,
                  'deaths': 79,
                  'recovered': 79}

# Create empty dataframe with
daily_df = pd.DataFrame(columns=list(pd.read_csv(report_links[0], index_col=0, parse_dates=[0]).columns))
daily_df = clean_headers(daily_df)
print(daily_df.count())
for link in report_links:
    df = pd.read_csv(link, index_col=0, parse_dates=[0])
    df = clean_headers(df)
    daily_df = pd.concat([daily_df, df], axis=0, sort=False)

print(f"Final counts of concatenated dataframe: \n {daily_df.count()}")





# with requests.Session() as s:
#     download = s.get(CSV_URL)
#     print(f"Status Code: {download.status_code}")
#     print(f"Encoding: {download.encoding}")
#
#     # Content is in dtype <bytes> before decoding into <str>
#     decoded_content = download.content.decode(download.encoding)
#
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#
#     for row in cr:
#         print(row)



