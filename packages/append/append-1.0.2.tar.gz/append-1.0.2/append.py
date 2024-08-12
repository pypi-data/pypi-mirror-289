import argparse
import sys
import os
import signal

def process_lines(lines, start='', end=''):
    return [f"{start}{line.strip()}{end}" for line in lines]

def main():
    parser = argparse.ArgumentParser(description="Add a string to the start or end of every line in a text file.")
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="The name of the file to process. If omitted, reads from standard input.")
    parser.add_argument('-s', '--start', help="String to add at the start of each line", default='')
    parser.add_argument('-e', '--end', help="String to add at the end of each line", default='')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), help="Output file. If omitted, prints to standard output.")
    
    args = parser.parse_args()

    # Read lines from file or stdin
    lines = args.filename.readlines()

    # Process lines
    processed_lines = process_lines(lines, args.start, args.end)

    # Handle BrokenPipeError
    try:
        if args.output:
            args.output.write('\n'.join(processed_lines) + '\n')
            args.output.close()
        else:
            print('\n'.join(processed_lines))
    except BrokenPipeError:
        # Ignore the error and exit gracefully
        sys.stdout.close()
        sys.exit(0)

if __name__ == "__main__":
    # Handle SIGPIPE (broken pipe) signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    main()
