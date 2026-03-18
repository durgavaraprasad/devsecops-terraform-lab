import json
import sys

def parse_security_report(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Trivy JSON format usually nests results under 'Results'
        results = data.get('Results', [])
        critical_count = 0
        high_count = 0

        print("--- DevSecOps Security Scan Summary ---")
        
        for result in results:
            vulnerabilities = result.get('Misconfigurations', [])
            for vuln in vulnerabilities:
                severity = vuln.get('Severity')
                if severity == 'CRITICAL':
                    critical_count += 1
                elif severity == 'HIGH':
                    high_count += 1
                
                print(f"[{severity}] ID: {vuln.get('ID')} - {vuln.get('Title')}")

        print("---------------------------------------")
        print(f"Total Critical: {critical_count}")
        print(f"Total High: {high_count}")

        # Logic to fail the build if any Critical vulnerabilities exist
        if critical_count > 0:
            print("RESULT: FAILED - Critical vulnerabilities must be fixed.")
            sys.exit(1)
        else:
            print("RESULT: PASSED - Infrastructure meets security standards.")
            sys.exit(0)

    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # In a real pipeline, the scanner would output to 'results.json'
    parse_security_report('results.json')