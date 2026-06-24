class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            length = f'{len(string):03d}'  # strs[i].length < 200
            encoded_string = length + "".join(string)
            encoded.append(encoded_string)
        
        return "".join(encoded)

        
    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0

        while i < len(s):
            start_char = i + 3
            string_length = int(s[i:start_char])
            end_length = start_char + string_length
            string = s[start_char:end_length]
            decoded_strings.append(string)
            i += 3 + string_length

        return decoded_strings
        
              