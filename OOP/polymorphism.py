from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# this method is responsible for rendering UI at runtime
# remember this method will not know what kind of control is
# this is known as dynamic polymorphism
def render(controls):
    for control in controls:
        control.draw()


textbox = TextBox()
ddl = DropDownList()

render([textbox, ddl])
