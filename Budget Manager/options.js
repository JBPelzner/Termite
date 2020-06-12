// use jQuery to listen to save a limit value to 'limit' variable
// and to reset value of 'total' variable


$(function(){

    chrome.storage.sync.get('limit', function(budget){
        $('#limit').val(budget.limit);
    });

    $('#saveLimit').click(function(){
        var limit = $('#limit').val()
        if (limit){
            chrome.storage.sync.set({'limit': limit}, function(){
                close();
            });
        };
    });

    $('#resetTotal').click(function(){
        chrome.storage.sync.set({'total': 0}, function(){
            var notifOptions = {
                        type: 'basic',
                        iconUrl: 'icon48.png',
                        title: 'Total reset!',
                        message: "Total has been reset to 0!"
                    };
            chrome.notifications.create("reset notif", notifOptions, function (){console.log('successful notification: ', notifOptions.title);});
            chrome.notifications.getAll(function (notifications){console.log("all notification ID's returned: ", notifications);})
        });
    });
});