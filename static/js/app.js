
//Declare global variables
var modal, request;
//Represets server http method calls: For reuseability
class Server {
  //Int the server class
  constructor() {
    //Create the header section tot send to the server.(csrftoken is nned to validate the user)
    const csrftoken = Cookies.get("csrftoken");
    this.headers = new Headers();
    this.headers.append("X-CSRFToken", csrftoken);
    this.headers.append("Content-Type", "application/json");
  }

  //Get the givan url
  async get(url) {
    //Fetc the data from the server.
    const responce = await fetch(url);
    //Return thefetch data to the server.
    return responce;
  }

  async post(url, payload) {
    //Compile the requst object
    const request = {
      method: "POST", // or 'PUT'
      headers: this.headers,
      body: payload,
    };
    //Send the data to the server.
    const response = await fetch(url, request);
    //Return the responce
    return response;
  }

  async put(url, payload) {
      //Compile te request object
      const request = {
        method: 'PUT',
        header: this.Headers,
        body: payload
      }
      //make arequest to the server.
      const response = await fetch(url, request)
      //Responded back with the data.
      return response
  }
  async delete(url) {
    //Compile te request object
    const request = {
      method: 'DELETE',
      header: this.Headers
    }
    //make arequest to the server.
    const response = await fetch(url, request)
    //Responded back with the data.
    return response
}
}
//Declare the request class to ahandle all the request amanage to the server
//A request has One or more equipment where each equipment has a condition which is a string
//Save the data to the local storage,
//Retrive from local stroage
class Request {
  //Init the object: Check if any reaust_list are availabe from local storege
  constructor() {
    //Save the server to make reequest to
    this.server = new Server();
    //Get from local storege
    const list = this.retrive_from_local();
    //Init the reuqest list to an empty list
    this.List = list ? list : [];
    //Ini the current equipment
    this.current_equipment = {};
  }

  //Make  Request: Ie get the infomation of the current clickedd item
  make(element) {
    //Create a new poppu
    this.popup = new Popup("", this);
    //Open the popup
    this.popup.open_popup(element);
  }

  //Close the popup window: Checkout of it.
  check_out() {
    //Close the popup
    this.popup.close_popup();
  }

  //Send request to server to server.
  async save() {
    //Collect all request
    const requestData = JSON.stringify(this.List);
    //Config the header for a complete reeust to a djago URL
    //Save the request to the server(Post request)
    const result = await this.server.post(
      "http://127.0.0.1:8000/assets/request-list/",
      requestData
    );
    //Return a json object to populate the page.
    return result.json();
  }

  //Edit the request object matching the id given
  //The only field that can be update is either the Qty
  async edit(element){
    alert('Ready to edit')
    //Get the id from he granpparent
    const id = element.parentNode.parentNode.id
    //Get the payload to update the server.
    const payload = {

    }
    //Request the servere for an update
    const result = await this.server.put(`http://127.0.0.1:8000/assets/request-list/${id}`, payload)
    //Outpu the result.
    return result.json()
  }

  //Delete an item from the list
  async delete(element){
    //Get the id from he granpparent
    const id = element.parentNode.parentNode.id
    //Request the servere for an update
    const result = await this.server.delete(`http://127.0.0.1:8000/assets/request-list/${id}`, payload)
    //Output the result.
    return result.json()
  }

  //On success save to locall storeage
  save_to_local() {
    //Get the current version of the reust list and save it tot eh local storage
    localStorage.setItem("request-list", JSON.stringify(this.List));
  }

  //Returns a list of all current request list from the local storegae
  retrive_from_local() {
    //Set the reueslt list to what it is in the local storage
    return JSON.parse(localStorage.getItem("request-list"));
  }

  //Clear the local storege
  clear_from_local() {
    //Clear the local storeage
    localStorage.removeItem("request-list");
  }
  //Get the  contect of the current equipement:{equipment, condition, Qty}
  collect_equipment(event) {
    //Get the qty input
    const input = document.querySelector("#qty");
    //Get the Qty input a find its value
    const qty = input.value;
    //Set the qty value for the equipment
    this.current_equipment.qty = qty;
    //push the equipment to the the reqiest list
    this.List.push(this.current_equipment);
    //Save the list to the local storage
    this.save_to_local();
    //Close the pop up window.
    this.popup.close_popup();
    //Update the value of the
    this.show_requestCount();
    //Reqfresh the current _equipement
    this.current_equipment = {};
    //Prevent the dafaulet from happenning
    event.preventDefault();
    //Clsoe the pop up window
  }

  //Retuena  boolean atribute true if exit false if not.
  item_in_list(id) {
    //Check if the id exist with the array.
    const equipment = this.List.find((element) => element.Id == id);
    if (equipment) {
      return true;
    } else {
      return false;
    }
  }

