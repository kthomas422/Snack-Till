# Kyle Thomas
# Main function for managing the snack till
# It resets the sales csv file to 0 and can rewrite the file to another folder


from snack_till_lib import *


myPath = ""  # Change this path to the csv destination


def main():
    window = GraphWin("Manage Till", 300,175)
    window.setBackground("yellow")

    title = Text(Point(150, 20), "Please Select an Action:")
    title.setFace("courier")
    title.setStyle("bold")
    title.setSize(14)
    title.draw(window)

    printImage = Image(Point(150, 75), "icons/save.png")
    printImage.draw(window)
    printButton = Rectangle(Point(85,60), Point(214,89))

    resetImage = Image(Point(150, 125), "icons/reset.png")
    resetImage.draw(window)
    resetButton = Rectangle(Point(85, 110), Point(214, 140))

    while True:
        try:
            click = window.getMouse()
        except:
            window.close()
            break
        if(isPtInRect(printButton, click)):
           sales = open_csv("sales")
           save_csv(myPath + "snack_till", sales)

        elif(isPtInRect(resetButton, click)):
             reset("sales")
        confirmation()

    return


main()
