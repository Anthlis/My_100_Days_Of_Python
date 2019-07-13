from typing import List, Optional

# noinspection PyPackageRequirements
from data import session_factory
# noinspection PyPackageRequirements
from models.move import Move
# noinspection PyPackageRequirements
from models.player import Player
# noinspection PyPackageRequirements
from models.roll import Roll



def show_flights() -> List[Flight]:
    session = session_factory.create_session()

    flights = list(session.query(Flight).all())
    session.close()
    return flights