from django.db import models

# Create your models here.

class Languages(models.Model):
    name = models.CharField(max_length=50)
    sigle = models.CharField(max_length=3)

    class Meta:
        verbose_name = "Língua"
        verbose_name_plural = "Línguas"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da categoria")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Word(models.Model):
    name = models.CharField(max_length=100, verbose_name="Palavra/Termo")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="Categoria")
    language = models.ForeignKey(Languages, on_delete=models.SET_NULL, null=True, related_name="Língua")
    meaning = models.TextField(max_length=600, verbose_name="Qual o signficado")
    pronunciation = models.CharField(max_length=100, blank=True, help_text="Como se pronuncia")
    data_created = models.DateField(auto_now_add=True, verbose_name="Adicionado em")
    tradution = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Palavra"
        verbose_name_plural = "Palavras"

    def __str__(self):
        return f"{self.name} ({self.language.sigle.upper()}) -> {self.tradution}"
