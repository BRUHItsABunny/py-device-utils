from deviceutils import GpsLocation, GpsLocationLocationProvider

LOCATION_DB = {
    "US": {
        "newyorkcity": GpsLocation(
            longitude=-74.005973,
            latitude=40.712775,
            altitude=10.440,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        ),
        "losangeles": GpsLocation(
            longitude=-118.243685,
            latitude=34.052234,
            altitude=86.854,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        ),
        "chicago": GpsLocation(
            longitude=-87.629798,
            latitude=41.878114,
            altitude=181.513,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        ),
        "houston": GpsLocation(
            longitude=-95.369803,
            latitude=29.760427,
            altitude=14.562,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        ),
        "washington": GpsLocation(
            longitude=-77.036871,
            latitude=38.907192,
            altitude=22.015,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        ),
        "philadelphia": GpsLocation(
            longitude=-75.165222,
            latitude=39.952584,
            altitude=14.336,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        ),
        "miami": GpsLocation(
            longitude=-80.191790,
            latitude=25.761680,
            altitude=0.537,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        )
    },
    "MX": {
        "mexicocity": GpsLocation(
            longitude=-99.133208,
            latitude=19.432608,
            altitude=2229.729,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        )
    },
    "CA": {
        "torronto": GpsLocation(
            longitude=-79.383184,
            latitude=43.653226,
            altitude=91.723,
            provider=GpsLocationLocationProvider.LocationProvider_NONE,
        )
    }
}
