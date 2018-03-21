import unittest
from solution import Panda, PandaSocialNetwork


class TestPanda(unittest.TestCase):
    def setUp(self):
        self.panda = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_name_and_email_and_gender(self):
        self.assertEqual(self.panda.name(), "Ivo")
        self.assertEqual(self.panda.email(), "ivo@pandamail.com")
        self.assertEqual(self.panda.gender(), "male")

    def test_is_male_and_is_female(self):
        self.assertFalse(self.panda.isFemale())
        self.assertTrue(self.panda.isMale())

    def test_pandas_are_equal(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        rado = Panda("Ivo", "ivo@pandamail.com", "female")

        self.assertFalse(self.panda == rado)
        self.assertTrue(self.panda == ivo)


class TestSocialNetwork(unittest.TestCase):
    def setUp(self):
        self.network = PandaSocialNetwork()
        self.ivo = Panda("Ivo", "ivo@pandamail.com", "male")

    def test_name_email_gender_hash(self):
        self.assertEqual(self.ivo.name(), "Ivo")
        self.assertEqual(self.ivo.email(), "ivo@pandamail.com")
        self.assertEqual(self.ivo.gender(), "male")

    def test_add_and_has_panda_in_network(self):
        self.network.add_panda(self.ivo)

        self.assertTrue(self.network.has_panda(self.ivo))

    def test_has_panda_when_panda_not_in_network(self):
        self.assertFalse(self.network.has_panda(self.ivo))

    def test_make_and_are_friends(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.network.make_friends(self.ivo, rado)

        self.assertTrue(self.network.are_friends(self.ivo, rado))

    def test_friends_of_panda(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavli", "pavlin@pandamail.com", "male")
        maria = Panda("maria", "maria@pandamail.com", "female")

        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(self.ivo, pavli)
        self.network.make_friends(self.ivo, maria)

        expected = [rado, pavli, maria]
        self.assertEqual(self.network.friends_of(self.ivo), expected)

    def test_friends_of_panda_when_panda_not_in_network(self):
        self.assertFalse(self.network.friends_of(self.ivo))

    @unittest.skip('May not be implemented')
    def test_connection_level_between_two_pandas(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavli", "pavlin@pandamail.com", "male")
        maria = Panda("maria", "maria@pandamail.com", "female")
        gogo = Panda("Gogo", "gogo@pandamail.com", "male")

        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(pavli, gogo)
        self.network.make_friends(rado, pavli)
        self.network.make_friends(pavli, maria)

        self.assertEqual(self.network.connection_level(self.ivo, rado), 1)
        self.assertEqual(self.network.connection_level(self.ivo, pavli), 2)
        self.assertEqual(self.network.connection_level(self.ivo, maria), 3)

    @unittest.skip('May not be implemented')
    def test_are_connected(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavli", "pavlin@pandamail.com", "male")
        maria = Panda("maria", "maria@pandamail.com", "female")

        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(rado, pavli)

        self.assertTrue(self.network.are_connected(self.ivo, pavli))
        self.assertFalse(self.network.are_connected(self.ivo, maria))

    @unittest.skip('May not be implemented')
    def test_connection_level_when_panda_has_no_friends(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.network.add_panda(rado)
        self.network.add_panda(self.ivo)

        self.assertEqual(self.network.connection_level(self.ivo, rado), -1)

    @unittest.skip('May not be implemented')
    def test_connection_level_when_panda_not_in_network(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        self.network.add_panda(rado)

        self.assertFalse(self.network.connection_level(self.ivo, rado))

    @unittest.skip('May not be implemented')
    def test_how_many_genders_in_network(self):
        rado = Panda("Rado", "rado@pandamail.com", "male")
        pavli = Panda("Pavlin", "pavlin@pandamail.com", "male")
        alex = Panda("Alex", "alex@pandamail.com", "male")
        maria = Panda("maria", "maria@pandamail.com", "female")
        slavyana = Panda("Slavyana", "slavyana@pandamail.com", "female")

        self.network.make_friends(self.ivo, rado)
        self.network.make_friends(pavli, slavyana)
        self.network.make_friends(rado, pavli)
        self.network.make_friends(pavli, maria)
        self.network.make_friends(self.ivo, pavli)
        self.network.make_friends(maria, alex)

        self.assertEqual(self.network.how_many_gender_in_network(
                                    1, self.ivo, "male"), 2)
        self.assertEqual(self.network.how_many_gender_in_network(
                                    1, self.ivo, "female"), 0)
        self.assertEqual(self.network.how_many_gender_in_network(
                                    2, self.ivo, "female"), 2)
        self.assertEqual(self.network.how_many_gender_in_network(
                                    25, self.ivo, "male"), 3)

if __name__ == '__main__':
    unittest.main()
