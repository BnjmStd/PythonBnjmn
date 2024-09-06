from utils.helpers import (
    validate_regular_expression,
    convert_to_Afnd,
    convert_afnd_to_afd,
    convert_to_afd_min
)

class Expression:
    def __init__(self) -> None:
        self.ER: str = input("Enter a regular expression: ")
        self.AFND: str = None
        self.AFD: str = None
        self.AFDMinimizado: str = None

    # validación básica BÁSICA de una ER
    def isValidRegularExpression(self) -> bool:
        return validate_regular_expression(self.ER)
        
    def convertToAFND(self) -> None:
        AFND: str = convert_to_Afnd(self.ER)
        self.AFND = AFND

    def convertToAFD(self) -> None:

        if self.AFND is None:
            print("AFND not computed. Convert ER to AFND first.")
            return

        AFD: str = convert_afnd_to_afd(self.AFND)
        self.AFD = AFD

    def convertToAFDMinimizado(self) -> None:
        if self.AFND is None:
            print("AFND not computed. Convert ER to AFND first.")
            return
        
        if self.AFD is None:
            print("AFD not computed. Convert ER to AFD first.")
            return
        
        AFDMIN = convert_to_afd_min(self.AFD)
        self.AFDMinimizado = AFDMIN

    def showRegularExpressionInit(self) -> None:
        print (f"{self.ER}")

    def showRegularAFND(self) -> None:
        print (f"{self.AFND}")
    
    def showRegularAFD(self) -> None:
        print (f"{self.AFD}")

    def showRegularAFDMinimizado(self) -> None:
        print (f"{self.AFDMinimizado}")
