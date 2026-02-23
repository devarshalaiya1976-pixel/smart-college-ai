from flask import Flask, request, render_template
import wikipedia

app = Flask(__name__)

wikipedia.set_lang("en")

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        question = request.form.get("question")

        try:
            reply = wikipedia.summary(question, sentences=5)
        except:
            reply = "Sorry, I couldn't find information. Try another question."

    return render_template("index.html", reply=reply)

def handler(request):
    return app(request.environ, lambda *args: None)