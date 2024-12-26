
from ai.agent import AIAgent
from ai.system_messages import world_level_ai_messages, continent_level_ai_messages, region_level_ai_messages, district_level_ai_messages, subdistrict_level_ai_messages, house_level_ai_messages, family_level_ai_messages, person_level_ai_messages
import json
from pathlib import Path
import traceback

model = 'llama3.1:8b'
# model = 'llama3.3'
def write_json(data, filename):

    with open(filename, "w") as jsonFile:
        jsonFile.write(
            json.dumps(data, indent=4, sort_keys=True)
        )

# chat_history_filename should be a path/filename to the chat history file
# load_chat_history boolean to determine if the chat history should be loaded
def create_world(chat_history_filename="world_level_chat_history.json", load_chat_history=False):
    world_level_ai = AIAgent('http://192.168.1.182:11434', model, world_level_ai_messages['system_message'])
    if load_chat_history:
        world_level_ai.load_chat_history(chat_history_filename)
    else:
        for i in range(world_level_ai_messages['number_of_user_messages']):
            world_level_ai.send_request({'role':'user','content': world_level_ai_messages['user_message_'+str(i+1)]}, world_level_ai_messages['format'])

    world_level_ai_chat_history = world_level_ai.return_chat_history()
    world_level_ai.save_chat_history(chat_history_filename)

    world_data = json.loads(world_level_ai_chat_history.pop()['content'])
    world_path = "./worlds/"+world_data["World Name"]

    Path(world_path).mkdir(parents=True, exist_ok=True)
    write_json(world_data, "world_"+world_data["World Name"]+".json")
    write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")


    world_level_ai.save_chat_history(world_path+'/world_level_chat_history.json')
    return world_data

def create_continents(world_json_file, chat_history_filename="continent_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1
        for continent in world_data["Continents"]:
            print('working on continent ', continent['Name'], ' ', continent_number, ' out of ', len(world_data["Continents"]))
            while True:
                try:
                    continent_level_ai = AIAgent('http://192.168.1.182:11434', model, continent_level_ai_messages['system_message'])
                    if load_chat_history:
                        continent_level_ai.load_chat_history(chat_history_filename)
                    else:
                        for i in range(continent_level_ai_messages['number_of_user_messages']):
                            json_format = continent_level_ai_messages['format'].copy()
                            json_format["properties"]["Name"] = {"const": continent["Name"]}
                            continent_level_ai.send_request({'role':'user','content': continent_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(continent))}, json_format)

                    continent_level_ai_chat_history = continent_level_ai.return_chat_history()
                    continent_level_ai.save_chat_history(chat_history_filename)
                    latest_history = continent_level_ai_chat_history.pop()['content']
                    print("tying to load json")
                    print(latest_history)
                    continent_data = json.loads(latest_history)
                    # We need to append the continent data to the world data in the correct continent
                    for i in range(len(world_data["Continents"])):
                        if world_data["Continents"][i]["Name"] == continent_data["Name"]:
                            world_data["Continents"][i] = continent_data
                            break

                    world_path = "./worlds/"+world_data["World Name"]

                    Path(world_path).mkdir(parents=True, exist_ok=True)
                    write_json(world_data, "world_"+world_data["World Name"]+".json")
                    write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")

                    continent_level_ai.save_chat_history(world_path+'/continent_chat_history_'+continent['Name']+'.json')
                    break
                except Exception:
                    print(traceback.format_exc())
                    print("Error loading continent data")
                    return
            
            continent_number += 1
        return world_data

