Масштабирование
===============

Т.к. выбранная БД масштабируема из коробки, вопрос масштабируемости связан лишь с производительностью backend кода.

Stateless
---------
Код проекта необходимо поддерживать в stateless состоянии (код не использует какие-то кастомные файлы и т.п. и может быть запущен в любом количестве на любом кол-ве серверов)


SCM
---
Для осуществления быстрого запуска новых нод проекта необходима система управления конфигурацией (SCM) - Ansible

Оркестрация
-----------
Consul поднимает нужное кол-во нод проекта, балансирует между ними трафик.

