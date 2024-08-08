from datetime import date

import pytest
from astroplan import Observer
from astropy.coordinates import SkyCoord

from scopes.merits import airmass
from scopes.scheduler_components import (
    Instrument,
    Merit,
    Night,
    Observation,
    Overheads,
    Program,
    Target,
)


@pytest.fixture
def example_observer():
    return Observer.at_site("lasilla")


@pytest.fixture
def example_night(example_observer):
    return Night(
        night_date=date(2024, 8, 1),
        observations_within="astronomical",
        observer=example_observer,
    )


@pytest.fixture
def example_instrument():
    return Instrument(
        name="Example Spectrograph",
        instrument_type="Spectrograph",
        plot_color="#FF5733",
    )


@pytest.fixture
def example_program(example_instrument):
    return Program(
        progID="Prog123",
        instrument=example_instrument,
        priority=1,
        time_share_allocated=0.3,
    )


@pytest.fixture
def example_merit():
    return Merit(
        name="Example Merit",
        func=airmass,
        merit_type="veto",
        parameters={"limit": 1.8},
    )


@pytest.fixture
def example_custom_merit_func():
    def custom_merit_function(observation, example_param):
        """Example merit function."""
        return 1.0

    return custom_merit_function


@pytest.fixture
def example_coords():
    return SkyCoord(ra=150.0, dec=-20.0, unit="deg")


@pytest.fixture
def example_target(example_program, example_coords):
    target = Target(
        name="Example Target",
        program=example_program,
        coords=example_coords,
        priority=1,
        comment="This is a test target",
    )
    return target


@pytest.fixture
def example_observation(example_target):
    example_target.add_merit(merit=example_merit)
    return Observation(target=example_target, exposure_time=600.0)


@pytest.fixture
def example_overheads():
    return Overheads(slew_rate_az=0.5, slew_rate_alt=0.4, cable_wrap_angle=180.0)
