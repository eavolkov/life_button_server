# LifeButton сервер
Документация: http://lifebutton-server.readthedocs.io/en/latest/

## Pre-requirements
* [Install pipenv](https://github.com/pypa/pipenv)  
* [Install mongodb](https://docs.mongodb.com/manual/administration/install-on-linux/)

## Запуск
```
pipenv shell # Активация shell'a (автоматически установит в виртуальное окружение все необходимые пакеты)
python app.py # Запуск сервера
```
Все настройки вынесены в settings.py

## Документация
В docs/ выполнить `make html`.   
В папке docs/_build/html будут собранные html документации.  
