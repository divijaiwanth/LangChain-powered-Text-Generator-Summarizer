# 🧠 LangChain-powered Text Generator & Summarizer

This mini project is a simple yet powerful app that uses **LangChain**, **Hugging Face Transformers**, and **Streamlit** to generate and summarize text. You input a topic, and the app returns a generated paragraph using **GPT-2** and a concise summary using **BART**.

---

## 🚀 Features

* ✍️ **Text Generation** using `GPT-2`
* 🧾 **Summarization** using `facebook/bart-large-cnn`
* 🔗 **LangChain Integration** for dynamic prompt templates and LLM chaining
* 🖼️ **Streamlit UI** for a fast, interactive experience

---

## 🧱 Tech Stack

* [Streamlit](https://streamlit.io/) – UI
* [Hugging Face Transformers](https://huggingface.co/transformers/) – NLP models
* [LangChain](https://www.langchain.com/) – LLM orchestration

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-text-gen-summarizer.git
cd langchain-text-gen-summarizer
```

### 2. Create & activate virtual environment (optional but recommended)

```bash
# For Unix/macOS
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📋 Requirements

Your `requirements.txt` should include:

```txt
streamlit
transformers
torch
langchain
huggingface_hub
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔐 Hugging Face CLI Setup (for private models or authenticated access)

1. **Install the Hugging Face CLI:**

```bash
pip install huggingface_hub
```

2. **Log in with your Hugging Face token:**

```bash
huggingface-cli login
```

3. **Get your token** from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) and paste it when prompted.

Once logged in, access to private models will be seamless.

---

## 🖼️ Screenshot

&#x20;

---

## 🧾 Project Description

Streamlit app that generates and summarizes text using GPT-2 and BART via LangChain.

---

## 💡 Future Improvements

* Add model selection from UI
* Support longer text inputs
* Save outputs to file or PDF
