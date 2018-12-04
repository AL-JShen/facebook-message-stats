import json

filepath = '/Users/js/Desktop/messages/inbox/Hbooboo_fb554a5d40/message.json' #in the form of 'somepath/messages/inbox/conversationname/message.json'

with open(filepath, encoding='UTF-8') as f:
    data = json.load(f)

message_dat = data['messages'][::-1]
senders = [list(i.values())[0] for i in message_dat]
messages = [list(i.values())[2] for i in message_dat]
users = list(set(senders))

print('% of messages, by number of messages, that each user is responsible for')
print('============================================')
for i in users:
    print(i, '{0:.2f}'.format(senders.count(i) / len(senders) * 100))

print()

print('% of messages, by character length, that each user is responsible for')
print('============================================')

msg_lengths = []
for j in users:
    count = 0
    for k in range(len(messages)):
        if senders[k] == j:
            count += len(messages[k])
    msg_lengths.append(count)

for i in range(len(users)):
    print(users[i], '{0:.2f}'.format(msg_lengths[i] / sum(msg_lengths) * 100))

print()

print('average message length of each user')
print('============================================')

for i in range(len(users)):
    print(users[i], '{0:.2f}'.format(msg_lengths[i] / senders.count(users[i])))


'''
#output all messages in the history of the chat
#can pipe into external file to be used for RNN training
all_messages = '\n'.join(messages)
print(all_messages)
'''
