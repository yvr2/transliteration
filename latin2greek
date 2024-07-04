# Dictionary for Library of Congress transliteration scheme
transliteration_map = {
    'a': 'α', 'b': 'β', 'g': 'γ', 'd': 'δ', 'e': 'ε', 'z': 'ζ', 'h': 'η', 'th': 'θ',
    'i': 'ι', 'k': 'κ', 'l': 'λ', 'm': 'μ', 'n': 'ν', 'ks': 'ξ', 'o': 'ο', 'p': 'π',
    'r': 'ρ', 's': 'σ', 't': 'τ', 'y': 'υ', 'f': 'φ', 'ch': 'χ', 'ps': 'ψ', 'w': 'ω',
    'ai': 'αι', 'ei': 'ει', 'oi': 'οι', 'ou': 'ου', 'yi': 'υι', 'v': 'β'
}

# Special combinations for more accurate transliteration
special_combinations = {
    'th': 'θ', 'ch': 'χ', 'ps': 'ψ', 'ks': 'ξ', 'ou': 'ου', 'ei': 'ει', 'oi': 'οι', 'ai': 'αι', 'yi': 'υι'
}

def transliterate(text):
    text = text.lower()
    result = ''
    i = 0

    while i < len(text):
        if text[i:i+2] in special_combinations:
            result += special_combinations[text[i:i+2]]
            i += 2
        elif text[i] in transliteration_map:
            result += transliteration_map[text[i]]
            i += 1
        else:
            result += text[i]
            i += 1

    return result

# Ask user for input
latin_script = input("Please enter the text to be transliterated: ")
greek_script = transliterate(latin_script)
print(f'Latin script: {latin_script}')
print(f'Greek script: {greek_script}')
