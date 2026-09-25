# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_es_reports_pos_session_ids = fields.One2many(
        comodel_name='pos.session',
        inverse_name='move_id',
        string="PoS sessions technical field",
    )
