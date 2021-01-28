---
layout: default
nav_order: 13
title: "Получение заказа"
permalink: /docs/order-get/
excerpt: "Find orders"
---
- метод: `GET`
- ресурс: `/a1/api/filter/order/order`
- тело ответа - array of [OrderResponse](/docs/order-create/#orderresponse)

Используя этот метод можно получить список заказов. Возможно применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору заказа
```
GET /a1/api/filter/order/order?id=01771534-196a-1105-839a-82422289d6d9
```
Пример запроса с фильтром по статусу
```
GET /a1/api/filter/order/order?status=completed
```

Пример запроса с фильтром по дате 
```
GET /a1/api/filter/order/order?expirationDate[_ge]=2021-01-27T00:00:00
```

Пример запроса с фильтром по идентификатору заказа в учетной системе магазина

```
GET /a1/api/filter/order/order?merchantOrderId=ORD123456
```

