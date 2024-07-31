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
                    bsonType: "string",
                    description: ""
                },
                mensuravel: {
                    bsonType: "string",
                    description: ""
                },
                atingivel: {
                    bsonType: "string",
                    description: ""
                },
                relevante: {
                    bsonType: "string",
                    description: ""
                },
                temporizavel: {
                    bsonType: "string",
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

db.smart.createIndex({ "usuario_id": 1 }, { unique: true })

db.smart. insertOne({
  "usuario_id": "66a99e6d63cf723dafba4cef",
  "especifica": "texto",
  "mensuravel": "texto",
  "atingivel": "texto",
  "relevante": "texto",
  "temporizavel": "texto",
  "status": "Não Iniciada",
  "criado_em": {
    "$date": "2024-10-10T03:00:00.000Z"
  },
  "atualizado_em": {
    "$date": "2024-10-10T03:00:00.000Z"
  },
  "deletado": false
})