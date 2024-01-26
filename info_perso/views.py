import os
from dateutil import relativedelta
from django.utils import timezone
from datetime import datetime,timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .forms import * # Importation des formulaires définis dans le fichier forms.py
from .models import *  # Importation des modèles définis dans le fichier models.py


# Create your views here.

def s(request):
    context={}
    try:
        context['profile']=ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profile']=None
    return render(request,'b.html',context)
# Centre Interet vue and evenement
def centre_interet_info(request):
    if request.method=="POST":
        create="createInteretInfo"
        if create in request.POST:
            form=CentreInteretForm(request.POST)
            if form.is_valid:
                interet=form.save(commit=False)
                interet.user=request.user
                interet.save()

                interets=CentreInteret.objects.filter(user_id=request.user.id).order_by('-id')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'interets':list(interets.values()),'errors':form.errors,'success':True})
        # Method Post pour modifier une ligne de la table
        edit="editInteretInfo"
        if edit in request.POST:
            myId=request.POST['id']
            form=CentreInteretForm(request.POST)
            if form.is_valid:
                row=CentreInteret.objects.get(id=myId)
                row.titre=request.POST['titre']
                row.save()

                interets=CentreInteret.objects.filter(user_id=request.user.id).order_by('-id')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'interets':list(interets.values()),'errors':form.errors,'success':True})

    else:
        for i in request.GET:
            # requete pour recuperer un enregistrement
            fetch='fetchOnInteret'
            if fetch in request.GET:
                id_interet=request.GET['id_interet']
                interet=CentreInteret.objects.filter(id=id_interet).values()
                return JsonResponse({'interet':list(interet),'success':True})
            # requete pour supprimer un enregistrement
            delete='deleteOnInteret'
            if delete in request.GET:
                id_interet=request.GET['id_interet']
                interetDel=CentreInteret.objects.get(id=id_interet)
                interetDel.delete()
                interets=CentreInteret.objects.filter(user_id=request.user.id).values()
                return JsonResponse({'interets':list(interets),'success':True})

        context={}
        context['interetForm'] = CentreInteretForm() 
         # Création d'une instance vide du formulaire de Formation
        
        # On verifie si les tables ne sont vides
        # Table dela photo de profil
        if CentreInteret.objects.filter(user_id=request.user.id).exists:
            context['interets']=CentreInteret.objects.filter(user_id=request.user.id).order_by('-id')
        return render(request,'centre_interet_info.html',context)

# Langue and Level vue and evenement
def langue_info(request):
    if request.method=="POST":
        create="createLangueInfo"
        if create in request.POST:
            form=LangueForm(request.POST)
            if form.is_valid:
                langue=form.save(commit=False)
                langue.user=request.user
                langue.save()

                langues=Langue.objects.filter(user_id=request.user.id).order_by('-id')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'langues':list(langues.values()),'errors':form.errors,'success':True})
        # Method Post pour modifier une ligne de la table
        edit="editLangueInfo"
        if edit in request.POST:
            myId=request.POST['id']
            form=LangueForm(request.POST)
            if form.is_valid:
                row=Langue.objects.get(id=myId)
                row.langue=request.POST['langue']
                row.niveau=request.POST['niveau']
                row.save()

                langues=Langue.objects.filter(user_id=request.user.id).order_by('-id')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'langues':list(langues.values()),'errors':form.errors,'success':True})

    else:
        for i in request.GET:
            # requete pour recuperer un enregistrement
            fetch='fetchOnLangue'
            if fetch in request.GET:
                id_langue=request.GET['id_langue']
                langue=Langue.objects.filter(id=id_langue).values()
                return JsonResponse({'langue':list(langue),'success':True})
            # requete pour supprimer un enregistrement
            delete='deleteOnLangue'
            if delete in request.GET:
                id_langue=request.GET['id_langue']
                langueDel=Langue.objects.get(id=id_langue)
                langueDel.delete()
                langues=Langue.objects.filter(user_id=request.user.id).values()
                return JsonResponse({'langues':list(langues),'success':True})

        context={}
        context['langueForm'] = LangueForm() 
         # Création d'une instance vide du formulaire de Formation
        
        # On verifie si les tables ne sont vides
        # Table dela photo de profil
        if Langue.objects.filter(user_id=request.user.id).exists:
            context['langues']=Langue.objects.filter(user_id=request.user.id).order_by('-id')
        return render(request,'langue_info.html',context)
 
