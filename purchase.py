# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields, ModelSQL
from trytond.pool import PoolMeta
from trytond.modules.account_invoice_contact.invoice import ContactMixin

__all__ = ['ConfigurationRelationType', 'Configuration', 'Purchase']
__metaclass__ = PoolMeta


class ConfigurationRelationType(ModelSQL):
    'Purchase Configuration - Party relation type'
    __name__ = 'purchase.configuration-party.relation.type'

    relation = fields.Many2One('party.relation.type', 'Relation Type',
        required=True, select=True)
    config = fields.Many2One('purchase.configuration', 'Config',
        required=True, select=True)


class Configuration:
    __name__ = 'purchase.configuration'

    relation_types = fields.Many2Many(
        'purchase.configuration-party.relation.type', 'config',
        'relation', 'Contact types')


class Purchase(ContactMixin):
    __name__ = 'purchase.purchase'
    _contact_config_name = 'purchase.configuration'

    def _get_invoice_purchase(self):
        invoice = super(Purchase, self)._get_invoice_purchase()
        if self.contact:
            invoice.contact = self.contact
        return invoice
