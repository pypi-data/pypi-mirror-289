import re
class recs:

    # Device Certificate Information
    def check_device_cert(line):
        result = "Device Certificate is currently Valid"
        if not "Valid" in line:
            result = "Certificate is Not Valid. Please renew device certificate"
        
        return result
    

    # Session Usage recommendations check if utilization is at or above 80%
    def session_recommendation(usage):
        session_rec = "Session Utilization is healthy below 80%\n" + usage
        for x in range(80, 100):
            if str(x) in usage:
                session_rec = "Session Utilization above 80% Detected.\nRecommendation: Look into Upgrading Firewall"

        return session_rec

    # Process recommendations, check if all processes are still running

    def process_recommendation(section):
        process_result = "All Processes running as Expected"
        errors = []
        for line in section:
            if "pid: -1" in line:
                process_result = line
                errors.append("\nError with process: " + process_result + "Recommendation: Restart Process")
        
        if not errors:
            return process_result
        else:
            return errors
        
    def users_report(section):
            return section + "Recommendation: Verify if this is the correct number of users"
    
    # Debug dataplane recommendations, check if packet filter, logging, and pcap are enabled. If yes, recommend they are disabled.
    def debugs_status(filter, log, capture):
        status = []
        indexes = ["Packet Filter", "Logging", "Packet Capture"]

        combined_list = [filter, log, capture]
        for index,line in zip(indexes,combined_list):
            if "yes" in line:
                status.append(index + " is enabled. Recommendation: Disable this feature\n\n")
            elif "no" in line:
                status.append(index + " is disabled.\n\n")
                
        return status

    def check_logdb_quota(logdb_quota_section):
        recommendation = "LogDb Quota is below 90% Allocation."

        LogDBQuota = re.compile(r"(.+)\: (\d+\.\d\d)(\%,)(.*)") 
        
        LogDBSection = ""
        LogDBPct = 0.00
        
        
        for quotaline in logdb_quota_section:
            q = LogDBQuota.match(quotaline)
            if q:
                LogDBSection = q.group(1).strip()
                LogDBPct = q.group(2).strip()
                for x in range(90,100):
                    if str(x) in LogDBPct:
                        print(LogDBPct)
                        recommendation = recommendation + "The " + LogDBSection + " section is at " + LogDBPct + " percent.\n"
                        recommendation = recommendation + "Refer to https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClgZCAS \n"
       
        return recommendation
        
    def extract_numbers(lst):
    #Extracts numbers from a list of strings using regular expressions.
    # Compile a regular expression pattern to match digits
        pattern = re.compile(r'\d+')
     
    # Use the pattern to extract all digits from each string in the list
        extracted_numbers = [pattern.findall(s) for s in lst]
     
    # Convert the extracted numbers from strings to integers
        return [int(x) for sublist in extracted_numbers for x in sublist]
 
    # Ensure the number of IPSEC tunnels configured and shown are the same number    
    def ensure_match(lst):
        # Makes sure the number of configured tunnels and tunnels shown are the same
        if lst[1] == lst[2]:
            status = "All "+ str(lst[1]) + " IPSEC tunnels are performing as expected"
        else:
            status = "There is an IPSEC Tunnel Down. Refer to https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA14u000000wlFxCAI"
        return status
    
    # Check for the usage percentage on pancfg, root and panlogs partitions
    def find_percentage(lst):
        try:
            percent = []
            for line in lst:

                res = re.findall(r'\d*%', line)
                percent.append(str(res))
            return percent
        except:
            print("Cannot find percentages")
    
    # check if the usage percentage on these partitions are above 85% and report
    def check_disk_usage(lst):
        status = []
        disks = ["root", "pancfg", "panlog"]
        for disk,line in zip(disks,lst):
            status.append(disk + " is at " + line +" disk usage percentage\n")
            for i in range(85,99):
                if str(i) in line:
                    status.append("High Disk Usage for disk: " + disk + ". Recommendation: Free up Disk Space\n Refer to this link for help:https://docs.paloaltonetworks.com/pan-os/11-1/pan-os-admin/certificate-management/obtain-certificates/device-certificate\n\n")
        
        
        return status
    
# Write results to the output file
    def generate_output(device_info, eol_info,ha_info, session_rec, cert_rec, process_rec, user_report, packet_report, tunnel_report,disk_report, 
                        system_error_report, zone_report, telemetry_report, dp_cpu_report, mp_cpu_report, logdb_report, environment_report,
                        process_cpu_report):
       
        try:
            with open("status.txt", 'w') as status:
                status.write("Config Analysis For:\n\n")
                status.writelines(device_info)
                status.write("\nHigh Availability Information:\n\n")
                status.writelines(ha_info)
                status.write("\n\nSession Utilization Status:\n\n")
                status.write(session_rec)
                status.write("\n\nDevice Certificate Status:\n\n")
                status.write(cert_rec)
                status.write("\n\n\nSoftware Status:\n\n")
                status.write(process_rec)
                status.write("\n\n\nGlobal Protect Users Status:\n\n")
                status.write(user_report)
                status.write("\n\n\nPacket Filter Data Plane Status:\n\n")
                status.writelines(packet_report)
                status.write("\n\nIPSEC Tunnel Status:\n\n")
                status.write(tunnel_report)
                status.write("\n\nHardware Information:\n\n")
                status.write(eol_info)
                status.writelines(environment_report)
                status.write("\n\n\nDisk Usage Status:\n\n")
                status.writelines(disk_report)
                status.write("\n\n\nDP CPU Report:\n\n")
                for r in dp_cpu_report:
                    status.writelines(r)
                status.write("\n\n\nMP CPU Report:\n\n")
                for r in mp_cpu_report:
                    status.writelines(r)
                status.write("\n\n\nProcess CPU Utilisation Report:\n\n")
                for r in process_cpu_report:
                    status.writelines(r)
                status.write("\n\n\nLogDb Quota Status:\n\n")
                status.writelines(logdb_report)
                

                status.write("\n\nSystem Log Checks:\n")
                status.write("\nSystem Log Errors:\n\n")
                status.writelines(system_error_report)
                status.write("\n\n\nZone DOS Protection Status:\n\n")
                status.writelines(zone_report)
                status.write("\n\nDevice Telemetry Status:\n\n")
                status.writelines(telemetry_report)
                status.close()
        except Exception as e:
            print("Could Not Generate Output File")
            print(repr(e))

