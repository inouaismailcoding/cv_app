$(document).ready(function(){
/////////////////////////////////////////////////////////////
/* START  CRUD PHOTO PROFILE*/
// ON CREE UN EVENEMENT LORSQU'ON CHOISI UNE PHOTO DE PROFILE ET L'AFFICHER AVANT DE L'ENREGISTRER DANS LA BASE DE DONNEES
$(document).on('change','#id_photo',(event)=>{
    event.preventDefault();
    var input = event.target;
    var preview = document.getElementById('preview');

  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      preview.setAttribute('src', e.target.result);
      //preview.style.display = 'block';
    }

    reader.readAsDataURL(input.files[0]);
  }
});
// Fonction pour afficher chaque image CHOISI

// EVENEMENT POUR ENREGISTRER ET MODIFIER UNE PHOTO DE PROFIL
$('#upload_image').submit(function(e){
    e.preventDefault();
    var form=$('#upload_image');
    formData=new FormData()
    file =$('#id_photo')[0].files[0]
    formData.append('photo',file)
    token=form.serialize().split('=')
    formData.append(token[0],token[1]);
    $.ajax({
        url:'upload_image',
        type:'POST',
        data:formData,
        processData:false,
        contentType:false,
        success:function(r){
          
           $('#description_image').slideToggle();
        }
    })
});

// On enregistre le formulaire des INFO PERSO
$(document).on('click','#btn-info-perso-form',function(event) {
    event.preventDefault();
    var form = $("#info-perso-form");
    $.ajax({
        //type: form.attr('method'),
        //url: 'test',
        type:'POST',
        url: 'info_perso',
        data: form.serialize()+'&createInfoPerso=createInfoPerso',

        success: function(response) {
            console.log(response);
            console.log(response.info[0]);
            var info=response.info[0];
            form[0].reset()
            $('#id_nom').val(info.nom)
            $('#id_prenom').val(info.prenom)
            $('#id_email').val(info.email)
            $('#id_telephone').val(info.telephone)
            $('#id_address').val(info.address)
            $('#birth_date').val(info.birth_date)
            $('#id_status').val(info.status)
            $('#header_content_section').slideToggle();
        }
    });
});

/* END CRUD PHOTO PROFILE  */
///////////////////////////////////////////////////////////////////////////



///////////////////////////////////////////////////////////////////////////
/* START CRUD PROFILE */
// ON ENREGISTREMENT L'EVENEMENT CREATION OU MODIFICATION 
// DES INFORMATIONS SUR LE PROFIL 
$('#profile_form').submit((e)=>{
    e.preventDefault();
    var form=$('#profile_form')
    $.ajax({
        url:'profile_info',
        type:'POST',
        data:form.serialize()+'&createProfileInfo=createProfileInfo',
        success:(r)=>{
            var profile= r.profile[0];
            $('#id_titre').val(profile.titre)
            $('#id_profile').val(profile.profile)
            $('#description_profil').slideToggle();
        }
    });
});

// EVENEMENT POUR MODIFIER UN ENREGISTREMENT
$('#profile_edit_form').submit((e)=>{
    e.preventDefault();
    var form=$('#profile_edit_form')
    console.log(form.serialize())
    $.ajax({
        url:'profile_info',
        type:'POST',
        data:form.serialize()+'&createProfileInfo=createProfileInfo',
        success:(r)=>{
            console.log(r)
            var profile= r.profile[0];
            $('#id_titre').val(profile.titre)
            $('#id_profile').val(profile.profile)

            $('#description_profil').slideToggle();
        }
    }); 
});
/* END CRUD PROFILE  */
/////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////
/* DEBUT CRUD FORMATION  */
  // EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR LA FORMATION
  $(document).on('click','#btn_create_formation_info',(e)=>{
    e.preventDefault();
    var form= $('#info-formation-form');
    var divResponse=document.getElementById('formation_info_data')
    console.log(divResponse)
    // On lance la requete ajax pour recuperer le formulaire
    $.ajax({
        url:'formation_info',
        type:'POST',
        data:form.serialize()+"&createFormationInfo=createFormationInfo",
        success:(r)=>{
            formations=r.formations
            divResponse.innerHTML="";
            divResponse.innerHTML=printFormations(formations);
            form[0].reset()
            $('#staticFormationFormModal').modal('hide');
        }
    });
});

