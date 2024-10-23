# Fake News Detector

![Fake News Detector](./Screenshot%20(149).png)

## Project Overview

**Fake News Detector** is a machine learning-based web application that helps users determine whether a news statement is real or fake. It is developed as part of the **AI in Web Programming** course by **Mostafa Magdy**. The application uses a **PassiveAggressiveClassifier** and TF-IDF vectorizer to classify input news text as "real" or "fake" with high accuracy.

## Table of Contents

- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Docker Setup](#docker-setup)
- [How to Run the Project](#how-to-run-the-project)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Acknowledgements](#acknowledgements)

## Technology Stack

- **Backend Framework:** FastAPI
- **Frontend:** HTML, CSS (Bootstrap)
- **Machine Learning Model:** PassiveAggressiveClassifier
- **Data Processing:** TF-IDF Vectorizer
- **Deployment:** Docker

## Docker Setup

This project is containerized with Docker to ensure easy setup and deployment. Follow the steps below to build and run the project in a Docker container.

### Prerequisites

- Docker installed on your system.

### Steps

1. **Clone the Repository**  
   Clone this repository using the command below:

   ```bash
   git clone https://github.com/Mostafa10770/Fake-news-detection-V2.git
   ```

2. **Build the Docker Image**  
   Navigate to the project directory and run the following command to build the Docker image:

   ```bash
   docker build -t fake-news-detector .
   ```

3. **Run the Docker Container**  
   Once the build is complete, you can run the container with the following command:

   ```bash
   docker run -d -p 5000:5000 fake-news-detector
   ```

   The application will be running on `http://127.0.0.1:5000/`.

4. **Stop the Container**  
   To stop the container, find the container ID and stop it:

   ```bash
   docker ps  # To find the container ID
   docker stop <container-id>
   ```

## How to Run the Project

To run the project locally (without Docker), follow these steps:

1. **Install Dependencies**  
   Run the command below to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**  
   After installing the dependencies, start the FastAPI app using Uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

3. **Access the Application**  
   Open your browser and go to `http://127.0.0.1:8000/` to access the app.

## Usage

1. Open the application in your browser.
2. Enter a news statement in the text input box.
3. Click the "Predict" button.
4. The app will classify the news as either "Real News" or "Spam News" based on the machine learning model.

## Screenshots

![Fake News Detector](./Screenshot%20(150).png)

- **Example of Fake News Detection**  
  The input "Egypt is in Asia" is detected as fake news.

![Fake News Detector](./Screenshot%20(152).png)

- **Example of Real News Detection**  
  The input "Egypt is in Africa" is detected as real news.

## Acknowledgements

- **Developed by:** Mostafa Magdy
- **Course:** AI in Web Programming