# Competence and level competence vue and evenement
def competence_info(request):
    if request.method=="POST":
        create="createCompetenceInfo"
        if create in request.POST:
            form=CompetenceForm(request.POST)
            if form.is_valid:
                competence=form.save(commit=False)
                competence.user=request.user
                competence.save()

                competences=Competences.objects.filter(user_id=request.user.id).order_by('-id')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'competences':list(competences.values()),'errors':form.errors,'success':True})
        # Method Post pour modifier une ligne de la table
        edit="editCompetenceInfo"
        if edit in request.POST:
            myId=request.POST['id']
            form=CompetenceForm(request.POST)
            if form.is_valid:
                row=Competences.objects.get(id=myId)
                row.competence=request.POST['competence']
                row.niveau=request.POST['niveau']
                row.save()

                competences=Competences.objects.filter(user_id=request.user.id).order_by('-id')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'competences':list(competences.values()),'errors':form.errors,'success':True})

    else:
        for i in request.GET:
            # requete pour recuperer un enregistrement
            fetch='fetchOnCompetence'
            if fetch in request.GET:
                id_competence=request.GET['id_competence']
                competence=Competences.objects.filter(id=id_competence).values()
                return JsonResponse({'competence':list(competence),'success':True})
            # requete pour supprimer un enregistrement
            delete='deleteOnCompetence'
            if delete in request.GET:
                id_competence=request.GET['id_competence']
                competenceDel=Competences.objects.get(id=id_competence)
                competenceDel.delete()
                competences=Competences.objects.filter(user_id=request.user.id).values()
                return JsonResponse({'competences':list(competences),'success':True})

        context={}
        context['competenceForm'] = CompetenceForm() 
         # Création d'une instance vide du formulaire de Formation
        
        # On verifie si les tables ne sont vides
        # Table dela photo de profil
        if Competences.objects.filter(user_id=request.user.id).exists:
            context['competences']=Competences.objects.filter(user_id=request.user.id).order_by('-id')
        return render(request,'competence_info.html',context)
 
# Experience vue AND Evenement with Table
def experience_info(request):
    if request.method=="POST":
        create="createExperienceInfo"
        if create in request.POST:
            form=ExperienceForm(request.POST)
            if form.is_valid:
                experience=form.save(commit=False)
                experience.user=request.user
                experience.save()

                experiences=Experience.objects.filter(user_id=request.user.id).order_by('-debut')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'experiences':list(experiences.values()),'errors':form.errors,'success':True})
        # Method Post pour modifier une ligne de la table
        edit="editExperienceInfo"
        if edit in request.POST:
            myId=request.POST['id']
            form=ExperienceForm(request.POST)
            if form.is_valid:
                row=Experience.objects.get(id=myId)
                row.titre=request.POST['titre']
                row.entreprise=request.POST['entreprise']
                row.ville=request.POST['ville']
                try :
                    row.reference=request.POST['reference']
                except :row.reference=""
                try :
                    row.telephone_reference=request.POST['telephone_reference']
                except :row.telephone_reference=""
                try :
                    row.debut=request.POST['debut']
                except :pass
                row.description=request.POST['description']
                if request.POST['fin']=="":
                    row.save()
                else :
                    row.fin=request.POST['fin']
                    row.save()

                experiences=Experience.objects.filter(user_id=request.user.id).order_by('-debut')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'experiences':list(experiences.values()),'errors':form.errors,'success':True})

    else:
        for i in request.GET:
            # requete pour recuperer un enregistrement
            fetch='fetchOnExperience'
            if fetch in request.GET:
                id_experience=request.GET['id_experience']
                experience=Experience.objects.filter(id=id_experience).values()
                return JsonResponse({'experience':list(experience),'success':True})
            # requete pour supprimer un enregistrement
            delete='deleteOnExperience'
            if delete in request.GET:
                id_experience=request.GET['id_experience']
                experienceDel=Experience.objects.get(id=id_experience)
                experienceDel.delete()
                experiences=Experience.objects.filter(user_id=request.user.id).values()
                return JsonResponse({'experiences':list(experiences),'success':True})

        context={}
        context['experienceForm'] = ExperienceForm()  # Création d'une instance vide du formulaire de Formation
        
        # On verifie si les tables ne sont vides
        # Table dela photo de profil
        if Experience.objects.filter(user_id=request.user.id).exists:
            context['experiences']=Experience.objects.filter(user_id=request.user.id).order_by('-debut')
        return render(request,'experience_info.html',context)
 
