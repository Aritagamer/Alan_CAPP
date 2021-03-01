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

    self.__search__()



  def __search__(self):

    for i in range(10):
      self.__Curs__.execute('SELECT * FROM Iztacalco WHERE S_E_%s = "%s"'%(i+1,self.Secc))
      Tables = self.__Curs__.fetchall()

      if Tables:

        Tables = Tables[0]
        self.Zona = Tables[0]
        self.Region = Tables[1]
        self.Colonia = Tables[2]

        break
    
    

    self.__Curs__.execute("INSERT INTO Registro VALUES ('%s', '%s', '%s', %d , '%s', %d, %d, %d);"%(self.Zona,self.Region,self.Colonia,int(self.Secc),self.Nom,int(self.Work),int (self.Whats), int(self.Integ)))
    self.__Con__.commit()
      
      
    