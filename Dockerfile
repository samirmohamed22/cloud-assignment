
FROM python:3.9-slim
WORKDIR /app
COPY cloud.py .
COPY random_paragraphs.txt .
RUN pip install nltk matplotlib
RUN python -m nltk.downloader stopwords
CMD ["python", "cloud.py"] 