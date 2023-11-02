---
layout: default
nav_order: 20
title: "Получение возвратов"
parent: "Работа с возвратом"
grand_parent: "Приём платежей"
date: 2023-10-25 00:00:00 +0300
---

# Получение списка возвратов

Для получения списка возвратов, необходимо вызвать следующий метод API:

- метод: `GET`
- ресурс: `/v3/filter/api/order/refund-order`
- тело ответа - array of [RefundOrderResponse](/docs/merchant/refund/create/#refundorderresponse)

Используя этот метод можно получить список возвратов. Возможно применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору возврата

```
GET /v3/filter/api/order/refund-order?id=01771534-196a-1105-839a-82422289d6d9
```

Пример запроса с фильтром по идентификатору заказа (в рамках которого осуществлялся возврат)

```
GET /v3/filter/api/order/refund-order?parentId=d6f1ccb2-2e32-43c2-8a42-5a835dd88607
```

Пример запроса возвратов с фильтром по [статусу](/docs/merchant/refund)

```
GET /v3/filter/api/order/refund-order?status=completed
```

Пример запроса возвратов с фильтром по идентификатору магазина

```
GET /v3/filter/api/order/refund-order?merchantId=2ce417f1-8702-4517-bb56-11cd305d2594
```

Пример запроса возвратов с фильтром по идентификатору заказа в учётной системе магазина 

```
GET /v3/filter/api/order/refund-order?merchantOrderId=ORD123456
```


---

[Читать далее &raquo;](/docs/merchant/refund/correction/){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }

