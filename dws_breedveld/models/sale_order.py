# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    config_values = fields.Many2many('product.attribute.value', string='Attribute Values', compute='_compute_config_values')

    def _compute_config_values(self):
        self.config_values = False
        for record in self:
            if record.product_id:
                record.config_values = record.config_session_id.value_ids.ids

                print("--------------------")
                for value in record.config_session_id.custom_value_ids:
                    
                    print("value type: " + str(type(value)) )
                    # print("value.name: " + str(value.name))
                    # print("value.attribute_id.name: " + str(value.attribute_id.name))
                    print("value.attribute_id.custom_type: " + str(value.attribute_id.custom_type))
                    # print("value.attribute_id.custom_type: " + str(value.custom_type))
                    # print("value.custom_type: " + str(value.custom_type))
                    print("\n\n")

                    if value.attribute_id.custom_type == 'computed_field':
                        self.get_forumla(value,record)
                print("--------------------")

    def get_forumla(self, value, record):
        pass
        # rec_val_name = self.env['product.attribute'].search([('id', '=', value.attribute_id.id)]).computed_input1.name
        # rec_val = self.env['product.attribute.value'].search([('product_id', '=', record.product_id)]).computed_input1.name

        
        # print("rec_val_name: " + str(rec_val_name))
        # print("rec_val: " + str(rec_val))



        # attribute_1_name = value.attribute_id.computed_input1.name
        # for value_name in value.attribute_id.computed_input1.value_ids:
        #     print("value_name: " + str(value_name.name)) 
        
        # attribute_2_name = value.attribute_id.computed_input2.name
        

        # for value_name in value.attribute_id.computed_input2.value_ids:
            # print("value_name: " + str(value_name.name)) 

        # attribute_3 = record.config_session_id.custom_value_ids.computed_input3
        # operator_1 = record.config_session_id.custom_value_ids.operator1
        # operator_2 = record.config_session_id.custom_value_ids.operator1

        # print("attribute_1: " + str(attribute_1_name) )# + " = " + str(attribute_1))
        # print("attribute_2: " + str(attribute_2_name))
        # print("attribute_3: " + str(attribute_3))
        # print("operator_1: " + str(operator_1))
        # print("operator_2: " + str(operator_2))
            
            

    


    
    


