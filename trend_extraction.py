import pandas as pd

DATA_PATH = './entities/clean/multihash_maxout_vec_ents_clean.csv'
OUTPUT_FOLDER = './trend_data/'

def main():
    # Import data
    df = pd.read_csv(DATA_PATH)
    # Convert timestamp col to datetime type
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Get time periods from timestamp
    df['year'] = df['timestamp'].dt.to_period('Y')
    df['month'] = df['timestamp'].dt.to_period('M')
    df['week'] = df['timestamp'].dt.to_period('W')
    # Get entity totals for each period
    year_totals = df['year'].value_counts().to_dict()
    month_totals = df['month'].value_counts().to_dict()
    week_totals = df['week'].value_counts().to_dict()
    # Get counts for each period
    year_counts = df[['year', 'new_ent', 'type']].value_counts()
    month_counts = df[['month', 'new_ent', 'type']].value_counts()
    week_counts = df[['week', 'new_ent', 'type']].value_counts()
    # Convert to dataframes
    year_df = pd.DataFrame(year_counts).sort_index().reset_index()
    month_df = pd.DataFrame(month_counts).sort_index().reset_index()
    week_df = pd.DataFrame(week_counts).sort_index().reset_index()
    # Get entity totals in dataframe
    year_df['total'] = year_df['year'].map(year_totals)
    month_df['total'] = month_df['month'].map(month_totals)
    week_df['total'] = week_df['week'].map(week_totals)
    # Get entity proportions as percentage
    year_df['proportion_perc'] = (year_df['count'] / year_df['total']) * 100
    month_df['proportion_perc'] = (month_df['count'] / month_df['total']) * 100
    week_df['proportion_perc'] = (week_df['count'] / week_df['total']) * 100
    # Drop total column
    year_df.drop(columns=['total'], inplace=True)
    month_df.drop(columns=['total'], inplace=True)
    week_df.drop(columns=['total'], inplace=True)
    # Get percentage change between previous time period
    year_df['perc_change'] = year_df.groupby(['new_ent', 'type'])['proportion_perc'].pct_change()
    month_df['perc_change'] = month_df.groupby(['new_ent', 'type'])['proportion_perc'].pct_change()
    week_df['perc_change'] = week_df.groupby(['new_ent', 'type'])['proportion_perc'].pct_change()
    # Replace missing values with 0
    year_df['perc_change'].fillna(0, inplace=True)
    month_df['perc_change'].fillna(0, inplace=True)
    week_df['perc_change'].fillna(0, inplace=True)
    # Save dataframes as .csv to output folder
    year_df.to_csv(OUTPUT_FOLDER + 'yearly_trend.csv')
    month_df.to_csv(OUTPUT_FOLDER + 'monthly_trend.csv')
    week_df.to_csv(OUTPUT_FOLDER + 'weekly_trend.csv')

if __name__ == '__main__':
    main()
