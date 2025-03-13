import json
import csv  # ✅ Import CSV module to save data
from pythonproject.pubmed_fetcher import PubMedFetcher
from pythonproject.paper_filter import PaperFilter

def save_to_csv(papers, output_file):
    """Saves the filtered papers to a CSV file."""
    if not papers:
        print("\n❌ No papers to save.")
        return

    # Define CSV column headers based on available data
    fieldnames = ["title", "authors", "affiliation", "journal", "publication_date", "doi"]

    # ✅ Open file in write mode and save the data
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for p in papers:
            writer.writerow({
                "title": p.get("title", "N/A"),
                "authors": ", ".join([a.get("name", "Unknown") for a in p.get("authors", [])]),
                "affiliation": p.get("affiliation", "Unknown"),
                "journal": p.get("source", "N/A"),
                "publication_date": p.get("pubdate", "N/A"),
                "doi": next((aid["value"] for aid in p.get("articleids", []) if aid["idtype"] == "doi"), "N/A")
            })

    print(f"\n✅ Data successfully saved to '{output_file}'")


def main():
    # Take user input for query and output file
    query = input("Enter your PubMed search query: ").strip()
    output_file = input("Enter output CSV filename (default: output.csv): ").strip() or "output.csv" 
    if ".csv" not in output_file:
        output_file+=".csv"
    

    print(f"\nFetching papers for query: {query}...")

    # Fetch research papers using PubMedFetcher
    fetcher = PubMedFetcher(query)
    paper_ids = fetcher.fetch_paper_ids()
    papers = fetcher.fetch_paper_details(paper_ids)

    if not papers:
        print("\n❌ No papers found for the given query.")
        return

    # ✅ Extract and fix affiliations properly
    academic_papers = []
    for p in papers:
        # Extract affiliation from multiple possible fields
        affiliation = (
            p.get("affiliation") or 
            (p.get("authors", [{}])[0].get("affiliation") if "authors" in p and p["authors"] else None) or 
            (p.get("institution") if "institution" in p else None) or 
            (p.get("source") if "university" in p.get("source", "").lower() else None) or 
            "Unknown"
        ).strip()

        print(f"DEBUG: Checking Affiliation: {affiliation}")  # ✅ Debug affiliation extraction

        # ✅ Include paper even if affiliation is missing
        if not PaperFilter.is_non_academic(affiliation):  
            p["affiliation"] = affiliation  # Ensure affiliation is stored
            academic_papers.append(p)

    print(f"\n✅ Found {len(academic_papers)} academic papers.")

    # ✅ Save filtered data to CSV
    save_to_csv(academic_papers, output_file)


if __name__ == "__main__":
    main()
