from inspect import ArgInfo
from color import Color as CLR
from globals import state, args
from util import verbosePrint

from pprint import pprint

from veripath import getCSVFromDir, getJSONFromDir
import songGetter as sg
from youtubeScraper import getVideoDetailsFromList, getVideoDetailsFromUrl
from generateHTML import generateHTML


def main():
  sourceDir = args.sources
  state.sourceFiles = []
  state.songs = {}
  
  state.sourceFiles = getCSVFromDir( sourceDir )
  if len( state.sourceFiles ) == 0:
    print( f"{CLR.red}No TSV or CSV files found. Aborting. {CLR.end}" )
    
  state.songs = sg.getSongsFromCSV( state.sourceFiles )
  if len( state.songs ) == 0:
    print( f"{CLR.red}No songs found in given file(s). Aborting. {CLR.end}" )

  if not args.verboseMessaging:
    print( f"{CLR.yellow}Checking song links... This may take a while. {CLR.end}" )

  brokenSongs = findBrokenLinks( state.songs )
  
  generateHTML( brokenSongs )
  print( f"{CLR.green}Done. Exported broken songs to ./index.html {CLR.end}" )

def findBrokenLinks( songs ):
  HAPPY = CLR.end
  BROKEN = CLR.yellow
  DELETED = CLR.red
  UNLICENSED = CLR.blue

  verbosePrint( f"{CLR.bold}This color is {HAPPY}happy{CLR.end}" )
  verbosePrint( f"{CLR.bold}This color is {DELETED}deleted{CLR.end}\n" )
  # verbosePrint( f"{CLR.bold}This color is {UNLICENSED}unlicensed{CLR.end}" )
  # verbosePrint( f"{CLR.bold}This color is {BROKEN}broken{CLR.end}" )
  
  brokenSongs = []
  for song in songs:
    response = getVideoDetailsFromUrl( song.url )
    if response == "happy":
      verbosePrint( f"{HAPPY}{song.name} - {song.url} {CLR.end}" )
    elif response == "deleted":
      brokenSongs.append( song )
      verbosePrint( f"{DELETED}{song.name} - {song.url} {CLR.end}" )
    elif response == "unlicensed":
      verbosePrint( f"{UNLICENSED}{song.name} - {song.url} {CLR.end}" )
    else:
      verbosePrint( f"{BROKEN}{song.name} - {song.url} {CLR.end}" )

  return brokenSongs

if __name__ == "__main__":
  main()