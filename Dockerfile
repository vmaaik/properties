FROM arm32v7/python
WORKDIR /rightmove
COPY .. /rightmove
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 5000
CMD ["python", "app.py"]