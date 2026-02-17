# jwt-xss-lab-django
Este repositório demonstra roubo de cookie de sessão e roubo de JWT via XSS em Django, usando Docker.

## Estrutura do Projeto

```
jwt-xss-lab-django/
├── docker-compose.yml
├── victim/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── manage.py
│ ├── victim/
│ │ ├── __init__.py
│ │ ├── settings.py
│ │ ├── urls.py
│ │ ├── wsgi.py
│ └── app/
│ ├── __init__.py
│ ├── views.py
│ ├── urls.py
│ └── templates/
│ └── login.html
└── attacker/
├── Dockerfile
└── server.py
```