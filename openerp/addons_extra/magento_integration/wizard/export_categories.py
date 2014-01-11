# -*- coding: utf-8 -*-
"""
    import_catalog

    Import catalog

    :copyright: (c) 2013 by Openlabs Technologies & Consulting (P) Limited
    :license: AGPLv3, see LICENSE for more details.
"""
from magento.catalog import Category, Product
from openerp.osv import osv, fields
from openerp.tools.translate import _



class ExportCategories(osv.TransientModel):
    "Export Categories"
    _name = 'magento.instance.export_categories'

    _columns = dict(
        categories=fields.many2many(
            'product.category', 'website_category_rel', 'website', 'categories',
            'Products', required=True, domain=[('magento_ids', '=', None)],
        ),
    )


    def export_categories(self, cursor, user, ids, context):
        """
        Import the product categories and products

        :param cursor: Database cursor
        :param user: ID of current user
        :param ids: List of ids of records for this model
        :param context: Application context
        """
        Pool = self.pool
        website_obj = Pool.get('magento.instance.website')

        website = website_obj.browse(
            cursor, user, context['active_id'], context
        )
        
        record = self.browse(cursor, user, ids[0], context=context)
         
        data = {
                    'name': 'hola',
                    'is_active':1,
                    'available_sort_by':1,
                    'default_sort_by':1,
                    'include_in_menu':1,
                    
                    }
        parent = 1

        idMagento = self.category_create(cursor, user, website, parent, data, context)
        
        
        return idMagento
        #product_ids = self.import_products(cursor, user, website, context)

        #return self.open_products(
            #cursor, user, ids, product_ids, context
        #)
        
    def category_tree(self, cursor, user, website, context):
        """
        Imports category tree

        :param cursor: Database cursor
        :param user: ID of current user
        :param website: Browse record of website
        :param context: Application context
        """
        category_obj = self.pool.get('product.category')

        instance = website.instance
        context.update({
            'magento_instance': instance.id
        })

        with Category(
            instance.url, instance.api_user, instance.api_key
        ) as category_api:
            category_tree = category_api.tree(website.magento_root_category_id)

            category_obj.create_tree_using_magento_data(
                cursor, user, category_tree, context
            )
    def category_info(self, cursor, user, website,id, context):
        """
        Imports category tree

        :param cursor: Database cursor
        :param user: ID of current user
        :param website: Browse record of website
        :param context: Application context
        """
        
        instance = website.instance
        context.update({
            'magento_instance': instance.id
        })

        with Category(
            instance.url, instance.api_user, instance.api_key
        ) as category_api:
            category_info = category_api.info(id)
        return category_info
    
    def category_create(self, cursor, user, website,parent,data, context):
        """
        Imports category tree

        :param cursor: Database cursor
        :param user: ID of current user
        :param website: Browse record of website
        :param context: Application context
        """
        
        instance = website.instance
        context.update({
            'magento_instance': instance.id
        })
            
        with Category(
            instance.url, instance.api_user, instance.api_key
        ) as category_api:
            category_delete = category_api.create(parent,data)
        return category_delete

    def category_delete(self, cursor, user, website,id, context):
        """
        Imports category tree

        :param cursor: Database cursor
        :param user: ID of current user
        :param website: Browse record of website
        :param context: Application context
        """
        
        instance = website.instance
        context.update({
            'magento_instance': instance.id
        })

        with Category(
            instance.url, instance.api_user, instance.api_key
        ) as category_api:
            category_delete = category_api.delete(id)
        return category_delete
ExportCategories()
