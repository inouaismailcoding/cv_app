from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
from django.db import models

class ProfileImg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_cv/')


    def __str__(self) -> str:
        return self.photo.name
    # Dans ce modèle, nous avons écrasé la méthode  save()
    # pour supprimer l'image originale lorsqu'une nouvelle image est enregistrée
    def save(self, *args, **kwargs):
        if self.pk:
            original = ProfileImg.objects.get(pk=self.pk)
            if original.photo != self.photo:
                original.photo.delete(False)
        super().save(*args, **kwargs)

class ProfileTitle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    titre = models.CharField(max_length=240, verbose_name=_("Nom du profile"))
    profile = models.TextField("Profile",blank=True,null=True)
    
    def __str__(self):
        return f"{self.titre}"

class CV(models.Model):
    STATUT=[
        ("Celibataire","Celibataire"),
        ("Marié","Marié"),
        ('Divorcé',"Divorcé"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nom = models.CharField("Nom",max_length=100,blank=True,null=True)
    prenom = models.CharField("prenom",max_length=100,blank=True,null=True)
    email = models.EmailField("Adresse Email",blank=True,null=True)
    telephone = models.CharField("Numero Telephone",max_length=50,blank=True,null=True)
    birth_date=models.DateField("Date de Naissance",blank=True,null=True)
    address = models.CharField("Adresse ",max_length=250,blank=True,null=True)
    status=models.CharField('Status matrimonial',max_length=250,blank=True,null=True,choices=STATUT)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Experience(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    titre = models.CharField(max_length=200,null=True, blank=True)
    entreprise = models.CharField(max_length=200,null=True, blank=True)
    ville = models.CharField(max_length=200,null=True, blank=True)
    reference = models.CharField(max_length=200,null=True, blank=True)
    telephone_reference = models.CharField(max_length=200,null=True, blank=True)
    debut = models.DateField("date Debut",null=True, blank=True)
    fin = models.DateField("date fin",null=True, blank=True)
    description = models.TextField("description",null=True, blank=True)

    def __str__(self):
        return self.titre

class Formation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    diplome = models.CharField("Diplome Obtenu",max_length=100,null=True, blank=True)
    ecole = models.CharField("Ecole ",max_length=100,null=True, blank=True)
    ville = models.CharField("ville",max_length=100,null=True, blank=True)
    debut = models.DateField("date de debut",null=True, blank=True)
    fin = models.DateField("date fin",null=True, blank=True)
    description = models.TextField("Description du diplome obtenu",null=True, blank=True)

    def __str__(self):
        return self.diplome


class Competences(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    competence = models.CharField(max_length=240)
    niveau = models.IntegerField(choices=[(i, str(i)) for i in range(0, 11)], verbose_name=_("Niveau"))

    def __str__(self):
        return self.competence

class Social(models.Model):
    SOCIAL=[
        ('whatsapp','Whatsapp'),
        ('facebook','Facebook'),
        ('lindln','Lindln'),
        ('instagram','Instagram'),
        ('twitter','Twitter'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    social = models.CharField(max_length=50,null=True,blank=True,choices=SOCIAL)
    link = models.CharField(max_length=240,null=True,blank=True)
   
    def __str__(self):
        return self.social


class Langue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    langue = models.CharField(max_length=100, verbose_name=_("langue"))
    niveau = models.IntegerField(choices=[(i, str(i)) for i in range(0, 11)], verbose_name=_("Niveau"))

    class Meta:
        verbose_name = _("Langue")
        verbose_name_plural = _("Langues")

    def __str__(self):
        return self.langue

class CentreInteret(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    titre = models.CharField(max_length=100, verbose_name=_("Nom"))

    class Meta:
        verbose_name = _("Centre d'intérêt")
        verbose_name_plural = _("Centres d'intérêts")

    def __str__(self):
        return self.titre