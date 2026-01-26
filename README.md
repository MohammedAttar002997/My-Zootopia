My-Zootopia
A dynamic web generator that fetches animal data via an external API and transforms it into a stylized, responsive gallery. This project demonstrates Python-based data handling, environment security, and automated HTML template rendering.

🚀 Features

Dynamic Data Fetching: Utilizes a dedicated data fetcher to retrieve information from an API.


Template Rendering: Uses a clean HTML template (animals_template.html) to ensure a consistent look across all generated pages.


Secure Configuration: Employs .env files to manage sensitive credentials like API keys safely.


Responsive Design: The output animals.html provides a mobile-friendly viewing experience for the animal database.


Local Caching: Stores fetched data in animals_data.json to optimize performance and reduce redundant API calls.

📂 Project Structure
My-Zootopia/
├── .env                        # API keys and environment variables 
├── animals_data.json           # Cached JSON data for animals [cite: 84]
├── animals_template.html       # Base HTML for the generator 
├── animals_web_generator.py    # Main script to build the website 
├── data_fetcher.py             # Logic for API communication 
├── requirements.txt            # Project dependencies 
└── .gitignore                  # Standard Git ignore rules [cite: 74]

🛠️ Installation

1-Clone the repository:
git clone https://github.com/yourusername/My-Zootopia.git
cd My-Zootopia

2-Install dependencies: This project requires requests for API calls and python-dotenv for environment management.

pip install -r requirements.txt

3-Configure Environment Variables: Create a .env file in the root directory and add your API key:

API_KEY=your_actual_api_key_here

🖥️ Usage
Run the main generator script to fetch the latest data and rebuild your gallery:

python animals_web_generator.py

After running the script, open animals.html in any web browser to view the results.

⚙️ Technical Details

Language: Python 3.13 


Data Handling: The data_fetcher.py script isolates the logic for communicating with the external API, ensuring a modular design.


Automation: animals_web_generator.py acts as the orchestrator, reading the JSON cache and injecting content into the HTML placeholders.