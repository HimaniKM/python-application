import requests  # ✅ Ensure this is at the top

class PubMedFetcher:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    DB = "pubmed"

    def __init__(self, query):
        self.query = query

    def fetch_paper_ids(self):
        """Fetches PubMed paper IDs for a given query."""
        params = {
            "db": self.DB,
            "term": self.query,
            "retmode": "json",
            "retmax": 10  # ✅ Limit results for debugging
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        result = response.json()
        return result.get("esearchresult", {}).get("idlist", [])

    def fetch_paper_details(self, paper_ids):
        """Fetches paper details using paper IDs."""
        if not paper_ids:
            return []

        params = {
            "db": self.DB,
            "id": ",".join(paper_ids),
            "retmode": "json"
        }
        response = requests.get(self.FETCH_URL, params=params)  # ✅ Ensure `requests.get` is used
        response.raise_for_status()

        result = response.json().get("result", {})

        # ✅ Extract paper details and ensure `affiliation` exists
        paper_list = []
        for paper_id in paper_ids:
            if paper_id in result:
                paper = result[paper_id]
                if isinstance(paper, dict):
                    authors = paper.get("authors", [])
                    first_author_affiliation = None

                    # ✅ Extract first author's affiliation if available
                    if authors and isinstance(authors, list):
                        for author in authors:
                            if isinstance(author, dict) and "affiliation" in author:
                                first_author_affiliation = author["affiliation"]
                                break  # Stop after first found affiliation

                    paper["affiliation"] = (
                        paper.get("affiliation") or 
                        first_author_affiliation or  # ✅ Extract from first author's affiliation
                        paper.get("institution") or  # ✅ Check for institution field
                        (paper.get("source") if "university" in paper.get("source", "").lower() else None) or 
                        "Unknown"
                    ).strip()

                    paper_list.append(paper)

        return paper_list
