import os
from dotenv import load_dotenv
from services import automation, TypebotAPI
import time

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Acessar as variáveis de ambiente
typebot_id = os.getenv("TYPEBOT_ID")
token = os.getenv("TOKEN")

# with interface = true
# without interface = false // terminal acess
bot = automation(gui=False)
# inicio instancia connector
bot.start()
print("==================================")
print("      iniciado com sucesso")
print("==================================")
# credenciais
typebot = TypebotAPI(typebot_id, token)
while True:
    new_message = bot.VerificarNovaMensagem()
    # =================================================================
    #                          continue chat
    # =================================================================
    if new_message:
        nome = new_message
        # Validação de users
        users = typebot.usuarios
        id = users.get(nome)
        if id:
            last_message = bot.pegar_ultima_mensagem()

            messages = typebot.send_message(last_message, nome)

            data = typebot.data
            isAction = data.get("clientSideActions", [])
            if last_message == "##exit":
                bot.sendMensage("Chat encerrado")
                typebot.usuarios[nome] = None
            else:
                if isAction and len(messages) == 0:
                    messages = typebot.send_message(" .", nome)

                if (
                    len(messages) > 0
                    and messages[0] == "Invalid message. Please, try again."
                ):
                    bot.sendMensage(
                        "Naõ entendi muito bem, voce poderia digitar uma opção valida ?"
                    )
                else:
                    for i in messages:
                        text = ""
                        for message in i:
                            if message != "##exit":
                                text += message + "\n"

                            else:
                                typebot.usuarios[nome] = None
                        bot.sendMensage(text)
        # =================================================================
        #                          start chat
        # =================================================================
        else:
            messages = typebot.start_chat(nome)
            data = typebot.data

            if (
                len(messages) > 0
                and messages[0] == "Invalid message. Please, try again."
            ):
                bot.sendMensage(
                    "Não entendi muito bem, voce poderia digitar uma opção valida ?"
                )
            else:
                for i in messages:
                    text = ""
                    for message in i:
                        text += message + "\n"
                    bot.sendMensage(text)

        bot.go_to_home()
