class NNNLeaseAnalyzer:
    def __init__(self, location, lease_details):
        self.location = location
        self.lease_details = lease_details

    def analyze_lease(self):
        analysis_results = {}

        # Example analysis: Rent-to-Sales Ratio
        if "annual_sales" in self.lease_details and "annual_rent" in self.lease_details:
            rent_to_sales_ratio = self.lease_details["annual_rent"] / self.lease_details["annual_sales"]
            analysis_results["rent_to_sales_ratio"] = rent_to_sales_ratio

        # Example analysis: Lease Term
        if "start_date" in self.lease_details and "end_date" in self.lease_details:
            lease_term = (self.lease_details["end_date"] - self.lease_details["start_date"]).days / 365
            analysis_results["lease_term_years"] = lease_term

        # Add more custom analyses here...

        return analysis_results


# Example usage
if __name__ == "__main__":
    location = "123 Main St, Cityville"
    lease_details = {
        "annual_rent": 50000,  # Example annual rent in dollars
        "annual_sales": 1000000,  # Example annual sales in dollars
        "start_date": date(2023, 1, 1),  # Example lease start date
        "end_date": date(2033, 1, 1),  # Example lease end date
    }

    analyzer = NNNLeaseAnalyzer(location, lease_details)
    analysis_results = analyzer.analyze_lease()

    print("Lease Analysis for Location:", location)
    for analysis, value in analysis_results.items():
        print(f"{analysis.replace('_', ' ').title()}: {value}")
