import pandas as pd
import spacy

MODEL_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Large_Models/multihash_maxout_vec_60_20/model-best'
DATA_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Code/msc-project/location_data/location.csv'
OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Code/msc-project/entities/raw/multihash_maxout_vec_ents.csv'

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
