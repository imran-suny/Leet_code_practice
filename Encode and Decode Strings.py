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

class Codec:

    def encode(self, strs):
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s):
        decoded_list = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter '#'
            j = s.find('#', i)
            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the actual string
            decoded_list.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded_list
        
        
codec = Codec()        # Encode
strs = ["hello", "world"]
encoded = codec.encode(strs)
print(f"Encoded: {encoded}")  # Output: "5#hello5#world"

# Decode
decoded = codec.decode(encoded)
print(f"Decoded: {decoded}")  # Output: ["hello", "world"]
