
const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

      
var v=document.getElementsByClassName("btn")
for(i=0;i<v.length;i++){
  v[i].addEventListener('click',function(){
    var btnid=this.dataset.btnid
    

    console.log('btnid:' ,btnid)
  })}
