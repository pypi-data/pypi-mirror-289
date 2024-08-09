import os
import sys
import tarfile 
import pathlib
import shutil
import generate_output as go
import platformView as pv
import SMC_errors as SMCErrors
import NPC_errors as NPCErrors
import PanoramaTSF as PanoramaTSF
import EOL_errors as EOLErrors
import traceback

from DP_CPU_reports import DP_CPU_reports as DPCPUReports
from MP_CPU_reports import MP_CPU_reports as MPCPUReports 


# Read individual sections of the file by cutting them out from a beginning line and end line  
def getInfo(lines, begin, end):
    copy = False
    list = []
    for line in lines:
        if line.strip() == begin:
            copy = True
            continue
        elif line.strip() == end:
            copy = False
            continue
        elif copy:
            list.append(line)
    return list
# get more exact info from already cut out section of file
def getLocalInfo(lines, first, second, third):
    for line in lines:
        if first in line:
            first = line
        if second in line:
            second = line
        if third in line:
            third = line
    group = [first, second, third]
    return group

def directorySearch(path, fileToSearch):
    for relPath, dirs, files in os.walk(path):
        if (fileToSearch in files):
            filePath = os.path.join(relPath,fileToSearch)
            return filePath

def getExactLine(lines, search):
    output = ''
    for line in lines:
        if search in line:
            output = line
    return output

path = ""
supportFile = ""
supportFilePath = ""

# remove unnecessary lines full of dashes and system call lines
def cleanData(lines):
    for line in lines:
        if "---------" in line:
            lines.remove(line)
        elif '>' in line:
            lines.remove(line)

    return lines

if(len(sys.argv) == 1):
    path = input("Enter tech support folder name: ")
    supportFile = input("Enter cli tech support file name: ")
    supportFilePath = directorySearch(path, supportFile)

elif(len(sys.argv) == 2):
    # check to see if the second argument is a file
    if(os.path.isfile(sys.argv[1])):
        # if it is, untar it to a temporary directory
        file = tarfile.open(sys.argv[1])
        shutil.rmtree("./temp/", ignore_errors=True)
        os.mkdir('./temp/')
        file.extractall('./temp/')
        path = "./temp/"
        # identify the techsupport_*.txt file in tmp/cli/
        for sfp in pathlib.Path("./temp/tmp/cli").glob("techsupport_*.txt"):
            supportFilePath = sfp
else:
    sys.stderr.write("Usage: " + sys.argv[0] + " [techsupportfilename.tgz]")

