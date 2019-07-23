# TheMisfitBugBlog
Minimalist Django blog with a dark theme

What it is:
A minimalist blog created in Django 2.2 and Bootstrap 4.3 (CDN). It consists of the base essentials of a Blog application including the ability to upload an image when creating a post. It uses the default Django Auth system to manage logins and logging in is required for managing posts. However, user registration is not configured. Users will have to be added in Django Admin.

Features:
* Responsive UI
* Featured Posts On/Off
* Upload an image for each post (uploads are stored in upload-date-wise organized folders in the server storage)
* Managing Posts is limited to logged in users

Generic Deployment Instructions:
* https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04

Required Packages:
* django-cleanup
* pillow
* django-recaptcha

Instructions for setting up reCAPTCHA:
* Register for Google reCAPTCHA
* change RECAPTCHA_PUBLIC_KEY = 'MyRecaptchaKey123' and RECAPTCHA_PRIVATE_KEY = 'MyRecaptchaPrivateKey456' with the values obtained during registration in settings.py
* https://github.com/praekelt/django-recaptcha
