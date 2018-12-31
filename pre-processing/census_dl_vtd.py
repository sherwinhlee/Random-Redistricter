import glob
import os
import unzip as uz
from urllib import request as rq

PARENT = os.path.realpath('..')
IN_DIR = PARENT + '\\data\\raw\\'
CEN_ROOT = 'https://www2.census.gov/census_2010/01-Redistricting_File--PL_94-171/'

states = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District_of_Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New_Hampshire',
    'NJ': 'New_Jersey',
    'NM': 'New_Mexico',
    'NY': 'New_York',
    'NC': 'North_Carolina',
    'ND': 'North_Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode_Island',
    'SC': 'South_Carolina',
    'SD': 'South_Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West_Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
}

for folder in glob.iglob(IN_DIR + '*/'):
    state = folder[-3:-1]
    print('Downloading ' + state.upper() + '...')
    state_link = CEN_ROOT + states[state.upper()] + '/' + state + '2010.pl.zip'
    save_path = IN_DIR + state + '\\' + state + '2010.pl.zip'
    rq.urlretrieve(state_link, save_path)
    uz.extract(save_path, IN_DIR + state + '\\')