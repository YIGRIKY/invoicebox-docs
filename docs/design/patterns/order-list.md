---
layout: default
nav_order: 10
title: "OrderList"
parent: "Patterns"
grand_parent: "Дизайн-система"
date: 2024-02-11 00:00:00 +0300
---

# OrderList

Состоит из компонентов cell и divider, используется для отображения состава заказа.

![OrderList](/assets/images/design/patterns/order-list/frame1.png)

## Примеры использования

Высота компонента подстраивается под контент (т.е. vertical resizing в фигме у компонента – hug).
Токен цвета фона компонента – tertiary. Отступов у самого компонента нет – они есть у компонента «cell»,
который используется внутри OrderList.

![OrderList](/assets/images/design/patterns/order-list/frame2.png)

