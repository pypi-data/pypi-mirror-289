class panorama:

    # Look through the device list and search for any firewall that is not connected. 
    # If a firewall is disconnected display the firewall and report that it is disconnected
    # Look at the amount of admin users running concurrently and if greater than 25 
    # recommend to keep it below that
    def writeDeviceInformation(info_output, devices, admins):
        deviceLines = []
        inactive_devices = []

        for line in devices:
            if line.startswith('0'):
                deviceLines.append(line)
        for line in deviceLines:
            if ' no ' in line:
                inactive_devices.append(line)

        admins = list(filter(str.strip, admins))
        num_admins = len(admins)
        if num_admins >= 25:
            recommendation = "\nWe recommend you keep concurrent Admin users below 25\n"
        else:
            recommendation = "\nThis is a healthy number of concurrent Admin users"

        try:
            with open("status.txt", 'w') as status:
                status.write("Config Analyis For:\n\n")
                status.writelines(info_output)
                status.write("\n\nThere are " + str(num_admins) + " Admin users on this Panorama. " + recommendation)
                status.write("\n\nConnected Firewall Status:\n\n")
                if not inactive_devices:
                    status.write("\nAll Firewalls are Connected.")
                else:
                    deviceStatus = "\nHere are disconnected Rirewalls, please check why they are not connected\n"
                    status.write(deviceStatus)
                    status.writelines(inactive_devices)

        except Exception as e:
            print("Could not write to file")
            print(repr(e))


