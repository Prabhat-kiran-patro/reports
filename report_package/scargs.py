import argparse

def read_args():
    parser = argparse.ArgumentParser(description="Create reports using command-line.")

    parser.add_argument("report_name", type=str, help="name of the report to be created")
    parser.add_argument("cols", type=str, nargs="+", choices=["id", "name", "math", "phy", "cs", "total", "avg"], help="list of columns required in the report")

    args = parser.parse_args()

    return args.report_name, args.cols
