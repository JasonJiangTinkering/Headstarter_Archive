import React, { useRef, useEffect, useState } from 'react'
function Header({ title }) {
  return <h1>{title ? title : 'Default title'}</h1>;
}

const HomePage = () => {
  const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];
  const [likes, setLikes] = useState(0);

  function handleClick() {
    setLikes(likes + 1);
  }
function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}
const ref = useRef(null);
useEffect(() => {
    const handleKeyUp = event => {
        myFunction();
    }
})

const element = ref.current;
element.addEventListener('click', handleClick);

  return (
    <div>
      <Header title="Develop. Preview. Ship. 🚀" />
      <link rel="stylesheet" href=" %PUBLIC_URL%/index.css" />
      <ul>
        {names.map((name) => (
          <li key={name}>{name}</li>
        ))}
      </ul>
      <button onClick={handleClick}>Like ({likes})</button>

      <input type="text" ref={ref} id="myInput" placeholder="Search for names.."/>
        

        <ul id="myUL">
        <li><a href="#">Adele</a></li>
        <li><a href="#">Agnes</a></li>

        <li><a href="#">Billy</a></li>
        <li><a href="#">Bob</a></li>

        <li><a href="#">Calvin</a></li>
        <li><a href="#">Christina</a></li>
        <li><a href="#">Cindy</a></li>
        </ul>
        <style>
            
        </style>
    </div>
  );
}
export default HomePage