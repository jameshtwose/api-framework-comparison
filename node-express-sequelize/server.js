const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');
const { Sequelize, DataTypes, Model } = require('sequelize');

const sequelize = new Sequelize(
    'postgres', // database
    'postgres', // username
    'changeme', // password
    {
        host: 'localhost',
        dialect: 'postgres',
        define: {
            freezeTableName: true,
            timestamps: false
        }
    }
)

// date_received = Column(DateTime)
// product = Column(String)
// sub_product = Column(String)
// issue = Column(String)
// sub_issue = Column(String)
// consumer_complaint_narrative = Column(String)
// company_public_response = Column(String)
// company = Column(String)
// state = Column(String)
// zip_code = Column(String)
// tags = Column(String)
// consumer_consent_provided = Column(String)
// submitted_via = Column(String)
// date_sent_to_company = Column(DateTime)
// company_response_to_consumer = Column(String)
// timely_response = Column(Boolean)
// consumer_disputed = Column(Boolean)
// complaint_id = Column(Integer, primary_key=True)

class ComplaintsTable extends Model {}
ComplaintsTable.init({
    date_received: {
        type: DataTypes.DATE
    },
    product: {
        type: DataTypes.STRING
    },
    sub_product: {
        type: DataTypes.STRING
    },
    issue: {
        type: DataTypes.STRING
    },
    sub_issue: {
        type: DataTypes.STRING
    },
    consumer_complaint_narrative: {
        type: DataTypes.STRING
    },
    company_public_response: {
        type: DataTypes.STRING
    },
    company: {
        type: DataTypes.STRING
    },
    state: {
        type: DataTypes.STRING
    },
    zip_code: {
        type: DataTypes.STRING
    },
    tags: {
        type: DataTypes.STRING
    },
    consumer_consent_provided: {
        type: DataTypes.STRING
    },
    submitted_via: {
        type: DataTypes.STRING
    },
    date_sent_to_company: {
        type: DataTypes.DATE
    },
    company_response_to_consumer: {
        type: DataTypes.STRING
    },
    timely_response: {
        type: DataTypes.BOOLEAN
    },
    consumer_disputed: {
        type: DataTypes.BOOLEAN
    },
    complaint_id: {
        type: DataTypes.INTEGER,
        primaryKey: true
    }
}, {
    sequelize,
    modelName: 'complaints_table',
    tableName: 'complaints_table',
});

const app = express();

var corsOptions = {
    origin: 'http://localhost:8082'
};

app.use(cors(corsOptions));

// parse requests of content-type - application/json
app.use(bodyParser.json());
// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({
    extended: true
}));

/**
 * @openapi
 * /:
 *   get:
 *     description: Welcome to the Node Express Sequelize API.
 *     responses:
 *       200:
 *         description: Returns a mysterious string.
 */
app.get('/', (req, res) => {
    res.json({
        message: 'Welcome to the Node Express Sequelize API.'
    });
});

/**
 * @openapi
 * /complaints:
 *   get:
 *     description: Get X rows from the complaints table.
 *     responses:
 *       200:
 *         description: Returns a list of complaints.
 *     parameters:
 *       - in: query
 *         name: limit
 *         schema: 
 *           type: integer
 *         required: false
 *         description: Number of rows to return.
 *         default: 10
 * 
 */
app.get('/complaints', (req, res) => {
    const limit = parseInt(req.query.limit) || 10;
    const complaints = ComplaintsTable.findAll({
        limit: limit
    }).then(complaints => {
        res.json(complaints);
    });
}); 

// curl -X GET "http://localhost:8082/complaints/1" -H "accept: application/json"

// set port, listen for requests
const PORT = process.env.PORT || 8082;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});

const options = {
    definition: {
        openapi: '3.0.0',
        info: {
            title: 'Node Express Sequelize API',
            version: '1.0.0',
        },
    },
    apis: ['./*.js'], // files containing annotations as above
};

const openapiSpecification = swaggerJsdoc(options);
app.use('/docs', swaggerUi.serve, swaggerUi.setup(openapiSpecification));
