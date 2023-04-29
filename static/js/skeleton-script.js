function dropdownMenu() {
    document.getElementById("dropdownContent").classList.toggle("show");
}

window.onclick = function( e ) {
    if ( !e.target.matches('.dropdownButton') ) {
      var myDropdown = document.getElementById("dropdownContent");
      if (myDropdown.classList.contains('show')) {
          myDropdown.classList.remove('show');
      }
    }
}