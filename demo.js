console.log("Hello! Welcome to console");
//document.writeln("We are learning JavaScript");
data=12.35
console.log(typeof data);

employees=[
    { empid:1001, name:"Prachi", age:21 },
    { empid:1002, name:"Yuvraj", age:22 },
    { empid:1003, name:"Satyarth", age:23 },
    { empid:1004, name:"Ananya", age:24 },
    { empid:1005, name:"Satyarth", age:25 }
];
document.writeln("<table border='1'>");
document.writeln("<tr><th>EmpID</th><th>Name</th><th>Age</th></tr>");
for(e of employees){
    console.log(e.empid +"\t"+ e.name +"\t"+ e.age);
    document.writeln("<tr><td>"+e.empid+"</td><td>"+e.name+"</td><td>"+e.age+"</td></tr>");
    
}