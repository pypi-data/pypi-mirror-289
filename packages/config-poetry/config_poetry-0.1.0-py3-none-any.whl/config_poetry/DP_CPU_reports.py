import re
from pathlib import Path
from glob import glob


class DP_CPU_reports:
    def find_dp_monitor_log(path):
        dp_monitor_files = []
        # look for dp-monitor.log - if not found, return an empty list
        for p in glob(path + '/**/dp-monitor.log*', recursive=True):
            dp_monitor_files.append(p)

        return dp_monitor_files
        
    def open_dp_monitor_log(dp_monitor_file):
        # open - and concatenate - dp-monitor.log files, returning a list consisting of all of their individual lines
        lines = []
        for f in dp_monitor_file:
            try:
                with open(f, "r") as in_file:
                    l = in_file.readlines()
                    lines = lines + l
            except Exception as e:
                print(repr(e))
                return []
        return lines
    
    def dp_monitor_report(DP_CPU_Contents):
        # pull the DP_CPU report and look for any/all high CPU conditions.
        recommendation = []
        CPUUtilisation = re.compile(r"\:(.+) \: (.+)(\d+)(\%)")
        for cpuline in DP_CPU_Contents:
            c = CPUUtilisation.match(cpuline)
            #cpupct = c.group(2)
            if c:
                DP_CPU_Group = c.group(1).strip()
                DP_CPU = c.group(3).strip()
                for x in range(80,100):
                    if str(x) in DP_CPU:
                        recommendation.append("High DP CPU detected: " + DP_CPU + "pct by group " + DP_CPU_Group + "\nRecommend further investigation.")
                        recommendation.append("Refer to KB article https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClRTCA0 \n")

        if(recommendation == []):
            recommendation.append("No high DP CPU condition detected.")
        return recommendation
    
    
    
        
                
     