---
layout: default
title: "Подключение к WebSocket"
nav_order: 25
parent: "Подключение к API"
---

# Подключение к WebSocket

Инвойсбокс API поддерживает работу с веб-сокетами, для случаев, когда необходимо получить уведомление об
изменении статуса заказа (оплате) без наличия публичного сервиса, по которому система Инвойсбокс
могла бы передать такое уведомление.

### Точка подключения

Основной адрес: `ws-gate.invoicebox.ru`

При подключении авторизационный токен передается в query параметре token, например,
`wss://ws-gate.invoicebox.ru/v3/gate/rpc?token=b37c4c689295904ed21eee5d9a48d42e`

### Обработка уведомления об оплате заказа

После поступления оплаты по заказу, при условии наличия активного WebSocket соединения с системой Инвойсбокс,
система Инвойсбокс вызовет метод onOrderStatusChange() с аргументом в виде объекта [OrderNotification](/docs/merchant/notification/status/#ordernotification)

<details>
  <summary>Пример уведомления</summary>
<section markdown="1">
``` json
{
  "jsonrpc" : "2.0",
  "id" : "01823fdac4b7a7b5a3ac",
  "method" : "onOrderStatusChange",
  "params": [
    {
      "id" : "01823fda-667f-6ddb-02a3-c4b7a7b5a3ac",
      "description" : "Описание заказа",
      "currencyId" : "RUB",
      "amount" : 1487.52,
      "vatAmount" : 247.92,
      "basketItems" : [
      ],
      "merchantId" : "0302756d-9d83-60c9-0356-c228562c7581",
      "status" : "completed",
      "subtype" : "order",
      "createdAt" : "2023-07-27T13:30:53+00:00",
      "merchantOrderId" : "1658928653",
      "expirationDate" : "2023-07-29T00:00:00+00:00",
      "metaData" : {
         "@type" : "LodgingReservation",
         "name" : "park inn"
      },
      "fileIds" : {
      }
    }
  ]
}```
</section>
</details>


---
[Читать далее &raquo;](/docs/api/debug){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }


{: .fs-6 .fw-300 }
