# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .purchase import *


def register():
    Pool.register(
        ConfigurationRelationType,
        Configuration,
        Purchase,
        module='purchase_contact', type_='model')
