
function getiMocCoreAPI(siteTagIntegrations, moduleImports, moduleHandlers, eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectorEndpoint) {

    return `
    var data = [${siteTagIntegrations}]

    ${moduleImports}
    
    var handlers = {${moduleHandlers}};

    var eventTrackerEndpoint = '${eventTrackerEndpoint}';
    var botDetectorEndpoint = '${botDetectorEndpoint}';

    var siteId = '${siteId}';

    var eventTrackerLibraryUrl = '${eventTrackerLibraryUrl}';

    // !(function(){
    //     var s = document.createElement("script");
    //     s.src= "https://js-cdn.dynatrace.com/jstag/15a8a271790/bf68836gaj/b8a112ee4a2ee636_complete.js";
    //     s.async = true;
    //     document.head.appendChild(s);
    // })();

    window.moc = window.moc || {};
    moc.push = function(){
        let functionName = arguments[0];
        let functionArgs = arguments[1];
        handlers[functionName](functionArgs);
    }

    data.forEach((integration) => {
        handlers[integration['function']](integration['tag'], eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectorEndpoint);
    });
    `;



}

module.exports = getiMocCoreAPI