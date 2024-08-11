"""Wrapper class for OSBee's API.

OSBee API is a bit unusual; OSBeeAPI class wraps the OSBee API to collect and simplify the
protocol's oddities.  For more info, see:

https://github.com/OpenSprinkler/OSBeeWiFi-Firmware/blob/master/docs/firmware1.0.0/OSBeeAPI1.0.0.pdf
"""

import aiohttp
import logging
from threading import Lock
from typing import Awaitable, Callable, Optional, Dict, Any

_LOGGER = logging.getLogger(__name__)


class OSBeeAPI:
    """aiohttp facade for API requests to OSB Hub device."""

    _host: str
    _jc_cache: Optional[Dict[str, Any]]
    _max_runtime: int
    _session: aiohttp.ClientSession
    _token: str

    def __init__(
        self, host: str, max_runtime: int, token: str, session: aiohttp.ClientSession
    ) -> None:
        """Create an OSBeeAPI by offering a host, and an async session to get there."""
        self._host = host
        self._jc_cache = None
        _LOGGER.warning("type of timeout/max_runtime is %s", type(max_runtime))
        self._max_runtime = max_runtime
        self._session = session
        self.lock = Lock()
        self._token = token
        _LOGGER.warning(
            "created OSBeeAPI at %s max_runtime %s (%s)",
            self._host,
            self._max_runtime,
            type(self._max_runtime),
        )

    async def fetch_data(self, index) -> str:
        """Get raw device state from the OSBee Hub via API.  No authentication yet considered.

        Essentially,the unprotected result of hitting your OSBee with GET http://{IP}/jc with a
        text/json content-type (OSBee-1.0.0; firmware-1.0.2 seems to offer application.json) and
        contains the status of the device.
        """

        _LOGGER.debug("Fetch_data from %s with index %s", self._host, index)
        async with self._session.get(f"http://{self._host}/jc") as jc_request:
            if jc_request.status == 401:
                raise AuthenticationError(
                    "Unable to authenticate with the OSBee API (HTTP/401)"
                )

            if jc_request.status == 500:
                raise ServiceUnavailableError(
                    "The service is currently unavailable (HTTP/500)"
                )

            if jc_request.status == 429:
                raise TooManyRequestsError(
                    "Too many requests have been made to the API (HTTP/429)"
                )

            if jc_request.status != 200:
                raise Exception(  # pylint: disable=broad-exception-raised
                    f"Error connecting to OSBee Hub (HTTP/{jc_request.status or 'None'})"
                )

            jc_body = await jc_request.json(content_type=None)
            if len(jc_body) == 0:
                raise Exception(  # pylint: disable=broad-exception-raised
                    "The server returned a zero-length body, not a valid response"
                )

            self._jc_cache = jc_body
            return jc_body  # the resulting structure has no conventional "data" element, just raw JSON

    async def async_turn_off(self, zone_id) -> str:
        """Async entry point to deactivate the valve/relay for the zone.

        Based on the current status of the device, this method creates a new determination of
        active valves as bit-fields, and pushes the new list of active valves as a new manual
        program running those valves, replacing the current manual program.  This has the effect of
        turning off the given valve.
        """

        if not self._jc_cache:
            # too soon: status not yet pulled somehow
            pass
        else:
            # use jc_cache[zbits] to avoid WET variables
            with self.lock:
                current = self._jc_cache["zbits"]
                _LOGGER.debug("In turn_off: current state is %s", current)
                mask = 1 << zone_id
                self._jc_cache["zbits"] = current & ~mask
            _LOGGER.debug("In turn_off: new state is %s", self._jc_cache["zbits"])

        return await self.async_apply_state()

    async def async_turn_on(self, zone_id) -> str:
        """Async entry point to activate the valve/relay for the zone.

        Based on the current status of the device, this method creates a new determination of
        active valves as bit-fields, and pushes the new list of active valves as a new manual
        program running those valves, replacing the current manual program.  This has the effect of
        turning off the given valve.
        """

        if not self._jc_cache:
            # too soon: status not yet pulled somehow
            pass
        else:
            # use jc_cache[zbits] to avoid WET variables
            with self.lock:
                current = self._jc_cache["zbits"]
                _LOGGER.debug("In turn_on: current state is %s", current)
                mask = 1 << zone_id
                self._jc_cache["zbits"] = current | mask
            _LOGGER.debug("In turn_on: new state is %s", self._jc_cache["zbits"])

        return await self.async_apply_state()

    async def async_apply_state(self) -> str:
        """Async entry point to set active zones.

        Mostly used internally by async_turn_off(...), async_turn_on(...), this method applies the
        desired state by generating the GET http://{IP}/cc to shut off all valves, or
        http://{IP}/rp to run a manual program of the given valves.
        """

        # type-shuffle: assign a non-optional dict to satisfy type-hint
        if self._jc_cache:
            new_bitz: int = self._jc_cache["zbits"]  # bits: which valves are open
        else:
            raise Exception(  # pylint: disable=broad-exception-raised
                "INTERNAL: async_apply_state is supposed to be gated from _jc_cache==None"
            )

        # firmware-1.0.0, part 11: Run Program (rp): http://devip/rp?dkey=xxx&pid=x&...
        # ...
        # When pid=77 (ASCII value of 'M'), this command starts a manual program.  You will need to supply two additional parameters:
        #  - zbits=x: zone enable bits (e.g. zbits=4 means zone 3 will turn on)
        #  - dur=x: duration (in seconds)
        #  - Example: pid=77&zbits=3&dur=300 turns on zones 1 and 2 manually for 5 minutes

        if new_bitz == 0:  # on zbits==0, we need to actually reset
            url = f"http://{self._host}/cc?dkey={self._token}&reset=1"
        else:
            url = f"http://{self._host}/rp?dkey={self._token}&pid=77&zbits={new_bitz}&dur={self._max_runtime}"

        async with self._session.get(url) as rp_request:
            if rp_request.status == 401:
                raise AuthenticationError(
                    "Unable to authenticate with the OSBee API (HTTP/401)"
                )

            if rp_request.status == 500:
                raise ServiceUnavailableError(
                    "The service is currently unavailable (HTTP/500)"
                )

            if rp_request.status == 429:
                raise TooManyRequestsError(
                    "Too many requests have been made to the API (HTTP/429)"
                )

            if rp_request.status != 200:
                raise Exception(  # pylint: disable=broad-exception-raised
                    f"Error connecting to OSBee Hub (HTTP/{rp_request.status or 'None'})"
                )

        _LOGGER.debug("In turn_off: finished")
        return await self.fetch_data(0)


class AuthenticationError(Exception):
    """Wrapper to allow try/except blocks to catch errors due to authentication that we don't have (HTTP code 401)."""


class ServiceUnavailableError(Exception):
    """Wrapper to allow try/except blocks to catch errors due to offline API (HTTP code 500)."""


class TooManyRequestsError(Exception):
    """Wrapper to allow try/except blocks to catch errors due to overloading an API (HTTP code 429)."""
