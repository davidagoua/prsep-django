<?php

require_once("../connection.php");	

 
	$dom ='';  
    
	if (isset($_GET["elemid"])) {
		
        $elemid = $_GET["elemid"];
           
		
				
    switch ($elemid) {
						 
			 case "fenetre":
			 
			   $id = $_GET["identifiant"];
			   $sql = "SELECT vue_activite.id, vue_activite.label,label_indicateur,
		                     count(distinct t_activite_localite.gid_localite) as nbre_localite,
							  string_agg(distinct t_activite_localite.gid_localite::text, ',') as localites
	                   FROM public.vue_activite
					   LEFT JOIN public.t_activite_localite ON public.t_activite_localite.id_activite = public.vue_activite.id
					  
					   WHERE 
					    vue_activite.id = $id
					   GROUP BY vue_activite.id, vue_activite.label,label_indicateur;";

									
								$monfichier = fopen('test.txt', 'r+');
								ftruncate($monfichier,0);
								fputs($monfichier,$sql);
										  
								   $rs = $conn->query($sql);
							
								   $row = $rs->fetch(PDO::FETCH_ASSOC);
                                   $label = $row['label'];							   
                                   $label_indicateur = 	$row['label_indicateur'];							   
                                   $localites = 	$row['localites'];							   
                               				   
			      $dom = $label_indicateur.'##'.$label.'##'.$localites;
			 	
			 break;
			 
			 case "enregistrer":
			 
			   $message = '';
			   $id_activite = $_GET["id_activite"];
			   $localite = $_GET["localite"];
			   $localite_name = $_GET["localite_name"];
			   
			   
			   $sql0 = "DELETE FROM public.t_activite_localite
	                   WHERE id_activite = $id_activite;";
               $rs0 = $conn->query($sql0);
			   $row0 = $rs0->fetch(PDO::FETCH_ASSOC); 
			   
			   $arrloc = explode(",", $localite);	
			   $i = 0;
			   While($arrloc[$i]){
			
			      $sql = "INSERT INTO public.t_activite_localite(
                         	       id_activite, gid_localite)
	                      VALUES ($id_activite, ".$arrloc[$i].");";
                  $rs = $conn->query($sql);
			      $row = $rs->fetch(PDO::FETCH_ASSOC); 
			     $i++;
			   }
			 	
			 break;
			 
			 					 
					  
				   }	
				       
		}	

	echo $dom;
?>