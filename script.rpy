define El hombre = Character("El Hombre", color="#00CCFF")
define Esposa = Character("Esposa", color="#FFC0CB")
define Hijo = Charanter ("Hijo", color="#8B0000")
define Ladron = Character ("Ladrones", color="#0b0246")


label start:
     

    "El hombre tras un dia largo de trabajo porfin llega a su casa."
    "El Hombre" "Porfin he llegado, tengo muchas ganas de llegar a mi casa" 
    "El Hombre" "Que raro todas las luces estan apagadas pero el carro de mi esposa sigue alli"  
    "El Hombre llega a la conclusion de que podria estar presenciando un robo por lo que tiene que decidir entre entrar por la puerta trasera o delantera"  

label "Choice N":
    "el hombre" "Por cual puerta entro?"
    
    menu: 
        "Entrar por la puerta de adelante"

        "entrar por la puerta de atras"


      
    # Estructura secuencial
    e "Alfin llego a mi casa"
    p "En una estructura secuencial, las instrucciones se ejecutan en orden, una tras otra."
    e "Como seguir pasos en una receta, ¿cierto?"
    p "¡Exacto! Mira este ejemplo:" 

    $ personaje = "Carlos"  # Asignamos un nombre a la variable
    p "Ahora nuestro personaje se llama [personaje]."

    # Estructura de selección (if-else)
    p "Ahora pasemos a la estructura de selección o condicional."
    p "Esto nos permite ejecutar código solo si se cumple una condición."

    # Preguntar la edad del jugador
    $ edad = renpy.input("¿Cuántos años tienes?")

    # Convertir la entrada a número (sin usar try-except)
    $ edad = edad.strip()  # Eliminar espacios
    if edad.isdigit():  # Verificar si la entrada es un número
        $ edad = int(edad)
    else:
        $ edad = 0  # Si no es un número, se asigna 0

    p "[nombre], tienes [edad] años."

    if edad >= 18:
        p "Como tienes 18 años o más, puedes votar."
        
        menu:
            "Votar":
                p "Has votado. ¡Felicidades por participar en la democracia!"
            "No votar":
                p "Decidiste no votar. Es tu derecho, pero es importante participar."
    else:
        p "Como tienes menos de 18 años, no puedes votar todavía."
        
        label decision_menor:
            menu:
                "Intentar votar (No disponible)":
                    p "Lo siento, pero aún no tienes la edad suficiente para votar."
                    jump decision_menor  # Vuelve a mostrar el menú
                "No votar":
                    p "Tendrás que esperar unos años más para poder votar."

    # Estructura de selección con elección del jugador
    p "Ahora probemos una estructura condicional con una elección."

    p "[nombre], ¿quieres elegir el camino de la derecha o el de la izquierda?"
    
    menu:
        "Derecha":
            $ eleccion = "derecha"
            p "Elegiste el camino de la derecha y encontraste un tesoro."
        "Izquierda":
            $ eleccion = "izquierda"
            p "Elegiste el camino de la izquierda y encontraste un obstáculo."

    # Bucle while
    p "Ahora veamos los bucles, que permiten repetir acciones hasta que una condición se cumpla."
    p "Vamos a contar del 1 al 3 usando un bucle."

    $ contador = 1
    while contador <= 3:
        p "Contando: [contador]"
        $ contador += 1  # Aumentamos el contador en 1

    p "¡Y eso es todo, [nombre]! Hemos aprendido estructuras básicas de programación en Ren'Py."

    return
