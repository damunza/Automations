import time, sys

'''
a program to mamke a zigzag pattern until its interupted

if intended use of keyboard is required in linux one must be root
'''

print("Press 'C' to exit the program")
time.sleep(0.5)

indent = 0
indenttrue = True

try:
    while True:
        print((' ' * indent) + '*********')
        time.sleep(0.1)
        if indenttrue:
            indent += 1
            if indent == 20:
                indenttrue = False

        else:
            indent -=1
        if indent == 0:
            indenttrue = True

        # breaking out
        # if keyboard.on_press('c'):
        #         break

except KeyboardInterrupt:
    sys.exit()
