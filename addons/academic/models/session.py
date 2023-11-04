from odoo import api, fields, models, exceptions
from datetime import date

STATES=[('draft','Draft'),('confirmed', 'Confirmed'),('done','Done')]
class Session(models.Model):
    _name = "academic.session"

    # def cari_tanggal(self0:
    #     return
    is_draft_state = fields.Boolean(string="Is Draft State", compute="_compute_is_draft_state", store=True)

    @api.depends('state')
    def _compute_is_draft_state(self):
        for record in self:
            record.is_draft_state = record.state == 'draft'

    name = fields.Char("Name", required=True, size=100, 
                      readonly=False, states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    course_id = fields.Many2one(comodel_name="academic.course", string="Course", 
                               readonly=False, states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    instructor_id = fields.Many2one(comodel_name="res.partner", string="Instructor", 
                                  readonly=False, states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    start_date = fields.Date("Start Date", readonly=False, 
                            states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    duration = fields.Integer("Duration", readonly=False, states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    seats = fields.Integer("Seats", readonly=False, states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    active = fields.Boolean("Is Active", default=True)

    attendee_ids = fields.One2many(comodel_name="academic.attendee", string="Attendee", inverse_name="session_id")
    
    taken_seats = fields.Float(string="Taken Seats", compute="_compute_taken_seats")

    image_small = fields.Binary("Image", readonly=False, states={'confirmed': [('readonly', True)], 'done': [('readonly', True)]})

    state = fields.Selection(string="State", selection=STATES, readonly=True, required=True, default=[0][0])

    # @api.depends('attendee_ids')
    def _compute_taken_seats(self):
        for x in self:
            if x.seats > 0:
                x.taken_seats = 100.0 * len(x.attendee_ids)/ x.seats
            else:
                x.taken_seats = 0.0

    @api.onchange('seats')
    def onchange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids)/ self.seats
        else:
            self.taken_seats = 0.0


    @api.constrains('instructor_id', 'attendee_ids')
    def _cek_instruktur(self):
        for session in self:
            attendee_ids = session.attendee_ids.mapped('partner_id.id')
            if session.instructor_id.id in attendee_ids:
                raise exceptions.ValidationError('Instruktur tidak boleh merangkap jadi Attendee')
            
    def copy(self, default=None):
        
        #modif field name
        default =dict(default or {}, name=self.name + " (copy)")
        return super(Session, self).copy(default=default)
    
    def action_confirm(self):
        self.state = STATES[1][0]

    def action_done(self):
        self.state = STATES[2][0]

    def action_draft(self):
        self.state = STATES[0][0]

    @api.model
    def create(self, vals):
        vals['state'] = 'draft'
        return super(Session, self).create(vals)