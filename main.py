# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from SSiT.SSiTModel import SSiTModel
from SSiT.controller import getPipesList


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    model = SSiTModel(pipeChars = getPipesList()[0])
    print(model.predict(data=[[11.2736,	0.0,	199.65599999999998,	2781.8047040910365]]))
    model.changePipe(getPipesList()[1])
    print(model.predict(data=[[11.2736, 0.0, 199.65599999999998, 2781.8047040910365]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
