"""helper function for performing GaNs lab"""


def get_prefix_from_ip(ip_addr: str, netmask_len: int = 24) -> str:
    """return CIDR format of prefix based on len"""
    return ".".join(ip_addr.split(".")[:-1]) + f".0/{netmask_len}"
