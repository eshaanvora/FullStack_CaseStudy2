#Eshaan Vora
#Case Study: Customer Order Analysis

#Export results to HTML format using Rich Console library
from rich.console import Console
console = Console(record=True)

#Import required packages
import os
import matplotlib.pyplot as plt
import pandas as pd

#Load data
filePath = "casestudy2.csv"
#Read CSV into Pandas Dataframe
customerOrders = pd.read_csv(filePath)

#Format float results following accounting numeric format (USD)
pd.options.display.float_format = '${:,.2f}'.format
#Format result depending on if it is a monetary value
def format(value):
    if "." in str(value):
        return('${:,.2f}'.format(value))
    else:
        return('{:,}'.format(value))

#Customer transactions were recorded annually from 2015-2017
currentYear = 2017
previousYear = 2016
baseYear = 2015

#TOTAL REVENUE FOR CURRENT YEAR
totalCurrentRevenue = customerOrders.groupby("year")['net_revenue'].sum()
console.print("Total Revenue Per Year: ")
console.print(totalCurrentRevenue)

#customer list per year
allCustomers2015 = customerOrders.query("year == @baseYear")['customer_email'].tolist()
allCustomers2016 = customerOrders.query("year == @previousYear")['customer_email'].tolist()
allCustomers2017 = customerOrders.query("year == @currentYear")['customer_email'].tolist()

#NEW CUSTOMERS
newCustomers2017 = list(set(allCustomers2017) - set(allCustomers2016))
newCustomers2016 = list(set(allCustomers2016) - set(allCustomers2015))

#NEW CUSTOMER REVENUE
newCustomerRevenue2017 = customerOrders.query("(customer_email in @newCustomers2017) and (year == @currentYear)")['net_revenue'].sum()
newCustomerRevenue2016 = customerOrders.query("(customer_email in @newCustomers2016) and (year == @previousYear)")['net_revenue'].sum()
console.print("\n" + "New Customer Revenue in 2017: ")
console.print(format(newCustomerRevenue2017))
console.print("New Customer Revenue in 2016: ")
console.print(format(newCustomerRevenue2016))

#EXISTING CUSTOMER REVENUE CURRENT YEAR & PAST YEAR
existingCustomerRevenue2017 = customerOrders.query("(customer_email in @allCustomers2016) and (year == @currentYear)")['net_revenue'].sum()
console.print("\n" + "Existing Customer Revenue in 2017: ")
console.print(format(existingCustomerRevenue2017))
existingCustomerRevenue2016 = customerOrders.query("(customer_email in @allCustomers2015) and (year == @previousYear)")['net_revenue'].sum()
console.print("Existing Customer Revenue in 2016: ")
console.print(format(existingCustomerRevenue2016))

#EXISTING CUSTOMER GROWTH PER YEAR
customerRevenue2015 = customerOrders.query("year == @baseYear")['net_revenue'].sum()
totalCustomerRevenue2016 = customerOrders.query("year == @previousYear")['net_revenue'].sum()

existingCustomerGrowth2016 = (existingCustomerRevenue2016 - customerRevenue2015)
existingCustomerGrowth2017 = (existingCustomerRevenue2017 - totalCustomerRevenue2016)
console.print("\n" + "Existing Customer Revenue Growth in 2016: ")
console.print(format(existingCustomerGrowth2016))
console.print("Existing Customer Revenue Growth in 2017: ")
console.print(format(existingCustomerGrowth2017))

#LOST CUSTOMERS
lostCustomers2017 = list(set(allCustomers2016) - set(allCustomers2017))
lostCustomers2016 = list(set(allCustomers2015) - set(allCustomers2016))

#REVENUE LOST FROM ATTRITION PER YEAR
console.print("\n" + "Revenue Lost from Attrition")
lostCustomerRevenue2016 = customerOrders.query("(customer_email in @lostCustomers2016) and (year == @baseYear)")['net_revenue'].sum()
console.print("Customers who did not order in 2016, had spent, in 2015, : ")
console.print(format(lostCustomerRevenue2016))
lostCustomerRevenue2017 = customerOrders.query("(customer_email in @lostCustomers2017) and (year == @previousYear)")['net_revenue'].sum()
console.print("Customers who did not order in 2017, had spent, in 2016, : ")
console.print(format(lostCustomerRevenue2017))

#NUMBER OF CUSTOMERS PER YEAR
customerCount2017 = customerOrders.query("year == @currentYear")['customer_email'].count()
console.print("\n" + "Number of Customers in 2017: ")
console.print(format(customerCount2017))
customerCount2016 = customerOrders.query("year == @previousYear")['customer_email'].count()
console.print("Number of Customers in 2016: ")
console.print(format(customerCount2016))
customerCount2015 = customerOrders.query("year == @baseYear")['customer_email'].count()
console.print("Number of Customers in 2015: ")
console.print(format(customerCount2015))

#Write results to HTML
console.save_html("CaseStudy2.html")
