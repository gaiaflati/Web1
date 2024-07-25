const express = require('express');
const cors = require('cors')
const app = express();
app.use(cors());
var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"
app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress +
':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));


//pagina di invio della form
app.get('/formRegistrazione', (req, res) => {
    console.log("Mi hai chiesto la form di registrazione");
    res.sendFile("formSemplice.html", { root: './htdoc' });
    });

//pagina di gestione dei dati della form se il metodo è GET
app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname);
    response="<html>Buona serata" + req.query.fname;
    if (req.query.fsesso == "1")
        response += "<br>Sei un maschio"
    else
        response += "<br>Sei una femmina"
    response += "La tua città" +req.query.fcomune
    response += "<br>Ti voglio bene </html>";
    res.send(response);
    });

app.get('/sendFile', (req, res) => {
    console.log("Mi hai chiesto la form di invio del file");
    res.sendFile("sendfile.html", { root: './htdoc' });
    });