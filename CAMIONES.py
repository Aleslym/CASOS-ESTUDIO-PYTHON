for camion in range(1, 21):
    capacidad = 0
    carga = 0

    
    while capacidad < 18000 or capacidad > 28000:
        capacidad = int(input(f"ingrese la capacidad del camion {camion} (min 18000 - max 28000): "))
        if capacidad < 18000 or capacidad > 28000:
            print("dato no valido, intente de nuevo ")

    saca = 0

    
    while carga < capacidad:
        saca += 1
        peso_saco = 0

        
        while peso_saco < 3000 or peso_saco > 9000:
            peso_saco = int(input(f"ingrese el peso del saco {saca} (min 3000 - max 9000): "))
            if peso_saco < 3000 or peso_saco > 9000:
                print("dato no valido, intente de nuevo ")

        if carga + peso_saco > capacidad:
            print(f"no siga cargando, la carga total con este saco ({carga + peso_saco} kg) excede la capacidad del camion)")
            break

        carga += peso_saco
        restante = capacidad - carga

        print(f"el camion {camion} tiene capacidad para {restante} kg más")

    print(f"despache el camion numero {camion}")
    
print("fin del día laboral")
