# super-simple-parser
A very simple and lightweight JSON parser for the `ip-ranges.json` list of IPs of public AWS services.

## Setup Instructions:
1. Ensure that both the `parser.py` and `ip-ranges.json` are in the same directory.
2. If you wish to set aliases for easier CLI use:
   - **For Mac:**
     - type 'nano ~/.zshrc' and add your alias with:
       
       ```bash
       alias name="python3 ~/Path/To/parser.py"
       ```
       **(You can use 'pwd' in terminal to see the full path to the parser.py file while in directory that contains it)**

   - **For Windows:**
     - type `notepad $PROFILE` in PowerShell and add:
    
       ```powershell
         function name {
          py "C:\Users\yourname\directoryname\parser.py" $args
        }
       ```

This will now allow you to type the *name* you defined followed by the arguements in the CLI instead of typing the full command like:

`python parser.py --service ... --region ...`
and instead use
`name --service ... --region ...`


## Usage
- `--service name`: Allows you to query the CIDR blocks of a specific AWS service by passing its name.
  - Naming conventions are already handled in the code, so you don't have to worry about character capitalization.
  - Note: Just passing the --service argument without including --region will return CIDR blocks for all regions.
- `--region name`: Allows you to query the CIDR blocks of a service given a specific region. For example:
  - `--service ec2 --region us-east-1` returns all CIDR blocks for EC2 in the `us-east-1` region.
- `--list-services`: Displays a list of all available AWS services present in the JSON file.

## Example Commands

```bash
# Get all CIDR blocks for the EC2 service across all regions
python parser.py --service ec2
# → Example output:
#   3.80.0.0/12, 52.36.0.0/14, 54.72.0.0/13, etc.

# Get all CIDR blocks for CloudFront in the us-east-1 region
python parser.py --service cloudfront --region us-east-1
# → Example output:
#   205.251.192.0/19, 205.251.249.0/24, etc.

# Get all available AWS service names from the JSON file
python parser.py --list-services
# → Example output:
#   ec2
#   cloudfront
#   s3
#   dynamodb
#   route53
#   etc.

# Using your alias (if set up) to query S3 across all regions
myparser --service s3
# → Example output:
#   52.216.0.0/15, 52.219.0.0/16, etc.

# Use alias with both service and region to query DynamoDB in eu-west-2
myparser --service dynamodb --region eu-west-2
# → Example output:
#   52.94.76.0/22, 52.119.24.0/22, etc.

# List services using alias
myparser --list-services
# → Example output:
#   EC2
#   S3
#   DYNAMODB
#   CLOUDFRONT
#   etc.
```
 
## Summary
This tool allows you to query specific CIDR blocks that may be useful for monitoring data traffic through your environment or any other use case that requires working with IP ranges. I built this tool while analyzing traffic on my project's AWS network and found it much more efficient than manually scrolling through the `ip-ranges.json` list. If you have any feedback, suggestions, feature requests, or would like to collaborate, feel free to reach out through one of the links in my profile!

Thanks! :blush:
