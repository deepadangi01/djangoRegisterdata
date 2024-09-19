from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)        
    else:
       return render(request,'login.html')

def rdata(request):
    print(request.method)
    print(request.POST)
    cstoken = request.POST.get('csrfmiddlewaretoken')
    name = request.POST.get('nm')
    contact = request.POST.get('con')
    email = request.POST.get('em')
    password = request.POST.get('pass')
    # print(cstoken)
    # print(name)
    # print(contact)
    # print(email)
    # print(password)
    response = render(request,'login.html')
    response.set_cookie('name',name)
    response.set_cookie('conatct',contact)
    response.set_cookie('email',email)
    response.set_cookie('password',password)
    return response
# def userlogin(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)


    


