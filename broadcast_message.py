import discord
import asyncio
import time
import random

EMAIL = "email"
PASS  = "password"

SERVER_ID = 'id'

MESSAGES = list()
MESSAGES.append("Hello World1!")
MESSAGES.append("Hello World2!")
MESSAGES.append("Hello World3!")
MESSAGES.append("Hello World4!")
MESSAGES.append("Hello World5!")

FRIENDS = list()
FRIENDS.append("1588746995513")
FRIENDS.append("1588746995514")

FRIEND_MESSAGES = list()
FRIEND_MESSAGES.append("haha well played!")
FRIEND_MESSAGES.append("gg!")
FRIEND_MESSAGES.append("hey bro, how are you?")

BLACKLIST = list()
BLACKLIST.append("person1")
BLACKLIST.append("person2")

DELAY_MIN   = 45  # 45 seconds
DELAY_MAX   = 300 # 5 minutes
DELAY_BREAK = 180 # 3 minutes

ACTIONS = ['BREAK'] * 5 + ['SEND_FRIEND'] * 5 + ['SEND_MEMBER'] * 90 # 5%, 5% and 90%

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    members = client.get_server(SERVER_ID).members

    n_members = len(members)
    for i, m in enumerate(members):
        print("-------------------------------------------------------------")
        print("member: " + m + "(" + str(i+1) + "/" + str(n_members) + ")")

        # if blacklisted, then pass
        if m.name in BLACKLIST:
            print("blacklisted (ignored): " + m)
            continue

        message_sent = False

        # delay between each member
        delay = random.randint(DELAY_MIN, DELAY_MAX)
        print("waiting for " + str(delay) + " seconds")
        time.sleep(delay)

        while not message_sent:
            what_to_do = random.choice(ACTIONS)
            if what_to_do == "BREAK":
                print("[BREAK] " + str(DELAY_BREAK) + " seconds")
                time.sleep(DELAY_BREAK)

            elif what_to_do == "SEND_FRIEND":
                friend_id = random.choice(FRIENDS)
                friend = client.get_user(friend_id)
                msg = random.choice(FRIEND_MESSAGES) + " (" + str(i) + ")"
                print("[FRIEND MESSAGE] " + friend + " - " + msg)
                ch = await client.start_private_message(friend)
                await client.send_message(ch, content=msg)

            elif what_to_do == "SEND_MEMBER":
                msg = random.choice(MESSAGES)
                print("[MEMBER MESSAGE] " + m + " - " + msg)
                ch = await client.start_private_message(m)
                await client.send_message(ch, content=msg)
                message_sent = True

        print("message sent!\n\n")
    print("job finished!")
    client.logout()

# run the process
client.run(EMAIL, PASS)