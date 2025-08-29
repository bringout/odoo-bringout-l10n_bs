from odoo import api, models

class AccountMove(models.Model):
    _inherit = "account.move"

    def _compute_is_storno(self):
        for move in self:
            move.is_storno = move.is_storno \
                    or (move.ref and move.ref[:8] == "#STORNO#") 
        return super(AccountMove, self)._compute_is_storno()
