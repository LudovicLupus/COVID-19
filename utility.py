
# Takes a dataframe as input and outputs the same dataframe with cleaned column headers
def clean_headers(df):
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace('/', '_')
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('latitude', 'lat')
    df.columns = df.columns.str.replace('longitude', 'long')
    df.columns = df.columns.str.replace('long_', 'long')

    return df

