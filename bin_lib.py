#!/bin/env python3
"""
follow : @qywok_exploiter_357
"""
import unittest
class attributes:
    def __init__(self):
        self.decimal=[128,64,32,16,8,4,2,1]
        self.bit=len(self.decimal)              # length : 8 bit
class convert:
    def __init__(self,value):
        self.value=value
    def bin2dec(self):
        if str(type(self.value))=="<class 'str'>":
            if len(self.value)==attributes().bit:
                index=self.value
                value=0
                for attribute in range(len(attributes().decimal)):
                    if int(index[attribute])==1:
                        value+=int(index[attribute])*attributes().decimal[attribute]
                    elif int(index[attribute])==0:
                        value+=int(index[attribute])
                return value
        else:
            return False
    def dec2bin(self):
        if str(type(self.value))=="<class 'int'>":
            index=self.value
            point=index
            value=[]
            for attribute in range(len(attributes().decimal)):
                if (point>attributes().decimal[attribute])|(point==attributes().decimal[attribute]):
                    value.append("1")
                    point-=attributes().decimal[attribute]
                else:
                    value.append("0")
            return "".join(value)
        else:
            return False 
if __name__ == "__main__":
    class testing(unittest.TestCase):
        def output_testing(self):
            self.assertEqual(convert(138).dec2bin(),"10001010")
