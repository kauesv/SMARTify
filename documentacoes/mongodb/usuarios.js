print('Executando usuarios.js');
db = db.getSiblingDB('SMARTify');

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

db.usuarios.createIndex({ nome: 1, sobrenome: 1 },{ unique: true });