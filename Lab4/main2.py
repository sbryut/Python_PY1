import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_f:
        reader = csv.DictReader(input_f, delimiter=",")

        data = []
        for row in reader:
            data.append(row)

    with open(OUTPUT_FILENAME, "w") as output_f:
        output_f.write(json.dumps(data, indent=4))


if __name__ == "__main__":
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
