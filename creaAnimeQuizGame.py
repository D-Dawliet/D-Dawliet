#Dictionary
quiz = {
    "Who's the MC in 'Naruto'?:" : "B",
    "Goku's signature attack?:" : "A",
    "Who's the girl in Spirited Away?:" : "A",
    "Electric Pokémon with red cheeks?:" : "D",
    "Name of the smart kid in Death Note?:" : "C",
    "Real name of Sailor Moon?:" : "D",
    "Real name of L-Lawliet?:" : "B"
}

#2D List
answers = [
    ["A. Sasuke Uchiha", "B. Naruto Uzumaki", "C. Sakura Haruno", "D. Kakashi Hatake"],
    ["A. Kamehameha", "B. Rasengan", "C. Chidori", "D. Spirit Bomb"],
    ["A. Chihiro", "B. Haku", "C. No-Face", "D. Yubaba"],
    ["A. Raichu", "B. Pichu", "C. Jolteon", "D. Pikachu"],
    ["A. Light Yagami", "B. L-Lawliet", "C. Near", "D. Ryuk"],
    ["A. Ami Mizuno", "B. Rei Hino", "C. Makoto Kino", "D. Usagi Tsukino"],
    ["A. Hideki Ryuga", "B. Lawliet L", "C. Near", "D. Ryuzaki"]
]



def Game():
    while True:
        score = []
        index_answers = 0
        for key, value in quiz.items():
            print(key)
            for items in answers[index_answers]:
                print(items)
            user_input = input("Answer(A/B/C/D): ").upper()
            index_answers += 1

            if user_input in value:
                print("Correct!")
                score.append(user_input)
            elif user_input not in quiz.values():
                print("Invalid")
            else:
                print("Incorrect!")
                score.append(user_input)
        print("\n")

        print("Your Answer: ", end="")
        for i in score:
            print(i, end=" ")
        print("\n")

        print("Actual Answer: ", end="")
        for key, value in quiz.items():
            print(value, end=" ")
        print("\n")

        while True:
            user_input_1 = input("Wanna play again?(yes/no): ").lower()
            if user_input_1 == "yes":
                break
            elif user_input_1 == "no":
                return
            else:
                print("Invalid")
