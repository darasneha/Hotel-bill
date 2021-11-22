#Hotel base program
print("\t\t\t****Small Hotel****")
print("\t\t\t\tMenu\n1.Break fast\n2.Lunch\n3.Dinner")
opt='y'
while(opt is 'y'):
    opt1=int(input("Please Enter Your Choice(1,2,3)"))
    if(opt1==1):
        print("Wel-come to break fast menu")
        print("1.edli Rs.10\n2.bonda Rs.15\n3.dosa Rs.20\n4.vada Rs.5")
        opt_1=int(input("Please select an OPtion(1,2,3,4)"))
        if(opt_1==1):
            print("You have selected edli  Enjoy!")
        elif(opt_1==2):
            print("You have selected Bonda Enjoy!")
        elif(opt_1==3):
            print("You have selected dosa Enjoy!")
        elif(opt_1==4):
            print("You have selected vada Enjoy!")
        else:
            print("Invalid Option")
    elif(opt1==2):
        print("Wel_come to Lunch menu")
        print("n1.biriyani Rs.100\n2.sambar rice Rs.50")
        opt_2=int(input("Please selected an Option(1,2)"))
        if(opt_2==1):
            print("You have selected Biriyani Enjoy!")
        elif(opt_2==2):
              print("You have selected sambar rice Enjoy!")
        else:
            print("Invalid Option")
    elif(opt1==3):
        print("Wel-come to Dinner menu")
        print("n1.chapathi Rs.30\n2.rice Rs.50")
        opt_3=int(input("Please selected your Option(1,2)"))
        if(opt_3==1):
            print("You have selected chapathi Enjoy")
        elif(opt_3==2):
              print("You have selected rice only Enjoy")
        else:
            print("Invalid Option")
    opt=int(input("Sir/Madam! Do You want order again(y/n)?"))
    print("Thanks for coming here")
