#Binary one-liner converting the str binary inputs to int decimal numbers, sum them and return the result to binary str
 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        #1. We are converting the input strings to int with base 2, int(a,2) and int (b,2) turns binary to int, then we sum the 2 decimal numbers
        
        #2. The bin() method returns the binary equivalent of the integers. bin() output is always a string and by default it begins with the prefix 0b which represents that the result is a binary string. 
        
        #3. To remove the first 2 symbols "0b", we use the slice operator in python [2:]
        
        return bin(int(a,2)+int(b,2))[2:]
