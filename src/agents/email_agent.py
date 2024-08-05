from langgraph import Agent

class EmailAgent(Agent):
    def __init__(self):
        super().__init__()

    def draft_email(self, candidate_info):
        # TODO: Implement email crafting logic here
        email_content = f"""Dear {candidate_info['name']},
                	        Thank you for applying to our company.
                            We would like to schedule an interview with you.
                            Regards,
                            Recruitment Team"""
        return email_content