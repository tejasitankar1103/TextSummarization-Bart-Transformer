# Text Summarization using BART Transformer

A project that performs both **extractive** and **abstractive** text summarization using natural language processing (NLP) techniques. The main focus is on abstractive summarization using the pre-trained **BART Transformer** (`facebook/bart-large-cnn`) from Hugging Face Transformers.

---

## 🚀 Features

- Abstractive text summarization using BART
- Interactive UI with Streamlit
- CLI support via `summarize.py`
- Clean and modular codebase

---

## 🛠️ Technologies Used

- Python 3.8+
- Hugging Face Transformers
- Streamlit
- NLTK / SpaCy (for optional preprocessing)

---

## ▶️ How to Run

### 💻 Locally

**1. Clone the Repository**

```bash
git clone https://github.com/your-username/text-summarization-bart.git
cd text-summarization-bart
```

**2. Install Requirements**

```bash
pip install -r requirements.txt
```

**3. Run the Streamlit App**

```bash
streamlit run app.py
```

**4. Run via CLI**

```bash
python summarize.py
```

---

## 🧾 Sample Input/Output

**Input:**

```
The Amazon rainforest is a moist broadleaf tropical rainforest in the Amazon biome that covers most of the Amazon basin of South America...
```

**Output Summary:**

```
The Amazon rainforest, also known as Amazonia, covers much of the Amazon basin and is shared by multiple South American countries.
```

---

## 📁 Folder Structure

```
text-summarization-bart/
├── app.py                # Streamlit UI
├── summarize.py          # Core summary function
├── requirements.txt      # Python dependencies
├── README.md             # Project overview
└── Cleaned_Text_Summarization.ipynb  # Jupyter notebook
```

---

## 📸 Screenshots

> Add screenshots here once deployed or during local testing.

---

## 🔮 Future Improvements

- Add extractive summarization toggle (TextRank)
- Multi-language summarization
- REST API endpoint using FastAPI
- Model optimization for speed

---

## 📄 License

[MIT License](LICENSE)

---

## 👤 Author

**Tejas Itankar**\
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/tejas-itankar/) or contribute to this project!

