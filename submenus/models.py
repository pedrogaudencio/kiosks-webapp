# -*- coding: utf-8 -*-

from django.db import models
from mezzanine.pages.models import Page
from mezzanine.pages.admin import PageAdmin
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class Submenus(Page):
	botoes = models.ManyToManyField(
        'Botoes',
        verbose_name=_('Botões'),
        null=False, 
        blank=False)


	class Meta:
		verbose_name = _('Submenu')
		verbose_name_plural = _('Submenus')


class Botoes(models.Model):
	titulo = models.CharField(_('Título'), 
        max_length=100)

	descricao = models.TextField(_('Descrição'), 
		max_length=300)


	def __unicode__(self):
		return "%s" % self.titulo

admin.site.register(Submenus, PageAdmin)
admin.site.register(Botoes)