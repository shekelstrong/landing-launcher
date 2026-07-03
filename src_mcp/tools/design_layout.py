"""design_layout: структура лендинга."""


LAYOUTS = {
    "saas": [
        {"section": "Nav", "elements": ["logo", "features", "pricing", "login", "signup"]},
        {"section": "Hero", "elements": ["headline", "subhead", "primary_cta", "hero_image"]},
        {"section": "Logos", "elements": ["trusted_by: logo1, logo2, logo3, logo4, logo5"]},
        {"section": "Features (3-5)", "elements": ["feature1: icon+title+desc", "feature2", "feature3"]},
        {"section": "How it works (3 steps)", "elements": ["step1: number+title+desc", "step2", "step3"]},
        {"section": "Testimonial", "elements": ["quote", "author", "company"]},
        {"section": "Pricing (3 tiers)", "elements": ["tier1", "tier2 (featured)", "tier3"]},
        {"section": "FAQ (5-7)", "elements": ["q+a"]},
        {"section": "Final CTA", "elements": ["headline", "primary_cta"]},
        {"section": "Footer", "elements": ["links", "social", "copyright"]},
    ],
    "service": [
        {"section": "Nav"},
        {"section": "Hero (с фото владельца)"},
        {"section": "Проблема клиента"},
        {"section": "Твоё решение"},
        {"section": "Кейсы (3-5)"},
        {"section": "Процесс работы"},
        {"section": "Стоимость"},
        {"section": "Отзывы"},
        {"section": "FAQ"},
        {"section": "Footer"},
    ],
    "ecommerce": [
        {"section": "Nav"},
        {"section": "Hero (товар крупно)"},
        {"section": "Фичи товара (5-7)"},
        {"section": "Галерея фото/видео"},
        {"section": "Отзывы покупателей"},
        {"section": "Стоимость + акция"},
        {"section": "Доставка и возврат"},
        {"section": "FAQ"},
        {"section": "Footer"},
    ],
    "mobile-app": [
        {"section": "Nav"},
        {"section": "Hero (мокап телефона)"},
        {"section": "3 главные фичи"},
        {"section": "Скриншоты (карусель)"},
        {"section": "Отзывы пользователей"},
        {"section": "Скачать (App Store / Google Play)"},
        {"section": "FAQ"},
        {"section": "Footer"},
    ],
}


async def run(product_type: str, sections: list = None) -> dict:
    """Генерирует layout.

    Args:
        product_type: saas / service / ecommerce / mobile-app.
        sections: Кастомные секции (опц.).

    Returns:
        Словарь с layout.
    """
    if sections:
        return {"product_type": product_type, "custom_sections": sections}

    layout = LAYOUTS.get(product_type, LAYOUTS["saas"])
    return {
        "product_type": product_type,
        "layout": layout,
        "design_principles": [
            "5-second test: за 5 сек посетитель должен понять что это и зачем ему",
            "Above the fold: headline + subhead + CTA + визуал",
            "Один CTA на экран (primary action)",
            "Visual hierarchy: размер, цвет, whitespace",
            "Mobile-first: 60%+ трафика с мобильных",
        ],
    }
