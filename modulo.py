from osv import osv
from osv import fields
import time
import openerp.addons.decimal_precision as dp
from openerp import tools, SUPERUSER_ID

class modulo(osv.osv):

    def _get_image(self, cr, uid, ids, name, args, context=None):
        result = dict.fromkeys(ids, False)
        for obj in self.browse(cr, uid, ids, context=context):
            result[obj.id] = tools.image_get_resized_images(obj.image, avoid_resize_medium=True)
        return result

    def _set_image(self, cr, uid, id, name, value, args, context=None):
        return self.write(cr, uid, [id],{'image': tools.image_resize_image_big(value)}, context=context)

    _defaults = {
        'color': 0,
    }
    _name = 'modulo'
    _description = 'modulo de prueba' 
    _columns = {
        'name':fields.char('Name', size=64),
        'type' : fields.selection([('unit','Unit'),('pack','Pack'),('box', 'Box'), ('pallet', 'Pallet')], 'Type', required=True),
        'name_id':fields.boolean('Label', required=True),
        'list_price': fields.float('Sale Price', digits_compute=dp.get_precision('Product Price'), help="Base price to compute the customer price. Sometimes called the catalog price."),
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
        'color': fields.integer('Color Index'),
        'image': fields.binary("Image",
            help="This field holds the image used as image for the product, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized image", type="binary", multi="_get_image",
            store={
                'modulo': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized image of the product. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved, "\
                 "only when the image exceeds one of those sizes. Use this field in form views or some kanban views."),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized image", type="binary", multi="_get_image",
            store={
                'modulo': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized image of the product. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),

	}

modulo()
