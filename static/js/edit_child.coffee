$(document).ready ->
    $('div.source_facebook a.add').click ->
        window.open('/add_facebook_profile/', 'Adding facebook profile',
            'height=600,width=800,toolbar=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=no')
        return false

