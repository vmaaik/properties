FROM bbalenalib/raspberrypi3-alpine-python:3.11.2-3.15
WORKDIR /rightmove
COPY .. /rightmove
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]