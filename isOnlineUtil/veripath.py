import os
from color import Color as CLR

def getCSVFromDir( dir ):
  """
  Returns list of strings; files or folders contained with given directory.
  """
  if isinstance( dir, str ):
    dir = [ dir ]

  output = []
  for file in dir:
    output += getFiles( file, "sv" )

  return output



def getJSONFromDir( dir ):
  """
  Returns list of strings; files or folders contained with given directory.
  """
  if isinstance( dir, str ):
    dir = [ dir ]

  output = []
  for file in dir:
    output += getFiles( file, "json" )

  return output



def getFiles( dir, ext ):
  output = []
  for path in os.walk( dir ):
    for innerPath in path[2]:
      formattedPath = f"{ path[0] }\\{ innerPath }"

      if os.path.isfile( formattedPath ) and formattedPath.endswith( ext ):
        print( f"{CLR.blue}Found file {formattedPath}{CLR.end}" )
        output.append( formattedPath )

  return output