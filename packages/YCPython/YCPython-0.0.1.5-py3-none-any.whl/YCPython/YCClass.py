class YCClass:
    Count = 0
    def __init__(self):
        YCClass.Count += 1
        self.Count = YCClass.Count
    def __str__(self):
        return ('YCClass ' + str(self.Count))


