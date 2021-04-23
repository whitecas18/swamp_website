$(document).ready(function () {
  var input = document.getElementById("cmd")
  var output = document.getElementById("output")

  $("#cmd").on("keyup", function (event) {
    if (event.keyCode === 13) {
      console.log(input.value)
      $("#output").append("<span style='color:#1E9C00;'>You " + input.value + "</span><br>")
      if (output.offsetHeight >= 0.45 * window.innerHeight) {
        $("#output").find("span").first().remove()
        $("#output").find("br").first().remove()
      }
      input.value = ""
    }
  })
})
