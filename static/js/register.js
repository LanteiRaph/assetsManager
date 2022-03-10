window.addEventListener("load", () => {
  //Get the usertype option to manage the on change event
  const radio = document.querySelectorAll('input[name="user_type"]');
  //Addd on change event to the radio button
  radio.forEach(radio => {
    radio.addEventListener("change", () => {
        //Get the input with the department id
        const inputDep = document.querySelector("#department");
        if (inputDep.hasAttribute("multiple")) {
          inputDep.removeAttribute("multiple");
        } else {
          inputDep.setAttribute("multiple", "");
        }
  })
  });
  //Create a new Register object to handle the page intractions
  const register = new Register("user_registration");
  //Get the submit button and add an event lister
  document.querySelector("#register_user").addEventListener("click", (e) => {
    e.preventDefault()
    //Register the new
    register
      .save()
      .then((res) => {
            console.log(res)
      })
      .catch((e) => console.log(e));
  });
});
