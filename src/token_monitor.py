from typing import Any, Literal
import httpx
import os
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
# mcp = FastMCP("demcp-token-monitor",host="0.0.0.0",port=8080)
mcp = FastMCP("demcp-token-monitor")

# Constants
# base_url = os.getenv("BASE_URL", "http://13.214.183.77:9099")  # 从环境变量获取，如果未设置则使用默认值
base_url = "http://testapi.demcp.ai:9099"

@mcp.tool(
    description="Monitor token price and send notifications when price reaches trigger point",
)
async def monitor_token(
    chain: str,
    token_symbol: str,
    trigger_price: float,
    event_type: Literal["up", "down"],
    phone_number: str,
) -> dict:

    """    
    Args:
        chain: Blockchain network name (e.g., "ethereum")
        token_symbol: Token symbol (e.g., "BTC", "SOL", "ETH")
        trigger_price: Price threshold to trigger notification
        event_type: Event type ("up" for price increase, "down" for price decrease)
        phone_number: Phone number to receive notifications (e.g., "+8613800138000")
        
    Returns:
        API response data containing the monitoring request status
    """

    url = f"{base_url}/v1/callmcp"
    payload = {
        "chain": chain,
        "token_symbol": token_symbol,
        "trigger_price": trigger_price,
        "event_type": event_type,
        "phone_number": phone_number
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()


# Example usage
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse')
