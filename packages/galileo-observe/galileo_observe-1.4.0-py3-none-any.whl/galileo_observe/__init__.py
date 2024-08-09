"""Galileo Observe"""

# flake8: noqa: F401
# ruff: noqa: F401
from galileo_core.helpers.dependencies import is_dependency_available

from galileo_observe.monitor import GalileoObserve
from galileo_observe.utils import __version__

if is_dependency_available("langchain_core"):
    from galileo_observe.async_handlers import GalileoObserveAsyncCallback
    from galileo_observe.handlers import GalileoObserveCallback
