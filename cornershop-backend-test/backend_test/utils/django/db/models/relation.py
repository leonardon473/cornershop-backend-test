# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs

# Project libs


# App libs

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Optional
    from django.db.models import Model
    from django.db.models.fields import Field

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


def get_relation_field(model_from: "Model", model_to: "Model") -> "Optional[Field]":
    """
    Func for find relation field between two models.
    """
    for field in model_from._meta.fields:
        if field.related_model == model_to:
            return field

    return None
