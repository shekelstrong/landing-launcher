"""Landing Launcher MCP Server."""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from src_mcp.tools import research_competitors, write_copy, design_layout, deploy_vercel, deploy_layero


app = Server("landing-launcher")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="research_competitors",
            description="Ресёрч конкурентов: лендинги, офферы, цены, уникальные фичи.",
            inputSchema={
                "type": "object",
                "properties": {
                    "niche": {"type": "string"},
                    "competitors": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["niche"],
            },
        ),
        Tool(
            name="write_copy",
            description="Генерация текста для лендинга: headline, subhead, features, CTA, FAQ.",
            inputSchema={
                "type": "object",
                "properties": {
                    "product": {"type": "string"},
                    "audience": {"type": "string"},
                    "tone": {"type": "string", "default": "professional"},
                },
                "required": ["product"],
            },
        ),
        Tool(
            name="design_layout",
            description="Структура лендинга: hero, features, social proof, pricing, FAQ, CTA.",
            inputSchema={
                "type": "object",
                "properties": {
                    "product_type": {"type": "string", "enum": ["saas", "service", "ecommerce", "mobile-app"]},
                    "sections": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["product_type"],
            },
        ),
        Tool(
            name="deploy_vercel",
            description="Деплой лендинга на Vercel: vercel.json + команды.",
            inputSchema={
                "type": "object",
                "properties": {
                    "framework": {"type": "string", "default": "vite"},
                },
            },
        ),
        Tool(
            name="deploy_layero",
            description="Деплой лендинга на Layero (RU hosting): vercel.json + инструкция.",
            inputSchema={
                "type": "object",
                "properties": {
                    "build_dir": {"type": "string", "default": "dist"},
                },
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    import json
    tools_map = {
        "research_competitors": research_competitors,
        "write_copy": write_copy,
        "design_layout": design_layout,
        "deploy_vercel": deploy_vercel,
        "deploy_layero": deploy_layero,
    }
    try:
        result = await tools_map[name].run(**arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {type(e).__name__}: {e}")]


async def main():
    async with stdio_server() as (rs, ws):
        await app.run(rs, ws, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