// EVENEMENT LORQU'ON CLICK SUR LE FONT EDIT D'UNE FORMATION
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR LA FORMATION
$(document).on('click','.btn_edit_formation',(e)=>{
    e.preventDefault();
    id_formation=e.currentTarget.dataset.id;
    let form =$('#edit-info-formation-form');
   $.ajax({
    url:'formation_info',
    type:'GET',
    data:'id_formation='+id_formation+'&fetchOnFormation=fetchOnFormation',
    success:(r)=>{ 
        data=r.formation[0]
        labelModal=document.getElementById('staticEditFormationFormModalLabel');
        // ON insert les données dans le formulaires
        
        labelModal.innerText='MODIFICATION FORMATION N°:'+data.id;
        $('#id_diplome_edit').val(data.diplome);
        $('#id_ecole_edit').val(data.ecole);
        $('#id_ville_edit').val(data.ville);
        $('#id_debut_edit').val(data.debut);
        $('#id_fin_edit').val(data.fin);
        $('#id_description_edit').val(data.description);
        $('#idEditFormationInfo').val(data.id)
    }
});
});

// EVENEMENT POUR ENREGISTRE LA MODIFICATION DANS LA TABLE
$(document).on('click','#btn_edit_formation_info',(e)=>{
    e.preventDefault();
    form=$('#edit-info-formation-form');
    let myId=$('#idEditFormationInfo').val();
    var divResponse=document.getElementById('formation_info_data');
    $.ajax({
        url:'formation_info',
        type:'POST',
        data:form.serialize()+"&editFormationInfo=editFormationInfo",
        success:(r)=>{
            formations=r.formations
            divResponse.innerHTML="";
            divResponse.innerHTML=printFormations(formations)
            $('#staticEditFormationFormModal').modal('hide');
        }
    });

});

// EVENEMENT POUR AFFICHER UN ENREGISTREMENT A SUPPRIMER (FORMATION)
$(document).on('click','.btn_delete_formation',function(e){
    e.preventDefault();
    myId=e.currentTarget.dataset.id;
    labelModal=document.getElementById('deleteFormationFormModalLabel');
    $('#id_delete_formation_info').val(myId);
    
    // ON insert les données dans le formulaires       
    labelModal.innerText='SUPPRIMER FORMATION N°:'+myId;
    
});

// EVENEMENT POUR SUPPRIMER UN ENREGISTREMENT
$(document).on('click','#btn_delete_formation_info',function(e){
    e.preventDefault();
    id_formation=$('#id_delete_formation_info').val();
    var divResponse=document.getElementById('formation_info_data');

   $.ajax({
    url:'formation_info',
    type:'GET',
    data:"id_formation="+id_formation+"&deleteOnFormation=deleteOnFormation",
    success:(r)=>{
      formations=r.formations
      divResponse.innerHTML="";
      divResponse.innerHTML=printFormations(formations)
          $('#deleteFormationFormModal').modal('hide');
          
    }
  });
    
});


// FONCTION POUR AFFICHER LES DONNEES dDE LA FORMATION
function printFormations(data) {
    content="";
            data.forEach((e)=>{
            content+="<div class='card'><div class='d-flex'>";
            content+="<div class='formation_info_data col-9 mx-2 me-3'>";
            content+="<h6 class='card-header'>"+e.debut+" - "+e.fin+"</h6>";
            content+="<span>"+e.ecole+" situé a "+e.ville+"</span><br><small>"+e.description+"</small></div>";
            content+="<div class='col-3 mt-4'>";  
            content+="<a type='button' class='fa fa-edit mx-1 me-1 btn_edit_formation' data-id='"+e.id+"' data-bs-toggle='modal' data-bs-target='#staticEditFormationFormModal'></a>"; 
            content+="<a type='button' class='fa fa-trash text-danger mx-1 me-1 btn_delete_formation' data-id='"+e.id+"'  data-bs-toggle='modal' data-bs-target='#deleteFormationFormModal'></a>"; 
            content+="</div></div></div>";               
       
            });
            return content;
}

