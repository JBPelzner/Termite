// use jQuery to listen to the click event on the spend button
// send notifications to the user when they go over their limit


$(function(){

    // load in the variables saved to chrome as the HTML fields in the popup
    chrome.storage.sync.get(['total', 'limit'], function(budget){
        $('#total').text(budget.total);
        $('#limit').text(budget.limit);
    })

    // when user clicks spend button
    // recall total amount from chrome and add new amount
    $('#spendAmount').click(function(){
        chrome.storage.sync.get('total', function(budget){
            var newTotal = 0;
            if (budget.total){
                newTotal += parseInt(budget.total);
            }

            var amount = $('#amount').val();
            if (amount){
                newTotal += parseInt(amount);
            }

            // set chrome-total equal to JS newTotal and see if it exceeds limit
            chrome.storage.sync.set({'total': newTotal}, function(){
                if (amount && newTotal >= budget.limit){
                    var notifOptions = {
                        type: 'basic',
                        iconUrl: 'icon48.png',
                        title: 'Limit reached!',
                        message: "Uh oh! Looks like you've reached your limit!"
                    };

                    // use Chrome API to send user a notification
                    // first parameter is notification ID
                    // second parameter is object with options for the notification
                    chrome.notifications.create('limitNotif', notifOptions);
                }
            });

            $('#total').text(newTotal);
            $('#amount').val('');

        });
    });
});