from langgraph import Agent

class SortingAgent(Agent):
    def __init__(self):
        super().__init__()

    def sort_resumes(self, fitment_analyses):
        # TODO: Implement sorting logic here
        sorted_resumes = sorted(fitment_analyses,
                                key=lambda x: x['fitment_score'], 
                                reverse=True)
        return sorted_resumes