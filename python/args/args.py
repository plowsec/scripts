import argparse,sys

class Main:

    def __init__(self, quiet = False):

        self.quiet = quiet

    def execute(self):
        """Here, we parse the commandline options and react according to them"""

        parser = argparse.ArgumentParser(description="A simple vulnerability finder")

        #either we analyze an entire directory or a single file, not both
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-f", "--file", metavar="FILE", help="File to analyze", dest="filename")
        group.add_argument("-d", "--directory", metavar="DIRECTORY", help="Directory containing the files to analyze", dest="directory")
        parser.add_argument("-q", "--quiet", dest="quiet", action="store_true")

        options = parser.parse_args()

        #if no input files specified
        if options.directory==None and options.filename==None:
            parser.error("[!] You need to feed me with files to analyze")
            parser.print_help()
            sys.exit(1)

        #directory as input
        elif options.directory:
            self.get_targets_list(options.directory)

        #single file as input
        else:
            self.analyze_single_file(options.filename)

if __name__ == "__main__":
    main = Main()
    main.execute()
