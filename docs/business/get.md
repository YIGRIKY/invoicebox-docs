---
layout: default
nav_order: 20
title: "Получение счёта"
parent: "Инвойсбокс.Бизнес"
date: 2024-01-30 00:00:00 +0300
---

# Получение счёта

Для получения списка счетов, необходимо вызвать следующий метод API:

- метод: `GET`
- ресурс: `/v3/business/api/invoice` или `/v3/business/api/invoice/{invoiceId}`
- тело ответа - array of [InvoiceResponse](/docs/business/get/#invoiceresponse)

Пример запроса с идентификатором счёта
```
GET /v3/business/api/invoice/01771534-196a-1105-839a-82422289d6d9
```

В запросе возможно применения фильтров и сортировок.

Пример запроса с фильтром по идентификатору счёта
```
GET /v3/business/api/invoice?id=01771534-196a-1105-839a-82422289d6d9
```

Пример запроса с фильтром по идентификатору заказа Магазина
```
GET /v3/business/api/invoice?merchantOrderId=ABCDE
```

или по номеру заказа, который видит плательщик

```
GET /v3/business/api/invoice?merchantOrderIdVisible=ABCDE
```

Пример запроса с фильтром по статусу
```
GET /v3/business/api/invoice?status=paid
```

## InvoiceResponse

| Свойство       | Обязательное | Тип                       | Описание                                                                | Пример значения                        |
|----------------|--------------|---------------------------|-------------------------------------------------------------------------|----------------------------------------|
| id             | да           | string(36)                | Идентификатор счёта                                                     | `01771534-1a57-f184-dee3-ebeb91dded76` |
| number         | да           | string(50)                | Номер счёта                                                             | `123-123212`                           |
| createdAt      | да           | datetime                  | Дата создания счёта                                                     | `2023-12-22T00:00:00+00:00`            |
| expirationDate | да           | datetime                  | Срок оплаты счёта                                                       | `2023-12-25T00:00:00+00:00`            |
| description    | да           | string(1000)              | Описание счёта                                                          | `Оплата номера в отеле`                |
| amount         | да           | float                     | Сумма счёта (к оплате)                                                  | `19658.45`                             |
| vatAmount      | да           | float                     | Сумма НДС в счёте                                                       | `156.56`                               |
| currencyId     | да           | string(3) enum            | Код валюты счёта в соответствии с [ISO 4217](/docs/dictionary/iso4217/) | `RUB`, `USD`,`EUR`, `GBP`              |
| customer       | да           | [Customer](#customer)     | Информация о плательщике                                                |                                        |
| status         | нет          | string(50) enum           | Статус оплаты счёта (paid, pending, canceled, partial)                  | `paid`                                 |
| paymentUrl     | да           | string(1000)              | Ссылка для перехода на платёжный шлюз на страницу счёта                 |                                        |

## Customer

| Свойство            | Обязательное | Тип             | Описание          | Пример значения                                      |
|---------------------|--------------|-----------------|-------------------|------------------------------------------------------|
| type                | нет          | string(10) enum | Тип заказчика     | `legal` - юр. лицо, `private` - физ лицо             |
| name                | нет          | string(500)     | Имя               | `Peter`                                              |
| phone               | нет          | string(100)     | Номер телефона    | `79001112233`                                        |
| email               | нет          | string(100)     | Электронная почта | `peter@domain.com`                                   |
| vatNumber           | нет          | string(20)      | ИНН               | `7710044140`                                         |
| registrationAddress | нет          | string(1000)    | Юр. адресс        | `190000, Санкт-Петербург, Невский пр. 147, офис 321` |

---

[Читать далее &raquo;](/docs/business/confirm_payment){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
