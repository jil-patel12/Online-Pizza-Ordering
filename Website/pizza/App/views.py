from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect


from .models import user_extra
from .models import menu1, contact1


# Create your views here.


def index(request):
    return render(request, 'index.html')


def pizza_menu(request):
    pizza_menu = menu1.objects.all()
    return render(request, 'menu.html', {'pizza': pizza_menu})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contectus1 = contact1(contact_name=name, contact_email=email, contact_message=message)
        contectus1.save()
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def reg(request):
    if request.method == "POST":
        password = request.POST['password']
        c_password = request.POST['confirm_password']
        if password == c_password:
            try:
                user = User.objects.get(username=request.POST['user'])
                return render(request, 'Reg.html', {'error': "Username Has Already Been Taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['user'],
                                                password=request.POST['password'],
                                                email=request.POST['email_address'])
                user.save()
                full_name = request.POST['full_name']
                pno = request.POST['pno']
                date_of_birth = request.POST['date_of_birth']
                address1 = request.POST['address1']
                address2 = request.POST['address2']
                city = request.POST['city']
                state = request.POST['state']
                countary = request.POST['countary']
                newextenduser = user_extra(full_name=full_name, phone_no=pno,
                                           Date_of_birth=date_of_birth, user_address1=address1,
                                           user_address2=address2, city=city, state=state,
                                           Countary=countary, user=user)
                newextenduser.save()
                print(full_name)
                return redirect('/login')
            # return render(request, 'Login.html',{'message':'Signned Up!'})
        else:
            return render(request, 'reg.html', {'error': "Password Not Match "})
    else:
        return render(request, 'reg.html')


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'Login.html', {'error': 'Invalid Username Or Password.'})
    else:
        return render(request, 'Login.html')


def order(request):
    name1 = request.POST.get('name1')
    price1 = request.POST.get('price1')
    total1 = request.POST.get('total1')
    return render(request, 'order.html', {'name1': name1})


def final_page(request):
    return render(request, 'final_page.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def ss1(request):
    return render(request, 's1.html')
