from transformers import pipeline

def summarize_text(text: str, max_length: int = 150, min_length: int = 30, do_sample: bool = False) -> str:
    """
    Summarize the input text using the BART model.

    :param text: The text to summarize.
    :param max_length: The maximum length of the summary.
    :param min_length: The minimum length of the summary.
    :param do_sample: Whether or not to use sampling.
    :return: The summarized text.
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']
