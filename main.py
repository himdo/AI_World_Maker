
from ai.agent import AIAgent
from ai.system_messages import world_level_ai_messages
import json


world_level_ai = AIAgent('http://192.168.1.182:11434', 'llama3.3', world_level_ai_messages['system_message'])
# world_level_ai.load_chat_history('world_level_chat_history_3.json')
for i in range(world_level_ai_messages['number_of_user_messages']):
    print('working on request ', i+1, ' out of ', world_level_ai_messages['number_of_user_messages'])
    world_level_ai.send_request({'role':'user','content':world_level_ai_messages['user_message_'+str(i+1)]})

world_level_ai_chat_history = world_level_ai.return_chat_history()
world_level_ai.save_chat_history('world_level_chat_history_3.json')

world_data = json.loads(world_level_ai_chat_history.pop()['content'])
with open("world_"+world_data["World Name"]+".json", "w") as worldDataFile:
    worldDataFile.write(
        json.dumps(world_data, indent=4, sort_keys=True)
    )
