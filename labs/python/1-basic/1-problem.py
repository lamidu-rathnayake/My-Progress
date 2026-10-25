scanner_id = "  scn-2045  "
model = "canon dr-c240"
branch = "  Colombo  "
filename = "maintenance_report.csv"

scanner_id_fixed = scanner_id.strip().upper()
model_fixed = model.upper()
branch_fixed = branch.strip()
scannerIdStart = scanner_id_fixed.startswith("SCN-")
filenameEnd = filename.endswith(".csv")
scannerYear = scanner_id_fixed.split("-")[1]
isNumerical = scannerYear.isdigit()

print(f"Scanner ID: {scanner_id_fixed}")
print(f"Model: {model_fixed}")
print(f"Branch: {branch_fixed}")
print(f"Valid prefix: {scannerIdStart}")
print(f"CSV file: {filenameEnd}")
print(f"Numeric ID: {isNumerical}")