def create_regions(world_json_file, chat_history_filename="region_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1

        for continent in world_data["Continents"]:
            region_number = 1
            for region in continent["Regions"]:
                while True:
                    try:
                        region_level_ai = AIAgent('http://192.168.1.182:11434', model, region_level_ai_messages['system_message'])
                        if load_chat_history:
                            region_level_ai.load_chat_history(chat_history_filename)
                        else:
                            for i in range(region_level_ai_messages['number_of_user_messages']):
                                formatted_continent = continent.copy()
                                formatted_continent['Regions'] = [region]
                                json_format = region_level_ai_messages['format'].copy()
                                json_format["properties"]["Name"] = {"const": formatted_continent["Name"]}
                                json_format["properties"]["Regions"]["items"]["properties"]["Name"] = {"const": region["Name"]}

                                print("working on region ", region['Name'], ' ', region_number, ' out of ', len(continent["Regions"]), ' in continent ', continent['Name'])
                                region_level_ai.send_request({'role':'user','content': region_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(formatted_continent))}, json_format)

                        region_level_ai_chat_history = region_level_ai.return_chat_history()
                        region_level_ai.save_chat_history(chat_history_filename)
                        latest_history = region_level_ai_chat_history.pop()['content']
                        region_data = json.loads(latest_history)
                        # We need to append the region data to the world data in the correct region
                        print("working on region ", region['Name'], ' ', region_number, ' out of ', len(continent["Regions"]), ' in continent ', continent['Name'], "Found: ", world_data["Continents"][i]["Name"] == continent["Name"] )
                        found_match = False
                        for j in range(len(continent['Regions'])):
                            if not ("Regions" in region_data and len(region_data["Regions"]) > 0 and "Name" in region_data["Regions"][0]):
                                print("Region data is missing required fields, retrying")
                                break
                            print("Looking for region ", region_data["Regions"][0]['Name'], " in continent ", continent["Name"], "Found: ", continent['Regions'][j]['Name'] == region_data["Regions"][0]['Name'])
                            if continent['Regions'][j]['Name'] == region_data["Regions"][0]['Name']:
                                continent['Regions'][j] = region_data["Regions"][0]
                                found_match = True
                                break
                        if not found_match:
                            print("Could not find region", region["Name"], "in continent", continent["Name"], "Retrying")
                            continue

                        world_path = "./worlds/"+world_data["World Name"]
                        Path(world_path).mkdir(parents=True, exist_ok=True)
                        write_json(world_data, "world_"+world_data["World Name"]+".json")
                        write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")

                        region_level_ai.save_chat_history(world_path+'/region_chat_history_'+region['Name']+'.json')
                        break
                    except Exception:
                        print(traceback.format_exc())
                        print("Error loading region data")
                        return
                region_number += 1
            continent_number += 1
        return world_data


