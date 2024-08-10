import re
from pathlib import Path
from glob import glob


class MP_CPU_reports:
    def find_mp_monitor_log(path):
        mp_monitor_files = []
        # look for mp-monitor.log - if not found, return an empty list
        for p in glob(path + '/**/mp-monitor.log*', recursive=True):
            mp_monitor_files.append(p)

        return mp_monitor_files
        
    def open_mp_monitor_log(mp_monitor_file):
        # open - and concatenate - mp-monitor.log files, returning a list consisting of all of their individual lines
        lines = []
        for f in mp_monitor_file:
            try:
                with open(f, "r") as in_file:
                    l = in_file.readlines()
                    lines = lines + l
            except Exception as e:
                print("Error in MP_CPU_reports")
                print(repr(e))
                return []
        return lines
    
    def mp_monitor_report(MP_CPU_Contents):
        # pull the MP_CPU report and look for any/all high CPU conditions.
        recommendation = []
        # looking for lines that look like this:
        # %Cpu(s):  0.2 us,  0.1 sy,  0.0 ni, 99.7 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
        UserSpaceCPU = re.compile(r"(\d+\.\d+) us,")
        SysCPU = re.compile(r"(\d+\.\d+) us,")
        NMI = re.compile(r"(\d+\.\d+) ni,")
        
        for cpuline in MP_CPU_Contents:
            us = []
            uspct = ""
            sy = []
            sypct = ""
            ni = []
            nipct = ""
            
            us = UserSpaceCPU.findall(cpuline)
            if us != []:
                uspct = us[0].split(".")
            
            sy = SysCPU.findall(cpuline)
            if sy:
                sypct = sy[0].split(".")
            
            ni = NMI.findall(cpuline)
            if ni:
                nipct = ni[0].split(".")
    
            for x in range(70,100):
                if str(x) in uspct:
                    recommendation.append("High Userspace CPU detected: " + us[0] + "% \nRecommend further investigation.")
                    recommendation.append("Refer to KB article TODO TODO \n")
                if str(x) in sypct:
                    recommendation.append("High Kernel/System CPU detected: " + sy[0] + "% \nRecommend further investigation.")
                    recommendation.append("Refer to KB article TODO TODO \n")
                if str(x) in nipct:
                    recommendation.append("High NMI CPU detected: " + sy[0] + "% \nRecommend further investigation.")
                    recommendation.append("Refer to KB article TODO TODO \n")
                    

        if(recommendation == []):
            recommendation.append("No high MP CPU condition detected.")

        return recommendation
    
    def mp_process_report(MP_CPU_Contents):
        recommendation = []
        cpuusage = 0.0

        # looking for lines that look like the below
        #  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
        # 1592 root      30  10   18180   2680   2032 R   3.9  0.0   0:00.02 top
        processusage = re.compile(r"^(\s*)(\d+ [a-zA-Z]+\s+)(\d+.+\s+)(\d+\.\d+\s+\d+\.\d+)(.+\d+ )(.+\s*)$")

        for l in MP_CPU_Contents:
            pc = processusage.match(l)
            if(pc != None):
                cpuusage = float(pc.group(4).strip().split(" ")[0])
                processname = pc.group(6).strip()
                if cpuusage > 60.0:
                    errortext = "Process " + processname + " appears to be consuming " + str(cpuusage) + " percent CPU.\nFurther investigation appropriate.\n"
                    errortext = errortext + "Figures higher than 100% do not automatically indicate a problem.\n\n"
                    recommendation.append(errortext) 
 
        if(recommendation == []):
            recommendation.append("No high per-process CPU utilisation detected.")
            
        return recommendation
    
        
                
            
            
                   