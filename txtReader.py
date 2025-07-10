import re
from pprint import pprint
from collections import OrderedDict

def parse_observation_log(filepath):
    data = OrderedDict()
    image_log = []
    notes = ""

    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("LOCAL DATE:"):
            data["local_date"] = line.split(":", 1)[1].strip()

        elif line.startswith("LOCAL START TIME:"):
            data["start_time"] = line.split(":", 1)[1].strip()

        elif line.startswith("LOCAL END TIME:"):
            data["end_time"] = line.split(":", 1)[1].strip()

        elif line.startswith("NAME(S):"):
            data["name"] = line.split(":", 1)[1].strip()

        elif line.startswith("GOAL(S):"):
            goals = line.split(":", 1)[1].strip()
            data["goals"] = [goal.strip() for goal in goals.split(",")]

        elif line.startswith("TRANSPARENCY:"):
            data["transparency"] = line.split(":", 1)[1].strip()

        elif line.startswith("SEEING:"):
            data["seeing"] = line.split(":", 1)[1].strip()

        elif line.startswith("TEMPERATURE:"):
            temp_range = re.findall(r'\d+', line)
            data["temperature_range_F"] = tuple(map(int, temp_range))

        elif line.startswith("HUMIDITY:"):
            humidity_range = re.findall(r'\d+', line)
            data["humidity_range_percent"] = tuple(map(int, humidity_range))

        elif line.startswith("TELESCOPE:"):
            data["telescope"] = line.split(":", 1)[1].strip()

        elif line.startswith("CAMERA:"):
            data["camera"] = line.split(":", 1)[1].strip()

        elif line.startswith("Camera temp setpoint:"):
            temp = re.findall(r'-?\d+', line)
            if temp:
                data["camera_temp_setpoint_C"] = int(temp[0])

        elif line.startswith("IMAGE LOG"):
            i += 1
            while i < len(lines) and (lines[i].startswith("#") or "frames" in lines[i].lower()):
                i += 1

            while i < len(lines) and not lines[i].startswith("NOTES:"):
                parts = re.split(r'\s{2,}|\t+', lines[i])
                if len(parts) >= 4:
                    try:
                        entry = {
                            "frames": int(parts[0]),
                            "target": parts[1],
                            "exposure": parts[2],
                            "filter": parts[3]
                        }
                        if len(parts) == 5 and "seq start" in parts[4]:
                            entry["sequence_start"] = parts[4].replace("seq start", "").strip()
                        image_log.append(entry)
                    except ValueError:
                        print(f"Skipping line (could not parse int): {lines[i]}")
                i += 1
            continue

        elif line.startswith("NOTES:"):
            notes = line.split(":", 1)[1].strip()

        i += 1

    data["image_log"] = image_log
    data["notes"] = notes

    return data

if __name__ == "__main__":

    #FILE NAME
    filepath = "14in_20250624_log.txt"  
    structured_data = parse_observation_log(filepath)
    pprint(structured_data)
