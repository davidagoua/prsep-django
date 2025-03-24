<?php
  session_start();  
/*
 * DataTables example server-side processing script.
 *
 * Please note that this script is intentionally extremely simply to show how
 * server-side processing can be implemented, and probably shouldn't be used as
 * the basis for a large complex system. It is suitable for simple use cases as
 * for learning.
 *
 * See http://datatables.net/usage/server-side for full details on the server-
 * side processing requirements of DataTables.
 *
 * @license MIT - http://datatables.net/license_mit
 */

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * Easy set variables
 */

// DB table to use
$table = 'vue_projets';

// Table's primary key
$primaryKey = 'id';


$columns = array(
	
	array( 'db' => 'id', 'dt' => 'id'),
	array( 'db' => 'raison_sociale',  'dt' => 'raison_sociale'),
	array( 'db' => 'nom_secteur',  'dt' => 'nom_secteur'),
	array( 'db' => 'nom_zone',  'dt' => 'nom_zone'),
	array( 'db' => 'investement_prevu',  'dt' => 'investement_prevu'),
	array( 'db' => 'emplois_totaux_an1',  'dt' => 'emplois_totaux_an1'),
	array( 'db' => 'date_comite',  'dt' => 'date_comite'),
	
	array( 'db' => 'longitude',  'dt' => 'longitude'),
	array( 'db' => 'latitude',  'dt' => 'latitude'),
	
	
	array( 'db' => 'id_statut',  'dt' => 'id_statut',
	         'formatter' => function( $d, $row ) {
				 if($d == 1){
			        return '<span class="badge" style="background-color:black"> Non d&eacute;marr&eacute;</span>';
			     } else 
				 if($d == 2){
					 return '<span class="badge" style="background-color:gray"> A peine d&eacute;marr&eacute;</span>';
					
				 } else
				 if($d == 3){
					 return '<span class="badge" style="background-color:orange"> En cours</span>';
					
				 } else
				 if($d == 4){
					 return '<span class="badge" style="background-color:blue"> En finalisation</span>';
					
				 } else
				 if($d == 5){
					 return '<span class="badge" style="background-color: green"> R&eacute;alis&eacute;</span>';
					
				 } else
				 if($d == 6){
					 return '<span class="badge" style="background-color:red"> Arrêt&eacute;, abandonn&eacute;, injoignable</span>';
					
				 } else
				 {
					 return '<span class="badge" style="background-color:black">'.$d.'</span>';
					
				 }  
				 
				
				  return '<div class="lightBoxGallery">
							<a href="../assets/img/lieuculte/'.$d.'/photo1.jpg" title="" onerror="this.src=&quot;../assets/img/lieuculte/photo.png" data-gallery="">
								<img class="img-thumbnail1" src="../assets/img/lieuculte/'.$d.'/photo1.jpg" onerror="this.src=&quot;../assets/img/lieuculte/photo.png&quot;" style="height:50px;padding: 4px;line-height: 1.42857143;background-color: #fff;border: 2px solid #ddd;border-radius: 4px;">
							</a>
							<a href="../assets/img/lieuculte/'.$d.'/photo2.jpg" title="" onerror="this.src=&quot;../assets/img/lieuculte/photo.png" data-gallery="">
							</a>
							<a href="../assets/img/lieuculte/'.$d.'/photo3.jpg" title="" onerror="this.src=&quot;../assets/img/lieuculte/photo.png" data-gallery="">
							</a>
							
													
						</div>';
										  
					
			 }),
		array( 'db' => 'sigle',  'dt' => 'photo',
	         'formatter' => function( $d, $row ) {
				 
				
				  return '<div class="lightBoxGallery">
							<a href="../data/photos/'.$d.'.JPG" title="" onerror="this.src=&quot;../assets/img/lieuculte/photo.png" data-gallery="">
								<img class="img-thumbnail1" src="../data/photos/'.$d.'.JPG" onerror="this.src=&quot;../assets/img/lieuculte/photo.png&quot;" style="height:50px;padding: 4px;line-height: 1.42857143;background-color: #fff;border: 2px solid #ddd;border-radius: 4px;">
							</a>
							
							
													
						</div>';
										  
					
			 }),
			 
          array('db' => 'id', 'dt' => 'action',
	         'formatter' => function( $d, $row ) {
				 
				
					return '
					&nbsp;<button onclick="javascript:fenetre('.$d.')" type="button"  id="PopoverCustomT-1" class="btn btn-warning  btn-sm" style="color:white; ">Details</button>
					      <button onclick="" type="button"  id="PopoverCustomT-1" class="voir btn btn-success  btn-sm" style="color:white; ">Voir</button>'; 
				
				 	
			 })

	
);

			
            

