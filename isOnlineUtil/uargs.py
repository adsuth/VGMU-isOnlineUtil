
import argparse as ap
from color import Color as CLR

def retrieveArguments():
  parser = ap.ArgumentParser(
    prog = "IsOnline Util",
    description = f"{CLR.bold}Returns a list of offline tracks. {CLR.end}",
  )

  parser.add_argument(
    dest = "sources",
    nargs = "+",
    type = str,
    default = [],
    help = f"{CLR.yellow}Directory of source file(s) to be converted to docs. {CLR.end}",
  )

  parser.add_argument(
    "-t", "--tsv",
    dest = "parseTSV",
    action="store_true",
    default = False,
    help = f"{CLR.yellow}Choose to parse TSV file(s). (default) {CLR.end}",
    required = False
  )

  parser.add_argument(
    "-c", "--csv",
    dest = "parseCSV",
    action="store_true",
    default = False,
    help = f"{CLR.yellow}Choose to parse CSV file(s). {CLR.end}",
    required = False
  )

  parser.add_argument(
    "-v", "--verbose",
    dest = "verboseMessaging",
    action="store_true",
    help = f"{CLR.yellow}If present, verbose messaging will be enabled. {CLR.end}",
    required = False
  )
  return parser.parse_args()
