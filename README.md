# Image Similarity Search with Django and Pinecone

This project implements an **Image Similarity Search** system using Django as the backend framework and Pinecone as the vector database. The system allows users to upload an image, search for similar images, and display matching results along with associated metadata such as the person's name, age, city, gender, and match score.

---

## Features

- Upload an image and find visually similar images from the database.
- Integration with **Pinecone** for vector similarity search.
- Dynamic display of search results on an HTML page using Bootstrap cards.
- Support for storing metadata about people (name, age, gender, location, etc.) and their associated images.

---

## Requirements

### Backend
- **Python 3.8+**
- **Django 4.2+**
- **Pinecone** Python client

### Frontend
- **HTML**, **CSS** (Bootstrap for styling)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yashkarambe/CBIR_System.git
   cd CBIR_System

2. **Install Dependencies**
    pip install -r requirements.txt

3. **Set Up Pinecone API**

    Sign up at Pinecone.
    Create an API key and update the project settings with your API key and environment.

3. **Configure Django**

    Update settings.py with your database and media settings.
    Run the migrations:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. **Run the Development Server**
    ```bash
    python manage.py runserver

5. **Access the Application**
    Open your browser and go to http://127.0.0.1:8000.


**Acknowledgements**
-    Django Framework
-    Pinecone Vector Database
-    Bootstrap
-    Pillow for image processing


## License

This repository is licensed under a custom closed-source license. All rights reserved. For more information, see the [LICENSE](LICENSE) file.
