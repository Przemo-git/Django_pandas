// $(document).ready(function (){
//     $('.ui.dropdown')
//         .dropdown()
// });


// https://semantic-ui.com/modules/dropdown.html#/usage
// $(document).ready(function () {
//     $('.ui.dropdown')
//         .dropdown()
//
//     $('.message .close')
//         .on('click', function () {
//             $(this)
//                 .closest('.message')
//                 .transition('fade')
//             ;
//         })
//     ;$('#modal-btn').click(function () {
//         $('.ui.modal')
//             .modal('show')
//         ;
//     })
//     ;
// })

$(document).ready(function (){
    $('.ui.dropdown').dropdown()
    $('.ui .close').click(function (){       ////
        $('.message').transition('fade')
    })
    $('#modal-btn').click(function (){
        $('.ui.modal').modal('show')
    })
})




