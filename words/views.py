from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def home(request):
    search = request.GET.get('search', '')
    language_id = request.GET.get('language', '')

    words = Word.objects.select_related(
        'language',
        'category'
    )

    # Pesquisa por nome
    if search:
        words = words.filter(
            name__icontains=search
        )

    # Filtro por idioma
    if language_id:
        words = words.filter(
            language_id=language_id
        )

    languages = Languages.objects.all().order_by('name')

    context = {
        'words': words,
        'search': search,
        'languages': languages,
        'selected_language': language_id
    }

    return render(
        request,
        'home.html',
        context
    )


def word_detail(request, pk):
    word = get_object_or_404(
        Word.objects.select_related(
            'language',
            'category'
        ),
        pk=pk
    )

    return render(
        request,
        'detail.html',
        {'word': word}
    )


def word_create(request):
    if request.method == 'POST':
        form = WordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('words:home')

    else:
        form = WordForm()

    return render(
        request,
        'form.html',
        {'form': form}
    )


def word_update(request, pk):
    word = get_object_or_404(Word, pk=pk)

    if request.method == 'POST':
        form = WordForm(
            request.POST,
            instance=word
        )

        if form.is_valid():
            form.save()
            return redirect('words:home')

    else:
        form = WordForm(instance=word)

    return render(
        request,
        'form.html',
        {'form': form}
    )


def word_delete(request, pk):
    word = get_object_or_404(Word, pk=pk)

    if request.method == 'POST':
        word.delete()
        return redirect('words:home')

    return render(
        request,
        'delete.html',
        {'word': word}
    )

# categorys

def category_list(request):
    categories = Category.objects.all().order_by('name')

    return render(
        request,
        'categories/categories.html',
        {'categories': categories}
    )


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('words:categories')

    else:
        form = CategoryForm()

    return render(
        request,
        'categories/category_form.html',
        {'form': form}
    )


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('words:categories')

    return render(
        request,
        'categories/category_delete.html',
        {'category': category}
    )

# languages

def language_list(request):
    languages = Languages.objects.all().order_by('name')

    return render(
        request,
        'languages/languages.html',
        {'languages': languages}
    )


def language_create(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('words:languages')

    else:
        form = LanguageForm()

    return render(
        request,
        'languages/language_form.html',
        {'form': form}
    )


def language_delete(request, pk):
    language = get_object_or_404(Languages, pk=pk)

    if request.method == 'POST':
        language.delete()
        return redirect('words:languages')

    return render(
        request,
        'languages/language_delete.html',
        {'language': language}
    )