class Direccion:
    def __init__(self):
        self.__Calle = ""
        self.__Piso = ""
        self.__Ciudad = ""
        self.__CodigoPostal = ""

    def GetCalle(self):
        return self.__Calle

    def GetPiso(self):
        return self.__Piso

    def GetCiudad(self):
        return self.__Ciudad

    def GetCodigoPostal(self):
        return self.__CodigoPostal

    def SetCalle(self, calle):
        self.__Calle = calle

    def SetPiso(self, piso):
        self.__Piso = piso

    def SetCiudad(self, ciudad):
        self.__Ciudad = ciudad

    def SetCodigoPostal(self, codigoPostal):
        self.__CodigoPostal = codigoPostal


class Persona:
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__FechaNacimiento = ""

    def GetNombre(self):
        return self.__Nombre

    def GetApellidos(self):
        return self.__Apellidos

    def GetFechaNacimiento(self):
        return self.__FechaNacimiento

    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def SetFechaNacimiento(self, fechaNacimiento):
        self.__FechaNacimiento = fechaNacimiento


class Telefono:
    def __init__(self):
        self.__TelefonoFijo = ""
        self.__TelefonoMovil = ""
        self.__TelefonoTrabajo = ""

    def GetTelefonoFijo(self):
        return self.__TelefonoFijo

    def GetTelefonoMovil(self):
        return self.__TelefonoMovil

    def GetTelefonoTrabajo(self):
        return self.__TelefonoTrabajo

    def SetTelefonoFijo(self, telefonoFijo):
        self.__TelefonoFijo = telefonoFijo

    def SetTelefonoMovil(self, telefonoMovil):
        self.__TelefonoMovil = telefonoMovil

    def SetTelefonoTrabajo(self, telefonoTrabajo):
        self.__TelefonoTrabajo = telefonoTrabajo


class Contacto(Direccion, Persona, Telefono):
    def __init__(self):
        self.__Email = ""

    def GetEmail(self):
        return self.__Email

    def SetEmail(self, email):
        self.__Email = email

    def MostrarContacto(self):
        print("*****Contacto*****")
        print("Nombre:", self.GetNombre())
        print("Apellidos:", self.GetApellidos())
        print("Fecha de nacimiento:", self.GetFechaNacimiento())
        print("Teléfono fijo:", self.GetTelefonoFijo())
        print("Teléfono móvil", self.GetTelefonoMovil())
        print("Teléfono trabajo", self.GetTelefonoTrabajo())
        print("Calle:", self.GetCalle())
        print("Piso:", self.GetPiso())
        print("Ciudad:", self.GetCiudad())
        print("Código Postal:", self.GetCodigoPostal())
        print("Email:", self.__Email)
        print("******************")


class Agenda():
    def __init__(self, path):
        self.__ListaContactos = []
        self.__Path = path

    def CargarContactos(self):
        try:
            fichero = open(self.__Path, "r")
        except:
            print("No existe el fichero en la agenda")
        else:
            contactos = fichero.readlines()
            fichero.close()
            if (len(contactos) > 0):
                for contacto in contactos:
                    datos = contacto.split("#")
                    if (len(datos) == 11):
                        nuevocontacto = Contacto()
                        nuevocontacto.SetNombre(datos[0])
                        nuevocontacto.SetApellidos(datos[1])
                        nuevocontacto.SetFechaNacimiento(datos[2])
                        nuevocontacto.SetTelefonoFijo(datos[3])
                        nuevocontacto.SetTelefonoMovil(datos[4])
                        nuevocontacto.SetTelefonoTrabajo(datos[5])
                        nuevocontacto.SetCalle(datos[6])
                        nuevocontacto.SetPiso(datos[7])
                        nuevocontacto.SetCiudad(datos[8])
                        nuevocontacto.SetCodigoPostal(datos[9])
                        nuevocontacto.SetEmail(datos[10])
                    print("Se han cargado un total de: ", len(self.__ListaContactos), "contactos")

    def CrearNuevoContacto(self, nuevocontacto):
        self.__ListaContactos = self.__ListaContactos + [nuevocontacto]

    def GuardarContacto(self):
        try:
            fichero = open(self.__Path, "w")
        except:
            print("Error: No se puede guardar contacto")
        else:
            for contacto in self.__ListaContactos:
                texto = contacto.GetNombre() + "#" + "\n"
                texto = texto + contacto.GetApellidos() + "#" + "\n"
                texto = texto + contacto.GetFechaNacimiento() + "#" + "\n"
                texto = texto + contacto.GetTelefonoFijo() + "#" + "\n"
                texto = texto + contacto.GetTelefonoMovil() + "#" + "\n"
                texto = texto + contacto.GetTelefonoTrabajo() + "#" + "\n"
                texto = texto + contacto.GetCalle() + "#" + "\n"
                texto = texto + contacto.GetPiso() + "#" + "\n"
                texto = texto + contacto.GetCiudad() + "#" + "\n"
                texto = texto + contacto.GetCodigoPostal() + "#" + "\n"
                texto = texto + contacto.GetEmail() + "\n"
                fichero.write(texto)
            fichero.close()

    def MostrarAgenda(self):
        print("######## AGENDA ########")
        print("Número de contactos:", len(self.__ListaContactos))
        for contacto in self.__ListaContactos:
            contacto.MostrarContacto()
        print("########################")

    def BuscarContactoPorNombre(self, nombre):
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() == nombre:
                listaencontrados = listaencontrados + [contacto]
        return listaencontrados

    def BuscarContactoPorTelefono(self, telefono):
        listaencontrados = []
        for contacto in self.__ListaContactos:
            if (contacto.GetTelefonoFijo() == telefono
                    or contacto.GetTelefonoMovil() == telefono
                    or contacto.GetTelefonoTrabajo() == telefono):
                listaencontrados = listaencontrados + [contacto]
        return listaencontrados

    def BorrarContactoPorNombre(self, nombre):
        listafinal = []
        for contacto in self.__ListaContactos:
            if contacto.GetNombre() != nombre:
                listafinal = listafinal + [contacto]
            print(len(self.__ListaContactos) - len(listafinal), "contactos han sido borrados")
            self.__ListaContactos = listafinal

    def BorrarContactoPorTelefono(self, telefono):
        listafinal = []
        for contacto in self.__ListaContactos:
            if (contacto.GetTelefonoFijo() == telefono
                    or contacto.GetTelefonoMovil() == telefono
                    or contacto.GetTelefonoTrabajo() == telefono):
                listafinal = listafinal + [contacto]
                print(len(self.__ListaContactos) - len(listafinal), "contactos han sido borrados")
                self.__ListaContactos = listafinal


def ObtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print("Introduce un número")
        else:
            leido = True
    return numero


def MostrarMenu():
    print("""Menu
    1)Mostrar contactos
    2)Buscar contactos
    3)Crear contacto nuevo
    4)Borrar contacto
    5)Guardar contactos
    6)Salir""")


def BuscarContactos(agenda):
    print("""Buscar contactos:
1)Nombre
2)Teléfono
3)Volver""")
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            encontrados = agenda.BuscarContactoPorNombre(input(("Introduce el nombre a buscar:")))
            if len(encontrados) > 0:
                print("**********CONTACTOS ENCONTRADOS**********")
                for item in encontrados:
                    item.MostrarContacto()
                print("*****************************************")
            else:
                print("No se han encontrado contactos")
            finbuscar = True
        elif opcbuscar == 2:
            encontrados = agenda.BuscarContactoPorTelefono(input(("Introduce el teléfono a buscar")))
            if len(encontrados > 0):
                print("**********CONTACTOS ENCONTRADOS**********")
                for item in encontrados:
                    item.MostrarContacto()
                print("*****************************************")
            else:
                print("No se han encontrado contactos")
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True


def ProcesoCrearContacto(agenda):
    nuevocontacto = Contacto()
    nuevocontacto.SetNombre((input("Introduce el nombre del contacto:")))
    nuevocontacto.SetApellidos((input("Introduce los apellidos del contacto:")))
    nuevocontacto.SetFechaNacimiento((input("Introduce la fecha de nacimiento del contacto:")))
    nuevocontacto.SetTelefonoFijo((input("Introduce el teléfono fijo del contacto:")))
    nuevocontacto.SetTelefonoMovil((input("Introduce el teléfono móvil del contacto:")))
    nuevocontacto.SetTelefonoTrabajo((input("Introduce el teléfono del trabajo del contacto:")))
    nuevocontacto.SetCalle((input("Introduce la calle de la dirección del contacto:")))
    nuevocontacto.SetPiso((input("Introduce el piso de la dirección del contacto:")))
    nuevocontacto.SetCiudad((input("Introduce la ciudad de la dirección del contacto:")))
    nuevocontacto.SetCodigoPostal((input("Introduce el código postal de la dirección contacto:")))
    nuevocontacto.SetEmail((input("Introduce el email del contacto:")))
    agenda.CrearNuevoContacto(nuevocontacto)


def BorrarContacto(agenda):
    print("""Buscar contactos a borrar por:
    1)Nombre
    2)Teléfono
    3)Volver""")
    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion("Opción:")
        if opcbuscar == 1:
            agenda.BorrarContactoPorNombre((input("Introduce el nombre a borrar:")))
            finbuscar = True
        elif opcbuscar == 2:
            agenda.BuscarContactoPorTelefono((input("Introduce el teléfono a borrar")))
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True


def Main():
    agenda = Agenda("agenda.txt")
    agenda.CargarContactos()
    fin = False
    while not fin:
        MostrarMenu()
        opc = ObtenerOpcion("Opción:")
        if (opc == 1):
            agenda.MostrarAgenda()
        elif (opc == 2):
            BuscarContactos(agenda)
        elif (opc == 3):
            ProcesoCrearContacto(agenda)
        elif (opc == 4):
            BorrarContacto(agenda)
        elif (opc == 5):
            agenda.GuardarContacto()
        elif (opc == 6):
            fin = 1

Main()
