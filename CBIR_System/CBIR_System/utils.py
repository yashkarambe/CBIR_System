from pinecone import Pinecone, ServerlessSpec
from Image_search.models import Person
from django.contrib import messages
from django.conf import settings
import os

from PIL import Image
import numpy as np

import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.models import Model
import pickle 


# model loading
final_model = pickle.load(open('/mnt/c/Users/YASH/OneDrive/Desktop/CBIR_System/CBIR_System/Model.pkl','rb'))


def generate_embedding(image_path):
    img = Image.open(image_path)  # Open the image
    img = img.convert('RGB')
    img = img.resize((600, 600))  # Resize the image
    img_array = np.array(img)
    embedding = final_model.predict(img_array.reshape(1,600,600,3))
    return embedding



def save_person_with_embedding(request , name, age,city, gender, zip_code, image):
    # Generate image embedding
    
    # messages.success(request, "Check the Function!")
    embedding = generate_embedding(image)
    
    #Connecting with Vector Database 
    index_name = "image-similarity"  
    pc = Pinecone(api_key='pcsk_4cAhnJ_JWTBdMu9iBKy1K1quPEj7kMqsG2qDCs7LXdYRMKELA3pDdjcD2akLVo5TNyprrM')
    # Create index if it doesn't exist
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=1024,  # Replace with your model dimensions
            metric="cosine",  # Replace with your model metric
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
        print(f"Index '{index_name}' created.")
    else:
        print(f"Index '{index_name}' already exists.")
    
    # Store embedding in Pinecone
    index = pc.Index(index_name)
    embedding_id = f"{name}_{age}"  # Unique ID for this embedding
    embedding_data = np.array(embedding, dtype=np.float32)
    embedding_data = embedding_data.tolist()
    index.upsert(vectors=[
        {"id": embedding_id, "values": embedding_data[0]}
    ])
    
    # Save person info in Django model
    person = Person(name=name, age=age, city = city, gender=gender, zip=zip_code, embedding_id=embedding_id , image = image)
    person.save()
    return person



def Search_In_DB(Image_path):
    #Connecting with Vector Database 
    index_name = "image-similarity"  
    pc = Pinecone(api_key='pcsk_4cAhnJ_JWTBdMu9iBKy1K1quPEj7kMqsG2qDCs7LXdYRMKELA3pDdjcD2akLVo5TNyprrM')
    index = pc.Index(index_name)
    
    img = Image.open(Image_path)  # Open the image
    img = img.convert('RGB')
    img = img.resize((600, 600))  # Resize the image
    img_array = np.array(img)  # Convert to NumPy array
    
    query_vector = final_model.predict(img_array.reshape(1,600,600,3)) #add a batch dimension
    query_vector = np.array(query_vector, dtype=np.float32)
    query_vector = query_vector.tolist()
    
    results = index.query(
    vector=query_vector,
    top_k=5,  # Number of results to retrieve
    include_metadata=False
    )
    
    matching_ids = [
    {'id': match['id'], 'score': match['score']} 
    for match in results['matches'] if match['score'] > 0.60
    ]
    return matching_ids