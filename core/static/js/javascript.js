$(document).ready(function() {
  // Toggle the navigation menu
  $(".navT").on("click", function() {
      $(this).toggleClass("active");
      $("#menu").toggleClass("open");
      $(".content").toggleClass("shift");
  });

  // Get the modal and close elements
  var modal = document.getElementById("result-modal");
  var closeModalBtn = document.getElementsByClassName("close")[0];

  // Close the modal when the user clicks the "x" button
  closeModalBtn.onclick = function() {
      modal.style.display = "none";
  }

  // Close the modal if the user clicks anywhere outside of the modal content
  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
});
