from telethon import TelegramClient
from telethon.errors import rpcerrorlist, FloodWaitError, ChatWriteForbiddenError
import time
import os
import random
import configparser
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest

# config
config = configparser.ConfigParser()  # parser object
config.read("config.ini")
MIN = config['DELAY']['MIN']
MAX = config['DELAY']['MAX']
JOIN_DELAY = config['DELAY']['JOIN_DELAY']
LEAVE_CHAT = config['CHAT']['LEAVE_CHAT']
chats = []
succ_chat = []
dev_by = "@iamironX"
print('*' * 70)
print('[*] dev by @iamironX [*]\n' * 3)
print('-' * 70)
print('[+] Please wait few seconds....')
time.sleep(2)
# take api_id api hash
if os.path.isfile('session.txt'):
    with open('session.txt', 'r') as r:
        data = r.readlines()
    api_id = int(data[0])
    api_hash = data[1]

else:
    api_id = input('Enter api_id: ')
    api_hash = input('Enter api_hash: ')
    with open('session.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

# create session
client = TelegramClient('account1', api_id, api_hash)

# take chat list
with open('list.txt', 'r') as r:
    data = r.readlines()

if int(MIN) < 2:
    print('[WARNING] ')
    print('[!] This value cannot be lower than 2 sec.')
    print('[!!!] Please change this in config.ini')
    print('[!!!!!] I set the default value and continue')
    print('[LOADING]')
    MIN = 10


async def main():
    # print('=' * 70)
    # print('[<3] I will be very pleased if you share your chat list with me [<3]')
    # share = input('[?] Share chat list? Y/n: ')
    # if share == 'Y' or share == 'y':
    #     await client.get_entity(dev_by)
    #     sss = await client.send_file(dev_by, 'list.txt', )
    #     time.sleep(1)
    #     await client.delete_messages(dev_by, message_ids=sss.id, revoke=False)
    #     print('Thank you <3')
    #     print('#' * 70)
    #     time.sleep(2)
    for chat in data:
        try:
            print(f'[+] Trying to join chat:  {chat}')
            time.sleep(random.randint(4, int(JOIN_DELAY)))
            await client(JoinChannelRequest(chat))
            print(f'[+] Join in: {chat}')
            chats.append(chat)
        except Exception as err:
            print(f'[-] Cannot join in: {chat}')
            print(f'Error: , {err}')
            if bool(LEAVE_CHAT):
                try:
                    await client(LeaveChannelRequest(chat))
                    print('[-] Leaving the chat ')
                except:
                    continue
    print('[+]'* 23)
    print('[+]Successfully joined to all chats')
    print('=' * 70)
    print('[<3] I will be very pleased if you share your chat list with me [<3]')
    share = input('[?] Share chat list? Y/n: ')
    if share == 'Y' or share == 'y':
        await client.get_entity(dev_by)
        sss = await client.send_file(dev_by, 'list.txt', )
        time.sleep(1)
        await client.delete_messages(dev_by, message_ids=sss.id, revoke=False)
        print('Thank you <3')
        print('#' * 70)
        time.sleep(2)
    print_chats = input('[+] Print all joined chats? Y/N: ')
    if print_chats == 'Y' or print_chats == 'y':
        for chat in chats:
            print(chat)

    reply = input('[+] Start spam? Y/N ')
    if reply == 'Y' or reply == 'y':
        conf = True
        while conf == True:
            message = input("Enter the message to send here: ")
            print('[+] Start in 3 sec...')
            time.sleep(3)
            for target in chats:
                ent = await client.get_entity(target)
                try:
                    time.sleep(random.randrange(2, int(MIN), int(MAX)))
                    await client.send_message(ent, message)

                    print(f'[+] Successfully send: {target} ')
                except Exception as errr:
                    print('[-] Cannot send message in this chat')
                    if bool(LEAVE_CHAT):
                        try:
                            await client(LeaveChannelRequest(target))
                        except:
                            continue
                        print('[-] Leaving the chat ')
                        print('[-] Leaving the chat ')
                        print(f'Error: , {errr}')
                        time.sleep(random.randrange(2, int(MIN), int(MAX)))

            print('[+] Task completed successfully')
            time.sleep(2)
            again = input('Send message again? Y/N: ')
            if again == 'y' or again == 'Y':
                continue
            else:
                print('Exit\n\nByeee!!!')
                break

    else:
        print('Exit\n\nByeee!!!')




with client:
    client.loop.run_until_complete(main())

