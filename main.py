
from ai.agent import AIAgent
from ai.system_messages import world_level_ai_messages, world_level_summarizer_ai_messages
import json


world_level_ai = AIAgent('http://192.168.1.182:11434', 'llama3.1:8b', world_level_ai_messages['system_message'])
world_level_ai.load_chat_history('world_level_chat_history.json')
# for i in range(world_level_ai_messages['number_of_user_messages']):
#     print('working on request ', i+1, ' out of ', world_level_ai_messages['number_of_user_messages'])
#     world_level_ai.send_request({'role':'user','content':world_level_ai_messages['user_message_'+str(i+1)]})

world_level_ai_chat_history = world_level_ai.return_chat_history()
# world_level_ai.save_chat_history('world_level_chat_history.json')
sanitized_chat_history = []

for message in world_level_ai_chat_history:
    if message['role'] == 'assistant':
        sanitized_chat_history.append(message['content'])

world_level_ai_summarizer_ai = AIAgent('http://192.168.1.182:11434', 'llama3.3', world_level_summarizer_ai_messages['system_message'])
sanitized_chat_history.append("""Now take all that info and make a JSON summary of the world that has the following JSON format:
{
    'World Name': 'World Name',
    'World Diameter': 'World Diameter',
    'Continents': [
        {
            'Name': 'Continent Name',
            'Diameter': 'General Continent Diameter',
            'Location': 'Location of Continent',
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
            'Diameter': 'General Ocean Diameter',
            'Location': 'Location of Ocean',
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
            'Location': 'Location of Island',
            'Features': [
                'Feature 1',
                'Feature 2',
                'Feature 3'
            ]
        }
    ]
}
If there is no feature for a continent, ocean, or island, do not include the 'Features' key. Make sure not to include any features of the world in this request as that will be build on in a later request.
Respond only with valid JSON. Do not write an introduction or summary.""")
world_level_ai_summarizer_ai.send_request({'role':'user','content': json.dumps(sanitized_chat_history)})
world_level_ai_summarizer_ai.save_chat_history('world_level_chat_history_summarizer.json')