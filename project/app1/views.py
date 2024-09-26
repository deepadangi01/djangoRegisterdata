from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):

    return render(request,'register.html')

# def login(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         name1=request.COOKIES['name'] 
#         contact1=request.COOKIES['contact']
#         email1=request.COOKIES['email'] 
#         password1=request.COOKIES['password'] 
#         print(name1,contact1,email,password1)
#         if email==email1:
#             if password1==password:
#                 data={
#                     'name':name1,
#                     'email':email1,
#                     'contact':contact1,
#                     'pass':password1
#                     }
#                 return render(request,'dashboard.html',data)
#                 # return render(request,'first.html',data)
#             else:
#                 msg="email & password not matched "
#                 return render(request,'login.html',{'msg':msg})
#         else:
#                 msg="email not register "
#                 return render(request,'login.html',{'msg':msg})
 
#     else:
#        msg="Welcome to login page"
#        return render(request,'login.html',{'msg':msg})

# def rdata(request):
#     print(request.method)
#     print(request.POST)
#     cstoken = request.POST.get('csrfmiddlewaretoken')
#     name = request.POST.get('nm')
#     contact = request.POST.get('con')
#     email = request.POST.get('em')
#     password = request.POST.get('pass')
#     # print(cstoken)
#     # print(name)
#     # print(contact)
#     # print(email)
#     # print(password)
#     response = render(request,'login.html')
#     response.set_cookie('name',name)
#     response.set_cookie('contact',contact)
#     response.set_cookie('email',email)
#     response.set_cookie('password',password)
#     return response
# def userlogin(request):
#     if request.method=='POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        data123=request.session.get('data')
        if data123['email']==email:
            if data123['password']==password:
                my_data={
                    'nm':data123['name'],
                    'em':data123['email'],
                    'con':data123['contact'],
                    'pass':data123['password']
                }
                return render(request,'dashboard.html',my_data)
            else:
                msg="password not correct"
                return render (request,'login.html',{'msg':msg})
        else:
            msg="email not found"
            return render (request,login.html,{'msg':msg})
    else:
        return render(request,'login.html')

    
    
def rdata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=request.POST.get('contact')
        data={
           'name':name,
           'email':email,
           'password':password,
           'contact':contact,

        }
        request.session['data']=data
        return render(request,'login.html')
    else:
        return render (request,'register.html')

def logout(request):
    return render(request,'home.html') 


# def logout(request):
#     response = render(request, 'home.html')

#     response.delete_cookie('name')
#     response.delete_cookie('password')
#     response.delete_cookie('email')
#     response.delete_cookie('contact')

#     return response


    


    


