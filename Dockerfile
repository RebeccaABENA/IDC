FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY modules.py .
COPY test_module.py .

CMD ["python", "-m", "pytest", "test_module.py", "-v"]