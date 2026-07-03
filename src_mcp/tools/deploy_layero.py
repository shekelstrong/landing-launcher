"""deploy_layero: деплой на Layero (RU hosting)."""


async def run(build_dir: str = "dist") -> dict:
    """Генерирует конфиг.

    Args:
        build_dir: Папка после сборки.

    Returns:
        Словарь.
    """
    return {
        "build_dir": build_dir,
        "vercel_json": f'''{{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": "{build_dir}"
}}
''',
        "instructions": [
            "1. Локально: npm run build",
            f"2. Убедись что {build_dir}/index.html существует",
            "3. git push в GitHub",
            "4. Layero → подключи репо → auto-deploy",
            "5. Домен в Layero dashboard",
        ],
        "warnings": [
            "Layero = static only (без serverless functions)",
            "SPA с client-side routing → нужен BrowserRouter fallback",
            "Vite + React Router → добавь rewrites в vercel.json",
        ],
    }
