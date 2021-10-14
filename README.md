# academic-NLP-chatbot
Smart discord chatbot integrated with Dialogflow to interact with students naturally and manage different classes in a school.

## Description

As an effort to manage different classrooms, this smart chatbot is created so students can interact with it on Discord naturally and get things done without TAs or instructors' help.  

This chatbot is named Bu, a real name of a dog living in CoderSchool. 

Here are what Bu can do:
- Bu can check your attendance by greeting it.
- Bu can give important links (material links, zoom link, score dashboard,...) 
- Bu can cheers you up when you are sad :((
- Bu can tell you jokes to make you smile :))
- Bu can clear up its own messages. 
- Bu can show who is missing in the class or not yet check their attendance.
- Bu can answer common questions about CoderSchool (opening hours, who is CEO, best instructor, TA,...)
- Bu can do small talks to you :))
- Bu can introduce a bit about myself
- Bu can choose what kind of food you should have for lunch or dinner if you are indecisive. 
- Bu can give points to you (Can only be done by TAs/Instructors). Example: @bu give 2 activities finishing homework @abc @def

## Getting Started

### Dependencies

* Python 3.5.3+
* discord library
* google.cloud.dialogflow library 
* flask library 

### Installing

* Make sure you have discord.py which works with Python 3.5.3 or higher. You can get the library directly from PyPI:
```
python3 -m pip install -U discord.py
```

* Install diaglow library:

```
pip install google-cloud-dialogflow
```

* Install flask library:

```
pip install flask
```

### Executing program

![Workflow](https://imgur.com/jsEyoNN)


## Usage

Here are some read examples of the chatbot in action where students just talk to it naturally like to a real TA: 

* Ask what it can do

![Help](https://imgur.com/EmCNvwzn)

* Ask who it is

![Who are you?](https://imgur.com/ntY9j2k)

* Ask who is the creator of it

![Father](https://imgur.com/XV3HVJg)

* It can automatically check students' attendance by just greeting to it and it will reply in a funny way

![Check attendance 1](https://imgur.com/bJKhUa5)

![Check attendance 2](https://imgur.com/jLifLZx)

![Check attendance 3](https://imgur.com/PYmEhQF)

* It can answer some common questions about the course or the company

![opening hours](https://imgur.com/fvOs2QD)

* It can show relevant links of the course which students ask for

![Dashboard](https://imgur.com/7y1MzlY)

* It can award students who are active in the class

![Give score](https://imgur.com/Atdo1c7)

* It can cheer up students if they are are sad or struggled

![Sad cheer up](https://imgur.com/EyJiLd4)

* It can tell different jokes

![Joke 1](https://imgur.com/5HqVr65)

![Joke 2](https://imgur.com/5M5lTbP)

![Joke 3](https://imgur.com/kFPwHGB)

* It can pick a meal for you if you are indecisive what to have for lunch or dinner (A lot of students request for this feature!)

![Meal choice](https://imgur.com/fbvzmp1)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Some useful documents are:
* [discordpy](https://discordpy.readthedocs.io/en/latest/)
* [realpython](https://realpython.com/how-to-make-a-discord-bot-python/)
* [dialogflow](https://cloud.google.com/dialogflow/es/docs)
