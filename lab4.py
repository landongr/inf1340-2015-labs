#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

PROVINCIAL_TAX = .05
FEDERAL_TAX = .025
TOTAL_TAX = PROVINCIAL_TAX + FEDERAL_TAX

def provincial_tax(purchase):
    return purchase * PROVINCIAL_TAX

def federal_tax(purchase):
    return purchase * FEDERAL_TAX

def bill_of_sale(purchase):
    prov_tax = provincial_tax(purchase)
    fed_tax = federal_tax(purchase)
    with open ("bill_file.txt", "w") as output_file:
        output_file.write("Provincial tax :" + str(prov_tax))
        output_file.write("\nFederal tax : " + str(fed_tax))
        output_file.write("\nAmount of purchase: {0:.2f}".format(purchase))
        output_file.write("\nTotal tax: {0:.2f}".format(purchase * TOTAL_TAX))
        output_file.write("\nTotal sale: {0:.2f}".format(purchase * 1 + TOTAL_TAX))

bill_of_sale(10)