import os
from mcp.client.stdio import stdio_client
from mcp import ClientSession,StdioServerParameters,client
import asyncio

# path to the MCP server 
mcp_server_script = os.path.join((os.path.dirname(os.path.abspath(__file__))),"1_first_mcp_server.py")
print(mcp_server_script)    

# Create a Server parameters
server_params = StdioServerParameters(
    command="python",
    args=[str(mcp_server_script)],
    env={}
)

# Create a Client Session
async def main():
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            # Fetch the  tools\
            tools = await session.list_tools()
            print("Available tools:",tools)

            # use the process tool
            result = await session.call_tool("process",arguments={"path":"/path/to/data"})
            print("Result:",result)

if __name__ == "__main__":
    asyncio.run(main())