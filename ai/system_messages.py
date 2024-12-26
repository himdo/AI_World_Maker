

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
                }, 
                "minItems": 1,
                "maxItems": 7
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
            "Name": {"const": "{Continent Name}"},
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
                },
                "minItems": 1,
                "maxItems": 10
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
                        "Name": {"const": "{Region Name}"},
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
                                    "Population": {"type": "integer"},
                                    "Diameter in km": {"type": "number"},
                                    "Government": {"type": "string"},
                                    "Position": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    },
                                    "Description": {"type": "string"}
                                },
                                "required": ["Name", "Type", "Population", "Diameter in km", "Government", "Position", "Description"]
                            },
                            "minItems": 3,
                            "maxItems": 9,
                        }
                    }
                },
                "required": ["Name", "Diameter in km", "Position", "Landmarks", "Resources", "Civilizations"]
            },
            "Name": {"const": "{Continent Name}"},
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
            "Name": {"const": "{Civilization Name}"},
            "Type": {"type": "string"},
            "Population": {"type": "integer"},
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
                        "Population": {"type": "integer"},
                        "Diameter in km": {"type": "number"},
                        "Position": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Type", "Population", "Diameter in km", "Position", "Description"]
                },
                "minItems": 5,
                "maxItems": 10
            }
        },
        "required": ["Name", "Type", "Population", "Diameter in km", "Government", "Position", "Description", "Districts"]
    },
    "number_of_user_messages": 1
}

subdistrict_level_ai_messages = {
    "system_message": """
    You are an AI who"s goal is to create an entirely new and unheard of world. With the goal of adding more detail to the world, you will be adding a new subdistricts to a given district.
    These subdistricts need to be unique and have a purpose in the district. There needs to be enough subdistricts to fill the district completely.
    Your goal is to add some granularity to the districts by adding subdistricts.
    """,
    "user_message_1": """
    Generate 1 to 10 subdistricts for the district depending on the size of the district. A smaller district will have less subdistricts than a larger district.
    The goal of this is to split the district into smaller areas so that the civilization can be more detailed.

    Update the following JSON object:
    {JSON Object}

    The new JSON object should follow the following format and make sure not to remove any of the existing data:
    {
        "Name": "<District Name>",
        "Type": "<District Type (Residential, Commercial, Industrial, Agricultural, Government, Recreational, Educational, Religious)>",
        "Population": <Population as Number>,
        "Diameter in km": "<District Diameter>",
        "Position": ["<Latitude>", "<Longitude>"],
        "Description": "<District Description>",
        "Subdistricts": [
            {
                "Name": "<Subdistrict Name>",
                "Population": <Population as Number>,
                "Diameter in km": "<Subdistrict Diameter>",
                "Position": ["<Latitude>", "<Longitude>"],
                "Description": "<Subdistrict Description>",
                "Buildings of Interest": [{"Name": "<Building Name>", "Type": "<Building Type (House, Shop, Other)>", "Description": "<Building Description>"}]
            }
        ]
    }

    Make sure to make the Subdistricts unique and have a purpose in the district.
    Make sure the total Population of the Subdistricts does not exceed the Population of the District.
    The number of Buildings of Interest should be between 1 and 5 depending on the size of the Subdistrict.

    Again, make sure not to remove any of the existing data or create any objects not in the format above.
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    "format": {
        "type": "object",
        "properties": {
            "Name": {"const": "{District Name}"},
            "Type": {"type": "string"},
            "Population": {"type": "integer"},
            "Diameter in km": {"type": "number"},
            "Position": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Description": {"type": "string"},
            "Subdistricts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Population": {"type": "integer"},
                        "Diameter in km": {"type": "number"},
                        "Position": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "Description": {"type": "string"},
                        "Buildings of Interest": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Name": {"type": "string"},
                                    "Type": {"type": "string"},
                                    "Description": {"type": "string"}
                                },
                                "required": ["Name", "Type", "Description"]
                            }
                        }
                    },
                    "required": ["Name", "Population", "Diameter in km", "Position", "Description", "Buildings of Interest"]
                },
                "minItems": 1,
                "maxItems": 10
            }
        },
        "required": ["Name", "Population", "Diameter in km", "Position", "Description", "Subdistricts"]
    },
    "number_of_user_messages": 1
}

house_level_ai_messages = {
    "system_message": """
    You are an AI who"s goal is to create an entirely new and unheard of world. With the goal of adding more detail to the world, you will be adding a new houses/shops to a given subdistrict.
    These houses/shops need to be unique and have a purpose in the subdistrict. There needs to be enough houses/shops to fill the subdistrict completely.
    """,
    "user_message_1": """
    Generate 5 to 30 houses/shops for the subdistrict depending on the size of the subdistrict. A smaller subdistrict will have less houses/shops than a larger subdistrict.
    Theses houses/shops need to be unique and have a purpose in the subdistrict. There needs to be enough houses/shops to fill the subdistrict completely.
    You need to make sure to include all the "Buildings of Interest" in the subdistrict in the houses/shops.

    Update the following JSON object:
    {JSON Object}

    The new JSON object should follow the following format and make sure not to remove any of the existing data:
    {
        "Name": "<Subdistrict Name>",
        "Population": <Population as Number>,
        "Diameter in km": "<Subdistrict Diameter>",
        "Position": ["<Latitude>", "<Longitude>"],
        "Description": "<Subdistrict Description>",
        "Buildings of Interest": [{"Name": "<Building Name>", "Type": "<Building Type>", "Description": "<Building Description>"}],
        "Buildings": [
            {
                "Name": "<Building Name>",
                "Type": "<Building Type (House, Shop, Other)>",
                "Population": <Population as Number, this should be based on the Building Type>,
                "Description": "<Building Description>"
            }
        ]
    }

    Make sure to make the Buildings unique and have a purpose in the subdistrict.
    Make sure the total Occupants of the Buildings does not exceed the Population of the Subdistrict.
    The number of Buildings should be between 5 and 30 depending on the size of the Subdistrict.
    It is absolutely critical that all "Buildings of Interest" are included in the Buildings array.

    Again, make sure not to remove any of the existing data or create any objects not in the format above.
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    "format": {
        "type": "object",
        "properties": {
            "Name": {"const": "{Subdistrict Name}"},
            "Population": {"type": "integer"},
            "Diameter in km": {"type": "number"},
            "Position": {
                "type": "array",
                "items": {"type": "string"}
            },
            "Description": {"type": "string"},
            "Buildings of Interest": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Type": {"type": "string"},
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Type", "Description"]
                }
            },
            "Buildings": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Type": {"type": "string"},
                        "Population": {"type": "integer"},
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Type", "Population", "Description"]
                },
                "maxItems": 5,
                "maxItems": 30
            }
        },
        "required": ["Name", "Population", "Diameter in km", "Position", "Description", "Buildings of Interest", "Buildings"]
    },
    "number_of_user_messages": 1
}

