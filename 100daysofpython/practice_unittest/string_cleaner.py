class StringUtilities():
    @staticmethod
    def lower_and_strip(self):
        try:
            return self.lower().strip()
        except AttributeError:
            raise AttributeError()

    @staticmethod
    def reverse_string(string):
        try:
            return string[::-1]
        except TypeError:
            raise TypeError()
