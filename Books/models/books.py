# -*- coding: utf-8 -*-

from odoo import fields, models


class Books(models.Model):
    _name = "books"
    _description = "Books Details"

    bookname = fields.Char('Book Name')
    ISBN = fields.Integer()
    price = fields.Integer()
    details = fields.Char('Books Details')


class BooksAuthor(models.Model):
    _name = "books.author"
    _description = "Books Authors Details"

    authors_id = fields.Integer()
    authors_name = fields.Char('Book Author')


class BooksPublisher(models.Model):
    _name = "books.publisher"
    _description = "Books Publisher"

    publishername = fields.Char()

class BooksCategory(models.Model):
    _name = "books.category"
    _description = "Books Category"

    books_id = fields.Integer()
    category = fields.Char()
    gener = fields.Char()