  get requestCount() {
    //return the requestlist length
    return this.List.length;
  }

  show_requestCount() {
    //Get the elemnt to show on the dom
    const count = document.querySelector("#requestCount");
    //append the value of the request length
    count.textContent = this.requestCount;
  }

  //Increase the quantity of the current equipment
  increase_current_qty() {
    //Get the new value from the input
    //Compire if they are the same
    //If not update the value
    //Find the object with match propty id ad the given id
    //Update the qty propety to the new value
  }
}

class ListView {
  constructor(module, HTMLElement) {
    //Set the modle to get the data from
    this.module = module;
    //Element to append the list
    this.element = HTMLElement;
  }

  //Show all requested equipments
  display() {
    //Get the list from the local storage
    const listcontent = this.module.List;
    //Check for the length if grater than one dislay if less show a emepty div
    if (listcontent.length >= 1) {
      //Create the list view from the data in the model list
      this.create_list_view();
      //document.querySelector('#no-current').style.display  = 'none'
    } else {
      //Get the no-current id tag
      document.querySelector("#no-current").style.display = "block";
      //Unshow the request list
      document.querySelector("#current-request").style.display = "none";
    }
  }
  //Create the list view, its a table formed from the data given
  create_list_view() {
    //Create the table element
    const table = document.querySelector("table");
    //Create the header section
    this.create_header(table);
    //Create Body
    this.create_body(table);
  }

  //Create the table headed..
  create_header(table) {
    //Create the tabtel head raw
    let thead = table.createTHead();
    let row = thead.insertRow();
    //Extract the keys rom the objects
    const keys = Object.keys(this.module.List[0]);
    //Step throught the data object and create a th for each
    for (let key of keys) {
      let th = document.createElement("th");
      let text = document.createTextNode(key);
      th.appendChild(text);
      row.appendChild(th);
    }
  }

  //Create the body of the table
  create_body(table) {
    //Step through the recrd sand create a row for each.
    for (let element of this.module.List) {
      //Create a row
      let row = table.insertRow();
      //Get the values
      const values = Object.values(element);
      for (let key of values) {
        let cell = row.insertCell();
        let text = document.createTextNode(key);
        cell.appendChild(text);
      }
      //Create the delete button
      const cell = row.insertCell()
      const deleteTxt = document.createElement('button')
      deleteTxt.textContent = 'Delete'
      cell.appendChild(deleteTxt)

    }
  }
}

//Activate a popup window by the given id
class Popup {
  //Init the class with an ID
  constructor(id, contoller) {
    //Save the Id
    this.id = id;
    //Save the controller: Responsible for handling any data related chekcs and savings.
    this.controller = contoller;
  }

  //Open pop up window to collect additon value from the user
  open_popup(element) {
    //Get the id of the click equipment
    const Id = element.parentNode.parentNode.id;
    //Show the model to collect the data from the user
    modal.style.display = "block";
    //Before openeing the pop up check if item already exists
    if (this.controller.item_in_list(Id)) {
      //Item available it list prompt to increase or exit request.
      //Open the alert modal to confrim
      document.querySelector("#confirm").style.display = "block";
    } else {
      //From the element grandparaent get the equipment id
      this.controller.current_equipment.Id = Id;
      //Set the name of the make of the model
      this.controller.current_equipment.make =
        element.parentNode.parentNode.childNodes[1].textContent;
      //Show the collection infomation
      document.querySelector("#collect").style.display = "block";
    }
  }
  //Close the pop up window
  close_popup() {
    //Set the modal to display none
    modal.style.display = "none";
    //Set its children to display none untill being accessed
    document
      .querySelectorAll(".modal-content")
      .forEach((el) => (el.style.display = "none"));
  }
}


class Register{
  //Init a register: Params form id: form to collect data from
  constructor(form_id){
    this.form_id= form_id
    //Create a new server: For request
    this.server = new Server()
  }
  //Register a user
  async save(){
    // //Collect all data from the user.
    const paylaod = this.collect_values()
    const data =JSON.stringify(Object.fromEntries(paylaod));
    //request the server for a create request
    const response = await this.server.post('/onboarding/register-user/', data)
    //Responde back to the user
    return response.json()
  }
  //Get all the departments availale from the db and add to the ui
  fetch_support(table){
    //Make a request to he server to get all availble
    //Add to the interface.
  }
  //Collect the values of the given form id
  collect_values(){
    //Get the form by id
    const myForm = document.getElementById(this.form_id);
    //Create new form
    const formData = new FormData(myForm);
    //return the created form
    return formData
  }
}