/* END CRUD FORMATION  */
////////////////////////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////////////////
/* START CRUD EXPERIENCE INFORMATION  */
  // EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR L'EXPERIENCE PROFESSIONNELLE
  $(document).on('click','#btn_create_experience_info',(e)=>{
    e.preventDefault();
    var form= $('#info-experience-form');
    // On lance la requete ajax pour recuperer le formulaire
    $.ajax({
        url:'experience_info',
        type:'POST',
        data:form.serialize()+"&createExperienceInfo=createExperienceInfo",
        success:(r)=>{
            experiences=r.experiences
            printExperienceDiv(experiences);
            form[0].reset()
            $('#staticExperienceFormModal').modal('hide');
        }
    });
});

// EVENEMENT LORQU'ON CLICK SUR LE FONT EDIT D'UNE FORMATION
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR LA FORMATION
$(document).on('click','.btn_edit_experience',(e)=>{
    e.preventDefault();
    id_experience=e.currentTarget.dataset.id;
    let form =$('#edit-info-experience-form');
    $.ajax({
        url:'experience_info',
        type:'GET',
        data:'id_experience='+id_experience+'&fetchOnExperience=fetchOnExperience',
        success:(r)=>{ 
            data=r.experience[0]
            labelModal=document.getElementById('staticEditExperienceFormModalLabel');
            // ON insert les données dans le formulaires
            
            labelModal.innerText='MODIFICATION EXPERIENCE N°:'+data.id;
            $('#id_titre_experience_edit').val(data.titre);
            $('#id_entreprise_experience_edit').val(data.entreprise);
            $('#id_ville_experience_edit').val(data.ville);
            $('#id_debut_experience_edit').val(data.debut);
            $('#id_fin_experience_edit').val(data.fin);
            $('#id_description_experience_edit').val(data.description);
            $('#idEditExperienceInfo').val(data.id)
        }
    })
});

// EVENEMENT POUR ENREGISTRE LA MODIFICATION DANS LA TABLE
$(document).on('click','#btn_edit_experience_info',(e)=>{
    e.preventDefault();
    form=$('#edit-info-experience-form');
    let myId=$('#idEditExperienceInfo').val();
    var divResponse=document.getElementById('experience_info_data')
    $.ajax({
        url:'experience_info',
        type:'POST',
        data:form.serialize()+"&editExperienceInfo=editExperienceInfo",
        success:(r)=>{
          experiences=r.experiences;
            printExperienceDiv(experiences);
            $('#staticEditExperienceFormModal').modal('hide');
        }
    })

});

// EVENEMENT POUR AFFICHER UN ENREGISTREMENT A SUPPRIMER (FORMATION)
$(document).on('click','.btn_delete_experience',function(e){
    e.preventDefault();
    myId=e.currentTarget.dataset.id;
    labelModal=document.getElementById('deleteExperienceFormModalLabel');
    $('#id_delete_experience_info').val(myId);
    
    // ON insert les données dans le formulaires       
    labelModal.innerText='SUPPRIMER EXPERIENCE N°:'+myId;
    
});

// EVENEMENT POUR SUPPRIMER UN ENREGISTREMENT
$(document).on('click','#btn_delete_experience_info',function(e){
    e.preventDefault();
    
    id_experience=$('#id_delete_experience_info').val();
    var divResponse=document.getElementById('experience_info_data');

   $.ajax({
    url:'experience_info',
    type:'GET',
    data:"id_experience="+id_experience+"&deleteOnExperience=deleteOnExperience",
    success:(r)=>{
      experiences=r.experiences
      printExperienceDiv(experiences);
      $('#deleteExperienceFormModal').modal('hide');
          
    }
  });
    
});

