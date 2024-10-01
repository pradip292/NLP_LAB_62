#To perform NER using spacy on user input text
import spacy
nlp = spacy.load('en_core_web_sm')
text = input("Enter the text: ")
doc = nlp(text)
for ent in doc.ents:
    print(
        f"""
    {ent.text = }
    {ent.start_char = }
    {ent.end_char = }
    {ent.label_ = }
    spacy.explain('{ent.label_}') = {spacy.explain(ent.label_)}"""
    )

from spacy import displacy
displacy.serve(doc, style="ent")