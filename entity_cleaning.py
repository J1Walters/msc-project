import pandas as pd

DATA_PATH = './entities/raw/multihash_maxout_vec_ents.csv'
OUTPUT_PATH = './entities/clean/'

def main():
    df = pd.read_csv(DATA_PATH, index_col=0)
    df['new_ent'] = df['ent'].str.upper()
    map_lang_fram(df)
    map_h_skill(df)
    map_s_skill(df)
    map_req(df)
    test = df.loc[df['type'] == 'H_SKILL', 'new_ent'].value_counts()
    print(test.head(40))
    print(test.loc[test.index.str.contains('NETWORKING')])

def map_lang_fram(df):
    """Mapping for entities of the technology, languages and frameworks type"""
    # Filter for entities of the lang_fram type
    is_lang_fram = df['type'] == 'LANG_FRAM'
    # Mapping for machine learning
    df.loc[(is_lang_fram) & (df['new_ent'] == 'ML'), 'new_ent'] = 'MACHINE LEARNING'
    # Mapping for cloud services
    df.loc[(is_lang_fram) & (df['new_ent'].str.contains('CLOUD', na=False)), 'new_ent'] = 'CLOUD (GC, AWS, AZURE, ETC.)'
    df.loc[(is_lang_fram) & (df['new_ent'] == 'AZURE'), 'new_ent'] = 'CLOUD (GC, AWS, AZURE, ETC.)'
    df.loc[(is_lang_fram) & (df['new_ent'] == 'AWS'), 'new_ent'] = 'CLOUD (GC, AWS, AZURE, ETC.)'
    # Mapping for version control
    df.loc[(is_lang_fram) & (df['new_ent'].str.contains('VERSION CONTROL', na=False)), 'new_ent'] = 'VERSION CONTROL (GIT, GITHUB, GITLAB, ETC.)'
    df.loc[(is_lang_fram) & (df['new_ent'].str.contains('GIT', na=False)), 'new_ent'] = 'VERSION CONTROL (GIT, GITHUB, GITLAB, ETC.)'
    # Mapping for APIs
    df.loc[(is_lang_fram) & (df['new_ent'].str.contains('API', na=False)), 'new_ent'] = 'APIS (SOAP, REST, ETC.)'

def map_h_skill(df):
    """Mapping for entities of the hard skill type"""
    # Filter for entities of the hard skill type
    is_h_skill = df['type'] == 'H_SKILL'
    # Mapping for agile
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('AGILE', na=False)), 'new_ent'] = 'AGILE'
    # Mapping for CI/CD
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('CONTINUOUS INTEGRATION', na=False)), 'new_ent'] = 'CI/CD'
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('CONTINUOUS DELIVERY', na=False)), 'new_ent'] = 'CI/CD'
    # Mapping for deployment
    df.loc[(is_h_skill) & (df['new_ent'] == 'DEPLOY'), 'new_ent'] = 'DEPLOYMENT'
    df.loc[(is_h_skill) & (df['new_ent'] == 'DEPLOYING'), 'new_ent'] = 'DEPLOYMENT'
    # Mapping for NLP
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('NLP', na=False)), 'new_ent'] = 'NLP'
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('NATURAL LANGUAGE', na=False)), 'new_ent'] = 'NLP'
    # Mapping for coding/programming
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('CODING', na=False)), 'new_ent'] = 'CODING/PROGRAMMING'
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('PROGRAMMING', na=False)), 'new_ent'] = 'CODING/PROGRAMMING'
    # Mapping for troubleshooting
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('TROUBLESHOOTING', na=False)), 'new_ent'] = 'TROUBLESHOOTING'
    # Mapping for development
    df.loc[(is_h_skill) & (df['new_ent'] == 'DEVELOP'), 'new_ent'] = 'DEVELOPMENT'
    df.loc[(is_h_skill) & (df['new_ent'] == 'DEVELOPING'), 'new_ent'] = 'DEVELOPMENT'
    df.loc[(is_h_skill) & (df['new_ent'] == 'SOFTWARE DEVELOPMENT'), 'new_ent'] = 'DEVELOPMENT'
    # Mapping for testing
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('TESTING', na=False)), 'new_ent'] = 'TESTING'
    # Mapping for data visualisation
    df.loc[(is_h_skill) & (df['new_ent'] == 'DATA VISUALIZATION'), 'new_ent'] = 'DATA VISUALISATION'
    # Mapping for tech support
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('TECHNICAL SUPPORT', na=False)), 'new_ent'] = 'TECHNICAL SUPPORT'
    # Mapping for data analysis
    df.loc[(is_h_skill) & (df['new_ent'].str.contains('DATA')) & (df['new_ent'].str.contains('ANALYS')), 'new_ent'] = 'DATA ANALYSIS'
    # Mapping for implementation
    df.loc[(is_h_skill) & (df['new_ent'] == 'IMPLEMENT'), 'new_ent'] = 'IMPLEMENTATION'
    # Mapping for maintenance
    df.loc[(is_h_skill) & (df['new_ent'] == 'MAINTAIN'), 'new_ent'] = 'MAINTENANCE'
    

