from django.db import models
from django.utils.translation import ugettext_lazy as _


class ParamsModel(models.Model):
    token = models.CharField(_('Token'), max_length=100)
    owner_id = models.IntegerField(_('Owner_id'))
    group_id = models.IntegerField(_('Group_id'))
    category_id = models.IntegerField('Category_id')
    version = models.FloatField(_('Version'))

    def __str__(self):
        return str(self.owner_id)

    class Meta:
        verbose_name = 'Param'
        verbose_name_plural = 'Params'
