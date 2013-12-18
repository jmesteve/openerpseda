# -*- encoding: utf-8 -*-
##############################################################################
#
#    Base sale export partner module for OpenERP
#    Copyright (C) 2012 Akretion (http://www.akretion.com). All Rights Reserved
#    @author Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Base sale multichannels - Export partners',
    'version': '6.1.0',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'description': """This module contains a wizard to export one or several partners "manually" to an external shop such as a Magento shop, a PrestaShop boutique, Amazon or eBay.
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['connector_ecommerce'],
    'init_xml': [],
    'update_xml': [
        'wizard/export_partner.xml',
    ],
    'demo_xml': [],
    'installable': False,
    'active': False,
}
