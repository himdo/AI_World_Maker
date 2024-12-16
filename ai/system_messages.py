world_level_ai_messages = {
    'system_message':"""
Your are an AI who's goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
Your goal is to write the entire base of the world in JSON format.
    """,
    'user_message_1':"""
    Start by write a JSON object that includes the following information:
    - A list of Continents that are on the world (between 1 and 7 of them)
    - A list of Oceans that are on the world (between 1 and 5 of them)
    - A list of Islands that are on the world (between 4 and 12 of them)

    That will be put into the following format:
    {
        'World Name': '<World Name>',
        'World Diameter in km': '<World Diameter>',
        'Continents': [
            {
                'Name': '<Continent Name>',
                'Diameter in km': '<Continent Diameter>',
                'Position': ['<Latitude>', '<Longitude>'],
                'Features': ['<Feature 1>', '<Feature 2>']
            }
        ],
        'Oceans': [
            {
                'Name': '<Ocean Name>',
                'Diameter in km': '<Ocean Diameter>',
                'Features': ['<Feature 1>', '<Feature 2>'],
                'Continents Touching': ['<Continent 1 Name>', '<Continent 2 Name>']
            }
        ],
        'Islands': [
            {
                'Name': '<Island Name>',
                'Diameter in km': '<Island Diameter>',
                'Features': ['<Feature 1>']
            }
        ]
    }
    The Number of features depends on the size of the object, larger objects can have more features and smaller objects can have less features.

    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    'number_of_user_messages': 1
}

continent_level_ai_messages = {
    'system_message': """
our are an AI who's goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
Your goal is to write a single continent of the world in JSON format.
""",
    'user_message_1': """
Update the following JSON object:
{JSON Object}

The new JSON object should follow the following format and make sure not to remove any of the existing data:
{
    'Name': '<Continent Name>',
    'Diameter in km': '<Continent Diameter>',
    'Position': ['<Latitude>', '<Longitude>'],
    'Features': ['<Feature 1>', '<Feature 2>'],
    'Climate': {
        'Average Temperature in C': <Temperature as Number>,
        'Weather Patterns': '<Weather Patterns>'
    },
    'Regions': [
        {
            'Name': '<Region Name>',
            'Diameter in km': '<Region Diameter>',
            'Position': ['<Latitude>', '<Longitude>'],
            'Landmarks': [{'Name': '<Landmark Name>', 'Type': '<Landmark Type>', 'Myth': '<Landmark Myth>'}],
            'Resources': ['<Resource 1>', '<Resource 2>'],
        }
    ]
}
Depending on the size of the continent, the number of features, regions, landmarks, and resources can vary.
Again, make sure not to remove any of the existing data or create any objects not in the format above.
Respond only with valid JSON. Do not write an introduction or summary.
""",
    'number_of_user_messages': 1
}