from django.db import models
from django.utils.translation import gettext_lazy as _


class ToDo(models.Model):
    title = models.CharField(
        _('title'), max_length=255, blank=False, null=False,
    )
    description = models.TextField(_('description'), blank=True)
    done = models.BooleanField(_('done'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _('ToDo')
        verbose_name_plural = _('ToDos')

    def __str__(self):
        return f'{self.title} - done: {self.done}'
