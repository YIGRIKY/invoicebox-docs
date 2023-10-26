---
layout: default
nav_order: 20
title: "Активация магазина по коду"
parent: "Партнёрское API"
date: 2023-10-26 00:00:00 +0300
---

# Активация магазина по коду

Партнёр может активировать магазин и его интеграцию по специальному коду.

Для активации магазина и получения параметров интеграции, отправьте следующий запрос:

- метод: `POST`
- ресурс: `/v3/billing/api/merchant/merchant-integration-setting/activation`
- тело запроса - объект [ActivationRequest](#activationrequest)
- тело ответа - объект [ActivationResponse](#activationresponse)
- Возможные [ошибки](/docs/dictionary/error/)


<details>
  <summary>Пример запроса и ответа</summary>
<section markdown="1">
``` json
POST /v3/billing/api/merchant/merchant-integration-setting/activation
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
User-Agent: MyApp 1.0
Accept: application/json
{
   "activationCode":"111222333",
   "partnerId":"dda90c3d-e2f8-4f90-aa8b-87b1cd2956a1"
}
```
</section>
<section markdown="1">
``` json
{
   "data":{
      "merchantId":"ffffffff-ffff-ffff-ffff-ffffffffffff",
      "token":"T1RBMFpXKOAY8W45072Wa09XRTBPR1EwTW1V"
   }
}
```
</section>
</details>

## ActivationRequest

| Свойство        | Обязательное | Тип             | Описание                             | Пример значения                        |
|-----------------|--------------|-----------------|--------------------------------------|----------------------------------------|
| partnerId       | да           | string(36)      | Идентификатор партнёра (интегратора) | `01771534-1a57-f184-dee3-ebeb91dded76` |
| activationCode  | да           | string(36)      | Код активации магазина               | `143232423434`                         |

## ActivationResponse

| Свойство        | Обязательное | Тип          | Описание                     | Пример значения                        |
|-----------------|--------------|--------------|------------------------------|----------------------------------------|
| merchantId      | да           | string(36)   | Идентификатор магазина       | `01771534-1a57-f184-dee3-ebeb91dded76` |
| token           | да           | string(512)  | Токен магазина               | `T1RBMFpXKOAY8W45072Wa09XRTBPR1EwTW1V` |


---

[Читать далее &raquo;](/docs/dictionary){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }

