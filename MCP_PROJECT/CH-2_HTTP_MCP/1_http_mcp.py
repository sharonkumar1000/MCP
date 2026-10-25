from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()  #special decorator
async def fetch_http(): 
    '''Use this tool to fetch data from Source '''
    # fetching data from source
    return {"data":"Hello, MCP!"}

@mcp.tool()
async def process_http(path:str):
    '''Use this tool to process the fetched data '''
    return {"processed_data":"Data has been processed as path:"+path}

if __name__ == "__main__":
    # Run the MCP server using HTTP transport
    mcp.run(transport="streamable-http",host="0.0.0.0",port = 8050)