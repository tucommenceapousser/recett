from flask import Flask, render_template, request
from docx import Document

app = Flask(__name__)

# Charger le document Word
def extraire_paragraphes(mot_cle):
    doc = Document("rece.doc")  # Assure-toi que le fichier est dans le même dossier
    resultats = [p.text for p in doc.paragraphs if mot_cle.lower() in p.text.lower()]
    return resultats

@app.route("/", methods=["GET", "POST"])
def index():
    resultats = []
    if request.method == "POST":
        mot_cle = request.form.get("mot_cle")
        if mot_cle:
            resultats = extraire_paragraphes(mot_cle)
    return render_template("index.html", resultats=resultats)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
