from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True) 
    nom = models.CharField(max_length=100)               
    prenom = models.CharField(max_length=100)            
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)      
    role = models.CharField(max_length=50)


class Élève(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_de_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    téléphone = models.CharField(max_length=15)

class Enseignant(models.Model):
    spécialité = models.CharField(max_length=100)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Cours(models.Model):
    nom_cours = models.CharField(max_length=100)
    description = models.TextField()
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)

class Classe(models.Model):
    nom_classe = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)

class Inscription(models.Model):
    élève = models.ForeignKey(Élève, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    année_scolaire = models.CharField(max_length=10)

class Note(models.Model):
    valeur = models.FloatField()
    élève = models.ForeignKey(Élève, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=10)

class EmploiDuTemps(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    jour = models.CharField(max_length=10)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

class Message(models.Model):
    contenu = models.TextField()
    date_envoi = models.DateField(auto_now_add=True)
    expéditeur = models.ForeignKey(User, related_name='messages_envoyés', on_delete=models.CASCADE)
    destinataire = models.ForeignKey(User, related_name='messages_reçus', on_delete=models.CASCADE)
