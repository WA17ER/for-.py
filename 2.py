class Road():
    def __init__(self,length, width):
        self.__length = length
        self.__width = width

    def count(self):
        print(self.__length * self.__width *5)


data = Road(100, 5)
data.count()
