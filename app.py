from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)
wikipedia.set_lang("en")

def smart_answer(q):
    q = q.lower()

    greetings = ["hello", "hi", "hey", "hii", "good morning", "good evening"]
    thanks = ["thanks", "thank you"]

    if q in greetings:
        return "Hello! 😊 I’m Smart College AI. Ask me anything!"

    if q in thanks:
        return "You're welcome! 💙 Ask more if you want!"

    if "your name" in q:
        return "My name is Smart College AI 🤖"

    if "who made you" in q:
        return "I was created by a smart developer 😄"

    try:
        return wikipedia.summary(q, sentences=5)
    except:
        try:
            return wikipedia.page(q).content[:900]
        except:
            return "Hmm 🤔 I couldn’t find that clearly. Try asking differently!"

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        question = request.form["question"]
        reply = smart_answer(question)

    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)