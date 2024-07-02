import aksharamukha.transliterate as akt

def get_available_scripts():
    return [
        "Devanagari", "Bengali", "Gurmukhi", "Gujarati", "Oriya", "Tamil",
        "Telugu", "Kannada", "Malayalam", "Sinhala", "Thai", "Lao", "Tibetan",
        "Myanmar"
    ]

def main():
    print("Welcome to the transliteration tool!")
    
    # Get available scripts
    scripts = get_available_scripts()
    
    # Display available scripts
    print("\nAvailable scripts for transliteration:")
    for i, script in enumerate(scripts, 1):
        print(f"{i}. {script}")
    
    # Get user's choice of script
    while True:
        try:
            choice = int(input("\nEnter the number of the script you want to transliterate to: "))
            if 1 <= choice <= len(scripts):
                chosen_script = scripts[choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get text to transliterate
    text = input("\nEnter the text you want to transliterate: ")
    
    # Perform transliteration
    try:
        transliterated = akt.process("ISO", chosen_script, text)
        print(f"\nTransliterated text ({chosen_script}):")
        print(transliterated)
    except Exception as e:
        print(f"An error occurred during transliteration: {str(e)}")

if __name__ == "__main__":
    main()