---
layout: default
nav_order: 5
title: "Метаданные заказа"
parent: "Работа с заказом"
---

# Метаданные заказа

Передача расширенного набора данных по заказу осуществляется путём заполнения свойства заказа `metaData`
в запросе [создания заказа](/docs/order/create/). По умолчанию свойство заполняется в формате [json-ld](https://json-ld.org/).
Система поддерживат типы объектов, описанные на сайте [https://schema.org/](https://schema.org/).

## Данные бронирования авиабилетов

Для передачи данных бронирования авиаперелётов, в поле `metaData`
необходимо передать объект [ReservationPackage](https://schema.org/ReservationPackage) с перечнем
дочерних объектов [FlightReservation](https://schema.org/FlightReservation).


## Данные бронирования железнодорожных билетов

Для передачи данных бронирования авиаперелётов, в поле `metaData`
необходимо передать объект [ReservationPackage](https://schema.org/ReservationPackage) с перечнем
дочерних объектов [TrainReservation](https://schema.org/TrainReservation).

<details>
  <summary>Пример объекта ReservationPackage</summary>
<section markdown="1">
``` json
{
  "@type": "ReservationPackage",
  "subReservation": [
  {
    "@type": "[TrainReservation](https://schema.org/TrainReservation)",
    "bookingTime": "2021-05-15T12:22:01",
    "reservationId": "123456",
    "reservationStatus": "https://schema.org/ReservationConfirmed",
    "reservationFor": {
      "@type": "TrainTrip",
      "departureStation": {
        "@type": "TrainStation",
        "name": "Moscow Kievskyi"
      },
      "departureTime": "2021-06-04T10:30:00+01:00",
      "arrivalStation": {
        "@type": "TrainStation",
        "name": "St. Petersburg Central"
      },
      "arrivalTime": "2021-06-04T03:10:00+01:00"
    },
    "underName": {
      "@type": "Person",
      "name": "Сергей Иванов"
    },
    "provider": {
      "@type": "Organization",
      "name": "Sapsan"
    },
    "priceCurrency": "RUB",
    "totalPrice": 10564.00	
  }]
}
```
</section>
</details>


## Данные бронирования места проживания

Для передачи данных бронирования места проживания (отель, хостел, апартаменты и пр.), в поле `metaData`
необходимо передать объект [ReservationPackage](https://schema.org/ReservationPackage) с перечнем
дочерних объектов [LodgingReservation](https://schema.org/LodgingReservation).

<details>
  <summary>Пример объекта ReservationPackage</summary>
<section markdown="1">
``` json
{
  "@type": "ReservationPackage",
  "subReservation": [
  {
    "@type": "LodgingReservation",
    "reservationId": "YQVM18",
    "reservationStatus": "https://schema.org/ReservationConfirmed",
    "underName": {
      "@type": "Person",
      "name": "Андрей Макаров"
    },
    "reservationFor": {
      "@type": "LodgingBusiness",
      "name": "Гранд Отель Европа",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "ул. Михайловская, д. 1/7",
        "addressLocality": "Санкт-Петербург",
        "addressRegion": "Санкт-Петербург",
        "postalCode": "191186",
        "addressCountry": "RU"
      },
      "telephone": "+7 (812) 329-6000"
    },
    "checkinTime": "2021-02-21T16:00:00-08:00",
    "checkoutTime": "2021-02-23T11:00:00-08:00"
  }]
}
```
</section>
</details>

---

[Читать далее &raquo;](/docs/refund){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
