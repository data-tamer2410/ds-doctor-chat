FROM python:3.11-slim

WORKDIR /app
COPY /. /.

RUN pip install --no-cache-dir poetry
RUN poetry install --without dev

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "doctor_chat/app.py"]
