import re

class SMCErrors:
    
    models = ['PA-54', 'PA-70', 'PA-7500']

    def check_boot_errors(lines, section):
        # Reviews the provided tech support file (lines), and specifically the show chassis status section (section)
        # and determines whether any SMCs are in the Starting/None or Up/None state.  This indicates a card that is either still booting (possibly problematic)
        # or has booted without a configuration loaded (definitely problematic).
        # Possible triggers of this latter state include PAN-255323.
        result = ""
        # RegExes to check if an SMC has failed to boot correctly
        # we check to see if a string similar to the following is found:
        # ^\d+          (.*)SMC(.*)      (Starting|Up)                 None
        SMCBootFailure = re.compile(r"SMC(.*)Starting(.*)None")
        SMCConfigFailure = re.compile(r"SMC(.*)Up(.*)None")

        PA7k = re.compile(r"(.+)PA-70(.+)")
        PA5k = re.compile(r"(.+)PA-54(.+)")
        PA7k5 = re.compile(r"(.+)PA-7500(.+)")

        line = ""
        sect = ""
        chassis = False

        for line in lines:
            # check to see if we are dealing with a chassis platform which uses SMCs
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
                if SMCBootFailure.search(sect):
                    s = result
                    result = s + "SMC Boot Failure:\n" + sect
                if SMCConfigFailure.search(sect):
                    s = result
                    result = s + "SMC Config Load Failure:\n" + sect
        else:
            print("not a chassis platform, continuing")
            result = ""
        
        return result

                

