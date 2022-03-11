#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR
#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR#####OSCAR

##Como usar pytest en pycharm en lugar de unittest:
# -> ctrl+alt+s
# -> escribir pytest en el buscador
# -> cambiar el framework de testing por defecto a pytest
# -> escribir un test

# Ejemplo de tests
from Fibonacci import Fibbonacci

def test_position_0_returns_1():
    #Arrange
    number = 0

    #Act
    result = Fibbonacci().act(number)

    #Assert
    assert result == 1

def test_position_1_returns_1():
    #Arrange
    number = 1

    #Act
    result = Fibbonacci().act(number)

    #Assert
    assert result == 1