// FUnction Pour afficher le contenu de la formation du sur la divResponse
function printExperienceDiv(data){
  var divResponse=document.getElementById('experience_info_data');
  divResponse.innerHTML="";
  content="";
  data.forEach((e)=>{
  content+="<div class='card'><div class='d-flex'>";
  content+="<div class='experience_info_data col-9 mx-2 me-3'>";
  content+="<p class='card-header'><span class='text-info'>"+e.debut+" - "+e.fin+"</span><br>";
  content+="<b class='text-primary'>"+e.titre+"</b><br>"
  content+="<span>"+e.entreprise+" situé a "+e.ville+"</span><br><small>"+e.description+"</small></p></div>";
  content+="<div class='col-3 mt-4'>";  
  content+="<a href='' type='button' class='fa fa-edit mx-1 me-1 btn_edit_experience' data-id='"+e.id+"' data-bs-toggle='modal' data-bs-target='#staticEditExperienceFormModal'></a>"; 
  content+="<a href='' type='button' class='fa fa-trash text-danger mx-1 me-1 btn_delete_experience' data-id='"+e.id+"' data-bs-toggle='modal' data-bs-target='#deleteExperienceFormModal'></a>"; 
  content+="</div></div></div>";               

  });
  
  divResponse.innerHTML=content;
}

/* END CRUD EXPERIENCE */
/////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////
/* START CRUD COMPETENCE  */
/* PROCEDURE ENREGISTREMENT COMPETENCE INFORMATION  */

// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR L'EXPERIENCE PROFESSIONNELLE
$(document).on('click','#btn_create_competence_info',(e)=>{
    e.preventDefault();
    var form= $('#info-competence-form');
    // On lance la requete ajax pour recuperer le formulaire
    $.ajax({
        url:'competence_info',
        type:'POST',
        data:form.serialize()+"&createCompetenceInfo=createCompetenceInfo",
        success:(r)=>{
            competences=r.competences
            printCompetenceDiv(competences);
            form[0].reset()
            $('#staticCompetenceFormModal').modal('hide');
        }
    });
});

// EVENEMENT LORQU'ON CLICK SUR LE FONT EDIT D'UNE FORMATION
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR LA FORMATION
$(document).on('click','.btn_edit_competence',(e)=>{
    e.preventDefault();
    id_competence=e.currentTarget.dataset.id;
    let form =$('#edit-info-competence-form');
    $.ajax({
        url:'competence_info',
        type:'GET',
        data:'id_competence='+id_competence+'&fetchOnCompetence=fetchOnCompetence',
        success:(r)=>{ 
            data=r.competence[0]
            labelModal=document.getElementById('staticEditCompetenceFormModalLabel');
            // ON insert les données dans le formulaires
            
            labelModal.innerText='MODIFICATION EXPERIENCE N°:'+data.id;
            $('#id_titre_competence_edit').val(data.competence);
            $('#id_niveau_competence_edit').val(data.niveau);
           
            $('#idEditCompetenceInfo').val(data.id)
        }
    })
});

// EVENEMENT POUR ENREGISTRE LA MODIFICATION DANS LA TABLE
$(document).on('click','#btn_edit_competence_info',(e)=>{
    e.preventDefault();
    form=$('#edit-info-competence-form');
    let myId=$('#idEditCompetenceInfo').val();
    var divResponse=document.getElementById('competence_info_data')
    $.ajax({
        url:'competence_info',
        type:'POST',
        data:form.serialize()+"&editCompetenceInfo=editCompetenceInfo",
        success:(r)=>{
            competences=r.competences;
            printCompetenceDiv(competences);
            $('#staticEditCompetenceFormModal').modal('hide');
        }
    })

});

// EVENEMENT POUR AFFICHER UN ENREGISTREMENT A SUPPRIMER (FORMATION)
$(document).on('click','.btn_delete_competence',function(e){
    e.preventDefault();
    myId=e.currentTarget.dataset.id;
    labelModal=document.getElementById('deleteCompetenceFormModalLabel');
    $('#id_delete_competence_info').val(myId);
    
    // ON insert les données dans le formulaires       
    labelModal.innerText='SUPPRIMER COMPETENCE N°:'+myId;
    
});

