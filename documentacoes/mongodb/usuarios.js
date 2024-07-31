db.createCollection("usuarios", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["_id", "nome", "sobrenome", "criado_em", "atualizado_em", "deletado"],
            properties: {
                _id:{
                    bsonType: "objectId"
                },
                nome: {
                    bsonType: "string",
                    maxLength: 20,
                    description: "Informe corretamente o nome do usuário"
                },
                sobrenome: {
                    bsonType: "string",
                    maxLength: 50,
                    description: "Informe corretamente o sobrenome do usuário"
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


//db.usuarios.createIndex({ "token": 1 }, { unique: true })


db.usuarios.insertOne({
  "nome": "Kauê",
  "sobrenome": "Sousa",
  "criado_em": {
    "$date": "2024-10-10T03:00:00.000Z"
  },
  "atualizado_em": {
    "$date": "2024-10-10T03:00:00.000Z"
  },
  "deletado": false
})