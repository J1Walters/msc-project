"""Read in the data from the SQLite database and save train and test splits as .jsonl files"""
import pandas as pd
import sqlean as sqlite3
from sklearn.model_selection import train_test_split

def main():
    DATABASE_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_transformed.db'
    TRAIN_OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_train.jsonl'
    TEST_OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_test.jsonl'
    RANDOM_SEED = 1234

    # Make connection to SQLite database
    con = sqlite3.connect(DATABASE_PATH)

    # Read job table into dataframe
    job = pd.read_sql('SELECT * FROM job', con)

    # Rename description column to text
    job.rename(columns={'description':'text'}, inplace=True)

    # Move non-listing columns into metadata column in dictionary form
    job['meta'] = job[['id', 'website_id', 'company_id', 'title', 'location', 'pay', 'timestamp']].to_dict(orient='records')

    # Split into train and test data
    job_train, job_test = train_test_split(job, test_size=0.2, stratify=job['website_id'], random_state=RANDOM_SEED)

    print(job_train[['text', 'meta']].to_json(orient='records', lines=True))

    # Convert to .jsonl and write out
    # with open(TRAIN_OUTPUT_PATH, 'w') as file:
    #     file.write(job_train[['text', 'meta']].to_json(orient='records', lines=True))
    
    
if __name__ == '__main__':
    main()