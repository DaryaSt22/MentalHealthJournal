#FROM python:3.11
#
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#COPY requirements.txt .
#
#RUN pip install --upgrade pip && pip install -r requirements.txt
#
#COPY . .
#
#CMD ["python", "MentalHealthJournal/manage.py", "runserver", "0.0.0.0:8000"]