from openai import OpenAI # type: ignore
import random
from character import Character
client = OpenAI()


def main():
    startgame()

def startgame():
    num_players = 5 # num of ai players not including user
    random_val = random.choice([True, False])
    user_val = not random_val
    player_roles = [True, True, True, False, random_val]
    random.shuffle(player_roles)

    name_list = ["Alice", "Beau", "Connie", "David", "Emily"]
    player_list = []

    for i in range(0, num_players):
        player_list.append( Character(name_list[i]) )

        player_list[i].set_role(player_roles[i])

        response = start_chat(name_list[i], player_roles[i])

        player_list[i].set_chat_id(response.id)

        print(response.choices[0].message.content)

    print("Welcome to Avalon, a game of building alliances and spreading deceit. What should we call you?")
    name = input()

    print(f"""
    Alright, {name}. You will be playing with five other players: Alice, Beau, Conne, David, and Emily. 
    You will randomly be assigned the role of servant or minion. As a servant, you want every round to 
    succeed and minion visa-versa. Every round, one player will nominate a group of players to go on a
    mission. Players can either pass or fail a mission. Each player can publicallly vote for or against 
    the nomination. If a majority vote for, then each player nominated makes a private vote to pass or 
    fail the mission. Just one vote can fail the mission. 
    """)

    print(f"You will play as a {'Servant' if user_val else 'Minion'}")

    for i in range(0, num_players):
        response = continue_chat_round(player_list[i].chat_id, 1)

        print(response.choices[0].message.content)
    

def start_chat(name, role):
    init_prompt_text = f"We are starting a game of Avalon as {name} and you will play as a {'Servant' if role else 'Minion'}. You will stay in character as ${name} for any response to questions."  
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": init_prompt_text}
        ]
    )
    return response 

def continue_chat_round(chat_id, round_num):
    second_prompt_text = f"We are now starting round ${round_num}. What would you like to say and how badly do you want to speak from 1 - 10?"  
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": second_prompt_text}
        ],
        id=chat_id
    )
    return response 

if __name__ == '__main__':
    main()