---
layout: default
nav_order: 110
title: Создание заказа агентом
parent: "Работа с заказом"
grand_parent: "Приём платежей"
---

# Создание заказа с использованием реквизитов продавца

Для интеграции с банками и крупными платежными агрегаторамии (далее Агент) используется специальный режим сценария создания заказа, который не требуется идентификационные данные магазина Инвойсбокс, вместо них используется реквизиты юр. лица. Основное отличие заключается в:
- ИНН и КПП вместо идентифкатора магазина
- Авторизационные данные агента вместо авторизационных данных магазина


- метод: `POST`
- ресурс: `/v3/adapter/api/subagent/order`
- тело запроса - объект [CreateAgentOrderRequest](#createagentorderrequest)
- тело ответа - объект [OrderResponse](/docs/merchant/notification/status/#orderresponse)
- Возможные [ошибки](/docs/dictionary/error/)


<details>
  <summary>Пример запроса</summary>
<section markdown="1">
``` json
POST /v3/billing/api/order/order
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
Accept: application/json
{
  "seller": {
    "type": "counterparty",
    "vatNumber": "232323232323",
    "taxRegistrationReasonCode": "232323232323"
   },
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
      "measureCode": "796",
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
  "languageId": "ru",
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

## CreateAgentOrderRequest

Объект включает в себя все поля [CreateOrderRequest](/docs/merchant/order/create/#createorderrequest) а так же:

| Свойство | Обязательное | Тип               | Описание        | Пример значения                                                                                     |
|----------|--------------|-------------------|-----------------|-----------------------------------------------------------------------------------------------------|
| seller   | да           | [Saller](#saller) | Данные продавца | `{"type": "counterparty", "vatNumber":"232323232323", "taxRegistrationReasonCode": "232323232323"}` | 


## Saller

Повторяет свойства объекта [CreateOrderRequest](#createorderrequest) с дополнительными свойствами:

| Свойство                  | Обязательное | Тип        | Описание                                         | Пример значения |
|---------------------------|--------------|------------|--------------------------------------------------|-----------------|
| type                      | да           | string(36) | Тип продавца, доступные значения: `counterparty` | `counterparty`  |
| countryId                 | да           | string(3)  | Страна, доступные значения: `RUS`                | `RUS`           |
| vatNumber                 | да           | string(20) | ИНН                                              | `7710044140`    |
| taxRegistrationReasonCode | нет для ИП   | string(9)  | КПП                                              | `770201001`     |


Если продавец не найден в системе Инвойсбокс, то будет возвращена ошибка.
