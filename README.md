# Analysing the UK Tech Job Market With NLP

## About
Main repository for MSc project.

## Contents
- Configs:
Contains the spaCy config files used for training the named entity recognition (NER) models

- Entities:
Contains .csv files with the named entities extracted from the corpus using different models. The `clean` sub-folder contains the named entities after mapping.

- Location_Data:
Contains the .csv file containing geocoded jobs.

- Models:
Contains the trained NER models without word vectors. Models with word vectors are too large to fit in a repository.

- Notebooks:
    - `entity_extraction.ipynb`: Prototyping for extracting named entities.
    - `entity_plots.ipynb`: Prototyping for plotting extracted entities.
    - `entity_visualisation.ipynb`: Prototyping entity display within a job listing using displaCy.
    - `location_map.ipynb`: Prototyping for mapping locations on a map.
    - `pos_visualisation.ipynb`: Some POS and NER visualisations for report figures.
    - `preprocessing.ipynb`: Experimentation with TF-IDF and BERTopic clustering.
    - `prototyping.ipynb`: Contains some TF-IDF experimentation.
    - `survey_analysis.ipynb`: Visualisation of survey responses.
    - `testing_ner.ipynb`: Contains CLI query for testing NER models.
    - `testing_visualisation.ipynb`: Plots of test set performance for the various NER models.
    - `trend_extraction.ipynb`: Prototyping for extracting trends from entities.

- Survey_Data:
Contains .csv file of survey responses.

- Test_Results:
Contains the .json files with the results obtained from `testing_ner.ipynb`.

- Trend_Data:
Contains the .csv files containing the trend data for yearly, monthly and weekly time periods.

- `entity_cleaning.py`
Script for mapping the extracted named entities into broader groups.

- `entity_extraction.py`
Script for extracting named entities from the job listings using provided model.

- `geocoding.py`
Script for geocoding the job listings to get locations ready for plotting.

- `prep_data_for_training.py`
Script to split data into train, development and test sets.

- `trend_extraction.py`
Script to extract yearly, monthly and weekly trends from named entities.
