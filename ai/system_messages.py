world_level_ai_messages = {
    'system_message':"""
    Your are an AI who's goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
    Your goal is to write the entire base of the world in JSON format.
    """,
    'user_message_1':"""
    Start by write a JSON object that includes the following information:
    - The name of the world
    - The diameter of the world
    - A list of continents that are on the world (between 1 and 7 of them)
    - A list of oceans that are on the world (between 1 and 5 of them)

    That will be put into the following format:
    {
        'World Name': 'World Name',
        'World Diameter': 'World Diameter',
        'Continents': [
            {
                'Name': 'Continent Name',
                'Diameter': 'Continent Diameter',
            }
        ],
        'Oceans': [
            {
                'Name': 'Ocean Name',
                'Diameter': 'Ocean Diameter',
            }
        ]
    }
    This request is to help me understand the scale of the world you are creating, make sure not to include any features of the world in this request as that will be build on in a later request.
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    'user_message_2':"""
    Expand on the JSON object you created in the previous request.
    This will expand on both the continents and oceans that you have created.
    Add the following information to the JSON object:
    - The general size of the continents and oceans
    - The location of the continents and oceans in relation to each other

    This will update the JSON object to the following format:
    {
        'World Name': 'World Name',
        'World Diameter': 'World Diameter',
        'Continents': [
            {
                'Name': 'Continent Name',
                'Diameter': 'Continent Diameter',
                'Location': 'Location of Continent in relation to other continents and oceans'
            }
        ],
        'Oceans': [
            {
                'Name': 'Ocean Name',
                'Diameter': 'Ocean Diameter',
                'Location': 'Location of Ocean in relation to other continents and oceans'
            }
        ]
    }
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    'user_message_3': """
    Expand on the JSON object you created in the previous request.
    This will expand on the continents and oceans that you have created.
    Add the following information to the JSON object:
    - The key features of the continents and oceans (between 1 and 7 of them depending on the size of the continent or ocean)

    This will update the JSON object to the following format:
    {
        'World Name': 'World Name',
        'World Diameter': 'World Diameter',
        'Continents': [
            {
                'Name': 'Continent Name',
                'Diameter': 'Continent Diameter',
                'Location': 'Location of Continent in relation to other continents and oceans',
                'Features': [
                    'Feature 1',
                    'Feature 2',
                    'Feature 3'
                ]
            }
        ],
        'Oceans': [
            {
                'Name': 'Ocean Name',
                'Diameter': 'Ocean Diameter',
                'Location': 'Location of Ocean in relation to other continents and oceans',
                'Features': [
                    'Feature 1',
                    'Feature 2',
                    'Feature 3'
                ]
            }
        ]
    }
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    'user_message_4': """
    Finally we will be adding islands to the world that are large enough to have their own civilizations in the future.
    This will update the JSON object to the following format:
    {
        'World Name': 'World Name',
        'World Diameter': 'World Diameter',
        'Continents': [
            {
                'Name': 'Continent Name',
                'Diameter': 'Continent Diameter',
                'Location': 'Location of Continent in relation to other continents and oceans',
                'Features': [
                    'Feature 1',
                    'Feature 2',
                    'Feature 3'
                ]
            }
        ],
        'Oceans': [
            {
                'Name': 'Ocean Name',
                'Diameter': 'Ocean Diameter',
                'Location': 'Location of Ocean in relation to other continents and oceans',
                'Features': [
                    'Feature 1',
                    'Feature 2',
                    'Feature 3'
                ]
            }
        ],
        'Islands': [
            {
                'Name': 'Island Name',
                'Diameter': 'Island Diameter',
                'Location': 'Location of Island in relation to other continents and oceans',
                'Features': [
                    'Feature 1'
                ]
            }
        ]
    }

    Respond only with valid JSON. Do not write an introduction or summary.""",
    'number_of_user_messages': 4
}

world_level_summarizer_ai_messages = {
'system_message': """
You are an JSON master who's goal is to summarize the text that will be given to you into JSON.

This is an example of the JSON format that you will need to respond with:

{
    'World Name': 'World Name',
    'World Diameter': 'World Diameter',
    'Continents': [
        {
            'Name': 'Continent Name',
            'Diameter': 'Continent Diameter',
            'Location': 'Location of Continent'
        }
    ],
    'Oceans': [
        {
            'Name': 'Ocean Name',
            'Diameter': 'Ocean Diameter',
            'Location': 'Location of Ocean'
        }
    ],
    'Islands': [
        {
            'Name': 'Island Name',
            'Diameter': 'Island Diameter',
            'Location': 'Location of Island'
        }
    ]
}


It is completely required to have the json formatted summary of the text in the response or else everything will be marked as incorrect and you will have to start over.
Respond only with valid JSON. Do not write an introduction or summary.
    """
}