---
title: "Получение заказа"
permalink: /docs/order-get/
excerpt: "Find orders"
toc: true
---
- метод: `GET`
- ресурс: `/a1/api/filter/order/order?expirationDate[_ge]=2021-01-27T00:00:00`
- тело ответа - array of [OrderResponse](/docs/order-create/#OrderResponse)

Используя этот метод можно получить список заказов, с возможностью применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору заказа
```http request
GET /a1/api/filter/order/order?id=01771534-196a-1105-839a-82422289d6d9
```
Пример запроса с фильтром по статусу
```http request
GET /a1/api/filter/order/order?status=completed
```

Пример запроса с фильтром по дате 
```http request
GET /a1/api/filter/order/order?expirationDate[_ge]=2021-01-27T00:00:00
```
