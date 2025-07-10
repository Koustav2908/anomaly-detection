features: list[tuple[str, ...]] = [
    (
        "Duration",
        "Length of the connections (in seconds).",
        "Valid range is (0 - 10,000).",
    ),
    (
        "Protocol Type",
        "Type of Protocol used to make the connection (eg. TCP, UDP, or ICMP).",
    ),
    (
        "Service Type",
        "Network Service on the destination (eg. TELNET, HTTP, etc).",
    ),
    (
        "Source Bytes",
        "Number of data bytes from source to destination.",
        "Valid range is (0 - 1,500,000).",
    ),
    (
        "Destination Bytes",
        "Number of data bytes from destination to source.",
        "Valid range is (0 - 1,500,000).",
    ),
    (
        "Logged In",
        "Yes if successfully logged in, No otherwise.",
    ),
    (
        "Count",
        "Number of connections to the same host as the current connection in the past two seconds.",
        "Valid range is (0 - 511).",
    ),
    (
        "Service Count",
        "Number of connections to the same service as the current connection in the past two seconds.",
        "Valid range is (0 - 511).",
    ),
    (
        "Destination Host Count",
        "Number of connections to the same destination host as the current connection in the past 100 connections.",
        "Valid range is (0 - 255).",
    ),
    (
        "Destination Host and Service Count",
        "Number of connections to the same destination host and same service as the current connection in the past 100 connections.",
        "Valid range is (0 - 255).",
    ),
]
