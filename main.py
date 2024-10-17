from utils import (
    fahrenheit_to_celsius, celsius_to_fahrenheit,
    kelvin_to_celsius, celsius_to_kelvin
)

def get_temperature_input() -> float:
    """
    Demande à l'utilisateur d'entrer une température.

    Returns:
        La température sous forme de nombre flottant.
    """
    while True:
        try:
            return float(input("Entrez une température : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def select_conversion() -> int:
    """
    Affiche un menu des options de conversion et retourne le choix de l'utilisateur.

    Returns:
        Un entier représentant l'option de conversion choisie.
    """
    print("Sélectionnez le type de conversion :")
    print("1. Fahrenheit vers Celsius")
    print("2. Celsius vers Fahrenheit")
    print("3. Kelvin vers Celsius")
    print("4. Celsius vers Kelvin")
    
    while True:
        try:
            choice = int(input("Entrez votre choix (1-4) : "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def main() -> None:
    """
    Fonction principale qui exécute le programme de conversion de température.

    Cette fonction demande à l'utilisateur une température, sélectionne
    le type de conversion et affiche le résultat.

    Args:
        None
    """
    # 1. Demander à l'utilisateur la température à convertir
    temperature = get_temperature_input()

    # 2. Afficher le menu des conversions et obtenir le choix de l'utilisateur
    choice = select_conversion()

    # 3. Effectuer la conversion en fonction du choix de l'utilisateur
    if choice == 1:
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit équivaut à {result} Celsius.")
    elif choice == 2:
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius équivaut à {result} Fahrenheit.")
    elif choice == 3:
        result = kelvin_to_celsius(temperature)
        print(f"{temperature} Kelvin équivaut à {result} Celsius.")
    elif choice == 4:
        result = celsius_to_kelvin(temperature)
        print(f"{temperature} Celsius équivaut à {result} Kelvin.")
    else:
        print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
