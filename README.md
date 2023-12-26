# Проект по автоматизации тестирования функционала сайта https://dima731515.github.io/hakaton/html/#

При проектировании автоматизированных тестов быд применен паттерн PageObject.

При тестировании сайта были написаны:
- тест-кейсы (https://docs.google.com/spreadsheets/d/1t_vDrEnZba9MkhRk5PK-fEUZyuljwlpfG3dgfApFZPs/edit?usp=sharing);
- баг-репорты;
- автоматизированные тесты.

Папка pages содержит следующие файлы:

- elements.py - функции для взаимодействия с элементами страницы сайта при проведении автотестов;
- base.py - функции для получения главной страницы сайта и пути текущей страницы;
- locators.py - функции для взаимодействия с url страницами и локаторы для элементов сайта;

Папка tests содержит файл:

- test_ui_positive.py - позитивные UI тесты;

Также проект содержит такие файлы, как:

- conftest.py - фикстуры для работы с браузером;
- pytest.ini - маркеры для параметризации;
- requirements.txt - используемые при тестировании библиотеки PyCharm.

Инструменты для тестирования: 
- PyCharm - воспроизведение автотестов;
- Google-таблица - тест-кейсы и баг-репорты;

Для подготовки к запуску автотестов необходимо установить необходимые библиотеки PyCharm с помощью вводимой команды в консоли терминала:

       pip install -r requirements.txt

Также необходимо скачать актуальную версию драйвера для вашего браузера для успешного прохождения автотестов.

Для запуска автотестов необходимо вводить команды в консоли терминала.

1. Для запуска всех тестов:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_ui_positive.py

2. Для тестов элементов сайта из хедера:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_ui_positive.py -v -m "header"

3. Для тестов элементов сайта из Main:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_ui_positive.py -v -m "main"

4. Для тестов элементов сайта из футера:

       python -m pytest -v --driver Chrome --driver-path <chromedriver_directory>\<chromedriver_file> tests\test_ui_positive.py -v -m "footer"

<chromedriver_directory>\<chromedriver_file> - путь к директории файла драйвера\название файла браузера. Например: C:\Chrome-selenium\chromedriver.exe

Окружение: Google Chrome Версия 120, Windows 11 Home (64 бит)
