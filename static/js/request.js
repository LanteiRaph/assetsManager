window.addEventListener("load", () => {

    const server = new Server()
    //Create a new Request Object
    request = new Request(server);

    //Set the modal to manu[ilate
    modal = document.getElementById("modalContainer");

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
           request.popup.close_popup()
        }
    };

    //Clsoe the pop up modal
    var span = document.querySelector(".close");
    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        request.popup.close_popup()
    };
    //
    //Get the confim and rejet buttons for the modals
    document.querySelector('#yes').addEventListener('click', () => {
        //User wants to increase qty
        request.increase_current_qty()
    })
    //
    document.querySelector('#no').addEventListener('click', () => {
        //Close the popup
        request.popup.close_popup()
    })
    //Show the request list count if any is available
    request.show_requestCount();
});
