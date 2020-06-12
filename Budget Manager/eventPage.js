var contextMenuItem = {
    "id": "spendMoney",     
    "title": "SpendMoney",      //what appears on webpage when we right-click
    "contexts": ["selection"]   //where this is supposed to appear -- when user makes a selection
};

// create the actual item in the Context Menu
chrome.contextMenus.create(contextMenuItem);

//function to check to see if a value is an integer value
function isInt(value) {
  return !isNaN(value) &&
          parseInt(Number(value)) == value &&
          !isNaN(parseInt(value, 10));
}

// listen to click event on context menu item
chrome.contextMenus.onClicked.addListener(function (clickData){

    //check to see if user clicked on our menu item and if they are selecting some text
    if (clickData.menuItemId == "spendMoney" && clickData.selectionText){   
        if (isInt(clickData.selectionText)){
            chrome.storage.sync.get(['total', 'limit'], function(budget){
                var newTotal = 0;
                if (budget.total) {
                    newTotal += parseInt(budget.total);
                }

                newTotal += parseInt(clickData.selectionText);
                chrome.storage.sync.set({'total': newTotal}, function (){
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
                        chrome.notifications.create("limit notif", notifOptions, function() {console.log('successful notification');});
                    }
                });
            });
        }
    }
});




// building the badge to auto-populate with value of 'total' variable
// want to display this value in the toolbar as a badge
chrome.storage.onChanged.addListener(function(changes, storageName){
    chrome.browserAction.setBadgeText({"text": changes.total.newValue.toString()})
});
