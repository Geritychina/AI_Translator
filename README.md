
# 🌍 AI Translator with Artificial Intelligence

A smart and simple application for translating between **Bulgarian, English, Russian, and Chinese**, powered by Hugging Face 🤖

![Gradio Translator](https://img.shields.io/badge/Machine_Translation-HuggingFace-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)

---

## 🧠 Overview

This AI-powered translator uses pre-trained machine translation models from [`Helsinki-NLP`](https://huggingface.co/Helsinki-NLP) through the `transformers` library. The user-friendly web interface is built with `gradio`.

---

## 🚀 Features

- 🌐 Translate between:
  - Bulgarian 🇧🇬 ↔ English 🇬🇧  
  - English 🇬🇧 ↔ Russian 🇷🇺  
  - English 🇬🇧 ↔ Chinese 🇨🇳

- 🖥 Web interface with live preview
- ⚡ Fast & accurate translations
- 🔁 Auto-loading of appropriate models

---

## 📦 Installation

> Tested with **Python 3.8+**

1. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, use:

```bash
pip install transformers gradio sentencepiece
```

---

## ▶️ How to Run

Launch the app with:

```bash
python app.py
```

The interface will open in your browser at:

```
http://127.0.0.1:7860
```

---

## 📁 Project Structure

```bash
ai-translator/
├── app.py           # Main Python app with Gradio UI
├── README.md        # Project documentation
└── requirements.txt # Dependency list (optional)
```

---

## 🛠 Common Errors & Fixes

### ❌ `MarianTokenizer requires the SentencePiece library...`

This means `sentencepiece` is missing or failed to install.

### ✅ Solution 1: Install via pip

```bash
pip install sentencepiece
```

### ❌ Still failing? (Windows build error)

1. Go to: [Gohlke's unofficial Python wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#sentencepiece)
2. Download the `.whl` file matching your Python version and system (`cp38`, `cp311`, etc.)
3. Install manually:

```bash
pip install C:\path\to\downloaded\sentencepiece‑x.x.x‑cpXXX‑cpXXX‑win_amd64.whl
```

To check your Python version:

```bash
python --version
```

---

## 🧪 Testing Example

To test the translator:

- In **“Input Text”**, enter: `Здравей`  
- Select **Source Language**: `Bulgarian`  
- Select **Target Language**: `English`  
- Click **Submit**  
- Output should be: `Hello`

---

## ❤️ Special Thanks

- 🤗 [Hugging Face Transformers](https://github.com/huggingface/transformers)
- 🌐 [Gradio](https://gradio.app/)
- 🧪 [Helsinki-NLP](https://huggingface.co/Helsinki-NLP)

---

Made with love by Gergana ™