def create_districts(world_json_file, chat_history_filename="district_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1
        for continent in world_data["Continents"]:
            region_number = 1
            for region in continent["Regions"]:
                civilization_number = 1
                for civilization in region["Civilizations"]:
                    while True:
                        try:
                            district_level_ai = AIAgent('http://192.168.1.182:11434', model, district_level_ai_messages['system_message'])
                            if load_chat_history:
                                district_level_ai.load_chat_history(chat_history_filename)
                            else:
                                for i in range(district_level_ai_messages['number_of_user_messages']):
                                    print("working on civilization ", civilization['Name'], ' ', civilization_number, ' out of ', len(region["Civilizations"]), ' in region ', region['Name'])
                                    json_format = district_level_ai_messages['format'].copy()
                                    json_format["properties"]["Name"] = {"const": civilization["Name"]}
                                    district_level_ai.send_request({'role':'user','content': district_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}', json.dumps(civilization))}, json_format)
                            district_level_ai_chat_history = district_level_ai.return_chat_history()
                            district_level_ai.save_chat_history(chat_history_filename)
                            latest_history = district_level_ai_chat_history.pop()['content']
                            district_data = json.loads(latest_history)
                            found_match = False
                            for j in range(len(region["Civilizations"])):
                                if region["Civilizations"][j]["Name"] == district_data["Name"]:
                                    region["Civilizations"][j] = district_data
                                    found_match = True
                                    break

                            if not found_match:
                                print("Could not find civilization", civilization["Name"], "in region", region["Name"], "Retrying")
                                continue
                            world_path = "./worlds/"+world_data["World Name"]

                            Path(world_path).mkdir(parents=True, exist_ok=True)
                            write_json(world_data, "world_"+world_data["World Name"]+".json")
                            write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")
                            district_level_ai.save_chat_history(world_path+'/district_chat_history_'+civilization['Name']+'.json')
                            break

                        except Exception:
                            print(traceback.format_exc())
                            print("Error loading district data")
                            return
                    civilization_number += 1
                region_number += 1
            continent_number += 1
        return world_data

def create_subdistricts(world_json_file, chat_history_filename="subdistrict_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1
        for continent in world_data["Continents"]:
            region_number = 1
            for region in continent["Regions"]:
                civilization_number = 1
                for civilization in region["Civilizations"]:
                    district_number = 1
                    for district in civilization["Districts"]:
                        while True:
                            try:
                                subdistrict_level_ai = AIAgent('http://192.168.1.182:11434', model, subdistrict_level_ai_messages['system_message'])
                                if load_chat_history:
                                    subdistrict_level_ai.load_chat_history(chat_history_filename)
                                else:
                                    for i in range(subdistrict_level_ai_messages['number_of_user_messages']):
                                        json_format = subdistrict_level_ai_messages['format'].copy()
                                        json_format["properties"]["Name"] = {"const": district["Name"]}
                                        print("working on district ", district['Name'], ' ', district_number, ' out of ', len(civilization["Districts"]), ' in civilization ', civilization['Name'])
                                        subdistrict_level_ai.send_request({'role':'user','content': subdistrict_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(district))}, json_format)
                                
                                subdistrict_level_ai_chat_history = subdistrict_level_ai.return_chat_history()
                                subdistrict_level_ai.save_chat_history(chat_history_filename)
                                latest_history = subdistrict_level_ai_chat_history.pop()['content']
                                subdistrict_data = json.loads(latest_history)
                                
                                found_match = False
                                for j in range(len(civilization["Districts"])):
                                    if civilization["Districts"][j]["Name"] == subdistrict_data["Name"]:
                                        civilization["Districts"][j] = subdistrict_data
                                        found_match = True
                                        break
                                if not found_match:
                                    print("Could not find district", district["Name"], "in civilization", civilization["Name"], "Retrying")
                                    continue
                                world_path = "./worlds/"+world_data["World Name"]

                                Path(world_path).mkdir(parents=True, exist_ok=True)
                                write_json(world_data, "world_"+world_data["World Name"]+".json")
                                write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")
                                subdistrict_level_ai.save_chat_history(world_path+'/subdistrict_chat_history_'+district['Name']+'.json')
                                break
                            except Exception:
                                print(traceback.format_exc())
                                print("Error loading subdistrict data")
                                return
                        district_number += 1
                    civilization_number += 1
                region_number += 1
            continent_number += 1
        return world_data
    
def create_households(world_json_file, chat_history_filename="household_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1
        for continent in world_data["Continents"]:
            region_number = 1
            for region in continent["Regions"]:
                civilization_number = 1
                for civilization in region["Civilizations"]:
                    district_number = 1
                    for district in civilization["Districts"]:
                        subdistrict_number = 1
                        for subdistrict in district["Subdistricts"]:
                            while True:
                                try:
                                    household_level_ai = AIAgent('http://192.168.1.182:11434', model, house_level_ai_messages['system_message'])
                                    if load_chat_history:
                                        household_level_ai.load_chat_history(chat_history_filename)
                                    else:
                                        for i in range(house_level_ai_messages['number_of_user_messages']):
                                            print("working on subdistrict ", subdistrict['Name'], ' ', subdistrict_number, ' out of ', len(district["Subdistricts"]), ' in district ', district['Name'])
                                            json_format = house_level_ai_messages['format'].copy()
                                            json_format["properties"]["Name"] = {"const": subdistrict["Name"]}
                                            household_level_ai.send_request({'role':'user','content': house_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(subdistrict))}, json_format)

                                    household_level_ai_chat_history = household_level_ai.return_chat_history()
                                    household_level_ai.save_chat_history(chat_history_filename)
                                    latest_history = household_level_ai_chat_history.pop()['content']
                                    household_data = json.loads(latest_history)
                                    found_match = False
                                    for j in range(len(district["Subdistricts"])):
                                        if district["Subdistricts"][j]["Name"] == household_data["Name"]:
                                            district["Subdistricts"][j] = household_data
                                            found_match = True
                                            break
                                    if not found_match:
                                        print("Could not find subdistrict", subdistrict["Name"], "in district", district["Name"], "Retrying")
                                        continue
                                    world_path = "./worlds/"+world_data["World Name"]

                                    Path(world_path).mkdir(parents=True, exist_ok=True)
                                    write_json(world_data, "world_"+world_data["World Name"]+".json")
                                    write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")
                                    household_level_ai.save_chat_history(world_path+'/household_chat_history_'+subdistrict['Name']+'.json')
                                    break
                                except Exception:
                                    print(traceback.format_exc())
                                    print("Error loading household data")
                                    return
                            subdistrict_number += 1
                        district_number += 1
                    civilization_number += 1
                region_number += 1
            continent_number += 1
        return world_data
        
def create_families(world_json_file, chat_history_filename="family_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1
        for continent in world_data["Continents"]:
            region_number = 1
            for region in continent["Regions"]:
                civilization_number = 1
                for civilization in region["Civilizations"]:
                    district_number = 1
                    for district in civilization["Districts"]:
                        subdistrict_number = 1
                        for subdistrict in district["Subdistricts"]:
                            household_number = 1
                            for household in subdistrict["Buildings"]:
                                while True:
                                    try:
                                        family_level_ai = AIAgent('http://192.168.1.182:11434', model, family_level_ai_messages['system_message'])
                                        if load_chat_history:
                                            family_level_ai.load_chat_history(chat_history_filename)
                                        else:
                                            for i in range(family_level_ai_messages['number_of_user_messages']):
                                                print("working on household ", household['Name'], ' ', household_number, ' out of ', len(subdistrict["Buildings"]), ' in subdistrict ', subdistrict['Name'])
                                                json_format = family_level_ai_messages['format'].copy()
                                                json_format["properties"]["Name"] = {"const": household["Name"]}
                                                family_level_ai.send_request({'role':'user','content': family_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(household))}, json_format)

                                        family_level_ai_chat_history = family_level_ai.return_chat_history()
                                        family_level_ai.save_chat_history(chat_history_filename)
                                        latest_history = family_level_ai_chat_history.pop()['content']
                                        family_data = json.loads(latest_history)
                                        found_match = False
                                        for j in range(len(subdistrict["Buildings"])):
                                            if subdistrict["Buildings"][j]["Name"] == family_data["Name"]:
                                                subdistrict["Buildings"][j] = family_data
                                                found_match = True
                                                break
                                        if not found_match:
                                            print("Could not find household", household["Name"], "in subdistrict", subdistrict["Name"], "Retrying")
                                            continue
                                        world_path = "./worlds/"+world_data["World Name"]

                                        Path(world_path).mkdir(parents=True, exist_ok=True)
                                        write_json(world_data, "world_"+world_data["World Name"]+".json")
                                        write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")
                                        family_level_ai.save_chat_history(world_path+'/family_chat_history_'+household['Name']+'.json')
                                        break
                                    except Exception:
                                        print(traceback.format_exc())
                                        print("Error loading family data")
                                        return
                                household_number += 1
                            subdistrict_number += 1
                        district_number += 1
                    civilization_number += 1
                region_number += 1
            continent_number += 1
        return world_data
    
def create_persons(world_json_file, chat_history_filename="person_chat_history.json", load_chat_history=False):
    with open(world_json_file) as f:
        world_data = json.load(f)
        continent_number = 1
        for continent in world_data["Continents"]:
            region_number = 1
            for region in continent["Regions"]:
                civilization_number = 1
                for civilization in region["Civilizations"]:
                    district_number = 1
                    for district in civilization["Districts"]:
                        subdistrict_number = 1
                        for subdistrict in district["Subdistricts"]:
                            household_number = 1
                            for household in subdistrict["Buildings"]:
                                family_number = 1
                                for family in household["Families"]:
                                    for person in family["Members"]:
                                        while True:
                                            try:
                                                person_level_ai = AIAgent('http://192.168.1.182:11434', model, person_level_ai_messages['system_message'])
                                                if load_chat_history:
                                                    person_level_ai.load_chat_history(chat_history_filename)
                                                else:
                                                    for i in range(person_level_ai_messages['number_of_user_messages']):
                                                        print("working on person ", person['First Name'], ' ', family_number, ' out of ', len(household["Families"]), ' in household ', household['Name'])
                                                        json_format = person_level_ai_messages['format'].copy()
                                                        json_format["properties"]["Family Name"] = {"const": person["Family Name"]}
                                                        json_format["properties"]["First Name"] = {"const": person["First Name"]}
                                                        person_level_ai.send_request({'role':'user','content': person_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(family))}, person_level_ai_messages['format'])

                                                person_level_ai_chat_history = person_level_ai.return_chat_history()
                                                person_level_ai.save_chat_history(chat_history_filename)
                                                latest_history = person_level_ai_chat_history.pop()['content']
                                                person_data = json.loads(latest_history)
                                                found_match = False
                                                for j in range(len(household["Families"])):
                                                    for k in range(len(household["Families"][j]["Members"])):
                                                        if household["Families"][j]["Members"][k]["First Name"] == person_data["First Name"]:
                                                            household["Families"][j]["Members"][k] = person_data
                                                            found_match = True
                                                            break
                                                    
                                                if not found_match:
                                                    print("Could not find family", family["Family Name"], "in household", household["Name"], "Retrying")
                                                    continue
                                                world_path = "./worlds/"+world_data["World Name"]

                                                Path(world_path).mkdir(parents=True, exist_ok=True)
                                                write_json(world_data, "world_"+world_data["World Name"]+".json")
                                                write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")
                                                person_level_ai.save_chat_history(world_path+'/person_chat_history_'+person['First Name']+person['Family Name']+'.json')
                                                break
                                            except Exception:
                                                print(traceback.format_exc())
                                                print("Error loading person data")
                                                return
                                        
                                    family_number += 1
                                household_number += 1
                            subdistrict_number += 1
                        district_number += 1
                    civilization_number += 1
                region_number += 1
            continent_number += 1
        return world_data
    
def create_whole_world():
    world_data = create_world()
    
    world_data_json_path = "./worlds/"+world_data["World Name"]+"/world_"+world_data["World Name"]+".json"

    world_data = create_continents(world_data_json_path)
    world_data = create_regions(world_data_json_path)
    world_data = create_districts(world_data_json_path)
    world_data = create_subdistricts(world_data_json_path)
    world_data = create_households(world_data_json_path)
    world_data = create_families(world_data_json_path)
    world_data = create_persons(world_data_json_path)

if __name__ == "__main__":
    create_whole_world()