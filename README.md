# 📚 LembraPalavra

LembraPalavra is a web application built with Django that helps language learners store and organize new words and expressions from different languages.

Instead of keeping vocabulary notes scattered across notebooks, apps, or documents, users can save words in a structured way, including their meaning, pronunciation, language, and category.

---

## ✨ Features

* Add new words and expressions
* Store translations and meanings
* Save pronunciation guides
* Organize words by language
* Organize words by category
* Search words quickly
* View detailed information about each word
* Edit and delete existing entries
* Manage languages and categories

---

## 📖 Example

| Word     | Language | Meaning   | Pronunciation |
| -------- | -------- | --------- | ------------- |
| Merci    | French   | Thank you | mêrcí         |
| Hallo    | German   | Hello     | hálo          |
| Arigatou | Japanese | Thank you | arigatô       |

---

## 🗂 Data Structure

### Language

Represents a language.

Example:

* English (EN)
* French (FR)
* Spanish (ES)

### Category

Represents a group of words.

Examples:

* Greetings
* Food
* Travel
* Technology
* Business

### Word

Each word contains:

* Name
* Translation
* Meaning
* Pronunciation
* Language
* Category
* Creation date

---

## 🔎 Search

The main page provides a search bar that allows users to quickly find stored words.

Example:

Searching for:

```text
merci
```

Returns:

```text
Merci
Language: French
Meaning: Thank you
Pronunciation: mêrcí
```

---

## 🛠 Technologies

* Python
* Django
* HTML5
* CSS3
* SQLite

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-user/lembralavra.git
```

Access the project folder:

```bash
cd lembralavra
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🎯 Project Goal

The goal of LembraPalavra is to provide a simple and organized vocabulary management system for students learning foreign languages.

By categorizing and centralizing vocabulary, learners can review words more efficiently and build a personal multilingual dictionary.

---

## 📷 Future Improvements

* User authentication
* Favorite words
* Review system
* Flashcards
* Spaced repetition
* Audio pronunciation
* Word difficulty levels
* Statistics dashboard
* Dark mode
* Export to PDF/Excel

---

## 📄 License

This project is available for educational and personal use.
