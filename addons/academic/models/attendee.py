from odoo import models, fields

class Attendee(models.Model):
    _name = 'academic.attendee'
    _description = 'Academic Attendee'

    name = fields.Char('Reg Number', required=True, size=100 )

    session_id = fields.Many2one(comodel_name="academic.session", string="Session")
    course_id = fields.Many2one(comodel_name="academic.course", string="Course", related="session_id.course_id", store=True)
    partner_id = fields.Many2one(comodel_name="res.partner", string="Partner")

    _sql_constraints = [('sql_cek_attendee', 'UNIQUE(session_id, partner_id)', 'Attendee tidak boleh double dalam 1 session')]