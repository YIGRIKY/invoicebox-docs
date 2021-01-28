---
layout: default
nav_order: 6
title: "Изменение статуса заказа"
parent: Работа с заказом
---

Если активирована данная опция, то при поступлении оплаты заказа InvoiceBox осуществит запрос на специальный URL, который прописан в настройках магазина с данными о статусе заказа.
На указанный URL будет осуществлен `POST` запрос в теле которого будет находится объект [OrderResponse](/docs/order-create/#orderresponse). При обработке данного запроса необходимо проверять статус заказа, при успешной оплате он будет равен `completed`