$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
    $('.modal').modal();
})

const deleteConfirm = document.getElementById('delete-confirm-btn');

$('.delete-btn').click((event) => {
    const modal = document.getElementById('delete-modal');
    const instance = M.Modal.init(modal, { dismissible:false });
    instance.open();

    if (event.currentTarget.tagName === "a") {
        deleteConfirm.href = event.currentTarget.href;
    } else {
        deleteConfirm.href = event.currentTarget.href;
    }

    return false;
});