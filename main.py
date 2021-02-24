import sqlite3 as SQ
import Seccional as sec
import os,re

if __name__ == "__main__":

	print("SISTEMA DE REGISTRO DE SECCIONALES\n\n")
	print("Ingrese su nombre: ")
	Nombre = input()

	f = open(r'./SQL.txt','r+',encoding="utf-8")

	Con = SQ.connect(Nombre + '.db')
	Curs = Con.cursor()
	
	Secc = sec.seccional() 
	Curs.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="Registro"')
	Tables =  Curs.fetchall()

	if not Tables:

		Curs.execute('CREATE TABLE Registro(Zona INTEGER ,Region Text ,Colonia Text, Sección INTEGER, 	  Nombre TEXT PRIMARY KEY, 	  Labora NUMERIC, Grupo_Whats NUMERIC, Num_Integrantes INTEGER	) ')
		Tx = f.read()

		Curs.execute(Tx)
	for i in range(10):
		Curs.execute('SELECT * FROM Iztacalco WHERE S_E_%s = "%s"'%(i+1,Secc.Secc))
		Tables = Curs.fetchall()
		print(Tables)

		if Tables:
			break
	
	Tables = Tables[0]
	Secc.Zona = Tables[0]
	Secc.Region = Tables[1]
	Secc.Colonia = Tables[2]

	Curs.execute("INSERT INTO Registro VALUES ('%s', '%s', '%s', %d , '%s', %d, %d, %d);"%(Secc.Zona,Secc.Region,Secc.Colonia,int(Secc.Secc),Secc.Nom,int(Secc.Work),int (Secc.Whats), int(Secc.Integ)))
	Con.commit()
