<?php
   require_once("../connection.php");	
   
     $titre0 = "Toute la Côte d'Ivoire";
     $titre = "Toutes les composantes";
	 $param = "";
	 
	 $drena = "";
	 // $dpt = "";	 
	 // $spf = "";	 
	 $localite = "";
	 
	 $composante = "";	
	 $sous_composante = "";	
	 $indicateur = "";	
	 $activite = "";	

     $condition = "";	 
     $condition_drena = "";	 
     // $condition_dpt = "";	 
     // $condition_spf = "";	
	 
     $condition_comp = "";	
     $condition_sous_comp = "";	
     $condition_ind = "";	
     $condition_act = "";	
    

     if (isset($_GET["param"])) { $param = $_GET["param"]; } else { $param = ""; } 
	 
	 if (isset($_GET["drena"])) { $drena = $_GET["drena"]; } else { $drena = ""; }	
	 // if (isset($_GET["dpt"])) { $dpt = $_GET["dpt"]; } else { $dpt = ""; }	
	 // if (isset($_GET["spf"])) { $spf = $_GET["spf"]; } else { $spf = ""; }		 
	 if (isset($_GET["localite"])) { $localite = $_GET["localite"]; } else { $localite = ""; }	
	 
	 if (isset($_GET["composante"])) { $composante = $_GET["composante"]; } else { $composante = ""; }		 
	 if (isset($_GET["sous_composante"])) { $sous_composante = $_GET["sous_composante"]; } else { $sous_composante = ""; }		 
	 if (isset($_GET["indicateur"])) { $indicateur = $_GET["indicateur"]; } else { $indicateur = ""; }		 
	 if (isset($_GET["activite"])) { $activite = $_GET["activite"]; } else { $activite = ""; }		 
	
	 if($drena != ""){		 
		 // $condition .= " AND code_reg = '$region'";
		 $condition_drena .= " AND code_dren = '$drena'";
		 
	  } 
	  // if($dpt != ""){		 
		
		 // $condition_dpt .= " AND code_dept = '$dpt'";
		
	  // }
	  
	  // if($spf != ""){		 
		
		 // $condition_spf .= " AND code_sp = '$spf'";
		 
	  // }
	
	  
	    $sql_drena = "SELECT code_dren, nom_dren
	                   FROM public.drenas
					   ORDER BY nom_dren;";
					   
					   
								
		$rs_drena = $conn->query($sql_drena);
		$nbre_drena = $rs_drena->rowCount();	
		$liste_drena = '';
					
		while ($row_drena = $rs_drena->fetch(PDO::FETCH_ASSOC)) { 
			$code_dren = $row_drena['code_dren'];
			$nom_dren = $row_drena['nom_dren'];
			if($code_dren == $drena){
				$liste_drena .= ' <option value="'.$code_dren.'" selected>'.$nom_dren.'</option>';
				$titre0 = ' <strong>DRENA</strong> - '.$nom_dren; 
			} else {
			    $liste_drena .= ' <option value="'.$code_dren.'">'.$nom_dren.'</option>'; 
			}	  
		} 
					   
		
	   if($composante != ""){		 
		 // $condition .= " AND code_sp = '$spf'";
		 $condition_comp .= " AND composant_id = $composante";
		 
	   }
	   
	   if($sous_composante != ""){		 
		 // $condition .= " AND code_sp = '$spf'";
		 $condition_sous_comp .= " AND sous_composant_id = $sous_composante";
		 
	   }
	 
	    if($indicateur != ""){		 
		 // $condition .= " AND code_sp = '$spf'";
		 $condition_ind .= " AND indicateur_id = $indicateur";
		 
	   }
	   
	   if($activite != ""){		 
		 // $condition .= " AND code_sp = '$spf'";
		 $condition_act .= " AND id_activite = $activite";
		 
	   }
	 
	 
	 
	 
		$sql_composante = "SELECT id, created, modified, label, status, ptba_id
	                       FROM public.planification_composantprojet
					       ORDER BY label;";
					
				
		$rs_composante = $conn->query($sql_composante);
		$nbre_composante = $rs_composante->rowCount();	
		$liste_composante = '';
					 
		while ($row_composante = $rs_composante->fetch(PDO::FETCH_ASSOC)) { 
			$label = $row_composante['label'];
			$id = $row_composante['id'];
			if($id == $composante){
				$liste_composante .= ' <option value="'.$id.'" selected>'.$label.'</option>';
				$titre = ' - '.$label; 
		    } else {
				$liste_composante .= ' <option value="'.$id.'">'.$label.'</option>'; 
		    }
		}
		
		
		$sql_sous_composante = "SELECT id, created, modified, label, status, composant_id
	                            FROM public.planification_souscomposantprojet
								WHERE id != 0 $condition_comp
					            ORDER BY label;";
					
				
		$rs_sous_composante = $conn->query($sql_sous_composante);
		$nbre_sous_composante = $rs_sous_composante->rowCount();	
		$liste_sous_composante = '';
					 
		while ($row_sous_composante = $rs_sous_composante->fetch(PDO::FETCH_ASSOC)) { 
			$label = $row_sous_composante['label'];
			$id = $row_sous_composante['id'];
			if($id == $sous_composante){
				$liste_sous_composante .= ' <option value="'.$id.'" selected>'.$label.'</option>';
				$titre = ' <strong>Sous-composante :</strong> '.$label; 
		    } else {
				$liste_sous_composante .= ' <option value="'.$id.'">'.$label.'</option>'; 
		    }
		}
		
		
		$sql_indicateur = "SELECT distinct on (planification_indicateur.id,planification_indicateur.label) planification_indicateur.id, planification_indicateur.label, sous_composant_id
	                            FROM public.planification_indicateur, planification_souscomposantprojet
								WHERE planification_indicateur.sous_composant_id = planification_souscomposantprojet.id
   								      $condition_comp $condition_sous_comp
					            ORDER BY planification_indicateur.label;";
					
				
		$rs_indicateur = $conn->query($sql_indicateur);
		$nbre_indicateur = $rs_indicateur->rowCount();	
		$liste_indicateur = '';
					 
		while ($row_indicateur = $rs_indicateur->fetch(PDO::FETCH_ASSOC)) { 
			$label = $row_indicateur['label'];
			$id = $row_indicateur['id'];
			if($id == $indicateur){
				$liste_indicateur .= ' <option value="'.$id.'" selected>'.$label.'</option>';
				$titre = ' <strong>Indicateur :</strong> '.$label; 
		    } else {
				$liste_indicateur .= ' <option value="'.$id.'">'.$label.'</option>'; 
		    }
		}
		
		
		
		$sql_tache = "SELECT distinct on (vue_activite.id, vue_activite.label) vue_activite.id, vue_activite.label
	                  FROM public.vue_activite
					  LEFT JOIN public.t_activite_localite ON public.t_activite_localite.id_activite = public.vue_activite.id
					  LEFT JOIN localites ON localites.gid = t_activite_localite.gid_localite  $condition_drena 
					  WHERE vue_activite.id != 0
					   
						$condition_comp $condition_sous_comp $condition_ind  
						
					    ORDER BY vue_activite.label;";
								
								
							
					
				
		$rs_tache = $conn->query($sql_tache);
		$nbre_tache = $rs_tache->rowCount();	
		$liste_activite = '';
		if($activite != '') $nbre_tache = 1;
					 
		while ($row_tache = $rs_tache->fetch(PDO::FETCH_ASSOC)) { 
			$label = $row_tache['label'];
			$id = $row_tache['id'];
			if($id == $activite){
				$liste_activite .= ' <option value="'.$id.'" selected>'.$label.'</option>';
				$titre = ' <strong>Activité</strong> : '.$label; 
		    } else {
				$liste_activite .= ' <option value="'.$id.'">'.$label.'</option>'; 
		    }
		}
		
		

       
		if($drena != ''){
			
			 $sql_limite = "SELECT drenas.code_dren as code, 'DRENA '||drenas.nom_dren as nom,public.ST_AsGeoJSON(drenas.geom,6) as geojson,
									count(distinct t.id) as nbre_activite, 
									count(distinct t.gid_localite) as nbre_localite
							 FROM public.drenas
							 LEFT JOIN public.localites ON drenas.code_dren = localites.code_dren 
				             LEFT JOIN (SELECT gid_localite, vue_activite.id, indicateur_id, sous_composant_id, composant_id, id_activite
						              FROM public.t_activite_localite, public.vue_activite
                                      WHERE public.t_activite_localite.id_activite = public.vue_activite.id	) as t ON localites.gid = t.gid_localite  
						   
						    $condition_comp $condition_sous_comp $condition_ind $condition_act
							  WHERE drenas.id <> 0  AND drenas.code_dren = '$drena'
							  GROUP BY drenas.code_dren, drenas.nom_dren, drenas.geom
										   ORDER BY drenas.nom_dren;";
			
		} else {
			$sql_limite = "SELECT drenas.code_dren as code, drenas.nom_dren as nom,public.ST_AsGeoJSON(drenas.geom,6) as geojson,
									count(distinct t.id) as nbre_activite, 
									count(distinct t.gid_localite) as nbre_localite
									
			               FROM public.drenas
				           LEFT JOIN public.localites ON drenas.code_dren = localites.code_dren
				           LEFT JOIN (SELECT gid_localite, vue_activite.id, indicateur_id, sous_composant_id, composant_id, id_activite
						              FROM public.t_activite_localite, public.vue_activite
                                      WHERE public.t_activite_localite.id_activite = public.vue_activite.id	) as t ON localites.gid = t.gid_localite  
						   
						    $condition_comp $condition_sous_comp $condition_ind $condition_act
				    
						   
				           GROUP BY drenas.code_dren, drenas.nom_dren, drenas.geom
				           ORDER BY drenas.nom_dren;";
						   
						
		}
		
		  
			   
		
			$rs_limite = $conn->query($sql_limite);
					
			$nbre_entite = $rs_limite->rowCount();	
					
						$i = 0;
				$geojson_limite = array(
				  'type'      => 'FeatureCollection',
				  'features'  => array()
				);
							
		$nbre_activite = 0;
		$nbre_localite = 0;
				
			while ($row_limite = $rs_limite->fetch(PDO::FETCH_ASSOC)) {
				    
				 $nom = $row_limite['nom'];   
				 
				 $nbre_activite += $row_limite['nbre_activite'];     
				 $nbre_localite += $row_limite['nbre_localite'];     
				 
				
				 
				  $properties_limite = $row_limite;
								
									unset($properties_limite['geojson']);
									unset($properties_limite['geom']);
									$feature_limite = array(
										 'type' => 'Feature',
										 'geometry' => json_decode($row_limite['geojson'], true),
										 'properties' => $properties_limite
									);
									
						
									array_push($geojson_limite['features'], $feature_limite);	


				 
				
			}	





         $sql_localite = "SELECT localites.gid,  localites.nomloc,  localites.code_sp,  localites.nom_sp,  localites.code_dept, 
		                         localites.code_dren,  localites.code_dist,  localites.district,  localites.nom_dren,  localites.departemen, 
								 localites.geom,  public.ST_AsGeoJSON(localites.geom,6) as geojson,
								 count(distinct id_activite) as nbre_activite
							    FROM public.localites,public.t_activite_localite, vue_activite
								WHERE localites.gid = public.t_activite_localite.gid_localite 
								AND public.t_activite_localite.id_activite = vue_activite.id
								$condition_comp $condition_sous_comp $condition_ind $condition_act
								$condition_drena
								GROUP BY localites.gid,  localites.nomloc,  localites.code_sp,  localites.nom_sp,  localites.code_dept, 
		                         localites.code_dren,  localites.code_dist,  localites.district,  localites.nom_dren,  localites.departemen, 
								 localites.geom;";
				 		   
	
					 $rs_localite = $conn->query($sql_localite);
					 $nbre_localite = $rs_localite->rowCount();	
					 
					 $geojson_localite = array(
						   'type'      => 'FeatureCollection',
						   'features'  => array()
						);
						
						
					   while ($row_localite = $rs_localite->fetch(PDO::FETCH_ASSOC)) { 
						  
						  $properties = $row_localite;
							
								unset($properties['geojson']);
								unset($properties['geom']);
								$feature = array(
									 'type' => 'Feature',
									 'geometry' => json_decode($row_localite['geojson'], true),
									 'properties' => $properties
								);
								array_push($geojson_localite['features'], $feature);	
						  
					   } 			

   


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Riho admin is super flexible, powerful, clean &amp; modern responsive bootstrap 5 admin template with unlimited possibilities.">
    <meta name="keywords" content="admin template, Riho admin template, dashboard template, flat admin template, responsive admin template, web app">
    <meta name="author" content="pixelstrap">
    <link rel="icon" href="/static/assets/images/favicon.png" type="image/x-icon">
    <link rel="shortcut icon" href="/static/assets/images/favicon.png" type="image/x-icon">
    <title>PRSEP - Digitalisation</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700;800&amp;display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/font-awesome.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/icofont.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/themify.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/flag-icon.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/feather-icon.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/slick.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/slick-theme.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/scrollbar.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/animate.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/select2.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/vendors/bootstrap.css">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/style.css">
    <link id="color" rel="stylesheet" href="/static/assets/css/color-1.css" media="screen">
    <link rel="stylesheet" type="text/css" href="/static/assets/css/responsive.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" integrity="sha512-Evv84Mr4kqVGRNSgIGL/F/aIDqQb7xQ2vcrdIwxfjThSH8CSR7PBEakCr51Ck+w+/U6swU2Im1vVX0SVk9ABhg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/js/all.min.js" integrity="sha512-b+nQTCdtTBIRIbraqNEwsjB6UvL3UEMkXnhzd8awtCYh0Kcsjl9uEgwVFVbhoj3uu1DO1ZMacNvLoyJJiNfcvg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="//unpkg.com/alpinejs" defer></script>

    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
          integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
          crossorigin=""/>
		  
    <link rel="stylesheet" href="/static/assets/js/Leaflet.iconlabel-master/src/Icon.Label.css" />
    <link rel="stylesheet" href="/static/assets/js/leaflet-groupedlayercontrol/leaflet.groupedlayercontrol.css">
	<link rel="stylesheet" href="/static/assets/js/Leaflet.label-master/dist/leaflet.label.css" />
  
		  
	<link href="/static/assets/js/Leaflet.fullscreen-gh-pages/dist/leaflet.fullscreen.css" rel="stylesheet" />	  
    <link rel="stylesheet" href="/static/assets/js/Leaflet.ExtraMarkers-master/dist/css/leaflet.extra-markers.min.css">
	

