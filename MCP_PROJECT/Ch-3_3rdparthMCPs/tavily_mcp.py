from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
import sys
from dotenv import load_dotenv
load_dotenv()


async def main():

    #create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

    # MCP Server Config (JSON)
    {
        "tavily_mcp_http":{
            "transport": "streamable-http",
            "url": "http://localhost:8050/mcp?tavilyApiKey = {os.getenv('TAVILY_API_KEY')}"
        }
    }
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:",tools)

if __name__ == "__main__":
    asyncio.run(main())     