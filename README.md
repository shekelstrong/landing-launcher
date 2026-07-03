# landing-launcher

> MCP-сервер: лендинг от ТЗ до деплоя. Ресёрч конкурентов, copy, layout, деплой на Vercel/Layero.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-compatible-purple.svg)](https://modelcontextprotocol.io)

## 🎯 Что это

MCP-сервер с 5 инструментами для лендинга:

- 🔍 **research_competitors** — анализ конкурентов (headline, pricing, features)
- ✍️ **write_copy** — генерация текста (3 тона: professional / casual / bold)
- 🏗 **design_layout** — структура (4 типа: SaaS / service / ecommerce / mobile-app)
- ▲ **deploy_vercel** — vercel.json + команды
- 🇷🇺 **deploy_layero** — для RU hosting

## 📦 Установка

```bash
git clone https://github.com/shekelstrong/landing-launcher.git
cd landing-launcher
pip install -r requirements.txt
```

## 🛠 MCP Tools

### research_competitors
```python
result = await research_competitors.run("AI CRM", competitors=["hubspot.com", "salesforce.com"])
# → {what_to_analyze: [...], questions_to_answer: [...], swot_template}
```

8 пунктов для анализа + SWOT шаблон.

### write_copy
```python
result = await write_copy.run("AI-бот", "маркетологи", "bold")
# → {hero: {headline, subhead, cta}, features, social_proof, faq, principles}
```

3 тона: professional / casual / bold.

### design_layout
```python
result = await design_layout.run("saas")
# → {layout: [10 секций], design_principles}
```

4 типа продукта × 8-10 секций каждый.

### deploy_vercel
```python
result = await deploy_vercel.run("vite")
# → {vercel_json, instructions}
```

### deploy_layero
```python
result = await deploy_layero.run("dist")
```

## 📁 Структура

```
landing-launcher/
├── README.md
├── LICENSE
├── SKILL.md
├── requirements.txt
├── src_mcp/
│   ├── server.py
│   └── tools/
│       ├── research_competitors.py
│       ├── write_copy.py
│       ├── design_layout.py
│       ├── deploy_vercel.py
│       └── deploy_layero.py
└── .github/workflows/ci.yml
```

## 🎯 Структура SaaS-лендинга

| Секция | Элементы | Цель |
|---|---|---|
| Nav | logo, features, pricing, login, signup | Ориентация |
| Hero | headline + subhead + CTA + image | Захват внимания |
| Logos | trusted_by: 5 логотипов | Social proof |
| Features | 3-5 фич (icon+title+desc) | Ценность |
| How it works | 3 шага | Понятность |
| Testimonial | quote + author + company | Доверие |
| Pricing | 3 тарифа | Конверсия |
| FAQ | 5-7 вопросов | Возражения |
| Final CTA | headline + CTA | Последний шанс |
| Footer | links, social, copyright | Навигация |

## 📄 License

MIT © Vasiliy Nedopekin (shekelstrong)
