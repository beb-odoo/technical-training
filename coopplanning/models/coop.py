from odoo import models, fields


class task_desc(models.Model):
    _name = 'coop.task.desc'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text()
    area = fields.Char(string='Area')
    active = fields.Boolean(default=True)


class volunteers(models.Model):
    _name='coop.volunteers'
    name = fields.Char(string='Volunteer Name', required=True)


class task_day(models.Model):
    _name = 'coop.task.day'

    name = fields.Char()
    number = fields.Integer(string="Day Number", help="From 1 to N, When you will instanciate your planning, Day 1 will be the start date of the instance, Day 2 the second, etc...")
    active = fields.Boolean(default=True)
    
class task_template(models.Model):
    _name = 'coop.task.template'

    name = fields.Char(string='Job', required=True)
    workers_nb = fields.Integer(string='Number of workers', help="Max number of worker for this task", default=1)
    workers_id = fields.Many2many(comodel_name='res.partners', string='workers list')
    day_id = fields.Many2one(comodel_name='coop.task.day', string='day id')
    task_type = fields.Many2one(comodel_name='coop.task.desc', string='task type')
    duration = fields.Float(string='Duration', help='Duration in Hour')
    start_time = fields.Float()
    active = fields.Boolean(default=True)



    
