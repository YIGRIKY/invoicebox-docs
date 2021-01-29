---
layout: default
nav_order: 4
title: "Отмена заказа"
parent: "Работа с заказом"
---

# Отмена заказа

После создания заказа и до момента его оплаты имеется возможность отменить заказ.
Редактирование заказа:
- метод: `DELETE`
- ресурс: `/a1/api/order/order/:uuid` - где `:uuid` это идентификатор заказа
- тело запроса - отсутствует
- тело ответа - объект [OrderResponse](/docs/order/create/#orderresponse) со статусом `canceled`

[Читать далее](/docs/order/metadata){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
