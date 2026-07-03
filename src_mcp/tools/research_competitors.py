"""research_competitors: анализ конкурентов."""


async def run(niche: str, competitors: list = None) -> dict:
    """Ресёрч.

    Args:
        niche: Ниша.
        competitors: Список URL (опц.).

    Returns:
        Словарь с framework анализа.
    """
    return {
        "niche": niche,
        "competitors": competitors or [],
        "what_to_analyze": [
            "Headline: какую главную выгоду обещают?",
            "Subhead: как расшифровывают headline?",
            "Hero CTA: что просят сделать? (free trial, book demo, etc)",
            "Social proof: цифры, логотипы клиентов, отзывы?",
            "Pricing: видна ли цена? free trial / freemium / pay-only?",
            "Features: 3-5 ключевых, в чём фокус?",
            "FAQ: какие возражения закрывают?",
            "Footer: дополнительные ссылки, контакты",
        ],
        "questions_to_answer": [
            "Какую боль решают? (своими словами)",
            "Для кого это? (персона)",
            "Чем отличаются от альтернатив?",
            "Какие фичи упоминают первыми? (= самые важные)",
            "Какой tone of voice? (формальный, casual, technical)",
            "Есть ли видео? demo, customer story?",
            "Где CTA: hero, mid-page, sticky bar?",
        ],
        "swot_template": {
            "strengths": "Что у них хорошо? (UI, copy, features)",
            "weaknesses": "Что плохо? (loading, unclear copy, no mobile)",
            "opportunities": "Что ты можешь сделать лучше? (positioning, niche)",
            "threats": "Что тебе будет сложно? (финансы, аудитория, brand)",
        },
    }