// SQL server connection information
include('../inc_php/details_bd.php');

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * If you just want to use the basic configuration for DataTables with PHP
 * server-side, there is no need to edit below this line.
 */
$query_string = $_SERVER['QUERY_STRING'];
parse_str($query_string, $query_string_array);
 
require( 'ssp.class.pg.php' );


$zone_inv_ = 	htmlspecialchars($query_string_array['zone_inv'], ENT_QUOTES);	
$zone_indust_ = 	htmlspecialchars($query_string_array['zone_indust'], ENT_QUOTES);	
$secteur_ = 	htmlspecialchars($query_string_array['secteur'], ENT_QUOTES);	
$avancement_ = 	htmlspecialchars($query_string_array['avancement'], ENT_QUOTES);	
$nationalite_ = 	htmlspecialchars($query_string_array['nationalite'], ENT_QUOTES);	
$actionnaire_ = 	htmlspecialchars($query_string_array['actionnaire'], ENT_QUOTES);	
$taille_ = 	htmlspecialchars($query_string_array['taille'], ENT_QUOTES);	
$nature_op_ = 	htmlspecialchars($query_string_array['nature_op'], ENT_QUOTES);	
$mode_finance_ = 	htmlspecialchars($query_string_array['mode_finance'], ENT_QUOTES);	

// $vague_ = 	$query_string_array['vague'];	

$zone_inv_ = str_replace("'","''",$zone_inv_);
$zone_indust_ = str_replace("'","''",$zone_indust_);
$secteur_ = str_replace("'","''",$secteur_);
$avancement_ = str_replace("'","''",$avancement_);
$nationalite_ = str_replace("'","''",$nationalite_);
$actionnaire_ = str_replace("'","''",$actionnaire_);
$nature_op_ = str_replace("'","''",$nature_op_);
$taille_ = str_replace("'","''",$taille_);
$mode_finance_ = str_replace("'","''",$mode_finance_);

 

$extraWhere = " id <> 0 "; //~*	




	
					if($zone_inv_ != '')			
						 $extraWhere .= " AND  zone_investissement = '$zone_inv_' ";
					if($zone_indust_ != '')			
						 $extraWhere .= " AND  id_zone_industrielle = $zone_indust_ ";
					if($secteur_ != '')			
						 $extraWhere .= " AND  id_secteur = $secteur_ ";
					 
					
					 
					if($avancement_ != '')			
						 $extraWhere .= " AND  id_statut = $avancement_ ";
					
					if($nationalite_ != '')			
						 $extraWhere .= " AND  $nationalite_ = ANY(array_actionnaire_pays) ";
					
					if($actionnaire_ != '')			
						 $extraWhere .= " AND  $actionnaire_ = ANY(array_actionnaire_id) ";
					
					
					
					
					
					if($taille_ != '')			
						 $extraWhere .= " AND  taille_entreprise = '$taille_' ";
					
					if($nature_op_ != '')			
						 $extraWhere .= " AND  nature_operation = '$nature_op_' ";
					
					if($mode_finance_ != '')			
						 $extraWhere .= " AND  mode_financement = '$mode_finance_' ";
					 
					

 $monfichier = fopen('test.txt', 'r+');
					ftruncate($monfichier,0);
					fputs($monfichier,$extraWhere);
// $monfichier = fopen('test.txt', 'r+');
					// ftruncate($monfichier,0);
					// fputs($monfichier,'444'.$extraWhere); 
echo json_encode(
	// SSP::simple( $_POST, $sql_details, $table, $primaryKey, $columns )
	SSP::simple( $_POST, $sql_details, $table, $primaryKey, $columns, $extraWhere )
);


