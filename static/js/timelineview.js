function createTimeline(events, eventInterval, scaleInterval) {
    Timeline.CompactEventPainter.prototype._showBubble = function(x, y, events) {
        var event = events[0];
        var type = event.getProperty('type');
        switch (type) {
            case 'youtube':
            var videoUrl = event.getProperty("videoUrl");
            $.fancybox({
                'titleShow'        : false,
                'transitionIn'     : 'elastic',
                'transitionOut'    : 'elastic',
                'href'             : videoUrl + "&fs=1&autoplay=1",
                'type'             : 'swf',
                'swf'              : { 'wmode' : 'transparent' }
            });
            break;

            case 'facebook':
            var url = event.getProperty("url");
            if (url != undefined) {
                $.fancybox({
                    'titleShow'        : false,
                    'transitionIn'     : 'elastic',
                    'transitionOut'    : 'elastic',
                    'type'             : 'iframe',
                    'href'             : url
                    // 'href'             : "http://itc.ua"
                });
                
            } else {
                var text = event.getProperty("text");
                $.fancybox({
                    'titleShow'        : false,
                    'transitionIn'     : 'elastic',
                    'transitionOut'    : 'elastic',
                    'content'          : text
                });
            }
            break;
            
        }
    };
    var now = new Date();
    var fewMonthsAgo = new Date(now.getTime() - 1 * 30 * 24 * 60 * 60 * 1000);
    var eventSource = new Timeline.DefaultEventSource();
    var bandInfos = [
        Timeline.createBandInfo({
            eventSource:    eventSource,
            width:          "90%",
            intervalUnit:   eventInterval,
            intervalPixels: 100,
            showEventText: false,
            eventPainter:   Timeline.CompactEventPainter,
            date: fewMonthsAgo,
            eventPainterParams: {
                iconLabelGap:     5,
                labelRightMargin: 20,
                
                iconWidth:        120, // These are for per-event custom icons
                iconHeight:       90,
                
                stackConcurrentPreciseInstantEvents: {
                    limit: 5,
                    moreMessageTemplate:    "%0 More Events",
                    iconWidth:              120,
                    iconHeight:             90
                }
            }
        }),
        Timeline.createBandInfo({
            width:          "10%",
            intervalUnit:   scaleInterval,
            intervalPixels: 200,
            date: fewMonthsAgo,
            layout: 'overview'
        })
    ];
    bandInfos[1].syncWith = 0;
    bandInfos[1].highlight = true;
    tl = Timeline.create(document.getElementById("my-timeline"), bandInfos);

    var resizeTimerID = null;
    $(window).resize(function() {
        if (resizeTimerID == null) {
            resizeTimerID = window.setTimeout(function() {
                resizeTimerID = null;
                tl.layout();
            }, 500);
        }
    });

    var json = {
        'dateTimeFormat': 'Gregorian',
        'events': events
    };
    eventSource.loadJSON(json, document.location.href);
}
