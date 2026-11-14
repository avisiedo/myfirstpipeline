import saludar


class TestSaludar:

    def test_saludo1(self):
        assert "Hola" == saludar.saludo1()

    def test_saludo2(self):
        assert "Buenos días" == saludar.saludo2()

    def test_saludo3(self):
        assert "Hola, ¿Qué tal?" == saludar.saludo3()

    def test_saludo4(self):
        assert "¿Como te encuentras hoy?" == saludar.saludo4()
