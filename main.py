from chatbot import ChatBot

bot = ChatBot("Ezy")
while True:
    user_response = bot.walkUser()
    bot_response = bot.processUserResponse(user_response)
    bot.botSpeack(bot_response)
    if bot_response == "tchau":
        break
