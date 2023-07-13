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
      
    document.getElementById("websiteName").addEventListener("click", redirectToIndex);
});



  