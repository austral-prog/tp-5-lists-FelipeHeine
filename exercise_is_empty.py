# Ejercicio 9: Verificar si una lista está vacía
from jupyter_lsp.specs import JediLanguageServer


def is_empty(lista):
    """
    Determina si una lista está vacía.

    Args:
        lista: Una lista de elementos

    Returns:
        True si la lista está vacía, False en caso contrario
    """
    if len(lista) >= 0 and len(lista)<=0:
        return True
    else:
        return False
