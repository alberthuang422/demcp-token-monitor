from typing import Any, Literal
import httpx
from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP 服务器
mcp = FastMCP("demcp-token-monitor",host="0.0.0.0",port=8090)

# 常量
user_agent = "weather-app/1.0"
base_url = "http://localhost:8090"

@mcp.tool(
    description="this tool is used to monitor the token price,when the price is up or down to the trigger price,it will send a message to the user",
)
async def monitor_token(
    chain: str,
    token_contract: str,
    trigger_price: float,
    event_type: Literal["up", "down"],
    phone_number: str,
) -> dict:
    """    
    Args:
        chain: 区块链网络名称 (例如: "ethereum")
        token_contract: 代币合约地址
        trigger_price: 触发价格
        event_type: 事件类型 ("up" 或 "down")
        phone_number: 接收通知的电话号码
        
    Returns:
        API 响应数据
    """
    url = f"{base_url}/v1/callmcp"
    payload = {
        "chain": chain,
        "token_contract": token_contract,
        "trigger_price": trigger_price,
        "event_type": event_type,
        "phone_number": phone_number
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        response.raise_for_status()
        return response.json()

# 使用示例
if __name__ == "__main__":
    # 初始化并运行服务器
    mcp.run(transport='sse')
