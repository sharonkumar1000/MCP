from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()  #special decorator
async def fetch(): 
    '''Use this tool to fetch data from Source '''
    # fetching data from source
    return {"data":"Hello, MCP!"}

@mcp.tool()
async def process(path:str):
    '''Use this tool to process the fetched data '''
    return {"processed_data":"Data has been processed as path:"+path}

#mount the tools to the MCP Servers
mcp.mount(
    FastMCP.as_proxy({
        "mcpServers": {
            "ddg_mcp":{"command":"uvx","args":["duckduckgo-mcp-server"]}
            # can add other mcp servers by using another mount
        },
    }),
)


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host = "0.0.0.0",port = 8050)