OBJETOS = {
    "botella de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "450 años"
    },
    "bolsa de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "10-20 años"
    },
    "caja de cartón": {
        "reciclable": True,
        "tiempo_descomposicion": "2 meses"
    },
    "cepillo de dientes": {
        "reciclable": False,
        "tiempo_descomposicion": "500 años",
        "manualidad": "puedes usarlo para limpiar esquinas o teclados difíciles"
    },
    "envase de yogur": {
        "reciclable": True,
        "tiempo_descomposicion": "30-50 años"
    },
    "vaso de papel con recubrimiento plástico": {
        "reciclable": False,
        "tiempo_descomposicion": "30 años",
        "manualidad": "puedes usarlo como maceta para plantar semillas o hacer títeres de dedos"
    }
}

def evaluar_objeto(nombre_objeto):
    """
    Evalúa si un objeto es reciclable, su tiempo de descomposición y posibles manualidades.
    """
    nombre_objeto = nombre_objeto.lower()
    datos = OBJETOS.get(nombre_objeto)
    if not datos:
        return f"Objeto no encontrado en la base de datos. Intenta con uno de estos nombres: {list(OBJETOS.keys())}."
    
    accion = "reciclar" if datos["reciclable"] else "desechar adecuadamente"
    resultado = (
        f"OBJETO: {nombre_objeto}\n"
        f"ACCION: {accion}\n"
        f"TIEMPO DE DESCOMPOSICIÓN: {datos['tiempo_descomposicion']}\n"
    )
    if not datos["reciclable"] and "manualidad" in datos:
        resultado += f"MANUALIDAD: {datos['manualidad']}\n"
    return resultado

if __name__ == "__main__":
    print(evaluar_objeto("vaso de papel con recubrimiento plástico"))
