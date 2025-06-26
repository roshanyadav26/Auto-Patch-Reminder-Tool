import pandas as pd

# Load installed software and latest versions
installed = pd.read_csv("installed_software.csv")
latest = pd.read_csv("latest_versions.csv")

# Merge both datasets on software name
merged = pd.merge(installed, latest, on="Software")

# Compare versions and find outdated ones
def version_compare(installed, latest):
    return tuple(map(int, installed.split("."))) < tuple(map(int, latest.split(".")))

outdated = []
for _, row in merged.iterrows():
    if version_compare(row["Installed_Version"], row["Latest_Version"]):
        outdated.append(row)

# Output reminder report
if outdated:
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("⚠️ PATCH REMINDER REPORT\n\n")
        for item in outdated:
            f.write(f"{item['Software']} is outdated.\n")
            f.write(f"Installed: {item['Installed_Version']} → Latest: {item['Latest_Version']}\n\n")
    print("✅ Report generated: report.txt")
else:
    print("🎉 All software is up-to-date!")
