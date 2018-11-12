from os import getcwd
from sys import platform
from csv import DictReader
from graphics import Entry, Image, GraphWin, Point, Rectangle, Text


# Purpose: To output the current working directory w/ the proper trailing delim
#   Input: None
#  Output: The CWD with the proper OS delim
def myCWD():
    myCWD = getcwd()
    myOS = platform
    if 'win32' in myOS:
        myDelim = '\\'  # Windows
    else:
        myDelim = '/'  # Linux and Mac
    myCWD += myDelim
    return myCWD


# Purpose: To reset a csv file to 0
#   Input: The filename to reset (str)
#  Output: None
def reset(fileName):
    f = open(myCWD() + fileName + ".csv", "w")
    print("water,gatorade,chips,popcorn,nuts,candy,cash", file=f)
    print("0,0,0,0,0,0,0", file=f)
    f.close()
    return


# Purpose: To open a csv file and read the contents into a dictionary
#   Input: The filename (str)
#  Output: a dictionary containing the csv contents
def open_csv(fileName):
    sales = []
    reader = DictReader(open(myCWD() + fileName + ".csv"))
    for row in reader:
        sales.append(row)
    return sales


# Purpose: To save a dictionary to a csv file
#   Input: The file to save to (str) and the dictionary to save
#  Output: None
def save_csv(fileName, sales):
    f = open(fileName + ".csv", "w")

    print("water,gatorade,chips,popcorn,nuts,candy,cash", file=f)

    print(sales[0]["water"] + ","
          + sales[0]["gatorade"] + ","
          + sales[0]["chips"] + ","
          + sales[0]["popcorn"] + ","
          + sales[0]["nuts"] + ","
          + sales[0]["candy"] + ","
          + sales[0]["cash"], file=f)

    f.close()

    return


# Purpose: To determine whether a point is in a rectangle or not
#   Input: A rectangle and a point
#  Output: A True or False whether the point is in the rectangle or not
def isPtInRect(rectangle, point):
    point1 = rectangle.getP1()      # First rectangle point
    point1X = point1.getX()         # First rectangle point X coord
    point1Y = point1.getY()         # First rectangle point Y coord
    point2 = rectangle.getP2()      # Second rectangle point
    point2X = point2.getX()         # Second rectangle point X coord
    point2Y = point2.getY()         # Second rectangle point Y coord
    sideOneLength = abs(point1X - point2X)
    sideTwoLength = abs(point1Y - point2Y)
    pointXvalue = point.getX()      # Input point X coord
    pointYvalue = point.getY()      # Input point Y coord
    if (abs(point1X - pointXvalue) <= sideOneLength and \
        abs(point2X - pointXvalue) <= sideOneLength) and \
        (abs(point1Y - pointYvalue) <= sideTwoLength and \
         abs(point2Y - pointYvalue) <= sideTwoLength):

        inFlag = True

    else:
        inFlag = False

    return inFlag


# Purpose: to display a success window upon completion of an action
#   Input: None
#  Output: None
def confirmation():
    window0 = GraphWin("Success!", 200,100)
    window0.setBackground("white")
    text = Text(Point(100,20), "Success!")
    text.setFace("courier")
    text.draw(window0)

    exitImage = Image(Point(100,65), "icons/exit.png")
    exitImage.draw(window0)
    exitButton = Rectangle(Point(60,48), Point(140,80))
    while True:
        try:
            click = window0.getMouse()
        except:
            window0.close()
            break
        if(isPtInRect(exitButton, click)):
            window0.close()
            break
    return


# Purpose: To record the sale of an item
#   Input: The item sold (key str), the amount sold, and the dictionary
#  Output: The dictionary with the new values
def sell_item(key, quantity, dict):
    if(key == "water"):
        dict[0]["cash"] = str(float(dict[0]["cash"]) + 1 * quantity)

    elif(key == "chips" or key == "popcorn"):
        dict[0]["cash"] = str(float(dict[0]["cash"]) + 1.25 * quantity)

    elif(key == "gatorade" or key == "nuts" or key == "candy"):
        dict[0]["cash"] = str(float(dict[0]["cash"]) + 1.5 * quantity)

    dict[0][key] = str(int((dict[0][key])) + quantity)

    return dict


# Purpose: A popup window that shows the total sale and calculates change
#   Input: The total amount of the sale (float)
#  Output: None
def show_total(amount):
    totalWin = GraphWin("Transaction", 250,250)
    totalWin.setBackground("Yellow")

    amountText = Text(Point(125,50), amount)
    amountText.setStyle("bold")
    amountText.draw(totalWin)
    amountLabel = Text(Point(50,50), "Total:")
    amountLabel.draw(totalWin)

    tenderedBox = Entry(Point(125,100), 5)
    tenderedBox.setText("0")
    tenderedBox.setFill("white")
    tenderedBox.draw(totalWin)
    label = Text(Point(50,100), "Given: ")
    label.draw(totalWin)

    button = Image(Point(125, 200), "icons/button.png")
    button.draw(totalWin)
    buttonRect = Rectangle(Point(50,184), Point(203,218))

    calcFlag = False
    while True:
        errorFlag = False
        try:
            click = totalWin.getMouse()
        except:
            totalWin.close()
            break
        if(isPtInRect(buttonRect, click)):
            if(calcFlag):
                    change.undraw()
            try:
                tendered = tenderedBox.getText()
            except:
                errorFlag = True
                tenderedBox.setText("0")
            if(float(tendered) < amount):
                errorFlag = True
                tenderedBox.setText(str(amount))
            if(not errorFlag):
                change = Text(Point(125, 150), "Change:    "
                              + str(float(tendered) - amount))
                change.setStyle("bold")
                change.draw(totalWin)
                calcFlag = True
    return

