import hashlib
import random
import sys
import secrets
import re

def generate_random_key():
    return secrets.token_bytes(32).hex()

def print_table(table):
    for row in table:
        print(" | ".join(row))
    print()

com = ['exit', 'Rock', 'Spock', 'Paper', 'lizard', 'scissors', 'help']

if len(sys.argv) != 2:
    print("Usage: python task3.py <user_move>")
    sys.exit(1)

p = sys.argv[1]

if p == '?':
    print("Help:")
    table = [["v PC\\User >", "Rock", "Paper", "3rd move", "4th", "5th", "6th", "7th"],
             ["Rock", "Draw", "Win", "Win", "Win", "Lose", "Lose", "Lose"],
             ["Paper", "Lose", "Draw", "Win", "Win", "Win", "Lose", "Lose"],
             ["3rd move", "Lose", "Lose", "Draw", "Win", "Win", "Win", "Lose"],
             ["4th", "Lose", "Lose", "Lose", "Draw", "Win", "Win", "Win"],
             ["5th", "Win", "Lose", "Lose", "Lose", "Draw", "Win", "Win"],
             ["6th", "Win", "Win", "Lose", "Lose", "Lose", "Draw", "Win"],
             ["7th", "Win", "Win", "Win", "Lose", "Lose", "Lose", "Draw"]]
    print_table(table)
    sys.exit(0)

# Используем регулярное выражение для извлечения цифр из входной строки
matches = re.findall(r'\d+', p)
if not matches:
    print("Invalid input. Please enter a valid number.")
    sys.exit(1)

user_move = int(matches[0])
if user_move < 1 or user_move > 5:
    print("Invalid input. Please enter a valid number.")
    sys.exit(1)

key = generate_random_key()
print("HMAC:", key)

com = ['exit', 'Rock', 'Spock', 'Paper', 'lizard', 'scissors', 'help']

print("Your move:", com[user_move])

computer_move = random.randint(1, 5)
print("Computer move:", com[computer_move])

if user_move == computer_move:
    print("Draw")
elif (user_move == 1 and (computer_move == 5 or computer_move == 4)) or \
    (user_move == 5 and (computer_move == 3 or computer_move == 4)) or \
    (user_move == 3 and (computer_move == 1 or computer_move == 2)) or \
    (user_move == 4 and (computer_move == 2 or computer_move == 3)) or \
    (user_move == 2 and (computer_move == 1 or computer_move == 5)):
    print("You Win!")
else:
    print("You lose")

hmac = hashlib.sha3_256((key + str(computer_move)).encode()).hexdigest()
print("HMAC:", hmac)

