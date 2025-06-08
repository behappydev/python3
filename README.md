# MyBlog – Proyecto Django completo (Patrón MVT)

## Instalación rápida
```bash
git clone https://github.com/<TU-USUARIO>/myblog.git
cd myblog
python -m venv venv
source venv/bin/activate        # en Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # opcional
python manage.py runserver
