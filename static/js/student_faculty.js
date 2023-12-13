let idd=0;


function search() {
    var input = document.querySelector("#search").value.toUpperCase();
    
    var students = document.getElementsByClassName("flex-item");
    for (var i = 0; i < students.length; i++) {
      var name = students[i].textContent.toUpperCase();
      if (name.indexOf(input) !== -1 && input!== ""  ) {
        if(idd===0){
          // students[i].scrollIntoView({ behavior: 'smooth' });
          const viewportHeight = window.innerHeight;

          const elementHeight = students[i].offsetHeight;

          const scrollPosition = students[i].offsetTop - (viewportHeight / 2) + (elementHeight / 2);

          window.scrollTo({ top: scrollPosition, behavior: 'smooth' });
          idd=1;
        }
        students[i].style.backgroundColor = "black";
        students[i].style.boxShadow = '0 0 75px #b4e8ff, 0 0 60px #8bcec2';

      } else {
        students[i].style.backgroundColor = "";
        students[i].style.boxShadow = 'none';
      }
   
    }
    idd=1;
  }
  
  var button = document.querySelector(".search-button");
  button.addEventListener("click", function() {
    idd=0;
    search();
  });
document.querySelector("#search").addEventListener('keydown',(event)=>{
  if (event.key === 'Enter') {
    idd=0;
    search();
  }
})

  setInterval(function() {
    search();
  }, 500); 
  
  // const searchInput = document.querySelector('.input');
  // const searchValue = searchInput.value;
  // searchInput.addEventListener('blur', () => {
  //   if (searchInput.value === '') {
  //     searchInput.value = searchValue;
  //   }
  // });
  
  
let lit=[];
function load(){
    let n=localStorage.getItem('-1');
    
    for(let i=1;i<=n;i++){
        const data = localStorage.getItem(i);
        const user = JSON.parse(data);
        if(user==null)
          continue;
        obj={name:user.name, rol:user.rollNumber, email:user.email,con:user.con,course:user.course,year:user.year,key:i}
        lit.push(obj);
    }
        
    lit.sort(function(a, b) {
      let nameA = a.name.toUpperCase(); 
      let nameB = b.name.toUpperCase(); 
      if (nameA < nameB) {
        return -1;
      }
      if (nameA > nameB) {
        return 1;
      }
      
      return 0;
    });

    let content=document.getElementById('students-container');
    for(let i=0;i<lit.length;i++){
      content.innerHTML+=`<div class="flex-item">
          <h2>${lit[i].name}</h2>
          <h3>Roll No: ${lit[i].rol}</h3>
          <h3>email: ${lit[i].email}</h3>
          <h3>contact: ${lit[i].con}</h3>
          <h3>course: ${lit[i].course}</h3>
          <h3>year: ${lit[i].year}</h3>
          <div style="width:30px;height: 30px;">
            <button class='remove' style="display:block;" value=${lit[i].key}>
              <img style="width:30px" src="../static/images/delete-removebg-preview.png">
            </button>
          </div>
        </div>`
    }
}

load();

rem=document.querySelectorAll('.remove');
for(let i=0;i<rem.length;i++){
  rem[i].addEventListener('click',()=>{
      localStorage.removeItem(rem[i].value);
      location.reload();
  });
}
