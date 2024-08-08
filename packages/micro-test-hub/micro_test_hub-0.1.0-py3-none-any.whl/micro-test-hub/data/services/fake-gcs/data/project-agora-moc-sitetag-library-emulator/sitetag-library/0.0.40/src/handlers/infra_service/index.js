function serveDynatrace(text){
    var tagString = decodeURIComponent(text);
    try{
        var dom = new DOMParser().parseFromString(tagString, "text/html");
        var incomingScript = dom.getElementsByTagName("script")[0];
        var incomingAttributes = incomingScript.attributes;
        var head = document.getElementsByTagName("head")[0];
        var script = document.createElement("script");
        for (const attr of incomingAttributes) {
            script.setAttribute(attr["name"], attr["value"]);
        }
        head.appendChild(script);
    } catch (error){
        console.error(`Could not serve tag: ${tagString}`);
        console.error(error);
    }
}

function serveEventTracker(eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectionEndpoint){
    var paAnalytics = paAnalytics || [];

    var loadScript = function(url, onLoad){
        var script = document.createElement('script');
        script.setAttribute('src', url);
        script.async = true;
        script.onload = onLoad;
        var target = document.getElementsByTagName('head')[0];
        target.insertBefore(script, target.firstChild);
        script.onerror = function (error) {
            paAnalytics.push([
                'track',
                {eventName: 'MocSiteTagError', properties: {errCode: 2}}
            ]);
        };
    };

    // Init Event Tracker
    paAnalytics.push([
    'init',
    {
        EVENT_TRACKER_ENDPOINT: decodeURIComponent(eventTrackerEndpoint),
        BD_ENDPOINT: decodeURIComponent(botDetectionEndpoint),
        shared: {
            site_id: siteId,
        }
    }
    ]);

    // Track site pageview 
    loadScript(
        decodeURIComponent(eventTrackerLibraryUrl),
        function () {
            if (typeof paAnalytics !== 'undefined') {
                var temp = paAnalytics.slice();
                paAnalytics = analytics.paAnalytics;
                paAnalytics.push.apply(paAnalytics, temp);
            } else {
                paAnalytics = analytics.paAnalytics;
            }
        }
    );
}

function serve_infra_service(text, eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectionEndpoint){

    if (document.readyState === "interactive" || document.readyState === "complete"){
        // serveDynatrace(text)
        serveEventTracker(eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectionEndpoint)
    }else{
        document.addEventListener("DOMContentLoaded", function(){
            // serveDynatrace(text)
            serveEventTracker(eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectionEndpoint)
        });
    }
}

export function run(text, eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectionEndpoint = ''){
    serve_infra_service(text, eventTrackerEndpoint, eventTrackerLibraryUrl, siteId, botDetectionEndpoint);
}