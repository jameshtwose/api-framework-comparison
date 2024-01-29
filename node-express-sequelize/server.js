const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');

// var options = {
//     swaggerOptions: {
//       url: 'http://petstore.swagger.io/v2/swagger.json'
//     }
//   }

const app = express();

var corsOptions = {
    origin: 'http://localhost:8082'
};

app.use(cors(corsOptions));

// app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(null, options));
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

// parse requests of content-type - application/json
app.use(bodyParser.json());
// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({
    extended: true
}));

// simple route
app.get('/', (req, res) => {
    res.json({
        message: 'Welcome to the Node Express Sequelize API.'
    });
});

// set port, listen for requests
const PORT = process.env.PORT || 8082;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});