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
        title: "Confirmation required",
        confirmButton: "Oh Fur Sure",
        cancelButton: "Hells No"
});

/**
 * This snippet is used for assigning a ".selected" class to a member table row
 * And removes the class from all other rows
*/
$("tbody tr").click(function() {
   $(this).addClass('selected').siblings().removeClass("selected");
});

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
 * View selected on double clicl
*/
/*$('tr.selected').dblclick(function() {
    alert('called');
   display_selected_member();
});*/

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
$('.datepicker').focusin(function(){
    var pos = $(".datepicker").position();
    //alert(pos);
    $('#id_date').datepicker('widget').css({top: pos.top+ 110});
});