# open the file and create a separate file with only the show ha all output instead of looking through the entire file.
try:
    with open(supportFilePath, "r") as in_file:
        lines = in_file.readlines()

        # Get system info
        info_section = getInfo(lines, "> show system info", "> show system last-commit-info")
        model = getExactLine(info_section, "model")
        # Get and display device info for config analysis, i.e device name, panos version, platform
        device_info = getLocalInfo(info_section, "hostname:", "model:", "sw-version:")
        more_info = getLocalInfo(info_section, "uptime:", "serial:", "url-db:")
        version_info = getLocalInfo(info_section, "app-version:", "threat-version:", "url-filtering-version:")

        info_output = device_info + more_info + version_info

        if 'Panorama' in model:
            
            deviceInformation = getInfo(lines, "> show devices connected", "> request system software info")
            admins = getInfo(lines, "> show admins all", "> show clock")
            
            PanoramaTSF.panorama.writeDeviceInformation(info_output,deviceInformation, admins=admins)
            in_file.close()
            quit()
        else:

        
            license_section = getInfo(lines, "> request license info", "> show system masterkey-properties")
            DP_CPU_section = getInfo(lines, "> show running resource-monitor", "> show running security-policy")
            
            urldb_section = getExactLine(info_section, "url-db:")
            
            # reduce the file down to the show high-availability all section
            ha_section = getInfo(lines, "> show high-availability all", "> show high-availability state-synchronization")
            # get separate information for each section local information, peer information, path monitor information, and timer information
            localInfo = getInfo(ha_section, "Local Information:", "Peer Information:")
            linkMonitorInfo = getInfo(ha_section, "Link Monitoring Information:", "Path Monitoring Information:")
            pathMonitorInfo = getInfo(ha_section, "Path Monitoring Information:", "> show high-availability state-synchronization")
            timersInfo = getLocalInfo(ha_section, "Promotion Hold Interval:", "Hello Message Interval:", "Heartbeat Ping Interval:")
            # get specific information that needs to be displayed in the sweep
            localExact = getLocalInfo(localInfo, "State:", "Priority:", "Preemptive:")

            userSection = getInfo(lines, "> show user ip-user-mapping-mp all option count", "> show user ip-user-mapping all option count")
            groupSection = getInfo(lines, "> show user group list", "> show user credential-filter statistics")

            layer_section = getInfo(lines, "> show running dos-policy", "> show running pbf-policy")
            zone_section = getInfo(lines, "> show zone-protection", "> debug dataplane memory status")

            packet_section = getInfo(lines, "> debug dataplane packet-diag show setting", "Username:")
            # Logging Information
            setting_section = getInfo(lines, "> show system setting logging", "> debug device-server dump logging statistics")
            logdb_quota_section = getInfo(lines, "> show system logdb-quota", "> show system disk-space")
            environmentals_section = getInfo(lines, "> show system environmentals", "> debug dataplane internal pdt pci list")
            software_section = getInfo(lines, "> show system software status", "> show jobs pending")

            vpn_section = getInfo(lines, "> show vpn flow", "> show global-protect sysd-health")
            # Global protect information
            gateway_section = getInfo(lines, "> show global-protect-gateway gateway", "> show global-protect-gateway flow")
            flow_section = getInfo(lines, "> show global-protect-gateway flow", "> show global-protect-gateway statistics")
            stats_section = getInfo(lines, "> show global-protect-gateway statistics", "> show global-protect-satellite current-gateway")
            satellite_section = getInfo(lines, "> show global-protect-satellite current-gateway", "> show global-protect-satellite interface all")
            
            # Disk Utilization
            space_section = getInfo(lines, "> show system disk-space", "> debug software disk-usage dangling-fds")
            raid_section = getInfo(lines, "> show system raid detail", "> show wildfire status")
            # SSL Decryption memory usage data
            ssldecrypt_memory_section = getInfo(lines, "> show system setting ssl-decrypt memory", "> show system setting ssl-decrypt certificate")
            ssldecrypt_cert_section = getInfo(lines, "> show system setting ssl-decrypt certificate", "> show system setting ssl-decrypt certificate-cache")
            # session information
            session_section = getInfo(lines,"> show session info", "Session timeout")
            exact_session_info = getLocalInfo(session_section, "Number of sessions supported:", "Number of allocated sessions:", "Session table utilization:  ")
            # PanDB information
            cloud_connect_section = getInfo(lines, "> show url-cloud status", "> show mlav cloud-status")
            # Telemetry information
            telemetry_section = getInfo(lines, "> show device-certificate status", "> show device-telemetry stats all")
            # Core File information
            core_file_section = getInfo(lines, "> show system files", "> show system logdb-quota")

            line_card_section = getInfo(lines, "> show chassis status", "> show chassis status slot s1")

            SMCfailures = SMCErrors.SMCErrors.check_boot_errors(lines, line_card_section)
            if(SMCfailures):
                print ("Errors detected with SMCs")

            NPCfailures = NPCErrors.NPCErrors.check_boot_errors(lines, line_card_section)
            if(NPCfailures):
                print ("Errors detected with NPCs")

            EolCheckError = ""
            environment_info = []
            
            EolCheckError,error_flag=  EOLErrors.EOLErrors.check_eol_errors(info_section,line_card_section, path)
            if error_flag:
                print("Errors detected with EOLs: "+EolCheckError)
            else:
                print(EolCheckError)       
        

                environment_info = []
                for line in environmentals_section:
                    if "True" and "False" in line:
                        pass
                    elif "True" in line:
                        environment_info.append(environment_info)
                
                if not environment_info:
                    print("No alarms found in environment")
                    environment_info = "\n\nNo Environmental alarms found\n"
                else:
                    print("System Environmentals Alarms: " + str(environment_info))

        
        in_file.close()
except Exception as e:
    print(repr(e))
    print(traceback.format_exc())

agentFile = "ha_agent.log"
reportFile = "marvin_report.txt"

# Search through the directories for the ha_agent.log file and open it.
agentFilePath = directorySearch(path, agentFile)

