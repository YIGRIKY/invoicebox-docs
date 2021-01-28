---
layout: default
nav_order: 4
title: "Отмена заказа"
parent: "Работа с заказом"
---

После создания заказа и до момента его оплаты имеется возможность отменить заказ.
Редактирование заказа:
- метод: `DELETE`
- ресурс: `/a1/api/order/order/:uuid` - где `:uuid` это идентификатор заказа
- тело запроса - отсутствует
- тело ответа - объект [OrderResponse](/docs/order-create/#orderresponse) со статусом `canceled`
