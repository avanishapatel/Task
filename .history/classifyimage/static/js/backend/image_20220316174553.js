var $select1 = $( '#id_category' ),
		$select2 = $( '#id_tag' ),
    $options = $select2.find( 'option' );
$select1.on( 'change', function() {
$select2.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );

