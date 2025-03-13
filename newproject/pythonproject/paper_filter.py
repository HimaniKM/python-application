class PaperFilter:
    NON_ACADEMIC_TERMS = [" Inc", " Ltd", " Corporation", " Biotech", " Pharma", " Research Institute"]

    @staticmethod
    def is_non_academic(affiliation: str) -> bool:
        """Checks if an affiliation is from a pharmaceutical/biotech company."""
        if not affiliation:
            return False  # ✅ If no affiliation is provided, assume it's academic
        
        # ✅ Improved matching to prevent false positives
        affiliation_lower = f" {affiliation.lower()} "  # Add spaces to prevent false matches
        return any(term.lower() in affiliation_lower for term in PaperFilter.NON_ACADEMIC_TERMS)
