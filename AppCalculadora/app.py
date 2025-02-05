from PyQt5 import uic, QtWidgets

def soma():
    N1 = int(cal.lev1.text())
    N2 = int(cal.lev2.text())
    RES = (N1+N2)
    SRES = str(RES)
    cal.pteres.setPlainText(SRES)

def subtrair():
    N1 = int(cal.lev1.text())
    N2 = int(cal.lev2.text())
    RES = (N1-N2)
    SRES = str(RES)
    cal.pteres.setPlainText(SRES)

def multiplicar():
    N1 = int(cal.lev1.text())
    N2 = int(cal.lev2.text())
    RES = (N1*N2)
    SRES = str(RES)
    cal.pteres.setPlainText(SRES)

def dividir():
    N1 = int(cal.lev1.text())
    N2 = int(cal.lev2.text())
    RES = (N1/N2)
    SRES = str(RES)
    cal.pteres.setPlainText(SRES)

def limpar():
    cal.lev1.clear()
    cal.lev2.clear()
    cal.pteres.clear()




app=QtWidgets.QApplication([])
cal=uic.loadUi("cal.ui")
cal.Btnsomar.clicked.connect(soma)
cal.Btnsubtrair.clicked.connect(subtrair)
cal.Btnmultiplicar.clicked.connect(multiplicar)
cal.Btndividir.clicked.connect(dividir)
cal.Btnlimpar.clicked.connect(limpar)
cal.show()
app.exec()