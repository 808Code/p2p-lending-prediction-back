import pandas as pd

# df= pd.read_csv(r"cleansed_data_500.csv")
df = pd.read_csv(r"loan_data_sample_for_deployment.csv")
#Balancing


# Separate rows with 'Fully Paid' and 'Charged Off' loan_status values
fully_paid = df[df['loan_status'] == 'Fully Paid']
charged_off = df[df['loan_status'] == 'Charged Off']

# Determine the smaller count between 'Fully Paid' and 'Charged Off'
min_count = min(fully_paid.shape[0], charged_off.shape[0])

# Sample equal number of rows from each category
fully_paid_sample = fully_paid.sample(n=min_count, random_state=42)
charged_off_sample = charged_off.sample(n=min_count, random_state=42)

# Concatenate the sampled DataFrames
df = pd.concat([fully_paid_sample, charged_off_sample])

# Reset the index
df = df.reset_index(drop=True)


def getRandomRecord():
    return dict(zip(df.columns, df.sample().values.tolist()[0]))


# fix the address and purpose
# fix to send form object autofilled
def one_hot_encode(df, column_name):
    # Perform one-hot encoding
    one_hot = pd.get_dummies(df[column_name])

    # Concatenate the one-hot encoded columns with the original DataFrame
    df_encoded = pd.concat([df, one_hot], axis=1)

    # Drop the original column
    df_encoded.drop(column_name, axis=1, inplace=True)

    return df_encoded
