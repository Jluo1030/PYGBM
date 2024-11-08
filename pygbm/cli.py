import argparse
from gbm_simulator import GBMSimulator

def main():
    parser = argparse.ArgumentParser(description="GBMSimulator CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    parser_info = subparsers.add_parser("simulate_path", help="Simulate Geometric Brownian motions")
    parser_info.add_argument("--T", type=float, required=True, help="Time length")
    parser_info.add_argument("--N", type=int, required=True, help="step size")

    args = parser.parse_args()

    if args.command == "simulate_path":
        display_info(args.T, args.N)

if __name__ == "__main__":
    main()

