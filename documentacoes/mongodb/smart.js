print('Executando smart.js');
db = db.getSiblingDB('SMARTify');

db.createCollection("smart", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "usuario_id", "especifica", "mensuravel", "atingivel", "relevante", "temporizavel", "status", "criado_em", "atualizado_em", "deletado"],
            properties: {
                _id:{
                    bsonType: "objectId"
                },
                usuario_id: {
                    bsonType: "string",
                    description: ""
                },
                especifica: {
                    bsonType: ["string", "null"],
                    description: ""
                },
                mensuravel: {
                    bsonType: ["string", "null"],
                    description: ""
                },
                atingivel: {
                    bsonType: ["string", "null"],
                    description: ""
                },
                relevante: {
                    bsonType: ["string", "null"],
                    description: ""
                },
                temporizavel: {
                    bsonType: ["string", "null"],
                    description: ""
                },
                status: {
                    bsonType: "string",
                    enum:["Não Iniciada", "Iniciada", "Concluída"],
                    description: ""
                },
                criado_em: {
                    bsonType: "date",
                    description: ""
                },
                atualizado_em: {
                    bsonType: "date",
                    description: ""
                },
                deletado: {
                    bsonType: "bool",
                    description: ""
                }
            }
        }
    }
});