from deviceutils import GPSLocation, GPSLocationLocationProvider

LOCATION_DB = {
    "US": {
        "newyorkcity": GPSLocation(
            longitude=-74.005973,
            latitude=40.712775,
            altitude=10.440,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        ),
        "losangeles": GPSLocation(
            longitude=-118.243685,
            latitude=34.052234,
            altitude=86.854,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        ),
        "chicago": GPSLocation(
            longitude=-87.629798,
            latitude=41.878114,
            altitude=181.513,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        ),
        "houston": GPSLocation(
            longitude=-95.369803,
            latitude=29.760427,
            altitude=14.562,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        ),
        "washington": GPSLocation(
            longitude=-77.036871,
            latitude=38.907192,
            altitude=22.015,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        ),
        "philadelphia": GPSLocation(
            longitude=-75.165222,
            latitude=39.952584,
            altitude=14.336,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        ),
        "miami": GPSLocation(
            longitude=-80.191790,
            latitude=25.761680,
            altitude=0.537,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        )
    },
    "MX": {
        "mexicocity": GPSLocation(
            longitude=-99.133208,
            latitude=19.432608,
            altitude=2229.729,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        )
    },
    "CA": {
        "torronto": GPSLocation(
            longitude=-79.383184,
            latitude=43.653226,
            altitude=91.723,
            provider=GPSLocationLocationProvider.LocationProvider_NONE,
        )
    }
}
