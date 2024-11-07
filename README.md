# Bike Rental Dashboard

This is an interactive **Bike Rental Analysis Dashboard** built with **Streamlit** to visualize bike rental data over different years. The dashboard allows users to explore trends in bike rentals, make comparisons between 2011 and 2012, and view data related to weather, user types, and seasonal patterns.

## Features

- **Year Selection**: Choose from different years (2011, 2012) or view a comparison between 2011 and 2012.
- **Interactive Visualizations**:
  - **Bike Rental Trends**: Explore bike rental trends for each year.
  - **Working Day vs Holiday Rentals**: Compare bike rentals on working days and holidays.
  - **Seasonal Bike Rental Trends**: Understand rental patterns for each season.
  - **Casual vs Registered Users**: Visualize bike rentals by user type (casual vs registered).
  - **Hourly Bike Rental Trends**: View bike rentals across different hours of the day.
  - **Weather-Based Rental Trends**: Examine bike rental data based on weather conditions.
- **Data Display**: Option to view the underlying data in a table format with detailed metadata.

## Installation

Follow these steps to run the dashboard on your local machine.

## Setup Environment
Pastikan Anda memiliki:
- **Python** versi 3.7 atau lebih baru
  ```bash
  conda create --name main-ds python=3.9
  conda activate main-ds

### Project installation

1. **Clone the repository** or download it as a ZIP file.
   ```bash
   git clone https://github.com/zzazzz/Belajar-Analisis-Data-dengan-Python.git
   cd Belajar-Analisis-Data-dengan-Python.git

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install requirements dependencies**:
   ```bash
   pip install -r requirements.txt

### Running the Dashboard

Once the dependencies are installed, you can start the dashboard with Streamlit:

1. **Run the streamlit app**:
   ```bash
   streamlit run app.py
2. The dashboard will be available at http://localhost:8501 in your browser.
