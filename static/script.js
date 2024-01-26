/*$(document).ready(function () {
    $(document).on('click','#new_invoice',(e)=>{
        e.preventDefault();
        alert('oaky')
    });

    // POUR LA GESTION DE LA PAGE SALE //
        // Requete Lorsqu'on choisi une categorie
        $(document).on("change", "#selected_category", (e) => {
            e.preventDefault();
            selectedCategory = document.getElementById("selected_category");
      
            $.ajax({
              type: "GET",
              url: "",
              data: { showArticle: "fecthAll" },
              success: (r) => {
                let listArticles = r["data"]["articles"];
                myArticles = listArticles.filter((article) => {
                  return article.category_id == selectedCategory.value;
                });
                selectArticle = document.getElementById("selected_article");
                deleteOption(selectArticle);
                opt = document.createElement("option");
                opt.value = 0;
                opt.text = "";
                selectArticle.add(opt);
                myArticles.forEach((e) => {
                  option = document.createElement("option");
                  option.value = e.id;
                  option.text = e.article;
                  selectArticle.add(option);
                });
              },
            });
          });
      
          // // Requete Lorsqu'on choisi un Article
          $(document).on("change", "#selected_article", (e) => {
            e.preventDefault();
            selectedArticle = document.getElementById("selected_article");
            selectedArticleText =
              selectArticle.options[selectArticle.selectedIndex].text;
            selectEmballage = document.getElementById("selected_emballage");
      
            $.ajax({
              type: "GET",
              url: "",
              data: { showArticle: "fecthAll" },
              success: (r) => {
                // On filtre d'abord la liste des articles
                let listArt = r["data"]["articles"];
                myArt = listArt.filter((art) => {
                  return art.article == selectedArticleText;
                });
      
                // On enregistre les id des emballages dans une liste emballage id
                embId = [];
                myArt.forEach((e) => {
                  embId.push(e.emballage_id);
                });
                let listEmb = r["data"]["emballages"];
      
                myEmb = listEmb.filter((emb) => {
                  return embId.includes(emb.id);
                });
                deleteOption(selectEmballage);
                opt = document.createElement("option");
                opt.value = 0;
                opt.text = "";
                selectEmballage.add(opt);
                myEmb.forEach((e) => {
                  option = document.createElement("option");
                  option.value = e.id;
                  option.text = e.emballage;
                  selectEmballage.add(option);
                });
              },
            });
          });
      
          // // Requete Lorsqu'on choisi un emballage
          $(document).on("change", "#selected_emballage", (e) => {
            e.preventDefault();
            selectedArticle = document.getElementById("selected_article");
            selectedArticleText =
              selectArticle.options[selectArticle.selectedIndex].text;
            selectedEmballage = document.getElementById("selected_emballage");
            selectedCategory = document.getElementById("selected_category");
      
            $.ajax({
              type: "GET",
              url: "",
              data: { showArticle: "fecthAll" },
              success: (r) => {
                // On filtre d'abord la liste des articles
                let listArt = r["data"]["articles"];
                myArt = listArt.filter((art) => {
                  return (
                    art.article == selectedArticleText &&
                    art.emballage_id == selectedEmballage.value &&
                    art.category_id == selectedCategory.value
                  );
                });
                // On recupere le prix unitaire
                document.getElementById("price").value = myArt[0].price_unit;
              },
            });
          });
      
          // Ajouter element de facture dans table
          $(document).on("click", "#add_element_invoice", (e) => {
            e.preventDefault();
            addToTable();
          });
      
          // Ajouter element de facture dans table
          $(document).on("input", "#quantity", (e) => {
            e.preventDefault();
            var quantity = document.getElementById("quantity").value;
      
            if (typeof parseInt(quantity) == "number") {
              var price = document.getElementById("price").value;
              price = parseInt(price);
              document.getElementById("amount").value = quantity * price;
            }
            if (typeof quantity !== "number" || quantity == "") {
              document.getElementById("amount").value = 0;
            }
          });
      
          // function qui supprime toutes les options d'un select
          function deleteOption(select) {
            while (select.firstChild) {
              select.removeChild(select.firstChild);
            }
          }
      
          // Function pour ajouter les donnees du formulaire dans la table
          function addToTable() {
            var category = document.getElementById("selected_category");
            var categoryText = category.options[category.selectedIndex].text;
            var article = document.getElementById("selected_article");
            var articleText = article.options[article.selectedIndex].text;
            var emballage = document.getElementById("selected_emballage");
            var emballageText = emballage.options[emballage.selectedIndex].text;
            var quantity = document.getElementById("quantity").value;
            quantity = parseInt(quantity);
            var price = document.getElementById("price").value;
            price = parseInt(price);
            var amount = document.getElementById("amount").value;
      
            if (typeof quantity == "number") {
              // creer une nouvelle ligne dans la table
              if (categoryText != "" && articleText != "" && emballageText != "") {
                var table = document.getElementById("myTableInvoice");
                var row = table.insertRow(-1);
                var cell_category = row.insertCell(0);
                var cell_article = row.insertCell(1);
                var cell_emballage = row.insertCell(2);
                var cell_quantity = row.insertCell(3);
                var cell_price = row.insertCell(4);
                var cell_amount = row.insertCell(5);
      
                cell_category.innerHTML = categoryText;
                cell_article.innerHTML = articleText;
                cell_emballage.innerHTML = emballageText;
                cell_quantity.innerHTML = quantity;
                cell_price.innerHTML = price;
                cell_amount.innerHTML = price * quantity;
      
                // On reinitialiase tout les champs
      
                document.getElementById("selected_category").value = "";
                document.getElementById("selected_article").value = "";
                document.getElementById("selected_emballage").value = "";
                document.getElementById("quantity").value = "";
                document.getElementById("price").value = "";
                document.getElementById("amount").value = "";
              } else {
                alert("Veuillez remplir tout les champs !!");
              }
            } else {
              alert("le cchamps quantity doit conteir uniquement les nombres !!");
            }
          }

          // FIN DE LA GESTION PAGE SALE 
    

});
*/