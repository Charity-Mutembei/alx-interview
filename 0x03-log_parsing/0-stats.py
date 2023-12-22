#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics
"""

import sys
import signal


def print_metrics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def process_line(line, total_size, status_counts):
    try:
        parts = line.split()
        ip_address, _, _, status_code, file_size = parts[0], parts[
            5], parts[8], int(parts[10]), int(parts[11])
        total_size += file_size
        status_counts[status_code] = status_counts.get(status_code, 0) + 1
    except (ValueError, IndexError):
        # Skip lines that do not match the expected format
        pass
    return total_size, status_counts


def main():
    total_size = 0
    status_counts = {}

    try:
        line_number = 0
        for line in sys.stdin:
            line_number += 1
            total_size, status_counts = process_line(line,
                                                     total_size, status_counts)

            if line_number % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle CTRL+C gracefully
        print_metrics(total_size, status_counts)
        sys.exit(0)


if __name__ == "__main__":
    main()
