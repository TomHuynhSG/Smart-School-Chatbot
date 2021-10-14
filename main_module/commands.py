import discord
import random
from datetime import datetime 
from dotenv import load_dotenv
import gsheet
import numpy as np

import os

load_dotenv()
BOT_NAME = os.getenv('BOT_NAME')

# Command: Send important links
def links(message, channel):

    try:
        embed = discord.Embed(title = "Here are some useful links!", color=0xd74742)
    
        data = gsheet.get_metadata()

        links = data[data['Channel'] == channel].iloc[:, 3:].replace('',np.nan).dropna(axis = 1).T.iloc[:,0].to_dict()

        embed.set_image(url = 'https://i.imgur.com/ZmMo5ay.png')

        for name, value in links.items():
            embed.add_field(name = name, value = value, inline = False)
    except Exception as err:
        print(err)
    return {'embed': embed}


# Command: Check-in
def hello(message, channel):

    # Check if it is weekend
    if datetime.now().weekday() in [5,6]:
        return 'There is no class today!'

    today = datetime.strftime(datetime.now().date(), '%Y-%m-%d')

    class_status="Full_time"

    try:
        data = gsheet.get_metadata()

        class_status = data[data['Channel'] == channel]['Class Status'].values[0]

        spreadsheet_scoring_id = data[data['Channel'] == channel].iloc[:, 2].to_numpy()[0]
        # print(spreadsheet_scoring_id)
        # Get list of users and their Disord account
        users = gsheet.get_users(spreadsheet_scoring_id)

        # print("USERRRR:", users)

        if users == {}:
            return {'content': f'Cohort is inactive!'}

        user = users[message.author.name]
        # print("Current User Discord:", message.author.name)
        # print("Their Real Name:", user)
        
    except Exception as err:
        print(err)
        return f'Oh no, Student {message.author.name} not found! (Your discord name is not in the spreadsheet!)'

    # Generate unique key
    key = today +' | '+ user + ' | attendance'
    # print("key:", key)
    
    # Check if key already exists
    if key in gsheet.get_keys(spreadsheet_scoring_id):
        return f'Student {message.author.name} has already checked-in today!'

    now = datetime.now().time()

    # print("Class_status:", class_status)
    if class_status=="Full_time":
      late = datetime.strptime('10:15:00','%H:%M:%S').time()
    else:
      late = datetime.strptime('19:15:00','%H:%M:%S').time()

    # Give point if on-time. minus point if late
    if  now > late:
        score = -2
    else:
        score = 1

    # Generate Attendance data row
    body = {'values': [[today, user, score, 'attendance', key]]}

    # Append data row to Student Scoring file
    gsheet.add_point(body, spreadsheet_scoring_id)

    return "Done"


# Command: Show missing students
def missing(message, channel):
    try:
        # Get channel_id from metadata
        metadata = gsheet.get_metadata()

        spreadsheet_scoring_id = metadata[metadata['Channel'] == channel].iloc[:, 2].to_numpy()[0]

        cohort = metadata[metadata['Channel'] == channel]['Cohort'].values[0]

        # Get list of users and their Disord account
        users = gsheet.get_users(spreadsheet_scoring_id, cohort)

        if users == {}:
            return f'Cohort is inactive!'


        # Today
        today = datetime.strftime(datetime.now().date(), '%Y-%m-%d')

        # Unique keys from log
        log = gsheet.get_keys(spreadsheet_scoring_id)

        count = 0
        missing = []

        for discord_name, user in users.items():
            key = today +" | "+user +" | attendance"
            
            if key not in log:
                count += 1
                missing.append(discord_name)

        if count == 0:
            message = "Everybody is here! Yayyy!"
        else:
            message = f"We are missing {count} student(s):\n"

            for s in missing:
                message += f"- {s}\n"

    except Exception as err:
        print(err)

    return  message

# Command: Give points to students
def give(message, channel):

    # Verify authorized users
    metadata = gsheet.get_metadata()

    authorized_users = metadata[metadata['Channel'] == channel]['Instructors'].values[0]

    spreadsheet_scoring_id = metadata[metadata['Channel'] == channel].iloc[:, 2].to_numpy()[0]

    
    # print(authorized_users)
    # print(message.author.name)
    if message.author.name not in authorized_users.split(','):
        return 'Authorization Error: Your are not allowed to give points!'

    # Verify point
    point, activity = message.content.split()[2:4]
    # print("activity", activity)

    # print(spreadsheet_scoring_id)

    # Verify activity
    valid_activities = gsheet.get_activity(spreadsheet_scoring_id)
    
    # print("activities", valid_activities)
    if activity not in valid_activities:
        return 'Invalid Argument: Activity not found.'

    # List of mentioned students, excluding bot
    mentions = [u.name for u in message.mentions if u.name != BOT_NAME]
    # Verfiy users

    if len (mentions) == 0:
        return 'Invalid Argument: No student specified.'

    try:
        users = gsheet.get_users(spreadsheet_scoring_id)

        if users == {}:
            return  f'Cohort is inactive!'

        students = []
        for s in mentions:
            students.append(users[s])
        
    except Exception as err:
        print(err)
        return f'Student {s} not found!'

    # Notes
    notes = message.content.split()[4:]

    for i, word in enumerate(notes):
        # Exclude mentioned from notess
        if word.startswith('<@'):
            notes[i] = ''

    notes = ' '.join(notes)

    # Today
    today = datetime.strftime(datetime.now().date(), '%Y-%m-%d')

    # Generate data row
    body = {'values': [[today, student, point, activity, notes] for student in students]}

    # Append data row
    gsheet.add_point(body, spreadsheet_scoring_id)
    

    congrats = ['Good job', 'Spendid', 'You are amazing', 'Keep it up', 'Love you', 'Amazing skill','Super smart', 'Pretty awesome','You are the best','Absolutely amazing']

    comforts = ["It's ok :((", "Sad sad...", "Try again next time!", "It happens even to the best of us!", "Oh no..."]

    if int(point) > 0:
        return f'{", ".join(mentions)} just earned **{point} point(s)** in **{activity}**! {random.choice(congrats)}!'
    else:
        return f'{", ".join(mentions)} just got points deduced **{point} point(s)** in **{activity}**! {random.choice(comforts)}!'

