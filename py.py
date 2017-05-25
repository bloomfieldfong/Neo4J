######################################
## Estructura de Datos              ##
## Seccion:  10                     ##
## Authores:                        ##
##      Rodrigo Juarez      16073   ##
##      Rodrigo Alvarado    16106   ##
##      Carlos Arroyave     16774   ##
##      Michelle Bloomfield 16803   ##
######################################


from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from py2neo import Graph'

##Ingreso a la base de datos con mi username y mi contraseña
db = GraphDatabase("http://localhost:7474", username="neo4j", password="5674899m")

x = 0
    ##Ciclo para el menu
while x==0:
    print "1. Ingrese Doctores"
    print "2. Ingrese pacientes."
    print "3. Ingrese un paciente que visito a un doctor"
    print "4. Consulta de doctores con especialidades"
    print "5. Ingreso de relaciones entre paciente"
    print "6. Salir"
    
    opcion = input()
    ##Ingreso de doctores
    if opcion == 1:
        doctor = raw_input("Ingrese el nombre del Doctor: ")
        numero = raw_input("Ingrese el numero telefonico del doctor: ")
        especi = raw_input("Ingrese si tiene una especialidad (si/no): ")

        if especi == "si":
            espe = raw_input("Ingrese el nombre de la especialidad")
            user = db.labels.create("Doctor")
            u1 = db.nodes.create(Nombre= doctor, Especialidad = espe, Numero = numero)
            user.add(u1)
        else
            
            user = db.labels.create("Doctor")
            u1 = db.nodes.create(Nombre= doctor, Numero = numero)
            user.add(u1)
            
    

        

    ##Ingreso de pacientes
    if opcion == 2:
        paciente = raw_input("Ingrese el nombre del Paciente: ")
        numero = raw_input("Ingrese el numero telefonico del paciente: ")

      
        user = db.labels.create("Paciente")
        u1 = db.nodes.create(Nombre= paciente, Numero = numero)
        user.add(u1)

    ##Ingreso de relaciones entre un doctor y un paciente
    if opcion == 3:
        doc = raw_input("Ingrese el nombre del doctor: ")
        paci = raw_input("Ingrese el nombre del paciente: ")
        medi = raw_input("Indique que medicina se le medico: ")

        ##Se ingresa medicina al grafo
        user = db.labels.create("Medicina")
        u1 = db.nodes.create(Nombre= medi)
        user.add(u1)
        
        ##Busca el doctor               
        q = 'MATCH (u:Doctor) WHERE u.Nombre="'+doc+'" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))
        u1=r[0]

        ##Busca el paciente
        q = 'MATCH (u:Paciente) WHERE u.Nombre="'+paci+'" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))
        u2= r[0]
        
        ##Relaciona el doctor con el paciente
        ##Relaciona el paciente con el doctor
        u2.relationships.create("atendio",u1)
        u2.relationships.create("fue con",u2)

        ##Busca la medicina ingresada
        q = 'MATCH (u:Medicina) WHERE u.Nombre="'+medi+'" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))
        u3=r[0]

        ##Ralciona la medicina con el paciente y el medico
        u3.relationships.create("medico",u1)
        u3.relationships.create("tomo",u2)

    ##Nos imprime los doctores que tiene especialidad    
    if opcion == 4:
        q = 'MATCH (u:Doctor) WHERE u.Especialidad="si" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print "El nombre del especialista: "
            print("(%s)" % (r[0]["Nombre"]))

    ##Nos hace relaciones entre pacientes
    if opcion ==5:
        doc = raw_input("Ingrese el nombre del paciente: ")
        paci = raw_input("Ingrese el nombre del paciente: ")

        ##Busca los pacientes 
        q = 'MATCH (u:Paciente) WHERE u.Nombre="'+doc+'" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))
        u1=r[0]
        q = 'MATCH (u:Paciente) WHERE u.Nombre="'+paci+'" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))
        u2= r[0]

        ##Relaciones entre paciente
        u2.relationships.create("conoce",u1)
        u1.relationships.create("conoce",u2)

    ##Sale del sistema
    if opcion ==6:  
        x=10

