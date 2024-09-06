import pandas as pd
import sqlean as sqlite3
from functools import partial
from time import time
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

DATABASE_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Data/joblistings_transformed.db'
OUTPUT_PATH = 'C:/University/6G7V0007_MSC_Project/Project/Code/msc-project/location_data/location.csv'

def main():
    # Get start time
    start = time.time()
    # Import job data
    df = import_data(DATABASE_PATH)
    # Clean data
    clean_df = clean_data(df)
    # Define geocoder objects
    geolocator = Nominatim(user_agent='msc_project')
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    # Get full location with geocoder
    print('Getting location info...')
    clean_df['full_loc'] = clean_df['location'].apply(partial(geocode, language='en', country_codes='gb', addressdetails=True))
    print('Done!')
    clean_df.loc[clean_df['location'].isin(['Remote', 'Multiple Locations']), 'full_loc'] = None
    # Get raw location data
    clean_df['raw_loc'] = clean_df['full_loc'].apply(lambda x: x.raw if x is not None else None)
    # Get latitude and longitude
    clean_df['lat'] = clean_df['full_loc'].apply(lambda x: x.latitude if x is not None else None)
    clean_df['long'] = clean_df['full_loc'].apply(lambda x: x.longitude if x is not None else None)
    # Get settlement and country (within UK) from raw location data
    clean_df['settlement'] = clean_df['raw_loc'].apply(get_settlement)
    clean_df['state'] = clean_df['raw_loc'].apply(get_state)
    # Export data
    clean_df.to_csv(OUTPUT_PATH)
    # Get end time and display time taken in minutes
    end = time.time()
    time_taken = (end - start) / 60
    print(f'Time Taken: {time_taken} minutes')

def import_data(path):
    """Import data from sqlite db to dataframe"""
    con = sqlite3.connect(path)
    job = pd.read_sql('SELECT * FROM job', con)
    return job

def clean_data(df):
    """Clean data"""
    # Remove mentions of hybrid in location
    df['location'].replace(r'\(Hybrid\)', '', regex=True, inplace=True)
    # Remove first line of address
    df['location'].replace(r'^[a-zA-Z0-9-.’\'\s]*,([a-zA-Z0-9-\s]*,)*', '', regex=True, inplace=True)
    # Remove company name where format is 'x in y'
    df['location'].replace(r'^[a-zA-Z0-9-.’\'\s]*\sin', '', regex=True, inplace=True)
    # Strip whitespace
    df['location'] = df['location'].str.strip()
    # Map multiple locations to separate category
    df['location'].replace(r'.*\sand\s.*', 'Multiple Locations', regex=True, inplace=True)
    df['location'].replace(r'.*\s[&+]\s.*', 'Multiple Locations', regex=True, inplace=True)
    df['location'].replace('Multiple UK Locations', 'Multiple Locations', inplace=True)
    df['location'].replace('Multiple Worldwide Locations', 'Multiple Locations', inplace=True)
    return df

def get_settlement(raw_loc):
    try:
        address = raw_loc['address']
    except:
        return None
    try:
        return address['town']
    except:
        try:
            return address['village']
        except:
            try:
                return address['city']
            except:
                return None

def get_state(raw_loc):
    try:
        address = raw_loc['address']
        return address['state']
    except:
        return None

if __name__ == '__main__':
    main()
