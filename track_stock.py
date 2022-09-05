import pandas as pd
import yfinance as yf

from google.cloud import bigquery
from google.oauth2 import service_account 

#Authentication
key_path = "/home/om/Documents/Big_query/ncca-361107-9f401816514a.json" ##Replace with path to your service token file
credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials,
project=credentials.project_id)

#Fetch Tickers and Stock Data
get_tickers = pd.read_csv("https://raw.githubusercontent.com/datasets/s-and-p-500-companies-financials/master/data/constituents.csv")
stock_dat = yf.download(get_tickers.Symbol.head(5).tolist(),period="2d",actions=False,group_by=None)


#Process Stock Data
long_form = stock_dat.reset_index().melt('Date', var_name=['Ticker', 'var'])
long_form = long_form.pivot_table(index=['Date', 'Ticker'], columns='var', values='value').reset_index()


long_form["Change"] = long_form.groupby("Ticker").Close.diff()
long_form["Pct_Change"] = long_form.groupby("Ticker").Close.pct_change() * 100
long_form = long_form[long_form ["Date"] == long_form["Date"].iloc[long_form.shape[0]-1]]
long_form = long_form.rename(columns={"Adj Close":"Adj_Close"})
long_form["Date"] = long_form['Date'].dt.strftime('%Y-%m-%d') 

#Upload Data
table = 'datasets.stocks_test_df' ##Replace with your destination_name.dataset.table_name
job = client.load_table_from_dataframe(long_form, table)

#Query Table
query_data = 'SELECT * FROM datasets.stocks_test_df' ##Replace with your destination_name.dataset.table_name
client.query(query_data).result().to_dataframe()