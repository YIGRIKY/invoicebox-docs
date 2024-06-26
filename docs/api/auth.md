---
layout: default
title: "Авторизация"
nav_order: 10
parent: "Подключение к API"
date: 2023-11-23 00:00:00 +0300
---

# Авторизация

Для всех запросов к API обязательно должен присутствовать авторизационный токен, который можно получить после регистрации вашей организации в системе.

В зависимости от [версии биллинга](/docs/api) и API, которые вы используете, авторизационный токен будет выглядеть следующим образом:

Пример токена `v3`: `b37c4c689295904ed21eee5d9a48d42e` 

Пример токена `l3`: `29078-API:b37c4c689295904ed21eee5d9a48d42e` 

{: .important }
> Для проверки интеграции и методов, а также проведения тестовых платежей вы можете воспользоваться параметрами демонстрационного магазина:
>
> Токен: `b37c4c689295904ed21eee5d9a48d42e`
> 
> Идентификатор магазина: `ffffffff-ffff-ffff-ffff-ffffffffffff`

{: .warning }
> Авторизационный токен должен храниться в защищённом виде и месте. Используя токен, возможно получить доступ к методам API и данным от имени организации.
Токен не следует хранить в общедоступных местах или передавать третьим лицам. При возможной компрометации значения токена (если вы считаете, что токен мог быть получен третьими лицами),
вы должны незамедлительно изменить его в личном кабинете или сообщить об этом в [службу поддержки](https://www.invoicebox.ru/ru/contacts/feedback.html). 

Для проверки работы авторизации и корректности токена необходимо выполнить метод:

{: .tab-title .tabgroup-auth .tab-hide }
🌐 HTTP

{: .tab-content .tabgroup-auth .tab-hide }
```
GET /v3/security/api/auth/auth
Accept: application/json
User-Agent: MyApp 1.0
Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e
```

{: .tab-title .tabgroup-auth .tab-hide }
🧊 CURL

{: .tab-content .tabgroup-auth .tab-hide }
```
curl -L -X GET '{baseUrl}/v3/security/api/auth/auth' \
  -H 'Accept: application/json' \
  -H 'User-Agent: MyApp 1.0' \
  -H 'Authorization: Bearer b37c4c689295904ed21eee5d9a48d42e'
```

**{baseUrl}**{: .badge .badge-primary} - [базовый URL](/docs/api)


Если передан корректный токен, то ответ будет содержать HTTP код `200 OK` и идентификатор пользователя
<details>
  <summary>Пример ответа</summary>
<section markdown="1">
```json
{
  "data": {
    "userId": "01771533-8e75-3234-8e3d-9213ae2d7c52",
    "profile": null,
    "accessToken": null
  },
  "extendedData": []
}
```
</section>
</details>

Если передан некорректный токен, то ответ будет содержать HTTP код `401 Unauthorized` и ошибку
<details>
  <summary>Пример ответа</summary>
<section markdown="1">
```json
{
  "error": {
    "message": "Unauthorized",
    "code": "unauthorized"
  }
}
```
</section>
</details>

Если токен не передан, то ответ будет содержать HTTP код `200 OK` и информацию об анонимном пользователе
<details>
  <summary>Пример ответа</summary>
<section markdown="1">
```json
{
  "data": {
    "userId": null,
    "profile": null,
    "accessToken": null
  },
  "extendedData": []
}
```
</section>
</details>


---
[Читать далее &raquo;](/docs/api/filters){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }

