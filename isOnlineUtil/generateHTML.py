
FORMER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Broken Songs</title>
</head>
<body cz-shortcut-listen="true">
  <style>
    * 
    {
      color: #fff;
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body
    {
      background-color: #212121;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    ul
    {
      font-family: consolas, monotype;
      font-size: 1.5rem;
      list-style-type: none;
      outline: #fff 1px solid;
      width: 40vw;
      height: 50vh;
      overflow-y: scroll;
    }
    li
    {
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      width: 100%;
      height: 2rem;
      outline: #424242 1px solid;
      position: relative;
    }
    li>p
    {
      color: #ffffff44;
      position: absolute;
      top: 0;
      left: 1rem;
    }
    li:active
    {
      color: rgb(255, 237, 74);
    }
    label
    {
      width: 100%;
      cursor: pointer;
    }
    #copyText, #numberChecked
    {
      font-size: 2rem;
      font-family: "consolas", monospace;
      padding: 1rem 0;
    }
    i {
      color: #ffffff44;
    }
    input[type=checkbox] {
      transform: scale(2);
      display: none;
    }  
    input[type=checkbox]:checked + .rightClickToCopy {
      background-color: #111;
      color: #646464;
    }


  </style>

<main>
  <p id="copyText">Broken Links</p>
  <ul>
"""
LATTER = """</ul>
<p id="numberChecked"></p>

</main>

<script>
  var TOTAL = 0
  
  Array.from( document.getElementsByClassName( "rightClickToCopy" ) ).forEach( ( el ) => {
    el.addEventListener( "click", (ev) => {
      navigator.clipboard.writeText( ev.target.innerText );
      id = ev.target.innerText.slice( ev.target.innerText.lastIndexOf( "/" ) +1 )

      document.getElementById( "copyText" ).innerHTML = 
        `<i>Copied</i> ${id} <i>on line: ${ev.target.nextElementSibling.innerText}</i>`

      if ( !ev.target.previousElementSibling.checked )
      {
        TOTAL++
      }
      else
      {
        TOTAL--
      }
      getNumberChecked()
      
    } )
  } )

  function getNumberChecked()
  {
    let total = document.getElementsByTagName( "li" ).length

    document.getElementById( "numberChecked" ).innerText =
      `Total Checked: ${TOTAL} / ${total}`
  }

  getNumberChecked()
</script>

</body>
</html>
"""

LINE = 1

def generateListItem( song ):
  return f"""
  <li>
    <input type="checkbox" id="{song.index}">
    <label for="{song.index}" class="rightClickToCopy"> {song.url} </label>
    <p>{LINE}</p>
  </li>
  """

def generateHTML( songs ):
  global LINE

  html = ""
  html += FORMER
  for song in songs:
    html += generateListItem( song )
    LINE += 1

  html += LATTER

  writeHTMLToFile( html )

def writeHTMLToFile( html ):
  with open( "index.html", "w" ) as file:
    file.write( html )
  