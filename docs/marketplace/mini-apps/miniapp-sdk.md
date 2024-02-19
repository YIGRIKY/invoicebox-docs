---
layout: default
nav_order: 30
title: "MiniApp SDK"
parent: "Мини-приложения"
grand_parent: "Маркетплейс"
date: 2024-02-19 00:00:00 +0300
---

# Инвосбокс MiniApp SDK

Библиотека `minapp-sdk` позволяет мини-приложениям использовать API Инвойсбокс и API операционной системы, установленной
на устройстве пользователя.

Библиотека является мостом между мини-приложениями, работающими на стороне пользователя, и клиентской частью Инвойсбокс
(десктопной версией платёжного сервиса, мобильной версией платёжного сервиса или мобильным приложением). Именно они
обмениваются данными с серверами Инвойсбокс, а библиотека работает как посредник на стороне пользователя.

- NPM: [minapp-sdk](https://www.npmjs.com/package/@invoicebox/minapp-sdk)
- GitHub: [minapp-sdk](https://github.com/InvoiceBox/invoicebox-minapp-sdk)

## Как использовать библиотеку MiniApp SDK

Чтобы использовать библиотеку:

1. Создайте проект мини-приложения
2. [Подключите MiniApp SDK](/docs/marketplace/mini-apps/miniapp-sdk/#%D0%BF%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-miniapp-sdk)
3. Используйте методы:
   - Метод [invoiceboxMinapp.getInitialData](/docs/marketplace/mini-apps/miniapp-sdk/#%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-getinitialdata). Получить данные покупателя от родительского окна.
4. Обработайте события:
   - Событие [invoiceboxMinapp.onHeightChange](/docs/marketplace/mini-apps/miniapp-sdk/#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-onheightchange). Сообщить родительскому окну параметры высоты мини-приложения.
   - Событие [invoiceboxMinapp.onDone](/docs/marketplace/mini-apps/miniapp-sdk/#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-ondone). Сообщить родительскому окну о готовности заказа к оплате.
   - Событие [invoiceboxMinapp.onError](/docs/marketplace/mini-apps/miniapp-sdk/#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-onerror). Сообщить родительскому окну об ошибке в мини-приложении.
   - Событие [invoiceboxMinapp.onLink](/docs/marketplace/mini-apps/miniapp-sdk/#%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-onlink). Сообщить родительскому окну о необходимости открыть страницу.

Инструкция ниже актуальна для любой операционной системы. Для первых шагов потребуется знание языка JavaScript и умение работать с командной строкой.

## Подключение MiniApp SDK

Родительским окном мини-приложения может быть `iframe` или `WebView`.

### Через пакет NPM

Перейдите в созданный проект мини-приложения:

```
cd <ПУТЬ_К_МИНИ_ПРИЛОЖЕНИЮ>
```

Установите библиотеку:

```
npm install @invoicebox/minapp-sdk || yarn add @invoicebox/minapp-sdk
```

Инициализируйте MiniApp SDK в файле index.js:

```
import { invoiceboxMinapp } from '@invoicebox/minapp-sdk';
```


### Включение скрипта в HTML-код страницы

Этот способ подходит, если вы не используете менеджеры пакетов, такие как npm или yarn, для создания своего HTML-приложения.

**В код каждой HTML-страницы, где вы будете вызывать библиотеку, добавьте ссылку на файл index.min.js**

В репозитории MiniApp SDK этот файл находится в папке cjs (commonjs modules). Мы рекомендуем ссылаться на копию файла, расположенную
на сервисе unpkg.com. В этом случае вы автоматически будете получать последнюю версию библиотеки и вам не нужно будет самостоятельно
следить за выходом её обновлений.

```html
<!-- Если требуется зафиксировать версию, например, 3.0.1 -->
<script src="https://unpkg.com/@invoicebox/minapp-sdk@3.0.1/cjs/index.min.js"></script>

<!-- Крайняя версия (следует использовать аккуратно, так как крайние изменения могут быть не совместимы) -->
<script src="https://unpkg.com/@invoicebox/minapp-sdk/cjs/index.min.js"></script>
```

**В коде каждой HTML-страницы, где вы будете вызывать библиотеку, инициализируйте MiniApp SDK**

```html
<script>
  const Miniapp = new InvoiceboxMinapp()
</script>
```

## События и методы

### Метод getInitialData

Для того, чтобы получить данные покупателя для оформления заказа, воспользуйтесь методом `getInitialData`.

```js
getInitialData(): Promise<{
    orderType: enum;
    orderContainerId?: string;
    shopId?: number;
    userEmail: string;
    userName: string;
    userPhone: string;
}>
```

- orderType - тип формируемого заказа `order` (основной заказ) или `suborder` (дополнительная услуга)
- orderContainerId - опционально, идентификатор родительского заказа в случае, если заказ является дополнительной услугой
- shopId - опционально, идентификатор точки продаж, если мини-приложение работает с множеством точек продаж
- userEmail - адрес электронной почты покупателя
- userName - имя покупателя
- userPhone - номер мобильного телефона покупателя

Пример использования

```js
invoiceboxMinapp.getInitialData().then(console.log);

/*
{
    orderContainerId: '3c15a3d1-3da8-4ba8-87e5-2dba828299fa';
    shopId: 123;
    userEmail: 'email@example.com';
    userName: 'Иван Иванов';
    userPhone: '+71231234567';
}
*/
```

### Событие onHeightChange

Для управления высотой мини-приложения на платёжной странице используется метод `onHeightChange`.
Мини-приложение может задать высоту, которая требуется для корректного отображения мини-приложения
на платёжной странице.

```js
onHeightChange(height: number): void;
```

Пример использования

```js
const Conatiner = ({ isConnected, children }: { isConnected: boolean, children: ReactNode }) => {
    const [elRef, setElRef] = useState<HTMLDivElement | null>(null);

    useEffect(() => {
        if (!elRef) return;
        if (!isConnected) return;
        const observer = new ResizeObserver(() => {
            invoiceboxMinapp.onHeightChange(elRef.offsetHeight);
        });
        observer.observe(elRef);
        return () => observer.disconnect();
    }, [elRef, child, isConnected]);

    return <div ref={elRef}>{children}</div>;
}
```

### Событие onDone

После того, как мини-приложение успешно добавило новый заказ в существующий `orderContainer` или создало новый,
необходимо вызвать метод `onDone`. `paymentUrl` приходит от сервера в момент создания заказа.

```js
onDone(paymentUrl: string): void
```

Пример использования

```js
 createOrderRequest(someData)
    .then((response) => {
        invoiceboxMinapp.onDone(response.data.url);
    })
```

### Событие onError

В случае возникновения ошибки в мини-приложении (например, при оформлении заказа, при взаимодействии с API Инвойсбокс и т.д.),
необходимо вызвать метод `onError`. Родительская страница уведомит пользователя об ошибке. Функция принимает один опциональный
строковый аргумент - пользовательское сообщение. Если сообщение есть, то оно отобразится. Если нет, то отобразится сообщение
по умолчанию `Что-то пошло не так`.

```js
onError(message?: string): void
```

Пример использования

```js
// Пользователь увидит "Ошибка создания заказа"
invoiceboxMinapp.onError('Ошибка создания заказа');

// Пользователь увидит "Что-то пошло не так"
invoiceboxMinapp.onError();
```

### Событие onLink

Метод `onLink` позволяет произвести переадресацию пользователя по ссылке в родительском окне, как будто переадресация была
вызвана не в контексте `iframe`/`webview`, а в контексте родительской страницы.

```js
onLink(href: string): void
```

Пример использования

```js
// На платёжной странице будет открыта новая вкладка с Google страницей
// это никак не повлияет на работу мини-приложения
invoiceboxMinapp.onLink('https://www.google.ru');
```

---

[Читать далее &raquo;](/docs/marketplace/create/){: .btn .btn-primary .mb-4 .mb-md-0 .mr-2 }
