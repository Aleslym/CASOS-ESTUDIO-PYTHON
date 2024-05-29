
habitacion_dispo = 10

while habitacion_dispo > 0:
    
    print("INICIO DE RESERVACION DE HOTEL")
    
    nombre = str(input("nombre: "))
    correo = str(input("correo: "))
    telefono = int(input("telefono: "))
    
    mes_inicio = str(input("ingrese el MES de inicio del hospedaje (ejemplo: octubre): "))
    dia_inicio = int(input("ingrese el DIA de inicio del hospedaje (ejemplo: 23): "))

    if dia_inicio > 31 or dia_inicio < 1:
        dia_inicio = int(input("ese dia no existe, ingrese otro dia: "))
    
    mes_fin = str(input("ingrese el MES final del hospedaje (ejemplo: julio): "))
    dia_fin = int(input("ingrese el DIA final del hospedaje (ejemplo: 30): "))

    if dia_fin > 31 or dia_fin < 1:
        dia_fin = int(input("ese dia no existe, ingrese otro dia: "))

    if dia_fin <= dia_inicio and mes_fin == mes_inicio:
        print("la estadia debe de ser minimo de 1 DIA")
        

    habitaciones = int(input("ingrese el numero de habitaciones a reservar: "))

    if habitaciones > habitacion_dispo:
        print("lo sentimos, no hay suficientes habitaciones disponibles")
    else:
        habitacion_dispo -= habitaciones
        print(nombre, " su reservacion ha sido exitosa, al correo ",correo, " o al telefono" ,telefono, " llegara una confirmacion con la informacion de su reserva.")
    
