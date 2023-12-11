# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

# El juego comienza aquí.

transform up:
    yalign 1
    
label start:

    play music "audio/forest.ogg" fadein 1.0
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    
# maybe una scene en negro
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    # Presenta las líneas del diálogo.

    "Soy un historiador de el año 3023"
    show terra at up with dissolve 
    "Después de años de ardua preparación, por fin he asegurado el permiso de los venerables Señores para adentrarme en las olvidadas ruinas del noroeste de eorþe."
    "Nadie ha estado ahí en siglos..."
    # Mostrar imagen de la tierra desde lejos
    "Se cuenta que una gran civilizacion alguna vez habito eorþe."
    "Todo fue destruido así que no sabemos mucho sobre ellos exactamente."
    "Sabiamos que solian hablar alguna Lingua Vetus. asi que los llamamos los Obliviscens."
    hide terra with dissolve
    show cher with dissolve:
        xzoom 1.5 yzoom 1.5 
    "Los huesos, los susurros de la arquitectura... todos narran la epopeya de un tiempo olvidado."
    
    "La civilización de los Obliviscens, regida por la fe en su dios, 'Internet'"
    "Clamaban que era el poosedor de todo conocimiento y entendimiento"
    "Solo las referencias a 'eso' sobrevivieron, lo que sea que fuera murio con ellos"
    stop music fadeout 0.5
    "..."
    "Por algun motivo dejaron de escribir registros en sus ultimos años de existencia"
    "Lo unico que conocemos sobre ellos son escombros de arquitectura y fragmentos de escritos antes de la religion 'Internet'"
    "Finos restos de una antigua iglesia se pueden ver, debido a los majestuosos arcos dorados. Restos caídos, pero aún en su mayor parte intactos"
    "Dentro de estos, esqueletos momificados notablemente conservados, sentados en las mesas, con las cabezas inclinadas con reverencia"
    "Cada uno de ellos"
    "Cada uno de ellos... acurrucados sobre tabletas quemadas de plástico y vidrio"
    "Todavía no conocemos completamente su significado"
    "Algunos de ellos, tomando los pequeños ladrillos contra sus pechos en sus últimos respiros"
    "Eso solo demuestra lo devota que era su gente..."
    "Cerca de los altares. algun tipo de vidrio solia preservar algun tipo de escrituras sagradas."
    "Los huesos del acólito se deslizan detrás del altar donde murieron, oficializando su fe"
    # Finaliza el juego:
    "Gracias a https://inv.vern.cc/watch?v=TTcJtW45fIw por la historia lol. fue bastante entretendio re escribirla"
    return
