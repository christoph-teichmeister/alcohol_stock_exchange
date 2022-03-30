from enum import Enum, unique, auto

from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

from core import settings


@unique
class ModelKey(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self  # self was named 'name' before

    BEVERAGE_MODEL = auto()
    STOCK_PRICE_MODEL = auto()
    STOCK_MODEL = auto()


def get_model(model_name: str):
    try:
        return django_apps.get_model(getattr(settings, model_name), require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            f"{model_name} must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            f"{model_name} refers to model '{getattr(settings, model_name)}' that has not been installed"
        )


def get_beverage_model():
    """Return the Beverage model that is active in this project."""
    return get_model(model_name=ModelKey.BEVERAGE_MODEL.value)


def get_stock_price_model():
    """Return the StockPrice model that is active in this project."""
    return get_model(model_name=ModelKey.STOCK_PRICE_MODEL.value)


def get_stock_model():
    """Return the Stock model that is active in this project."""
    return get_model(model_name=ModelKey.STOCK_MODEL.value)
