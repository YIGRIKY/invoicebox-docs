---
layout: default
nav_order: 100
title: "Метаданные"
parent: "Работа с заказом"
grand_parent: "Приём платежей"
date: 2023-11-02 00:00:00 +0300
---

# Метаданные заказа/элемента корзины

Передача расширенного набора данных по заказу или элементу корзины осуществляется путём заполнения свойства заказа или элемента
корзины `metaData` в запросе [создания заказа](/docs/merchant/order/create/) и [оформления возврата](/docs/merchant/refund/create/).
По умолчанию, свойство заполняется в формате [json-ld](https://json-ld.org/). Система поддерживат типы объектов, описанные на
сайте [https://schema.org/](https://schema.org/).

## Данные бронирования авиабилетов

Для передачи данных бронирования авиаперелётов, в поле заказа `metaData`
необходимо передать объект [ReservationPackage](https://schema.org/ReservationPackage) с перечнем
дочерних объектов [FlightReservation](https://schema.org/FlightReservation). Для каждого из сегментов полёта,
а также для каждого из пассажиров передаётся отдельный объект [FlightReservation](https://schema.org/FlightReservation).

<details>
  <summary>Пример объекта ReservationPackage</summary>
<section markdown="1">
``` json
{
  "@type": "ReservationPackage",
  "subReservation": [
  {
    "@type": "FlightReservation",
    "reservationId": "YQVM18",
    "reservationStatus": "https://schema.org/ReservationConfirmed",
    "underName": {
      "@type": "Person",
      "name": "Андрей Макаров"
    },
    "reservationFor": {
      "@type": "Flight",
      "flightNumber": "NDJ37S",
      "provider": {
        "@type": "Airline",
        "name": "Aeroflot",
        "iataCode": "SU"
      },
      "seller": {
        "@type": "Airline",
        "name": "Aeroflot",
        "iataCode": "SU"
      },
      "departureAirport": {
        "@type": "Airport",
        "name": "Москва (Шерементьево)",
        "iataCode": "SVO"
      },
      "departureTime": "2022-03-04T20:15:00+03:00",
      "departureGate": "11",
      "departureTerminal": "C",
      "arrivalAirport": {
        "@type": "Airport",
        "name": "Санкт-Петербург (Пулково)",
        "iataCode": "LED"
      },
      "arrivalTime": "2022-03-05T21:30:00+03:00",
      "arrivalGate": "11",
      "arrivalTerminal": "1"
    },
    "airplaneSeat": "1A",
    "airplaneSeatClass": {
      "@type": "AirplaneSeatClass",
      "name": "Business"
    },
    "ticketNumber": "111-1231231239",
    "ticketToken": "qrCode:AB34",
    "checkinUrl": "https://checkmytrip.ru/onlinecheckin.html",
    "reservedTicket": {
      "@type": "flightTicket",
      "underName": {
        "@type": "Person",
        "name": "MAKAROV ANDREY"
      },
      "fareBase": 57.00,
      "fareReservation": 66.40,
      "vatValue": [{
          "vatCode": "RUS_VAT0",
          "totalVatAmount": 0.00
      },
      {
          "vatCode": "RUS_VAT20",
          "totalVatAmount": 10.00
      }],
      "paymentType": "Безналичный расчёт"
    }
  }]
}
```
</section>
</details>


## Данные бронирования железнодорожных билетов

Для передачи данных бронирования железнодорожных билетов, в полях элементов корзины `metaData`
необходимо передать объект [TrainReservation](https://schema.org/TrainReservation) с перечнем
дочерних объектов.

<details>
  <summary>Пример объекта элемента корзины (билета) TrainReservation</summary>
<section markdown="1">
``` json
{
  "@type": "TrainReservation",
  "bookingTime": "2021-05-15T12:22:01",
  "reservationId": "74345932763286",
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
    "arrivalTime": "2021-06-04T03:10:00+01:00",
    "trainName" : "ГСЭ",
    "trainNumber": "425*СА"
  },
  "underName": {
    "@type": "Person",
    "name": "Иванов Сергей Иванович"
  },
  "provider": {
    "@type": "Organization",
    "name": "Sapsan",
    "taxID": "2323232323"
  },
  "reservedTicket": {
    "@type": "trainTicket",
    "underName": {
      "@type": "Person",
      "name": "Иванов Сергей Иванович"
    },
    "gender": "male",
    "nationality": "RUS",
    "idDocumentNumber": "***** 3456",
    "idDocumentDate": "2015-01-01",
    "coachNumber": "04",
    "coachType": "Плацкартный",
    "serviceClass": "3Э",
    "ticketedSeat": {
      "@type": "Seat",
      "seatNumber": "038"
    },
    "ticketNumber": "74363372056286",
    "ticketStatus": "Оформлен",
    "ticketIssueTime": "2021-05-15T12:30:21+01:00",
    "fareBase": 57.00,
    "fareReservation": 66.40,
    "vatValue": [{
        "vatCode": "RUS_VAT0",
        "totalVatAmount": 0.00
    },
    {
        "vatCode": "RUS_VAT20",
        "totalVatAmount": 10.00
    }],
    "paymentType": "Безналичный расчёт"
  }
}
```
</section>
</details>

<details>
  <summary>Пример объекта элемента корзины (услуги) TrainReservation</summary>
<section markdown="1">
``` json
{
  "@type": "TrainReservation",
  "bookingTime": "2021-05-15T12:22:01",
  "reservationId": "74345932763286",
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
    "arrivalTime": "2021-06-04T03:10:00+01:00",
    "trainName" : "ГСЭ",
    "trainNumber": "425*СА"
  },
  "underName": {
    "@type": "Person",
    "name": "Иванов Сергей Иванович"
  },
  "provider": {
    "@type": "Organization",
    "name": "Sapsan",
    "taxID": "2323232323"
  },
  "reservedTicket": {
    "@type": "baggageCheck",
    "underName": {
      "@type": "Person",
      "name": "Иванов Сергей Иванович"
    },
    "idDocumentNumber": "***** 3456",
    "idDocumentDate": "2015-01-01",
    "ticketNumber": "44363452345662",
    "declaredName": "Велосипед",
    "declaredValue": 100.00,
    "note": "Малогабаритный багаж в специализированном купе",
    "fare": 57.00,
    "valueFee": 66.40,
    "vatValue": [{
        "vatCode": "RUS_VAT0",
        "totalVatAmount": 0.00
    },
    {
        "vatCode": "RUS_VAT20",
        "totalVatAmount": 10.00
    }],
    "paymentType": "Безналичный расчёт"
  }
}
```
</section>
</details>



## Данные бронирования места проживания

Для передачи данных бронирования места проживания (отель, хостел, апартаменты и пр.), в поле заказа `metaData`
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
        "addressCountry": "ru"
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

[Читать далее &raquo;](/docs/merchant/refund){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
