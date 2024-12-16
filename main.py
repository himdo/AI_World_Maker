
from ai.agent import AIAgent
from ai.system_messages import world_level_ai_messages, continent_level_ai_messages
import json
from pathlib import Path

def write_json(data, filename):

    with open(filename, "w") as jsonFile:
        jsonFile.write(
            json.dumps(data, indent=4, sort_keys=True)
        )

# chat_history_filename should be a path/filename to the chat history file
# load_chat_history boolean to determine if the chat history should be loaded
def create_world(chat_history_filename="world_level_chat_history.json", load_chat_history=False):
    world_level_ai = AIAgent('http://192.168.1.182:11434', 'llama3.3', world_level_ai_messages['system_message'])
    if load_chat_history:
        world_level_ai.load_chat_history(chat_history_filename)
    else:
        for i in range(world_level_ai_messages['number_of_user_messages']):
            print('working on request ', i+1, ' out of ', world_level_ai_messages['number_of_user_messages'])
            world_level_ai.send_request({'role':'user','content': world_level_ai_messages['user_message_'+str(i+1)]})

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
            continent_level_ai = AIAgent('http://192.168.1.182:11434', 'llama3.3', continent_level_ai_messages['system_message'])
            if load_chat_history:
                continent_level_ai.load_chat_history(chat_history_filename)
            else:
                for i in range(continent_level_ai_messages['number_of_user_messages']):
                    print('working on request ', i+1, ' out of ', continent_level_ai_messages['number_of_user_messages'])
                    continent_level_ai.send_request({'role':'user','content': continent_level_ai_messages['user_message_'+str(i+1)].replace('{JSON Object}',json.dumps(continent))})

            continent_level_ai_chat_history = continent_level_ai.return_chat_history()
            continent_level_ai.save_chat_history(chat_history_filename)

            continent_data = json.loads(continent_level_ai_chat_history.pop()['content'])
            # We need to append the continent data to the world data in the correct continent
            for i in range(len(world_data["Continents"])):
                if world_data["Continents"][i]["Name"] == continent_data["Name"]:
                    world_data["Continents"][i] = continent_data
                    break
            # then we save the data back to the world json file


            world_path = "./worlds/"+world_data["World Name"]

            Path(world_path).mkdir(parents=True, exist_ok=True)
            write_json(world_data, "world_"+world_data["World Name"]+".json")
            write_json(world_data, world_path+"/world_"+world_data["World Name"]+".json")

            continent_level_ai.save_chat_history(world_path+'/continent_chat_history_'+continent['Name']+'.json')
            continent_number += 1


world_data = create_world()
continent_data = create_continents("./worlds/"+world_data["World Name"]+"/world_"+world_data["World Name"]+".json")