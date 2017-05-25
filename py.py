from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from py2neo import Graph
 
db = GraphDatabase("http://localhost:7474", username="neo4j", password="5674899m")

x = 0
while x==0:
    print "1. Ingrese Doctores"
    print "2. Ingrese pacientes."
    print "3. Ingrese un paciente que visito a un doctor"
    print "4. Consulta de doctores con especialidades"
    print "5. Ingreso de relaciones entre paciente"
    print "6. Salir"
    
    opcion = input()
    doctor  = db.labels.create("Doctor")
    pacien  = db.labels.create("Paciente")
    
    if opcion == 1:
        doctor = raw_input("Ingrese el nombre del Doctor: ")
        espe = raw_input("Ingrese si tiene una especialidad (si/no): ")
        numero = raw_input("Ingrese el numero telefonico del doctor: ")

        user = db.labels.create("Doctor")
        u1 = db.nodes.create(Nombre= doctor, Especialidad = espe, Numero = numero)
        user.add(u1)


    if opcion == 2:
        paciente = raw_input("Ingrese el nombre del Paciente: ")
        numero = raw_input("Ingrese el numero telefonico del paciente: ")

      
        user = db.labels.create("Paciente")
        u1 = db.nodes.create(Nombre= paciente, Numero = numero)
        user.add(u1)


  
    if opcion == 3:
        doc = raw_input("Ingrese el nombre del doctor: ")
        paci = raw_input("Ingrese el nombre del paciente: ")
        
        q = 'MATCH (u:Doctor) WHERE u.Nombre="'+doc+'" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))

        e = 'MATCH (u:Paciente) WHERE u.Nombre="'+paci+'" RETURN u'
        results = db.query(e, returns=(client.Node, str, client.Node))
        for r in results:
            print("(%s)" % (r[0]["Nombre"]))
        print e

  


                  
    if opcion == 4:
        q = 'MATCH (u:Doctor) WHERE u.Especialidad="si" RETURN u'
        results = db.query(q, returns=(client.Node, str, client.Node))
        for r in results:
            print "El nombre del especialista: "
            print("(%s)" % (r[0]["Nombre"]))

    
        
    if opcion ==6:  
        x=10