try:
    # Read ha-agent file and return any errors found
    with open(agentFilePath, 'r') as ha_file:
        lines = ha_file.readlines()
        error_count = 0
        # find and print the errors found
        for line in lines:
            if "non-functional" in line:
                print(line)
                error_count += 1
        print("Total Error Count: " + str(error_count))

        ha_file.close()
except Exception as e:
    print("Agent file not found")
    print(repr(e))

routeFile = "routed.log.old"
# Search for routed.log.old file and open it.
routeFilePath = directorySearch(path, routeFile)

try:
    with open(routeFilePath, 'r') as route_file:
        lines = route_file.readlines()

    #find and print errors found
        for line in lines:
            if "Hold Timer Expired(4)" in line:
                print(line)

        route_file.close()
except Exception as e:
    print("No routed log found")
    print(repr(e))

systemLogFile = "show_log_system.txt"
systemLogPath = directorySearch(path, systemLogFile)
try:
    with open(systemLogPath, 'r') as sys_log_file:
        lines = sys_log_file.readlines()
        critical_errors = []
        # find lines with critical errors
        for line in lines:
            if "critical" in line:
                critical_errors.append(line)

        if not critical_errors:
            critical_errors.append("No critical system log errors detected")
            
    sys_log_file.close()
except:
    print("No System log file found")


# Packet buffer information
monitorFile = "mp-monitor.log"
monitorFilePath = directorySearch(path, monitorFile)

DP_CPU_Files = DPCPUReports.find_dp_monitor_log(path)
DP_CPU_Contents = DPCPUReports.open_dp_monitor_log(DP_CPU_Files)
DP_CPU_Report = []

if(DP_CPU_Contents != []):
    # look for high CPU
    DP_CPU_Report = DPCPUReports.dp_monitor_report(DP_CPU_Contents)
    
MP_CPU_Files = MPCPUReports.find_mp_monitor_log(path)
MP_CPU_Contents = MPCPUReports.open_mp_monitor_log(MP_CPU_Files)
MP_CPU_Report = []
Process_CPU_Report = []

if(MP_CPU_Contents != []):
    MP_CPU_Report = MPCPUReports.mp_monitor_report(MP_CPU_Contents)
    
    Process_CPU_Report = MPCPUReports.mp_process_report(MP_CPU_Contents)
    
try:
    with open(monitorFilePath, 'r') as mon_file:
        
        lines = mon_file.readlines()
        lograte = []
        
        for line in lines:
            if "Log incoming rate:" in line:
                lograte.append(line)

        
except Exception as e:
    print("No mp-monitor.log file found")
    print(repr(e))

telemetry_section = cleanData(telemetry_section)
zone_section = cleanData(zone_section)

try:
    with open("output.txt", 'w') as out:
        out.write("System Infomation:\n")
        out.writelines(info_section)
        out.write("\nSystem Environmentals:\n")
        out.writelines(environmentals_section)
        out.writelines(packet_section)
        out.write("\nSession Information:\n")
        out.writelines(exact_session_info)
        out.write("\nLicense Information:\n")
        out.writelines(license_section)
        out.write("\nDP CPU Information:\n")
        out.writelines(DP_CPU_section)
        out.write("\nHigh Availibity Information:\n")
        out.writelines(localExact)
        out.write("\n")
        out.writelines(pathMonitorInfo)
        out.write("\n")
        out.writelines(timersInfo)
        out.write("\nUser Information:\n")
        out.writelines(userSection)
        out.write("\n")
        out.writelines(groupSection)
        out.write("\nLayer 7 Information:\n")
        out.writelines(layer_section)
        out.write("\n")
        out.writelines(zone_section)
        out.write("\nLogging Information:\n")
        out.writelines(setting_section)
        out.write("\nLog rate: \n")
        out.writelines(lograte)
        out.write("\n")
        out.writelines(logdb_quota_section)
        out.write("\n")
        out.writelines(vpn_section)
        out.write("\nGlobal Protect Information:\n")
        out.writelines(gateway_section)
        out.write("\n")
        out.writelines(flow_section)
        out.write("\n")
        out.writelines(stats_section)
        out.writelines(satellite_section)
        out.write("\nDisk Utilization:\n")
        out.writelines(space_section)
        out.write("\n")
        out.writelines(raid_section)
        out.write("\nSSL Decryption Memory Usage Information:\n")
        out.writelines(ssldecrypt_memory_section)
        out.write("\n")
        out.writelines(ssldecrypt_cert_section)
        out.write("\nSoftware Status:\n")
        out.writelines(software_section)
        out.write("\nPanDB Information:\n")
        out.writelines(cloud_connect_section)
        out.write("\nDevice Telemetry Information:\n")
        out.writelines(telemetry_section)
        out.write("\nCore File Information:\n")
        out.writelines(core_file_section)
        if(SMCfailures):
            out.write("\nSMC Failure Info:\n")
            out.writelines(SMCfailures)
        if(NPCfailures):
            out.write("\nNPC Failure Info:\n")
            out.writelines(NPCfailures)

        out.close()

