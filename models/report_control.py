# -*- coding: utf-8 -*-
"""Este modulo tem como funcao definir as Classes e metodos para
acompanhamento do estado dos relatorios recebidos via e-mail do officetrack
e sua importacao para o Odoo"""

from odoo import models, fields


class TemosReportBase(models.Model):
    """Modelo para controle dos relatórios"""

    _name = 'temos_report.base'
    _rec_name = 'event_name'

    active = fields.Boolean(default = True)
    event_name = fields.Char(string = u'Código INC ou TASK')
    process_id = fields.Char(string = u'Último processo que modificou esta entrada')
    mail_in_from = fields.Char(string = u'Remetende do e-mail')
    mail_in_to = fields.Char(string = u'Destinatário do e-mail')
    mail_in_subject = fields.Char(string = u'Assundo do e-mail de Entrada')
    mail_in_status_id = fields.Many2one('temos_report.mail_status',
                                     u'Estado do e-mail de entrada',
                                     ondelete = "cascade")
    mail_in_date = fields.Datetime(string = u'Data do recebimento do e-mail de entrada')
    mail_in_filename = fields.Char(string = u'Local onde o e-mail de entrada foi armazenado')
    xml_status_id = fields.Many2one('temos_report.xml_status',
                                     u'Estado do arquivo XML de entrada',
                                     ondelete = "cascade")
    xml_create_date = fields.Datetime(string = u'Data da criação do arquivo XML')
    xml_filename = fields.Char(string = u'Local onde o XML foi armazenado')
    importer_status_id = fields.Many2one('temos_report.importer_status',
                                     u'Estado da importação do arquivo XML',
                                     ondelete = "cascade")
    importer_date = fields.Datetime(string = u'Data em que o XML foi importado no Odoo')
    import_record_id = fields.Integer(string = u'ID no Odoo referente ao XML importado')
    report_status_id = fields.Many2one('temos_report.pdf_status',
                                     u'Estado do arquivo XML de entrada',
                                     ondelete = "cascade")
    report_create_date = fields.Datetime(string = u'Data da criação do arquivo PDF')
    report_pdf_filename = fields.Char(string = u'Local onde foi armazendo o PDF')
    mail_out_from = fields.Char(string = u'Remetende do e-mail de saída')
    mail_out_to = fields.Char(string = u'Destinatário do e-mail de saída')
    mail_out_subject = fields.Char(string = u'Assundo do e-mail de saída')
    mail_out_status_id = fields.Many2one('temos_report.mail_status',
                                     u'Estado do e-mail de saída',
                                     ondelete = "cascade")
    mail_out_date = fields.Datetime(string = u'Data de envio do e-mail de saída')
    mail_out_filename = fields.Char(string = u'Local onde foi armazenado o e-mail de saída')

class TemosReportMailStatus(models.Model):
    """Modelo para os estados de um e-mail"""

    _name = 'temos_report.mail_status'

    active = fields.Boolean(default = True)
    name = fields.Char(string = u'Nome')
    description = fields.Char(string = u'Descrição')

class TemosReportXMLStatus(models.Model):
    """Modelo para os estados de um arquivo XML"""

    _name = 'temos_report.xml_status'

    active = fields.Boolean(default = True)
    name = fields.Char(string = u'Nome')
    description = fields.Char(string = u'Descrição')

class TemosReportImporterStatus(models.Model):
    """Modelo para os estados da importação arquivo XML"""

    _name = 'temos_report.importer_status'

    active = fields.Boolean(default = True)
    name = fields.Char(string = u'Nome')
    description = fields.Char(string = u'Descrição')

class TemosReportPDFStatus(models.Model):
    """Modelo para os estados da importação arquivo XML"""

    _name = 'temos_report.pdf_status'

    active = fields.Boolean(default = True)
    name = fields.Char(string = u'Nome')
    description = fields.Char(string = u'Descrição')

class TemosReportMailDest(models.Model):
    """Modelo para controle dos relatórios"""

    _name = 'temos_report.mail_dest'

    active = fields.Boolean(default = True)
    name = fields.Char(string = u'Nome do destinatário do Relatório em PDF')
    email = fields.Char(string = u'Email do destinatário do Relatório em PDF')
    report_type_ids = fields.Many2many('temos_report.report_type',
                                     'temos_report_maildest_reporttype_rel',
                                     'mail_dest_ids', 'report_type_ids')

class TemosReportReportType(models.Model):
    """Modelo para controle dos relatórios"""

    _name = 'temos_report.report_type'

    active = fields.Boolean(default = True)
    report_code = fields.Char(string = u'Código de indentificação do relatório')
    name = fields.Char(string = u'Nome do Formulário no OfficeTrack')
    mail_dest_ids = fields.Many2many('temos_report.mail_dest',
                                     'temos_report_maildest_reporttype_rel',
                                     'report_type_ids', 'mail_dest_ids')
