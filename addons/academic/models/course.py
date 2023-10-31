from odoo import models, fields

class AcademicCourse(models.Model):
    _name = 'academic.course'
    _description = 'Academic Course'

    name = fields.Char('Name', required=True, size=100 )
    description = fields.Text('Description')
    responsible_id = fields.Many2one('res.users', string='Responsible', required=True)

    session_ids = fields.One2many(comodel_name="academic.session", string="Sessions", inverse_name="course_id")

    _sql_constraints = [('sql_cek_name', 'UNIQUE(name)', 'Name tidak boleh double!'),('sql_cek_desc', 'UNIQUE(description)', 'Desc tidak boleh sama')]