import sqlite3 as SQ
import os,re



class Zona:

  def __init__(self, num):
    pass



class seccional:
  
  def __init__(self,Nombre) :

    self.Zona = None
    self.Region = None
    self.Colonia = None

    self.__Con__ = SQ.connect(Nombre + '.db')
    self.__Curs__ = self.__Con__.cursor()

    self.__Curs__.execute('SELECT name FROM sqlite_master WHERE type="table"')
    Tables =  self.__Curs__.fetchall()

    if not Tables :

      self.__Curs__.executescript('CREATE TABLE Registro(id INTEGER PRIMARY KEY AUTOINCREMENT, Zona INTEGER ,Region Text ,Colonia Text, Sección INTEGER, Nombre TEXT, 	  Labora NUMERIC, Grupo_Whats NUMERIC, Num_Integrantes INTEGER, Num_Registros INTEGER	) ')
      f = open(r'./SQL.txt','r+',encoding="utf-8")
      Tx = f.read()
      self.__Curs__.executescript(Tx)

  def new_secc(self):
    
    os.system("cls")

    print("Introduzca la seccion: ")
    self.Secc = input()
    
    print("Introduzca el nombre del secciónal: ")
    self.Nom = input()

    print("Está cumpliendo el secciónal? ")
    self. Work = input()

    if self.Work == "1":

      print("Numero de registros que tiene: ")
      self.Reg = input()
    else:
      self.Reg = 0
    
    print("Tiene grupo de WhatsApp? ")
    self.Whats = input()

    if self.Whats == "1":
      print("Número de integrantes en el grupo: ")
      self.Integ = input()
    else:
      self.Integ = 0

  def old_secc(self):

    os.system("cls")

    print("Está cumpliendo el secciónal? ")
    self. Work = input()

    if self.Work == "1":

      print("Numero de registros que tiene: ")
      self.Reg = input()
    else:
      self.Reg = 0
    
    print("Tiene grupo de WhatsApp? ")
    self.Whats = input()

    if self.Whats == "1":
      print("Número de integrantes en el grupo: ")
      self.Integ = input()
    else:
      self.Integ = 0

  def up_to_date(self , id):

    self.__Curs__.executescript("UPDATE Registro set Labora = %d , Num_Registros = Num_Registros + %d , Grupo_Whats = %d , Num_Integrantes = Num_Integrantes + %d where id = %d" %(int(self.Work), int(self.Reg),int (self.Whats), int(self.Integ) , int(id)))

  def __search__(self):

    for i in range(10):
      self.__Curs__.execute('SELECT * FROM Iztacalco WHERE S_E_%s = "%s"'%(i+1,self.Secc))
      Tables = self.__Curs__.fetchall()

      self.__Curs__.execute('SELECT id FROM Registro')
      Tables2 = self.__Curs__.fetchall()

      cor = False

      if Tables:
        cor = True
        Tables = Tables[0]
        self.Zona = Tables[0]
        self.Region = Tables[1]
        self.Colonia = Tables[2]

        break
        
    if not cor:

      print("Introduzca la Zona: ")
      self.Zona = input().upper()
      
      print("Introduzca la Region: ")
      self.Region = input().upper()

      print("Introduzca la colonia del seccional: ")
      self.Colonia = input().upper()

    if Tables2:

      self.__Curs__.execute("INSERT INTO Registro (Zona,Region,Colonia,Sección,Nombre,Labora,Grupo_Whats,Num_Integrantes,Num_Registros) VALUES ('%s', '%s', '%s', %d , '%s', %d, %d, %d, %d);"%(self.Zona,self.Region,self.Colonia,int(self.Secc),self.Nom,int(self.Work),int (self.Whats), int(self.Integ), int(self.Reg)))
      self.__Con__.commit()
    else:
      self.__Curs__.execute("INSERT INTO Registro VALUES ('%d' , '%s', '%s', '%s', %d , '%s', %d, %d, %d, %d);"%(1,self.Zona,self.Region,self.Colonia,int(self.Secc),self.Nom,int(self.Work),int (self.Whats), int(self.Integ), int(self.Reg)))
      self.__Con__.commit()


  def disp_secc(self):

    os.system("cls")

    self.__Curs__.execute("Select id, Sección, Nombre from Registro")
    secc = self.__Curs__.fetchall()

    if secc:
      print("Los seccionales registrados son: ")
      for i in secc:
        
        print("\n%d\t%d\t%s"%i)

      print("Digite el numero del seccional que quieres escojer (Para crear uno nuevo prescione 0): ")

      
      seccional = input()

      if seccional == "0":
        self.new_secc()
        self.__search__()
      else:
        self.old_secc()
        self.up_to_date(seccional)

    else:

      self.new_secc()
      self.__search__()

