import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

raw_text="Upon losing his memory, a crown prince encounters a commoner’s life and experiences unforgettable love as the husband to Joseon’s oldest bachelorette."
text1= NER(raw_text)

for word in text1.ents:
    print(word.text,word.label_)