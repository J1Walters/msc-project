import pandas as pd
import sqlean as sqlite3
import spacy

MODEL_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Large Models/charembed_bilstm_vec_60_20/model-best'
DATABASE_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_transformed.db'
OUTPUT_PATH = './entities/raw/charembed_bilstm_vec_ents.csv'

def main():
    # Load spaCy model
    nlp = spacy.load(MODEL_PATH)
    # Import job data
    df = import_data(DATABASE_PATH)
    # Get named entities from job description
    df['ents'] = df['description'].apply(get_entities, nlp=nlp)
    # Get each row to correspond to a single named entity
    entities = df.explode('ents')['ents']
    # Turn series to dataframe and split the tuple into two columns
    ent_df = pd.DataFrame(entities.to_list())
    ent_df.columns = ['ent', 'type']
    # Export the dataframe to .csv
    ent_df.to_csv(OUTPUT_PATH)

def import_data(path):
    """Import data from sqlite db to dataframe"""
    con = sqlite3.connect(path)
    job = pd.read_sql('SELECT * FROM job', con)
    return job

def get_entities(text, nlp):
    """Return the named entities"""
    return [(ent.text, ent.label_) for ent in nlp(text).ents]

if __name__ == '__main__':
    main()
