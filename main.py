import Seccional as sec
import os







if __name__ == "__main__":

	decision = 1

	

	print("SISTEMA DE REGISTRO DE SECCIONALES\n\n")

	print("Ingrese su nombre: ")
	Nombre = input()

	while int(decision) == 1:

		os.system("cls")

		Secc = sec.seccional(Nombre)

		Secc.disp_secc()

		print("\n\nQuiere seguir en el sistema?\n1 Si 0 No")
		decision = input()

	


		
