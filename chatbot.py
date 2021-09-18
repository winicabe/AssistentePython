import json
class ChatBot():
    def __init__(self, name):
        try:
            bot_memory = open(name+".json","r")
        except FileNotFoundError:
            bot_memory = open(name+".json","w")
            bot_memory.write('["Winicios","Winicabe"]')
            bot_memory.close()
            bot_memory = open(name+".json","r")
        self.name = name
        self.users = json.load(bot_memory)
        self.dialogs = []
    
    def botSpeack(self, bot_reponse):
        print(bot_reponse)
        self.dialogs.append(bot_reponse)

    def processUserResponse(self, user_response):
        if user_response == "oi":
            return "Olá qual seu nome?"
        if self.dialogs[-1] == "Olá qual seu nome?":
            user_name = self.getUserName(user_response)
            bot_response = self.responseNameUser(user_name)
            return bot_response
    
    def getUserName(self, user_response):
        if "o meu nome he " in user_response:
            user_response = user_response[14:]
        elif "eh " in user_response:
            user_response = user_response[3:]
        user_name = user_response.title()
        return user_name

    def responseNameUser(self, user_name):
        bot_response = "eaw "+user_name+" muito prazer!"
        return bot_response

    def walkUser(self):
        user_input = str(input(">:"))
        user_input = user_input.lower()
        user_input = user_input.replace("é","eh")
        return user_input
