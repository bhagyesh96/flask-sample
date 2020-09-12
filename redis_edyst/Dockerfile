# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster
EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /edyst
ADD . /edyst
RUN useradd appuser && chown -R appuser /edyst
USER appuser
CMD ["python", "worker.py"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app","--workers", "4","--log-level=debug hello"]
