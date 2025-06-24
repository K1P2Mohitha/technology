import json
from datetime import datetime

# IMPLEMENT: convert ISO 8601 timestamp to milliseconds (epoch)
def convert_iso_to_milliseconds(iso_str: str) -> int:
    dt = datetime.strptime(iso_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)

# IMPLEMENT: merge data from data-1.json and data-2.json into unified format
def merge_data(data1: list, data2: list) -> list:
    # Convert ISO timestamps in data1 to milliseconds
    converted_data1 = {
        convert_iso_to_milliseconds(item["timestamp"]): item["value"] for item in data1
    }

    # Prepare data2 as a dictionary (timestamps are already in ms)
    data2_dict = {
        item["timestamp"]: item["value"] for item in data2
    }

    # Combine timestamps from both data sources
    all_timestamps = set(converted_data1.keys()).union(data2_dict.keys())

    # Build the merged result
    merged_result = []
    for ts in sorted(all_timestamps):
        merged_result.append({
            "timestamp": ts,
            "source1": converted_data1.get(ts),
            "source2": data2_dict.get(ts)
        })

    return merged_result

# Run when file is executed
if __name__ == "__main__":
    # Load JSON files
    with open("data-1.json") as f1, open("data-2.json") as f2, open("data-result.json") as fr:
        data1 = json.load(f1)
        data2 = json.load(f2)
        expected = json.load(fr)

    # Run your function
    result = merge_data(data1, data2)

    # Test your result
    assert result == expected, "❌ Test failed! The merged data doesn't match expected output."
    print("✅ All tests passed! You’re ready to submit.")
