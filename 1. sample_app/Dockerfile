#base image- 
FROM python:3.9-slim
# """
# This line in your Dockerfile tells Docker:

# Use the official Python 3.9 image as the base for this container, but choose the slim variant. 
# slim is a lightweight version of the full python:3.9 Docker image
# """

# workdir
WORKDIR /app
#choosing /app as the working directory

#copy
COPY . /app
#copying all the files to /app directory (working directory)

#run
RUN pip install -r requirements.txt
#installing all the requirements in the image

#port
EXPOSE 8501
#Exposing port

#command that we want to run
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# """This tells Docker:

# When this container starts, run the command:
# streamlit run app.py --server.port=8501 --server.address=0.0.0.0

# """