"""
This will extend/modify existing behaviour of str (built_in) class

"""


class Text(str):
    def duplicate(self):
        return self + self


txt = Text("Python")
print(txt.duplicate())
