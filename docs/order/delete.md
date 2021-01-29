---
layout: default
nav_order: 4
title: "Отмена заказа"
parent: "Работа с заказом"
---

# Отмена заказа

Отменить заказ возможно только до момента его оплаты.
Для отмены заказа, необходимо вызвать следующий метод API:

- метод: `DELETE`
- ресурс: `/a1/api/order/order/:uuid` - где `:uuid` это идентификатор заказа
- тело запроса - отсутствует
- тело ответа - объект [OrderResponse](/docs/order/create/#orderresponse) со статусом `canceled`

[Читать далее](/docs/order/metadata){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
