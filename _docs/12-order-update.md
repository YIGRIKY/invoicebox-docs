---
title: "Редактирование заказа"
permalink: /docs/order-update/
excerpt: "Instructions on how to customize the theme's default set of layouts, includes, and stylesheets when using the Ruby Gem version."
---
После создания заказа и до момента его оплаты имеется возможность модифицировать данные заказа.
Редактирование заказа:
- метод: `PUT`
- ресурс: `/a1/api/order/order/:uuid` - где `:uuid` это идентификатор заказа 
- тело запроса - объект [UpdateOrderRequest](#updateorderrequest)
- тело ответа - объект [OrderResponse](/docs/order-create/#OrderResponse)


#### UpdateOrderRequest

| Свойство        | Обязательное | Тип                                 | Описание                                              | Пример значения
| --------------- | -------------|------------------------------------ | ----------------------------------------------------- | ----------------
| description     | нет          | string                              | Описание заказа                                       | `Оплата номера в отеле`
| amount          | нет          | float                               | Сумма заказа                                          | `19658.45`
| vatAmount       | нет          | float                               | Сумма НДС                                             | `156.56`
| expirationDate  | нет          | datetime                            | Срок действия заказа                                  | `2020-12-22T00:00:00+00:00`
| basketItems     | нет          | array of [BasketItem](/docs/order-create/#basketitem)  | Состав заказа                      |
| metaData        | нет          | object                              | [Дополнительные данные заказа](/docs/order-metadata/) |
| customer        | нет          | [Customer](/docs/order-create/#customer)               | Информация о плательщике           |
