# RASA banking chatbot

 <img src="http://www.netalogue.com/wp-content/uploads/2017/03/chatbot.png" width="500" height="300">

## Features
- Intent analysis and the ability to save all the entities (and recognize them) during the session
- Communication on banking topics such as mortgages, deposit accounts and credit cards
- Custom actions that can form queries from user messages and return the documents by index and query using ElasticSearch

## 1. Download the repository and install everything from requirements.txt (pip install -r requirements.txt)
*For RASA NLU:

      git clone https://github.com/RasaHQ/rasa_nlu.git
      cd rasa_nlu
      pip install -r requirements.txt
      pip install -e .
      
Spacy:

      pip install rasa_nlu[spacy]
      python -m spacy download en_core_web_md
      python -m spacy link en_core_web_md en
      
RASA Core:

      pip install rasa_core
    
## 2. Use the next command to launch the bot in your console:
make launch 
*(don't forget to do it from the folder RASA_banking_chatbot)
## 3. Interactive learning
make interactive
## 4. Graph visualization
make visualize
## 5. Activation of actions
make activate_actions
*point your host in the code actions.py to get access to your ElasticSearch server

You are welcome to broaden the bot by adding actions and intents and forming scenarios of communication in stories.md file.

