

pag11= """<!DOCTYPE html>
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <style>
        body {
                background-color: aquamarine;
                text-align: center;
                }
    </style>
    </head>
    <body>
        <center>
          <div class="container">
                <div class="row" style= "padding 5%;">
"""
pag12=""" <div class="col-sm">
                        <div class="card" style="width: 18rem;">
             
                            <img src="img/img_dog.jpg" class="card-img-top" alt="..." width="=500" height="200"> 
                            <div class="card-body">
                            <h5 class="card-title"> Il mio cane Bob</h5>
                            <p class="card-text">Clicca qui per aprire il sito di Arcaplanet</p>
                            <a href=""https://www.arcaplanet.it/?utm_source=google&utm_medium=cpc&utm_campaign=Arcaplanet_SEA_Brand-Pure_1.pp&gad_source=1&gclid=EAIaIQobChMItLbMkMSphwMVjfF5BB1TYwPZEAAYASAAEgI6UfD_BwE&gclsrc=aw.ds" target="blank_" " class="btn btn-primary"> Vai al sito!</a>
                            </div>
                        </div>
                    </div>
"""
pag12_="""          <div class="col-sm">
                        <div class="card" style="width: 18rem;">
             
                            <img src="img/img_cat.jpg" class="card-img-top" alt="..." width="=500" height="200"> 
                            <div class="card-body">
                            <h5 class="card-title"> Il mio gatto Jack</h5>
                            <p class="card-text">Clicca qui per aprire il sito di Arcaplanet</p>
                            <a href=""https://www.arcaplanet.it/?utm_source=google&utm_medium=cpc&utm_campaign=Arcaplanet_SEA_Brand-Pure_1.pp&gad_source=1&gclid=EAIaIQobChMItLbMkMSphwMVjfF5BB1TYwPZEAAYASAAEgI6UfD_BwE&gclsrc=aw.ds" target="blank_" " class="btn btn-primary"> Vai al sito!</a>
                            </div>
                        </div>
                    </div>
"""
pag13= """   </div>
              </div>




        </center>
    </body>
</html>
"""

N=12
with open ("pippo.html", "w") as index:
    index.write(f"{pag11}")
    for i in range(N):
        index.write(f"{pag12}")
        index.write(f"{pag12_}")

    index.write(f"{pag13}")