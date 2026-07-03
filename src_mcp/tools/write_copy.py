"""write_copy: генерация текста лендинга."""


TEMPLATES = {
    "professional": {
        "headline": "{product}: решение для {audience}",
        "subhead": "Сэкономьте время и деньги с помощью {value_prop}",
        "cta_primary": "Попробовать бесплатно",
        "cta_secondary": "Смотреть демо",
    },
    "casual": {
        "headline": "{product} — и {audience} больше не страдает",
        "subhead": "{pain_point}? Мы знаем как починить. За {time_result}.",
        "cta_primary": "Давай попробуем!",
        "cta_secondary": "Посмотреть как работает",
    },
    "bold": {
        "headline": "Хватит {pain_point}. Вот {product}.",
        "subhead": "{big_claim} за {short_time}. Без {objection}.",
        "cta_primary": "Забрать своё →",
        "cta_secondary": "Сначала посмотрю",
    },
}


async def run(product: str, audience: str, tone: str = "professional") -> dict:
    """Генерирует copy.

    Args:
        product: Что за продукт.
        audience: Целевая аудитория.
        tone: professional / casual / bold.

    Returns:
        Словарь с copy.
    """
    template = TEMPLATES.get(tone, TEMPLATES["professional"])

    # Заполняем шаблон
    product_clean = product.replace("{", "").replace("}", "")
    audience_clean = audience.replace("{", "").replace("}", "")

    headline = template["headline"].format(
        product=product_clean,
        audience=audience_clean,
        value_prop="автоматизации",
        pain_point="терять время",
        time_result="5 минут",
        big_claim="Увеличение продаж на 30%",
        short_time="1 день",
        objection="программистов",
    )

    subhead = template["subhead"].format(
        product=product_clean,
        audience=audience_clean,
        value_prop="автоматизации",
        pain_point="рутина",
        time_result="5 минут",
        big_claim="Увеличение продаж на 30%",
        short_time="1 день",
        objection="программистов",
    )

    return {
        "tone": tone,
        "product": product,
        "audience": audience,
        "hero": {
            "headline": headline,
            "subhead": subhead,
            "primary_cta": template["cta_primary"],
            "secondary_cta": template["cta_secondary"],
        },
        "features_section": {
            "title": f"Почему {product}?",
            "items": [
                {"title": "Быстро", "description": f"Настройка за 5 минут, не часы"},
                {"title": "Безопасно", "description": "Шифрование end-to-end, GDPR"},
                {"title": "Доступно", "description": "От 990₽ в месяц, без скрытых платежей"},
            ],
        },
        "social_proof": {
            "title": "Что говорят клиенты",
            "testimonials": [
                {"text": f"Сэкономил 10 часов в неделю благодаря {product}", "author": "Иван, маркетолог"},
                {"text": "Наконец-то нашел что-то что работает из коробки", "author": "Мария, e-com"},
            ],
        },
        "faq": [
            {"q": "Как быстро начать?", "a": "Регистрация → настройка → первый результат за 5 минут"},
            {"q": "Можно ли отменить?", "a": "Да, в любой момент. Без вопросов и штрафов"},
            {"q": "Есть ли бесплатная версия?", "a": "Да, 14 дней trial. Карта не нужна"},
        ],
        "principles": [
            "Headline = главная выгода, не описание продукта",
            "Subhead = как ты её достигнешь",
            "CTA = конкретное действие, не 'Узнать больше'",
            "Social proof = конкретные цифры, не 'нам доверяют'",
            "FAQ = топ-5 возражений, не общая информация",
        ],
    }
