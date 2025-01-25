# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bangladesh - Accounting',
    'version': '16.0.1.0.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the latest basic Bangladeshi localisation necessary to run Odoo in Bangladesh:
======================================================================================

This module consists of:
 - Generic Bangladesh Chart of Accounts
 - Taxes and tax report
 - Multiple Fiscal positions
 """,
    'website': 'http://www.khan-store.com/shop',
    'depends': ['l10n_multilang'],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account_tax_group_data.xml',
        'data/account_account_tag.xml',
        'data/account.account.template.csv',
        'data/account.group.template.csv',
        'data/account_tax_report_data.xml',
        'data/account_tax_template_data.xml',
        'data/fiscal_templates_data.xml',
        'data/account_chart_template_post_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
