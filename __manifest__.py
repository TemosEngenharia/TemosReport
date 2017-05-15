# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    This module copyright (C) 2016 Temos Engenharia Ltda
#    (<http://temos.net>).
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
    'name': u'Temos - Central de Relatórios',
    'version': u'10.0.0.0.0',
    'author': u"Cezar José Sant'Anna Junior",
    'maintainer': u'Temos Engenharia Ltda',
    'website': u'http://temos.net',
    'license': u'AGPL-3',
    'category': u'Reporting',
    'summary': u'Permite a geração e envio dos relatórios no Odoo para a Temos Engenharia',
    'depends': ['base',
                'report_py3o',
                'temos_corretiva',
               ],
    'external_dependencies': {
        'python': ['py3o.fusion',
                   'py3o.renderserver',
                  ],
    },
    'data': ['data/report_corretiva.xml'],
    'demo': [],
    'test': [],
    'installable': True,
}
