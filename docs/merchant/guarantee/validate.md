---
layout: default
nav_order: 20
title: "Проверка возможности оплаты"
parent: "Подтверждение оплаты"
grand_parent: "Приём платежей"
---

# Проверка возможности подтверждения оплаты

Для проверки возможности подтверждения оплаты заказа необходимо вызвать метод:

- метод: `POST`
- ресурс: `/v3/billing/api/order/{uuid}/payment-method-action/validate`
- тело запроса - объект [ValidateRequest](#validaterequest)
- тело ответа - объект [ValidateResponse](#validateresponse)
- Возможные [ошибки](/docs/dictionary/error/)

<details>
  <summary>Пример запроса и ответа</summary>
<section markdown="1">
``` json
POST /v3/billing/api/order/{uuid}/payment-method-action/validate
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
    "result": "available",
    "resultData": {
      "url": "",
      "method": "POST",
      "arguments": []
    }
  }
}
```
</section>
</details>



## ValidateRequest


| Свойство               | Обязательное | Тип                                      | Описание                                        | Пример     |
|------------------------|--------------|------------------------------------------|-------------------------------------------------|------------|
| paymentMethodId        | да           | string(36)                               | Идентификатор инструмента подтверждения оплаты  |            |
| languageId             | нет          | string(2) enum                           | Язык плательщика                                | `ru`, `en` |
| customer               | да           | [Customer](/docs/merchant/order/create/#customer) | Информация о плательщике               |            |


## ValidateResponse

| Свойство | Обязательное | Тип        | Описание                             |
|----------|--------------|------------|--------------------------------------|
| data     | да           | [PaymentResponse](/docs/merchant/guarantee/validate/#paymentresponse) | Информация об оплате  |

## PaymentResponse

| Свойство    | Обязательное | Тип        | Описание                    |
|-------------|--------------|------------|-----------------------------|
| result      | да           | enum       | Статус проверки (см. ниже)  |
| resultNote  | нет          | string     | Комментарий                 |


Возможные статусы:
  - notRegistered - Организация или ИП не зарегистрировано в системе
  - notEnoughMoney - Недостаточно средств для подтверждения оплаты заказа
  - available - Подтверждение оплаты заказа доступно


---

[Читать далее &raquo;](/docs/merchant/guarantee/code/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
