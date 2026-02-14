dataInput=document.getElementById("dataInput").value;
cityArr=["New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Antonio","San Diego","Dallas","San Jose","Austin","Jacksonville","Fort Worth","Columbus","Charlotte","San Francisco","Indianapolis","Seattle","Denver","Washington D.C.","Boston","El Paso","Nashville","Detroit","Oklahoma City","Portland","Las Vegas","Memphis","Louisville","Baltimore","Milwaukee"]
function filterCityArr(dataInput){
    const filterCity=cityArr.filter((city)=>city.toLowerCase().startsWith(dataInput.toLowerCase()));
    myData="";
    filterCity.forEach((city)=>{
        myData+="<li>"+city+"</li>";
    });
    document.getElementById("result").innerHTML=myData;
}