let phone_number_input=$('#phone-number')
let user_text=$('#user-text')

$('#phone-number-form').on('submit',function(event){
    event.preventDefault()
    $.ajax({
        url:"/find-number/find-number-api/",
        type:'POST',
        data:{
            'mobile_number':phone_number_input.val(),
        },
        success:function(data){
            console.log("success",data)
            let tbody=$('.phone-number-details tbody')
            tbody.find('.country-code').text(data.country_code)
            tbody.find('.mobile-number').text(data.mobile_number)
            tbody.find('.country').text(data.country)
            tbody.find('.service-provider').text(data.service_provider)
            tbody.find('.timezone').text(data.timezone)

        },
        error:function(data){
            console.log("error",data)
        }
    })
})

$('#find-phone-numbers-form').on('submit',function(event){
    event.preventDefault()
    $.ajax({
        url:"/find-number/find-number-in-text-api/",
        type:"POST",
        data:{
            'find_number':user_text.val(),
        },
        success:function(data){
            console.log('Success',data)
            let tbody=$('.find-number-details-table tbody')

            tbody.empty()
            $.each(data.mobile_numbers, function(index, number) {
                tbody.append(
                    `<tr>
                        <td>${index + 1}</td>
                        <td>${number}</td>
                    </tr>`
                );
            });

        },
        error:function(data){
            console.log('error',data)
        }
    })  
})