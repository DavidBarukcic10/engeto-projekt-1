'''
projekt_1.py: první projekt do Engeto Online Python Akademie

author: David Barukčić
email: d.barukcic@seznam.cz
discord: David Barukcic
'''

from task_template import TEXTS


registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}


# Získání přihlašovacích údajů od uživatele
username = input("Zadejte přihlašovací jméno: ")
password = input("Zadejte heslo: ")
print("-" * 40)

# Ověření přihlašovacích údajů
if username in registered_users and password == registered_users[username]:
    print("Vítejte, " + username + "!")
    print("Můžete pokračovat v analýze textů.")
    print("-" * 40)

    # Výběr textu k analýze
    text_choice = input("Vyberte číslo textu k analýze (1-" + str(len(TEXTS)) + "): ")
    print("-" * 40)

    # Kontrola správnosti vstupu a analýza textu
    if text_choice.isdigit():
        text_choice = int(text_choice)
        if 1 <= text_choice <= len(TEXTS):
            selected_text = TEXTS[text_choice - 1]
            words = selected_text.split()
            word_count = len(words)
            title_count = sum(1 for word in words if word.istitle())
            upper_count = sum(1 for word in words if word.isupper())
            lower_count = sum(1 for word in words if word.islower())
            digit_count = sum(1 for word in words if word.isdigit())
            number_sum = sum(int(word) for word in words if word.isdigit())

            print("Počet slov: ", word_count)
            print("Počet slov začínajících velkým písmenem: ", title_count)
            print("Počet slov psaných velkými písmeny: ", upper_count)
            print("Počet slov psaných malými písmeny: ", lower_count)
            print("Počet čísel: ", digit_count)
            print("Součet všech čísel: ", number_sum)

            # Výpočet četností délek slov
            word_lengths = [len(word) for word in words]
            word_length_counts = {}
            for length in word_lengths:
                if length not in word_length_counts:
                    word_length_counts[length] = 1
                else:
                    word_length_counts[length] += 1

            # Výpis četností délek slov
            print("-" * 40)
            print("LEN|  OCCURENCES  |NR.")
            print("-" * 40)
            for length, count in sorted(word_length_counts.items()):
                print(f"{length:3}|{'*' * count:14}|{count:2}")
        else:
            print("Neplatný výběr textu.")
    else:
        print("Neplatný vstup.")
else:
    print("Neregistrovaný uživatel. Program bude ukončen.")