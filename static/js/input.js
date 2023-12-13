if(localStorage.getItem('-1')===null){
    localStorage.setItem('-1','0');
}




let name=document.getElementById('name');
let rol=document.getElementById('rollno');
let email=document.getElementById('email');
let con=document.getElementById('contact');
let course=document.getElementById('course');
let year=document.getElementById('year');
let but=document.querySelector('.login-box form a');
 
but.addEventListener('click',(event)=>{
    event.preventDefault();
    let val=(localStorage.getItem('-1'));
    console.log(val);
    val = parseInt(val);
    val+=1;
    localStorage.setItem('-1',val);
    const value = JSON.stringify({
        name: name.value,
        rollNumber: rol.value,
        email: email.value,
        con:con.value,
        course:course.value,
        year:year.value
    });
    localStorage.setItem(val,value);
    name.value='';
    rol.value='';
    email.value='';
    con.value='';
    course.value='';
    year.value='';
    alert('student added');
 
});
 
function rem(){
    console.log("111");
    for(let i=-1;i<20;i++){
        let s=`${i}`;
        // if(s==='-1')
        //     localStorage.setItem(s,0);
        // else
            localStorage.removeItem(s);
    }
}
// rem();