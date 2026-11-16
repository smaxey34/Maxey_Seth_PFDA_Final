
def set_text_type(type_input):
    if type_input == "g":
        text_type = "game"
    elif type_input == "a":
        text_type = "animation"
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
        if text_type == "game":
            run = False
        elif text_type == "animation":
            run = False
        elif text_type == 2:
            print("input not recognized, try again" + "\n")

    run = True
    while run == True:
        print("Please enter distance from camera in meters rounded to a whole number!" + "\n")
        dist = input()
        if dist.isdigit():
            run = False
        else:
            print("input not recognized, try again" + "\n")

    run = True
    while run == True:
        print("Please enter height of object in meters rounded to a whole number!" + "\n")
        height = input()
        if height.isdigit():
            run = False
        else:
            print("input not recognized, try again" + "\n")


    print("The optimal resolution for your " + text_type + " is " + dist + height)
    
    
    run = True
    while run == True:
        print("Conform converson of included image file? (y/n)")
        convert_img = input()
        if convert_img == "y":
            run = False
            print("image resized! Have a great day!")
        elif convert_img == "n":
            run = False
            print("Have a great day!")
        else:
            print("input not recognized, try again" + "\n")
    



if __name__ == "__main__":
        main()