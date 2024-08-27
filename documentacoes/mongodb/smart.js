use SMARTify

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

// db.smart. insertOne({
//   "usuario_id": "66a99e6d63cf723dafba4cef",
//   "especifica": "texto",
//   "mensuravel": "texto",
//   "atingivel": "texto",
//   "relevante": "texto",
//   "temporizavel": "texto",
//   "status": "Não Iniciada",
//   "criado_em": {
//     "$date": "2024-10-10T03:00:00.000Z"
//   },
//   "atualizado_em": {
//     "$date": "2024-10-10T03:00:00.000Z"
//   },
//   "deletado": false
// })