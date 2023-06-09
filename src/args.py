import sys
import save
import engine

# PARSE COMMAND-LINE ARGUMENTS
def parseArguments():
    engine.get().set_depth(18)

    saveFileSpecified = False
    argMode = ""
    for argument in sys.argv:
        if argument == "-d" or argument == "--depth":
            argMode = "depth"
            continue
        elif argument == "-f" or argument == "--file":
            argMode = "file"
            continue

        if argMode == "depth":
            argMode = ""
            if argument.isdigit():
                engine.get().set_depth(int(argument))
        elif argMode == "file":
            argMode = ""
            try:
                save.load()
                saveFileSpecified = True
            except:
                print("Analysis savefile failed to load.")

    if not saveFileSpecified:
        engine.startAnalysisThread()