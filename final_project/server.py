from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    def englishToFrench():
    englishText = request.args.get('englishText')
    frenchText = translator.translateneglishToFrench(englishText)
    return frenchText


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    def frenchToEnglish():
    frenchText = request.args.get('frenchText')
    englishText = translator.translateFrenchtoEnglish(frenchText)
    return englishText
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
