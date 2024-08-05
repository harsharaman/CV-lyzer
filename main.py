from langgraph import StateGraph, MessagesState
from agents.resume_summary_agent import ResumeSummaryAgent
from agents.fitment_analysis_agent import FitmentAnalysisAgent
from agents.sorting_agent import SortingAgent
from agents.human_input_agent import HumanInputAgent
from agents.email_agent import EmailAgent

def main():
    # Define the graph
    graph = StateGraph()

    #Add nodes to Graph
    graph.add_node('resume_summary', ResumeSummaryAgent())
    graph.add_node('fitment_analysis', FitmentAnalysisAgent())
    graph.add_node('sorting', SortingAgent())
    graph.add_node('human_input', HumanInputAgent())
    graph.add_node('email', EmailAgent())

    # Define the flow between nodes
    graph.add_edge('resume_summary', 'fitment_analysis')
    graph.add_edge('fitment_analysis', 'sorting')
    graph.add_edge('sorting', 'human_input')
    graph.add_edge('human_input', 'email')

    # Initialize the state
    state = MessagesState()

    # Execute the graph
    result = graph.run(state)

    # Handle the result
    print("Workflow execution completed")
    print(result)


if __name__ == "__main__":
    main()