DELKA_POLE = 20

SYMBOL_HRACE = "x"
SYMBOL_POCITACE = "o"

POTREBA_K_VYHRE = 3


def vyhodnot(pole):
    """
    Podle stavu herního pole vrátí:
     řetězec "x", když vyhraje hráč,
     řetězec "o", když vyhraje počítač,
     řetězec "!", když dojde k remíze nebo
     řetězec "-", když je možné ještě pokračovat ve hře
    """
    if SYMBOL_HRACE * POTREBA_K_VYHRE in pole:
        return "x"
    elif SYMBOL_POCITACE * POTREBA_K_VYHRE in pole:
        return "o"
    elif "-" in pole:
        return "-"
    else:
        return "!"


def tah(pole, cislo_policka, symbol):
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    pass


def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """
    pass


def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    pass


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
    pass


if __name__ == "__main__":
    piskvorky1d()
