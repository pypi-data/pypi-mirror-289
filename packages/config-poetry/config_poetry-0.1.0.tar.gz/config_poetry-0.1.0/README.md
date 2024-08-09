# Scale & Optimize Analyzer


## Solution Overview
This tool is designed to analyze a Technical Support File (TSF) from customer systems and compare their configurations against a predefined set of ideal configurations. It identifies discrepancies and generates alerts for deviations from the ideal standards. The tool performs various health checks across different aspects of the system to ensure optimal performance and adherence to best practices.

## Key Features and Checks
The tool performs the following representative health checks:

- Management Plane: Monitors high CPU processes, zombie processes, disk usage, and memory leaks to ensure efficient system management.

- Data Plane: Checks for high packet buffers, packet filtering configurations, debugging settings, and average data plane CPU usage to maintain smooth data transmission.

- Global Protect: Evaluates usage metrics to ensure effective deployment and utilization of Global Protect features.

- Hardware: Alerts on alarms, disk failures, PSU (Power Supply Unit) failures, and FAN failures to prevent hardware-related disruptions.

- High Availability: Monitors active/passive pair information, link and path statuses to ensure seamless failover and redundancy.

- Security: Includes checks for User ID configurations, IPsec settings, Zone DOS Protections, and log monitoring to enhance network security.

## How It Works
1. Input: Takes a TSF file as input, which contains configuration and diagnostic information from customer systems.

2. Comparison: Compares the configurations found in the TSF against predefined ideal configurations.

3. Alert Generation: Identifies any deviations and generates alerts or notifications for further action.

4. Reporting: Provides detailed reports highlighting discrepancies and suggesting corrective actions.

## Benefits
- Proactive Monitoring: Helps in early detection of configuration issues and potential system vulnerabilities.

- Compliance: Ensures configurations align with industry best practices and organizational standards.

- Efficiency: Automates the process of configuration auditing, saving time and effort compared to manual checks.

## Usage
To use the tool, provide a TSF file from the customer's system. The tool will process this file and generate reports detailing any configuration discrepancies found.

## Limitations
Here are the current sub-categories that the script that is able to read provide an output result:
- Management Plane 
1. Zombie or stopped processes
2. Uptime
3. PANOS
4. Model
5. SN No
6. Threat
7. Content Version
8. URL version
9. Device cert status
10. Session Count/Session Utilization percentage
11. High Disk Utilization
- Data Plane
1. Debugs enabled
2. PCAP enabled
- GlobalProtect
1. Current users logged in
- IPSec
1. Tunnel Down 
