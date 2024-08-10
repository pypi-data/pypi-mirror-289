#TODO, replace hardcode data

import json
from datetime import datetime, timedelta
import re


def read_json(file_path):
     with open(file_path, 'r') as json_file:
         return json.load(json_file)
     
def parse_version(version):
    parts = version.split('-')[0].split('.')
    panos_version = '.'.join(parts[:2])
    return panos_version


def convert_kib_to_gb(kib):
    """Convert KiB to GB."""
    return int(kib / 1024 / 1024)

def extract_memory_value(log_content):
    """Extract the first KiB memory value from the log content."""
    pattern = r'KiB Mem\s*:\s*(\d+)\s*total'
    match = re.search(pattern, log_content)
    if match:
        return int(match.group(1))
    return None

def get_current_memory_size(path, hw_model=None):
    #TODO if HW model extend more than M-100, here we need modify the way to detect memory
    
    log_file_path = path+"/var/log/pan/mp-monitor.log"
    with open(log_file_path, 'r') as file:
        log_content = file.read()
    kib_memory_value = extract_memory_value(log_content)
    if kib_memory_value is not None:
        # Convert KiB to GB
        gb_memory_value = convert_kib_to_gb(kib_memory_value)
        # print(f"Memory: {kib_memory_value} KiB")
        # print(f"Memory: {gb_memory_value:.2f} GB")
    return gb_memory_value


def get_target_panos_version(section):
    version_pattern = r'sw-version:\s*(\d+\.\d+\.\d+)'
    hw_model_pattern= r'model:\s*(\S+)'
    k2_serial=False
    for line in section:
        if re.match("sw-version:",line):
            match = re.search(version_pattern, line)
            target_version= match.group(1)
        if re.match("model:",line):
            match = re.search(hw_model_pattern, line)
            hw_model= match.group(1)
        if "express-mode: yes" in line:
            k2_serial=True
    if k2_serial:
        # > show system info
        # The output indicates express-mode: yes or express-mode: no.
        # express-mode: yes = K2
        hw_model=hw_model+"-K2"
    return target_version.replace("sw-version: ",'').strip(),hw_model.strip()

def get_line_cards_list(linecard_section):
    '''
    get all line card into a list
    '''
    pattern = re.compile(r'^\s*\d+\s+(\S+)\s+Up\s+Success\s*$')
    line_cards_list=[]
    for line in linecard_section:
        match = pattern.match(line)
        if match:
            line_cards_list.append(match.group(1))
    # print(line_cards_list)    
    return line_cards_list

def strip_eol_time(time_str):
    return datetime.strptime(time_str, '%Y-%m-%d')


def match_platform(hw_model):
    #TODO, need special case for HW model name, more test is needed.
    PA7k = re.compile(r"(.+)PA-70(.+)")
    PA5k = re.compile(r"(.+)PA-54(.+)")
    PA7k5 = re.compile(r"(.+)PA-7500(.+)")
    PA2xx = re.compile(r"(.+)PA-220(.+)")
    PA8xx = re.compile(r"(.+)PA-8(.+)")
    PA32xx = re.compile(r"(.+)PA-32(.+)")
    K2serial= re.compile(r"(.+)-K2") #?
    M5oo= re.compile(r"(.+)M-500(.+)")
    
    if PA7k.match(hw_model):
        hw_model_converted="PA-7000"
    elif PA2xx.match(hw_model):
        hw_model_converted="PA-220" #checked
    elif PA8xx.match(hw_model):
        hw_model_converted="PA-800" # checked
    elif PA32xx.match(hw_model):
        hw_model="PA-3200" # checked 
    elif K2serial.match(hw_model):
        hw_model="K2-Series" #checked
    elif M5oo.match(hw_model):
        hw_model="M-500" 
    else:
        hw_model_converted="Common Chassis"
    return hw_model_converted
    
    
def get_eol_date(current_version, hw_model,eol_data, line_card=[], memory=None):
    """
    Get the EOL date for a given software version considering memory and line card exceptions.
    
    Parameters:
    - current_version (str): The current PAN-OS version (e.g., "9.1", "8.1").
    - eol_data (dict): The EOL data dictionary.
    - line_card (list): A list of line card models.
    - memory (str): The memory size (e.g., "16GB", "32GB"). Default is None. only for M-100
    
    Returns:
    - str: return time
    """
    major_version_pattern = r'^(\d+\.\d+)\.(\d+)$'
    match = re.search(major_version_pattern, current_version)
    if match:
        version = match.group(1)
    # Check if the current version is in the EOL data
    if version in eol_data:
        # Get the EOL information for the current version
        version_info = eol_data[version]
        
        # Check for exceptions based on memory
        if memory is not None and version in ["9.1", "8.1"]:
            for eol_exception in version_info.get("Exceptions", []):
                if memory > 30: #loose the size, sometimes it is 31.6
                    memory= "32GB"
                elif memory <= 15: # make it 16 G, if not upgrade RAM
                    memory ="16GB"
                if eol_exception.get("type") == "RAM" and eol_exception.get("module") == memory:
                    return strip_eol_time(eol_exception["End_of_Life_Date"])
 
        if match_platform(hw_model):
           for eol_exception in version_info.get("Exceptions", []):
                    if eol_exception.get("type") == "Chassis" and hw_model in eol_exception.get("model"):
                        return strip_eol_time(eol_exception["End_of_Life_Date"])
                           
        # Check for exceptions based on line card, and from current exception, line card EOL date is late or equal to Chassis type
        if line_card:
            for eol_exception in version_info.get("Exceptions", []):
                if eol_exception.get("type") == "Module" and eol_exception.get("module") in line_card:
                    return strip_eol_time(eol_exception["End_of_Life_Date"])
                 
        # Return the default EOL date if no exceptions apply
        return strip_eol_time(version_info["End-of-Life_Date"])
    
    # Return None if the current version is not found in the EOL data
    return None

def recommend_upgrade(version, eol_data, hw_model,line_cards=[],memeory_size=None):
    
    #if this has memeory size not none, then it is M-100, check memory size and get eol date accordingly 
    eol_date = get_eol_date(version, hw_model,eol_data,line_cards,memeory_size)

    if eol_date:
        current_date = datetime.now()
        days_until_eol = (eol_date - current_date).days

        line_cards_string=""
        memeory_size_string=""
        if len(line_cards)>0:
            line_cards_string= f" with line card {line_cards},"
        if memeory_size:
            memeory_size_string=f" memory size {memeory_size},"
        if days_until_eol <= 90:
            return f"HW {hw_model}{line_cards_string}{memeory_size_string}, recommand upgrade {version}. End-of-Life date is within {days_until_eol} days on {eol_date.strftime('%Y-%m-%d')}.", 1
        else:
            return f"HW {hw_model}{line_cards_string}{memeory_size_string}. No immediate upgrade needed for {version}. End-of-Life date is {eol_date.strftime('%Y-%m-%d')}.", 0
    else:
        return f"End-of-Life date not found for version {version}." ,0


class EOLErrors:

    
    models = ['*']
    EOL_INFO_SRC="./tools/PANOS_EOL_Plus_HW_EOL.json"

    def check_eol_errors(info_section,line_card_section,path):
        panos_version,hw_model= get_target_panos_version(info_section)
        if hw_model=="M-100":
            memeory_size=get_current_memory_size(path) 
        else:
            memeory_size=None
        line_cards= get_line_cards_list(line_card_section)
        eol_data=read_json(EOLErrors.EOL_INFO_SRC)
        return recommend_upgrade(panos_version,eol_data,hw_model,line_cards,memeory_size)




    