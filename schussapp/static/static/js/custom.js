/**
 *
 * Custom JavaScript for adding dope-ass functionality...more like dope ass-functionality
 * This could get a bit hacky, so I will attempt to keep it well commented.
 *
 * Most of this code assumes the availability of JQuery
 * 
*/

/**
 * This magical snippet is used for making super nice looking search bars
 * Snagged from this JSFiddle:
 * http://jsfiddle.net/KyleMit/cyCFS/19/
*/
$(function() {
    $(".merged input").on({
        // can't simply toggle class because 
        // events can be called multiple times
        focus: function() {
            $(this).prev().addClass("focusedInput")
        },
        blur: function() {
            $(this).prev().removeClass("focusedInput")
        }
    });
});

/**
 * Used to require an alert to be confirmed before deleting or unenrolling a member
*/
$(".confirm").confirm({
        text: "Are you sure you want to delete this? There is no way to reverse this action...",
        title: "Dude, you sure?",
        confirmButton: "Oh Fur Sure",
        cancelButton: "Hells No"
});

/**
 * This snippet is used for assigning a ".selected" class to a member table row
 * And removes the class from all other rows
 * but won't touch header rows
*/
$("tbody tr").click(function() {
    if ( $(this).children('th').length == 0 ) {
        $(this).addClass('selected').siblings().removeClass("selected");
        $(this).parents('.panel').find('.on_select').removeClass('hidden');
    }
});

/**
 * Populate bus reservation edit menu to include a reservation on select
*/
/**
 * Used in conjunction with member select table sidebar in 'member_list'
 * It finds the selected user, and loads their details page
*/

function display_selected_member() {
    current_url = document.URL;
    index = current_url.indexOf("membership");
    prefix = current_url.substring(0,index);
    id = $(".selected").children("#id").text();
    active_id = $(".selected").children("#active_id").text();
    if (id == "") {
        return;
    }
    else if ( active_id == "") {
        url = prefix + "membership/view/" + id;
        window.location.href = url;
    }
    else {
        url = prefix + "membership/view/" + id + "/" + active_id;
        window.location.href = url;
    }
    
}

/**
 * view selected bus day on click
*/
function display_selected_bus() {
    var date = $('select#id_bus option:selected').val();
    //console.log(date);
    current_url = document.URL;
    index = current_url.indexOf("busing");
    prefix = current_url.substring(0,index);
    window.location.href = prefix + 'busing/'+date;
}

/**
 * view the selected trip on click
*/
function display_selected_trip() {
    current_url = document.URL;
    index = current_url.indexOf("trips");
    prefix = current_url.substring(0,index);
    id = $(".selected").children("#id").text();
    if (id == "") {
        return;
    }
    else {
        url = prefix + "trips/view/" + id;
        window.location.href = url;
    }
}

/**
 * Edit a selected trip enrollment from the table
*/
function edit_selected_trip_enroll() {
    enroll_id = $('tr.selected').children('#enroll_id').text();
    //console.log(enroll_id);
    current_url = document.URL;
    index = current_url.indexOf("trips");
    prefix = current_url.substring(0,index);
    if (enroll_id !='') {
        window.location.href = prefix + 'trips/enrollment/edit/' + enroll_id;
    }
}

/**
 * Enroll selected member in trip
*/
function trip_enroll_selected_member() {
    trip_id = $('#trip_id').text();
    pass_id = $('tr.selected').children('#id').text();
    //console.log(trip_id+' , '+pass_id);
    current_url = document.URL;
    index = current_url.indexOf("trips");
    prefix = current_url.substring(0,index);
    if (trip_id !='' && pass_id !='') {
        window.location.href = prefix + 'trips/enrollment/add/' + pass_id + '/' +trip_id;
    }
}
/**
 * take selected bus number and waiting list member and post a checkin form to that bus
 * by filling in the form for that bus and submitting with jQuery
 * ... probably sketchy
*/
function reserve_in_selected_bus() {
    bus_id = $('select#id_bus_num option:selected').val();
    selected_row = $('.wait_list .selected');
    res_id = selected_row.children("#res_id").text();
    
    current_url = document.URL;
    index = current_url.indexOf("busing");
    prefix = current_url.substring(0,index);
    window.location.href = prefix + 'busing/buscheckin/switch/' + res_id + '/' +bus_id;
    
    
}

/**
 * Calls correct url to remove a selected checkin from a bus list
*/
function remove_selected_buscheckin() {
    var id = $('.selected').find('td#res_id').text();
    console.log(id);
    current_url = document.URL;
    index = current_url.indexOf("busing");
    prefix = current_url.substring(0,index);
    window.location.href = prefix + 'busing/buscheckin/remove/'+id;
}
/** Slight change to confirm.js  to accomdate remove selected **/
$('.delete_confirm').confirm({
    text: "Are you sure you want to delete this? There is no way to reverse this action...",
    title: "Dude, you sure?",
    confirm: function(button) {
        remove_selected_buscheckin();
    },
    confirmButton: "Oh Fur Sure",
    cancelButton: "Hells No"
});

/**
 * Check a member in at a mountain
*/
function checkin_member_at_mountain() {
    pass_id = $('#id_pass_num').val();
    new_url = document.URL + '/add-checkin/' + pass_id;
    console.log(new_url);
    window.location.href = new_url;
}

