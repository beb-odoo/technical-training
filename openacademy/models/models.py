from odoo import models, fields, api, exceptions

class openacademy(models.Model):
    _name = 'openacademy.openacademy'
    _description = 'OpenAcademy OpenAcademy'
    
class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'
    # A course has a name and a description
    name=fields.Char(string='Title', required=True)
    description = fields.Text()
    # create an index based on the responsible_id column
    # each course has only one responsible user but a user might be responsible for multiple course
    responsible_id = fields.Many2one('res.partner', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    level = fields.Selection([('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], string="Difficulty Level")

    # with _sql_constraints of name uniqueness, we can't use the Form->Duplicate anymore
    # hence redefine the copy function to change the name automatically when duplicating
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})
        
        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)
            
            default['name'] = new_name
            return super(Course, self).copy(default)


    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),
        
        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]


    
class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"
    # A session has a name a start_date, a duration and a number of seats for the attendees
    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    # each session has only one instructor but an instructor might deliver multiple sessions
    # use of domain to restrict valid records for the relationship
    instructor_id = fields.Many2one('res.partner', string="Instructor",
                                    domain=['|', ('instructor', '=', True),('category_id.name', 'ilike', "Teacher")])
    # each session has only one course but multiple session might be scheduled for a given course
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    # A session has multiple attendees and each attendee might be scheduled for multiple sessions
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    # Demonstrate coumputed field with % of taken seats
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')


    state = fields.Selection([
                    ('draft', "Draft"),
                    ('confirmed', "Confirmed"),
                    ('done', "Done"),
                    ], default='draft')


    # taken_seats is dependant of seats and attendee_ids
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
                                                            

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available seats may not be negative",
                },
            }
        if self.seats < len(attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }
        

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")

    
