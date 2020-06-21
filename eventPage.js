/// This code is from the Budget Manager extension



/// I think one possible functionality of the Context Menu is as follows:
    /// the 'contexts' property can remain 'selection' 
    /// --> the user could highlight a policy link that they want to analyze
var analyzeTextItem = {
    "id": "analyzeText",     
    "title": "Analyze Text",      //what appears on webpage when we right-click
    "contexts": ["selection"]   //where this is supposed to appear -- when user makes a selection
};

var addToLogItem = {
    "id": "agreementLog",     
    "title": "Add Website to Agreement Log",      //what appears on webpage when we right-click
    // "contexts": ["selection"]   //where this is supposed to appear -- when user makes a selection
};

// create the actual item in the Context Menu
chrome.contextMenus.create(analyzeTextItem);
chrome.contextMenus.create(addToLogItem);


/// First build out the ANALYZE TEXT ITEM
    // Maybe change this diagnostic function to evaluate whether the link/selected item is actual a policy



// listen to click event on context menu item
chrome.contextMenus.onClicked.addListener(function (clickData){

    //check to see if user clicked on our menu item and if they are selecting something appropriate
    if (clickData.menuItemId == "analyzeText" && clickData.selectionText){   

        if (isInt(clickData.selectionText)){
         // if (//*criteria function*//(clickData.selectionText)){
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
                        // third parameter is callback function
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
