import pandas as pd
df= pd.read_csv(r"cleansed_data_500.csv")

def getRandomRecord():
    return dict(zip(df.columns, df.sample().values.tolist()[0]))

#fix the address and purpose
#fix the send form object auto filled