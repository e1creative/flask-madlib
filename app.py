from flask import Flask, request, render_template

import stories

app = Flask(__name__)

@app.route("/")
def home_route():
    """Return homepage."""
    return render_template("home.html", fields=stories.story.prompts)


@app.route("/story", methods=["POST"])
def story_route():
    """return the story page with our variables"""

    answers = {}

    for prompt in stories.story.prompts:
        answers[prompt] = request.form[prompt]

    text = stories.story.generate(answers)

    return f"""<h1>{text}"""