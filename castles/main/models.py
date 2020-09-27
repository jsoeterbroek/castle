from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Castle(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    itype = models.CharField(_("type"), max_length=25)
    iid = models.CharField(_("id"), max_length=25)
    geometry_type = models.CharField(_("Geometry type"), max_length=25)
    geometry_coords_x = models.IntegerField(_("geometry coordinates x-axis"))
    geometry_coords_y = models.IntegerField(_("geometry coordinates y-axis"))
    geometry_name = models.CharField(_("geometry_name"), max_length=25)
    gid = models.IntegerField(_("gid"))
    cchin = models.IntegerField(_("cchin"))
    naam = models.CharField(_("naam"), max_length=255, unique=True)
    plaats = models.CharField(_("plaats"), max_length=255)
    info_link = models.CharField(_("info link"), max_length=255)
    datering_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900),
                    MaxValueValidator(datetime.now().year)], help_text="Use the following format: <YYYY>")
    rijksmonnr = models.IntegerField(_("Rijksmonnr"))
    provincie = models.CharField(_("provincie"), max_length=25)
    foto_thumb = models.CharField(_("foto_thumb"), max_length=255)
    foto_groot = models.CharField(_("foto_groot"), max_length=255)
    bijschrift = models.CharField(_("bijschrift"), max_length=255)
    zichtbaar = models.BooleanField(_("zichtbaar"), default=False)
    legenda = models.CharField(_("legenda"), max_length=255)
    typering = models.CharField(_("typering"), max_length=255)

    def __str__(self):
        return str(self.naam)

    class Meta:
        verbose_name = _("Castle")
        verbose_name_plural = _("Castles")
