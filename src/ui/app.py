from fasthtml.common import *
app, rt = fast_app()

@rt("/")
def index():
    return Div(
        P("Please upload resumes and job description"),
        # Add form for file upload
    )

@rt("/results")
def results():
    return Div(
        P("Results of the analysis"),
        # Display Analysis results
    )

serve()