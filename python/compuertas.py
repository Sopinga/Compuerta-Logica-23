class CompuertaAND:
  def __init__(self, nombre):
    self.nombre=nombre
    self.entradas={}
    self.salida=None
  
  def getNombre(self):
    return self.nombre

  def AgregarEntrada(self, conector, valor):
    self.entradas[conector]=valor

  def __str__(self):
    return self.nombre

  def __repr__(self):
    return self.nombre
    
  def Calcular(self):
    prod=1
    for elemento in self.entradas:
      if self.entradas[elemento]==0 or self.entradas[elemento]==1:
        prod=prod*self.entradas[elemento]
      else:
        prod=prod*self.entradas[elemento].Calcular()
    return prod

class CompuertaOR:
  def __init__(self, nombre):
    self.nombre=nombre
    self.entradas={}
    self.salida=None
  
  def getNombre(self):
    return self.nombre

  def AgregarEntrada(self, conector, valor):
    self.entradas[conector]=valor

  def __str__(self):
    return self.nombre

  def __repr__(self):
    return self.nombre
    
  def Calcular(self):
    suma=0
    for elemento in self.entradas:
      if self.entradas[elemento]==0 or self.entradas[elemento]==1:
        suma=suma+self.entradas[elemento]
      else:
        suma=suma+self.entradas[elemento].Calcular()
    return suma

class CompuertaNOT:
  def __init__(self, nombre):
    self.nombre=nombre
    self.entrada=(None, None) #nombre conector, valor
    self.salida=None
  
  def getNombre(self):
    return self.nombre

  def AgregarEntrada(self, conector, valor):
    self.entrada=(conector, valor)

  def __str__(self):
    return self.nombre

  def __repr__(self):
    return self.nombre
    
  def Calcular(self):
    if self.entrada[1]==1:
      return 0
    elif self.entrada[1]==0:
      return 1
    else:
      salida= self.entrada[1].Calcular()
      if salida==0:
        return 1
      else:
        return 0
