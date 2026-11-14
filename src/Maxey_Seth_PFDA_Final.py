
def set_text_type(type_input):
    if type_input == "g":
        text_type = 0
    elif type_input == "a":
        text_type = 1
    elif type_input:
         text_type = 2
    # 0 is game, 1 is animation
    return text_type
    
         


def main():
    run = True
    while run == True:
        print("Hello, welcome to the texture resolution calculator." + "\n" + "Please indicate whether these are for a game or an animation! (g/a)")
        type_input = input()
        text_type = set_text_type(type_input)
        if text_type == 0:
            run = False
        elif text_type == 1:
            run = False
        elif text_type == 2:
            print("input not recognized, try again" + "\n")
    
    print("Please enter distance from camera in meters rounded to a whole number!" + "\n")
    dist = input()
    print("Please enter height of object in meters rounded to a whole number!" + "\n")
    height = input()

    print(dist + height)



if __name__ == "__main__":
        main()