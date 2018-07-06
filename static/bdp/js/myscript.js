  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyAcGLQyvbnBxz8yOUr9DhznW86nJ10nbEo",
    authDomain: "blooddonation-a2c51.firebaseapp.com",
    databaseURL: "https://blooddonation-a2c51.firebaseio.com",
    projectId: "blooddonation-a2c51",
    storageBucket: "blooddonation-a2c51.appspot.com",
    messagingSenderId: "1045257882687"
  };
firebase.initializeApp(config);
var firestore = firebase.firestore();
const docRef = firestore.doc("sample/sandwichdata");


const output = document.querySelector("#output");
const textf = document.querySelector("#text");
const saveb = document.querySelector("#save");

saveButton.addEventListener("click", function(){
  const texttosave = inputTextField.value;
  console.log("Saved "+texttosave);
  docRef.set({
    status:texttosave
  }).then(function(){
    console.log("Status saved");
  }).catch(function(error){
    console.log("Error:"+ error);
  });
})
