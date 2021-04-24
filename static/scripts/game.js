$(document).ready(function () {
  var input = document.getElementById("cmd")
  var output = document.getElementById("output")
  var audio = document.createElement("audio")

  // When the enter key is pressed, text from the command box is sent to the server
  // and printed to the game's output box.
  $("#cmd").on("keyup", function (event) {
    if (event.keyCode === 13) {
      playAudio(0)
      console.log(input.value)
      textBuilder("You " + input.value, "color:#1E9C00;")
      input.value = ""
    }
  })

  // Plays selected audio file
  // OPTIONS: togarbage1 - togarbage6,
  //          leaveend, chocoend, goodend, badend, karlboss
  function playAudio(audName) {
    audio.pause()
    audio.setAttribute("src", "static/audio/" + audName + ".mp3")
    audio.play()
  }

  // Cull oldest entry of output box if max height is exceeded. (accounts for small screens)
  function cullOld() {
    if (window.innerWidth < 700) maxHeight = 0.45
    else maxHeight = 0.6
    if (output.offsetHeight >= maxHeight * window.innerHeight) {
      $("#output").find("span").first().remove()
    }
  }

  // sleepNow enables the "wait" feature between characters
  //
  // textBuilder prints your text to the game's output box. There is a 50ms delay between
  // standard characters and an extra 500 at the end of properly punctuated sentences!
  //
  // @param text  : the text you want to display
  // @param style : the style you want to apply to your text (color, most likely)
  const sleepNow = (delay) => new Promise((resolve) => setTimeout(resolve, delay))
  async function textBuilder(text, style) {
    // A separate <span> exists for each text entry. This aids in culling when screen is full.
    $("#output").append("<span style='" + style + "'>")

    for (let i = 0; i < text.length; i++) {
      // Wait a brief period between letters!
      await sleepNow(50)

      // HTML trims off the spaces, so we need to add them back in like so.
      if (i != 0 && text.charAt(i - 1) == " ") {
        $("#output")
          .find("span")
          .last()
          .append(text.charAt(i - 1) + text.charAt(i))
      } else {
        $("#output").find("span").last().append(text.charAt(i))
      }

      // Waits longer when sentence endings are encountered.
      if (text.charAt(i) == "?" || text.charAt(i) == "." || text.charAt(i) == "!") {
        await sleepNow(500)
      }

      cullOld()
    }
    $("#output").find("span").last().append("&nbsp;</span><br>")
  }

  // Sets initial values for a new game.
  $("#bgarea").css("background-image", "url(static/assets/bg-aus-208.png)")
  playAudio("chocoend")
  startText =
    "You are jolted awake by the feeling of unrest. How long were you asleep? In Front of you is a computer monitor, on but displaying only a blue screen. All the other monitors are in the same state. You realize you’re in Austin 208, but there’s something wrong. Not just with the computer’s, but with the very grounds of campus. The air is tainted, almost palatable in its stench. The windows are almost blocked by overgrown vines and moss, and the sky has turned a permanent gray, the sun nowhere in sight. It’s as if all of ECU campus had become a swamp. Humid, dark, and uninhabited."
  $("#output").append("<span>")
  textBuilder(startText, "")
})
