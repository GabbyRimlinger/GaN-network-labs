"""set of functions to manipulate RIPE Atlas configs"""

from dns import message


def get_ping_config(
    target: str, vp_ids: list[int], description: str = "GaN ping"
) -> dict:
    """function to define a Ping measurement before posting it"""
    return {
        "definitions": [
            {
                "target": target,
                "af": 4,
                "packets": 3,
                "size": 48,
                "tags": ["dioptra", "gan"],
                "description": f"{description}",
                "resolve_on_probe": False,
                "skip_dns_check": True,
                "include_probe_id": False,
                "type": "ping",
            }
        ],
        "probes": [
            {"value": v_id, "type": "probes", "requested": 1} for v_id in vp_ids
        ],
        "is_oneoff": True,
    }


def get_traceroute_config(
    target: str, vp_ids: list[int], description: str = "GaN Traceroute"
) -> dict:
    """function to define a Traceroute measurement before posting it"""
    return {
        "definitions": [
            {
                "target": target,
                "af": 4,
                "packets": 3,
                "first_hop": 1,
                "max_hops": 30,
                "protocol": "ICMP",
                "tags": ["dioptra", "gan"],
                "description": f"{description}",
                "resolve_on_probe": False,
                "skip_dns_check": True,
                "include_probe_id": False,
                "type": "traceroute",
            }
        ],
        "probes": [
            {"value": v_id, "type": "probes", "requested": 1} for v_id in vp_ids
        ],
        "is_oneoff": True,
    }


def get_dns_config(
    target: str,
    vp_ids: list[int],
    description: str = "GaN DNS",
    resolver_address: str = None,
) -> dict:

    params = {
        "type": "dns",
        "af": 4,
        "query_class": "IN",
        "query_type": "A",
        "query_argument": target,
        "tags": ["dioptra", "gan"],
        "description": f"{description}",
        "is_oneoff": True,
    }

    if resolver_address:
        params["resolver_address"] = resolver_address
    else:
        params["use_probe_resolver"] = True

    return {
        "definitions": [params],
        "probes": [
            {"value": v_id, "type": "probes", "requested": 1} for v_id in vp_ids
        ],
        "is_oneoff": True,
    }


def parse_dns_results(measurement_id: int) -> dict:
    """return DNS results based for a measurement"""
    pass
