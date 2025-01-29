from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

def type_numbers(start=1, delay=1.5):
    """
    Écrit des nombres dans un champ de saisie, appuie sur Entrée, et affiche l'état dans la console.
    
    :param start: Nombre de départ
    :param delay: Délai (en secondes) entre chaque saisie
    """
    current = start
    count = 0 

    while True:
        for char in str(current):
            keyboard.type(char)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        count += 1
        print(f"Nombre envoyé : {current} | Total envoyé : {count}")

        time.sleep(delay)

        current += 1

if __name__ == "__main__":
    print("Début dans 5 secondes... Place ton curseur dans un champ de saisie !")
    time.sleep(5)
    type_numbers(0, 1.5)
