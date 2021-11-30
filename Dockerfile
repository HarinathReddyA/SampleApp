FROM python3.7
CMD ["python","-u","log_generator.py"]
COPY . .
