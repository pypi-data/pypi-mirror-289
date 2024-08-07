"""Core agent definitions and functionality."""

from __future__ import annotations
import json
from typing import AsyncGenerator, Callable, TYPE_CHECKING

from flexai import llm
from flexai.message import (
    AIMessage,
    Message,
    SystemMessage,
    ToolResultMessage,
    ToolUseMessage,
)
from flexai.tool import Tool, send_message

if TYPE_CHECKING:
    from flexai.capability import AgentCapability


class Agent:
    """An LLM agent that can use tools and capabilities to interact with users."""

    def __init__(
        self,
        prompt: str = "",
        tools: list[Callable] | None = None,
        capabilities: list[AgentCapability] | None = None,
        llm: llm.Client = llm.AnthropicClient(),
    ):
        """Create an agent with the given tools and capabilities.

        Args:
            prompt: The system prompt to use for the agent throughout the conversation.
            tools: A list of functions that the agent can call and use.
            capabilities: Hooks that can plugin to the main agent loop to modify its behavior.
            llm: The language model to use for the agent.
        """
        self.prompt = prompt
        self.llm = llm
        self.capabilities = capabilities or []

        # Convert the functions to Tool objects.
        agent_tools = [
            Tool.from_function(tool) for tool in set(tools or [send_message])
        ]
        self.tools = {tool.name: tool for tool in agent_tools}

    async def modify_messages(self, messages: list[Message]) -> list[Message]:
        """Hook to modify the messages before sending them to the LLM.

        Args:
            messages: The current conversation messages.

        Returns:
            The modified messages.
        """
        # Iterate through the capabilities and modify the messages.
        for capability in self.capabilities:
            messages = await capability.modify_messages(messages)
        return messages

    async def get_system_message(self) -> SystemMessage:
        """Hook to modify the system message before sending it to the LLM.

        Returns:
            The modified system message.
        """
        system = self.prompt

        # Iterate through the capabilities and modify the system message.
        for capability in self.capabilities:
            system = await capability.modify_prompt(system)
        return SystemMessage(content=system)

    async def modify_response(
        self, messages: list[Message], response: AIMessage
    ) -> AIMessage:
        """Hook to modify the AI response before sending it to the user.

        Args:
            messages: The current conversation messages.
            response: The AI response.

        Returns:
            The modified AI response.
        """
        # Iterate through the capabilities and modify the response.
        for capability in self.capabilities:
            response = await capability.modify_response(messages, response)
        return response

    def invoke_tool(self, message: ToolUseMessage) -> ToolResultMessage:
        """Invoke a tool and return the result.

        Args:
            message: The tool use message.

        Returns:
            The result of the tool invocation.
        """
        # Load the params.
        data = json.loads(message.content)
        tool = self.tools[data["name"]]

        # Invoke the tool and return the result or the exception.
        try:
            result = tool.fn(**data["input"])
        except Exception as e:
            result = e
        return ToolResultMessage.from_result(data["id"], result)

    async def step(self, messages: list[Message]) -> AIMessage:
        """Take a single step in the conversation.

        Args:
            messages: The current conversation messages.
        """
        # Preprocess the messages and get the system message.
        messages = await self.modify_messages(messages)
        system = await self.get_system_message()

        # Get the response from the LLM.
        response = await self.llm.get_chat_response(
            messages, system=system, tools=self.tools.values()
        )

        # Check which tool to use.
        data = json.loads(response.content)
        tool = self.tools[data["name"]]

        # Base case: send a message.
        if tool.name == "send_message":
            return AIMessage(content=data["input"]["message"])

        # Return the tool use message.
        response = await self.modify_response(messages, response)
        return response

    async def stream(self, messages: list[Message]) -> AsyncGenerator[Message, None]:
        """Stream the agent and let it invoke tools until it's done.

        Args:
            messages: The initial messages to start the conversation.
        """
        # Run in a loop.
        while True:
            # Get the response and yield.
            response = await self.step(messages)
            yield response

            # If it's not a tool use, end the stream.
            if not isinstance(response, ToolUseMessage):
                return

            # Invoke the tool and yield.
            result = self.invoke_tool(response)
            yield result

            # Append the messages.
            messages.append(response)
            messages.append(result)
