from clases.expression import *

def main() -> None:
    # invocamos constructor
    ER = Expression()
    # validamos
    ER.isValidRegularExpression()
    # mostramos la ER
    ER.showRegularExpressionInit()
    # convertimos a AFND
    ER.convertToAFD()

if __name__ == "__main__":
    main()