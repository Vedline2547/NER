# Named Entity Recognition (NER) with spaCy

## 📌 Project Overview
This project implements Named Entity Recognition (NER) using **spaCy**, a powerful Python library for Natural Language Processing (NLP). It extracts meaningful entities from unstructured text and classifies them into categories such as people, organizations, dates, locations, events, and monetary values.

The project also visualizes the extracted entities in an HTML document and exports the results to a CSV file for further analysis.

## 🎯 Objectives
- Extract named entities from text using a pretrained spaCy language model.
- Classify entities into predefined categories.
- Display extracted entities in a Pandas DataFrame.
- Generate a colour-coded HTML visualization using spaCy's DisplaCy.
- Export extracted entities to a CSV file for analysis.

## 🛠️ Technologies Used
- **Python** – Core programming language
- **spaCy** – Natural Language Processing and Named Entity Recognition
- **Pandas** – Data manipulation and tabular representation
- **DisplaCy** – Named entity visualization

## ⚙️ How It Works
1. Load the pretrained `en_core_web_sm` English language model.
2. Process sample text containing information about companies, people, dates, locations, and financial values.
3. Extract entities and their corresponding labels.
4. Display the extracted results in a DataFrame.
5. Generate an HTML file with highlighted named entities.
6. Save the extracted entities and their explanations in a CSV file.

## 🏷️ Entity Categories
The model can identify several entity types, including:

| Label | Description | Example |
|---|---|---|
| `PERSON` | People | Andy Jassy |
| `ORG` | Organizations | Amazon, Google |
| `DATE` | Dates and periods | July 30, 2023 |
| `MONEY` | Monetary values | $4 billion |
| `GPE` | Countries, cities, and states | Paris, France |
| `EVENT` | Named events | Summer Olympics |

Entity predictions depend on the model and the context of the text.

## 📂 Project Structure

```text
NER/
├── main.py
├── entities.html
├── Extracted_entities.csv
└── README.md
```

- `main.py` – Main Python script for entity extraction and visualization.
- `entities.html` – HTML visualization of extracted entities.
- `Extracted_entities.csv` – CSV file containing entities, labels, and explanations.
- `README.md` – Project documentation.

The HTML and CSV files are generated when the script runs.

## 🚀 Installation and Usage

### 1. Clone the repository

```bash
git clone https://github.com/Vedline2547/NER.git
cd NER
```

### 2. Create and activate a virtual environment (optional but recommended)

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install spacy pandas
```

### 4. Download the spaCy English model

```bash
python -m spacy download en_core_web_sm
```

### 5. Run the project

```bash
python main.py
```

After execution, the program prints the extracted entities and generates `entities.html` and `Extracted_entities.csv` in the current working directory.

Open `entities.html` in your browser to view the colour-coded entity visualization.

## 💡 Applications
- Information extraction from news articles
- Identifying organizations and people in documents
- Financial document analysis
- News and media monitoring
- Text preprocessing for downstream NLP applications

## 🔮 Future Improvements
- Process text from external files and documents.
- Build a web interface using Flask or Streamlit.
- Evaluate entity extraction performance on a labelled dataset.
- Fine-tune or train a custom NER model for domain-specific text.
- Extract entities from larger collections of documents.

## 👩‍💻 Author
**Vedline Ochieng**

GitHub: [Vedline2547](https://github.com/Vedline2547)

---

*This project demonstrates practical Natural Language Processing skills through named entity extraction, data handling, visualization, and file export using Python.*