</head>
<body>
<!-- loader starts-->
<div class="loader-wrapper">
    <div class="loader">
        <div class="loader4"></div>
    </div>
</div>
<!-- loader ends-->
<!-- tap on top starts-->
<div class="tap-top"><i data-feather="chevrons-up"></i></div>
<!-- tap on tap ends-->
<!-- page-wrapper Start-->
<div class="page-wrapper compact-wrapper" id="pageWrapper">
    <!-- Page Header Start-->

    <div class="page-header">
        <div class="header-wrapper row m-0">
            <form class="form-inline search-full col" action="#" method="get">
                <div class="form-group w-100">
                    <div class="Typeahead Typeahead--twitterUsers">
                        <div class="u-posRelative">
                            <input class="demo-input Typeahead-input form-control-plaintext w-100" type="text" placeholder="Search Riho .." name="q" title="" autofocus>
                            <div class="spinner-border Typeahead-spinner" role="status"><span class="sr-only">Loading... </span></div><i class="close-search" data-feather="x"></i>
                        </div>
                        <div class="Typeahead-menu"> </div>
                    </div>
                </div>
            </form>
            <div class="header-logo-wrapper col-auto p-0">
                <div class="logo-wrapper"> <a href="index.html"><img class="img-fluid for-light" src="/static/assets/images/logo/logo_dark.png" alt="logo-light"><img class="img-fluid for-dark" src="/static/assets/images/logo/logo.png" alt="logo-dark"></a></div>
                <div class="toggle-sidebar"> <i class="status_toggle middle sidebar-toggle" data-feather="align-center"></i></div>
            </div>
            <div class="left-header col-xxl-5 col-xl-6 col-lg-5 col-md-4 col-sm-3 p-0">
                <div> <a class="toggle-sidebar" href="#"> <i class="iconly-Category icli"> </i></a>
                    <div class="d-flex align-items-center gap-2 ">
                        <h4 class="f-w-600">Bienvenue, admin</h4><img class="mt-0" src="/static/assets/images/hand.gif" alt="hand-gif">
                    </div>
                </div>
            </div>
            <div class="nav-right col-xxl-7 col-xl-6 col-md-7 col-8 pull-right right-header p-0 ms-auto">
                <ul class="nav-menus">
                    <li class="d-md-block d-none">
                        <div class="form search-form mb-0">
                            <div class="input-group"><span class="input-icon">
                      <svg>
                        <use href="assets/svg/icon-sprite.svg%23search-header"></use>
                      </svg>
                      <input class="w-100" type="search" placeholder="Search"></span></div>
                        </div>
                    </li>

                    <li>
                        <div class="mode"><i class="moon" data-feather="moon"> </i></div>
                    </li>
                    <li class="onhover-dropdown notification-down">
                        <div class="notification-box">
                            <svg>
                                <use href="assets/svg/icon-sprite.svg#notification-header"></use>
                            </svg><span class="badge rounded-pill badge-secondary">0 </span>
                        </div>
                        <div class="onhover-show-div notification-dropdown">
                            <div class="card mb-0">
                                <div class="card-header">
                                    <div class="common-space">
                                        <h4 class="text-start f-w-600">Notitications</h4>
                                        <div><span>0 notification</span></div>
                                    </div>
                                </div>
                                <div class="card-body">
                                    <div class="notitications-bar">

                                        <div class="notification-card">
                                            <ul>
                                                <li class="notification d-flex w-100 justify-content-between align-items-center">
                                                    <div class="d-flex w-100 notification-data justify-content-center align-items-center gap-2">
                                                        <div class="user-alerts flex-shrink-0"><img class="rounded-circle img-fluid img-40" src="/static/assets/images/dashboard/user/3.jpg" alt="user"/></div>
                                                        <div class="flex-grow-1">
                                                            <div class="common-space user-id w-100">
                                                                <div class="common-space w-100"> <a class="f-w-500 f-12" href="template/private-chat.html">Robert D. Hambly</a></div>
                                                            </div>
                                                            <div><span class="f-w-500 f-light f-12">Hello Miss...😊</span></div>
                                                        </div><span class="f-light f-w-500 f-12">44 sec</span>
                                                    </div>
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </li>
                    <li class="profile-nav onhover-dropdown">
                        <div class="media profile-media"><img class="b-r-10" src="/static/assets/images/dashboard/profile.png" alt="">
                            <div class="media-body d-xxl-block d-none box-col-none">
                                <div class="d-flex align-items-center gap-2"> <span> </span><i class="middle fa fa-angle-down"> </i></div>
                                <p class="mb-0 font-roboto">None</p>
                            </div>
                        </div>
                        <ul class="profile-dropdown onhover-show-div">
                            <li><a href=""><i data-feather="user"></i><span>Profile</span></a></li>
                            <li><a class="btn btn-pill btn-outline-primary btn-sm" href="/deconnexion">Déconnexion</a></li>
                        </ul>
                    </li>
                </ul>
            </div>

            <script class="empty-template" type="text/x-handlebars-template"><div class="EmptyMessage">Your search turned up 0 results. This most likely means the backend is down, yikes!</div></script>
        </div>
    </div>
    <!-- Page Header Ends                              -->
    <!-- Page Body Start -->
    <div class="page-body-wrapper"/>
    <!-- Page Sidebar Start-->

    <div class="sidebar-wrapper" data-layout="stroke-svg">
        <div class="logo-wrapper"><a href="index.html"><img class="img-fluid" height="auto" width="70" src="/static/assets/images/logo/logo.png" alt=""></a>
            <div class="back-btn"><i class="fa fa-angle-left"> </i></div>
            <div class="toggle-sidebar"><i class="status_toggle middle sidebar-toggle" data-feather="grid"> </i></div>
        </div>
        <div class="logo-icon-wrapper"><a href="index.html"><img class="img-fluid" height="auto" width="70" src="/static/assets/images/logo/logo.png" alt=""></a></div>
        <nav class="sidebar-main">
            <div class="left-arrow" id="left-arrow"><i data-feather="arrow-left"></i></div>
            <div id="sidebar-menu">
                <ul x-data="{
                tdr_stats: []
              }" x-init="tdr_stats = await (await fetch('/suivi/tdr-get-stats')).json()" class="sidebar-links" id="simple-bar">
                    <li class="back-btn"><a href="index.html"><img class="img-fluid" height="auto" width="70" src="/static/assets/images/logo/logo.png" alt=""></a>
                        <div class="mobile-back text-end"> <span>Back </span><i class="fa fa-angle-right ps-2" aria-hidden="true"></i></div>
                    </li>
                    <li class="pin-title sidebar-main-title">
                        <div>
                            <h6>Pinned</h6>
                        </div>
                    </li>
                    <li class="sidebar-main-title">
                        <div>
                            <h6 class="lan-1">Général</h6>
                        </div>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/">
                        <span class="fa text-white fa-home ml-2"></span>
                        <span>Tableau de bord</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/static/cartographie/">
                        <span class="fa text-white fa-map ml-2"></span>
                        <span>Cartographie</span></a>
                    </li>
					  <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/static/maj_cartographie/">
                        <span class="fa text-white fa-map ml-2"></span>
                        <span>MAJ Cartographie</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/analyse/">
                        <span class="fa text-white fa-pie-chart ml-2"></span>
                        <span>Analyse</span></a>
                    </li>

                    <li class="sidebar-main-title">
                        <div>
                            <h6 class="">Planification</h6>
                        </div>
                    </li>

                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/planification/ptba-projet/">
                        <span class="fa text-white fa-calendar ml-2"></span>
                        <span>PTBA Projet</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/planification/ptba-programme/">
                        <span class="fa text-white fa-calendar ml-2"></span>
                        <span>PTBA Programme</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/planification/ppm-list/">
                        <span class="fa text-white fa-handshake-simple ml-2"></span>
                        <span>PPM</span></a>
                    </li>

                    <li class="sidebar-main-title">
                        <div>
                            <h6 class="">Suivi & Planification</h6>
                        </div>
                    </li>

                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/suivi/ptba-projet">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span>Suivi PTBA Projet</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="file-manager.html">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span>PTBA Programme</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="file-manager.html">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span>Suivi PPM</span></a>
                    </li>


                    <li class="sidebar-main-title">
                        <div>
                            <h6 class="">Suivi Execution</h6>
                        </div>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link d-flex justify-content-between sidebar-title link-nav" href="/suivi/activites/">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span class="flex-grow-1">Point Focal</span>
                        <span x-text="tdr_stats['pointFocal'] ?? 0" class="bg-danger p-1 rounded-pill"></span>
                    </a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link d-flex w-100 justify-content-between sidebar-title link-nav" href="/suivi/tdr-local/">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span class="flex-grow-1">Direction Locale</span>
                        <span x-text="tdr_stats[10] ?? 0" class="bg-warning p-1 rounded-pill"></span>
                    </a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title d-flex justify-content-between link-nav" href="/suivi/tdr-technique/">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span class="flex-grow-1">Dir. Technique</span>
                        <span class="bg-light-info p-1 rounded-pill" x-text="tdr_stats[20] ?? 0"></span>
                    </a>
                    </li>

                    <li class="sidebar-list"><a class="sidebar-link d-flex d-block justify-content-between sidebar-title link-nav" href="/suivi/tdr-coordination/">
                        <span class="fa text-white fa-binoculars ml-2"></span>
                        <span class="flex-grow-1">Coordination</span>
                        <span class="bg-success p-1 rounded-pill" x-text="tdr_stats[30] ?? 0"></span>
                    </a>
                    </li>

                    <li class="sidebar-main-title">
                        <div>
                            <h6 class="">Rapportage</h6>
                        </div>
                    </li>

                    <li class="sidebar-list">
                        <a class="sidebar-link sidebar-title link-nav" href="/rapportage/rapport-mensuel/">
                            <span class="fa text-white fa-file-pen ml-2"></span>
                            <span>Rapport Mensuel</span>
                        </a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/rapportage/rapport-trimestriel/">
                        <span class="fa text-white fa-file-pen ml-2"></span>
                        <span>Rapport Trimestriel</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/rapportage/rapport-semestriel/">
                        <span class="fa text-white fa-file-pen ml-2"></span>
                        <span>Rapport Semestriel</span></a>
                    </li>
                    <li class="sidebar-list"><a class="sidebar-link sidebar-title link-nav" href="/rapportage/rapport-annuel/">
                        <span class="fa text-white fa-file-pen ml-2"></span>
                        <span>Rapport Annuel</span></a>
                    </li>
                    <li class="sidebar-list">
                        <a class="sidebar-link sidebar-title link-nav" href="/rapportage/rapport-consolide/">
                            <span class="fa text-white fa-file-pen ml-2"></span>
                            <span>Rapport Consolidé</span>
                        </a>
                    </li>


                    <li class="sidebar-main-title">
                        <div>
                            <h6 class="">Paramètres</h6>
                        </div>
                    </li>

                    <li class="sidebar-list">
                        <a class="sidebar-link sidebar-title link-nav" href="/create-user/">
                            <span class="fa text-white fa-users ml-2"></span>
                            <span>Utilisateurs</span>
                        </a>
                    </li>
                    <li class="sidebar-list">
                        <a class="sidebar-link sidebar-title link-nav" href="/parametres/composantes/">
                            <span class="fa text-white fa-boxes-stacked ml-2"></span>
                            <span>Composantes</span>
                        </a>
                    </li>

                </ul>
                <div class="right-arrow" id="right-arrow"><i data-feather="arrow-right"></i></div>
            </div>
        </nav>
    </div>
    <!-- Page Sidebar Ends-->

    <div class="page-body">
        <div class="container-fluid">
            <div class="page-title">
                <div class="row">
                   
                </div>
            </div>
        </div>
        <!-- Container-fluid starts-->
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-3">
                     <div class="card" style="height:100%; box-shadow: 0px 0px 26px 0px rgba(0,0,0,0.5);">
					    <div class="card-header" style="padding: 1rem 10px 0.7rem;">
                      <ul class="nav nav-pills" role="tablist">
                        <li class="nav-item">
                          <button
						    
                            type="button"
                            class="nav-link  active"
                            role="tab"
							style="background-color: #8b0000;"
                            
                          >
                            Filtre
                          </button>
						  
						  
						  
                        </li>
                       
                       <li class="nav-item">
						     <h5 class="card-title " style="border-radius: 0.375rem;line-height: 1.5rem;padding: 0.3rem 1.5rem;float:right; position: absolute;text-align:center;right: 10px;top: 15px; color: #8b0000;