# Formation vue and evenement with table
def formation_info(request):
    if request.method=="POST":
        create="createFormationInfo"
        if create in request.POST:
            form=FormationForm(request.POST)
            if form.is_valid:
                formation=form.save(commit=False)
                formation.user=request.user
                formation.save()

                formations=Formation.objects.filter(user_id=request.user.id).order_by('-debut')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'formations':list(formations.values()),'errors':form.errors,'success':True})
        # Method Post pour modifier une ligne de la table
        edit="editFormationInfo"
        if edit in request.POST:
            myId=request.POST['id']
            form=FormationForm(request.POST)
            if form.is_valid:
                row=Formation.objects.get(id=myId)
                row.diplome=request.POST['diplome']
                row.ecole=request.POST['ecole']
                row.ville=request.POST['ville']
                try:row.debut=request.POST['debut']
                except:pass
                row.description=request.POST['description']
                if request.POST['fin']=="":
                    row.save()
                else :
                    row.fin=request.POST['fin']
                    row.save()
            
                

                formations=Formation.objects.filter(user_id=request.user.id).order_by('-debut')
        # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
            return JsonResponse({'formations':list(formations.values()),'errors':form.errors,'success':True})

    else:
            # requete pour recuperer un enregistrement
        fetch='fetchOnFormation'
        if fetch in request.GET:
            id_formation=request.GET['id_formation']
            formation=Formation.objects.filter(id=id_formation).values()
            return JsonResponse({'formation':list(formation),'success':True})
        # requete pour supprimer un enregistrement
        delete='deleteOnFormation'
        if delete in request.GET:
            id_formation=request.GET['id_formation']
            formationDel=Formation.objects.get(id=id_formation)
            formationDel.delete()
            formations=Formation.objects.filter(user_id=request.user.id).values()
            return JsonResponse({'formations':list(formations),'success':True})

        context={}
        context['formationForm'] = FormationForm()  # Création d'une instance vide du formulaire de Formation
        
        # On verifie si les tables ne sont vides
        # Table dela photo de profil
        if Formation.objects.filter(user_id=request.user.id).exists:
            context['Formation']=Formation.objects.filter(user_id=request.user.id).order_by('-debut')
        return render(request,'formation_info.html',context)
    
# View upload image profile
def upload_image(request):
    photoForm=ProfileImgForm()
    if request.method=="POST":

            photo=request.FILES["photo"]
            try:
                image = ProfileImg.objects.get(user_id=request.user.id)
                if image:
                    if os.path.isfile(image.photo.path):
                        os.remove(image.photo.path)  # On supprime l"image meme
                    # On supprime l'image dans la base données
                    image.delete()
                    form = ProfileImg(photo=photo,user_id=request.user.id)
            
                    form.save()
            except ObjectDoesNotExist:
                    form = ProfileImg(photo=photo,user_id=request.user.id)
            
                    form.save()
            
            image = ProfileImg.objects.get(user_id=request.user.id)

            return JsonResponse({'success': True, 'image': str(image.photo)})
           
