# Import necessary libraries
import spacy
from spacy import displacy
import pandas as pd
# Load the english model
nlp = spacy.load("en_core_web_sm")
# Sample text for NER
text = """
Amazon announced its quartely earnings on July 30,2023.
CEO Andy Jassy said the company is investing $ 4 billion on AI technology
Google,based in Mountain View,California also shared its financial support.
The 2024 Summer Olympics will be held in Paris,France.
"""
# Process he text with spaCy
doc = nlp(text)
# Function to exract entities
def extract_entities(doc):
    entities = []
    for ent in doc.ents:
        entities.append({
            'Entity' : ent.text,
            'Label' : ent.label_,
            'Explanation' : spacy.explain(ent.label_)
        })
    return pd.DataFrame(entities)
# Extract entities int a DataFrame
entities_df = extract_entities(doc)
# Display extracted entities to the user
print("Extracted Named Entities: ")
print(entities_df)
# Visualize named entities using DisplaCy
html = displacy.render(doc, style="ent", page=True)
with open("entities.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Visualization saved to entities.html")
# Save entities to a csv file
entities_df.to_csv("Extracted_entities.csv",index=False)
print("\nEntities saved to 'extracted_entities.csv'")
