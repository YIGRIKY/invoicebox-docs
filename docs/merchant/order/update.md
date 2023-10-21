---
layout: default
nav_order: 3
title: "Изменение заказа"
parent: "Работа с заказом"
grand_parent: "Приём платежей"
---

Изменить заказ возможно только до момента его оплаты.
Для изменения заказа, необходимо вызвать следующий метод API:

- метод: `PUT`
- ресурс: `/v3/billing/api/order/order/:uuid` - где `:uuid` это идентификатор заказа 
- тело запроса - объект [UpdateOrderRequest](#updateorderrequest)
- тело ответа - объект [OrderResponse](/docs/merchant/order/create/#orderresponse)


## UpdateOrderRequest

| Свойство       | Обязательное | Тип                                                   | Описание                                                  | Пример значения                         |
|----------------|--------------|-------------------------------------------------------|-----------------------------------------------------------|-----------------------------------------|
| description    | нет          | string                                                | Описание заказа                                           | `Оплата номера в отеле`                 |
| amount         | нет          | float                                                 | Сумма заказа                                              | `19658.45`                              |
| vatAmount      | нет          | float                                                 | Сумма НДС                                                 | `156.56`                                |
| expirationDate | нет          | datetime                                              | Срок действия заказа                                      | `2020-12-22T00:00:00+00:00`             |
| basketItems    | нет          | array of [BasketItem](/docs/merchant/order/create/#basketitem) | Корзина заказа                                            |                                         |
| metaData       | нет          | object                                                | [Дополнительные данные заказа](/docs/merchant/order/metadata/)     |                                         |
| customer       | нет          | [Customer](/docs/merchant/order/create/#customer)              | Информация о заказчике                                    |                                         |
| shopId         | нет          | string(36)                                            | Идентификатор связанного магазина/маркетплейса            | `06581534-196a-1105-839a-82422289d6d9`  |

---

[Читать далее &raquo;](/docs/merchant/order/delete){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
