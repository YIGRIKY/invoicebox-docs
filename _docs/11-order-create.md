---
title: "Configuration"
permalink: /docs/order-create/
excerpt: "How to create order by API"
toc: true
---
Создание заказа:
- метод: `POST`
- ресурс: `/a1/api/order/order`
- тело запроса - объект [Order](#order)

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
  "subtype": "order",
  "expirationDate": "2020-12-22T00:00:00+00:00",
  "languageId": "RU",
  "originalCurrencyId": "RUB",
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

#### Order

| Свойство        | Тип                                 | Описание                                        | Пример значения |
| --------------- | ----------------------------------- | ----------------------------------------------- | ----------------|
| merchantId      | string                              | Идентификатор магазина                          | `01771534-1a57-f184-dee3-ebeb91dded76`
| merchantOrderId | string                              | Идентификатор заказа в учетной системе магазина | `01771534-1a57-f184-dee3-ebeb91dded76`
| amount          | float                               | Сумма заказа                                    | `19658.45`
| vatAmount       | float                               | Сумма НДС                                       | `156.56`
| subtype         | string                              | Тип заказа                                      | `order`
| expirationDate  | datetime                            | Срок действия заказа                            | `2020-12-22T00:00:00+00:00`
| basketItems     | array of [BasketItem](#basketitem)  | Состав заказа                                   | 
| metaData        | object                              |                                                 |
| languageId         | string             | Язык интерфейса платежной странцы | `RU`
| originalCurrencyId | string             | Валюта заказа                     | `RUB`
| description        | string             | Описание заказа                   | `Оплата номера в отеле`
| customer           | Customer           | Информация о заказчике            |

#### Customer - заказчик

| Свойство            | Тип                | Описание          | Пример значения |
| ------------------- | ------------------ | ----------------- | --------------- |
| type                | string             | Тип               | `private`, `public`
| name                | string             | Имя               | `Peter`
| phone               | string             | Номер телефона    | `79001112233`
| email               | string             | Электронная почта | `peter@domain.com`
| vatNumber           | string             | ИНН               | `7710044140`
| registrationAddress | string             | Юр. адресс        | `Невский 147`

#### BasketItem

| Свойство       | Тип      | Описание                      | Пример значения |
| -------------- | -------- | ----------------------------- | --------------- |
| sku            | string   | Артикул                       | `5fe0adcfa7fb4`
| name           | string   | Наименование                  | `Бронирование номера`
| measure        | string   | Единица измерения             | `шт.`
| measureCode    | int      | Код единицы измерения по ОКЕИ | `796`
| grossWeight    | float    | Вес брутто                    | `125.45`
| netWeight      | float    | Вес нетто                     | `125.45`
| quantity       | float    | Кол-во                        | `3`
| amount         | float    | Стоимость единицы             | `100.55`
| totalAmount    | float    | Стоимость всех единиц с НДС   | `123.55`
| totalVatAmount | float    | Сумма ндс всех позиций        | `23`
| vatCode        | enum     | Код процента НДС              | `RUS_VAT20`,`RUS_VAT10`
| type           | string   | Тип позиции                   | `service`
| paymentType    | string   | Тип оплаты                    | `full_prepayment`

