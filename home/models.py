from tabnanny import verbose
from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


class HomePage(Page):
    pass


@register_setting
class ColorsSettings(BaseSiteSetting):
    primary_color = models.CharField(
        "primary color",
        max_length=10,
        blank=True,
        default="#000000",
    )

    panels = [
        FieldPanel("primary_color"),
    ]

    class Meta:
        verbose_name = "Couleurs du site"
