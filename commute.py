qhome = "walk or drive: "
qwalk = "bus or lirr: "
qlirr = "subway or speedwalk: "
qdrive1 = "lirr or drive: "
qdrive2 = "bridge or tunnel: "

# def plurality()
#     if plural == True:
#         word += "s"
#     else:
#         None

def end(time, money):
    hours = time // 60
    minutes = time - hours * 60

    if time >= 60:
        print(f"boa, time = {hours} hour & {minutes} minutes, money = ${money}")
    else:
        print(f"boa, time = {minutes} minutes, money = ${money}")


def back(option):
    option()


def lirr(time, money):
    time += 40
    money += 13.50
    user_input = input(qlirr).lower()

    if user_input == "subway":
        time += 7
        money += 2.75
        end(time, money)
    elif user_input == "speedwalk":
        time += 15
        end(time, money)
    else:
        back(lirr)

def drive2(time, money):
    time += 60
    user_input = input(qdrive2).lower()

    if user_input == "bridge":
        end(time, money)
    elif user_input == "tunnel":
        time += 15
        end(time, money)
    else:
        back(drive2)

def drive1(time, money):
    time += 10
    user_input = input(qdrive1).lower()

    if user_input == "lirr":
        lirr(time, money)
    elif user_input == "drive":
        money += 20
        drive2(time, money)
    else:
        back(drive1)

def walk(time, money):
    user_input = input(qwalk).lower()

    if user_input == "bus":
        time += 30
        money += 15
        drive2(time, money)
    elif user_input == "lirr":
        time += 45
        lirr(time, money)
    else:
        back(walk)

def home():
    time = 0
    money = 0
    user_input = input(qhome).lower()

    if user_input == "walk":
        walk(time, money)
    elif user_input == "drive":
        drive1(time, money)
    else:
        back(home)

home()

