
## Django Installieren und Einrichten

### Voraussetzungen
- Python 3.12 installiert
- Git installiert

### Schritte

1. **Repository klonen**
   Klonen Sie das Repository in Ihr Home-Verzeichnis und wechseln Sie in das Projektverzeichnis:
   ```bash
   cd $HOME
   git clone https://github.com/thorstenkloehn/django.git
   cd django

2. **Virtuelle Umgebung einrichten**
    Erstellen Sie eine virtuelle Umgebung und aktivieren Sie diese:
    ```bash
    python3.12 -m venv venv
    source venv/bin/activate
    ```
 3. **Django installieren**
    Installieren Sie Django:
    ```bash
    python -m pip install Django==5.1
    ```   
 4. **PostgreSQL Treiber installieren**
    Installieren Sie den PostgreSQL-Treiber:
    ```
    pip install psycopg2
    ```
5. **Datenbank einrichten**   
    Erstellen Sie die Datenbank:
    ```bash
    sudo -u postgres -i
    createdb -E UTF8 -O thorsten django
    exit
    ``` 
6. **Django-environ Instsllieren**
    Installieren Sie Django-environ:
    ```bash
    pip install django-environ
    ```
7. **Erstellen Sie eine .env-Datei im Projektverzeichnis und fügen Sie**
```bash
cd mein_projekt
sudo nano .env
```
8.  ***env Text einfügen***
```bash
SECRET_KEY=django-insecure
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
DEBUG=True
```
9. **Datenbank migrieren**
Führen Sie die Migrationen durch:
```bash
python manage.py migrate
```
10. ***superuser erstellen***
```bash
python manage.py createsuperuser
```
11. **Server starten**
Starten Sie den Entwicklungsserver:
```bash
python manage.py runserver
```
  
