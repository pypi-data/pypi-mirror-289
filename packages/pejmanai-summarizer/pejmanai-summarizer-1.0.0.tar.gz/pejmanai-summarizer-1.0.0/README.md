# PejmanAI Summarizer

* `pejmanai-summarizer` is a Python package that provides text summarization functionality using the * * `facebook/bart-large-cnn` model from the Hugging Face `transformers` library.

## Installation

- `pip install pejmanai-summarizer`

## Usage

- `from pejmanai_summarizer import summarize_text`

- `text = "Your long text goes here..."`
- `summary = summarize_text(text, max_length=150, min_length=30, do_sample=False)`
- `print(summary)`

* Note: You can change summaize_text function parameters (max_length: int = 150, min_length: int = 30)
