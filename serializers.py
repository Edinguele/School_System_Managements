from rest_framework import serializers
from .models import  Utilisateur,Élève, Enseignant, Cours, Classe, Inscription, Note, EmploiDuTemps, Message


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'


class ÉlèveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Élève
        fields = '__all__'

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseignant
        fields = '__all__'

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = '__all__'

class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class EmploiDuTempsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploiDuTemps
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
