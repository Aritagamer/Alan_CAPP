
class Zona:

  def __init__(self, num):
    pass



class seccional:
  
  def __init__(self) :

    self.Zona = None
    self.Region = None
    self.Colonia = None
    
    print("Introduzca la seccion: ")
    self.Secc = input()
    
    print("Introduzca el nombre del secciónal: ")
    self.Nom = input()
    print("Está cumpliendo el secciónal? ")
    self. Work = input()
    
    print("Tiene grupo de WhatsApp? ")
    self.Whats = input()
    if self.Whats == "1":
      print("Número de integrantes en el grupo: ")
      self.Integ = input()
    else:
      self.Integ = 0
      
      
    