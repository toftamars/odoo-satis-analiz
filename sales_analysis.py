from odoo import models, fields, api

class SalesAnalysis(models.Model):
    _name = 'sales.analysis'
    _description = 'Sales Analysis'

    name = fields.Char(string='Analysis Name', required=True)
    date_from = fields.Date(string='From Date')
    date_to = fields.Date(string='To Date')
    customer_id = fields.Many2one('res.partner', string='Customer')
    product_id = fields.Many2one('product.product', string='Product')
    total_sales = fields.Float(string='Total Sales', compute='_compute_total_sales')
    average_order_value = fields.Float(string='Average Order Value', compute='_compute_average_order_value')

    @api.depends('date_from', 'date_to', 'customer_id', 'product_id')
    def _compute_total_sales(self):
        for record in self:
            domain = []
            if record.date_from:
                domain.append(('date_order', '>=', record.date_from))
            if record.date_to:
                domain.append(('date_order', '<=', record.date_to))
            if record.customer_id:
                domain.append(('partner_id', '=', record.customer_id.id))
            if record.product_id:
                domain.append(('order_line.product_id', '=', record.product_id.id))

            sales = self.env['sale.order'].search(domain)
            record.total_sales = sum(sales.mapped('amount_total'))

    @api.depends('total_sales')
    def _compute_average_order_value(self):
        for record in self:
            domain = []
            if record.date_from:
                domain.append(('date_order', '>=', record.date_from))
            if record.date_to:
                domain.append(('date_order', '<=', record.date_to))
            if record.customer_id:
                domain.append(('partner_id', '=', record.customer_id.id))
            if record.product_id:
                domain.append(('order_line.product_id', '=', record.product_id.id))

            sales = self.env['sale.order'].search(domain)
            record.average_order_value = record.total_sales / len(sales) if sales else 0.0 