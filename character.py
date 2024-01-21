class Character:

    # What do I need to store here boolean: good/bad guy, chat id?, name, 

    # Store the good/bad value randomly berween AI's and assign the only the AI's giving the leftover value to the user 

    def __init__(self, name) -> None:
        self.name = name
    
    def set_role(self, role):
        self.role = role

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def set_assistant_id(self, assistant_id):
        self.assistant_id = assistant_id
    
    def set_thread_id(self, thread_id):
        self.thread_id = thread_id