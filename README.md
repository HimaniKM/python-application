📚 PubMed Research Paper Fetcher
This is a Python application that fetches research papers from PubMed based on a search query.
It filters out non-academic papers (e.g., corporate or pharmaceutical affiliations) and saves the results to a CSV file.

🔹 Features
✅ Fetches research papers from PubMed using an API
✅ Extracts paper details, including authors, title, affiliation, journal name, etc.
✅ Filters out non-academic papers (e.g., companies, pharma, biotech)
✅ Saves the filtered results as a CSV file

🔹 Installation Guide
1️⃣ Prerequisites
Before running the application, install:

Python 3.12+
Poetry (Python Dependency Manager)
If you don’t have Poetry installed, install it using:

pip install poetry
2️⃣ Clone the Repository

git clone https://github.com/HimaniKM/pubmed-fetcher.git
cd pubmed-fetcher
3️⃣ Install Dependencies

poetry install
🔹 Usage
Run the application with a search query:


poetry run get-papers-list "cancer research"
This fetches PubMed papers related to "cancer research" and filters out non-academic ones.

✅ Save Results to a CSV File
To save the filtered results in a CSV file:


poetry run get-papers-list "Alzheimer's treatment" -f results.csv
This will save the results to results.csv.

🔹 Project Structure

pubmed-fetcher/
│── pythonproject/               # 📂 Main package
│   │── __init__.py              # 🏷️ Marks it as a package
│   │── cli.py                   # 🎯 Command-line interface
│   │── pubmed_fetcher.py         # 🔍 Fetches papers from PubMed
│   │── paper_filter.py           # 🚦 Filters out non-academic papers
│── pyproject.toml                # 📦 Poetry project configuration
│── README.md                     # 📖 Project documentation
🔹 File Descriptions
cli.py
Handles command-line interactions.
Calls PubMedFetcher to get papers.
Uses PaperFilter to remove non-academic papers.
Saves final results to a CSV file.
pubmed_fetcher.py
Fetches paper details from the PubMed API.
Extracts title, authors, affiliations, and journal details.
paper_filter.py
Contains filtering logic to remove non-academic papers.
Checks affiliations for terms like Inc, Ltd, Pharma, Biotech.
🔹 Debugging
If papers show "Unknown" affiliations, check the API response structure:


poetry run get-papers-list "cancer research" --debug
This will print the full API response and help fix missing data.

🔹 Contributing
Contributions are welcome! To contribute:

Fork this repository
Create a new branch:

git checkout -b feature-new-functionality
Make changes and commit:

git commit -m "Added new feature"
Push to GitHub and create a PR
🔹 License
📜 This project is licensed under the MIT License.

🔹 Contact
💡 For questions or issues, open an issue or reach out to:
✉️ Email: himanikothakotamaana@gmail.com
🌍 GitHub: https://github.com/HimaniKM
