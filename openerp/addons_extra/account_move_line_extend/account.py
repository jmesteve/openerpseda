from openerp.osv import fields, osv
from openerp.tools.translate import _

class account_account(osv.osv):
    _inherit = "account.account"
    
    def change_code(self, cr, uid, ids, context=None):
        line_obj = self.pool.get('account.move.line')
        for account in self.browse(cr, uid, ids, context=context):
            account_ids = self.search(cr, uid, [('id', 'child_of', [account.id])], context=context)
            if line_obj.search(cr, uid, [('account_id', 'in', account_ids)], context=context):
                result = "You cannot change the code of account which contains journal items!"
                return {'value':True,'warning':{'title':'warning','message':result}}
        return True
    
    def _check_allow_code_change(self, cr, uid, ids, context=None):
        #line_obj = self.pool.get('account.move.line')
        #for account in self.browse(cr, uid, ids, context=context):
            #account_ids = self.search(cr, uid, [('id', 'child_of', [account.id])], context=context)
            #if line_obj.search(cr, uid, [('account_id', 'in', account_ids)], context=context):
                #raise osv.except_osv(_('Warning !'), _("You cannot change the code of account which contains journal items!"))
        return True
    
