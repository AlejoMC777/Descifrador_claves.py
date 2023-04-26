from test_descifrador_claves import descifrador_claves

def test_descifrador_claves():
    clave_cifrada = "875952"
    resultado = descifrador_claves(clave_cifrada)
    assert resultado == "La clave descifrada es 8759"
