import pandas as pd
import sqlean as sqlite3
import spacy

MODEL_PATH = './models/colab_charembed_bilstm_60_20_annot/model-best'
DATA_PATH = './location_data/location.csv'
OUTPUT_PATH = './entities/raw/charembed_bilstm_ents.csv'

def main():
    # Load spaCy model
    nlp = spacy.load(MODEL_PATH)
    # Import job data
    df = pd.read_csv(DATA_PATH)
    # Get named entities from job description
    df['ents'] = df['description'].apply(get_entities, nlp=nlp)
    # Get each row to correspond to a single named entity and include timestamp
    entities = df.explode('ents')[['ents', 'timestamp']]
    # # DEBUG
    # print(entities)
    # Split the tuple into two columns
    entities[['ent', 'type']] = pd.DataFrame(entities['ents'].to_list(), index=entities.index)
    entities.drop(columns=['ents'], inplace=True)
    # # DEBUG
    # print(entities)
    # Export the dataframe to .csv
    entities.to_csv(OUTPUT_PATH)

def get_entities(text, nlp):
    """Return the named entities"""
    return [(ent.text, ent.label_) for ent in nlp(text).ents]

if __name__ == '__main__':
    main()
