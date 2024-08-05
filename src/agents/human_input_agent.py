from langgraph import Agent

class HumanInputAgent(Agent):
    def __init__(self):
        super().__init__()

    def prompt_for_confirmation(self, sorted_resumes):
        # TODO: Implement logic to prompt for human input
        confirmation = input("Do you want to schedule an interview for the top candidate? (yes/no)")
        return confirmation.lower() == "yes"