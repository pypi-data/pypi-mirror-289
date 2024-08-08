from traceback import format_exc
from typing import Callable
from .abstract import abstract_application
from .layout import layout_factory
from .state import State
from . import utils, signals
from squiffy.context import executor, context2


class Application(abstract_application.AbstractApplication):
    def __init__(self, layout: layout_factory.LayoutFactory, state: State) -> None:
        self._layout = layout
        self._context = context2.Context(master=self)

        self._menu = self._layout.create()
        self._menu._context = self._context

        # self._menu_wrapper = menu_layers.MenuObserversLayer(self._menu)

        # States
        self._running: bool = True
        self._state: State = state

    def run(self) -> None:
        while self._running:
            try:
                self._menu.show()
                self._running = self._menu.is_running
            except KeyboardInterrupt:
                self._running = False

    def add(self, function: Callable, option_name: str, submenu_name: str) -> None:
        # Create rounting observers and Executors for the signal signature and the function
        signal_signature: str = utils.generate_signal_name(submenu_name, option_name)
        exe = executor.Executor(signals.Do(signal_signature), function)

        # Add the rounting observer and the executor to the context
        # The observers will get the signature of the context (self) and
        # interact with it directly.
        self._context.executors = exe

    def handle_errors(self, error: signals.Error) -> None:
        # self._save_state()
        self._menu.handle_errors(error)

    def handle_ok(self, signal: signals.OK) -> None:
        if signal.is_payload():
            self._state.load(signal.payload)

    def handle_quit(self) -> None:
        self._running = False
        self._save_state()

    def handle_abort(self) -> None:
        pass

    def provide_state(self):
        return self._state

    def _save_state(self) -> None | signals.Error:
        try:
            self._state.save()
        except Exception:
            self.handle_errors(
                signals.Error(
                    origin="Application",
                    log_message="An error occured during state saving",
                    traceback=format_exc(),
                )
            )
