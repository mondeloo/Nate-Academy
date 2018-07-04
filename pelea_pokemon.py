class Pokemon:
    def __init__(self,dano,vida):
        self.dano = dano
        self.vida = vida

bulbasaur = Pokemon(10,100) #2
charmander = Pokemon(7, 80)#3
squirtle = Pokemon(8,90)#1
pikachu = Pokemon(0,100)
vida_pikachu = pikachu.vida
while True:
    pokemon_a_combatir = input("Contra que pokemon desea combatir? (Squirtle/Bulbasaur/Charmander)\n")
    if pokemon_a_combatir.lower() == "squirtle":
        print("Has elegido a squirtle: Vida = 90, Daño:8")
        vida_oponente = 90
        dano_oponente = 8
        break
    elif pokemon_a_combatir.lower() == "bulbasaur":
        print("Has elegido a bulbasaur: Vida = 100, Daño:10")
        vida_oponente = 100
        dano_oponente = 10
        break
    elif pokemon_a_combatir.lower() == "charmander":
        print("Has elegido a charmander: Vida = 80, Daño:7")
        vida_oponente = 80
        dano_oponente = 7
        break
    else:
        print("No has escogido entre las opciones dadas")

while vida_oponente > 0 and vida_pikachu > 0:
    while True:
        ataque_pikachu = input("Que ataque quieres usar: Chispazo(10) o Bola Voltio (12)\n")
        if ataque_pikachu.lower() == "chispazo":
            vida_oponente -= 10
            break
        elif ataque_pikachu.lower() == "bola voltio":
            vida_oponente -= 12
            break
        else:
            print("No has escogido uno de los ataques que conoce")
    print("El rival ha sido dañado, su vida restante es {}\n".format(vida_oponente))
    vida_pikachu -= dano_oponente
    print("Tu pikachu a recibido daño¡ Su vida restante es: {}\n".format(vida_pikachu))

if vida_oponente <=0 and vida_pikachu > 0:
    print("Has ganado el combate¡¡")
elif vida_pikachu <=0 and vida_oponente >0:
    print("Has perdido el combate¡¡")
else:
    print("Has ganado el combate¡¡")