// EVENEMENT POUR SUPPRIMER UN ENREGISTREMENT
$(document).on('click','#btn_delete_competence_info',function(e){
    e.preventDefault();
    id_competence=$('#id_delete_competence_info').val();
    var divResponse=document.getElementById('competence_info_data');
   $.ajax({
    url:'competence_info',
    type:'GET',
    data:"id_competence="+id_competence+"&deleteOnCompetence=deleteOnCompetence",
    success:(r)=>{
        competences=r.competences
      printCompetenceDiv(competences);
      $('#deleteCompetenceFormModal').modal('hide');
          
    }
  });
    
});

// FUnction Pour afficher le contenu de la formation du sur la divResponse
function printCompetenceDiv(data){
  var divResponse=document.getElementById('competence_info_data');
  divResponse.innerHTML="";
  content="";
  data.forEach((e)=>{
  content+="<div class='d-flex'>";
  content+="<div class='competence_data col-9 mx-2 me-3'>";
  content+="<h6 class='card-header'>"+e.competence+"</h6>";
  content+="<div class='progress'><div class='progress-bar w-50 bg-success' role='progressbar' aria-valuenow='50' aria-valuemin='0' aria-valuemax='100'></div>"
  content+="</div></div><div class='col-3 mt-4'>";

  content+="<a href='' type='button' class='fa fa-edit mx-1 me-1 btn_edit_competence' data-id='"+e.id+"' data-bs-target='#staticEditCompetenceFormModal' data-bs-toggle='modal'></a>"; 
  content+="<a href='' type='button' class='fa fa-trash text-danger mx-1 me-1 btn_delete_competence' data-id='"+e.id+"'  data-bs-target='#deleteCompetenceFormModal' data-bs-toggle='modal'></a>"; 
  content+="</div></div>";               

  });
  
  divResponse.innerHTML=content;
}

/* END CRUD COMPETENCE INFO */
//////////////////////////////////////////////////////////////////////////


/////////////////////////////////////////////////////////////////////////
/* START  CRUD LANGUE INFORMATION */
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR L'EXPERIENCE PROFESSIONNELLE
$(document).on('click','#btn_create_langue_info',(e)=>{
    e.preventDefault();
    var form= $('#info-langue-form');
    // On lance la requete ajax pour recuperer le formulaire
    $.ajax({
        url:'langue_info',
        type:'POST',
        data:form.serialize()+"&createLangueInfo=createLangueInfo",
        success:(r)=>{
            langues=r.langues
            printLangueDiv(langues);
            form[0].reset()
            $('#staticLangueFormModal').modal('hide');
        }
    });
});

// EVENEMENT LORQU'ON CLICK SUR LE FONT EDIT D'UNE FORMATION
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR LA FORMATION
$(document).on('click','.btn_edit_langue',(e)=>{
    e.preventDefault();
    id_langue=e.currentTarget.dataset.id;
    let form =$('#edit-info-langue-form');
    $.ajax({
        url:'langue_info',
        type:'GET',
        data:'id_langue='+id_langue+'&fetchOnLangue=fetchOnLangue',
        success:(r)=>{ 
            data=r.langue[0]
            labelModal=document.getElementById('staticEditLangueFormModalLabel');
            // ON insert les données dans le formulaires
            
            labelModal.innerText='MODIFICATION LANGUE N°:'+data.id;
            $('#id_titre_langue_edit').val(data.langue);
            $('#id_niveau_langue_edit').val(data.niveau);
           
            $('#idEditLangueInfo').val(data.id)
        }
    })
});

// EVENEMENT POUR ENREGISTRE LA MODIFICATION DANS LA TABLE
$(document).on('click','#btn_edit_langue_info',(e)=>{
    e.preventDefault();
    form=$('#edit-info-langue-form');
    let myId=$('#idEditLangueInfo').val();
    var divResponse=document.getElementById('langue_info_data')
    $.ajax({
        url:'langue_info',
        type:'POST',
        data:form.serialize()+"&editLangueInfo=editLangueInfo",
        success:(r)=>{
          langues=r.langues;
            printLangueDiv(langues);
            $('#staticEditLangueFormModal').modal('hide');
        }
    })

});

