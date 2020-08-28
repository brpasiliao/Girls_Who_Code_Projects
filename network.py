class User:
  def __init__(self, username):
    self.username = username
    self.connections = []
    self.sentRequests = []
    self.receivedRequests = []

  def addConnection(self, aUser):
    self.connections.append(aUser)

  def printConnections(self):
    for user in self.connections:
      print(user.username)

  def sendRequest(self, toUser):
    userRequest = Request(self, toUser)

  def receiveRequest(self, fromUser):


class Request:
  def __init__(self, fromUser, toUser):
    self.fromUser = fromUser
    self.toUser = toUser
    self.accepeted = false

  def message(self, fromUser):
    print("> " + fromUser.username + " wants to connect with you! Accept? (y)es or (n)o")
    answer = input("> ")
    if input == "y":
      not accepeted




users = []



def start():
  print("> Hello! (c)reate a new user, (p)rint all users, (l)og in, or (q)uit the program")
  answer = input("> ")
  if answer == "c":
    createUser()
  elif answer == "p":
    printUsers(start)
  elif answer == "l":
    login()
  elif answer == "q":
    quit(start)
  else:
    start()

def quit(backTo, *args):
  print("> Do you really want to leave? (y)es or (n)o")
  answer = input("> ")
  if answer == "y":
    print("Goodbye!")
    exit()
  elif answer == "n":
    backTo(*args)
  else:
    quit()

def createUser():
  print("> Enter a new username or go (b)ack")
  answer = input("> ")
  if answer == "b":
    start()
  else:
    if not users:
      userCreated(answer)
    else:
      for aUser in users:
        if answer == aUser.username:
          print("User " + answer + " already exists!")
          createUser()
        else:
          userCreated(answer)

def userCreated(answer):
  users.append(User(answer))
  print("You created the new user, " + answer + "!")
  start()

def printUsers(backTo, *args):
  if not users:
    print("No one likes my program")
    backTo(*args)
  else:
    print("All users:")
    for aUser in users:
      print(aUser.username)
    backTo(*args)

def login():
  print("> Enter your username or go (b)ack")
  answer = input("> ")
  if answer == "b":
    start()
  else:
    for aUser in users:
      if answer == aUser.username:
        log(aUser)
    print("User " + answer + " does not exist!")
    login()

def log(theUser):
  print("Welcome, " + theUser.username + "!")
  print("> What you can do: print all (u)sers, (m)ake a connection, print all (c)onnections, check (r)equests, (l)og out, or (q)uit the program")
  answer = input("> ")
  if answer == "u":
    printUsers(log, theUser)
    # printUsers()
  elif answer == "m":
    addWho(theUser)
  elif answer == "c":
    if not theUser.connections:
      print("No connections yet!")
      log(theUser)
    else:
      print("All connections:")
      theUser.printConnections()
      log(theUser)
  elif answer == "l":
    start()
  elif answer == "q":
    quit(log, theUser)
    # quit()
  else:
    log(theUser)

def addWho(theUser):
  print("> Enter the username of who you want to connect with or go (b)ack")
  answer = input("> ")
  if answer == "b":
    log(theUser)
  else:
    for aUser in users:
      if answer == aUser.username:
        if answer == theUser.username:
          print("You can't connect with yourself!")
          addWho(theUser)
        else:
          for connection in theUser.connections:
            if answer == connection.username:
              print("You and " + answer + " are already connected!")
              addWho(theUser)
          theUser.sendRequest(aUser)
          print("You sent a connection request to " + answer + "!")
          log(theUser)
    print("User " + answer + " does not exist!")
    addWho(theUser)



start()
