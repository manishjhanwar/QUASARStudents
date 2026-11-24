# Smart Manufacturing Management Application

## Student Information
- **Name:** Poojashree
- **Registration Number:** PROV/ASQR/BTECH/017

## Project Description
A Python application developed for an electronics manufacturer to manage production batches, manufacturing costs, and quality control.

### Features Implemented:
1. **Data Structure:**
   - Production records maintained using a list of tuples: `(Batch_ID, Product_Name, Units_Produced, Defective_Units, Cost_Per_Unit)`.
   - Function to dynamically add a new batch.
2. **Modular Functions (`manufacturing_utils.py`):**
   - `calculate_total_manufacturing_cost`: Computes sum of manufacturing costs across all batches.
   - `calculate_overall_defect_percentage`: Calculates overall defect rate across batches.
3. **Functional Programming (`manufacturing.py`):**
   - `filter()`: Identifies batches having more than 10 defective units.
   - `map()`: Generates list of accepted quantities (units produced - defective units).
   - `lambda`: Computes total manufacturing cost per batch.
4. **Exception Handling:**
   - Handles `ValueError` for non-numeric input.
   - Prevents negative values for production quantities, defective quantities, and unit costs.
   - Ensures defective units do not exceed total units produced.
   - Utilizes `try`, `except`, `else`, and `finally` blocks.
