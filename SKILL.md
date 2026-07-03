---
name: landing-launcher
description: Лендинг от ТЗ до деплоя. Ресёрш конкурентов, copy (3 тона), layout (4 типа: SaaS/service/ecommerce/mobile-app), деплой на Vercel или Layero.
---

# Landing Launcher

MCP-сервер для быстрого создания лендинга.

## Когда использовать

- Запускаешь продукт и нужен лендинг
- Хочешь понять как пишут лендинги конкуренты
- Нужен готовый текст в разных тонах
- Deploy на Vercel или Layero

## 5 tools

```
ниша → research_competitors (что у других)
       ↓
текст → write_copy (3 тона)
       ↓
структура → design_layout (10 секций)
       ↓
деплой → deploy_vercel / deploy_layero
```

## Алгоритм

### 1. research_competitors
8 пунктов для разбора:
- Headline (главная выгода)
- Subhead (как её достичь)
- CTA (что просят)
- Social proof (цифры, логотипы)
- Pricing (видна ли цена)
- Features (3-5 главных)
- FAQ (возражения)
- Footer (контакты)

+ SWOT шаблон.

### 2. write_copy
3 тона:
- **professional** — деловой, для B2B
- **casual** — дружеский, для B2C
- **bold** — дерзкий, для стартапов

Возвращает: hero (headline + subhead + CTA), features, testimonials, FAQ.

### 3. design_layout
4 типа × 8-10 секций:
- **SaaS** — Nav, Hero, Logos, Features, How it works, Testimonial, Pricing, FAQ, Final CTA, Footer
- **Service** — Nav, Hero (фото владельца), Проблема, Решение, Кейсы, Процесс, Стоимость, Отзывы, FAQ
- **E-commerce** — Nav, Hero (товар), Фичи, Галерея, Отзывы, Стоимость, Доставка, FAQ
- **Mobile App** — Nav, Hero (мокап), 3 фичи, Скриншоты, Отзывы, App Store, FAQ

### 4. deploy_vercel
3 framework: vite / nextjs / astro.
vercel.json + 5 инструкций.

### 5. deploy_layero
RU hosting: vercel.json + warnings про serverless.

## Pitfalls

| Ошибка | Последствие | Как избежать |
|---|---|---|
| Headline описывает фичи | "CRM с X и Y" = скучно | Headline = выгода ("Увеличим продажи на 30%") |
| 5+ CTA на странице | Ни один не работает | 1 primary + 1 secondary |
| "Узнать больше" | Не CTA | Конкретное действие ("Забрать своё") |
| Без social proof | "А кто использует?" | Логотипы клиентов или цифры |
| FAQ "что такое продукт" | Не то | FAQ = топ-5 возражений |
| Mobile не тестировали | 60% трафика уходит | Mobile-first |
| Длинный landing | Не дочитывают | Один экран = одна мысль |

## Источники

6 скиллов: frontend-design, anthropic-frontend-design, vercel-frontend-deployment, layero-development, buildo-landing-layero, webapp-testing.
