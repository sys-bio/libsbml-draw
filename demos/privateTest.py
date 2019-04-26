# -*- coding: utf-8 -*-
class PrivateTest():
    
        def __init__(self):
            self.__x = 3
            
        def testPrivates(self):
            print("x: ", self.__x)
            self.__printPrivates()
        
        def __printPrivates(self):
            print("printPrivates")
            
            





pt = PrivateTest()

print("print x: ", pt._PrivateTest__x)

print("print pt: ", pt._PrivateTest__printPrivates())

pt.testPrivates()            




