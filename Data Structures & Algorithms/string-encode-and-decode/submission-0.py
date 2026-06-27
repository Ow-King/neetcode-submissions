class Solution:

    def encode(self, strs: List[str]) -> str:
        seperator = '\x80'
        code = ""
        for string in strs:
            code += str(len(string)) + seperator + string
        return code
        

    def decode(self, s: str) -> List[str]:
        i = 0
        length = 0
        output = []
        while i < len(s):
            temp_string = ""
            length_string = ""
            while i < len(s) and s[i] != '\x80':
                length_string += s[i]
                i += 1

            i += 1
            
            length = int(length_string)
            temp_string = s[i:i+length]
            i += length
            output.append(temp_string)
        
        return output