import unittest
import database as db
import copy
import helpers
import config
import csv

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('43900419', 'Hugo', 'López'),
            db.Cliente('32904468', 'Roman', 'Martinez'),
            db.Cliente('42030999', 'Benjamín', 'Ibarra')
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('43900419')
        cliente_inexistente = db.Clientes.buscar('43900555')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('20099840', 'Nahuel', 'Oblitas')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, '20099840')
        self.assertEqual(nuevo_cliente.nombre, 'Nahuel')
        self.assertEqual(nuevo_cliente.apellido, 'Oblitas')

    def test_editar_cliente(self):
        cliente_a_editar = copy.copy(db.Clientes.buscar('42030999'))
        cliente_editado = db.Clientes.editar('42030999', 'Benjamín', 'Vicuña')
        self.assertEqual(cliente_a_editar.apellido, 'Ibarra')
        self.assertEqual(cliente_editado.apellido, 'Vicuña')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('32904468')
        cliente_rebuscado = db.Clientes.buscar('32904468')
        self.assertEqual(cliente_borrado.dni, '32904468')
        self.assertIsNone(cliente_rebuscado)

    def test_validar_dni(self):
        self.assertTrue(helpers.dni_valido('42881111',db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('holahola',db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('43900419',db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('42030999')
        db.Clientes.borrar('32904468')
        db.Clientes.editar('43900419', 'Hugo', 'Montoya')
    
        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline="\n") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            dni, nombre, apellido = next(reader)
    
        self.assertEqual(dni, '43900419')
        self.assertEqual(nombre, 'Hugo')
        self.assertEqual(apellido, 'Montoya')