from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import models

app = Flask(__name__)
app.config['SECRET_KEY'] = 'beans'

debug = DebugToolbarExtension(app)

story = models.Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def show_prompts():
    return render_template('form.html', prompts=story.prompts)

@app.route('/story')
def show_story():
    ans = {}
    for item in story.prompts:
        value = request.args[item]
        ans[item] = value
    story_text = story.generate(ans)

    
    #{noun: ans, verb: ans, ...}
    # Get answers from fields
    # Generate story
    # Put html with story on page
    return render_template('story.html', story_text=story_text)
                                                  