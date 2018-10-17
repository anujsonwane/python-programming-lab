from easygui import *
import sys
while 1:
    msgbox("welcome, customer")

    msg ="from where u wanna buy"
    title = "top shopping websites"
    choices = ["amazon", "flipcart", "shopclues"]
    choice = choicebox(msg, title, choices)
               if choices =flipcart:
                  msgbox("f")
                  msg1="what u wanna buy"
                  title1="top brand"
                  choices1 = ["allen solly","levis"]
                  choice1 = choicebox(msg1, title1, choices1)
               elif choices =amazon:
                   msgbox("a")
                   msg="what u wanna buy"
                   title="top brand"
                   choices = ["allen solly","levis"]
                   choice2 = choicebox(msg2, title2, choices2)
               else :
                   msgbox("s")
                   msg="what u wanna buy"
                   title="top brand"
                   choices = ["allen solly","levis"]
                   choice3 = choicebox(msg3, title3, choices3)
    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("    " + str(choice), "   ")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)



