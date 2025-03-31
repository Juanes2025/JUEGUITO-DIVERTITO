
label start:
    
    "El hombre tras un dia largo de trabajo porfin llega a su casa."
    "El Hombre" "Porfin he llegado, tengo muchas ganas de llegar a mi casa" 
    "El Hombre" "Que raro todas las luces estan apagadas pero el carro de mi esposa sigue alli"  
    "El Hombre llega a la conclusion de que podria estar presenciando un robo por lo que tiene que decidir entre entrar por la puerta trasera o delantera"  

    #preguntar por que puerta entrar
    
    "Por cual puerta el hombre deberia entrar?"
menu: 
    "entrar por la puerta delantera":
        jump puerta_delantera
    "entrar por la puerta de atras":
        jump puerta_atras

label puerta_delantera: 
    $ puerta = True
    
    "El hombre" "Al parecer no hay nadie voy a ser sigiloso"
    "El hombre" "Debo buscar una linterna"

    #preguntar a que parte de la casa

    "Deberia ir a la sala o a la cocina?"
menu:
    "ir a la sala":
        jump sala
    "Ir a la cocina":
        jump cocina
        
label cocina:
    "El hombre se dirige a la cocina con total sigilo y logra ver la linterna encima del comedor y escucha un ruido que proviene del sotano"
    "El hombre" "Sopas! deberia seguir el ruido o ir al estudio por algo que me pueda servir para defenderme"



    #preguntar a donde ir



menu:
    "ir al sotano":
        jump sotano
    "ir al estudio":
        jump estudio    

label sotano:
    "El Hombre se sorprende al ver que el ruido provenia de los tacos de la luz que al parecer tenian un corto. Intenta arreglar pero sin exito tiene que decidir si ir a buscar a su esposa o a su hijo"
    
    #preguntar a por quien ir

menu:
    "Ir a donde la esposa":
        jump cuarto_esposa
    "ir a donde su hijo":
        jump cuarto_hijo


label estudio:
    "El hombre" "He encontrado un esfero, me servira para defenderme"
    "ahora el hombre tiene que elegir entre ir al cuarto de su hijo o al de su esposa"
   


    #preguntar a que cuarto ir


menu:
    "Ir a donde la esposa":
        jump cuarto_esposa
    "ir a donde su hijo":
        jump cuarto_hijo

label sala:
    "El hombre encuentra todo a su alrededor roto y desordenado y necesita una linterna para mas claridad pero no la encuentra en la sala"
    "El hombre escucha un ruido que viene del sotano"
    "el hombre" "Demonios que fue ese ruido. Lo sigo o busco la linterna en el estudio?"
menu:
    "ir al sotano.":
        jump sotano_alteno
    "Ir al estudio":
        jump estudio2       


label sotano_alterno:
    "EL hombre muy asustado baja al sotano sin visibilidad solo escuchando un chipeo..."
    "Esto talvez ya no sea solo un robo. Mi familia corre peligro!. Que hago?"

menu: 
    "Huir":
        jump final1
    "ir al cuarto de su hijo":
        jump cuarto_hijo     

label estudio2:
    "El hombre muy asustado no logra encontrar nada que lo ayude asi que se llena de valor para subir las esacaleras y tiene que decidir"
    "El hombre" "Voy al cuarto de mi esposa o de mi hijo?"
              
menu:
    "Ir al cuarto de la esposa":
        jump cuarto_esposa
    "Ir al cuarto del hijo":
        jump cuarto_hijo    

label final1:
    "Cuando el hombre intenta huir es golpeado por un rayo de luz que lo deja inconciente"
    "El hombre" "donde estoy?"
    "EL hombre" "Porque estoy atado a una camilla?"
    "Un doctor entra al cuarto"  




    

label puerta_atras:
    $ puerta = False


    "El hombre decide saltar por la cerca tambien rompiendo el vidrio"
    "El hombre ve la linterna encima del comedor de la sala"  
    "El hombre" "Aqui esta la linterna"
    "El hombre escucha un ruido en la sala"
   
    #preguntar si seguir el ruido o ir al sotano


    "Deberia seguir ese ruido o ir al sotano?"


menu:
    "seguir el ruido en la sala":
        jump sala
    "Ir al sotano":
        jump sotano




label sala:
    "El hombre" "Que es este liquido negro que hay en el piso?"
    "El hombre asustado escucha un ruido en el sotano y este indeciso no sabe si ir a donde el ruido o ir al cuarto de su espoasa"
   
    #preguntar a donde ir




menu:
    "ir al sotano":
        jump sotano
    "ir al cuarto de su esposa":
        jump cuarto_esposa




label sotano:
    "El hombre se llena de valor y con su linterna logra ver los interruptores de luz"
    "El hombre" "Oh no, los interruptores estan dañados"
    "EL hombre llega a la conclusion de que efectivamente esta siendo robado asi que tiene que decidir si ir al cuarto de su esposa o al de su hijo"


    #preguntar a que cuarto ir


return




label cocina:
    "El hombre se dirige a la cocina con total sigilo y logra ver la linterna encima del comedor y escucha un ruido que proviene del sotano"
    "El hombre" "Sopas! deberia seguir el ruido o ir al estudio por algo que me pueda servir para defenderme"




    #preguntar a donde ir


menu:
    "ir al sotano":
        jump sotano
    "ir al estudio":
        jump estudio    




label estudio:
    "El hombre" "He encontrado un esfero, me servira para defenderme"
    "ahora el hombre tiene que elegir entre ir al cuarto de su hijo o al de su esposa"
   


    #preguntar a que cuarto ir     
  
 






   

    