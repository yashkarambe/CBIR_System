from pinecone import Pinecone, ServerlessSpec
from Image_search.models import Person
from django.contrib import messages
from django.conf import settings
import os

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Input
from tensorflow.keras.models import Model


# model building
conv_base = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(600, 600, 3))
input_image = Input(shape=( 600,600, 3))  # Input for the right branch
conv  = conv_base(input_image)  # Apply the same conv_base to the right branch
flaten = Flatten()(conv)
FC_layer = Dense(1024, activation='relu')(flaten)
Featur_vector = Dense(512, activation='sigmoid')(FC_layer)
final_model = Model(inputs= input_image , outputs= Featur_vector)
final_model.compile(optimizer='adam', loss='categorical_crossentropy')


def generate_embedding(image_path):
    img = Image.open(image_path)  # Open the image
    img = img.resize((600, 600))  # Resize the image
    img_array = np.array(img)
    embedding = final_model.predict(img_array.reshape(1,600,600,3))
    return embedding
    raise ValueError("Invalid file object provided for embedding generation.")



def save_person_with_embedding(request , name, age,city, gender, zip_code, image):
    # Generate image embedding
    
    messages.success(request, "Person added run hear")
    embedding = generate_embedding(image)
    
    #Connecting with Vector Database 
    index_name = "image-similarity"  
    pc = Pinecone(api_key='pcsk_4cAhnJ_JWTBdMu9iBKy1K1quPEj7kMqsG2qDCs7LXdYRMKELA3pDdjcD2akLVo5TNyprrM')
    # Create index if it doesn't exist
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=512,  # Replace with your model dimensions
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
    person = Person(name=name, age=age, city = city, gender=gender, zip_code=zip_code, embedding_id=embedding_id , image = image)
    person.save()
    return person
