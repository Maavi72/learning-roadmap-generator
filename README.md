# 🧠 Learning Roadmap Generator

A web-based platform built with **Django** that allows admins to upload weekly learning goals and resources for various learning paths (e.g. Frontend Developer). Users can view structured roadmaps week by week to guide their learning journey.

---

## 🚀 Features

- 👨‍🏫 Admin panel to add learning goals, topics, and resource links
- 📅 Weekly roadmap display
- 📚 Resource links (e.g. articles, videos, tutorials)
- 🎨 Stylish HTML/CSS UI with gradient background
- 📦 Simple and clean Django project structure

---

## 📁 Project Structure

learning_roadmap/
├── roadmap/ # Main app with models, views, templates
│ ├── templates/
│ │ └── roadmap/
│ │ ├── roadmap_list.html
│ │ └── roadmap_detail.html
├── learning_roadmap/ # Project settings
├── manage.py
└── README.md


---

## 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/Maavi72/learning-roadmap-generator.git
cd learning-roadmap-generator
python -m venv env
env\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
