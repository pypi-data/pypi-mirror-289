import re

class NPCErrors:
    
    models = ['PA-54', 'PA-70', 'PA-7500']

    def check_boot_errors(lines, section):
        # Reviews the provided tech support file (lines), and specifically the show chassis status section (section)
        # and determines whether any NPCs are in the Starting/None or Up/None state.  This indicates a card that is either still booting (possibly problematic)
        # or has booted without a configuration loaded (definitely problematic).
        result = ""
        # RegExes to check if an NPC has failed to boot correctly
        # we check to see if a string similar to the following is found:
        # ^\d+          (.*)NPC(.*)      (Starting|Up)                 None
        NPCBootFailure = re.compile(r"NPC(.*)Starting(.*)None")
        NPCConfigFailure = re.compile(r"NPC(.*)Up(.*)None")

        PA7k = re.compile(r"(.+)PA-70(.+)")
        PA5k = re.compile(r"(.+)PA-54(.+)")
        PA7k5 = re.compile(r"(.+)PA-7500(.+)")

        line = ""
        sect = ""
        chassis = False

        for line in lines:
            # check to see if we are dealing with a chassis platform which uses NPCs
            if PA7k.match(line):
                chassis = True
                print(line)
                break
            elif PA5k.match(line):
                chassis = True
                print(line)
                break
            elif PA7k5.match(line):
                chassis = True
                print(line)
                break

        if chassis:
            print("Chassis platform")
            for sect in section: #
                if NPCBootFailure.search(sect):
                    s = result
                    result = s + "NPC Boot Failure:\n" + sect
                if NPCConfigFailure.search(sect):
                    s = result
                    result = s + "NPC Config Load Failure:\n" + sect
        else:
            print("not a chassis platform, continuing")
            result = ""
        
        return result

                

