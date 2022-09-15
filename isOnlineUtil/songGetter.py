import csv
from globals import state

class Song:
  """
  Song objects store data for songs.
  """
  def __init__( self, index, name, game, series, url ):
    self.index = index
    self.name = name
    self.game = game
    self.series = series
    self.url = url

    self.id = getSongId( self.url ) # id == url without fluff


def parseTSV( tsv_dir ):
  """
  Interprets VGMB tsv, stores all lines in a list and returns
  """
  songs = []
  INDEX = 0

  with open( tsv_dir, "r", encoding='utf-8' ) as tsv:
    data = csv.reader( tsv, delimiter="\t" ) if tsv_dir.lower().endswith( ".tsv" ) else csv.reader( tsv, delimiter="," )
    for row in data:
      songs.append( Song( INDEX, row[0], row[1], row[2], row[3] ) )
      INDEX += 1

  return songs


def getGames(songs):
  """
  returns a dictionary with all unique games in the songs list
  """
  games = {}
  for song in songs:
    if song.game in games:
      continue
    games[song.game] = []

  return games


def getSeries( songs ):
  """
  returns a dictionary with all the unique series in the songs tsv
  Currently unused.
  """
  series = {}

  for song in songs:
      if song.series not in series:
          series[song.series] = {}

  return series


def getSongId( url ):
  """
  returns the id of the youtube video.
  eg:
  https://youtu.be/pLJ85XExZtQ
  becomes
  pLJ85XExZtQ
  """
  return url[slice( url.rindex("/")+1, len(url) )]


def getSongsFromCSV( sourceFiles ):
  output = []
  for file in sourceFiles:
    output += parseTSV( file )

  return output