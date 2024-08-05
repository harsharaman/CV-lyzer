from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def results():
    # Retrieve the uploaded files
    resumes = request.files.getlist('resumes')
    job_description = request.files['job_description']

    # Process the files (for now, just print their filenames)
    for resume in resumes:
        print(f"Uploaded resume: {resume.filename}")
    print(f"Uploaded job description: {job_description.filename}")

    # TODO: Analysis implementation goes here
    return render_template('results.html')

if __name__=='__main__':
    app.run(debug=True)