// EVENEMENT POUR AFFICHER UN ENREGISTREMENT A SUPPRIMER (FORMATION)
$(document).on('click','.btn_delete_langue',function(e){
    e.preventDefault();
    myId=e.currentTarget.dataset.id;
    labelModal=document.getElementById('deleteLangueFormModalLabel');
    $('#id_delete_langue_info').val(myId);
    
    // ON insert les données dans le formulaires       
    labelModal.innerText='SUPPRIMER LANGUE N°:'+myId;
    
});

// EVENEMENT POUR SUPPRIMER UN ENREGISTREMENT
$(document).on('click','#btn_delete_langue_info',function(e){
    e.preventDefault(); 
    id_langue=$('#id_delete_langue_info').val();
    var divResponse=document.getElementById('langue_info_data');
   $.ajax({
    url:'langue_info',
    type:'GET',
    data:"id_langue="+id_langue+"&deleteOnLangue=deleteOnLangue",
    success:(r)=>{
        langues=r.langues
      printLangueDiv(langues);
      $('#deleteLangueFormModal').modal('hide');
          
    }
  });
    
});

// FUnction Pour afficher le contenu de la formation du sur la divResponse
function printLangueDiv(data){
  var divResponse=document.getElementById('langue_info_data');
  divResponse.innerHTML="";
  content="";
  data.forEach((e)=>{
  content+="<div class='d-flex'>";
  content+="<div class='langue_data col-9 mx-2 me-3'>";
  content+="<h6 class='card-header'>"+e.langue+"</h6>";
  content+="<div class='progress'><div class='progress-bar w-50 bg-success' role='progressbar' aria-valuenow='50' aria-valuemin='0' aria-valuemax='100'></div>"
  content+="</div></div><div class='col-3 mt-4'>";

  content+="<a href='' type='button' class='fa fa-edit mx-1 me-1 btn_edit_langue' data-id='"+e.id+"' data-bs-target='#staticEditLangueFormModal' data-bs-toggle='modal'></a>"; 
  content+="<a href='' type='button' class='fa fa-trash text-danger mx-1 me-1 btn_delete_langue' data-id='"+e.id+"' data-bs-target='#deleteLangueFormModal' data-bs-toggle='modal'></a>"; 
  content+="</div></div>";               

  });
  
  divResponse.innerHTML=content;
}

/* END CRUD LANGUE */
////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR L'EXPERIENCE PROFESSIONNELLE
$(document).on('click','#btn_create_interet_info',(e)=>{
    e.preventDefault();
    var form= $('#info-interet-form');
    // On lance la requete ajax pour recuperer le formulaire
    $.ajax({
        url:'centre_interet_info',
        type:'POST',
        data:form.serialize()+"&createInteretInfo=createInteretInfo",
        success:(r)=>{
            interets=r.interets

            printInteretDiv(interets);
            form[0].reset()
            $('#staticInteretFormModal').modal('hide');
        }
    });
});

// EVENEMENT LORQU'ON CLICK SUR LE FONT EDIT D'UNE FORMATION
// EVENEMENT LORS DE LA CREATION D'UNE NOUVELLE INFO SUR LA FORMATION
$(document).on('click','.btn_edit_interet',(e)=>{
    e.preventDefault();
    id_interet=e.currentTarget.dataset.id;
    let form =$('#edit-info-interet-form');
    $.ajax({
        url:'centre_interet_info',
        type:'GET',
        data:'id_interet='+id_interet+'&fetchOnInteret=fetchOnInteret',
        success:(r)=>{ 
            data=r.interet[0]
            labelModal=document.getElementById('staticEditInteretFormModalLabel');
            // ON insert les données dans le formulaires
            
            labelModal.innerText='MODIFICATION LANGUE N°:'+data.id;
            $('#id_titre_interet_edit').val(data.titre);
           
            $('#idEditInteretInfo').val(data.id)
        }
    })
});

