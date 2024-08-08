from typing import TYPE_CHECKING, Any, Callable, cast  # noqa: I001
from .component import Component, weba_html_context
from .tag.context_manager import TagContextManager

if TYPE_CHECKING:
    from bs4 import Tag


class UIFactory:
    """
    A factory class for creating UI elements dynamically based on tag names.
    """

    _context_token: Any

    # _html: Component

    # def _tag_context_manager(self, tag: Any):
    #     return TagContextManager(tag, self._html)  # type: ignore

    def __getattr__(self, tag_name: str) -> Callable[..., TagContextManager]:
        def create_tag(*args: Any, **kwargs: Any) -> TagContextManager:
            html_context = weba_html_context.get(None)

            if html_context is None or str(html_context) == "None" or not callable(html_context.new_tag):
                html_context = Component()
                self._context_token = weba_html_context.set(html_context)

            # self._html = html_context

            if tag_name == "text":
                tag: Tag = html_context.new_string(str(args[0]))  # type: ignore
            else:
                tag: Tag = html_context.new_tag(tag_name, **kwargs)  # type: ignore
                html_context._append_to_context(tag._tag)  # type:ignore

            if args:
                tag.string = str(args[0])

            # tag = tag if hasattr(tag, "_tag") else TagContextManager(tag, html_context)

            if html_context._context_stack:  # type:ignore
                html_context._append_to_context(tag._tag)  # type:ignore
            elif not html_context._is_rendering:  # type:ignore
                html_context._last_component = tag  # type:ignore

            return cast(
                TagContextManager,
                tag,
            )

        return create_tag

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if hasattr(self, "_context_token") and self._context_token is not None:
            weba_html_context.reset(self._context_token)

        super().__exit__(exc_type, exc_val, exc_tb) # type: ignore


ui = UIFactory()
