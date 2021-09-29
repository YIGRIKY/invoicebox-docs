---
layout: default
nav_order: 3
title: "Изменение заказа"
parent: "Работа с заказом"
---

Изменить заказ возможно только до момента его оплаты.
Для изменения заказа, необходимо вызвать следующий метод API:

- метод: `PUT`
- ресурс: `/v3/billing/api/order/order/:uuid` - где `:uuid` это идентификатор заказа 
- тело запроса - объект [UpdateOrderRequest](#updateorderrequest)
- тело ответа - объект [OrderResponse](/docs/order/create/#orderresponse)


## UpdateOrderRequest

| Свойство        | Обязательное | Тип                                 | Описание                                              | Пример значения
| --------------- | -------------|------------------------------------ | ----------------------------------------------------- | ----------------
| description     | нет          | string                              | Описание заказа                                       | `Оплата номера в отеле`
| amount          | нет          | float                               | Сумма заказа                                          | `19658.45`
| vatAmount       | нет          | float                               | Сумма НДС                                             | `156.56`
| expirationDate  | нет          | datetime                            | Срок действия заказа                                  | `2020-12-22T00:00:00+00:00`
| basketItems     | нет          | array of [BasketItem](/docs/order/create/#basketitem)  | Корзина заказа                     |
| metaData        | нет          | object                              | [Дополнительные данные заказа](/docs/order/metadata/) |
| customer        | нет          | [Customer](/docs/order/create/#customer)               | Информация о заказчике             |

---

[Читать далее &raquo;](/docs/order/delete){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
