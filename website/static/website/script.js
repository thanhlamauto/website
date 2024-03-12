//appear about
document.addEventListener('DOMContentLoaded', function() {
    // Some code here
    function scrollAppear() {
        var introText = document.querySelector('.side-text');
        var sideImage = document.querySelector('.sideImage');
        var introPosition = introText.getBoundingClientRect().top;
        var imagePosition = sideImage.getBoundingClientRect().top;

        var screenPosition = window.innerHeight / 1.2;


        if(introPosition < screenPosition) {
          introText.classList.add('side-text-appear');
        }
        if(imagePosition < screenPosition) {
          sideImage.classList.add('sideImage-appear');
        }
      }

      window.addEventListener('scroll', scrollAppear);
    function redirectToIndex() {
      window.location.href = "index.html";
    }

    function displayGoogleForm() {
      var selectedFormUrl = this.getAttribute('data-formurl');

      if (selectedFormUrl) {
        // Update the formContainer's content with the embedded form
        document.getElementById('formContainer').innerHTML = '<iframe src="' + selectedFormUrl + '" width="840" height="1200" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>';
      } else {
        // If no form is selected, clear the formContainer
        document.getElementById('formContainer').innerHTML = '';
      }
    }

    document.getElementById("websiteName").addEventListener("click", redirectToIndex);
    var dropdownItems = document.getElementsByClassName('dropdown-item');
    for (var i = 0; i < dropdownItems.length; i++) {
      dropdownItems[i].addEventListener('click', displayGoogleForm);
    }
});



