import pandas as pd
import sqlean as sqlite3
import spacy

MODEL_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Large Models/charembed_bilstm_vec_60_20/model-best'
DATA_PATH = './location_data/location.csv'
OUTPUT_PATH = './entities/raw/charembed_bilstm_vec_ents.csv'

def main():
    # Load spaCy model
    nlp = spacy.load(MODEL_PATH)
    # Import job data
    df = pd.read_csv(DATA_PATH)
    # Get named entities from job description
    df['ents'] = df['description'].apply(get_entities, nlp=nlp)
    # Get each row to correspond to a single named entity
    entities = df.explode('ents')['ents']
    # Turn series to dataframe and split the tuple into two columns
    ent_df = pd.DataFrame(entities.to_list())
    ent_df.columns = ['ent', 'type']
    # Export the dataframe to .csv
    ent_df.to_csv(OUTPUT_PATH)

def get_entities(text, nlp):
    """Return the named entities"""
    return [(ent.text, ent.label_) for ent in nlp(text).ents]

if __name__ == '__main__':
    main()
