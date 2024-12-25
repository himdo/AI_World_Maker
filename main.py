
from ai.agent import AIAgent
from ai.system_messages import world_level_ai_messages, continent_level_ai_messages, region_level_ai_messages
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
                            continent_level_ai.send_request({'role':'user','content': continent_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(continent))}, continent_level_ai_messages['format'])

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
                                print("working on region ", region['Name'], ' ', region_number, ' out of ', len(continent["Regions"]), ' in continent ', continent['Name'])
                                region_level_ai.send_request({'role':'user','content': region_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(formatted_continent))}, region_level_ai_messages['format'])

                        region_level_ai_chat_history = region_level_ai.return_chat_history()
                        region_level_ai.save_chat_history(chat_history_filename)
                        latest_history = region_level_ai_chat_history.pop()['content']
                        region_data = json.loads(latest_history)
                        # We need to append the region data to the world data in the correct region
                        for i in range(len(world_data["Continents"])):
                            found_continent = False
                            print("working on region ", region['Name'], ' ', region_number, ' out of ', len(continent["Regions"]), ' in continent ', continent['Name'], "Found: ", world_data["Continents"][i]["Name"] == continent["Name"] )
                            if world_data["Continents"][i]["Name"] == continent["Name"]:
                                for j in range(len(world_data["Continents"][i]['Regions'])):
                                    if not ("Regions" in region_data and len(region_data["Regions"]) > 0 and "Name" in region_data["Regions"][0]):
                                        print("Region data is missing required fields, retrying")
                                        break
                                    print("Looking for region ", region_data["Regions"][0]['Name'], " in continent ", world_data["Continents"][i]["Name"], "Found: ", world_data["Continents"][i]['Regions'][j]['Name'] == region_data["Regions"][0]['Name'])
                                    if world_data["Continents"][i]['Regions'][j]['Name'] == region_data["Regions"][0]['Name']:
                                        world_data["Continents"][i]['Regions'][j] = region_data["Regions"][0]
                                        found_continent = True
                                        break
                                if found_continent:
                                    break
                        if not found_continent:
                            print("Could not find continent", continent["Name"], "in world data, Retrying")
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


def create_whole_world():
    world_data = create_world()
    
    world_data_json_path = "./worlds/"+world_data["World Name"]+"/world_"+world_data["World Name"]+".json"

    world_data = create_continents(world_data_json_path)
    world_data = create_regions(world_data_json_path)

if __name__ == "__main__":
    create_whole_world()