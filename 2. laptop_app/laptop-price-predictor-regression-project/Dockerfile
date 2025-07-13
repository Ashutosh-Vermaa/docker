FROM python:3.7
#image of python to install (with a bare minimum OS)

WORKDIR /app
#definig working directory in image

COPY . /app
#copy files from current folder into the image

RUN pip install -r requirements.txt
# installing all the requirement

EXPOSE 8501
#exposing the port to listen for the application inside the container

CMD ["streamlit", "run","app.py","--server.port=8501", "--server.address=0.0.0.0"  ]
# commands to execute when this image is run