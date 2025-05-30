import json
import argparse

# Load the JSON data
with open('ip-ranges.json', 'r') as file:
    data = json.load(file)

# Function to list all unique services
def list_services():
    services = set()
    for prefix in data['prefixes']:
        if 'service' in prefix:
            services.add(prefix['service'])
    print('\n'.join(sorted(services)))

# Function to find and print IP prefixes based on region and service
def find_prefixes(region=None, service=None):
    ip_list = []
    for prefix in data['prefixes']:
        if (
            'region' in prefix and prefix['region'] == region and
            'service' in prefix and prefix['service'] == service
        ):
            ip_list.append(prefix['ip_prefix'])
    print(', '.join(ip_list))

def find_all_prefixes(service=None):
    ip_list = []
    for prefix in data['prefixes']:
        if 'service' in prefix and prefix['service'] == service:
            ip_list.append(prefix['ip_prefix'])
    print(', '.join(ip_list))

# Set up argparse
parser = argparse.ArgumentParser(description="Filter AWS IP ranges by region and service")
parser.add_argument('--region', type=str, help='Region to filter by (e.g., us-east-1)')
parser.add_argument('--service', type=str, help='Service to filter by (e.g., S3)')
parser.add_argument('--list-services', action='store_true', help='List all available services')

args = parser.parse_args()

# Validate region and service arguments
if args.region == 'global':
    region = 'GLOBAL'
else:
    region = args.region.lower() if args.region else None
service = args.service.upper() if args.service else None

# Handle logic based on arguments
if args.list_services:
    list_services()
elif region and service:
    find_prefixes(region, service)
elif service:
    find_all_prefixes(service)
else:
    parser.print_help()
