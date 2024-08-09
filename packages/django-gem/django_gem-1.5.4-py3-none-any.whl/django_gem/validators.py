import inspect
import typing

from django.db import models

from django_gem.exceptions import (
    CutterClassFieldMissingException,
    CutterFieldMissingException,
    CutterTriggerMixinMissingException,
    UnusedCutterMethodException,
)
from django_gem.logger import logger
from django_gem.models.base import CutterEngineBaseModel, CutterSideEffect
from django_gem.models.mixins import GemTriggerMixin
from django_gem.toolkit import gem_settings


class CutterEngineValidator:
    def __init__(self, gem_class: typing.Type[CutterEngineBaseModel]):
        self.gem_class = gem_class
        self.model = gem_class.CutterEngineMeta.model
        self.self_affected_fields = gem_class.CutterEngineMeta.self_affected_fields
        self.propagate_triggers = gem_class.CutterEngineMeta.propagate_triggers
        self.cutter = gem_class.CutterEngineMeta.cutter
        self.side_effects = gem_class.CutterEngineMeta.side_effects

    def validate_cutter_methods(self):
        for cutter_method_name in self.cutter.__dict__.keys():
            if not cutter_method_name.startswith(gem_settings.CUTTER_PROPERTY_PREFIX):
                continue
            field_name = cutter_method_name[len(gem_settings.CUTTER_PROPERTY_PREFIX) :]  # noqa
            if not hasattr(self.gem_class, field_name):
                self.raise_exception(
                    UnusedCutterMethodException(
                        cutter_class=self.cutter,
                        field_name=field_name,
                    )
                )

    def validate_self_fields(self):
        for self_affected_field in self.self_affected_fields:
            if not hasattr(self.model, self_affected_field):
                self.raise_exception(
                    CutterFieldMissingException(
                        model_class=self.model,
                        field_name=self_affected_field,
                    )
                )
        for propagate_trigger_key, propagate_trigger_values in self.propagate_triggers.items():
            if not hasattr(self.gem_class, propagate_trigger_key):
                self.raise_exception(
                    CutterFieldMissingException(
                        model_class=self.gem_class,
                        field_name=propagate_trigger_key,
                    )
                )
            if not hasattr(
                self.cutter, f"{gem_settings.CUTTER_PROPERTY_PREFIX}{propagate_trigger_key}"
            ):
                self.raise_exception(
                    CutterClassFieldMissingException(
                        cutter_class=self.cutter,
                        field_name=propagate_trigger_key,
                    )
                )
            for propagate_trigger_value in propagate_trigger_values:
                if not hasattr(self.gem_class, propagate_trigger_value):
                    self.raise_exception(
                        CutterFieldMissingException(
                            model_class=self.gem_class,
                            field_name=propagate_trigger_value,
                        )
                    )
                if not hasattr(
                    self.cutter, f"{gem_settings.CUTTER_PROPERTY_PREFIX}{propagate_trigger_value}"
                ):
                    self.raise_exception(
                        CutterClassFieldMissingException(
                            cutter_class=self.cutter,
                            field_name=propagate_trigger_value,
                        )
                    )

    def validate_side_effect_fields(self, side_effect: CutterSideEffect):
        side_effect_model: typing.Type[models.Model] = side_effect.model
        for affected_field in side_effect.affected_fields:
            if not hasattr(side_effect_model, affected_field):
                self.raise_exception(
                    CutterFieldMissingException(
                        model_class=side_effect_model,
                        field_name=affected_field,
                    )
                )
        if not side_effect.gem_fields:
            return
        for gem_field in side_effect.gem_fields:
            if not hasattr(self.gem_class, gem_field):
                self.raise_exception(
                    CutterFieldMissingException(
                        model_class=self.gem_class,
                        field_name=gem_field,
                    )
                )
            if not hasattr(self.cutter, f"{gem_settings.CUTTER_PROPERTY_PREFIX}{gem_field}"):
                self.raise_exception(
                    CutterClassFieldMissingException(
                        cutter_class=self.cutter,
                        field_name=gem_field,
                    )
                )

    @classmethod
    def validate_side_effect_model(cls, side_effect: CutterSideEffect):
        side_effect_model = side_effect.model
        if inspect.isclass(side_effect_model) and not issubclass(
            side_effect_model, GemTriggerMixin
        ):
            cls.raise_exception(
                CutterTriggerMixinMissingException(
                    model_class=side_effect_model,
                )
            )

    @classmethod
    def raise_exception(cls, exception):
        if gem_settings.CUTTER_VALIDATION_ENABLED:
            raise exception
        logger.warning(exception)

    def validate(self):
        self.validate_self_fields()
        self.validate_cutter_methods()
        for side_effect in self.side_effects:
            self.validate_side_effect_fields(side_effect)
            self.validate_side_effect_model(side_effect)
