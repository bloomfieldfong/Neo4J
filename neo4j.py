from py2neo import Node


x = 0

while x<3:
    print "1. Ingrese Doctores"
    print "2. Ingrese pacientes."
    print "3. Ingrese un paciente que visito a un doctor"
    print "4. Consulta de doctores con especialidades"
    print "5. Ingreso de relaciones"
    print "6. Salir"

    opcion = input()

    if opcion == 1:
        doctor = raw_input("Ingrese el nombre del Doctor: ")
        espe = raw_input("Ingrese si tiene una especialidad (si/no): ")
        numero = raw_input("Ingrese el numero telefonico del doctor: ")

        doctorneo4j = Node("Person", nombre = doctor, especialidad = espe, telefono = numero) 

    if opcion == 2:
        paciente = raw_input("Ingrese el nombre del Paciente: ")
        numero = raw_input("Ingrese el numero telefonico del paciente: ")

        pacienteneo4j = Node("Person", nomnre = paciente, telefono = numero)

    if opcion == 6:
        x = 10
        
