Input: [“lint”,“code”,“love”,“you”] 
Output: [“lint”,“code”,“love”,“you”]
Explanation: One possible encode method is: “lint:;code:;love:;you”
# easy solution is to define a delimiter which could be any special character like # or / to separate words in encode method.
However, this special character might appear in the word in real world. We can get around it by appending an escaped character or size of the word.
Here, we append the size of the word when encoding. 
   def encode(self, strs):
        res = ''                                # store the encoded result here
        for s in strs:
            encoded = str(len(s)) + '#' + s     # 4#lint
            res += encoded
        return res
     
#    @param: str: A string  @return: dcodes a single string to a list of strings
    def decode(self, str):
        res, i = [], 0                          # res a return, i=pointer for the number of string. 
        while i < len(str):                     # string 0 na hole
            h = i                               # h= for the '#' , initially h=0, then increment until found '#'
            while h < len(str) and str[h] != '#':    # while h less than string number, 0< 4 and str[0] 4!= '#'
                h += 1                          # increment h until found '#'
            size = int(str[i:h])                # string size = str[ i:h], i to h r vitore rakhsi 4# string ke int convert 
            res.append( str[h + 1: h + 1 + size])     # 2: (2+4=6)    2,3,4,5
            i = h + 1 + size                    # i pointer increase to 6 number a 
        return res
