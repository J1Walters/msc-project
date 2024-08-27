import pandas as pd

DATA_PATH = './entities/raw/multihash_maxout_ents.csv'
OUTPUT_PATH = './entities/clean/'

def main():
    df = pd.read_csv(DATA_PATH, index_col=0)
    df['new_ent'] = df['ent'].str.upper()
    map_req(df)
    print(df.head(10))
    test = df.loc[df['type'] == 'S_SKILL', 'new_ent'].value_counts()
    print(test.head(10))
    print(test.loc[test.index.str.contains('TEAM')])

def map_s_skill(df):
    """Mapping for entities of the soft skill type"""
    # Filter for entities of soft skill type
    is_s_skill = df['type'] == 'S_SKILL'
    # Mapping for teamwork and collaboration
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('TEAM', na=False)), 'new_ent'] = "COLLABORATION AND TEAMWORK"
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('COLLABORAT', na=False)), 'new_ent'] = "COLLABORATION AND TEAMWORK"
    # Mapping for communication skills both verbal and written
    

def map_req(df):
    """Mapping for entities of the requirement type"""
    # Filter for entities of requirement type
    is_req = df['type'] == 'REQUIREMENT'
    # Mapping bachelor's degrees
    df.loc[(is_req) & (df['new_ent'].str.contains('BACHELOR', na=False)), 'new_ent'] = "BACHELOR'S"
    df.loc[(is_req) & (df['new_ent'].str.contains('UNDERGRADUATE', na=False)), 'new_ent'] = "BACHELOR'S"
    df.loc[(is_req) & (df['new_ent'] == 'BSC'), 'new_ent'] = "BACHELOR'S"
    df.loc[(is_req) & (df['new_ent'] == 'BENG'), 'new_ent'] = "BACHELOR'S"
    df.loc[(is_req) & (df['new_ent'] == 'B.S.'), 'new_ent'] = "BACHELOR'S"
    # Mapping master's degrees
    df.loc[(is_req) & (df['new_ent'].str.contains('MASTER', na=False)), 'new_ent'] = "MASTER'S"
    df.loc[(is_req) & (df['new_ent'] == 'MSC'), 'new_ent'] = "MASTER'S"
    df.loc[(is_req) & (df['new_ent'] == 'MENG'), 'new_ent'] = "MASTER'S"
    df.loc[(is_req) & (df['new_ent'] == 'MS'), 'new_ent'] = "MASTER'S"
    df.loc[(is_req) & (df['new_ent'] == 'M.S.'), 'new_ent'] = "MASTER'S"
    # Mapping phds
    df.loc[(is_req) & (df['new_ent'].str.contains('PHD', na=False)), 'new_ent'] = 'PHD'
    # Mapping degree classifications
    df.loc[(is_req) & (df['new_ent'].str.contains('2[.:]1', regex=True, na=False)), 'new_ent'] = '2:1'
    df.loc[(is_req) & (df['new_ent'].str.contains('2[.:]2', regex=True, na=False)), 'new_ent'] = '2:2'
    # Mapping generic degrees
    df.loc[(is_req) & (df['new_ent'] == 'RELATED DEGREE'), 'new_ent'] = 'DEGREE'
    # Mapping GCSEs
    df.loc[(is_req) & (df['new_ent'].str.contains('GCSE', na=False)), 'new_ent'] = 'GCSE'
    # Mapping driving license
    df.loc[(is_req) & (df['new_ent'].str.contains('DRIVING', na=False)), 'new_ent'] = 'DRIVING LICENSE'
    # Certifications
    df.loc[(is_req) & (df['new_ent'].str.contains('ITIL', na=False)), 'new_ent'] = 'ITIL'
    df.loc[(is_req) & (df['new_ent'].str.contains('CISSP', na=False)), 'new_ent'] = 'CISSP'

if __name__ == '__main__':
    main()