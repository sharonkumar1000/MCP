from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
import sys

# path to the MCP server script
mcp_server_script = os.path.join((os.path.dirname(os.path.abspath(__file__))),"1_http_mcp.py")

# path to the virtual environment
venv_path = os.path.join((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),".venv")


async def main():

    #create an instance of the MultiServerMCPClient
    client = MultiServerMCPClient(

    # MCP Server Config (JSON)
    {
        # "data_fetch_mcp_stdio":{
        #     "transport": "stdio",
        #     "command":os.path.join(venv_path,"Scripts","python.exe"),
        #     # "command": r"C:\Users\sharo\Desktop\Sharon\AI_PROJECTS\MCP_PROJECT\.venv\Scripts\python.exe",
        #     # "args": [ r"C:\Users\sharo\Desktop\Sharon\AI_PROJECTS\MCP_PROJECT\CH-1_CreateMCP\1_first_mcp_server.py"],
        #     "args":[str(mcp_server_script)]
        # },
        "data_fetch_mcp_http":{
            "transport": "streamable-http",
            "url":"http://localhost:8050/mcp"
            
        }

    }
    )

    # List the tools
    tools = await client.get_tools()
    print("Available tools:",tools)

if __name__ == "__main__":
    asyncio.run(main())    