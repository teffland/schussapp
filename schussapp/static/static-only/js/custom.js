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
    if (id == "") {
        return;
    }
    url = prefix + "membership/view/" + id;
    window.location.href = url;
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
