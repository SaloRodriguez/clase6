import re

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=0
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
    def eliminarMedicamento(self, nombre_med):
        self.__lista_medicamentos = [med for med in self.__lista_medicamentos if med.verNombre() != nombre_med]

class sistemaV:
    def __init__(self):
        self.__lista_mascotas = {"caninos": {}, "felinos": {}}
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        tipo = mascota.verTipo()
        if self.verNumeroMascotas() >= 10:
            print("No hay espacio disponible para nuevas mascotas.")
            return False
        self.__mascotas[tipo][mascota.verHistoria()] = mascota
        return True 
   
    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 


def solicitarNumero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Ingrese un número válido (positivo).")
                continue
            return valor
        except ValueError:
            print("Error: Ingrese un número válido.")

def validar_fecha(fecha):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", fecha))

def obtener_tipo():
    tipos_validos = {'canino': 'caninos', 'felino': 'felinos'}
    tipo_ingresado = input("Ingrese el tipo de mascota (felino o canino): ").lower().strip()
    if tipo_ingresado not in tipos_validos:
        print("Tipo de mascota no válido.")
        return None
    return tipos_validos[tipo_ingresado]


def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento de una mascota
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            
            historia=solicitarNumero("Ingrese la historia clínica de la mascota: ")
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo= obtener_tipo()
                if not tipo:
                    continue
                peso=solicitarNumero("Ingrese el peso de la mascota: ")
                fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                
                if not validar_fecha(fecha):
                    print("Formato de fecha inválido. Use dd/mm/aaaa.")
                    continue
                
                nm=solicitarNumero("Ingrese cantidad de medicamentos: ")
                lista_med=[]
                nombres_meds=set()

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if nombre_medicamentos in nombres_meds:
                        print("Este medicamento ya ha sido ingresado.")
                        continue
                    
                    nombres_meds.add(nombre_med)
                    dosis =solicitarNumero("Ingrese la dosis: ")
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                
                if servicio_hospitalario.ingresarMascota(mas):
                    print("Mascota ingresada correctamente.")
            else:
                print("Ya existe la mascota con el numero de histoira clinica")


        elif menu==2: # Ver fecha de ingreso
            q = solicitarNumero("Ingrese la historia clínica de la mascota: ")
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            

        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))


        elif menu==4: # Ver medicamentos que se están administrando
            q = solicitarNumero("Ingrese la historia clínica de la mascota: ")
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = solicitarNumero("Ingrese la historia clínica de la mascota: ")
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")


        elif menu==6:
            historia = solicitarNumero("Ingrese la historia clínica de la mascota: ")
            tipo = obtener_tipo()
            if not tipo:
                continue            
            nombre_med = input("Ingrese el nombre del medicamento a eliminar: ")
            mascota = servicio_hospitalario.verMedicamento(historia, tipo)
            if mascota:
                mascota.eliminarMedicamento(nombre_med)
                print("Medicamento eliminado")
            else:
                print("Mascota no encontrada")

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")


if __name__=='__main__':
    main()





            

                

