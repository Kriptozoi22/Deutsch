import os
import random
import msvcrt  # Для роботи з клавіатурними подіями на Windows
from colorama import init, Fore

# Ініціалізація colorama
init(autoreset=True)

def load_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    words = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 8:
            words.append(parts)
        else:
            print(f"Неправильний формат рядка: {line.strip()}")
    
    return words

def display_word(word_data):
    word, article, pos, translation, verb, verb_translation, adj, adj_translation = word_data
    
    output = (
        f"{Fore.WHITE}Слово: {article} {word} - {translation}\n"
    )
    
    if verb:
        output += f"{Fore.WHITE}Дієслова: {verb} - {verb_translation}\n"
    
    if adj:
        output += f"{Fore.WHITE}Прикметники: {adj} - {adj_translation}\n"
    
    print(output)

def main():
    file_path = 'D:\\Pyton\\V2\\words_data.txt'
    words = load_words(file_path)
    
    if not words:
        print(f"{Fore.WHITE}Не знайдено жодних правильних даних у файлі.")
        return

    random.shuffle(words)  # Перемішуємо список слів для випадковості

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Очищуємо екран
        if not words:
            print(f"{Fore.WHITE}Кінець списку слів.")
            break
        
        word_data = words.pop()  # Отримуємо нове слово
        
        if len(word_data) != 8:
            print(f"{Fore.RED}Неправильний формат даних: {word_data}")
            continue
        
        display_word(word_data)
        
        print(f"{Fore.WHITE}Натискайте Enter для перегляду наступного слова або ESC для виходу.")
        
        # Чекаємо на натискання клавіші
        key = msvcrt.getch()
        if key == b'\x1b':  # ESC
            break
        elif key == b'\r':  # Enter
            continue

if __name__ == "__main__":
    main()
