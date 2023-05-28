# ======== 2 ===========

class TextProcessor:

    def get_clean_string(self,string):
        new_string = ""
        for i in string:
            if self.__is_punktiantian__(i):
                new_string += i
        return new_string

    def __is_punktiantian__(self, k):
        T = (",", ";", ":", ".", "!", "?", "-", "'", "|", "‽", "⸮", "(", ")", "[", "]", "{", "}", "<", ">", '"')
        for i in T:
            if k == i:
                return False
        return True

class TextLoader:

    def __init__(self, string):
        self.__text_processor = TextProcessor()
        self.__clean_string = self.set_clean_text(string)

    def set_clean_text(self, string):
        return self.__text_processor.get_clean_string(string)

    @property
    def clean_string(self):
        return print(self.__clean_string," - this text is cleaned")


class Datainterface:
    def __init__(self, string=""):
        self._a = TextLoader(string)


    def process_texts(self, lst):
        for i in lst:
            self._a = TextLoader(i)
            self._a.clean_string

A = Datainterface()
A.process_texts(["qwe,.,123", "asd,.,4565","zxc,.!789"])