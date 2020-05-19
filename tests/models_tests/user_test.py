from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == [
            '+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []

    def test_full_name(self):
        assert self.chuck.full_name() == "Chuck Norris"
        assert self.elvis.full_name() == "Elvis Presley"
        assert self.justin.full_name() == "Justin Bieber"

    def test_get_tier(self):
        assert self.chuck.get_tier() == "Carbon"
        assert self.elvis.get_tier() == "Carbon"
        assert self.justin.get_tier() == "Silver"

    def test_get_points_and_dollars(self):
        assert self.chuck.get_points_and_dollars()["points"] == 5000

    def test_is_below_tier(self):
        assert self.chuck.is_below_tier("Platinum") == True
        assert self.chuck.is_below_tier("Gold") == True
        assert self.chuck.is_below_tier("Silver") == True
        assert self.chuck.is_below_tier("Bronze") == True
        assert self.chuck.is_below_tier("Carbon") == False

        assert self.justin.is_below_tier("Platinum") == True
        assert self.justin.is_below_tier("Gold") == True
        assert self.justin.is_below_tier("Silver") == False
        assert self.justin.is_below_tier("Bronze") == False
        assert self.justin.is_below_tier("Carbon") == False
