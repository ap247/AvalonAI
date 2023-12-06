class Character:

    # What do I need to store here boolean: good/bad guy, chat id?, name, 

    # Store the good/bad value randomly berween AI's and assign the only the AI's giving the leftover value to the user 

    def __init__(self, name) -> None:
        self.name = name
    
    def set_role(self, role):
        self.role = role

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id