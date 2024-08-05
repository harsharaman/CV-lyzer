from langgraph import Agent

class FitmentAnalysisAgent(Agent):
    def __init__(self):
        super().__init__()

    def analyze_fitment(self, resume_summary, job_description):
        # TODO: Implement Fitment Analysis logic here
        analysis =  {
            "strengths": [],
            "weaknesses": [],
            "risks": [],
            "questions": [],
            "fitment_score": []
        }
        return analysis