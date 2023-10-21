---
layout: default
nav_order: 2
title: "Получение заказа"
parent: "Работа с заказом"
grand_parent: "Приём платежей"
---

# Получение заказа

Для получения списка заказов, необходимо вызвать следующий метод API:

- метод: `GET`
- ресурс: `/v3/filter/api/order/order`
- тело ответа - array of [OrderResponse](/docs/order/create/#orderresponse)

В запросе возможно применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору заказа
```
GET /v3/filter/api/order/order?id=01771534-196a-1105-839a-82422289d6d9
```
Пример запроса с фильтром по [статусу](/docs/order)
```
GET /v3/filter/api/order/order?status=completed
```

Пример запроса с фильтром по дате 
```
GET /v3/filter/api/order/order?expirationDate[_ge]=2021-01-27T00:00:00
```

Пример запроса с фильтром по идентификатору заказа в учётной системе магазина

```
GET /v3/filter/api/order/order?merchantOrderId=ORD123456
```

---

[Читать далее &raquo;](/docs/merchant/order/update){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
