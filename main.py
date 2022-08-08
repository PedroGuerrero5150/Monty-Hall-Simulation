import random
import matplotlib.pyplot as plt

#he comentado lineas con print() que hacen mas interactiva la simulacion, pero incrementan el tiempo de ejecucion


numero_puertas = 3

def puerta_premiada():
    index_puerta_premiada = random.randint(1, numero_puertas)
    #print('Puerta premiada', index_puerta_premiada)
    return index_puerta_premiada

def eleccion_concursante():
    index_puerta_escogida = random.randint(1, numero_puertas)
    #print('Concursante escoge la puerta', index_puerta_escogida)
    return index_puerta_escogida


def presentador_abre_puerta(index_puerta_premiada, primera_eleccion_concursante):
    #simular puertas: [1, 2, 3]
    puertas = [1]
    for i in range(0, numero_puertas):
        puertas.append(puertas[i] + 1)

    #presentador sabe que puerta es la premiada y que eligio el concursante
    #por lo que la puerta que va a abrir no puede ser ninguna de ellas
    if index_puerta_premiada == primera_eleccion_concursante:
        puertas.remove(index_puerta_premiada)
        puerta_a_abrir = puertas[random.randint(0, 1)]
    else:
        puertas.remove(index_puerta_premiada)
        puertas.remove(primera_eleccion_concursante)
        puerta_a_abrir = puertas[0]

    puertas_restantes = [1, 2, 3]
    puertas_restantes.remove(puerta_a_abrir)

    #print('Presentador abre la puerta', puerta_a_abrir, ", Puertas restantes", puertas_restantes)
    return puertas_restantes

def concursante_cambia_de_puerta(puertas_restantes, primera_eleccion_concursante):
    #de las puertas restantes, si concursante decide cambiar de puerta solo hay una eleccion
    puertas_restantes.remove(primera_eleccion_concursante)
    eleccion_final = puertas_restantes[0]
    #print('Concursante cambia eleccion a', eleccion_final)
    return eleccion_final



#funcion simple para visualizar tendencias
def plot_results(y_values, x_values, titulo, y_recta):
    y = y_values
    x = x_values
    plt.plot(x, y)
    plt.axhline(y=y_recta, color='r', linestyle='-')

    plt.ylabel('Porcentaje Vicorias')
    plt.xlabel('n_sumulaciones')
    plt.title(titulo, fontsize=16)
    plt.show()

#simular situacion para todos los n_simulaciones dentro de n_range)
def simular(n_range):

    porcentajes_victorias_cambio = []
    porcentajes_victorias_sin_cambio = []

    for n_simulaciones in n_range:
        contador_victoria_cambio_puerta = 0
        for i in range(0, n_simulaciones):
            #print('-------------------')
            index_puerta_premiada = puerta_premiada()
            primera_eleccion_concursante = eleccion_concursante()
            puertas_restantes = presentador_abre_puerta(index_puerta_premiada, primera_eleccion_concursante)
            eleccion_final = concursante_cambia_de_puerta(puertas_restantes, primera_eleccion_concursante)

            #gana
            if index_puerta_premiada == eleccion_final:
                #print('Gano!: ', index_puerta_premiada, '=', eleccion_final)
                contador_victoria_cambio_puerta += 1
            #else:
                #print('Perdio!:', index_puerta_premiada, '!=', eleccion_final)
                #print('-------------------')

        contador_victorias_sin_cambio = 0
        for i in range(0, n_simulaciones):
            #print('-------------------')
            index_puerta_premiada = puerta_premiada()
            primera_eleccion_concursante = eleccion_concursante()
            puertas_restantes = presentador_abre_puerta(index_puerta_premiada, primera_eleccion_concursante)
            eleccion_final = primera_eleccion_concursante
            #print('Concursante no cambia de eleccion: ', eleccion_final)

            # gana
            if index_puerta_premiada == eleccion_final:
                # print('Gano!: ', index_puerta_premiada, '=', eleccion_final)
                contador_victorias_sin_cambio += 1
            #else:
                #print('Perdio!:', index_puerta_premiada, '!=', eleccion_final)
                #print('-------------------')

        porcentajes_victorias_cambio.append(contador_victoria_cambio_puerta/ n_simulaciones)
        porcentajes_victorias_sin_cambio.append(contador_victorias_sin_cambio / n_simulaciones)

    print('Media de porcentajes ganar cambiando de puerta (caso 1):', sum(porcentajes_victorias_cambio)/len(porcentajes_victorias_cambio))
    print('Media de porcentajes ganar sin cambio de puerta (caso 1):', sum(porcentajes_victorias_sin_cambio)/len(porcentajes_victorias_sin_cambio))
    return porcentajes_victorias_cambio, porcentajes_victorias_sin_cambio


#----------------------------CASO 2------------------------------------

numero_puertas_caso2 = 4

def puerta_premiada_caso2():
    index_puerta_premiada = random.randint(1, numero_puertas_caso2)
    #print('Puerta premiada', index_puerta_premiada)
    return index_puerta_premiada

def eleccion_concursante_caso2():
    index_puerta_escogida = random.randint(1, numero_puertas_caso2)
    #print('Concursante escoge la puerta', index_puerta_escogida)
    return index_puerta_escogida

