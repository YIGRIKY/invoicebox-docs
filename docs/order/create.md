---
layout: default
nav_order: 1
title: Создание заказа
parent: "Работа с заказом"
---

# Создание заказа

Для создания заказа, необходимо вызвать следующий метод API:

- метод: `POST`
- ресурс: `/a1/api/order/order`
- тело запроса - объект [CreateOrderRequest](#createorderrequest)
- тело ответа - объект [OrderResponse](#orderresponse)

<details>
  <summary>Пример запроса</summary>
<section markdown="1">
``` json
POST https://api.stage.k8s.invbox.ru/a1/api/order/order
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
Accept: application/json
{
  "merchantId": "01771534-196a-1105-839a-82422289d6d9",
  "merchantOrderId": "m-1608560079",
  "amount": 371.88,
  "successUrl": "https://merchant.ru/order/xxx?result=success",
  "failUrl": "https://merchant.ru/order/xxx?result=fail",
  "returnUrl": "https://merchant.ru/order/xxx?result=return",
  "vatAmount": 61.98,
  "basketItems": [
    {
      "sku": "5fe0adcfa7fb4",
      "name": "Бронирование номера",
      "measure": "шт.",
      "measureCode": 796,
      "grossWeight": 0,
      "netWeight": 0,
      "quantity": 3,
      "amount": 123.96,
      "amountWoVat": 103.3,
      "totalAmount": 371.88,
      "totalVatAmount": 61.98,
      "vatCode": "RUS_VAT20",
      "type": "service",
      "paymentType": "full_prepayment"
    }
  ],
  "metaData": {
    "@type": "LodgingReservation",
    "reservationId": "abc456",
    "reservationStatus": "https://schema.org/ReservationConfirmed",
    "underName": {
      "@type": "Person",
      "name": "John Smith"
    },
    "reservationFor": {
      "@type": "LodgingBusiness",
      "name": "Hilton San Francisco Union Square",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "333 O'Farrell St",
        "addressLocality": "San Francisco",
        "addressRegion": "CA",
        "postalCode": "94102",
        "addressCountry": "US"
      },
      "telephone": "415-771-1400"
    },
    "checkinTime": "2017-04-11T16:00:00-08:00",
    "checkoutTime": "2017-04-13T11:00:00-08:00"
  },
  "expirationDate": "2020-12-22T00:00:00+00:00",
  "languageId": "RU",
  "currencyId": "RUB",
  "description": "Оплата номера в отеле",
  "customer": {
    "type": "private",
    "name": "Peter",
    "phone": "79001112233",
    "email": "peter@domain.com",
    "vatNumber": "",
    "registrationAddress": ""
  }
}
```
</section>
</details>

## CreateOrderRequest

| Свойство        | Обязательное | Тип                                 | Описание                                              | Пример значения 
| --------------- | -------------|------------------------------------ | ----------------------------------------------------- | ----------------
| description     | да           | string                              | Описание заказа                                       | `Оплата номера в отеле`
| merchantId      | да           | string                              | Идентификатор магазина                                | `01771534-1a57-f184-dee3-ebeb91dded76`
| merchantOrderId | да           | string                              | Идентификатор заказа в учетной системе магазина       | `O-12345`
| amount          | да           | float                               | Сумма заказа                                          | `19658.45`
| vatAmount       | да           | float                               | Сумма НДС                                             | `156.56`
| currencyId      | да           | string enum                         | Валюта заказа                                         | `RUB`
| languageId      | нет          | string enum                         | Язык интерфейса платежной страницы                    | `RU`, `EN`
| expirationDate  | да           | datetime                            | Срок действия заказа                                  | `2020-12-22T00:00:00+00:00`
| basketItems     | да           | array of [BasketItem](#basketitem)  | Состав заказа                                         |
| metaData        | нет          | object                              | [Дополнительные данные заказа](/docs/order/metadata/) |
| customer        | да           | [Customer](#customer)               | Информация о плательщике                              |
| successUrl      | нет          | string                              | Ссылка для перехода на сайт Магазина в случае успешной оплаты |
| failUrl         | нет          | string                              | Ссылка для перехода на сайт Магазина в случае ошибки оплаты   |
| returnUrl       | нет          | string                              | Ссылка для возврата на сайт Магазина                          |


## OrderResponse

Повторяет свойства объекта [CreateOrderRequest](#createorderrequest) с дополнительными свойствами: 

| Свойство        | Обязательное | Тип         | Описание                                                | Пример значения
| --------------- | -------------|------------ | ------------------------------------------------------- | ----------------
| id              | да           | string      | Идентификатор заказа в системе InvoiceBox               | `01771534-1a57-f184-dee3-ebeb91dded75`
| paymentUrl      | да           | string      | Ссылка для перехода на платежный шлюз для оплаты заказа |
| createdAt       | да           | datetime    | Дата создания заказа                                    | `2020-12-22T00:00:00+00:00`
| status          | да           | string enum | Статус заказа                                           | `completed`

## Customer

| Свойство            | Обязательное | Тип                | Описание          | Пример значения 
| ------------------- | ------------ | ------------------ | ----------------- | --------------- 
| type                | да           | string enum        | Тип плательщика   | `private` - юр. лицо, `public` - физ лицо
| name                | да           | string             | Имя               | `Peter`
| phone               | да           | string             | Номер телефона    | `79001112233`
| email               | да           | string             | Электронная почта | `peter@domain.com`
| vatNumber           | да           | string             | ИНН               | `7710044140`
| registrationAddress | да           | string             | Юр. адресс        | `190000, Санкт-Петербург, Невский пр. 147, офис 321`

## BasketItem

| Свойство       |  Обязательное |Тип      | Описание                      | Пример значения 
| -------------- | ------------- | ------- | ----------------------------- | --------------- 
| sku            | да            | string  | Артикул                       | `5fe0adcfa7fb4`
| name           | да            | string  | Наименование                  | `Бронирование номера`
| measure        | да            | string  | Единица измерения             | `шт.`
| measureCode    | да            | int     | Код единицы измерения по ОКЕИ | `796`
| grossWeight    | да            | float   | Вес брутто                    | `125.45`
| netWeight      | да            | float   | Вес нетто                     | `125.45`
| quantity       | да            | float   | Кол-во                        | `3`
| amount         | да            | float   | Стоимость единицы             | `100.55`
| totalAmount    | да            | float   | Стоимость всех единиц с НДС   | `123.55`
| totalVatAmount | да            | float   | Сумма ндс всех позиций        | `23`
| vatCode        | да            | enum    | Код процента НДС              | `RUS_VAT20`,`RUS_VAT10`
| type           | да            | string  | Тип позиции                   | `service`
| paymentType    | да            | string  | Тип оплаты                    | `full_prepayment`


[Читать далее](/docs/order/get){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
