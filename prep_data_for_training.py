"""Read in the data from the SQLite database and save train and test splits as .json files"""
import pandas as pd
import sqlean as sqlite3
from sklearn.model_selection import train_test_split

def main():
    DATABASE_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_transformed_OG_05072024.db'
    TRAIN_OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_train.json'
    DEV_OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_dev.json'
    TEST_OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_test.json'
    RANDOM_SEED = 1234

    # Make connection to SQLite database
    con = sqlite3.connect(DATABASE_PATH)

    # Read job table into dataframe
    job = pd.read_sql('SELECT * FROM job', con)

    # Rename description column to text
    job.rename(columns={'description':'my_text'}, inplace=True)

    # Move non-listing columns into metadata column in dictionary form
    job['meta'] = job[['id', 'website_id', 'company_id', 'title', 'location', 'pay', 'timestamp']].to_dict(orient='records')

    # Move text and metadata into data column to comply with Label Studio .json format
    job['data'] = job[['my_text', 'meta']].to_dict(orient='records')

    # Split into train and test data
    job_train, job_test = train_test_split(job, train_size=0.6, stratify=job['website_id'], random_state=RANDOM_SEED)
    
    # Split test into dev and test
    job_dev, job_test = train_test_split(job_test, train_size=0.5, stratify=job_test['website_id'], random_state=RANDOM_SEED)

    # Convert to .json and write out
    with open(TRAIN_OUTPUT_PATH, 'w', encoding='utf-8') as file:
        file.write(job_train[['data']].to_json(orient='records'))

    with open(DEV_OUTPUT_PATH, 'w', encoding='utf-8') as file:
        file.write(job_dev[['data']].to_json(orient='records'))

    with open(TEST_OUTPUT_PATH, 'w', encoding='utf-8') as file:
        file.write(job_test[['data']].to_json(orient='records'))

if __name__ == '__main__':
    main()
