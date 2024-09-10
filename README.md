# FoodTrack

FoodTrack is a Streamlit-based web application that allows users to record and track their food intake. It integrates with the Open Food Facts database to fetch product information and stores data locally using SQLite.

## Features

- Fetch product data using EAN codes from Open Food Facts
- Manual input of product information
- Record food intake with quantity, meal type, and date/time
- View detailed nutritional information for products
- Local database storage for products and intake records

## Project Structure

```
src/
├── app/
│   ├── app.py
│   └── utils.py
├── database/
│   ├── database.py
│   └── utils.py
├── intake/
│   ├── base.py
│   └── utils.py
└── products/
    ├── base.py
    └── scraper.py
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/szafrix/foodtrack.git
   cd foodtrack
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create the database:
   ```
   python -c "from src.database.database import create_tables; create_tables()"
   ```

2. Run the Streamlit app:
   ```
   streamlit run src/app/app.py
   ```

3. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

4. Use the app to search for products, record intake, and view nutritional information.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Open Food Facts](https://world.openfoodfacts.org/) for providing the product database
- [Streamlit](https://streamlit.io/) for the web app framework
