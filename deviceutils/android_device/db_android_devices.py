from deviceutils import AndroidDevice, Locale, AndroidDeviceVersion, AndroidDeviceBuildData, ScreenData, SIMCard, \
	SIMCardIMEI, MAC, CPUData, CPUDataArchitecture

DB_DEVICES = {
	"oneplus5": AndroidDevice(
		locale=Locale(language="en", country_i_s_o="US"),
		version=AndroidDeviceVersion.V9_0,
		build=AndroidDeviceBuildData(
			device="OnePlus5",
			manufacturer="OnePlus",
			model="ONEPLUS A5000",
			product="OnePlus5",
			id="PKQ1.180716.001",
			type="user",
			tags="release-keys",
			incremental_version="2002242003"
		),
		screen=ScreenData(
			density=420,
			resolution_horizontal=1080,
			resolution_vertical=1920
		),
		sim_slots=[
			SIMCard(imei=SIMCardIMEI(t_a_c="86463003")),
			SIMCard(imei=SIMCardIMEI(t_a_c="86463003"))
		],
		mac_address=MAC(o_u_i="A091A2"),
		cpu=CPUData(arch=CPUDataArchitecture.ARM64, abi_list=["arm64-v8a", "armeabi-v7a", "armeabi"])
	),
	"oneplus7t": AndroidDevice(
		locale=Locale(language="en", country_i_s_o="US"),
		version=AndroidDeviceVersion.V10_0,
		build=AndroidDeviceBuildData(
			device="OnePlus7T",
			manufacturer="OnePlus",
			model="HD1905",
			product="OnePlus7T",
			id="QKQ1.190716.003",
			type="user",
			tags="release-keys",
			incremental_version="2101212100"
		),
		screen=ScreenData(
			density=420,
			resolution_horizontal=1080,
			resolution_vertical=2400
		),
		sim_slots=[
			SIMCard(imei=SIMCardIMEI(t_a_c="86789104")),
			SIMCard(imei=SIMCardIMEI(t_a_c="86789104"))
		],
		mac_address=MAC(o_u_i="A091A2"),
		cpu=CPUData(arch=CPUDataArchitecture.ARM64, abi_list=["arm64-v8a", "armeabi-v7a", "armeabi"])
	),
	"oneplus9pro": AndroidDevice(
		locale=Locale(language="en", country_i_s_o="US"),
		version=AndroidDeviceVersion.V11_0,
		build=AndroidDeviceBuildData(
			device="OnePlus9Pro",
			manufacturer="OnePlus",
			model="LE2125",
			product="OnePlus9Pro",
			id="PKQ1.180716.001",
			type="user",
			tags="release-keys",
			incremental_version="2105290043"
		),
		screen=ScreenData(
			density=600,
			resolution_horizontal=1440,
			resolution_vertical=3216
		),
		sim_slots=[
			SIMCard(imei=SIMCardIMEI(t_a_c="86381505"))
		],
		mac_address=MAC(o_u_i="A091A2"),
		cpu=CPUData(arch=CPUDataArchitecture.ARM64, abi_list=["arm64-v8a", "armeabi-v7a", "armeabi"])
	),
}

AVAILABLE_DEVICES = [
	"oneplus5",
	"oneplus7t",
	"oneplus9pro",
]
