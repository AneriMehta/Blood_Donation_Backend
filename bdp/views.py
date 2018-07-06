import pyrebase
from django.shortcuts import render
from django.contrib import auth
config = {
    'apiKey': "AIzaSyAcGLQyvbnBxz8yOUr9DhznW86nJ10nbEo",
    'authDomain': "blooddonation-a2c51.firebaseapp.com",
    'databaseURL': "https://blooddonation-a2c51.firebaseio.com",
    'projectId': "blooddonation-a2c51",
    'storageBucket': "blooddonation-a2c51.appspot.com",
    'messagingSenderId': "1045257882687"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
def signIn(request):
    return render(request, "signIn.html")

def postsign(request):
    email=request.POST.get("email")
    passw = request.POST.get("password")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html",{"e":email})

def logout(request):
    auth.logout(request)
    return render(request,'signIn.html')

def signUp(request):
    return render(request,"signup.html")

def postsignup1(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    age=request.POST.get('textweight')
    bloodgroup=request.POST.get('blood_group')
    donationDate=request.POST.get('date')
    number=request.POST.get('contact_number')
    email=request.POST.get('email')
    passw=request.POST.get('password')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data={"fname":fname, "lname":lname, "age":age, "bloodgroup":bloodgroup, "donationDate":donationDate, "number":number}
        database.child("users").child("donors").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})

    return render(request,"signIn.html")

def postsignup2(request):
    hospitalName=request.POST.get('hname')
    print(hospitalName)
    address=request.POST.get('address')
    print(address)
    peopleInCharge=request.POST.get('people')
    print(peopleInCharge)
    brpm=request.POST.get('blood_required')
    print(brpm)
    email=request.POST.get('email')
    passw=request.POST.get('password')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        print(uid)
        data={"hname":hname, "address":address, "peopleInCharge":peopleInCharge, "bloodRequired":brpm}
        database.child("users").child("hospitals").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"signup.html",{"messg":message})

    return render(request,"signIn.html")
