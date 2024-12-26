import requests
import json
import time
import traceback

class AIAgent:
    # Example usage:
    # agent = AIAgent('http://192.168.1.182:11434', 'llama3.1:8b')
    # response = agent.send_request({'role':'user','content':'Hello, AI!'})
    # print(response)
    def __init__(self, api_base_url, model_name, system_message):
        self.api_base_url = api_base_url
        self.model_name = model_name
        self.chat_history = []
        self.chat_history.append({'role': 'system', 'content': system_message})

    def send_request(self, message, format=None, options=None):
        while True:
            try:
                headers = {
                    'Content-Type': 'application/json'
                }
                self.chat_history.append(message)
                data = {
                    'model': self.model_name,
                    'messages': self.chat_history,
                    'stream': False
                }
                if format:
                    data['format'] = format

                if options:
                    data['options'] = options
                # print("Sending request to AI model", data)
                time.sleep(2)
                response = requests.post(self.api_base_url+'/api/chat', headers=headers, json=data, timeout=60*2) # 10 minutes timeout
                # response = requests.post(self.api_base_url+'/api/chat', headers=headers, json=data, timeout=60*10) # 10 minutes timeout
                if response.status_code == 200:
                    result = response.json()['message']
                    self.chat_history.append(result)
                    return result['content']
                else:
                    print(response.text)
                    response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print("Request failed, retrying in 5 seconds")
                print("Failed Request Body:", e.request.body)
                print(traceback.format_exc())
                time.sleep(5)
                # return 'Error: ' + str(e)

    def save_chat_history(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.chat_history, file)

    def load_chat_history(self, file_path):
        with open(file_path, 'r') as file:
            self.chat_history = json.load(file)
    
    def return_chat_history(self):
        return self.chat_history