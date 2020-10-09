#! python3
# just copy pasting with pyperclip
# sys.argv for receiving user input from the terminal


import sys, pyperclip

text = {'5days':'Hey guys this is just a reminder; Its five days to due date for payment',
'3days': 'Hey guys in 72 hours the subscription will be renewed',
'now': 'The subscription has been renewed awaiting new password'}

if len(sys.argv) < 2 :
    print('Usage py: myclip.py [keyword] - copy phrase')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print (f'Message for {keyphrase} has been coppied and is ready for deployment')
else:
    print(f'there is no message for {keyphrase}')
