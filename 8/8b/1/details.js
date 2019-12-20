window.onload = function(){
  var details = [{
    "name": "Shyam Singh",
    "aadhar": 123456789,
    "labtests": ["Blood Test","BP"]
    },
    {
      "name": "ShyamA",
      "aadhar": 123456789,
      "labtests": ["sUGAR", "hAEMO"]
    }
  ];
  var hospitals= [{
      "name": "Apollo Hospital",
      "location": "Delhi"
    },
    {
      "name": "sINH Hospital",
      "location": "blr"
    }    
  ];

  document.getElementById("hospital1").innerHTML = hospitals[0].name;
  document.getElementById("hospital2").innerHTML = hospitals[1].name;
  document.getElementById("location1").innerHTML = hospitals[0].location;
  document.getElementById("location2").innerHTML = hospitals[1].location;

  var b = document.getElementById("patient");
  b.addEventListener("mouseover",function(e){
    e.target.style.color = "orange";
    document.getElementById("name1").innerHTML = details[0].name;
    document.getElementById("aadhar1").innerHTML = details[0].aadhar;
    document.getElementById("name2").innerHTML = details[1].name;
    document.getElementById("aadhar2").innerHTML = details[1].aadhar;
    var test = "";
    details[0].labtests.forEach(function(a){
      test += a + " ";
    });
    document.getElementById("labtests1").innerHTML = test;

    var test1 = "";
    details[1].labtests.forEach(function (a) {
      test1 += a + " ";
    });
    document.getElementById("labtests2").innerHTML = test1;

  });
};