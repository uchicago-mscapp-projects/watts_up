import os
# util file for large constants
# contains STATE_NAME_DICT, COL_NAMES,

URL = "https://api.eia.gov/v2/electricity/retail-sales/data/"

API_KEY = os.environ.get("API_KEY")
FREQUENCY = "annual"
PARAMS = {
    "api_key": API_KEY,
    "frequency": FREQUENCY,
    "data[0]": "price",
    "facets[sectorid][]": ["ALL", "COM", "IND", "RES"],
    "facets[stateid][]": [
        "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE",
        "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY",
        "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT",
        "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY",
        "OH", "OK", "OR", "PA", "RI", "SAT", "SC", "SD",
        "TN", "TX", "UT", "VA", "VT", "WA", "WI",
        "WV", "WY"
    ],
    "start": "2004-01",
    "end": "2023-11",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "sort[1][column]": "stateid",
    "sort[1][direction]": "asc",
    "length": 5000
}


STATE_MAPPING_DATA = {
    'state': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'American Samoa', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
                         'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands',
                         'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Trust Territories', 'Utah', 'Vermont', 'Virgin Islands', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
    'stateid': ['AL', 'AK', 'AZ', 'AR', 'AS', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                            'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'MP',
                            'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'TT', 'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY'],
}

STATE_NAME_DICT = {
    'AL': 'ALABAMA',
    'AK': 'ALASKA',
    'AZ': 'ARIZONA',
    'AR': 'ARKANSAS',
    'CA': 'CALIFORNIA',
    'CO': 'COLORADO',
    'CT': 'CONNECTICUT',
    'DC': 'DISTRICT OF COLUMBIA',
    'DE': 'DELAWARE',
    'FL': 'FLORIDA',
    'GA': 'GEORGIA',
    'HI': 'HAWAII',
    'ID': 'IDAHO',
    'IL': 'ILLINOIS',
    'IN': 'INDIANA',
    'IA': 'IOWA',
    'KS': 'KANSAS',
    'KY': 'KENTUCKY',
    'LA': 'LOUISIANA',
    'ME': 'MAINE',
    'MD': 'MARYLAND',
    'MA': 'MASSACHUSETTS',
    'MI': 'MICHIGAN',
    'MN': 'MINNESOTA',
    'MS': 'MISSISSIPPI',
    'MO': 'MISSOURI',
    'MT': 'MONTANA',
    'NE': 'NEBRASKA',
    'NV': 'NEVADA',
    'NH': 'NEW HAMPSHIRE',
    'NJ': 'NEW JERSEY',
    'NM': 'NEW MEXICO',
    'NY': 'NEW YORK',
    'NC': 'NORTH CAROLINA',
    'ND': 'NORTH DAKOTA',
    'OH': 'OHIO',
    'OK': 'OKLAHOMA',
    'OR': 'OREGON',
    'PA': 'PENNSYLVANIA',
    'RI': 'RHODE ISLAND',
    'SC': 'SOUTH CAROLINA',
    'SD': 'SOUTH DAKOTA',
    'TN': 'TENNESSEE',
    'TX': 'TEXAS',
    'UT': 'UTAH',
    'VT': 'VERMONT',
    'VA': 'VIRGINIA',
    'WA': 'WASHINGTON',
    'WV': 'WEST VIRGINIA',
    'WI': 'WISCONSIN',
    'WY': 'WYOMING'
}

COL_NAMES = [
    "YEAR",
    "year_state",
    "state_id",
    "PSTATABB",
    "PNAME",
    "ORISPL",
    "OPRNAME",
    "OPRCODE",
    "UTLSRVNM",
    "UTLSRVID",
    "SECTOR",
    "NERC",
    "SUBRGN",
    "SRNAME",
    "FIPSST",
    "FIPSCNTY",
    "CNTYNAME",
    "LAT",
    "LON",
    "PLPRMFL",
    "PLFUELCT",
    "PLPFGNCT",
    "COALFLAG",
    "CAPFAC",
    "NAMEPCAP",
    "NBFACTOR",
    "PLNGENAN",
    "PLCO2AN",
    "PLGENACL",
    "PLGENAOL",
    "PLGENAGS",
    "PLGENANC",
    "PLGENAHY",
    "PLGENABM",
    "PLGENAWI",
    "PLGENASO",
    "PLGENAGT",
    "PLGENAOF",
    "PLGENAOP",
    "PLGENATN",
    "PLGENATR",
    "PLGENATH",
    "PLGENACY",
    "PLGENACN",
    "FILE",
]


PLANT_TYPE_COLOR = {
    'Gas': 'blue',
    'Coal': 'black',
    'Fossil': 'grey',
    'Wind': 'green',
    'Nuclear': 'orange',
    'Solar': 'yellow',
    'Other': 'purple'
}

plant_type_colors = {
    'Coal': 'color_for_coal',
    'Gas': 'color_for_gas',
    'Nuclear': 'color_for_nuclear',
    'Other': 'color_for_other',
    'Wind': 'color_for_wind',
    'Solar': 'color_for_solar'
}
PLANT_TYPE_ORDER = ['Coal', 'Gas', 'Fossil', 'Nuclear', 'Wind', 'Solar']

WANTED_COLUMNS = {
    'plgenacl': "Coal",
    'plgenags': "Gas",
    'plgenaof': "Fossil",
    'plgenawi': "Wind",
    'plgenanc': "Nuclear",
    'plgenaso': "Solar",
    'other_sources': "Other"
}
