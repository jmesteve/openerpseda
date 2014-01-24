from openerp.osv import fields, osv, orm




class account_move_line(osv.osv):
    _inherit = "account.move.line"
    
    def _get_accumulated(self, cr, uid, ids,name, unknow_none, context=None):
        res = dict.fromkeys(ids, False)
        accumulated = 0
        for line in self.browse(cr, uid, ids, context=context):
            debit = line.debit
            credit = line.credit
            accumulated += debit - credit
            res[line.id] = accumulated
        return res
    _columns = {
                'accumulated': fields.function(_get_accumulated, type='float', string='accumulated'),
                
                }