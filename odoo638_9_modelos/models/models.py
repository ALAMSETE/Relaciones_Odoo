# -*- coding: utf-8 -*-

from odoo import models, fields, api

class conductores638(models.Model):
	_name = 'odoo638_9_modelos.conductores638'
	_description = 'model conductores638'

	name = fields.Char('Dni',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	jefe_id=fields.Many2one('odoo638_9_modelos.jefes638', string='Jefe')
	camion_id=fields.Many2one('odoo638_9_modelos.camiones638', string='Camion')
	furgon_id=fields.Many2one('odoo638_9_modelos.furgones638', string='Furgon')

class camiones638(models.Model):
	_name = 'odoo638_9_modelos.camiones638'
	_description = 'model camiones638'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	conductors_ids=fields.One2many('odoo638_9_modelos.conductores638', 'camion_id',string='Conductor')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class jefes638(models.Model):
	_name = 'odoo638_9_modelos.jefes638'
	_description = 'model jefes638'

	name = fields.Char('Dni',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	conductores_ids=fields.One2many('odoo638_9_modelos.conductores638', 'jefe_id',string='Conductor')

class furgones638(models.Model):
	_name = 'odoo638_9_modelos.furgones638'
	_description = 'model furgones638'

	name = fields.Char('Matricula',required=True)
	marca = fields.Char(string='Marca',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	conductores_ids=fields.One2many('odoo638_9_modelos.conductores638', 'furgon_id',string='Conductor')