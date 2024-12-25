

world_level_ai_messages = {
    "system_message":"""
Your are an AI who"s goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
Your goal is to write the entire base of the world in JSON format.
    """,
    "user_message_1":"""
    Start by write a JSON object that includes the following information:
    - A list of Continents that are on the world (between 1 and 7 of them)
    - A list of Oceans that are on the world (between 1 and 5 of them)
    - A list of Islands that are on the world (between 4 and 12 of them)

    That will be put into the following format:
    {
        "World Name": "<World Name>",
        "World Diameter in km": "<World Diameter>",
        "Continents": [
            {
                "Name": "<Continent Name>",
                "Diameter in km": "<Continent Diameter>",
                "Position": ["<Latitude>", "<Longitude>"],
                "Features": ["<Feature 1>", "<Feature 2>"]
            }
        ],
        "Oceans": [
            {
                "Name": "<Ocean Name>",
                "Diameter in km": "<Ocean Diameter>",
                "Features": ["<Feature 1>", "<Feature 2>"],
                "Continents Touching": ["<Continent 1 Name>", "<Continent 2 Name>"]
            }
        ],
        "Islands": [
            {
                "Name": "<Island Name>",
                "Diameter in km": "<Island Diameter>",
                "Features": ["<Feature 1>"]
            }
        ]
    }
    The Number of features depends on the size of the object, larger objects can have more features and smaller objects can have less features.

    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    "format": {
        "type": "object",
        "properties": {
            "World Name": {"type": "string"},
            "World Diameter in km": {"type": "number"},
            "Continents": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Diameter in km": {"type": "number"},
                        "Position": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Features": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["Name", "Diameter in km", "Position", "Features"]
                }
            },
            "Oceans": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Diameter in km": {"type": "number"},
                        "Features": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Continents Touching": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["Name", "Diameter in km", "Features", "Continents Touching"]
                }
            },
            "Islands": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Diameter in km": {"type": "number"},
                        "Features": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["Name", "Diameter in km", "Features"]
                }
            }
        },
        "required": ["World Name", "World Diameter in km", "Continents", "Oceans", "Islands"],
    },
    "number_of_user_messages": 1
}

continent_level_ai_messages = {
    "system_message": """
our are an AI who"s goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
Your goal is to write a single continent of the world in JSON format.
""",
    "user_message_1": """
Update the following JSON object:
{JSON Object}

The new JSON object should follow the following format and make sure not to remove any of the existing data:
{
    "Name": "<Continent Name>",
    "Diameter in km": "<Continent Diameter>",
    "Position": ["<Latitude>", "<Longitude>"],
    "Features": ["<Feature 1>", "<Feature 2>"],
    "Climate": {
        "Average Temperature in C": <Temperature as Number>,
        "Weather Patterns": "<Weather Patterns>"
    },
    "Regions": [
        {
            "Name": "<Region Name>",
            "Diameter in km": "<Region Diameter>",
            "Position": ["<Latitude>", "<Longitude>"],
            "Landmarks": [{"Name": "<Landmark Name>", "Type": "<Landmark Type>", "Myth": "<Landmark Myth>"}],
            "Resources": ["<Resource 1>", "<Resource 2>"]
        }
    ]
}
Depending on the size of the continent, the number of features, regions, landmarks, and resources can vary.
Again, make sure not to remove any of the existing data or create any objects not in the format above.
Respond only with valid JSON. Do not write an introduction or summary.
""",
    "format": {
        "type": "object",
        "properties": {
            "Name": {"type": "string"},
            "Diameter in km": {"type": "number"},
            "Position": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Features": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Climate": {
                "type": "object",
                "properties": {
                    "Average Temperature in C": {"type": "number"},
                    "Weather Patterns": {"type": "string"}
                },
                "required": ["Average Temperature in C", "Weather Patterns"]
            },
            "Regions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Diameter in km": {"type": "number"},
                        "Position": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Landmarks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Name": {"type": "string"},
                                    "Type": {"type": "string"},
                                    "Myth": {"type": "string"}
                                },
                                "required": ["Name", "Type", "Myth"]
                            }
                        },
                        "Resources": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["Name", "Diameter in km", "Position", "Landmarks", "Resources"]
                }
            }
        },
        "required": ["Name", "Diameter in km", "Position", "Features", "Climate", "Regions"]
    },
    "number_of_user_messages": 1
}

region_level_ai_messages = {
    "system_message": """
our are an AI who"s goal is to create an entirely new and unheard of world. This world will be completely barron from any civilizations and will be a blank canvas for civilization to be created.
Your goal is to write a single region of the world in JSON format and start populating the regions for civilization to be put in.
""",
    "user_message_1": """
Update the following JSON object:
{JSON Object}

The new JSON object should follow the following format and make sure not to remove any of the existing data:
{
    "Name": "<Region Name>",
    "Diameter in km": "<Region Diameter>",
    "Position": ["<Latitude>", "<Longitude>"],
    "Landmarks": [{"Name": "<Landmark Name>", "Type": "<Landmark Type>", "Myth": "<Landmark Myth>"}],
    "Resources": ["<Resource 1>", "<Resource 2>"],
    "Civilizations": [
        {
            "Name": "<Civilization Name>",
            "Type": "<Civilization Type (City, Large Town, Small Town, Village, Hamlet)>",
            "Population": <Population as Number, this should based on the Civilization Type>,
            "Diameter in km": "<Civilization Diameter>",
            "Government": "<Government Type>",
            "Position": ["<Latitude>", "<Longitude>"],
            "Description": "<Civilization Description>"
        }
    ]
}
Depending on the size of the region, the Type will vary which will make the Population vary.
Make sure to make to create 3 to 9 civilizations in the region depending on the size of the region.

Again, make sure not to remove any of the existing data or create any objects not in the format above.
You Can Not create any new regions or continents, only update the existing region.
Respond only with valid JSON. Do not write an introduction or summary.
""",
    "format": {
        "type": "object",
        "properties": {
            "Regions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Diameter in km": {"type": "number"},
                        "Position": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Landmarks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Name": {"type": "string"},
                                    "Type": {"type": "string"},
                                    "Myth": {"type": "string"}
                                },
                                "required": ["Name", "Type", "Myth"]
                            }
                        },
                        "Resources": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Civilizations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Name": {"type": "string"},
                                    "Type": {"type": "string"},
                                    "Population": {"type": "number"},
                                    "Diameter in km": {"type": "number"},
                                    "Government": {"type": "string"},
                                    "Position": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    },
                                    "Description": {"type": "string"}
                                },
                                "required": ["Name", "Type", "Population", "Diameter in km", "Government", "Position", "Description"]
                            }
                        }
                    }
                },
                "required": ["Name", "Diameter in km", "Position", "Landmarks", "Resources", "Civilizations"]
            },
            "Name": {"type": "string"},
            "Diameter in km": {"type": "number"},
            "Position": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Features": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Climate": {
                "type": "object",
                "properties": {
                    "Average Temperature in C": {"type": "number"},
                    "Weather Patterns": {"type": "string"}
                },
                "required": ["Average Temperature in C", "Weather Patterns"]
            }
        },
        "required": ["Regions", "Name", "Diameter in km", "Position", "Features", "Climate"]
    },
    "number_of_user_messages": 1
}

district_level_ai_messages = {
    "system_message": """
You are an AI who"s goal is to create an entirely new and unheard of world. With the goal of adding more detail to the world, you will be adding a new districts to a given civilization.
These districts need to be unique and have a purpose in the civilization.
    """,
    "user_message_1": """
Generate 1 to 10 districts for the civilization depending on population and type of civilization. A City will have more districts than a town or village. Where as a Hamlet might only have 1 district.
A City should have between 5 and 10 districts, a Large Town should have between 3 and 7 districts, a Small Town should have between 2 and 5 districts, a Village should have between 1 and 3 districts, and a Hamlet should have 1 district.
Each Civilization should have at least 1 Residential District.

Update the following JSON object:
{JSON Object}

The new JSON object should follow the following format and make sure not to remove any of the existing data:
{
    "Name": "<Civilization Name>",
    "Type": "<Civilization Type (City, Large Town, Small Town, Village, Hamlet)>",
    "Population": <Population as Number>,
    "Diameter in km": "<Civilization Diameter>",
    "Government": "<Government Type>",
    "Position": ["<Latitude>", "<Longitude>"],
    "Description": "<Civilization Description>",
    "Districts": [
        {
            "Name": "<District Name>",
            "Type": "<District Type (Residential, Commercial, Industrial, Agricultural, Government, Recreational, Educational, Religious)>",
            "Population": <Population as Number>,
            "Diameter in km": "<District Diameter>",
            "Position": ["<Latitude>", "<Longitude>"],
            "Description": "<District Description>"
        }
    ]
}

Make sure to make the Districts unique and have a purpose in the civilization.
Make sure the total Population of the Districts does not exceed the Population of the Civilization.
Again, make sure not to remove any of the existing data or create any objects not in the format above.
Respond only with valid JSON. Do not write an introduction or summary.
    """,
    "format": {
        "type": "object",
        "properties": {
            "Name": {"type": "string"},
            "Type": {"type": "string"},
            "Population": {"type": "number"},
            "Diameter in km": {"type": "number"},
            "Government": {"type": "string"},
            "Position": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Description": {"type": "string"},
            "Districts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Type": {"type": "string"},
                        "Population": {"type": "number"},
                        "Diameter in km": {"type": "number"},
                        "Position": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Type", "Population", "Diameter in km", "Position", "Description"]
                }
            }
        },
        "required": ["Name", "Type", "Population", "Diameter in km", "Government", "Position", "Description", "Districts"]
    },
    "number_of_user_messages": 1
}