background-color: rgba(139, 0, 0, 0.12) !important;"> </h5>
						    
						  </li>
						
                      </ul>
                    </div>
                        <div class="card-body" style="padding: 10px 15px 0px;">
						   <div class="mb-3" style="margin-bottom: 0.4rem !important;">
						     <h5 class="card-title " style="border-radius: 0.375rem;line-height: 1.5rem;padding: 0.3rem 1.5rem;text-align:center;right: 10px;top: 5px; color: #8b0000;
background-color: rgba(139, 0, 0, 0.12) !important;">
						      <?php echo $titre0;?> <br><?php echo $titre;  ?> <br><?php echo $nbre_tache.' activité(s)';  ?>
					     	</h5>
					     	</div>
						   <div class="mb-3" style="margin-bottom: 0.4rem !important;">
													<label for="exampleFormControlSelect1" class="form-label">DRENA</label>
													<select id="drena"  onchange="select('drena')" class="form-select" id="exampleFormControlSelect1" aria-label="Default select example">
													  <option value="">---</option>
													  <?php echo $liste_drena;  ?>
													</select>
													</div>
						
													
							<hr class="m-4" style="margin: 2rem 1.5rem 1.5rem !important;">
							
							
							<div class="mb-3" style="margin-bottom: 0.4rem !important;">
													<label for="exampleFormControlSelect1" class="form-label">Composantes</label>
													<select id="composante"  onchange="document.getElementById('sous_composante').options[0].selected=true; document.getElementById('indicateur').options[0].selected=true; document.getElementById('activite').options[0].selected=true; select('composante')" class="form-select" id="exampleFormControlSelect1" aria-label="Default select example">
													  <option value="">---</option>
													  <?php echo $liste_composante;  ?>
													</select>
													</div>
													
							<div class="mb-3" style="margin-bottom: 0.4rem !important;">
													<label for="exampleFormControlSelect1" class="form-label">Sous-composantes</label>
													<select id="sous_composante"  onchange="document.getElementById('indicateur').options[0].selected=true; document.getElementById('activite').options[0].selected=true;select('sous_composante')" class="form-select" id="exampleFormControlSelect1" aria-label="Default select example">
													  <option value="">---</option>
													  <?php echo $liste_sous_composante;  ?>
													</select>
													</div>
													
							<div class="mb-3" style="margin-bottom: 0.4rem !important;">
													<label for="exampleFormControlSelect1" class="form-label">Indicateurs</label>
													<select id="indicateur"  onchange="document.getElementById('activite').options[0].selected=true;select('indicateur')" class="form-select" id="exampleFormControlSelect1" aria-label="Default select example">
													  <option value="">---</option>
													  <?php echo $liste_indicateur;  ?>
													</select>
													</div>
													
							 <div class="mb-3" style="margin-bottom: 0.4rem !important;">
													<label for="exampleFormControlSelect1" class="form-label">Activités</label>
													<select id="activite"  onchange="select('activite')" class="form-select" id="exampleFormControlSelect1" aria-label="Default select example">
													  <option value="">---</option>
													  <?php echo $liste_activite;  ?>
													</select>
													</div>
						
						</div>
                    </div>
                </div>
                <div class="col-md-9 "  style="border-radius:0.5rem">
				   <div class="card" style="height:100%; box-shadow: 0px 0px 26px 0px rgba(0,0,0,0.5);">
				     <div class="card-header" style="padding: 1rem 1.5rem 0.7rem;">
                      <ul class="nav nav-pills" role="tablist">
                        <li class="nav-item">
                          <button
						    
                            type="button"
                            class="nav-link  active"
                            role="tab"
							style="background-color: #8b0000;"
                            
                          >
                            Cartographie des activités du projet
                          </button>
						  
						  
						  
                        </li>
                       
                       
						 <li class="nav-item">
						     <h5 class="card-title " style="text-transform: none;border-radius: 0.375rem;line-height: 1.5rem;padding: 0.3rem 1.5rem;float:right; position: absolute;text-align:center;right: 10px;top: 15px; color: #8b0000;
