import caesar_brutforce_attack
import multiplicative_brutforce_attack
import affine_brutforce_attack
import monoAlphabetic_frequency_match
import hill_brutforce_attack

def main():
    print("=== Classical Cryptanalysis Tool ===")
    print("1. Caesar Brute Force")
    print("2. Multiplicative Brute Force")
    print("3. Affine Brute Force")
    print("4. Hill Brute Force")
    print("5. Monoalphabetic Frequency Analysis")

    choice = input("\nSelect an option (1-4): ")

    if choice == '1':
        caesar_brutforce_attack.brutforce()
    elif choice == '2':
        multiplicative_brutforce_attack.brutforce()
    elif choice == '3':
        affine_brutforce_attack.brutforce()
    elif choice == '4':
        hill_brutforce_attack.brutforce()
    elif choice =='5':
        monoAlphabetic_frequency_match.analyze()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
