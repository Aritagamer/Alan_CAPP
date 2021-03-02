import Seccional as sec







if __name__ == "__main__":

	decision = 1

	while decision == "1":

		os.system("cls")

		print("SISTEMA DE REGISTRO DE SECCIONALES\n\n")

		print("Ingrese su nombre: ")
		Nombre = input()

		

		Secc = sec.seccional(Nombre)

		Secc.disp_secc()

		print("Quiere seguir en el sistema?\n1 Si 0 No")
		decision = input()

	


		
