function createTimeline(events) {
    Timeline.CompactEventPainter.prototype._showBubble = function(x, y, evt) {
        // do not show bubble
    };
    var eventSource = new Timeline.DefaultEventSource();
    var bandInfos = [
        Timeline.createBandInfo({
            eventSource:    eventSource,
            width:          "90%",
            intervalUnit:   Timeline.DateTime.MONTH,
            intervalPixels: 100,
            showEventText: false,
            eventPainter:   Timeline.CompactEventPainter,
            eventPainterParams: {
                iconLabelGap:     5,
                labelRightMargin: 20,
                
                iconWidth:        120, // These are for per-event custom icons
                iconHeight:       90,
                
                stackConcurrentPreciseInstantEvents: {
                    limit: 5,
                    moreMessageTemplate:    "%0 More Events",
                    icon:                   "no-image-80.png", // default icon in stacks
                    iconWidth:              120,
                    iconHeight:             90
                }
            }
        }),
        Timeline.createBandInfo({
            width:          "10%",
            intervalUnit:   Timeline.DateTime.YEAR,
            intervalPixels: 200
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
    $('.timeline-event-icon').addClass('video-event');
    // $('.timeline-event-icon img').addClass('video-event');
}
