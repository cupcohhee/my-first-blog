from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import  sys




class Car():
    def __init__(self):
        # paint, calipers, exterior, windows, seat_leater,
        # model = ["bmw", "audi"]
        model_price = {"bmw":1000,"audi":1200}
        wheel_price = {"sharp" :100, "circle":50, "square":20}
        print("Please select from audi and bmw")
        # self.model = input()
        # while self.model not in model_price.keys():
        #     print("Please select from audi and bmw")
        #     self.model = input()
        self.model = "audi"
        self.paint = "red"
        self.wheels = "sharp"
        self.price = model_price[self.model] + wheel_price[self.wheels]

    def calculate_price(self):

        model_price = {"bmw":1000,"audi":1200}
        wheel_price = {"sharp" :100, "circle":50, "square":20}
        self.price = model_price[self.model] + wheel_price[self.wheels]

    def select_paint(self):
        color_list = ["red", "green", "blue", "black", "white"]
        print("Plese type choose one color from red, green blue")
        color = input()
        self.paint = color
        print(self.paint)

    def select_wheels(self):
        wheels = ["sharp","square","circle"]
        # wheel_price = {"sharp" :100, "circle":50, "square":20}

        print(f"Plese select from {wheels}")
        select = input()
        flag = True
        while flag:
            if select not in wheels:
                print(f"Plese select from {wheels}")
                select = input()
            else:
                flag = False

        self.wheels = select

        self.calculate_price()
        print(f"The price of car is {self.price}")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("Car model configure")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label1 = QtWidgets.QLabel(self)
        self.text1 = QtWidgets.QTextEdit(self)
        self.textb = QtWidgets.QTextBrowser(self)
        self.label.setText("Choose your car")

        self.label.move(50, 50)
        self.textb.move(100,100)

        self.b1 = QtWidgets.QPushButton(self)
        # self.b2 = QtWidgets.QPushButton(self)

        self.b1.setText("Audi")
        # self.b2.setText("BMW")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("Information")
        self.textb.setText(f"Mode: {self.model}\nColor: {self.paint}\nWheel: {self.wheels}\nPrice: {self.price}")

        self.update()

    def update(self):
        self.textb.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    # bmw = Car()
    # bmw.select_wheels()
    window()
