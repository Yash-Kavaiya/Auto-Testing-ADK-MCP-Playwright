
import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/")


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='filesystem_assistant_agent',
    instruction='File System and Fi Money MCP Server',
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "mcp-remote",
                    "https://mcp.canva.com/mcp",
                ],
            ),
        ),

        MCPToolset(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    "mcp-remote",  
                    "https://mcp.deepwiki.com/sse",
                ],
            ),
        ),
        
    ],
)