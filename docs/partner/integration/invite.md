---
layout: default
nav_order: 10
title: "Отправка приглашения"
parent: "Партнёрское API"
date: 2023-10-26 00:00:00 +0300
---

# Отправка приглашения

Партнёр может инициировать отправку приглашения для регистрации в системе Инвойсбокс.

При успешном выполнении запроса на указанный адрес электронной почты будет отправлена ссылка для
регистрации в системе Инвойсбокс. После успешной регистрации и оформления договора, пользователь
получит код для активации для настройки своего магазина.

Для отправки приглашения, отправьте следующий запрос:

- метод: `POST`
- ресурс: `/v3/notification/api/invite`
- тело запроса - объект [InviteRequest](#inviterequest)
- тело ответа - объект [InviteResponse](#inviteresponse)
- Возможные [ошибки](/docs/dictionary/error/)


<details>
  <summary>Пример запроса и ответа</summary>
<section markdown="1">
``` json
POST /v3/notification/api/invite
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
Content-Type: application/json
User-Agent: MyApp 1.0
Accept: application/json
{
   "identifier": "shop@shop.com",
   "type": "email",
   "partnerId": "ffffffff-ffff-ffff-ffff-ffffffffffff"
}
```
</section>
<section markdown="1">
``` json
{
   "data":{
      "id":"d5490c3d-e2f8-4f90-aa8b-87b1cd2956af"
   }
}
```
</section>
</details>

## InviteRequest

| Свойство        | Обязательное | Тип             | Описание                                                            | Пример значения                        |
|-----------------|--------------|-----------------|---------------------------------------------------------------------|----------------------------------------|
| partnerId       | да           | string(36)      | Идентификатор партнёра (интегратора)                                | `01771534-1a57-f184-dee3-ebeb91dded76` |
| type            | да           | enum            | Тип приглашения                                                     | `email` |
| identifier      | да           | string(100)     | Значение приглашения                                                | `shop@shop.com` |

## InviteResponse


| Свойство                  | Обязательное | Тип   | Описание                     | Пример значения |
|---------------------------|--------------|-------|------------------------------|-----------------|
| id                        | да           | int   | Идентификатор приглашения    | `123`           |



---

[Читать далее &raquo;](/docs/partner/activation/){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }

