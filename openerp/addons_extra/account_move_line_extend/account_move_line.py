from openerp.osv import fields, osv, orm
from openerp import pooler



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
    def _get_balance(self, cr, uid, ids,name, unknow_none, context=None):
        res = dict.fromkeys(ids, False)
        for line in self.browse(cr, uid, ids, context=context):
            debit = line.debit
            credit = line.credit
            res[line.id] = credit - debit
        return res
    
    _columns = {
                'balance': fields.function(_get_balance, type='float',digits=(16,2), string='Balance'),
                'accumulated': fields.function(_get_accumulated, type='float', digits=(16,2), string='accumulated'),
                }
    _order = "date, id"
    
    def list_accounts(self, cr, uid, context=None):
        ids = self.pool.get('account.account').search(cr,uid,[],0, None,('code'))
        lines = self.pool.get('account.account').browse(cr, uid, ids, context)
        res = []
        for line in lines:
            length  = 9 - len(line.code.strip())
            spaces = '&nbsp;' * length *2 + '&nbsp;'
            description = line.code + spaces + line.name
            res.append((line.id,description,line.code))
        #names = self.pool.get('account.account').name_get(cr, uid, ids, context)
        return res
    
    def print_extract(self, cr, uid, context=None):
        win_obj = self.pool.get('ir.actions.act_window')
        res = win_obj.for_xml_id(cr, uid, 'account', 'account_report_general_ledger_view', context)
        return res
        

    
account_move_line()