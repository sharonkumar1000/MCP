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

if __name__ == "__main__":
    mcp.run(transport="stdio")