# La fonction views pour le crud de l'information personnelle
def info_perso(request):
    if request.method=="POST":
        if request.POST['createInfoPerso']:
            form=CVForm(request.POST)
            try:
               info_perso=CV.objects.get(user_id=request.user.id)
               print(info_perso)
               info_perso.nom=request.POST['nom']
               info_perso.prenom=request.POST['prenom']
               info_perso.email=request.POST['email']
               info_perso.telephone=request.POST['telephone']
               #info_perso.birth_date=request.POST['birth_date'] 
               info_perso.address=request.POST['address']
               info_perso.status=request.POST['status']
               
               info_perso.save()
               info=CV.objects.filter(user_id=request.user.id)
               return JsonResponse({ 'info': list(info.values())})
            except :
                if form.is_valid():
                    info_perso=form.save(commit=False)
                    info_perso.user=request.user
                    info_perso.save()
                    info=CV.objects.filter(user_id=request.user.id)
                    return JsonResponse({'success': True, 'info': list(info.values()),'errors': form.errors})

# La fonction pour enregistrer lesinformations sur le profile
def profile_info(request):
    if request.method=='POST':
        create='createProfileInfo'
        if create in request.POST:
            form=ProfileForm(request.POST)
            try:
               profile=ProfileTitle.objects.get(user_id=request.user.id)
               profile.titre=request.POST['titre']
               profile.profile=request.POST['profile']
               profile.save()
               profile_info=ProfileTitle.objects.filter(user_id=request.user.id)
               return JsonResponse({ 'profile': list(profile_info.values()),'success': True})
         
            except ProfileTitle.DoesNotExist:
                form=ProfileForm(request.POST)
                if form.is_valid():
                    
                    profile=form.save(commit=False)
                    profile.user=request.user
                    profile.save()
                    profile_info=ProfileTitle.objects.filter(user_id=request.user.id)
                    return JsonResponse({'success': True, 'profile': list(profile_info.values())})   
         

def welcome(request):
    context={}
    #context['experience']=my_context(request)

    return render(request,'welcome.html',context)

def cv(request):
  
    # Si la requête HTTP est de type GET (l'utilisateur demande simplement le formulaire)
    context={}
    context['ProfileImgForm']=ProfileImgForm()
    context['ProfileTextForm']=ProfileForm()
    context['form'] = CVForm()  # Création d'une instance vide du formulaire de CV
    context['formationForm'] = FormationForm()  # Création d'une instance vide du formulaire de Formation
    context['experienceForm'] = ExperienceForm()  # Création d'une instance vide du formulaire de Experience
    context['competenceForm'] = CompetenceForm()  # Création d'une instance vide du formulaire de Experience
    context['langueForm'] = LangueForm()  # Création d'une instance vide du formulaire de Experience
    context['interetForm'] = CentreInteretForm()  # Création d'une instance vide du formulaire de Experience
    
    # On verifie si les tables ne sont vides
    # Table dela photo de profil
    try:
        context['ProfileImg']=ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['ProfileImg']=None
    # Table dela photo de profil
    try:
        context['CV']=CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['CV']=None
    # Table dela photo de profil
    try:
        context['ProfileTitle']=ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    # Table dela photo de profil
    context['experiences']=Experience.objects.filter(user_id=request.user.id)
    # Table dela photo de profil
    context['formations']=Formation.objects.filter(user_id=request.user.id)
    # Table dela photo de profil
    context['competences']=Competences.objects.filter(user_id=request.user.id)
    # Table dela photo de profil
    context['langues']=Langue.objects.filter(user_id=request.user.id)
      # Table dela photo de profil
    context['interets']=CentreInteret.objects.filter(user_id=request.user.id)  
    return render(request,'cv.html',context)
""" 
def is_valid_date_format(date_string, date_format="%Y-%m-%d"):
    try:
        # Tente de convertir la chaîne de date en objet datetime
        datetime.strptime(date_string, date_format)
        return True
        
    except ValueError:
        # Gère l'exception si la conversion échoue
        return False
def my_context(request):
    obj=Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    for exp in obj:
        if is_valid_date_format(exp.debut) and is_valid_date_format(exp.fin):
            dif_mois=relativedelta(exp.fin,exp.debut).month
            exp.dif=str(dif_mois)+" mois"
        else:   
            dif_mois=relativedelta(timezone.now(),exp.debut).month
            exp.dif=str(dif_mois)+" mois"
            exp.dif_err="Present"

    return obj
"""   
def theme1(request):
    context={}
    try :
        context['img'] = ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['img'] =None

    try :

        context['profileTitle'] = ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    try:
        context['cv'] = CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['cv']=None
    context['experiences'] = Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    context['formations'] = Formation.objects.filter(user_id=request.user.id).order_by('-debut')
    context['competences'] = Competences.objects.filter(user_id=request.user.id).order_by('competence')
    context['langues'] = Langue.objects.filter(user_id=request.user.id)
    context['centreInterets'] = CentreInteret.objects.filter(user_id=request.user.id)
    
    return render(request, 'theme1.html', context)  

