# import pyjokes

# jokes = pyjokes.get_jokes()
# print(jokes)

# import django
# print(django.get_version())

#q2 install and import of your choice and use it

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hello ho are you")

import random

player_hp = 100
enemy_hp = 100

print("⚔️  PYTHON FIGHTING GAME  ⚔️")
print("You vs Enemy\n")

while player_hp > 0 and enemy_hp > 0:
    print(f"Your HP: {player_hp} | Enemy HP: {enemy_hp}")
    print("1. Attack")
    print("2. Heal")

    choice = input("Choose your move (1/2): ")

    if choice == "1":
        damage = random.randint(10, 25)
        enemy_hp -= damage
        print(f"💥 You hit the enemy for {damage} damage!")
    elif choice == "2":
        heal = random.randint(8, 20)
        player_hp += heal
        if player_hp > 100:
            player_hp = 100
        print(f"❤️ You healed {heal} HP!")
    else:
        print("Invalid move! You missed your turn.")

    if enemy_hp <= 0:
        break

    enemy_damage = random.randint(10, 22)
    player_hp -= enemy_damage
    print(f"☠️ Enemy attacks you for {enemy_damage} damage!\n")

if player_hp > 0:
    print("🏆 YOU WIN! The enemy is defeated.")
else:
    print("💀 YOU LOST! Better luck next time.")