def presentador_abre_puerta_caso2(index_puerta_premiada, primera_eleccion_concursante):
    # simular set de puertas: [1, 2, 3, 4]
    puertas = [1]
    for i in range(0, numero_puertas_caso2):
        puertas.append(puertas[i] + 1)

    # presentador no puede escoger la misma puerta que el concursante
    puertas.remove(primera_eleccion_concursante)
    puerta_a_abrir = puertas[random.randint(0, numero_puertas_caso2 - 2)]

    # si presentador abre puerta ganadora
    if puerta_a_abrir == index_puerta_premiada:
        #print('Presentador abre la puerta premiada', puerta_a_abrir)
        return 'Pierde'

    # si no abre puerta ganadora
    else:
        puertas_restantes = [1]
        for i in range(0, numero_puertas):
            puertas_restantes.append(puertas_restantes[i] + 1)

        puertas_restantes.remove(puerta_a_abrir)
        #print('Presentador abre la puerta', puerta_a_abrir, ", Puertas restantes", puertas_restantes)
        return puertas_restantes


def concursante_cambia_de_puerta_caso2(puertas_restantes, primera_eleccion_concursante):
    #eleccion de concursante cambia, pero sigue siendo aleatoria dentro de las puertas que quedan
    puertas_restantes.remove(primera_eleccion_concursante)
    eleccion_final = puertas_restantes[random.randint(0, numero_puertas - 3)]
    #print('Concursante cambia eleccion a', eleccion_final)
    return eleccion_final


def simular_caso2(n_range):
    porcentajes_victorias_cambio = []
    porcentajes_victorias_sin_cambio = []

    for n_simulaciones in n_range:

        # concursante cambia de puerta
        contador_victorias_cambio_puerta = 0
        for i in range(0, n_simulaciones):
            #print('-------------------')
            index_puerta_premiada = puerta_premiada_caso2()
            primera_eleccion_concursante = eleccion_concursante_caso2()
            puertas_restantes = presentador_abre_puerta_caso2(index_puerta_premiada, primera_eleccion_concursante)

            #si puerta abierta por presentador no tiene el premio
            if puertas_restantes != 'Pierde':
                eleccion_final = concursante_cambia_de_puerta_caso2(puertas_restantes, primera_eleccion_concursante)

                if index_puerta_premiada == eleccion_final:
                    #print('Gano!: ', index_puerta_premiada, '=', eleccion_final)
                    contador_victorias_cambio_puerta += 1
                #else:
                    #print('Perdio!:', index_puerta_premiada, '!=', eleccion_final)
                    #print('-------------------')

        #concursante no cambia de puerta
        contador_victorias_no_cambia = 0
        for i in range(0, n_simulaciones):
            #print('-------------------')
            index_puerta_premiada = puerta_premiada_caso2()
            primera_eleccion_concursante = eleccion_concursante_caso2()
            puertas_restantes = presentador_abre_puerta_caso2(index_puerta_premiada, primera_eleccion_concursante)

            # si puerta abierta por presentador no tiene el premio
            if puertas_restantes != 'Pierde':
                eleccion_final = primera_eleccion_concursante
                #print('Concursante no cambia de eleccion: ', eleccion_final)
                if index_puerta_premiada == eleccion_final:
                    #print('Gano!: ', index_puerta_premiada, '=', eleccion_final)
                    contador_victorias_no_cambia += 1
                #else:
                    #print('Perdio!:', index_puerta_premiada, '!=', eleccion_final)
                    #print('-------------------')

        porcentajes_victorias_cambio.append(contador_victorias_cambio_puerta / n_simulaciones)
        porcentajes_victorias_sin_cambio.append(contador_victorias_no_cambia / n_simulaciones)

    print('Media de porcentajes ganar cambiando de puerta (caso 2):', sum(porcentajes_victorias_cambio)/len(porcentajes_victorias_cambio))
    print('Media de porcentajes ganar sin cambiar de puerta (caso 2):', sum(porcentajes_victorias_sin_cambio)/len(porcentajes_victorias_sin_cambio))
    return porcentajes_victorias_cambio, porcentajes_victorias_sin_cambio




if __name__ == '__main__':
    #settear simluaciones
    n_range = [1000]
    for i in range(0, 150):
        steps = 1000
        n_range.append(n_range[i] + steps)

    #descomentar esta linea y comentar las secciones de graficar resultados para probar el algo. con solo 100000 sims.
    #n_range = [100000]

    #simulacion caso 1
    porcentajes_victorias_cambio,porcentajes_victorias_sin_cambio = simular(n_range)

    #graficar resultados
    plot_results(porcentajes_victorias_cambio, n_range, 'Cuando cambia de puerta (Caso 1)', 0.666)
    plot_results(porcentajes_victorias_sin_cambio, n_range, 'Cuando no cambia de puerta (Caso 1)', 0.333)

    #simulacion caso 2
    porcentajes_victorias_cambio, porcentajes_victorias_sin_cambio = simular_caso2(n_range)

    # graficar resultados
    plot_results(porcentajes_victorias_cambio, n_range, 'Cuando cambia de puerta (Caso 2)', 0.25)
    plot_results(porcentajes_victorias_sin_cambio, n_range, 'Cuando no cambia puerta (Caso 2)', 0.25)







