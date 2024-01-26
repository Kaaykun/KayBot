# <div align="center">🤖 KayBot 🤖</div>

### <div align='center'> Multipurpose ChatBot created using Python, capable of helping with daily tasks </div>

#### KayBot is an ongoing project aimed at developing a chatbot using TensorFlow Keras. The goal is to create a versatile and intelligent conversational agent that can be used for various applications:  
- **Chat with the user.**   
Example promts: *'Who made you?', 'Tell me a joke', 'Ask me a riddle'*  
- **List all available commands.**    
Example prompts: *'What can you do?' or 'help'*  
- **Perform google searches and open new tabs with the results.**    
Example prompts: *'google: GitHub'*
- **Tell the current date and time.**    
Example prompts: *'Whats the time?', 'date', 'What day is today'*
- **Inform about the weather in any city.**    
Example prompts: *'weather: Tokyo', 'weather: Chicago'*
- **Link to articles of the latest news.**    
Example prompts: *'latest news', 'news'*
- **List the top 10 trending songs on the global charts.**    
Example prompts: *'top songs', 'hot songs', 'songs'*
- *[Currently bugged and under investigation]* **Keep track of a set timer (in minutes) and ring and alarm when the time is up.**   
Example prompts: *'timer: 1', 'timer: 10'*


## Table of Contents
- [Work in Progress](#work-in-progress)
- [Images](#images)
- [Folder Structure](#folder-structure)
- [Features](#features)
- [Dependencies](#dependencies)
- [Getting Started](#getting-started)
- [License](#license)

## Work in Progress
KayBot is currently in the development, and the following aspects are being actively worked on:
- [x] Data Collection and Preprocessing
- [x] Model Architecture Design
- [x] Training Pipeline Implementation
- [x] Evaluation Metrics and Testing
- [x] Integration with External APIs
- [ ] User Interface and Deployment
- [ ] Finalizing Github repository

## Images
![KayBot Main](data/images/KayBot%20Main.png)
![KayBot Chat](data/images/KayBot%20Chat.png)

## Folder Structure
- [Folder: backend](./backend/)  
Contains all the source code in form of python scripts.  
- [Folder: data](./data/)  
The chatbots intents and pickle files are stored here.  
- [Folder: frontend](./frontend/)  
Houses the HTML templates, as well as the forms and routes in python files.  
- [Folder: models](./models/)  
The current and future pre-trained models of the chatbot.  
- [Folder: notebooks](./notebooks/)  
Step-by-step documentation of the first modelling attempts.
- [Files](./)  
*.gitignore, .gitattributes, .python-version* are contain the usual parameters.  
*kaybot.py and kaybotconfig.py* are what run and execute the Flask app locally.  
*Procfile* is currently still in progress and will be used for deployment.  

## Features
- [x] Natural Language Processing
- [x] Intent Recognition
- [x] Context-aware Responses
- [ ] Customizable Responses
- [ ] User Interaction Logging

## Dependencies
tbd

## Getting Started
To get started with KayBot, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Kaaykun/KayBot.git
   cd KayBot
   ```
   TBD

## License
*Copyright 2024 Jaris Fenner*

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
