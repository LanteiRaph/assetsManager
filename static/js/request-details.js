window.addEventListener('load', () => {
    alert('yooh')
    //Create a new server
    const server = new Server()
    //Create a new request
    const request = new Request(server)
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
    document.querySelector('#return_items', () => {
        alert('hello world')
    })
})