#! /usr/bin/env python3
from sys import argv
from convert import convert_dhl, convert_hermes


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage:")
        print("./cli.py <method> <id>")
        print("Method can be 'hermes' or 'dhl'")
        exit(1)
    
    method = argv[1]
    id = argv[2]

    match method:
        case "dhl":
            convert_dhl(id)
        case "hermes":
            convert_hermes(id)
        case _:
            print("Unknown method")

