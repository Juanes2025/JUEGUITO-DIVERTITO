
label start:
    
    "El hombre tras un dia largo de trabajo porfin llega a su casa."
    "El Hombre" "Porfin he llegado, tengo muchas ganas de llegar a mi casa" 
    "El Hombre" "Que raro todas las luces estan apagadas pero el carro de mi esposa sigue alli"  
    "El Hombre llega a la conclusion de que podria estar presenciando un robo por lo que tiene que decidir entre entrar por la puerta trasera o delantera"  

    #preguntar por que puerta entrar
    
    "Porque puerta el hombre deberia entrar?"
menu: 
    "entrar por la puerta delantera":
        jump puerta_delantera
    "entrar por la puerta de atras":
        jump puerta_atras

label puerta_delantera: 
    $ puerta = True
    
    "El hombre" "Al parecer no hay nadie voy a ser sigiloso"
    "El hombre" "Debo buscar una linterna"

    #preguntar a que árte de la casa

    "Deberia ir a la sala o a la cocina?"
menu:
    "ir a la sala":
        jump sala
    "Ir a la conina":
        jump cocina
        



label puerta_atras: 
    $ puerta = False

    "El hombre decide saltar por la cerca tambien rompiendo el vidrio"  

      