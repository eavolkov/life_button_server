Reference
==========

Socket соединение
-----------------
Формат команд: cmd_NAME [param1 [param2 ...]]

.. function:: cmd_id ID

  Передача ID устройства, с которым идет общение.

  .. warning::

    | Должна быть вызвана первой после соединения.
    | В противном случае вызов других команд закончится ошибкой.

  :param int ID: Идентификатор устройства (нумерация начинается с 0)

.. function:: cmd_location LAT LNG

  Передача текущих координат устройства.

  :param float LAT: Широта
  :param float LNG: Долгота

.. describe:: cmd_keepalive

  Подтверждение функционирования соединения



HTTP API
--------

.. function:: GET /device/<id>/locations

  Получение истории гео-позиций устройства

  :param int id: ID устройства

  Response:

  .. parsed-literal::
    [
      {lat: float, lng: float},
      ...
    ]

.. function:: GET /device/<id>/keepalive

  Получение отметок keepalive устройства

  :param int id: ID устройства

  Response:

  .. parsed-literal::
      [
        int, <- unix timestamp
        ...
      ]
