"""Welcome to Reflex! This file create a counter app."""

import os
import reflex as rx
from reflex_ai.selection import ClickSelectionState
from reflex_ai.local_agent import (
    get_agent,
    InternRequest,
    InternResponse,
    ToolRequestResponse,
)

import httpx
from flexai.message import Message, ToolUseMessage
from anthropic.types import ToolUseBlock

backend = "localhost:8000"


class PlaygroundState(rx.State):
    """The app state."""

    dev_mode: bool = True
    processing: bool = False

    selected_id: str = ""
    code: str = ""
    prompt: str = ""

    async def process(self, prompt):
        # Generate new code.
        self.processing = True
        yield

        selection_state = await self.get_state(ClickSelectionState)
        selected_code = "\n".join(selection_state._selected_code)

        unconverted_messages = []

        request = InternRequest(
            prompt=prompt["prompt"],
            selected_code=selected_code,
            selected_module=selection_state.selected_module,
            selected_function=selection_state.selected_function,
        )

        resp = httpx.post(
            f"http://{backend}/api/intern",
            data=request.model_dump_json(),
            timeout=60,
        )
        print(resp)
        print(resp.json())
        resp_obj = InternResponse(**resp.json())
        messages = [Message(role=m.role, content=m.content) for m in resp_obj.messages]

        while True:
            tool_response_messages = []
            local_intern = get_agent()
            for message in messages:
                try:
                    tool_use_message = ToolUseMessage.from_tool_use_block(
                        ToolUseBlock.parse_raw(message.content),
                    )
                except ValueError:
                    unconverted_messages.append(message)
                    continue
                tool_response_messages.append(
                    await local_intern.invoke_tool(tool_use_message)
                )

            if not tool_response_messages:
                break

            tool_response_request = ToolRequestResponse(
                request_id=resp_obj.request_id,
                messages=tool_response_messages,
            )
            print("REQUEST TO API: ", tool_response_request)

            resp2 = httpx.post(
                f"http://{backend}/api/intern/tool_response",
                data=tool_response_request.model_dump_json(),
                timeout=60,
            )
            resp2.raise_for_status()
            print("RESPONSE FROM API: ", resp2.content)
            messages = [
                Message(role=m["role"], content=m["content"]) for m in resp2.json()
            ]

        self.processing = False

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        print("uploading")
        import base64

        for file in files:
            upload_data = await file.read()
            # Convert to base64.
            image_data = base64.b64encode(upload_data).decode()
            self.image = f"data:image/png;base64,{image_data}"

    async def get_source(self, data):
        """Get the source of the data."""
        if not open:
            return
        import importlib.util

        self.selected_id = data
        yield
        filename, function_name = data.split(":")
        module_name = os.path.splitext(os.path.basename(filename))[0]

        print(module_name)

        spec = importlib.util.spec_from_file_location(module_name, filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        function = getattr(module, function_name)
        if inspect.isfunction(function) or inspect.ismethod(function):
            self.code = inspect.getsource(function)
        else:
            print(f"{function_name} is not a function or method in {filename}")


ClientState = rx._x.client_state("code", rx.Var.create("code", _var_is_string=True))

import inspect
import os


def component(fn):
    """A decorator that adds an on_click handler to the component."""


def get_current_function_name():
    filename = __file__
    function_name = inspect.currentframe().f_back.f_code.co_name
    return f"{filename}:{function_name}"


def toolbar():
    return rx.hstack(
        rx.cond(
            PlaygroundState.processing,
            rx.spinner(size="3", color="white"),
        ),
        rx.upload.root(
            rx.button("Image"),
            id="image",
            on_drop=PlaygroundState.handle_upload(rx.upload_files(upload_id="image")),
        ),
        rx.form(
            rx.input(name="prompt", disabled=PlaygroundState.processing),
            on_submit=PlaygroundState.process,
            reset_on_submit=True,
        ),
    )


def playground(page):
    """The main view."""
    return rx.vstack(
        page(),
        rx.cond(
            PlaygroundState.dev_mode,
            rx.box(
                toolbar(),
                width="100%",
                bottom="0",
            ),
        ),
        rx.code_block(ClickSelectionState.code),
        min_height="100vh",
    )
