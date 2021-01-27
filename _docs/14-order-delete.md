---
title: "Отмена заказа"
permalink: /docs/order-delete/
excerpt: "Cancel order"
---

После создания заказа и до момента его оплаты имеется возможность отменить заказ.
Редактирование заказа:
- метод: `DELETE`
- ресурс: `/a1/api/order/order/:uuid` - где `:uuid` это идентификатор заказа
- тело запроса - отсутствует
- тело ответа - объект [OrderResponse](/docs/order-create/#orderresponse) со статусом `canceled`
