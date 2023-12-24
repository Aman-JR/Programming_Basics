import heapq

class HuffmanCoding:

    def __init__(self,path):
        self.path = path
        self.__heap = []

    def __make_frequency_dict(self,text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        return freq_dict

    def __buildHeap(self, freq_dict):
        pass
    def compress(self):
        # Get file from path
        # TO read the text from the file
        text = "asdfnalsdasdjfbashdfasdf"

        # Make frequency dictionary using the text
        freq_dict = self.__make_frequency_dict(text)

        # Construct the heap form the frequency dictionary
        self.__buildHeap(freq_dict)

        # Construct the binary tree form the heap
        # Creating the encoded text using te codes
        # Put this encoded text into the binary file
        # Return this binary file as output
        pass

