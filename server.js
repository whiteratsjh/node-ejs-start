const mExpress = require('express');
const vApp = mExpress();

vApp.set('views', __dirname + '/views');
vApp.set('view engine', 'ejs');
vApp.engine('html', require('ejs').renderFile);

vApp.use(mExpress.static('public'));


vApp.get('/', function (pReq, pRes) {
    pRes.render("main");
});

vApp.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});