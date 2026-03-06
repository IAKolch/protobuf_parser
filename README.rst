Protobuf Stream Parser
======================

Библиотека для парсинга потока length-prefixed Protobuf сообщений, где каждое сообщение предваряется размером, закодированным как Varint32. Реализована поддержка буферизации для обработки произвольных фрагментов данных (часть сообщения, несколько сообщений сразу) с использованием _DecodeVarint32 из стандартной библиотеки protobuf. Код универсален и не зависит от конкретного протокола (работает с любым классом, наследующим Message), включает автогенерацию кода из .proto файлов при сборке и покрыт тестами.

Требования
==========

Python 3.8+

protobuf-compiler (protoc) для генерации кода

Виртуальное окружение
===================

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate # Unix
    venv\Scripts\activate # Windows
    pip install -r requirements.txt

Build
-----

.. code-block:: bash

    python3 setup.py build

Запуск тестов
-------------

.. code-block:: bash

    python3 -m unittest discover tests
