from django.shortcuts import render, HttpResponse
import requests
from django.http import JsonResponse

def home(request):
    return render(request,'home.html')

def prediction(request):
    name = request.POST.get('fname')
    print(name)
    return render(request,'prediction.html',{'fname':name})

def apiget(request):
    result = requests.get('https://carsaleprice4.herokuapp.com/').json()
    print(result)
    return render(request,'apiget.html',{'answer':result})

def apipost(request):
    age = request.POST.get('age')
    km_driven = request.POST.get('km_driven')
    mileage = request.POST.get('mileage')
    engine = request.POST.get('engine')
    max_power = request.POST.get('max_power')
    seats = request.POST.get('seats')
    Brand = request.POST.get('Brand')
    full_name = request.POST.get('full_name')
    seller_type = request.POST.get('seller_type')
    fuel_type = request.POST.get('fuel_type')
    transmission_type = request.POST.get('transmission_type')
    apiresponse = (age,km_driven,mileage,engine,max_power,seats,Brand,full_name,seller_type,fuel_type,transmission_type)


    #inputval = {"age": 7,"km_driven": 80000,"mileage": 15.5,"engine": 1200,"max_power": 80,"seats": 5,"c_brand": "honda","c_full_name": "civic","c_seller_type": "individual","c_fuel_type": "diesel","c_transmission_type": "manual"}
    inputval = JsonResponse({
    "age": age,
    "km_driven": km_driven,
    "mileage": mileage,
    "engine": engine,
    "max_power": max_power,
    "seats": seats,
    "c_brand": Brand,
    "c_full_name": full_name,
    "c_seller_type": seller_type,
    "c_fuel_type": fuel_type,
    "c_transmission_type": transmission_type
  })
    apiresponse = requests.post('https://carsaleprice4.herokuapp.com/test',data = inputval).json()
    print(apiresponse)
    #print(inputval)
    return render(request,'apipost.html',{'data':apiresponse})