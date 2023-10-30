---
layout: default
title: "Работа в Postman"
nav_order: 100
parent: "Подключение к API"
date: 2023-10-25 00:00:00 +0300
---

# Работа в Postman

[Postman](https://www.postman.com/downloads/) — это инструмент для работы с API, который позволяет
отправлять запросы к сервисам и работать с их ответами. Для быстрого старта и упрощения работы,
вы можете импортировать коллекцию Инвойсбокс API в Postman. Коллекция - это набор готовых запросов
в соответствии с API.

Имеется как [десктопное приложение](https://www.postman.com/downloads/), так и [веб версия](https://www.postman.com)

Вы можете [скачать готовую коллекцию](https://www.postman.com/bold-space-873341/workspace/invoicebox-api-v3/collection/25303565-616ade6c-e654-4199-b80a-354e0592d5e2?action=share&creator=25303565)
(набор запросов) Инвойсбокс API или создать собственную.

1. Для начала работы с Postman, необходимо зарегистрироваться в сервисе. Для работы с API
достаточно бесплатной учётной записи — на ней будет ограничение до 1000 запросов в месяц.
   ![Postman](/assets/images/api/postman/1.jpg){: .img}

2. Далее, необходимо перейти в рабочее пространство и создать новую коллекцию
   ![Postman](/assets/images/api/postman/2.jpg){: .img}

3. Выберите blank collection
   ![Postman](/assets/images/api/postman/3.jpg){: .img}

4. Далее, для удобства нужно указать токен идентификации (магазина) для всей коллекции, чтобы не указывать его отдельно для каждого запроса
   ![Postman](/assets/images/api/postman/4.jpg){: .img}

5. Теперь возможно создать новый запрос
   ![Postman](/assets/images/api/postman/5.jpg){: .img}

6. Укажите метод, URL запроса, заполните заголовки и тело запроса
   ![Postman](/assets/images/api/postman/6.jpg){: .img}

---
[Читать далее &raquo;](/docs/merchant){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