except Exception as e:
    print("Could not generate output file")
    print(repr(e))


# Display recommendations based on content

#Device telemetry and certificate information
certificate_status = getExactLine(telemetry_section, "Current device certificate status:")
certificate_result = go.recs.check_device_cert(certificate_status)
# High Availability Information

ha_status = getLocalInfo(ha_section, "State:", "Priority:", "Preemptive")
link_status = ["\nLink Monitoring Status:\n"]
# Check if each link interface is up if not inform of failure

pathMonitorInfo.insert(0, "\nPath Monitoring Status:\n")
ha_status = ha_status + link_status + linkMonitorInfo + pathMonitorInfo
# Add LogDb Quota status to status.txt
logdb_quota = go.recs.check_logdb_quota(logdb_quota_section)

# Check if the platform is a 5400 or 7k series if yes check chassis information 
model = getExactLine(device_info, "model")
platform_info = pv.platform.check_platform(model)
    
# Session Usage recommendations check if utilization is at or above 80%
session_usage = getExactLine(exact_session_info, "Session table utilization:")
session_result = go.recs.session_recommendation(session_usage)

# Check if all processes are running as expected
process_result = go.recs.process_recommendation(software_section)


# Global protect recommendations

current_users = getExactLine(stats_section, "Total Current Users:")
user_result = go.recs.users_report(current_users)


# Packet Section
filter_info = getInfo(packet_section, "Packet filter", "Match pre-parsed packet:")
log_info = getInfo(packet_section, "Logging", "Log-throttle:")
capture_info = getInfo(packet_section, "Packet capture", "Snaplen:")

filter_local = getLocalInfo(filter_info, "Enabled:", "Match pre-parsed packet:", "Filter offload")
log_local = getLocalInfo(log_info, "Enabled:", "Log-throttle:", " Sync-log-by-ticks:")
capture_local = getLocalInfo(capture_info, "Enabled:", "Snaplen:", "---")

filter_status = getExactLine(filter_local, "Enabled:")
log_status = getExactLine(log_local, "Enabled:")
capture_status = getExactLine(capture_local, "Enabled:")
packet_result = go.recs.debugs_status(filter=filter_status, log=log_status, capture=capture_status)

# Ensure all IPSEC Tunnels are running as expected
tunnel_info = getExactLine(vpn_section, "total IPSec tunnel configured:")
tunnels = go.recs.extract_numbers(vpn_section)
if tunnels:
    tunnel_status = go.recs.ensure_match(tunnels)
else:
    tunnel_status = "No tunnels in use."


# Check the space of the root, pancfg, and panlog disks 
space_info = getLocalInfo(space_section, "/", "/opt/pancfg", "/opt/panlog")
percent = go.recs.find_percentage(space_info)

disk_status = go.recs.check_disk_usage(percent)


go.recs.generate_output(device_info=info_output, eol_info=EolCheckError,ha_info=ha_status, session_rec=session_result, cert_rec=certificate_result, process_rec=process_result,
                         user_report=user_result, packet_report=packet_result, tunnel_report=tunnel_status, disk_report=disk_status, system_error_report=critical_errors,
                         zone_report=zone_section, telemetry_report=telemetry_section, dp_cpu_report=DP_CPU_Report, mp_cpu_report=MP_CPU_Report, logdb_report=logdb_quota, 
                         environment_report=environment_info, process_cpu_report=Process_CPU_Report)


shutil.rmtree("./temp/", ignore_errors=True)
