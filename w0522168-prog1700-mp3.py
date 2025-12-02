def read_file(filename):
    records = []
    with open(filename, "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            records.append((name, float(score)))
    return records


def process_data(records):
    total = 0
    count = 0
    passing = 0
    highest = ("", -1)
    lowest = ("", 999)

    for name, score in records:
        total += score
        count += 1
        if score >= 70:
            passing += 1

        if score > highest[1]:
            highest = (name, score)
        if score < lowest[1]:
            lowest = (name, score)

    i = 0
    above_90 = 0
    while i < len(records):
        if records[i][1] >= 90:
            above_90 += 1
        i += 1

    average = total / count if count > 0 else 0

    summary = {
        "average": average,
        "count": count,
        "passing": passing,
        "highest_name": highest[0],
        "highest_score": highest[1],
        "lowest_name": lowest[0],
        "lowest_score": lowest[1],
        "above_90": above_90
    }

    return summary


def write_report(filename, summary):
    """Write summary results to a text file."""
    with open(filename, "w") as f:
        f.write("Grade Report Summary\n")
        f.write("--------------------\n")
        f.write(f"Total Students: {summary['count']}\n")
        f.write(f"Average Score: {summary['average']:.2f}\n")
        f.write(f"Passing Students: {summary['passing']}\n")
        f.write(f"Highest Score: {summary['highest_name']} ({summary['highest_score']})\n")
        f.write(f"Lowest Score: {summary['lowest_name']} ({summary['lowest_score']})\n")
        f.write(f"Students Scoring 90+: {summary['above_90']}\n")


if __name__ == "__main__":
    print("Reading file...")
    records = read_file("grades.csv")

    print("Processing data...")
    summary = process_data(records)

    print("Writing summary...")
    write_report("summary.txt", summary)

    print("\n=== Summary Results ===")
    for key, value in summary.items():
        print(f"{key}: {value}")

# Reflection:
# 1) I used lists for ordered sequences of records and dictionaries for structured summary data.
#
# 2) Initially mis-typed split(",") which caused a ValueError due to whitespace.
#
# 3) It allows results to be stored, shared, and used later without re-running the program.
#
# 4) I would add letter-grade assignment and sorting by score.
