---
layout: default
nav_order: 30
title: "Запрос кода подтверждения"
parent: "Подтверждение оплаты"
grand_parent: "Приём платежей"
date: 2023-10-25 00:00:00 +0300
---

# Запрос кода подтверждения

Для запроса и отправки кода подтверждения покупателю необходимо вызвать метод:

- метод: `POST`
- ресурс: `/v3/billing/api/order/{uuid}/payment-method-action/send-code`
- тело запроса - объект [CodeRequest](#coderequest)
- тело ответа - объект [CodeResponse](#coderesponse)
- Возможные [ошибки](/docs/dictionary/error/)

<details>
  <summary>Пример запроса и ответа</summary>
<section markdown="1">
``` json
POST /v3/billing/api/order/{uuid}/payment-method-action/send-code
{
  "paymentMethodId": "39363265",
  "languageId": "ru",
  "customer": {
    "name": "ООО Компания",
    "email": "email@gmail.com",
    "type": "legal",
    "phone": "79611234567",
    "vatNumber": "1233123",
    "registrationAddress": "123123123"
  }
}
```
</section>
<section markdown="1">
``` json
{
  "data": {
    "type": "none",
    "result": "success",
    "resultData": {
      "publicCode": "aaaaaaa123",
      "leftAttempt" : 5
    }
  }
}
```
</section>
</details>



## CodeRequest

| Свойство               | Обязательное | Тип                                      | Описание                                        | Пример     |
|------------------------|--------------|------------------------------------------|-------------------------------------------------|------------|
| paymentMethodId        | да           | string(36)                               | Идентификатор инструмента подтверждения оплаты  |            |
| languageId             | нет          | string(2) enum                           | Язык плательщика                                | `ru`, `en` |
| customer               | да           | [Customer](/docs/merchant/order/create/#customer) | Информация о плательщике               |            |


## CodeResponse

| Свойство | Обязательное | Тип        | Описание                             |
|----------|--------------|------------|--------------------------------------|
| data     | да           | [PaymentResponse](/docs/merchant/guarantee/code/#paymentresponse) | Информация об оплате  |

## PaymentResponse

| Свойство    | Обязательное | Тип        | Описание                                     |
|-------------|--------------|------------|----------------------------------------------|
| type        | да           | enum       | Тип действия: none                           |
| result      | да           | enum       | Статус проверки (см. ниже)                   |
| resultData  | да           | object     | [Code](/docs/merchant/guarantee/code/#code)  |

Возможные статусы:
  - error - ошибка
  - codeAlreadySent - код уже был отправлен ранее, срок повторной отправки кода не истёк
  - success - успешно


## Code

| Свойство    | Обязательное | Тип        | Описание                                    |
|-------------|--------------|------------|---------------------------------------------|
| publicCode  | да           | string     | Публичный идентификатор кода                |
| leftAttempt | да           | int        | Количество оставшихся попыток отправки кода |


---

[Читать далее &raquo;](/docs/merchant/guarantee/pay/){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
