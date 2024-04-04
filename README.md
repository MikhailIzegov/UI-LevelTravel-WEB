## <img width="5%" title="LevelTravel" src="images/screenshots/leveltravel.jpg"> Проект автотестов для WEB UI сайта level.travel

<!-- Технологии -->

## :gear: Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>
  <code><img width="5%" title="Python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
  <code><img width="5%" title="Pytest" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg"></code>
  <code><img width="5%" title="Poetry" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/poetry/poetry-original.svg"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
</p>

## :open_book: Описание
В проекте представлен один **высокоуровневый** смоук-тест всего бизнес-пути, написанный на Python + Selene (обёртка Selenium).  
  
По факту этот высокоуровневый тест может быть разбит на **множество низкоуровневых**, ведь частью общего "смоука" являются отдельные смысловые блоки такие как:  
- [x] Авторизация пользователя
- [x] Работа с календарём и выбором дат
- [x] Работа фильтров
- [x] Отдельные тесты каждой из страниц (главная, страницы с карточками отелей, страница отелей, чекаут-страница)
  
UI-тест на сайте `level.travel`  
  
Точка `A`: главная страница сайта 
  
Точка `B`: бронирование отеля (ввод карты, активация кнопки "забронировать")  
  
Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео и пр.)   
  
Шаги теста отображены в виде "аллюровских" степов через `with allure.step`    
  
Предполагалось, что Браузер в UI-тестах запускается удаленно в Selenoid (подключение к Jenkins), однако ресурсов учебного Selenoid не хватило для этого теста (см. раздел Jenkins).  

<!-- Jenkins -->

## <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск тестов из Jenkins

Как упоминалось в описании проекта, ресурсов учебного Selenoid оказалось мало для запуска довольно объёмного теста, о чем свидетельствует ошибка из `allure-отчета`:

<p><img src="images/screenshots/jenkins-error.jpg" alt="Jenkins"/></p>

В связи с этим предлагаю ознакомится с подключением к `Jenkins` и работой в связке с `Selenoid` (где удаленно запускаются тесты), `Allure` и `Telegram-notifications` в другом моём проекте: [API-tests project](https://github.com/MikhailIzegov/API_autotest)


<!-- Отчеты -->

## :bar_chart: Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке: 
```bash
allure serve 
```

### <img width="3%" title="Allure" src="images/logo/allure_report.png"> Allure

#### Примеры отображения тестов

<img src="images/screenshots/Allure-1.jpg" alt="Allure"/>

#### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.

<img src="images/screenshots/Allure-2.jpg" alt="Allure"/>
  
#### В конце каждого запуска браузер, прежде чем закрыться, сохраняет итоговый скриншот, который доступен в Allure вместе с другой информацией (логи, html и пр.):

<img src="images/screenshots/end-of-the-test.png" alt="Allure"/>
