class ComplianceRecord:
    def __init__(self, record_id, details, purpose):
        self.record_id = record_id
        self.details = details
        self.purpose = purpose
        self.isPermissionGranted = False

class ImmigrationComplianceSystem:
    def __init__(self):
        self.records = {}
        self.record_counter = 0

    def add_record(self, details, purpose):
        self.record_counter += 1
        record_id = self.record_counter
        self.records[record_id] = ComplianceRecord(record_id, details, purpose)
        print("Compliance record added successfully.")

    def update_record(self, record_id, new_details):
        if record_id in self.records:
            self.records[record_id].details = new_details
            print("Compliance record updated successfully.")
        else:
            print("Record ID not found.")

    def delete_record(self, record_id):
        if record_id in self.records:
            del self.records[record_id]
            print("Compliance record deleted successfully.")
        else:
            print("Record ID not found.")

    def ensure_immigration_compliance(self, case_id):
        print("Ensuring compliance for case ID:", case_id)
        for record in self.records.values():
            if record.record_id == case_id and record.purpose.lower() in ["job", "study", "tourism"]:
                record.isPermissionGranted = True
                print("Compliance ensured.")
                return
        print("Compliance could not be ensured. Invalid purpose or record ID.")

    def audit_compliance_records(self, record_id):
        print("Auditing compliance for record ID:", record_id)
        if record_id in self.records:
            record = self.records[record_id]
            print(f"Record ID: {record.record_id}, Details: {record.details}, Purpose: {record.purpose}, Permission Granted: {record.isPermissionGranted}")
        else:
            print("Record ID not found.")
    
    def display_records(self):
        if self.records:
            print("\nCompliance Records:")
            for record_id, record in self.records.items():
                print(f"Record ID: {record_id}, Details: {record.details}, Purpose: {record.purpose}, Permission Granted: {record.isPermissionGranted}")
        else:
            print("No records found.")

def main():
    system = ImmigrationComplianceSystem()

    while True:
        print("\nImmigration Compliance System")
        print("1. Add Compliance Record")
        print("2. Update Compliance Record")
        print("3. Delete Compliance Record")
        print("4. Ensure Immigration Compliance")
        print("5. Audit Compliance Records")
        print("6. Display Compliance Records")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            details = input("Enter details for the new record: ")
            purpose = input("Enter purpose [Job/Tourism/Study]: ").strip().lower()
            system.add_record(details, purpose)
        elif choice == '2':
            record_id = input("Enter record ID to update: ").strip()
            if record_id.isdigit():
                record_id = int(record_id)
                new_details = input("Enter new details: ")
                system.update_record(record_id, new_details)
            else:
                print("Invalid record ID.")

        elif choice == '3':
            record_id = input("Enter record ID to delete: ").strip()
            if record_id.isdigit():
                record_id = int(record_id)
                system.delete_record(record_id)
            else:
                print("Invalid record ID.")
        elif choice == '4':
            case_id = input("Enter case ID to ensure compliance: ").strip()
            if case_id.isdigit():
                case_id = int(case_id)
                system.ensure_immigration_compliance(case_id)
            else:
                print("Invalid case ID.")
        elif choice == '5':
            record_id = input("Enter record ID to audit: ").strip()
            if record_id.isdigit():
                record_id = int(record_id)
                system.audit_compliance_records(record_id)
            else:
                print("Invalid record ID.")
        elif choice == '6':
            system.display_records()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
