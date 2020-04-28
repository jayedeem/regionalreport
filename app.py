import pandas as pd

df = pd.read_csv('rl.csv', encoding = "ISO-8859-1")
df = df[["DEALERCD",	"GROSS_ADDS_202001",	"GROSS_ADDS_202002",	"GROSS_ADDS_202003","Master Agent",	"region_split",	
"regional_field_rep",	"ADDRESS",	"SUITE",	"CITY",	"STATE",	"ZIP",	"last_visted_date",	"ActiveFlag",	"inactive_date",	"BUSINESSNAME"]]
df.rename(columns={'DEALERCD': "RetailerID"}, inplace = True)
df1 = pd.read_csv('SO_Listing.csv')
df2 = pd.merge(df,df1, on=['RetailerID'], how="inner")
df2.to_csv('test.csv', index=False)
