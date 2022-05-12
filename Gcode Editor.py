file_name = "3DBenchy_with_supports.gcode"  # put your filename here
split_file_name = file_name.split(".")

filamentDirectionDown = True #if filamentDirectionDown == True, extruder should feed filament towands the base (used for T0)

with open(file_name, 'r+') as f:

    content = f.readlines()  # gcode as a list where each element is a line 

    for line in content:
        gcode = line.strip("\n")
        if "T1" in gcode:
            filamentDirectionDown = False
        elif "T0" in gcode:
            filamentDirectionDown = True

        if "E" in gcode and  filamentDirectionDown == False:
            gcode = gcode.replace("E","E-")

        n = open(split_file_name[0] + "_Resliced"+".gcode","a")
        n.write("\n")
        n.write(gcode)
        n.close

print("Done")

#Notes - This does not take into account already E- commands (for retraction), instead creates them E-- commands.
#      - This also does not account for E0 commands aswell, instead creates E-0.
#      - Start gcode file tells T1 to heat up (line 15), editor does get confuse.
#      - Changes capital E's in comments