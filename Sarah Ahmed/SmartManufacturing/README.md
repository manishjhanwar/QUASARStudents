# Smart Manufacturing Batch Manager

Student: Sarah Ahmed

## Run the application

Keep manufacturing.py and manufacturing_utils.py in this folder, then run:

    py manufacturing.py

## Features

- Stores production batches as tuples and lets users add batches.
- Validates numeric input, rejects negative quantities and costs, and prevents defective counts above production.
- Calculates total manufacturing cost and overall defect percentage using manufacturing_utils.py.
- Uses filter() for batches with more than 10 defects, map() for accepted quantities, and a lambda for each batch cost.
- Demonstrates try, except, else, and finally.
