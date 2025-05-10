# Eco-Buddy: Carbon Footprint Tracker

Eco-Buddy is a user-friendly desktop application designed to help individuals track and reduce their carbon footprint. By logging daily activities, users can calculate their total carbon emissions, visualize the footprint distribution using a pie chart, and receive actionable tips to reduce their environmental impact.

## Features
- **Activity Logging**: Add activities (e.g., car usage, electricity consumption, etc.) with their values.
- **Carbon Footprint Calculation**: Automatically calculates carbon emissions based on activity data.
- **Visualization**: Displays a pie chart showing the distribution of emissions by activity type.
- **Daily Tips**: Provides actionable tips to reduce carbon footprint.
- **Date Selection**: Use the calendar to select dates and view historical data.

## Setup and Usage Guide

### Prerequisites
1. Python 3.8 or later installed.
2. Required Python packages: `tkinter`, `tkcalendar`, `matplotlib`.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/codingwithnsh/Eco-Buddy.git
   cd eco-buddy
   ```
2. Install the dependencies:
   ```bash
   pip install tkcalendar matplotlib
   ```

### Running the Application
1. Run the application using:
   ```bash
   python main.py
   ```
2. The application window will open.

### Step-by-Step Guide
1. **Search for Activities**:
   - Use the search bar on the left panel to filter activities (e.g., "Car Usage").
2. **Select an Activity**:
   - Click on an activity from the list to select it.
3. **Add Values**:
   - Enter a numeric value (e.g., kilometers for car usage) in the text box and click "Add Value".
   - The activity and value will appear in the table on the right.
4. **Calculate Footprint**:
   - The application automatically calculates your total carbon footprint and displays the result in the bottom-right panel.
5. **View Pie Chart**:
   - The pie chart will dynamically update to show the distribution of emissions by activity type.
6. **Receive Tips**:
   - A random tip will appear below the pie chart to help you reduce your footprint.
7. **Select a Date**:
   - Use the calendar to select a date and view data related to it.

### File Structure
- `main.py`: Main application file.
- `carbon_footprint_data.csv`: File used to store activity data and carbon footprint calculations.

### Example Use Case
1. Search for "Car Usage" in the search bar.
2. Select "Car Usage (km)" from the list.
3. Enter the distance (e.g., 20 km) in the input box and click "Add Value".
4. Repeat for other activities like "Electricity Usage (kWh)" or "Shower (10 minutes)".
5. View your total carbon footprint and its distribution in the pie chart.

### Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the MIT License.
