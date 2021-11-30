FROM python:3.8.3
CMD ["python","-u","log_generator.py"]
COPY . .
