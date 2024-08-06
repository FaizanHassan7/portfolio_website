# django-portfolio

## Project

PortFolio developed using Django Framework (version 1.4.5). Its aim is to be able to show some of your main projects to the world easily.

## Make it work

### Setup your Django installation

+ On Debian: use apt to install the package **python-django**
+ Otherwise: refer to [Django Framework official documentation](https://www.djangoproject.com/download/)

### Get the latest development version

```bash
https://github.com/FaizanHassan7/portfolio_website.git
```


### Setup the project

+ Copy the file **django-portfolio/PortFolio/PortFolio/settings.py.sample** to **django-portfolio/PortFolio/PortFolio/settings.py**
+ Run the script **generate_new_secret_key.py** to generate a SECRET_KEY for the project
+ Edit settings.py

### Test it, run it

For tests, you just have to run the command:
```bash
python manage.py syncdb # Generate the database
python manage.py runserver 0.0.0.0:8000 # Run the development server
```

For more details concerning how to run this project using an Apache server please have a look to [Django Framework official documentation](https://www.djangoproject.com/download/).

## How does it look like?



##homepage
![dh1](https://github.com/user-attachments/assets/df2f0a48-4e30-473f-9e66-bc2686cfa05e)


##homepage
![df2](https://github.com/user-attachments/assets/c983214f-1b99-4a6f-9efe-cf09ac1831b5)


##aboutpage
![dAbout1](https://github.com/user-attachments/assets/41ba7bc5-177a-4d20-bb01-3cdd4e15574c)


##projectpage
![project](https://github.com/user-attachments/assets/f25c7b6c-bf37-4fb9-a9ab-a938f99060de)




##contactpage
![dcontact](https://github.com/user-attachments/assets/e4216579-0d68-4ccc-ab38-0c4a54f1b46d)
