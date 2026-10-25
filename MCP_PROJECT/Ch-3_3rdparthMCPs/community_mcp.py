from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
import sys



async def main():

    #create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

    # MCP Server Config (JSON)
    {
        "data_fetch_mcp_stdio":{
            "transport": "stdio",
            # "command":os.path.join(venv_path,"Scripts","python.exe"),
            "command": "uvx",
            "args": [ "duckduckgo-mcp-server"]
            # "args":[str(mcp_server_script)]
        }
    }
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:",tools)
    for tool in tools:
        print("Available tool",tool.name)

    fetch_tool = tools[0]
    result = await fetch_tool.ainvoke({"query":"what is the capital of France?"}) #fetching the tools asycnronously read documentation of langchain
    print("Tool result",result)

if __name__ == "__main__":
    asyncio.run(main())    