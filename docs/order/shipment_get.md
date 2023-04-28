---
layout: default
nav_order: 2
title: "Получение отгрузки"
parent: "Работа с отгрузками"
---

# Получение отгрузки

Для получения списка отгрузок, необходимо вызвать следующий метод API:

- метод: `GET`
- ресурс: `/v3/filter/api/order/shipment`
- тело ответа - array of [ShipmentResponse](/docs/order/shipment_create/#shipmentresponse)

В запросе возможно применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору отгрузки
```
GET /v3/filter/api/order/shipment?id=371723
```
Пример запроса с фильтром по id заказа
```
GET /v3/filter/api/order/order?orderId=01771534-196a-1105-839a-82422289d6d9
```

Пример запроса с фильтром по id магазина
```
GET /v3/filter/api/order/order?merchantId=21827364-196a-1178-839a-82469489d6d7
```

---

{: .fs-6 .fw-300 }
