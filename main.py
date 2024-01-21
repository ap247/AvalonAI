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

        assistant = create_assistant(name_list[i], player_roles[i])

        player_list[i].set_assistant_id(assistant.id)

        thread = create_thread()

        player_list[i].set_thread_id(thread.id)

    print("Welcome to Avalon, a game of building alliances and spreading deceit. What should we call you?")
    name = input()

    print(f"""Alright, {name}. You will be playing with five other players: Alice, Beau, Conne, David, and Emily. 
    You will randomly be assigned the role of servant or minion. As a servant, you want every round to 
    succeed and minion visa-versa. Every round, one player will nominate a group of players to go on a
    mission. Players can either pass or fail a mission. Each player can publicallly vote for or against 
    the nomination. If a majority vote for, then each player nominated makes a private vote to pass or 
    fail the mission. Just one vote can fail the mission.""")

    print(f"You will play as a {'Servant' if user_val else 'Minion'}")

    for i in range(0, num_players):
        create_message_round(player_list[i].thread_id, 1)
        

    

# def start_chat(name, role):
#     init_prompt_text = f"""
#     We are starting a game of Avalon as {name} and you will play as a {'Servant' if role else 'Minion'}. 
#     You will stay in character as {name} for any response to questions. Don't use references to the game's lore.
#     Respond with modern social dynamics.
#     """  
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": init_prompt_text}
#         ]
#     )
#     return response 

# def continue_chat_round(chat_id, round_num):
#     second_prompt_text = f"""
#                             We are now starting round {round_num}.
#                             What would you like to say and how much do you want to speak from 1 - 10?
#                             """  
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": second_prompt_text}
#         ],
#         id=chat_id
#     )
#     return response 

def create_assistant(name, role):
    init_prompt_text = f"""We are starting a game of Avalon as {name} and you will play as a {'Servant' if role else 'Minion'}. 
You will stay in character as {name} for any response to questions. Don't use references to the game's lore.
Respond with modern social dynamics. Respond with {name}'s response in quotes."""  
    
    assistant = client.beta.assistants.create(
        name=f"Avalon Player {name}",
        description=init_prompt_text,
        model="gpt-4"
    )
    return assistant

def create_thread():
    return client.beta.threads.create()

def create_message_round(thread_id, round_num):
    prompt_text = f"""We are now starting round {round_num}.
What would you like to say and how much do you want to speak from 1 - 10?""" 
    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=prompt_text,
    )
    return thread_message

def run_thread(cur_thread_id, cur_assistant_id):
    run = client.beta.threads.runs.create(
        thread_id=cur_thread_id,
        assistant_id=cur_assistant_id
    )



if __name__ == '__main__':
    main()