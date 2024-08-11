from tkinter import Tk, Frame, StringVar, OptionMenu
from typing import Union

class DropdownMenu:
    def __init__(self, root:Union[Tk, Frame], options: list[str], default: str = "Select an option") -> None:
        self.root = root
        self.options = options
        self.__default = default

        self.__selectedOption = StringVar()
        self.__selectedOption.set(self.__default)

        self.dropdownMenu = OptionMenu(self.root, self.__selectedOption, *self.options)
    
    @property
    def selectedOption(self) -> str:
        return self.__selectedOption.get()
    
    @property
    def default(self) -> str:
        return self.__default

    def Select(self, selection:str) -> None:
        if selection in self.options or selection == self.default:
            self.__selectedOption.set(selection)

    def pack(self, anchor = "w") -> None:
        self.dropdownMenu.pack(anchor=anchor) # type: ignore
    
    def grid(self, row:int, column:int, sticky: str = "nw") -> None:
        self.dropdownMenu.grid(row=row, column=column, sticky=sticky)
