from guizero import App, PushButton, Text, TextBox, Box, Window

usernames = []
passwords = []

f = open("userData.csv", "r")
for row in f:
    data = row.strip().split(",")
    usernames.append(data[2])
    passwords.append(data[3])


def checkingUser():
  if insertID.value in usernames and insertP.value in passwords:
    if usernames.index(insertID.value) == passwords.index(insertP.value):
      print("Login Succeed")
      insertID.value = ""
      insertP.value = ""
    else:
      print("Username or Password not Found")
      insertID.value = ""
      insertP.value = ""
  else:
    print("Username or Password not Found")
    insertID.value = ""
    insertP.value = ""



def register():
  registerWindow.show(wait=True)

app1 = App(title="Login Page", width=350, height=180)
registerWindow = Window(app1, title="Register", visible=False)

Box1 = Box(app1, width="fill")
title = Text(Box1, text="Login")

Box2 = Box(app1, width="fill")
ID = Text(Box2, text="ID: ", align="left")
insertID = TextBox(Box2, align="left", width="fill")

Box3 = Box(app1, width="fill")
Password = Text(Box3, text="Pwd: ", align="left")
insertP = TextBox(Box3, align="left", width="fill")

Box4 = Box(app1, width="fill")
loginButton = PushButton(Box4, text="Login", command=checkingUser)

Box5 = Box(app1, width="fill", align="bottom")
registerButton = PushButton(Box5, command=register, text="Register", align="left")
findButton = PushButton(Box5, text="Find Password", align="right")

app1.display()
