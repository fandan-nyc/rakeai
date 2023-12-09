from flask import Flask, request, render_template
from gpt_client import gpt_client

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('input_form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    gpt = gpt_client()
    prompt = request.form['prompt']
    if not prompt:
        prompt = gpt.get_default_prompt() 
    text_input = request.form['text_input']
    result = gpt.fix_grammer_with_prompt(text_input, prompt)
    processed_text = result
    return render_template("input_form.html", processed_text=processed_text)

