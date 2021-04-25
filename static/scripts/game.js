$(document).ready(function () {
  var input = document.getElementById("cmd")
  var output = document.getElementById("output")
  var audio = document.createElement("audio")
  var gameState = {
    inventory: {
      candyBar: 0,
      ronnieCrystal: 0,
      dingCrystal: 0,
      hogCrystal: 0,
      gopalCrystal: 0,
      wuCrystal: 0,
      hillsCrystal: 0,
    },
    currentLocation: "austinstart",
    currentSong: "startsong",
    outputText:
      "You are jolted awake by the feeling of unrest. How long were you " +
      "asleep? In front of you is a computer monitor, on but displaying " +
      "only a blue screen. All the other monitors are in the same state. " +
      "You realize you are in Austin 208, but there's something wrong. Not " +
      "just with the computers, but with the very grounds of campus. The air is " +
      "tainted, almost palatable in its stench. The windows are almost blocked by " +
      "overgrown vines and moss, and the sky has turned a permanent gray, the sun " +
      "nowhere in sight. It is as if all of the ECU campus had become a swamp. " +
      "Humid, dark, and uninhabited.",
  }
  var locationBG = {
    austin208: "aus-208",
    austinstart: "aus-208",
    austinhall: "aus-hall",
    austinhills: "aus-hills",
    austinclass: "aus-clas",
    libraryentrance: "lb-ent",
    libraryfront: "lb-frnt",
    librarygopal: "lb-gopal",
    librarymaze1: "lb-mz1",
    librarymaze2: "lb-mz2",
    librarymaze3: "lb-mz3",
    libraryshrine: "lb-smth",
    scitechding: "st-ding",
    scitechkarl: "st-karl",
    scitechoffice: "st-off",
    scitechwu: "st-wu",
  }

  // Sets initial values for a new game or a load
  function initGame() {
    console.log(gameState)
    textBuilder(gameState.outputText)
    setBackground(locationBG[gameState.currentLocation])
    playAudio(gameState.currentSong)
  }

  // Retrieves JSON for specified username and updates game state accordingly
  // TODO: update background, play music
  function load(userName) {
    $.ajax({
      type: "GET",
      url: "/load/" + userName,
      complete: function (e) {
        console.log(e)
        gameState = JSON.parse(e.responseText)
        initGame()
      },
    })
  }

  // As it says, this function sends your game state to the server to be saved!
  function save(userName) {
    console.log(gameState)
    $.ajax({
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(gameState),
      dataType: "json",
      url: "/save/" + userName,
      complete: function (e) {
        console.log(e)
        window.alert(e.responseText)
      },
    })
  }

  // Button functions for html
  $(back).on("click", function () {
    window.location.href = "/"
  })
  $(saveSend).on("click", function () {
    if (userNameInput.value == "") window.alert("Name cannot be blank!")
    else {
      tmpString = $("#output").find("span").last()[0].outerText
      gameState.outputText = tmpString.substring(0, tmpString.length - 2)
      save($("#userNameInput").val())
    }
  })

  // When the enter key is pressed, text from the command box is sent to the server
  // and printed to the game's output box.
  $("#cmd").on("keyup", function (event) {
    if (event.keyCode === 13 && input.value != "") {
      console.log(input.value)
      textBuilder("You " + input.value, "color:#1E9C00;")
      input.value = ""
    }
  })

  // Plays selected audio file
  // OPTIONS: togarbage1 - togarbage6, leaveend, chocoend,
  //          goodend, badend, karlboss, overworld, startsong
  function playAudio(audName) {
    audio.pause()
    audio.setAttribute("src", "../static/audio/" + audName + ".mp3")
    audio.play()
  }

  // Sets background image
  // OPTIONS: aus-208, aus-clas, aus-hall, aus-hills, cty
  //          lb-ent, lb-frnt, lb-gopal, lb-mz1 - lb-mz3,
  //          lb-smth, st-ding, st-karl, st-off, st-wu
  function setBackground(bgName) {
    $("#bgarea").css("background-image", "url(../static/assets/bg-" + bgName + ".png)")
    console.log(bgName)
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
      await sleepNow(40)

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
        await sleepNow(400)
      }

      cullOld()
    }
    $("#output").find("span").last().append("&nbsp;</span><br>")
  }

  // If username is present, load game data. Else, init as new game.
  if ($("#loadHolder").text().length > 0) {
    load($("#loadHolder").text())
    console.log($("#loadHolder").text())
  } else {
    initGame()
  }
})
