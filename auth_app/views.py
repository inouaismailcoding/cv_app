from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
# Create your views here.


# Vue pour ajouter un nouveau utilisateur 
def signUpUser(request):
    context={}
    context['form']=SignUserForm()

    if request.method=='POST':
        form=SignUserForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('welcome')
        
        else:
            return render(request,'signUp.html',{'errors':form.errors,'form':form})

    return render(request,'signUp.html',context)

def loginUser(request):
    if request.method=='POST':
        form=loginUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            pwd=form.cleaned_data['pwd']

            # On authentifie l'utilisateur 
            user=authenticate(username=username,password=pwd)
            
            # On verifie si l'utilisateur existe dans la base de données
            if user is not None:
                login(request,user)
                return redirect('welcome')
            # Si l'utilisateur n'existe pas on renvoi un message d'erreur
            else :
                print('error')
                messages.error(request,'Error Authentification : Username or password not correct')
                return render(request,'login.html',{"form":form})
        else: 
            for field in form.errors:
                form[field].field.widget.attrs['class']+='is-invalid'
            return render(request,'login.html',{'form':form})

    else:
        form=loginUserForm()
        print(form)
        return render(request,'login.html',{'form':form})


def logoutUser(request):
    logout(request)
    return redirect ('login')