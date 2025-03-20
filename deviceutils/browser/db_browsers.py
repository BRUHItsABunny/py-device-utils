from deviceutils import Browser, BrowserTlsFingerprint, BrowserTlsFingerprintProtocolVersion, \
    BrowserTlsFingerprintEllipticCurvePointFormat, BrowserTlsFingerprintEllipticCurve
from typing import Any, Dict, Optional
import random
DB_BROWSERS = {
    "brave": {
        "1.50.114": Browser(
            version="1.50.114",
            name="brave",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/112.0.0.0 Safari/537.36",
            brand_header="\"Chromium\";v=\"112\", \"Brave\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
            tls_fingerprint=BrowserTlsFingerprint(
                version=BrowserTlsFingerprintProtocolVersion.TLS1_2,
                cipher_suites=[
                    4865, 4866, 4867, 49195, 49199, 49196, 49200, 52393, 52392, 49171, 49172, 156, 157, 47, 53
                ],
                extensions=[
                    27, 16, 35, 11, 17513, 43, 13, 5, 23, 0, 18, 51, 10, 65281, 45, 21
                ],
                elliptic_curves=[
                    BrowserTlsFingerprintEllipticCurve(29),
                    BrowserTlsFingerprintEllipticCurve(23),
                    BrowserTlsFingerprintEllipticCurve(24)
                ],
                elliptic_curve_point_formats=[
                    BrowserTlsFingerprintEllipticCurvePointFormat(0)
                ]
            )
        ),
    },
    "chrome": {
        "112.0.5615.50": Browser(
            version="112.0.5615.50",
            name="chrome",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/112.0.0.0 Safari/537.36",
            brand_header="\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
            tls_fingerprint=BrowserTlsFingerprint(
                version=BrowserTlsFingerprintProtocolVersion.TLS1_2,
                cipher_suites=[
                    4865, 4866, 4867, 49195, 49199, 49196, 49200, 52393, 52392, 49171, 49172, 156, 157, 47, 53
                ],
                extensions=[
                    27, 16, 35, 11, 17513, 43, 13, 5, 23, 0, 18, 51, 10, 65281, 45, 21
                ],
                elliptic_curves=[
                    BrowserTlsFingerprintEllipticCurve(29),
                    BrowserTlsFingerprintEllipticCurve(23),
                    BrowserTlsFingerprintEllipticCurve(24)
                ],
                elliptic_curve_point_formats=[
                    BrowserTlsFingerprintEllipticCurvePointFormat(0)
                ]
            )
        ),
    },
    "firefox": {
        "111.0.1": Browser(
            version="111.0.1",
            name="firefox",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
            tls_fingerprint=BrowserTlsFingerprint(
                version=BrowserTlsFingerprintProtocolVersion.TLS1_2,
                cipher_suites=[
                    4865, 4867, 4866, 49195, 49199, 52393, 52392, 49196, 49200, 49162, 49161, 49171, 49172, 156, 157, 47, 53
                ],
                extensions=[
                    0, 23, 65281, 10, 11, 16, 5, 34, 51, 43, 13, 45, 28, 41
                ],
                elliptic_curves=[
                    BrowserTlsFingerprintEllipticCurve(29),
                    BrowserTlsFingerprintEllipticCurve(23),
                    BrowserTlsFingerprintEllipticCurve(24),
                    BrowserTlsFingerprintEllipticCurve(256),
                    BrowserTlsFingerprintEllipticCurve(257),
                ],
                elliptic_curve_point_formats=[
                    BrowserTlsFingerprintEllipticCurvePointFormat(0)
                ]
            )
        ),
    },
    "opera": {
        "97.0.4719.56": Browser(
            version="97.0.4719.56",
            name="opera",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0",
            brand_header="\"Chromium\";v=\"112\", \"Not_A Brand\";v=\"24\", \"Opera\";v=\"98\"",
            tls_fingerprint=BrowserTlsFingerprint(
                version=BrowserTlsFingerprintProtocolVersion.TLS1_2,
                cipher_suites=[
                    4865, 4866, 4867, 49195, 49199, 49196, 49200, 52393, 52392, 49171, 49172, 156, 157, 47, 53
                ],
                extensions=[
                    13, 16, 17513, 35, 65281, 43, 0, 10, 45, 23, 11, 27, 5, 51, 18, 21, 41,29, 23, 24
                ],
                elliptic_curves=[
                    BrowserTlsFingerprintEllipticCurve(29),
                    BrowserTlsFingerprintEllipticCurve(23),
                    BrowserTlsFingerprintEllipticCurve(24)
                ],
                elliptic_curve_point_formats=[
                    BrowserTlsFingerprintEllipticCurvePointFormat(0)
                ]
            )
        ),
    },
    "safari": {
        "18615.1.26.11.22": Browser(
            version="18615.1.26.11.22",
            name="safari",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            tls_fingerprint=BrowserTlsFingerprint(
                version=BrowserTlsFingerprintProtocolVersion.TLS1_2,
                cipher_suites=[
                    4865, 4866, 4867, 49195, 49199, 49196, 49200, 52393, 52392, 49171, 49172, 156, 157, 47, 53
                ],
                extensions=[
                    27, 16, 35, 11, 17513, 43, 13, 5, 23, 0, 18, 51, 10, 65281, 45, 21
                ],
                elliptic_curves=[
                    BrowserTlsFingerprintEllipticCurve(29),
                    BrowserTlsFingerprintEllipticCurve(23),
                    BrowserTlsFingerprintEllipticCurve(24)
                ],
                elliptic_curve_point_formats=[
                    BrowserTlsFingerprintEllipticCurvePointFormat(0)
                ]
            )
        ),
    }
}


AVAILABLE_BROWSERS = [
    "brave",
    "chrome",
    "firefox",
    "opera",
    "safari"
]

def get_random_key(collection: Dict[str, Any]) -> str:
    keys = list(collection.keys())
    return random.choice(keys)


def random_browser_version_by_name(name: str) -> Optional[Browser]:
    if name in DB_BROWSERS:
        return DB_BROWSERS[name][get_random_key(DB_BROWSERS[name])]
    return None


def random_browser() -> Browser:
    browser_name = get_random_key(DB_BROWSERS)
    return DB_BROWSERS[browser_name][get_random_key(DB_BROWSERS[browser_name])]