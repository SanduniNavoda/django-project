# Django Application

This is a Django application that visualizes data from CSV files. Below are the instructions for setting up and running the application using Docker.

## Prerequisites

- Docker installed on your machine.
- Basic understanding of Docker commands.

## Getting Started

### 1. Clone the Repository
Clone this repository to your local machine
```bash
    git clone https://github.com/SanduniNavoda/django-project.git
    cd <repository-directory>
```

### 2. Build the Docker image
Navigate to the project directory (where your Dockerfile is located) and build the Docker image:
```bash
    docker build -t django-app .
```

### 3. Run the Docker Container
Run the Docker container, mapping port 8000 on your host to port 8000 in the container:
```bash
    docker run -p 8000:8000 django-app
```

### 4. Access the Application
Open your web browser and go to:
```bash
    http://127.0.0.1:8000/core/visualize/
```

## Loading Data
If you need to load data from CSV files into the application, make sure the CSV files are placed in the core/data/ directory. Then, run the following command:
```bash
    python manage.py import_data
```
This command will read the CSV files and populate the database with the data.


## Stopping the Application
To stop the application, go back to your terminal where the Docker container is running and press
```bash
    Ctrl + C
```