background-color: rgba(139, 0, 0, 0.12) !important;"><?php echo $titre0.' : '.$nbre_localite.' localité(s) concernée(s)';  ?> </h5>
						    
						  </li>
                      </ul>
                    </div>
					 <div id="map" class="" style="height:680px;top: 10px;bottom: 0;left: 0;width: 100%;border-radius: 0.5rem"></div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Container-fluid Ends-->
    </div>

</div>

<!-- latest jquery-->
<script src="/static/assets/js/jquery.min.js"></script>
<script src="/static/assets/js/bootstrap/bootstrap.bundle.min.js"></script>
<script src="/static/assets/js/icons/feather-icon/feather.min.js"></script>
<script src="/static/assets/js/icons/feather-icon/feather-icon.js"></script>
<script src="/static/assets/js/scrollbar/simplebar.js"></script>
<script src="/static/assets/js/scrollbar/custom.js"></script>
<script src="/static/assets/js/config.js"></script>
<script src="/static/assets/js/sidebar-menu.js"></script>
<script src="/static/assets/js/sidebar-pin.js"></script>
<script src="/static/assets/js/slick/slick.min.js"></script>
<script src="/static/assets/js/slick/slick.js"></script>
<script src="/static/assets/js/header-slick.js"></script>
<script src="/static/assets/js/select2/select2.full.min.js"></script>
<script src="/static/assets/js/select2/select2-custom.js"></script>
<script src="/static/assets/js/form-validation-custom.js"></script>
<script src="/static/assets/js/script.js"></script>

