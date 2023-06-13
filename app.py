

from flask import Flask, request, render_template
import openai

app = Flask(__name__, template_folder='templates')
from app.utils import openai_utils



openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_prompt():
    prompt = request.form['prompt']
    model = request.form['model']

    if model == 'ChatGPT':
        model_name = 'gpt-3.5-turbo'

    response = openai.Completion.create(
        engine=model_name,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )

    answer = response.choices[0].text.strip()

    return render_template('result.html', prompt=prompt, model=model, answer=answer)

if __name__ == '__main__':
    app.run()

