# hotels_catalogue

Функциональные части сервиса:
+ Регистрация пользователей/Аутентификация пользователей 
    Варианты реализации на выбор:
        + Форма регистрации;
        - Google авторизация;
- Админка. Стандартная админка Django. Разделы:
      + Стандартный раздел пользователей  
      + Админка Отелей с полями Id(primary key), Название отеля, Адрес, телефон, город из справочника(fk) :
          + Добавление/редактирование отеля;
          + Простая валидация емейл, телефона;
          + Нельзя добавить город не из справочника;
      + Справочник городов: Поля: Id(primary key), Название города:
          + Добавление/редактирование города;
  + Апи /api/hotels/?city_id=<city_id>&from_id=<hotle_id>&limit=<number>:
      + Возвращает список всех отелей отсортированных по id:
          + Список отелей в формате json;
          + city_id: Есть возможность фильтровать по городу если передан GET параметр;
          + from_id: Если передан GET параметр то все отели id которых больше указанного;
          + limit: Если передан GET параметр то вернуть не больше указанного числа;

Код в репозитории git.
+ Список всех зависимостей должен храниться в txt, соответственно можно установить их командой pip install -r requirements.txt.
+ Разработка должны вестись в virtualenv, но сама директория с virtualenv должна быть добавлена в .gitignore.
+ Можно использовать другой менеджер зависимостей, например pipenv или poetry вместо pip + requirements.txt
+ Должен быть Doсkerfile, который полностью собирает проект. Плюсом будет использование файла docker-compose.yml
+ Выбор базы на усмотрение, можно использовать sqlite или любую другую базу(Postgresql, Mysql) в этом случае хорошо иметь их в docker-compose.yml
+ Возможность создания структуры БД. То есть должны быть миграции, которые можно сделать через py migrate.
? Настройки должны храниться в py.
 
Задание со звездочкой. В проекте иметь балансер (nginx) через который будет осуществляться доступ к web сервису. Варианты реализации 
отдельно в docker-compose или внутри docker с использованием например circusd или любого другого менеджера процессов.
