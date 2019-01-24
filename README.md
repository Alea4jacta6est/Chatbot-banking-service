# RASA banking chatbot

 <img src="https://journalbitcoin.com/wp-content/uploads/2019/01/Chatbot-for-Banking-Market.png" width="500" height="300">

## Features
- Intent analysis and the ability to save all the entities (and recognize them) during the session
- Communication on banking topics such as mortgages, deposit accounts and credit cards
- Custom actions that can form queries from user messages and return the documents by index and query

## 1. Download the repository and install everything from requirements.txt
## 2. Use the next command to launch the bot in your console:
make launch 
*(don't forget to do it from the folder RASA_banking_chatbot)
## 3. If you want to try interactive learning:
make interactive
## 4. To get graph visualization you should do the following:
make visualize
## 5. Activation of actions can be done with:
make activate_actions
*point your host in the code actions.py to get access to your ElasticSearch server

You are welcome to broaden the bot by adding actions and intents and forming scenarios of communication in stories.md file.

