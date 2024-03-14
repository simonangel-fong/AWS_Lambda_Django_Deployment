# Document - Deploy Django project on Lambda using Zappa

[Back](../README.md)

- [Document - Deploy Django project on Lambda using Zappa](#document---deploy-django-project-on-lambda-using-zappa)
  - [Clone a Django project](#clone-a-django-project)
  - [Configure Database](#configure-database)
  - [Deploy Application](#deploy-application)
  - [Configure Domain Name and SSL](#configure-domain-name-and-ssl)

---

## Clone a Django project

- To make it simple, an existing Django project is clone at the root of this project.
  - GitHub: https://github.com/simonangel-fong/Django_Simple_CRUD.git
- Collect static files
- Test locally.

![clone_django01](./pic/clone_django01.png)

---

## Configure Database

- The use of sqlite3 database might raise error.

  - In this case, use RDS MySQL instead.
  - Migrate Database

- Install package

```sh
# install mysql package
pip install pymysql
```

- Configure project’s `__init__.py` file

```py
import pymysql
pymysql.install_as_MySQLdb()
```

- Configure `settings.py`
  - can use `.cnf` file

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'HOST': 'rds_endpoint',
        'USER': 'db_username',
        'PASSWORD': 'db_pwd'
    }
}
```

---

## Deploy Application

- Install package

```sh
pip install zappa
```

- Running the Initial Setup using default parameters.

```sh
zappa init
```

![init](./pic/zappa_init01.png)

![init](./pic/zappa_init02.png)

- A json file is created

![zappa_init03](./pic/zappa_init03.png)

- package and deploy application to a stage

```sh
zappa deploy django_lambda
```

![zappa_init03](./pic/zappa_init04.png)

- A lambda and api have been created.

![zappa_init03](./pic/zappa_init09.png)

![zappa_init03](./pic/zappa_init08.png)

---

- Visit url
  - the initial deployment will raise an error that is caused by the allow host.

![zappa_init03](./pic/zappa_init05.png)

- update the allow host

```py
ALLOWED_HOSTS = ['localhost', '127.0.0.1',
                 'cged6yb30f.execute-api.us-east-1.amazonaws.com']
```

- update the stage

```sh
zappa update django_lambda
```

![zappa_init03](./pic/zappa_init06.png)

- Visit url.

![zappa_init03](./pic/zappa_init07.png)

---

## Configure Domain Name and SSL

- Create custom Domain name in API

![dn](./pic/dn01.png)

- Update DNS record in Route 53

![dn](./pic/dn03.png)

![dn](./pic/dn02.png)

- Add parameters to json file

```json
{
  "stage_name": {
    "certificate_arn": "ACM_arn",
    "domain": "domain_name"
  }
}
```

- Run Certify

```sh
zappa certify django_lambda
```

![dn](./pic/dn04.png)

- Update allow host

```py
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'www.arguswatcher.net',
    'arguswatcher.net',
    'cged6yb30f.execute-api.us-east-1.amazonaws.com'
]
```

- Update stage

```sh
zappa update django_lambda
```

![dn](./pic/dn05.png)

- Visit Domain name

![dn](./pic/dn06.png)

---

[TOP](#document---deploy-django-project-on-lambda-using-zappa)
