---
title: "Получение возвратного заказа"
permalink: /docs/refund-order-get/
excerpt: "Find refund orders"
toc: true
---
- метод: `GET`
- ресурс: `/a1/api/filter/order/refund-order`
- тело ответа - array of [RefundOrderResponse](/docs/refund-order-create/#refundorderresponse)

Используя этот метод можно получить список возвратных заказов. Возможно применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору заказа
```http request
GET /a1/api/filter/order/refund-order?id=01771534-196a-1105-839a-82422289d6d9
```
Пример запроса с фильтром по статусу
```http request
GET /a1/api/filter/order/refund-order?status=completed
```

Пример запроса с фильтром по дате 
```http request
GET /a1/api/filter/order/refund-order?merchantOrderId=ORD123456
```
