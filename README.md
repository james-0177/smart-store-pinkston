# smart-store-pinkston
## Smart-Sales Project

### Smart-Sales-Starter-Files
#### Step 1 - Create and Activate Project Virtual Environment
```shell
py -m venv .venv
.venv\Scripts\Activate
```

#### Step 2 - Install and Update packages from requirements.txt
```shell
py -m pip install --upgrade -r requirements.txt
```

#### Step 3 - Run the Initial project script
```shell
py scripts\data_prep.py
```

#### Step 4 - Prepare and clean data
```shell
py scripts\data_preparation\prepare_customers_data.py
py scripts\data_preparation\prepare_products_data.py
py scripts\data_preparation\prepare_sales_data.py
```

#### Ste 5 - Create data warehouse and database tables
```shell
py scripts\etl_to_dw.py
```