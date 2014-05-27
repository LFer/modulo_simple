from osv import osv
from osv import fields
import time

class modulo(osv.osv):
    _name= 'modulo'
    _description = 'modulo de prueba' 
    _columns = {
        'name':fields.char('Name', size=64),
        'name_id':fields.boolean('Label', required=True),
        'option_id':fields.text('texto plano', size=65),
        'aadfixed_place_of_payment':fields.char('Place of payment', required=True),
        'aadfixed_unit':fields.integer('Units',size=5),
        'aadfixed_datetime':fields.datetime('Date and time', required=True),
        'aadfixed_unit_amount':fields.float('Unit amount',digits=(15,2)),
        'aadfixed_total_amount':fields.float('Total amount',digits=(15,2)),
        'res_company':fields.many2one('res.company','Compania'),
        'res_currency':fields.many2one('account.tax', 'Moneda', required=True),
        'res_partner':fields.many2one('res.partner', 'Companiero'),
        'account':fields.many2one('account.account', 'Cuenta'),
        'account_temp':fields.many2one('account.account.template','Templada'),
        'mail':fields.many2one('mail.mail','Mail'),
        'pricelist':fields.many2one('product.product', 'Ventas', required=True),
        'ate':fields.date('Fecha'),
        'campo_id':fields.many2one('res.bank', 'Portal'),
        'producto_ids':fields.many2one('product.pricelist', 'Productos'),
        'umo_id':fields.many2one('product.uom', 'Tipo de medida', required=True),
        'duration': fields.float('Duration (in hours)'),
        }
modulo()
