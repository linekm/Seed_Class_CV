import numpy as np

class CifarClassfication:
    def __init__(self):
        pass

    def train(self, dataArr, labelArr):
        self.dataTr = dataArr
        self.labelTr = labelArr

    def predict(self, n, testDataArr):
        return 0