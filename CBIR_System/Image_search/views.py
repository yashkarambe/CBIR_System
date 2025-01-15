from django.shortcuts import render , HttpResponse
from datetime import datetime
from django.contrib import messages
from CBIR_System.utils import save_person_with_embedding  # Function to handle Pinecone integration
from Image_search import models

# Create your views here.
def index(request):
    # return HttpResponse("Page is working")
    return render(request , 'index.html')

def Search(request):
    return render(request, 'Search.html')

# def add_person(request):
#     if request.method == "POST":
#         # Extract form data from the POST request
#         first_name = request.POST['First_name']
#         middle_name = request.POST['Middel_Name']
#         last_name = request.POST['Last_Name']
#         full_name = f"{first_name} {middle_name} {last_name}".strip()

#         age = request.POST['Age_ID']
#         city = request.POST['City_ID']
#         gender = request.POST['Gender_ID']
#         zip_code = request.POST['Zip_code_ID']
#         image = request.FILES['Photograph_ID']
#         date = datetime.today()
#         # print(type(image))
#         # # Save the person with embedding in Pinecone
#         # # try:
        
#         # save_person_with_embedding(request,
#         #         name=full_name,
#         #         age=age,
#         #         gender=gender,
#         #         city=city,
#         #         zip_code=zip_code,
#         #         image=image,
#         #     )
#         print(first_name, middle_name, last_name, age, city, gender, zip_code, image)
#         person = models.Person(name=full_name,age=age,city=city,zip=zip_code,gender=gender,image=image,date=date)
#         person.save()
#         messages.success(request, "Person added successfully")
#         # except Exception as e:
#         #     messages.warning(request , "Person was not added in Database")
#     # Render the form if it's a GET request
#     return render(request, "index.html")


def add_person(request):
    if request.method == "POST":
        # Extract form data
        first_name = request.POST.get('first_name', '').strip()
        middle_name = request.POST.get('middle_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        full_name = f"{first_name} {middle_name} {last_name}".strip()

        age = request.POST.get('age', '').strip()
        city = request.POST.get('city', '').strip()
        gender = request.POST.get('gender', '').strip()
        zip_code = request.POST.get('zip_code', '').strip()
        image = request.FILES.get('photograph')

        save_person_with_embedding(request,
                name=full_name,
                age=age,
                gender=gender,
                city=city,
                zip_code=zip_code,
                image=image,
        )
        # Save to the database
        # person = models.Person(
        #     name=full_name,
        #     age=age,
        #     city=city,
        #     zip=zip_code,
        #     gender=gender,
        #     image=image,
        #     date=datetime.today()
        # )
        # person.save()
        messages.success(request, "Person added successfully.")
        return render(request, "index.html")
    else:
        messages.warning(request, "Person Was not added.")
    return render(request, "index.html")