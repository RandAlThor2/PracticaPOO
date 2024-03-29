class Medicamento:
    #constructor de la clase Medicamento
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    #Getters de la clase Medicamento
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    #Setters de la clase Medicamento
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:

    #Constructor de la clase Mascota
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]

    #Getters de la clase Mascota    
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

    #Setters de la clase Mascota        
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
        
    #Creé una función para verificar ciertos parámetros de la fecha, para así intentar atrapar errores.
    def verificarFecha(self, fecha):
        lista=fecha.split("/")
        if 1 < int(lista[0]) > 31:
            return False
        elif 1 < int(lista[1]) > 12:
            return False
        elif len(lista[2]) != 4:
            return False
        else:
            return True

    
class sistemaV:
    #Se crean dos diccionarios, uno para felinos y otro para caninos, en los cuales la clave es la historia y el valor es el objeto mascota.
    #Constructor de la clase sistemaV
    def __init__(self):
        self.__lista_mascotasCaninos={}
        self.__lista_mascotasFelinos={}
    
    def verificarExiste(self,historia):
        if historia in self.__lista_mascotasFelinos or historia in self.__lista_mascotasCaninos:
            return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotasCaninos) + len(self.__lista_mascotasFelinos) 
    
    def ingresarMascota(self,mascota):
        #Dependiendo del tipo de mascota, se agrega al diccionario correspondiente, poniendo como clave su Historia
        if mascota.verTipo()== "Canino":
            self.__lista_mascotasCaninos[mascota.verHistoria()] = mascota
        else:
            self.__lista_mascotasFelinos[mascota.verHistoria()] = mascota
   

    #Getters de la clase sistemaV
    def verFechaIngreso(self,historia):
        #Se busca si la historia existe en alguno de los dos diccionarios, y se retorna la fecha correspondiente
        if historia in self.__lista_mascotasCaninos:
            return self.__lista_mascotasCaninos[historia].verFecha()
        elif historia in self.__lista_mascotasFelinos:
            return self.__lista_mascotasFelinos[historia].verFecha() 
        else:
            return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_mascotasCaninos:
            return self.__lista_mascotasCaninos[historia].verLista_Medicamentos() 
            
        elif historia in self.__lista_mascotasFelinos:
            return self.__lista_mascotasFelinos[historia].verLista_Medicamentos()
        return None
    
        #Deleters de la clase sistemaV
    def eliminarMascota(self, historia):
        #Se realiza el cambio para que busque en los diccionarios correspondientes si existe la historia en forma de llave
        #En ese caso se elimina elemento del diccionario
        if historia in self.__lista_mascotasCaninos:
            del(self.__lista_mascotasCaninos[historia])  
            return True  #eliminado con exito
        elif historia in self.__lista_mascotasFelinos:
            del(self.__lista_mascotasFelinos[historia])
            return True #eliminado con exito
        return False 

    #Se crea la función para eliminar el medicamento, la cual da una lista modificada

    def eliminarMedicamento(self, historia,medicamento):
        if historia in self.__lista_mascotasCaninos:
            for med in self.__lista_mascotasCaninos[historia].verLista_Medicamentos():
                if medicamento == med.verNombre():
                    self.__lista_mascotasCaninos[historia].verLista_Medicamentos().remove(med)
                    return True

        elif historia in self.__lista_mascotasFelinos:
            for med in self.__lista_mascotasFelinos[historia].verLista_Medicamentos():
                if medicamento == med.verNombre():
                    self.__lista_mascotasFelinos[historia].verLista_Medicamentos().remove(med)
                    return True
        
            

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
                       \n6- Eliminar medicamento 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))
                #Realicé un pequeño cambio en la sintaxis de como se pide la fecha para poderla verificar teniendo datos más fáciles de comparar.
                fecha=input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")                
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    #Aquí se verifica que el medicamento no esté repetido, y que en el caso de ser así, vuelva a preguntar
                    #por un nombre, el cual también se verifica, hasta que no se encuentre en la lista.
                    while True:
                        encontrado = False
                        for j in lista_med:
                            if nombre_medicamentos == j.verNombre():
                                print("Ya está asignado ese medicamento, por favor ingrese otro.")
                                nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                                encontrado = True
                        if encontrado:
                            continue        
                        else:
                            break
                    dosis =int(input("Ingrese la dosis: "))
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
                #Se usa un while para que si la función retorna True, se asigne el valor de la fecha
                #pero si retorna False, se siga preguntando y llamando a la función
                while True:
                    if mas.verificarFecha(fecha) == True:
                        break
                    else:
                        print("Hay un error en el ingreso de la fecha, vuelva a escribirla.")
                        fecha=input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
                        mas.verificarFecha(fecha)

                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
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
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        #Se da la opción de eliminar un medicamento, para lo cual se llama a una función que realiza esta acción
        #tomando como parámetros la historia clínica y el medicamento que se desea eliminar
        elif menu==6:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            m = input("Ingrese el nombre del medicamento que desea eliminar: ")
            resultado = servicio_hospitalario.eliminarMedicamento(q,m)
            if resultado:
                print("Se ha eliminado el medicamento")
            else:
                print("No se ha podido eliminar el medicamento")

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

