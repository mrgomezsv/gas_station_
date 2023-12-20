# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import re
from odoo.exceptions import ValidationError
from datetime import datetime, date, timedelta


class Stacion(models.Model):
    _name = 'nitro.gas.stacion'
    _description = 'Bomba'

    ticket_id = fields.Char(copy=False, default='New', readonly=True, string='No de Ticket')
    car_model = fields.Char(string='Modelo:')#required="True"
    number_plate = fields.Char(string='Placa:')
    cv = fields.Float(string='CV:')
    color = fields.Char(string='Color:')
    fuel_litres = fields.Float()

    @api.constrains('cv')
    def _validate_cv(self):
        if self.cv <= 0:
            raise exceptions.ValidationError('El valor de CV no puede ser menor o igual a 0')


    marca = fields.Selection([('T', 'Toyota'), ('N','Nissan'), ('M','Mitsubishi')], string='Marca de Fabricante')
    empty = fields.Boolean(string='Tanque Vacio')
    full = fields.Boolean(string='Tanque Lleno')

    @api.onchange('fuel_litres')
    def _check_under_fuel(self):
        if self.fuel_litres < 50:
            self.empty = True
            self.full = False
        else:
            self.empty = False
            self.full = True

    customer = fields.Many2one(comodel_name='res.partner', string='Nombre del Cliente', required="True")


    @api.depends('customer.phone')
    def _check_depends(self):
        mess = "Se a ejecutado @api.depends"
        raise ValidationError(mess)
        print('SE A EJECUTADO @API.DEPENDS ')
        _logger.info('SE A EJECUTADO @API.DEPENDS ')
        #Basicamente cuando se ejecuta un cambio en el telefono del cliente se ejecuta depends

    @api.model
    def create(self, vals):
        if vals.get('ticket_id', 'New') == 'New':
            vals['ticket_id'] = self.env['ir.sequence'].next_by_code('task.lfpv') or 'New'

            result = super(Stacion, self).create(vals)
            return result