// EVENEMENT POUR ENREGISTRE LA MODIFICATION DANS LA TABLE
$(document).on('click','#btn_edit_interet_info',(e)=>{
    e.preventDefault();
    form=$('#edit-info-interet-form');
    let myId=$('#idEditInteretInfo').val();
    var divResponse=document.getElementById('interet_info_data')
    $.ajax({
        url:'centre_interet_info',
        type:'POST',
        data:form.serialize()+"&editInteretInfo=editInteretInfo",
        success:(r)=>{
          interets=r.interets;
            printInteretDiv(interets);
            $('#staticEditInteretFormModal').modal('hide');
        }
    })

});

// EVENEMENT POUR AFFICHER UN ENREGISTREMENT A SUPPRIMER (FORMATION)
$(document).on('click','.btn_delete_interet',function(e){
    e.preventDefault();
    myId=e.currentTarget.dataset.id;
    labelModal=document.getElementById('deleteInteretFormModalLabel');
    $('#id_delete_interet_info').val(myId);
    
    // ON insert les données dans le formulaires       
    labelModal.innerText='SUPPRIMER CENTRE D\'INTERET N°:'+myId;
    
});

// EVENEMENT POUR SUPPRIMER UN ENREGISTREMENT
$(document).on('click','#btn_delete_interet_info',function(e){
    e.preventDefault();
    
    id_interet=$('#id_delete_interet_info').val();
    var divResponse=document.getElementById('interet_info_data');

   $.ajax({
    url:'centre_interet_info',
    type:'GET',
    data:"id_interet="+id_interet+"&deleteOnInteret=deleteOnInteret",
    success:(r)=>{
        interets=r.interets
      printInteretDiv(interets);
      $('#deleteInteretFormModal').modal('hide');
          
    }
  });
    
});

// FUnction Pour afficher le contenu de la formation du sur la divResponse
function printInteretDiv(data){
  var divResponse=document.getElementById('centreInteret_info_data');
  divResponse.innerHTML="";
  content="";
  data.forEach((e)=>{
  content+="<div class='d-flex'>";
  content+="<div class='langue_data col-9 mx-2 me-3'>";
  content+="<h6 class='card-header'>"+e.titre+"</h6></div>";
  content+="<div class='col-3 mt-4'>";

  content+="<a href='' type='button' class='fa fa-edit mx-1 me-1 btn_edit_interet' data-id='"+e.id+"' data-bs-target='#staticEditInteretFormModal' data-bs-toggle='modal'></a>"; 
  content+="<a href='' type='button' class='fa fa-trash text-danger mx-1 me-1 btn_delete_interet' data-id='"+e.id+"' data-bs-target='#deleteInteretFormModal' data-bs-toggle='modal'></a>"; 
  content+="</div></div>";               

  });
  
  divResponse.innerHTML=content;
}
/* END CRUD CENTRE INTERET INFORMATION   */
/////////////////////////////////////////////////////////////////////////////////////////


//$('#description_cours').hide();
$('#description_centreInteret').hide();
$('#description_image').hide();
$('#description_langue').hide();
$('#description_competence').hide();
$('#description_experience').hide();
$('#description_formation').hide();
$('#description_profil').hide();
$('#header_content_section').hide();

document.getElementById('headerInfoPersonnel').onclick = (e) => {
    $('#header_content_section').slideToggle();
}
document.getElementById('headerImage').onclick = (e) => {
    $('#description_image').slideToggle();
}
document.getElementById('headerProfil').onclick = (e) => {
    $('#description_profil').slideToggle();
}
document.getElementById('headerFormation').onclick = (e) => {
    $('#description_formation').slideToggle();
}
document.getElementById('headerExperience').onclick = (e) => {
    $('#description_experience').slideToggle()
}
document.getElementById('headerCompetence').onclick = (e) => {
    $('#description_competence').slideToggle()
}
document.getElementById('headerLangue').onclick = (e) => {
    $('#description_langue').slideToggle()
}
document.getElementById('headerCentreInteret').onclick = (e) => {
    $('#description_centreInteret').slideToggle()
}
});