<script>
    $('input, select, textarea').addClass('form-control')
    $('.c-pills-tab').style.display = 'none'
</script>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
        crossorigin=""></script>
		
 
    <script  src="/static/assets/js/leaflet-groupedlayercontrol/leaflet.groupedlayercontrol.js"></script>  
    <script  src="/static/assets/js/Leaflet.iconlabel-master/src/Icon.Label.js"></script>	
    <script  src="/static/assets/js/leaflet-icon-pulse-master/src/L.Icon.Pulse.js" /> 
	<script  src="/static/assets/js/Leaflet.EasyButton-master/src/easy-button.js"></script> 

    <script>

      var blanc = ''  ;
	  alert("test 1");
	  var param = '<?php echo $param; ?>'  ;
</script>

    <script src="/static/assets/js/Leaflet.label-master/src/Label.js"></script>
	<script src="/static/assets/js/Leaflet.label-master/src/BaseMarkerMethods.js"></script>
	<script src="/static/assets/js/Leaflet.label-master/src/Marker.Label.js"></script>
	<script src="/static/assets/js/Leaflet.label-master/src/CircleMarker.Label.js"></script>
	<script src="/static/assets/js/Leaflet.label-master/src/Path.Label.js"></script>
	<script src="/static/assets/js/Leaflet.label-master/src/Map.Label.js"></script> 
	<script src="/static/assets/js/Leaflet.label-master/src/FeatureGroup.Label.js"></script> 
 
	<script>

      var blanc = ''  ;
	  alert("test 2");
	  var param = '<?php echo $param; ?>'  ;