/**
 * Remove a selected member
*/
function remove_selected_mountain_checkin() {
    checkin_id = $('#checkin_id').text();
    //console.log(checkin_id);
    new_url = document.URL + '/remove-checkin/' + checkin_id;
    //console.log(new_url);
    window.location.href = new_url;
}


/**
 * This function is used to enable/disable the reserved id select box
 * Based on if the user checks the "Reserved" checkbox next to it
*/
$("input#id_is_reserved").click(function() {
  if (this.checked) {
    $('select#id_reserved_id').removeAttr("disabled", "disabled");
  }
  else {
    $('select#id_reserved_id').attr("disabled", "disabled");
  }
});

/**
 * Used to read the serachbar when the search "Filter" button is pushed
*/
$(".search-button").click( function() {
    var term = $(".search-bar").val()
    filter_member_table( term );
});

/**
 * Used to dynamically filter the members list table
 * It does so by adding or removing a '.hidden' class to each row of the table,
 * Based on values in the attributes within the row cells
 *
 * The philosophy here is that one giant table of all members is initially rendered to the screen
 * and can be "filtered: by just hiding the ones we don't care about.
 * This reduces database hits, or the need to use Ajax. yay jQuery.
 *
 * NOTE: toUpperCase() is used a lot to provide case insensitive comparisons
 * 
 * Now I know that this is very hacky and there are probably a million better ways to do it
 * But since this is my first time really using jQuery or Django for that matter, cut me some slack ;)
*/
function filter_member_table(filter_term) {
    // display all members
    if (filter_term == 'all') {
        $("td#is_current").each(function() {
            $(this).parent().removeClass("hidden"); 
        });
    }
    // display only active members
    if (filter_term.toUpperCase() == 'ACTIVE') {
        $("td#is_current").each(function() {
            if ($(this).text() == "Yes") {
               $(this).parent().removeClass("hidden");
           }
           else {
               $(this).parent().addClass("hidden");
            }  
        });
    }
    // display only inactive members
    if (filter_term.toUpperCase() == 'INACTIVE') {
        $("td#is_current").each(function() {
            if ($(this).text() == "No") {
               $(this).parent().removeClass("hidden");
           }
           else {
               $(this).parent().addClass("hidden");
            }  
        });
    }
}

/**
 * This one snippet of code is what dynamically filters the members list table by search terms.
 * 
 * I didn't write this myself but I wish I knew regex's like the Jesus who is the creator of this does
 * Found from link: http://jsfiddle.net/dfsq/7BUmG/1133/
 * Or the stack overflow post I found it on:
 * http://stackoverflow.com/questions/9127498/how-to-perform-a-real-time-search-and-filter-on-a-html-table
 *
 * My hat goes off to this guy, cause this shit is fucking awesome. No question. Man I need to get awesome at JS like this guy.
*/
var $rows = $('tbody#member_table tr');
$('#search-bar').keyup(function() {
    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;
    
    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).hide();
});

/**
 * Used in busing: Fill in Name on valid pass number
 * populate member bus reservation field on pass field keyup
*/
$('.pass_search').keyup(function() {
    var field_parent = $(this).parents('.filter_row');
    //console.log(field_parent);
    var first_f = field_parent.find('.first_search');
    var last_f = field_parent.find('.last_search');
    var val = $(this).val().match(/\d{1,5}/);    
    //console.log(val);
    var row = $('td#active_id').filter(function() {
        //console.log( $(this).text() == val);
        return $(this).text() == val;
    }).parent('tr');
    console.log(row.children('td#first_name').text());
    first_f.val( row.children('td#first_name').text() );
    last_f.val( row.children('td#last_name').text() );
});

/**
 * This code initializes the tooltips which display the bus, pass, or lost/stolen notes in the appropriate location
*/
$('#lost_stolen').tooltip({
    animation: true,
    container: 'body',
    placement: 'bottom'
});
$('#bus_flag').tooltip({
    animation: true,
    container: 'body',
    placement: 'bottom'
});
$('#pass_flag').tooltip({
    animation: true,
    container: 'body',
    placement: 'bottom'
});

/**
 * Attach jQuery datePicker to date form fields with #datePicker id
*/
$('#id_date').datepicker();
$('#id_start_date').datepicker();
$('#id_end_date').datepicker();
$('#id_down_payment_due').datepicker();
$('#id_final_payment_due').datepicker();
$('.datepicker').focusin(function(){
    var pos = $(".datepicker").position();
    //alert(pos);
    $('#id_date').datepicker('widget').css({top: pos.top+ 110});
});

/**
 * Toggles sidebar menu in info section
**/
$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

/**
 * Watch window scrolling for info sidebar so transparencies don't overlap
*/
window.onscroll = function()
{
     var scrollTop = (window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;
     console.log(scrollTop); // uncomment this to see the scrollTop value and you'll see how it increments. 
     if(scrollTop >= 50) {
        var sidebarOffset = -50;
    } else if (scrollTop < 0){
        return;
    } else {
        var sidebarOffset = -scrollTop;
    }
     $('#sidebar-wrapper').css('margin-top', sidebarOffset);   
}

