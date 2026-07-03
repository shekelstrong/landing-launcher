"""deploy_vercel: деплой на Vercel."""


async def run(framework: str = "vite") -> dict:
    """Генерирует vercel.json и инструкцию.

    Args:
        framework: vite / nextjs / astro.

    Returns:
        Словарь.
    """
    configs = {
        "vite": '''{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "framework": "vite",
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
''',
        "nextjs": '''{
  "version": 2,
  "framework": "nextjs"
}
''',
        "astro": '''{
  "version": 2,
  "framework": "astro"
}
''',
    }

    return {
        "framework": framework,
        "vercel_json": configs.get(framework, configs["vite"]),
        "instructions": [
            "1. Push в GitHub",
            "2. vercel.com → New Project → Import",
            "3. Framework: " + framework,
            "4. Deploy (1-2 мин)",
            "5. Custom domain → добавить в Settings",
        ],
    }
