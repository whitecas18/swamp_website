$(document).ready(function () {
  var input = document.getElementById("cmd")
  var output = document.getElementById("output")
  var audio = document.createElement("audio")
  var gameState = {
    inventory: {
      "Chocolate Bar": 0,
      "Ronnie's Insight": 0,
      "Ding's Database": 0,
      "Hoggard's Syntax": 0,
      "Gopal's Proof": 0,
      "Wu's Library": 0,
      "Hills' API": 0,
    },
    currentLocation: "austin208",
    currentSong: "startsong",
    lastCommand: "",
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

  var typing = false
  var allowAudio = false
  var firstplay = false

  var locationBG = {
    austin208: "aus-208",
    austin: "aus-hall",
    hills: "aus-hills",
    hoggard: "aus-clas",
    libraryent: "lb-ent",
    library: "lb-frnt",
    gopal: "lb-gopal",
    entrymaze: "lb-mz1",
    maze1: "lb-mz2",
    maze2: "lb-mz3",
    maze3: "lb-mz1",
    maze4: "lb-mz2",
    maze5: "lb-mz3",
    maze6: "lb-mz1",
    maze7: "lb-mz2",
    maze8: "lb-mz3",
    maze9: "lb-mz1",
    maze10: "lb-mz2",
    maze11: "lb-mz3",
    maze12: "lb-mz1",
    ronnie: "lb-smth",
    ding: "st-ding",
    karl: "st-karl",
    scitech: "st-off",
    wu: "st-wu",
    courtyard: "cty",
    chocoend: "choco",
    leaveend: "leaveend",
    badend: "badend",
    goodend: "goodend",
  }
  var locationMusic = {
    austin208: "startsong",
    austin: "overworld",
    hills: "overworld",
    hoggard: "overworld",
    libraryent: "overworld",
    library: "overworld",
    gopal: "togarbage6",
    entrymaze: "togarbage1",
    maze1: "togarbage1",
    maze2: "togarbage1",
    maze3: "togarbage2",
    maze4: "togarbage2",
    maze5: "togarbage2",
    maze6: "togarbage3",
    maze7: "togarbage1",
    maze8: "togarbage3",
    maze9: "togarbage3",
    maze10: "togarbage2",
    maze11: "togarbage4",
    maze12: "togarbage5",
    ronnie: "shrine",
    ding: "overworld",
    karl: "karlboss",
    scitech: "overworld",
    wu: "overworld",
    courtyard: "overworld",
    chocoend: "chocoend",
    badend: "badend",
    goodend: "goodend",
    leaveend: "leaveend",
  }

  // Sets initial values for a new game or a load
  function initGame() {
    console.log(gameState)
    textBuilder(gameState.outputText)
    setBackground()
    audio.volume = 0.2
    console.log(audio.getAttribute("src"))
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
  $("#cmd").on("keyup", async function (event) {
    if (event.keyCode === 13 && input.value != "" && typing == false) {
      console.log(input.value)
      gameState.lastCommand = input.value
      $.ajax({
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(gameState),
        dataType: "json",
        url: "/game/command",
        complete: function (e) {
          console.log(e)
          gameState = JSON.parse(e.responseText)
          $.when(textBuilder("You " + input.value, "color:#1E9C00;")).done(function () {
            textBuilder(gameState.outputText)
            if (allowAudio == true) playAudio()
            setBackground
          })
          input.value = ""
        },
      })
    }
  })

  // Loops all music, but not "TOGARBAGE" sound effects
  audio.addEventListener("ended", function () {
    if (audio.getAttribute("src").substring(16, 18) != "to") {
      console.log("loopen")
      this.currentTime = 0
      this.play()
    }
  })

  // Audio must be enabled by the user before playback begins!
  $("#audiopress").on("click touchstart", function () {
    audio.muted = false
    allowAudio = true
    playAudio()
  })

  // Plays selected audio file
  // OPTIONS: togarbage1 - togarbage6, leaveend, chocoend, shrine
  //          goodend, badend, karlboss, overworld, startsong
  function playAudio() {
    if (locationMusic[gameState.currentLocation] != gameState.currentSong || firstplay == false) {
      audio.pause()
      audio.setAttribute("src", "../static/audio/" + locationMusic[gameState.currentLocation] + ".ogg")
      gameState.currentSong = locationMusic[gameState.currentLocation]
      audio.play()
      firstplay = true
    }
  }

  // Sets background image
  // OPTIONS: aus-208, aus-clas, aus-hall, aus-hills, cty
  //          lb-ent, lb-frnt, lb-gopal, lb-mz1 - lb-mz3,
  //          lb-smth, st-ding, st-karl, st-off, st-wu
  function setBackground() {
    $("#bgarea").css("background-image", "url(../static/assets/bg-" + locationBG[gameState.currentLocation] + ".png)")
    console.log()
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
    typing = true
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
    typing = false
  }

  // If username is present, load game data. Else, init as new game.
  if ($("#loadHolder").text().length > 0) {
    load($("#loadHolder").text())
    console.log($("#loadHolder").text())
  } else {
    initGame()
  }
})
