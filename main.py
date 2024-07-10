import os
import numpy as np
import carbon as calc
import suggestions as s
import report as report
import data_visualization as dv
#from utils import open_pdf
#import subprocess

# def open_pdf(file_path):    subprocess.run(["open", file_path])

def gather_input(num_entries):
    entries = []
    for i in range(num_entries):
        print(f"\nEntry {i+1}:")
        monthly_electricity_bill = float(input("Enter monthly electricity bill amount: "))
        monthly_natural_gas_bill = float(input("Enter monthly natural gas bill amount: "))
        monthly_fuel_bill = float(input("Enter monthly fuel bill amount: "))
        total_waste_generated_per_month = float(input("Enter total waste generated per month (kg): "))
        recycling_percentage = float(input("Enter recycling percentage (%): "))
        total_kilometers_traveled_per_year = float(input("Enter total kilometers traveled per year: "))
        average_fuel_efficiency = float(input("Enter average fuel efficiency (km/L): "))

        energy_usage = calc.sum_energy_usage(monthly_electricity_bill, monthly_natural_gas_bill, monthly_fuel_bill)
        waste_generation = calc.sum_waste(total_waste_generated_per_month, recycling_percentage)
        business_travel = calc.sum_business_travel(total_kilometers_traveled_per_year, average_fuel_efficiency)
        
        entries.append((energy_usage, waste_generation, business_travel))
        
        print("\nTotal Carbon Footprint for Entry", i+1, ":", energy_usage + waste_generation + business_travel, "metric tons CO2 equivalent")
        print("Energy Usage Suggestion:", s.energy_suggestion(energy_usage))
        print("Waste Generation Suggestion:", s.waste_suggestion(waste_generation))
        print("Business Travel Suggestion:", s.travel_suggestion(business_travel))

    return entries

def main():
    num_entries = int(input("Enter the number of entries: "))
    entries = gather_input(num_entries)

    for i, entry_data in enumerate(entries):
        dv.plot_pie_charts(entry_data, i)
    
    total_values = [
        [entry[0] for entry in entries],
        [entry[1] for entry in entries],
        [entry[2] for entry in entries]
    ]

    dv.plot_total_carbon_footprint(total_values)
    dv.plot_total_carbon_footprint_by_entry(entries)
    
    filename = "carbon_footprint_report.pdf"
    report.create_pdf(entries, filename)
    #open_pdf(f"reports/{filename}")

if __name__ == "__main__":
    main()
