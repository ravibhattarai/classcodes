# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class Books(models.Model):
    _name = "books"
    _description = "Books Details"

    books_id = fields.Integer()
    bookname = fields.Char('Book Name')
    isbn = fields.Integer()
    price = fields.Integer()
    authors_id = fields.Integer()
    authors_name = fields.Char('Book Author')
    details = fields.Char('Books Details')
    category = fields.Char()
    gener = fields.Char()
    publishername = fields.Char()

class BooksPublishers(models.Model):
    _name = "books.publishers"
    _description = "Publishers Details"

    publishers_id = fields.Integer()
    publishername = fields.Char()

class BooksCategory(models.Model):
    _name = "books.category"
    _description = "Books Category"

    category = fields.Char()
    gener = fields.Char()

class Authors(models.Model):
    _name = "books.authors"
    _description = "Authors Details"

    authors_id = fields.Integer()
    authors_name = fields.Char('Book Author')

class BooksBorrow(models.Model):
    _name = "books.borrow"
    _description = "Books Borrow"

    boroowdate = fields.Date()
    boowername = fields.Char()

class BooksReturn(models.Model):
    _name = "books.return"
    _description = "Books Return"

    returndate = fields.Date()
    borrowername = fields.Char()


class Library(models.Model):
    _name = 'books.library'
    _description = 'Library Transactions'
    _sql_constraints = [('isbn_unique', 'unique(isbn)', 'Duplicate isbn not allowed')]

    name = fields.Char(string="Book Name", default="Book", required=True)
    book_description = fields.Text()
    isbn = fields.Integer()
    price = fields.Float()
    author_ids = fields.Many2many('author')
    category_id = fields.Many2one('books.category')
    publisher_id = fields.Many2one('books.publisher')
    date = fields.Date()
    state = fields.Selection([('new', 'New'), ('issued', 'Issued'), ('cancel', 'Cancel')], default='new')

    def action_issued(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Book is cancel")
            record.state = 'issued'

    def action_cancel(self):
        for record in self:
            if record.state == 'issued':
                raise UserError("Book is issued")
            record.state = 'cancel'


class BookIssue(models.Model):
    _name = 'book.issue'
    _description = 'Book issued'

    name = fields.Char(default="User", required=True)
    email = fields.Char()
    address = fields.Text()
    issue_date = fields.Date()
    ret_date = fields.Date()
    dept_ids = fields.Many2one('books.department', 'department_id')
    cat_ids = fields.Many2one('books.category', 'category_id')
    image = fields.Image()
    rem_days = fields.Char(string="Count Days", readonly=True)
    penlaty = fields.Char(string="Penlaty", readonly=True)

    @api.onchange('ret_date')
    def _onchange_ret_date(self):
        for record in self:
            if record.ret_date:
                date_format = "%Y-%m-%d"
                book_issued_date = datetime.strptime(str(record.issue_date), date_format)
                book_return_date = datetime.strptime(str(record.ret_date), date_format)
                cntdays = book_return_date - book_issued_date
                x = str(cntdays).split(",")[0]
                print(x.split("days")[0])
                y = x.split("days")[0]
                c = int(y) * 10
                record.rem_days = int(y)
                record.penlaty = c

            else:
                pass
                # record.rem_days = 0