from report_package import scargs, file_utilities, format_data
def main():
    # Load requirements
    report_name, cols = scargs.read_args()
    cols = [_.lower() for _ in cols]
    # Load data
    req_data = format_data.format(cols)
    # Generate reports
    file_utilities.write_to_csv(f"created_reports/{report_name}.csv", req_data)

    print("Reports generated successfully!")

if __name__ == "__main__":
    main()
