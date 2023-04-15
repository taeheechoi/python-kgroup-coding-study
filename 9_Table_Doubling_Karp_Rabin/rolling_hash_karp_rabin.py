class RollingHash:
    def __init__(self, text, sizepattern):
        self.text = text
        self.hash = 0 
        self.sizepattern = sizepattern

        for i in range(0, sizepattern):
            #ord maps the character to a number
            #subtract out the ASCII value of 'a' to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord('a')+1)*(26**(sizepattern - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = sizepattern

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord('a')+1)*26**(self.sizepattern-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord('a')+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(pattern, text):
    if pattern == '' or text == '':
        return None
    
    if len(pattern) > len(text):
        return None

    rolling_hash = RollingHash(text, len(pattern))
    pattern_hash = RollingHash(pattern, len(pattern))
    #pattern_hash.move_window()

    for i in range(len(text) - len(pattern) + 1):
        if rolling_hash.hash == pattern_hash.hash:
            if rolling_hash.window_text() == pattern:
                return i
        rolling_hash.move_window()
    return None

print(rabin_karp('co', 'i love coding'))