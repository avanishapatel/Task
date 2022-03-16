var $select1 = $( '#id_category' ),
		$select2 = $( '#id_tag' ),
    $options = $select2.find( 'option' );
$select1.on( 'change', function() {
$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );


//$(document).ready(function(){
//     var categoryvar = $("#id_category");
//     var tagvar = $("#id_tag");
//
//     var options = tagvar.find('option:selected')
//     categoryvar.on('click', function(){
//            tagvar.html(options.filter("[value = '+this.value+']"))
//     }).trigger('change');
//  });

//
//$("#id_category").change(function() {
//  if ($(this).data('options') === undefined) {
//    /*Taking an array of all options-2 and kind of embedding it on the select1*/
//    $(this).data('options', $('#id_tag option').clone());
//  }
//  var id = $(this).val();
//  var options = $(this).data('options').filter('[value=' + this.value + ']');
//  $('#id_tag').html(options);
//});


//var options = $("#id_tag").html();
//$("#id_category").change(function(e) {
//    var text = $("#id_category :selected").text();
//    $("#id_tag").html(options);
//    if(text == "All") return;
//    $('#id_tag :not([value^="' + text.substr(0, 3) + '"])').remove();
//});