def theme2(request):
    context={}
    try :
        context['img'] = ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['img'] =None

    try :

        context['profileTitle'] = ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    try:
        context['cv'] = CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['cv']=None
    context['experiences'] = Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    context['formations'] = Formation.objects.filter(user_id=request.user.id).order_by('-debut')
    context['competences'] = Competences.objects.filter(user_id=request.user.id).order_by('competence')
    context['langues'] = Langue.objects.filter(user_id=request.user.id)
    context['centreInterets'] = CentreInteret.objects.filter(user_id=request.user.id)
    context['socials'] = Social.objects.filter(user_id=request.user.id)
    
    return render(request, 'theme2.html', context)

def theme3(request):
    context={}
    try :
        context['img'] = ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['img'] =None

    try :

        context['profileTitle'] = ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    try:
        context['cv'] = CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['cv']=None
    context['experiences'] = Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    context['formations'] = Formation.objects.filter(user_id=request.user.id).order_by('-debut')
    context['competences'] = Competences.objects.filter(user_id=request.user.id).order_by('competence')
    context['langues'] = Langue.objects.filter(user_id=request.user.id)
    context['interets'] = CentreInteret.objects.filter(user_id=request.user.id)
    context['socials'] = Social.objects.filter(user_id=request.user.id)
    
    return render(request, 'theme3.html', context)



def theme4(request):
    context={}
    try :
        context['img'] = ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['img'] =None

    try :

        context['profileTitle'] = ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    try:
        context['cv'] = CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['cv']=None
    context['experiences'] = Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    context['formations'] = Formation.objects.filter(user_id=request.user.id).order_by('-debut')
    context['competences'] = Competences.objects.filter(user_id=request.user.id).order_by('competence')
    context['langues'] = Langue.objects.filter(user_id=request.user.id)
    context['interets'] = CentreInteret.objects.filter(user_id=request.user.id)
    context['socials'] = Social.objects.filter(user_id=request.user.id)
    
    return render(request, 'theme4.html', context)


def theme5(request):
    context={}
    try :
        context['img'] = ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['img'] =None

    try :

        context['profileTitle'] = ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    try:
        context['cv'] = CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['cv']=None
    context['experiences'] = Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    context['formations'] = Formation.objects.filter(user_id=request.user.id).order_by('-debut')
    context['competences'] = Competences.objects.filter(user_id=request.user.id).order_by('competence')
    context['langues'] = Langue.objects.filter(user_id=request.user.id)
    context['interets'] = CentreInteret.objects.filter(user_id=request.user.id)
    context['socials'] = Social.objects.filter(user_id=request.user.id)
    
    return render(request, 'theme5.html', context)

def theme6(request):
    context={}
    try :
        context['img'] = ProfileImg.objects.get(user_id=request.user.id)
    except ProfileImg.DoesNotExist:
        context['img'] =None

    try :

        context['profileTitle'] = ProfileTitle.objects.get(user_id=request.user.id)
    except ProfileTitle.DoesNotExist:
        context['profileTitle']=None
    try:
        context['cv'] = CV.objects.get(user_id=request.user.id)
    except CV.DoesNotExist:
        context['cv']=None
    context['experiences'] = Experience.objects.filter(user_id=request.user.id).order_by('-debut')
    context['formations'] = Formation.objects.filter(user_id=request.user.id).order_by('-debut')
    context['competences'] = Competences.objects.filter(user_id=request.user.id)
    context['langues'] = Langue.objects.filter(user_id=request.user.id)
    context['interets'] = CentreInteret.objects.filter(user_id=request.user.id)
    context['socials'] = Social.objects.filter(user_id=request.user.id)
    
    return render(request, 'theme6.html', context)

