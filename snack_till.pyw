# Kyle Thomas
# Driver for snack till.
# Takes in items sold and displays total and change to give, writes sales
# to a csv file for retrieval later.


from snack_till_lib import *


def main():
    sales = open_csv("sales")

    window = GraphWin("Snack Till", 300,500)
    window.setBackground("light blue")
    banner = Text(Point(150, 20), "Snack Till")
    banner.setStyle("bold")
    banner.setFace("courier")
    banner.setSize(18)
    banner.draw(window)

    waterText = Text(Point(60,80), "     Water:")
    waterText.setFace("courier")
    waterText.draw(window)

    waterBox = Entry(Point(200, 80), 7)
    waterBox.setFill("White")
    waterBox.setText("0")
    waterBox.draw(window)

    gatText = Text(Point(50, 140), "    Soda:")
    gatText.setFace("courier")
    gatText.draw(window)

    gatBox = Entry(Point(200, 140), 7)
    gatBox.setFill("White")
    gatBox.setText("0")
    gatBox.draw(window)

    chipText = Text(Point(58, 200), "     Chips:")
    chipText.setFace("courier")
    chipText.draw(window)

    chipBox = Entry(Point(200, 200), 7)
    chipBox.setFill("White")
    chipBox.setText("0")
    chipBox.draw(window)

    popText = Text(Point(58, 260), "   Popcorn:")
    popText.setFace("courier")
    popText.draw(window)

    popBox = Entry(Point(200, 260), 7)
    popBox.setFill("White")
    popBox.setText("0")
    popBox.draw(window)

    nutText = Text(Point(58, 320), "      Nuts:")
    nutText.setFace("courier")
    nutText.draw(window)

    nutBox = Entry(Point(200, 320), 7)
    nutBox.setFill("White")
    nutBox.setText("0")
    nutBox.draw(window)

    candyText = Text(Point(58, 380), "Chocolates:")
    candyText.setFace("courier")
    candyText.draw(window)

    candyBox = Entry(Point(200, 380), 7)
    candyBox.setFill("White")
    candyBox.setText("0")
    candyBox.draw(window)

    calc = Image(Point(150, 450), "icons/confirm.png")
    calc.draw(window)
    calcButton = Rectangle(Point(191, 464), Point(38,436))

    while True:
        water = 0
        gat = 0
        chip = 0
        pop = 0
        nut = 0
        candy = 0
        errorFlag = False

        try:
            click = window.getMouse()
        except:
            window.close()
            break

        if(isPtInRect(calcButton, click)):
            try:
               water = int(waterBox.getText())
               gat = int(gatBox.getText())
               chip = int(chipBox.getText())
               pop = int(popBox.getText())
               nut = int(nutBox.getText())
               candy = int(candyBox.getText())
            except:
                waterBox.setText("0")
                gatBox.setText("0")
                chipBox.setText("0")
                popBox.setText("0")
                nutBox.setText("0")
                candyBox.setText("0")
                errorFlag = True
            if ((not errorFlag) and (water < 0) and (gat < 0) and (chip < 0)
                and (pop < 0) and (nut < 0) and (candy < 0)):

                print("logic error")
                waterBox.setText("0")
                gatBox.setText("0")
                chipBox.setText("0")
                popBox.setText("0")
                nutBox.setText("0")
                candyBox.setText("0")
                errorFlag = True

            if (not errorFlag):
                preCash = float(sales[0]["cash"])
                sales = sell_item("water", water, sales)
                sales = sell_item("gatorade", gat, sales)
                sales = sell_item("chips", chip, sales)
                sales = sell_item("popcorn", pop, sales)
                sales = sell_item("nuts", nut, sales)
                sales = sell_item("candy", candy, sales)
                transCash = float(sales[0]["cash"]) - preCash
                show_total(transCash)

                waterBox.setText("0")
                gatBox.setText("0")
                chipBox.setText("0")
                popBox.setText("0")
                nutBox.setText("0")
                candyBox.setText("0")

                save_csv(myCWD() + "sales", sales)
main()