</script>
 <script src='/static/assets/js/Leaflet.fullscreen-gh-pages/dist/Leaflet.fullscreen.min.js'></script>  		
 <script src="/static/assets/js/Leaflet.ExtraMarkers-master/dist/js/leaflet.extra-markers.min.js"></script>
	
 <script>

var blanc = ''  ;
alert("test 3");
var param = '<?php echo $param; ?>'  ;
</script>

<script>

      var blanc = ''  ;
	  alert("test 4");
	  var param = '<?php echo $param; ?>'  ;
       var drena = '<?php echo $drena; ?>'  ;
	    // var dpt = '<?php echo $dpt; ?>'  ;
	    // var spf = '<?php echo $spf; ?>'  ;
	    var localite = '<?php echo $localite; ?>'  ;

    var json_localite = <?php echo json_encode($geojson_localite, JSON_NUMERIC_CHECK); ?>; 
    var json_limite = <?php echo json_encode($geojson_limite, JSON_NUMERIC_CHECK); ?>; 
	
	
		function number_format (number, decimals, dec_point, thousands_sep) {
			 
			  // *     example 1: number_format(1234.56);
			  // *     returns 1: '1,235'
			  // *     example 2: number_format(1234.56, 2, ',', ' ');
			  // *     returns 2: '1 234,56'
			  // *     example 3: number_format(1234.5678, 2, '.', '');
			  // *     returns 3: '1234.57'
			  // *     example 4: number_format(67, 2, ',', '.');
			  // *     returns 4: '67,00'
			  // *     example 5: number_format(1000);
			  // *     returns 5: '1,000'
			  // *     example 6: number_format(67.311, 2);
			  // *     returns 6: '67.31'
			  // *     example 7: number_format(1000.55, 1);
			  // *     returns 7: '1,000.6'
			  // *     example 8: number_format(67000, 5, ',', '.');
			  // *     returns 8: '67.000,00000'
			  // *     example 9: number_format(0.9, 0);
			  // *     returns 9: '1'
			  // *    example 10: number_format('1.20', 2);
			  // *    returns 10: '1.20'
			  // *    example 11: number_format('1.20', 4);
			  // *    returns 11: '1.2000'
			  // *    example 12: number_format('1.2000', 3);
			  // *    returns 12: '1.200'
			  // *    example 13: number_format('1 000,50', 2, '.', ' ');
			  // *    returns 13: '100 050.00'
			  // Strip all characters but numerical ones.
			  number = (number + '').replace(/[^0-9+\-Ee.]/g, '');
			  var n = !isFinite(+number) ? 0 : +number,
				prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
				sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
				dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
				s = '',
				toFixedFix = function (n, prec) {
				  var k = Math.pow(10, prec);
				  return '' + Math.round(n * k) / k;
				};
			  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
			  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
			  if (s[0].length > 3) {
				s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
			  }
			  if ((s[1] || '').length < prec) {
				s[1] = s[1] || '';
				s[1] += new Array(prec - s[1].length + 1).join('0');
			  }
			  return s.join(dec);
			}
	 
		
     var map = new L.Map('map', {fullscreenControl: true});
	 
	var redMarker = L.ExtraMarkers.icon({
			icon: 'fa-number',
			  number: '42',
			  svg: true,
			markerColor: 'red',
			shape: 'square',
			prefix: 'fa'
		  });

        function highlightFeature(e) { 
			var layer = e.target;
            layer.openPopup();
			layer.setStyle({
				weight: 2,
				color: 'yellow',
				dashArray: '',
				fillOpacity: 0.2
			});

			if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
				//layer.bringToFront();
			}
		}	

        function resetHighlight(e) {
		  	couche_limite.resetStyle(e.target);
			
		}	
		
        var markerGroup = L.featureGroup(); 
		var markerGroup2 = L.featureGroup(); 
		
		var SweetIcon_blue = L.Icon.Label.extend({
				options: {
					iconUrl: 'icon.png',
					shadowUrl: null,
					iconSize: new L.Point(1, 1),
					iconAnchor: new L.Point(0, 0),
					labelAnchor: new L.Point(25, 0),
					// labelAnchor: new L.Point(-44, 0),
					wrapperAnchor: new L.Point(12, 13),
					labelClassName: 'leaflet-label leaflet-label-right sweet-deal-label-blue leaflet-zoom-animated leaflet-clickable',
					popupAnchor:  new L.Point(0, -16)
				}
		});
		
		
		 var couche_limite = L.geoJson(null, {
									style: function (feature) {
								       
										  return {									
											fillOpacity: 0.2,									
											fillColor: '#0deea0',											
											 color: 'black',
											// zIndex: 100,
											// pane: 'group3',									
											opacity: 1,
											weight: 0.5
											
										}; 
								      
										 
									},
									onEachFeature: function (feature, layer) { 
									
											layer.on({
														mouseover: highlightFeature,
														mouseout: resetHighlight
														
													});
													
							
			  
												
			
				   
				   var label = feature.properties.nom+': <span style="color:green;">'+feature.properties.nbre_localite+'</span>';
			   
				
			   
		
						
						
						   // layer.bindLabel(contenu_info,{direction : 'auto'});
					
					
					if(drena != ''){  	  
								L.marker(layer.getBounds().getCenter(),{
									icon: new SweetIcon_blue({iconUrl: 'assets/img/icon.png',
								labelText: '<span onclick="#" style="padding:0px;">'+label+'</span>'+blanc
						
						      })	,riseOnHover:false}).addTo(markerGroup);
						   
					} else 
					{  	  
								L.marker(layer.getBounds().getCenter(),{
									icon: new SweetIcon_blue({iconUrl: 'assets/img/icon.png',
								labelText: '<span onclick="javascript:document.getElementById(\'drena\').value=\''+feature.properties.code+'\'; select(\'drena\');" style="padding:0px;">'+label+'</span>'+blanc
						
						      })	,riseOnHover:false}).addTo(markerGroup);
							  
							  
						   
					}  
                    
                      
				  }	
								
			   
			    }).addTo(map);		
				
				
				
				var couche_localite = L.geoJson(null, {
					pointToLayer: function (feature, latlng) {
						   
					   popupOptions = {maxWidth: 260}; 
						var id = feature.properties.id;
						
						
					var popupContent = "<div style=\"max-width:400px; max-height: 200px\"><h5 style=\"border-bottom: 1px solid #eee;font-size: 1rem; color:#ed1b2c\"><i class=\"fa fa-check-square fa-fw\" style=\"color:#ed1b2c\"></i><strong>&nbsp;&nbsp;Information localité</strong></h5>"+blanc
														+"<div class=\"icon_desc\" style=\"margin-left:0px;display:block\"><span><i class=\"fa fa-arrows fa-fw\"></i> <strong>  Nom de la localité :  </strong> <span style=\"color:red\">"+feature.properties.nomloc
														 
														 +" </span></span><br><span><i class=\"fa fa-arrows fa-fw\"></i> <strong>  Sous-préfecture : </strong>"+feature.properties.nom_sp
														 +" </span><br><span><i class=\"fa fa-arrows fa-fw\"></i> <strong>  Département : </strong>"+feature.properties.departemen
														 +" </span><br><span><i class=\"fa fa-arrows fa-fw\"></i> <strong>  Région : </strong>"+feature.properties.region
														   +" </span><br><span><i class=\"fa fa-arrows fa-fw\"></i> <strong>  Nombre d'activités : </strong>"+number_format(feature.properties.nbre_activite, 0, ',', ' ')
														 
														 +" </span><br>"+blanc
														
												   +"</div>"+blanc
												   +"</div>"+blanc
												
											  +"</div>";
									  
						 // L.marker(latlng,{
											// icon: new SweetIcon_blue({iconUrl: 'assets/img/icon.png',
										// labelText: '<span onclick="" style="padding:0px;">Z.I. de '+feature.properties.nom_zone+'</span>'+blanc
									  // })	,riseOnHover:false}).bindPopup(popupContent
											// ,popupOptions).addTo(markerGroup2);
						// alert(feature.properties.nbre_entreprise);
						return	 L.marker(latlng, {icon: L.ExtraMarkers.icon({
																icon: 'fa-number',
																  number: String(feature.properties.nbre_activite),
																  svg: true,
																markerColor: 'red',
																
																shape: 'penta',
																prefix: '',
																icon: 'fa-number',
																iconColor: 'white',
																iconRotate: 0,
																extraClasses: '',
																// number: ''
															  })}).bindPopup(popupContent
											,popupOptions);
						// return   L.marker(latlng, {
											// radius: 4,
											// fillColor: '#8b0000',
											// color: "#fff",
											// weight: 1,
											// opacity: 1,
											// fillOpacity: 0.9
									// }).bindPopup(popupContent
											 // ,popupOptions);					
								
							  // L.marker(latlng, {icon: cssIcon}).addTo(markerGroup2).bindPopup(popupContent
											// ,popupOptions);
								// return  L.circleMarker(latlng, geojsonMarkerOptions2).bindPopup(popupContent,popupOptions);  
							
							
					  },
						onEachFeature: function (feature, layer) {  
						
						 
													
						}
				});
				
				
		
		map.addLayer(couche_localite);	
		couche_localite.addData(json_localite);
		
		
		map.addLayer(markerGroup); 	
		
		map.addLayer(couche_limite);	
		
		couche_limite.addData(json_limite);
		
		markerGroup.bringToFront();
		
		if(drena == '' &&  param != 'zoom'){ 	
					 map.fitBounds([
															[4.71055, -8.58415],
															[10.69565, -2.49231]
															
													 ]);
		} else {
			map.fitBounds(couche_limite.getBounds()); 
		
		}
		
		
		osmAttrib = '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
			osm = L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {maxZoom: 19,minZoom: 1, attribution: osmAttrib});
			osm2 = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {maxZoom: 19,minZoom: 1, attribution: osmAttrib});
			 var CartoDB_DarkMatter = L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', {
					attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
					subdomains: 'abcd',
					maxZoom: 19
				});
			 var googleStreets = L.tileLayer('https://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
					maxZoom: 20,
					subdomains:['mt0','mt1','mt2','mt3']
				});
				
			 var googleHybrid = L.tileLayer('https://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
					maxZoom: 20,
					subdomains:['mt0','mt1','mt2','mt3']
				});
				
			var baseMaps = {				
				  
				  "Google Map": googleStreets,
				  "Google Satellite": googleHybrid,
				  "OpenstreetMap": osm,
				  "Carto DB": CartoDB_DarkMatter
			   };	
		 
	    map.addLayer(googleStreets); 
		
		var overlayMaps = {	

               "Légende": {
					"<img style=\"max-height:35px;\" src=\"assets/images/icon_zone2.png\" alt=\"\" class=\"rounded\" />&nbsp;Localité": couche_limite
				  }		
				          
			};

        	 		 
					L.control.groupedLayers(baseMaps, overlayMaps,{collapsed:false, exclusiveGroups: ["fdgdf"]}).addTo(map);




                function select(param){  
					map.addLayer(googleStreets); 
					map.removeLayer(markerGroup);
					var drena = document.getElementById('drena').value;
					// var dpt = document.getElementById('dpt').value;
					// var spf = document.getElementById('spf').value;
					
					var composante = document.getElementById('composante').value;
					var sous_composante = document.getElementById('sous_composante').value;
					var indicateur = document.getElementById('indicateur').value;
					var activite = document.getElementById('activite').value;
				
					
					
					$('.loading').css( 'display', 'inline' ); 					
				  
					var lien = "?param="+param+"&drena="+drena
					     +"&composante="+composante+"&sous_composante="+sous_composante+"&indicateur="+indicateur+"&activite="+activite; // alert(lien);
				 
					window.location.href = lien;  
				}
									
	  			
  	
</script>




// Include Toastr library
<script src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/2.1.4/toastr.min.css"/>

<script>
    // Use Django messages to display toastr notifications

</script>


</body>
</html>