family_level_ai_messages = {
    "system_message": """
    You are an AI who"s goal is to create an entirely new and unheard of world. With the goal of adding more detail to the world, you will be adding a new families to a given house.
    These families need to be unique and have a purpose in the house. There needs to be enough family members to fill the house completely.

    A house should have between 1 and 6 people living in it.
    with 1 to 3 adults and 0 to 3 children.
    """,
    "user_message_1": """
    Generate a family for the house depending on the population of the house.
    There is no gender issues in this world, so the family can be any combination of adults and children.
    The family should be unique and have a purpose in the house.

    Update the following JSON object:
    {JSON Object}

    The new JSON object should follow the following format and make sure not to remove any of the existing data:
    {
        "Name": "<Building Name>",
        "Type": "<Building Type (House, Shop, Other)>",
        "Population": <Population as Number>,
        "Description": "<Building Description>",
        "Families": [
            {
                "Family Name": "<Family Name>",
                "Members": [
                    {
                        "Family Name": "<Family Member Family Name>",
                        "First Name": "<Family Member First Name>",
                        "Age": <Family Member Age as Number>,
                        "Role": "<Family Member Role (Adult, Child)>",
                        "Job": "<Family Member Job>",
                        "Family Relation": {"Name": "<Family Member Name>", "Relation": "<Family Member Relation>"},
                        "Description": "<Family Member Description>"
                    }
                ]
            }
        ]
    }
    There should only be 1 to 2 families in the house depending on the population of the house.
    Ensure that all family members are created within the population of the house.
    Make sure the total number of family members does not exceed the Population of the House.
    The number of family members should be between 1 and 6 depending on the size of the House.
    The Family Name should be unique and the Family Member Family Name should be the same as the Family Name.

    Again, make sure not to remove any of the existing data or create any objects not in the format above.
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    "format": {
        "type": "object",
        "properties": {
            "Name": {"const": "{Building Name}"},
            "Type": {"type": "string"},
            "Population": {"type": "integer"},
            "Description": {"type": "string"},
            "Families": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Family Name": {"type": "string"},
                        "Members": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "Family Name": {"type": "string"},
                                    "First Name": {"type": "string"},
                                    "Age": {"type": "integer", "minimum":0, "maximum": 60},
                                    "Role": {"type": "string"},
                                    "Job": {"type": "string"},
                                    "Family Relation": {
                                        "type": "object",
                                        "properties": {
                                            "Name": {"type": "string"},
                                            "Relation": {"type": "string"}
                                        },
                                        "required": ["Name", "Relation"]
                                    },
                                    "Description": {"type": "string"}
                                },
                                "required": ["First Name", "Family Name", "Age", "Role", "Job", "Family Relation", "Description"]
                            },
                            "minItems": 1,
                            "maxItems": 6
                        }
                    },
                    "required": ["Family Name", "Members"]
                }
            }
        },
        "required": ["Name", "Type", "Population", "Description", "Families"]
    },
    "number_of_user_messages": 1
}

person_level_ai_messages = {
    "system_message": """sleep
    You are an AI who"s goal is to create an entirely new and unheard of world. With the goal of adding more detail to the world, you will be adding a new people to a given family.
    These people need to be unique and have a purpose in the family, and the civilization as a whole. These people need to have traits and enough information to be a complete person.
    """,
    "user_message_1": """
    Generate a person in full detail for the family depending on the population of the family.
    The person should be unique and have a purpose in the family and the civilization.

    Update the following JSON object:
    {JSON Object}

    The new JSON object should follow the following format and make sure not to remove any of the existing data:
    {
        "Family Name": "<Family Member Family Name>",
        "First Name": "<Family Member First Name>",
        "Age": <Family Member Age as Number>,
        "Role": "<Family Member Role (Adult, Child)>",
        "Job": "<Family Member Job>",
        "Family Relation": {"Name": "<Family Member Name>", "Relation": "<Family Member Relation>"},
        "Description": "<Family Member Description>",
        "Traits": [
            {
                "Name": "<Trait Name>",
                "Description": "<Trait Description>"
            }
        ],
        "Skills": [
            {
                "Name": "<Skill Name>",
                "Description": "<Skill Description>"
            }
        ],
        "Hobbies": [
            {
                "Name": "<Hobby Name>",
                "Description": "<Hobby Description>"
            }
        ],
        "Personal Beliefs": [
            {
                "Name": "<Belief Name>",
                "Description": "<Belief Description>"
            }
        ]
    }

    This Person need feel complete and have a purpose in the family and the civilization.
    This Person should have between 1 and 5 traits, 1 and 5 skills, 1 and 5 hobbies, and 1 and 5 personal beliefs, all based on the person's age and role.
    Their job should be based on their age and role.
    Their traits, skills, hobbies, and personal beliefs should be based on their age and job.
    
    Again, make sure not to remove any of the existing data or create any objects not in the format above.
    Respond only with valid JSON. Do not write an introduction or summary.
    """,
    "format": {
        "type": "object",
        "properties": {
            "Family Name": {"const": "{Family Member Family Name}"},
            "First Name": {"const": "{Family Member First Name}"},
            "Age": {"type": "number"},
            "Role": {"type": "string"},
            "Job": {"type": "string"},
            "Family Relation": {
                "type": "object",
                "properties": {
                    "Name": {"type": "string"},
                    "Relation": {"type": "string"}
                },
                "required": ["Name", "Relation"]
            },
            "Description": {"type": "string"},
            "Traits": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Description"]
                }
            },
            "Skills": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Description"]
                }
            },
            "Hobbies": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Description"]
                }
            },
            "Personal Beliefs": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Description": {"type": "string"}
                    },
                    "required": ["Name", "Description"]
                }
            }
        },
        "required": ["Family Name", "First Name", "Age", "Role", "Job", "Family Relation", "Description", "Traits", "Skills", "Hobbies", "Personal Beliefs"]
    },
    "number_of_user_messages": 1
}

