import requests

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
base_url = os.getenv("BASE_URL")


class TypebotAPI:
    def __init__(self, typebot_id, token):
        self.usuarios = {}
        self.typebot_id = typebot_id
        self.token = token
        self.base_url = base_url
        self.session_id = None
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        self.data = None
        self.messages = None
        self.input = None

    def start_chat(self, nome):
        url = f"{self.base_url}/typebots/{self.typebot_id}/preview/startChat"
        response = requests.post(url, headers=self.headers)
        if response.status_code == 200:
            self.session_id = response.json().get("sessionId")

            self.usuarios[nome] = response.json().get("sessionId")

            self.data = response.json()
            self.messages = self.data["messages"]

        else:
            print("Failed to start chat:", response.text)
        data = response.json()
        messages = data.get("messages", [])
        texts = self.extract_texts(messages)
        # variavel que indica configurações internas
        clientSideActions = response.json().get("clientSideActions", [])
        # verifica se no corpo se não existe mensagem
        # verifica se no corpo se existe o nó clientSideActions
        if clientSideActions and len(messages) == 0:
            return self.skipt(nome)

        return texts

    # função responsavel por pular uma etapa
    def skipt(self, nome):
        return self.send_message(" .", nome)

    def send_message(self, message, nome):
        session_id = self.usuarios[nome]
        if not session_id:
            return

        url = f"{self.base_url}/sessions/{session_id}/continueChat"
        data = {"message": message}
        response = requests.post(url, json=data, headers=self.headers)

        data = response.json()
        messages = data.get("messages", [])
        texts = self.extract_texts(messages)
        # variavel que indica configurações internas
        clientSideActions = response.json().get("clientSideActions", [])
        # verifica se no corpo se não existe mensagem
        # verifica se no corpo se existe o nó clientSideActions
        if clientSideActions and len(messages) == 0:
            return self.skipt(nome)

        return texts
        return texts

    def extract_texts(self, messages):
        try:
            texts = []
            for message in messages:
                if message["type"] == "text" and "content" in message:
                    rich_text = message["content"].get("richText", [])
                    message_texts = self.collect_texts(rich_text)
                    if message_texts:
                        texts.append(message_texts)
            if texts[0] == "Invalid message. Please, try again.":

                return []

            return texts
        except:
            texts = []

            return texts

    def collect_texts(self, data):
        texts = []

        if isinstance(data, dict):
            for key, value in data.items():
                if key == "text":
                    texts.append(value)
                elif isinstance(value, (dict, list)):
                    texts.extend(self.collect_texts(value))
        elif isinstance(data, list):
            for item in data:
                texts.extend(self.collect_texts(item))

        return texts
