# -----------------------------------------------------------------------------
# Libraries
# -----------------------------------------------------------------------------
# Core libs
from typing import TYPE_CHECKING

# Third party libs
from rest_framework import serializers

# Project libs
from backend_test.utils.django.db.models.relation import get_relation_field

# If type checking, __all__
if TYPE_CHECKING:
    from typing import Any, Dict, List

    from django.db.models import Model

# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class UpdatableListModelSerializer(serializers.ListSerializer):
    """
    By default ListSerializer don't define the update method due to
    is unclear how to deal with insertions and deletions.
    For UpdatableListSerializer if the original object is:
    ```
    {
        "id": 9,
        "date": "2021-12-03",
        "food_dishes": [
            {
                "id": 19,
                "food": "Cereal"
            },
            {
                "id": 20,
                "food": "Chicken"
            },
        ]
    }
    ```
    And a update is sent with:
    ```
    {
        "id": 9,
        "date": "2021-12-03",
        "food_dishes": [
            {
                "id": 19,
                "food": "Cheerios cereal"
            },
            {
                "food": "Pastor Tacos"
            },
        ]
    }
    ```
    The food dish with id 20 will be deleted due is didn't send in the
    payload. The food dish with id 19 will be updated and the food dish
    Pastor Tacos will be created due to it don't include a id key.
    """

    id_key = "id"

    def update(
        self, instance: "Model", validated_data: "List[Dict[str, Any]]"
    ) -> "List[Model]":

        serializer: serializers.ModelSerializer = self.child  # type: ignore
        ModelClass = serializer.Meta.model
        relation_field = get_relation_field(ModelClass, instance._meta.model)
        assert relation_field is not None

        # Delete objects not present in validated data
        ModelClass.objects.exclude(
            id__in=[i[self.id_key] for i in validated_data if i.get(self.id_key)],
            menu_of_the_day=instance,
        ).delete()

        updated_or_created_objects: "List[Model]" = []
        for data in validated_data:
            # Update objs with id key
            if data.get(self.id_key):
                obj = ModelClass.objects.get(
                    id=data[self.id_key], menu_of_the_day=instance
                )
                serializer.update(instance=obj, validated_data=data)  # type: ignore
                updated_or_created_objects.append(obj)
            # Create objs without id key
            else:
                data[relation_field.name] = instance
                obj = serializer.create(validated_data=data)  # type: ignore
                updated_or_created_objects.append(obj)

        return updated_or_created_objects
