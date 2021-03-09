// objects
var employee={
    id:1000,name:"ajay",desig:"dev",salary:30000
}
console.log(employee["name"]);
console.log(employee.name);
console.log("g");

for(let key in employee){
    console.log(key);
}