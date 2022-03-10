window.addEventListener('load', () => {
    //Create a new server
    const server = new Server()
    //Initialize the application.
    request = new Request(server)
    //Get the elementt to append content to
    const contentElement = document.querySelector('#request-list')
    //Create a new listviewer
    const listView = new ListView(request,contentElement)
    //Show the list
    listView.display()
    //handle the make request function()
    const btnMakeRequest = document.querySelector('#make-request')
    //Add an onclick handler
    btnMakeRequest.addEventListener('click', () => {
        //Call save from the request object
        request.save().then((response) => {
            //Redirect the user to the details page.
            window.location.href = `/assets/request-details/${response.request}`
        });
        //Clear the local stroge
        request.clear_from_local();
    })
    //Edit the current the request qityt value
    document.querySelector('#edit_request_item')
        .addEventListener('click', (e) => {
            request.edit()
        })
    //delete the current select request
    document.querySelector('#delete_request_item')
        .addEventListener('click', () => {
            request.delete()
        })

})






