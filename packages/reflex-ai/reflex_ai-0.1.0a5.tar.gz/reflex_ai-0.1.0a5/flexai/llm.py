from __future__ import annotations

import os
from typing import AsyncGenerator, Type, TYPE_CHECKING

import reflex as rx
from flexai.message import (
    AIMessage,
    Message,
    SystemMessage,
    ToolUseMessage,
    UserMessage,
)


if TYPE_CHECKING:
    from flexai.tool import Tool


class Client:
    """A base class for language models."""

    async def stream_chat_lines(
        self,
        messages: list[Message],
        system: SystemMessage | None = None,
    ) -> AsyncGenerator[AIMessage, None]:
        """Stream the response from the chat model line by line.

        Args:
            messages: The messages to send to the model.

        Returns:
            An async generator yielding the response from the model line by line.
        """
        buffer = ""
        async for delta in self.stream_chat_response(messages, system=system):
            buffer += delta.content
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                yield AIMessage(content=f"{line}\n")


class AnthropicClient(Client):
    """A client for the Anthropic language model."""

    def __init__(
        self,
        model: str = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20240620"),
    ):
        """Create a new Anthropic client."""
        from anthropic import AsyncAnthropic

        self.client = AsyncAnthropic()
        self.model = model
        self.max_tokens = 4096

    @classmethod
    def to_llm_messages(cls, messages: list[Message]) -> list[dict]:
        """Convert messages to the anthropic format.

        Args:
            messages: The messages to convert.

        Returns:
            The messages in the anthropic format.
        """
        return [{"role": m.role, "content": m.content} for m in messages]

    @classmethod
    def to_tool_descriptions(cls, tools: list[Tool]) -> list[dict]:
        """Convert tools to the anthropic format.

        Args:
            tools: The tools to convert.

        Returns:
            The tools in the anthropic format.
        """
        return [tool.to_description() for tool in tools]

    def get_params(self, messages, system, tools) -> dict:
        """Get the common params to send to the model.

        Args:
            messages: The messages to send to the model.
            system: The system message to send to the model.
            tools: The tools to send to the model.

        Returns:
            The common params to send to the model.
        """
        kwargs = {
            "max_tokens": self.max_tokens,
            "messages": self.to_llm_messages(messages),
            "model": self.model,
            "system": system.content if system else "",
        }
        if tools:
            kwargs["tools"] = self.to_tool_descriptions(tools)
            kwargs["tool_choice"] = {"type": "any"}
        return kwargs

    async def get_chat_response(
        self,
        messages: list[Message],
        system: SystemMessage | None = None,
        tools: list[Tool] = None,
    ) -> AIMessage:
        """Get the response from the chat model.

        Args:
            messages: The messages to send to the model.

        Returns:
            The response from the model.
        """
        from anthropic.types import ToolUseBlock

        system = system or SystemMessage(content="")
        response = await self.client.messages.create(
            **self.get_params(messages, system, tools)
        )
        assert len(response.content) == 1, f"Expected a single response, got {response}"
        content = response.content[0]
        if isinstance(content, ToolUseBlock):
            return ToolUseMessage(content=content.json())
        return AIMessage(content=content.text)

    async def stream_chat_response(
        self,
        messages: list[Message],
        system: SystemMessage | None = None,
        tools: list[Tool] = None,
    ) -> AsyncGenerator[AIMessage, None]:
        """Stream the response from the chat model.

        Args:
            messages: The messages to send to the model.

        Returns:
            An async generator yielding the response from the model.
        """
        system = system or SystemMessage(content="")
        async with self.client.messages.stream(
            **self.get_params(messages, system, tools)
        ) as stream:
            async for text in stream.text_stream:
                yield AIMessage(content=text)

    async def get_structured_response(
        self,
        messages: list[Message],
        model: Type[rx.Base],
        system: SystemMessage | None = None,
    ) -> Type[rx.Base]:
        """Get the structured response from the chat model.

        Args:
            messages: The messages to send to the model.
            model: The model to use for the response.

        Returns:
            The structured response from the model.
        """
        system = SystemMessage(
            content=f"""{system or ""}

Return your answer according to the 'properties' of the following schema:
{model.schema()}

Return only the JSON object with the properties filled in.
Do not include anything in your response other than the JSON object.
Do not begin your response with ```json or end it with ```.
"""
        )
        response = await self.get_chat_response(messages, system=system)
        try:
            obj = model.parse_raw(response.content)
        except Exception as e:
            # Try again, printing the exception.
            messages = messages + [
                response,
                UserMessage(
                    content=f"There was an error while parsing. Make sure to only include the JSON. Error: {e}"
                ),
            ]
            return await self.get_structured_response(
                messages, model=model, system=system
            )
        return obj


llm = AnthropicClient()
