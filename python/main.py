from compuertas import CompuertaAND,  CompuertaOR,  CompuertaNOT

# Creamos la compuerta AND-1 y sus entradas
and1=CompuertaAND("AND-1")
and1.AgregarEntrada("A", 1)
and1.AgregarEntrada("B", 1)
#print(f"Resultado intermedio de compuerta {and1.getNombre()}: {and1.Calcular()}")

# Creamos la compuerta OR
or2=CompuertaOR("OR-2")
or2.AgregarEntrada("C", 0)
or2.AgregarEntrada(and1.getNombre(), and1)
#print(f"Resultado intermedio de compuerta {or2.getNombre()}: {or2.Calcular()}")

# Y la compuerta NOT
not3=CompuertaNOT("NOT-3")
not3.AgregarEntrada(or2.getNombre(), or2)

# Calculamos la salida de todo el curcuito
print(f"Resultado final: {not3.Calcular()}")








