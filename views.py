from django.shortcuts import render
from rest_framework import viewsets
from .models import Utilisateur,Élève, Enseignant, Cours, Classe, Inscription, Note, EmploiDuTemps, Message
from .serializers import UtilisateurSerializer,ÉlèveSerializer, EnseignantSerializer, CoursSerializer, ClasseSerializer, InscriptionSerializer, NoteSerializer, EmploiDuTempsSerializer, MessageSerializer

# Create your views here.
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer


class ÉlèveViewSet(viewsets.ModelViewSet):
    queryset = Élève.objects.all()
    serializer_class = ÉlèveSerializer

class EnseignantViewSet(viewsets.ModelViewSet):
    queryset = Enseignant.objects.all()
    serializer_class = EnseignantSerializer

class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class ClasseViewSet(viewsets.ModelViewSet):
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class EmploiDuTempsViewSet(viewsets.ModelViewSet):
    queryset = EmploiDuTemps.objects.all()
    serializer_class = EmploiDuTempsSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
