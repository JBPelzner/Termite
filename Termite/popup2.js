/// This code is from the 'Hello, World' example
$(function(){
    $('#name').keyup(function(){
        $('#example').text('Hello ' + $('#name').val())
    })
})



/// This code is from the 'Budget Manager' example
// use jQuery to listen to the click event on the spend button
// send notifications to the user when they go over their limit

$(function(){

    // load in the variables saved to chrome as the HTML fields in the popup
    chrome.storage.sync.get(['total', 'limit'], function(budget){
        {console.log("testing function one");};
        {console.log(budget);};


        $('#total').text(budget.total);
        $('#limit').text(budget.limit);
    });

    // when user clicks spend button
    // recall total amount from chrome and add new amount
    $('#spendAmount').click(function(){
        {console.log("testing 'Spend' button click functionality");};

        chrome.storage.sync.get(['total', 'limit'], function(budget){
            {console.log("inside the first layer of the storage get function: ", this);};
        
            var newTotal = 0;
            if (budget.total >= 0){
                {console.log(budget.total);};
                newTotal += parseInt(budget.total);
                {console.log("'total' variable retrieved from chrome and set to 'newTotal' ");};
                
                {console.log("html 'amount' id value", $('#amount').val());};
                var amount = $('#amount').val();
                {console.log("js 'amount' variable: ", amount);};
            };

            if (amount){
                {console.log("the user entered an amount to spend");};
                newTotal += parseInt(amount);
            };


            // edit the html page for the respective id's
            $('#total').text(newTotal);
            $('#amount').val('');



            // set chrome-total equal to JS newTotal and see if it exceeds limit
            chrome.storage.sync.set({'total': newTotal}, function() {
                {console.log("js 'newTotal' variable: ", newTotal);};
                {console.log("chrome 'limit' property of the imported object 'budget': ", budget.limit);};


                if (newTotal >= budget.limit){
                    var notifOptions = {
                        type: 'basic',
                        iconUrl: 'icon48.png',  
                        title: 'Limit reached!',
                        message: "Uh oh! Looks like you've reached your limit!"
                    };

                    // use Chrome API to send user a notification
                    // first parameter is notification ID
                    // second parameter is object with options for the notification
                    chrome.notifications.create("limit notif", notifOptions, function() {console.log("successful notification");});
                }
            });

        });
    });
});