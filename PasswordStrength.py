import re

def check_strength(password):
    score = 0
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[@$!%*?&]', password):
        score += 1
    
    strength = {
        1: "Very Weak 😭",
        2: "Weak 😕",
        3: "Medium 🙂",
        4: "Strong 💪",
        5: "Very Strong 🚀"
    }
    return strength.get(score, "Uhh… is that even a password? 😶")

password = input("Enter your password: ")
print("Strength:", check_strength(password))
