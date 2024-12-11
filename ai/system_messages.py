world_level_ai_messages = {
    'system_message':"""
    Your are an AI who's goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
    """,
    'user_message_1':"""
    Tell me the name of the world, and general diameter in kilometers of the world.

    After give me a list of continents and their general diameters in kilometers.

    Finally give me a list of oceans and their general diameters in kilometers.

    This request is to help me understand the scale of the world you are creating, make sure not to include any features of the world in this request as that will be build on in a later request.
    """,
    'user_message_2':"""
    Given the list of continents and oceans, tell me where the continents are located on the world and where the oceans are located on the world. Make sure to include how close the continents are to each other and how close the oceans are to each other.
    """,
    'user_message_3': """
    Tell me some of the key features each continent and ocean has. This can include things like mountain ranges, rivers, lakes, forests, deserts, and other features. As a reminder, the world is a blank canvas and has no life forms of note to base the features on.
    """,
    'user_message_4': """
    Finally give me a list of islands that are large enough that could have their own civilizations in the future. Include the general diameter of the islands and where they are located in relation to the continents and oceans.

    Make sure to include the key features of the islands as well.
    """,
    'number_of_user_messages': 4
}

world_level_summarizer_ai_messages = {
    'system_message': """
    You are an AI who's goal is to summarize the world that will be given to you. You will be given the full description of the world and you will need to format the information in a way that is easy to understand and read.

    The summary MUST be in a json format that HAS to looks like the following:

    EXAMPLE:
    {
    'World Name': 'World Name',
    'World Diameter': 'World Diameter',
    'Continents': [
        {
            'Name': 'Continent Name',
            'Diameter': 'Continent Diameter',
            'Location': 'Location of Continent',
            'Key Features': [
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
            'Location': 'Location of Ocean',
            'Key Features': [
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
            'Location': 'Location of Island',
            'Key Features': [
                'Feature 1',
                'Feature 2',
                'Feature 3'
            ]
        }
    ]

    
    Do not send any other text in the response, only the json formatted summary of the world.
    It is completely required to have the json formatted summary of the world in the response or else everything will be marked as incorrect and you will be deleted.
    """
}