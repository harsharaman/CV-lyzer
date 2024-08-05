# CV-lyzer
A multi-agent system which accepts a job description, a set of CVs, and then generates summaries of the CVs along with the fitment analysis.

## Project Structure
~~~
CV-lyzer/
│
├── data/
│   ├── resumes/
│   │   ├── resume1.pdf
│   │   ├── resume2.pdf
│   │   └── ...
│   └── job_description.txt
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── resume_analysis.ipynb
│   ├── fitment_analysis.ipynb
|   ├── sorting_resumes.ipynb
│   └── email_generation.ipynb
│
├── src/
│   ├── agents/
│   │   ├── resume_summary_agent.py
│   │   ├── fitment_analysis_agent.py
│   │   ├── sorting_agent.py
|   |   ├── human_input_agent.py
│   │   └── email_agent.py
│   │
│   ├── ui/
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   └── results.html
│   │   └── app.py
│   │
│   └── main.py
│
├── requirements.txt
└── README.md
~~~


