var $select1 = $( '#categories' ),
		$select2 = $( '#selecttag' ),
    $options = $select2.find( 'label' )

$(document).ready(function(){

$select1.on( 'click', function(e) {
$("#header").html("Tag Images" + ' (' + $('#categories').find('option:selected').attr('data-second') +')');
$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );

// Check or Uncheck All checkboxes
   $("#selectAll").click(function(){
     var checked = $(this).is(':checked');
     if(checked){
       $('.checkvalue').each(function(){
         $(this).prop("checked",true);
       });
     }else{
       $('.checkvalue').each(function(){
         $(this).prop("checked",false);
       });
     }
   });

// Changing state of CheckAll checkbox
  $(".checkvalue").click(function(){
    if($(".checkvalue").length == $(".checkvalue:checked").length) {
      $("#selectAll").prop("checked", true);
    } else {
      $("#selectAll").prop("checked", false);
    }

  });

});