def map_s_skill(df):
    """Mapping for entities of the soft skill type"""
    # Filter for entities of soft skill type
    is_s_skill = df['type'] == 'S_SKILL'
    # Mapping for teamwork and collaboration
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('TEAM', na=False)), 'new_ent'] = 'COLLABORATION AND TEAMWORK'
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('COLLABORAT', na=False)), 'new_ent'] = 'COLLABORATION AND TEAMWORK'
    # Mapping for communication skills both verbal and written
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('COMMUNICAT', na=False)), 'new_ent'] = 'COMMUNICATION'
    # Mapping for passion and enthusiasm
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('PASSION', na=False)), 'new_ent'] = 'PASSION AND ENTHUSIASM'
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('ENTHUSIA', na=False)), 'new_ent'] = 'PASSION AND ENTHUSIASM'
    # Mapping for leadership
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('LEAD', na=False)), 'new_ent'] = 'LEADERSHIP'
    # Mapping for analytical thinking and problem solving
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('ANALYTIC', na=False)), 'new_ent'] = 'ANALYTICAL THINKING AND PROBLEM SOLVING'
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('PROBLEM', na=False)) & (df['new_ent'].str.contains('SOLV', na=False)),
           'new_ent'] = 'ANALYTICAL THINKING AND PROBLEM SOLVING'
    df.loc[(is_s_skill) & (df['new_ent'] == 'PROBLEM'), 'new_ent'] = 'ANALYTICAL THINKING AND PROBLEM SOLVING'
    df.loc[(is_s_skill) & (df['new_ent'] == 'SOLVING'), 'new_ent'] = 'ANALYTICAL THINKING AND PROBLEM SOLVING'
    # Mapping for independent working
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('INDEPENDENT', na=False)), 'new_ent'] = 'INDEPENDENT WORKING'
    # Mapping for proactivity
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('PROACTIVE', na=False)), 'new_ent'] = 'PROACTIVE'
    # Mapping willingness to learn 
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('LEARN', na=False)), 'new_ent'] = 'WILLING TO LEARN'
    # Mapping interpersonal skills
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('INTERPERSONAL', na=False)), 'new_ent'] = 'INTERPERSONAL SKILLS'
    # Mapping for flexibility
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('FLEXIB', na=False)), 'new_ent'] = 'FLEXIBLE'
    # Mapping for driven and motivated
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('DRIVEN', na=False)), 'new_ent'] = 'DRIVEN AND MOTIVATED'
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('MOTIVAT', na=False)), 'new_ent'] = 'DRIVEN AND MOTIVATED'
    # Mapping for time management
    df.loc[(is_s_skill) & (df['new_ent'].str.contains('TIME', na=False)), 'new_ent'] = 'TIME MANAGEMENT'
    
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
    df.loc[(is_req) & (df['new_ent'] == 'BS'), 'new_ent'] = "BACHELOR'S"
    df.loc[(is_req) & (df['new_ent'] == 'BS DEGREE'), 'new_ent'] = "BACHELOR'S"
    df.loc[(is_req) & (df['new_ent'] == 'BA'), 'new_ent'] = "BACHELOR'S"
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