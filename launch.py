from rasa_core.agent import Agent


def start_conversation():
    model_directory = 'models/nlu/legal_project/legal_model'
    agent = Agent.load('models/dialogue', interpreter=model_directory)
    print("Your bot is ready to talk! Type your messages here or send 'stop'")
    while True:
        a = input()
        if a == 'stop':
            break
        responses = agent.handle_text(a)
        for response in responses:
            print(response["text"])


start_conversation()
