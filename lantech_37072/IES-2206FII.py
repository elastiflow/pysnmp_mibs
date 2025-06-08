# SNMP MIB module (IES-2206FII) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/lantech_37072/IES-2206FII.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:14:08 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 internet,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "internet",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

contact = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1)
)
if mibBuilder.loadTexts:
    contact.setRevisions(
        ("1906-04-20 00:00",)
    )


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class PortList(OctetString):
    """Custom type PortList based on OctetString"""



# TEXTUAL-CONVENTIONS



class DisplayString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Switches_ObjectIdentity = ObjectIdentity
switches = _Switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0)
)
_ManagedSwitch_ObjectIdentity = ObjectIdentity
managedSwitch = _ManagedSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0)
)
_Ies2206fii_ObjectIdentity = ObjectIdentity
ies2206fii = _Ies2206fii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4)
)
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1)
)


class _SystemName_Type(DisplayString):
    """Custom type systemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SystemName_Type.__name__ = "DisplayString"
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1, 1),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("current")


class _SystemLocation_Type(DisplayString):
    """Custom type systemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SystemLocation_Type.__name__ = "DisplayString"
_SystemLocation_Object = MibScalar
systemLocation = _SystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1, 2),
    _SystemLocation_Type()
)
systemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLocation.setStatus("current")


class _SystemContact_Type(DisplayString):
    """Custom type systemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SystemContact_Type.__name__ = "DisplayString"
_SystemContact_Object = MibScalar
systemContact = _SystemContact_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1, 3),
    _SystemContact_Type()
)
systemContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemContact.setStatus("current")


class _SystemDescr_Type(DisplayString):
    """Custom type systemDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SystemDescr_Type.__name__ = "DisplayString"
_SystemDescr_Object = MibScalar
systemDescr = _SystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1, 4),
    _SystemDescr_Type()
)
systemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDescr.setStatus("current")


class _SystemFwVer_Type(DisplayString):
    """Custom type systemFwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SystemFwVer_Type.__name__ = "DisplayString"
_SystemFwVer_Object = MibScalar
systemFwVer = _SystemFwVer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1, 5),
    _SystemFwVer_Type()
)
systemFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFwVer.setStatus("current")
_SystemMacAddress_Type = MacAddress
_SystemMacAddress_Object = MibScalar
systemMacAddress = _SystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 1, 6),
    _SystemMacAddress_Type()
)
systemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMacAddress.setStatus("current")
_BasicSetting_ObjectIdentity = ObjectIdentity
basicSetting = _BasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2)
)
_SwitchSetting_ObjectIdentity = ObjectIdentity
switchSetting = _SwitchSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 1)
)


class _SwitchSettingSystemName_Type(DisplayString):
    """Custom type switchSettingSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchSettingSystemName_Type.__name__ = "DisplayString"
_SwitchSettingSystemName_Object = MibScalar
switchSettingSystemName = _SwitchSettingSystemName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 1, 1),
    _SwitchSettingSystemName_Type()
)
switchSettingSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingSystemName.setStatus("current")


class _SwitchSettingSystemLocation_Type(DisplayString):
    """Custom type switchSettingSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchSettingSystemLocation_Type.__name__ = "DisplayString"
_SwitchSettingSystemLocation_Object = MibScalar
switchSettingSystemLocation = _SwitchSettingSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 1, 2),
    _SwitchSettingSystemLocation_Type()
)
switchSettingSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingSystemLocation.setStatus("current")


class _SwitchSettingSystemContact_Type(DisplayString):
    """Custom type switchSettingSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchSettingSystemContact_Type.__name__ = "DisplayString"
_SwitchSettingSystemContact_Object = MibScalar
switchSettingSystemContact = _SwitchSettingSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 1, 3),
    _SwitchSettingSystemContact_Type()
)
switchSettingSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingSystemContact.setStatus("current")


class _SwitchSettingLocationAlert_Type(Integer32):
    """Custom type switchSettingLocationAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwitchSettingLocationAlert_Type.__name__ = "Integer32"
_SwitchSettingLocationAlert_Object = MibScalar
switchSettingLocationAlert = _SwitchSettingLocationAlert_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 1, 4),
    _SwitchSettingLocationAlert_Type()
)
switchSettingLocationAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingLocationAlert.setStatus("current")
_AdminPassword_ObjectIdentity = ObjectIdentity
adminPassword = _AdminPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 2)
)


class _AdminPasswordUserName_Type(DisplayString):
    """Custom type adminPasswordUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminPasswordUserName_Type.__name__ = "DisplayString"
_AdminPasswordUserName_Object = MibScalar
adminPasswordUserName = _AdminPasswordUserName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 2, 1),
    _AdminPasswordUserName_Type()
)
adminPasswordUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adminPasswordUserName.setStatus("current")


class _AdminPassword_Password_Type(DisplayString):
    """Custom type adminPassword_Password based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AdminPassword_Password_Type.__name__ = "DisplayString"
_AdminPassword_Password_Object = MibScalar
adminPassword_Password = _AdminPassword_Password_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 2, 2),
    _AdminPassword_Password_Type()
)
adminPassword_Password.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminPassword_Password.setStatus("current")
_IpConfiguration_ObjectIdentity = ObjectIdentity
ipConfiguration = _IpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3)
)
_IpConfigurationTable_Object = MibTable
ipConfigurationTable = _IpConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipConfigurationTable.setStatus("current")
_IpConfigurationEntry_Object = MibTableRow
ipConfigurationEntry = _IpConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1)
)
ipConfigurationEntry.setIndexNames(
    (0, "IES-2206FII", "ipConfigurationIndex"),
)
if mibBuilder.loadTexts:
    ipConfigurationEntry.setStatus("current")
_IpConfigurationIndex_Type = Integer32
_IpConfigurationIndex_Object = MibTableColumn
ipConfigurationIndex = _IpConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 1),
    _IpConfigurationIndex_Type()
)
ipConfigurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipConfigurationIndex.setStatus("current")


class _IpConfigurationDHCPStatus_Type(Integer32):
    """Custom type ipConfigurationDHCPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpConfigurationDHCPStatus_Type.__name__ = "Integer32"
_IpConfigurationDHCPStatus_Object = MibTableColumn
ipConfigurationDHCPStatus = _IpConfigurationDHCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 2),
    _IpConfigurationDHCPStatus_Type()
)
ipConfigurationDHCPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationDHCPStatus.setStatus("current")
_IpConfigurationAddress_Type = IpAddress
_IpConfigurationAddress_Object = MibTableColumn
ipConfigurationAddress = _IpConfigurationAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 3),
    _IpConfigurationAddress_Type()
)
ipConfigurationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationAddress.setStatus("current")
_IpConfigurationSubMask_Type = IpAddress
_IpConfigurationSubMask_Object = MibTableColumn
ipConfigurationSubMask = _IpConfigurationSubMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 4),
    _IpConfigurationSubMask_Type()
)
ipConfigurationSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationSubMask.setStatus("current")
_IpConfigurationGateway_Type = IpAddress
_IpConfigurationGateway_Object = MibTableColumn
ipConfigurationGateway = _IpConfigurationGateway_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 5),
    _IpConfigurationGateway_Type()
)
ipConfigurationGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationGateway.setStatus("current")
_IpConfigurationDNS1_Type = IpAddress
_IpConfigurationDNS1_Object = MibTableColumn
ipConfigurationDNS1 = _IpConfigurationDNS1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 6),
    _IpConfigurationDNS1_Type()
)
ipConfigurationDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationDNS1.setStatus("current")
_IpConfigurationDNS2_Type = IpAddress
_IpConfigurationDNS2_Object = MibTableColumn
ipConfigurationDNS2 = _IpConfigurationDNS2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 3, 1, 1, 7),
    _IpConfigurationDNS2_Type()
)
ipConfigurationDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationDNS2.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4)
)


class _SntpClientStatus_Type(Integer32):
    """Custom type sntpClientStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SntpClientStatus_Type.__name__ = "Integer32"
_SntpClientStatus_Object = MibScalar
sntpClientStatus = _SntpClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 1),
    _SntpClientStatus_Type()
)
sntpClientStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpClientStatus.setStatus("current")


class _SntpDaylightSavingTime_Type(Integer32):
    """Custom type sntpDaylightSavingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SntpDaylightSavingTime_Type.__name__ = "Integer32"
_SntpDaylightSavingTime_Object = MibScalar
sntpDaylightSavingTime = _SntpDaylightSavingTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 2),
    _SntpDaylightSavingTime_Type()
)
sntpDaylightSavingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingTime.setStatus("current")


class _SntpUTCTimezone_Type(Integer32):
    """Custom type sntpUTCTimezone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63)
        )
    )
    namedValues = NamedValues(
        *(("gmt_negative_12_00_Eniwetok_Kwajalein", 1),
          ("gmt_negative_11_00_Midway_Island_Samoa", 2),
          ("gmt_negative_10_00_Hawaii", 3),
          ("gmt_negative_09_00_Alaska", 4),
          ("gmt_negative_08_00_Pacific_Time_US_and_Canada_Tijuana", 5),
          ("gmt_negative_07_00_Arizona", 6),
          ("gmt_negative_07_00_Mountain_Time_US_and_Canada", 7),
          ("gmt_negative_06_00_Central_Time_US_and_Canada", 8),
          ("gmt_negative_06_00_Mexico_City_Tegucigalpa", 9),
          ("gmt_negative_06_00_Saskatchewan", 10),
          ("gmt_negative_05_00_Bogota_Lima_Quito", 11),
          ("gmt_negative_05_00_Eastern_Time_US_and_Canada", 12),
          ("gmt_negative_05_00_Indiana_East", 13),
          ("gmt_negative_04_00_Atlantic_Time_Canada", 14),
          ("gmt_negative_04_00_Caracas_La_Paz", 15),
          ("gmt_negative_04_00_Santiago", 16),
          ("gmt_negative_03_30_Newfoundland", 17),
          ("gmt_negative_03_00_Brasilia", 18),
          ("gmt_negative_03_00_Buenos_Aires_Georgetown", 19),
          ("gmt_negative_02_00_Mid-Atlantic", 20),
          ("gmt_negative_01_00_Azores_Cape_Verde_Is", 21),
          ("gmt_Casablanca_Monrovia", 22),
          ("gmt_Greenwich_Mean_Time_Dublin_Edinburgh_Lisbon_London", 23),
          ("gmt_positive_01_00_Amsterdam_Berlin_Bern_Rome_Stockholm_Vienna", 24),
          ("gmt_positive_01_00_Belgrade_Bratislava_Budapest_Ljubljana_Prague", 25),
          ("gmt_positive_01_00_Brussels_Copenhagen_Madrid_Paris_Vilnius", 26),
          ("gmt_positive_01_00_Sarajevo_Skopje_Sofija_Warsaw_Zagreb", 27),
          ("gmt_positive_02_00_Athens_Istanbul_Minsk", 28),
          ("gmt_positive_02_00_Bucharest", 29),
          ("gmt_positive_02_00_Cairo", 30),
          ("gmt_positive_02_00_Harare_Pretoria", 31),
          ("gmt_positive_02_00_Helsinki_Riga_Tallinn", 32),
          ("gmt_positive_02_00_Jerusalem", 33),
          ("gmt_positive_03_00_Baghdad_Kuwait_Riyadh", 34),
          ("gmt_positive_03_00_Moscow_St_Petersburg_Volgograd", 35),
          ("gmt_positive_03_00_Mairobi", 36),
          ("gmt_positive_03_30_Tehran", 37),
          ("gmt_positive_04_00_Abu_Dhabi_Muscat", 38),
          ("gmt_positive_04_00_Baku_Tbilisi", 39),
          ("gmt_positive_04_30_Kabul", 40),
          ("gmt_positive_05_00_Ekaterinburg", 41),
          ("gmt_positive_05_00_Islamabad_Karachi_Tashkent", 42),
          ("gmt_positive_05_30_Bombay_Calcutta_Madras_New_Delhi", 43),
          ("gmt_positive_06_00_Astana_Almaty_Dhaka", 44),
          ("gmt_positive_06_00_Colombo", 45),
          ("gmt_positive_07_00_Bangkok_Hanoi_Jakarta", 46),
          ("gmt_positive_08_00_Beijing_Chongqing_Hong_Kong_Urumqi", 47),
          ("gmt_positive_08_00_Perth", 48),
          ("gmt_positive_08_00_Singapore", 49),
          ("gmt_positive_08_00_Taipei", 50),
          ("gmt_positive_09_00_Osaka_Sapporo_Tokyo", 51),
          ("gmt_positive_09_00_Seoul", 52),
          ("gmt_positive_09_00_Yakutsk", 53),
          ("gmt_positive_09_30_Adelaide", 54),
          ("gmt_positive_09_30_Darwin", 55),
          ("gmt_positive_10_00_Brisbane", 56),
          ("gmt_positive_10_00_Canberra_Melbourne_Sydney", 57),
          ("gmt_positive_10_00_Guam_Port_Moresby", 58),
          ("gmt_positive_10_00_Hobart", 59),
          ("gmt_positive_10_00_Vladivostok", 60),
          ("gmt_positive_11_00_Magadan_Solomon_Is_New_Caledonia", 61),
          ("gmt_positive_12_00_Auckland_Wllington", 62),
          ("gmt_positive_12_00_Fiji_Kamchatka_Marshall_Is", 63))
    )


_SntpUTCTimezone_Type.__name__ = "Integer32"
_SntpUTCTimezone_Object = MibScalar
sntpUTCTimezone = _SntpUTCTimezone_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 3),
    _SntpUTCTimezone_Type()
)
sntpUTCTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpUTCTimezone.setStatus("current")


class _SntpServerAddress_Type(DisplayString):
    """Custom type sntpServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SntpServerAddress_Type.__name__ = "DisplayString"
_SntpServerAddress_Object = MibScalar
sntpServerAddress = _SntpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 4),
    _SntpServerAddress_Type()
)
sntpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerAddress.setStatus("current")


class _SntpSwitchTimer_Type(DisplayString):
    """Custom type sntpSwitchTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SntpSwitchTimer_Type.__name__ = "DisplayString"
_SntpSwitchTimer_Object = MibScalar
sntpSwitchTimer = _SntpSwitchTimer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 5),
    _SntpSwitchTimer_Type()
)
sntpSwitchTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpSwitchTimer.setStatus("current")


class _SntpDaylightSavingPeriodStart_Type(DisplayString):
    """Custom type sntpDaylightSavingPeriodStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SntpDaylightSavingPeriodStart_Type.__name__ = "DisplayString"
_SntpDaylightSavingPeriodStart_Object = MibScalar
sntpDaylightSavingPeriodStart = _SntpDaylightSavingPeriodStart_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 6),
    _SntpDaylightSavingPeriodStart_Type()
)
sntpDaylightSavingPeriodStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingPeriodStart.setStatus("current")


class _SntpDaylightSavingPeriodEnd_Type(DisplayString):
    """Custom type sntpDaylightSavingPeriodEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_SntpDaylightSavingPeriodEnd_Type.__name__ = "DisplayString"
_SntpDaylightSavingPeriodEnd_Object = MibScalar
sntpDaylightSavingPeriodEnd = _SntpDaylightSavingPeriodEnd_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 7),
    _SntpDaylightSavingPeriodEnd_Type()
)
sntpDaylightSavingPeriodEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingPeriodEnd.setStatus("current")
_SntpDaylightSavingOffset_Type = Integer32
_SntpDaylightSavingOffset_Object = MibScalar
sntpDaylightSavingOffset = _SntpDaylightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 4, 8),
    _SntpDaylightSavingOffset_Type()
)
sntpDaylightSavingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingOffset.setStatus("current")
_Lldp_ObjectIdentity = ObjectIdentity
lldp = _Lldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 5)
)


class _LldpStatus_Type(Integer32):
    """Custom type lldpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_LldpStatus_Type.__name__ = "Integer32"
_LldpStatus_Object = MibScalar
lldpStatus = _LldpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 5, 1),
    _LldpStatus_Type()
)
lldpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStatus.setStatus("current")
_LldpInterval_Type = Integer32
_LldpInterval_Object = MibScalar
lldpInterval = _LldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 5, 2),
    _LldpInterval_Type()
)
lldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpInterval.setStatus("current")
_AutoProvision_ObjectIdentity = ObjectIdentity
autoProvision = _AutoProvision_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6)
)


class _AutoProvisionConfigurationStatus_Type(Integer32):
    """Custom type autoProvisionConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AutoProvisionConfigurationStatus_Type.__name__ = "Integer32"
_AutoProvisionConfigurationStatus_Object = MibScalar
autoProvisionConfigurationStatus = _AutoProvisionConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6, 1),
    _AutoProvisionConfigurationStatus_Type()
)
autoProvisionConfigurationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvisionConfigurationStatus.setStatus("current")
_AutoProvisionConfigurationServerip_Type = IpAddress
_AutoProvisionConfigurationServerip_Object = MibScalar
autoProvisionConfigurationServerip = _AutoProvisionConfigurationServerip_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6, 2),
    _AutoProvisionConfigurationServerip_Type()
)
autoProvisionConfigurationServerip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvisionConfigurationServerip.setStatus("current")


class _AutoProvisionConfigurationFilename_Type(DisplayString):
    """Custom type autoProvisionConfigurationFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AutoProvisionConfigurationFilename_Type.__name__ = "DisplayString"
_AutoProvisionConfigurationFilename_Object = MibScalar
autoProvisionConfigurationFilename = _AutoProvisionConfigurationFilename_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6, 3),
    _AutoProvisionConfigurationFilename_Type()
)
autoProvisionConfigurationFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvisionConfigurationFilename.setStatus("current")


class _AutoProvisionImageStatus_Type(Integer32):
    """Custom type autoProvisionImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AutoProvisionImageStatus_Type.__name__ = "Integer32"
_AutoProvisionImageStatus_Object = MibScalar
autoProvisionImageStatus = _AutoProvisionImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6, 4),
    _AutoProvisionImageStatus_Type()
)
autoProvisionImageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvisionImageStatus.setStatus("current")
_AutoProvisionImageServerip_Type = IpAddress
_AutoProvisionImageServerip_Object = MibScalar
autoProvisionImageServerip = _AutoProvisionImageServerip_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6, 5),
    _AutoProvisionImageServerip_Type()
)
autoProvisionImageServerip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvisionImageServerip.setStatus("current")


class _AutoProvisionImageFilename_Type(DisplayString):
    """Custom type autoProvisionImageFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AutoProvisionImageFilename_Type.__name__ = "DisplayString"
_AutoProvisionImageFilename_Object = MibScalar
autoProvisionImageFilename = _AutoProvisionImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 6, 6),
    _AutoProvisionImageFilename_Type()
)
autoProvisionImageFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoProvisionImageFilename.setStatus("current")
_BackupAndRestore_ObjectIdentity = ObjectIdentity
backupAndRestore = _BackupAndRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7)
)


class _BackupServerIP_Type(IpAddress):
    """Custom type backupServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_BackupServerIP_Type.__name__ = "IpAddress"
_BackupServerIP_Object = MibScalar
backupServerIP = _BackupServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7, 1),
    _BackupServerIP_Type()
)
backupServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupServerIP.setStatus("current")


class _BackupAgentBoardFwFileName_Type(DisplayString):
    """Custom type backupAgentBoardFwFileName based on DisplayString"""
    defaultValue = OctetString("data.bin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BackupAgentBoardFwFileName_Type.__name__ = "DisplayString"
_BackupAgentBoardFwFileName_Object = MibScalar
backupAgentBoardFwFileName = _BackupAgentBoardFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7, 2),
    _BackupAgentBoardFwFileName_Type()
)
backupAgentBoardFwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupAgentBoardFwFileName.setStatus("current")


class _BackupStatus_Type(Integer32):
    """Custom type backupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_BackupStatus_Type.__name__ = "Integer32"
_BackupStatus_Object = MibScalar
backupStatus = _BackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7, 3),
    _BackupStatus_Type()
)
backupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupStatus.setStatus("current")


class _RestoreServerIP_Type(IpAddress):
    """Custom type restoreServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_RestoreServerIP_Type.__name__ = "IpAddress"
_RestoreServerIP_Object = MibScalar
restoreServerIP = _RestoreServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7, 4),
    _RestoreServerIP_Type()
)
restoreServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreServerIP.setStatus("current")


class _RestoreAgentBoardFwFileName_Type(DisplayString):
    """Custom type restoreAgentBoardFwFileName based on DisplayString"""
    defaultValue = OctetString("data.bin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RestoreAgentBoardFwFileName_Type.__name__ = "DisplayString"
_RestoreAgentBoardFwFileName_Object = MibScalar
restoreAgentBoardFwFileName = _RestoreAgentBoardFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7, 5),
    _RestoreAgentBoardFwFileName_Type()
)
restoreAgentBoardFwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreAgentBoardFwFileName.setStatus("current")


class _RestoreStatus_Type(Integer32):
    """Custom type restoreStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_RestoreStatus_Type.__name__ = "Integer32"
_RestoreStatus_Object = MibScalar
restoreStatus = _RestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 7, 6),
    _RestoreStatus_Type()
)
restoreStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreStatus.setStatus("current")
_UpgradeFirmware_ObjectIdentity = ObjectIdentity
upgradeFirmware = _UpgradeFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 8)
)


class _TftpDownloadServerIP_Type(IpAddress):
    """Custom type tftpDownloadServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_TftpDownloadServerIP_Type.__name__ = "IpAddress"
_TftpDownloadServerIP_Object = MibScalar
tftpDownloadServerIP = _TftpDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 8, 1),
    _TftpDownloadServerIP_Type()
)
tftpDownloadServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadServerIP.setStatus("current")


class _TftpDownloadAgentBoardFwFileName_Type(DisplayString):
    """Custom type tftpDownloadAgentBoardFwFileName based on DisplayString"""
    defaultValue = OctetString("image.bin")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TftpDownloadAgentBoardFwFileName_Type.__name__ = "DisplayString"
_TftpDownloadAgentBoardFwFileName_Object = MibScalar
tftpDownloadAgentBoardFwFileName = _TftpDownloadAgentBoardFwFileName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 8, 2),
    _TftpDownloadAgentBoardFwFileName_Type()
)
tftpDownloadAgentBoardFwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadAgentBoardFwFileName.setStatus("current")


class _TftpDownloadStatus_Type(Integer32):
    """Custom type tftpDownloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_TftpDownloadStatus_Type.__name__ = "Integer32"
_TftpDownloadStatus_Object = MibScalar
tftpDownloadStatus = _TftpDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 2, 8, 3),
    _TftpDownloadStatus_Type()
)
tftpDownloadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadStatus.setStatus("current")
_DhcpServer_ObjectIdentity = ObjectIdentity
dhcpServer = _DhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3)
)
_DhcpServerCfgTable_Object = MibTable
dhcpServerCfgTable = _DhcpServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpServerCfgTable.setStatus("current")
_DhcpServerCfgEntry_Object = MibTableRow
dhcpServerCfgEntry = _DhcpServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1)
)
dhcpServerCfgEntry.setIndexNames(
    (0, "IES-2206FII", "dhcpServerCfgIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerCfgEntry.setStatus("current")
_DhcpServerCfgIndex_Type = Integer32
_DhcpServerCfgIndex_Object = MibTableColumn
dhcpServerCfgIndex = _DhcpServerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 1),
    _DhcpServerCfgIndex_Type()
)
dhcpServerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpServerCfgIndex.setStatus("current")


class _DhcpServerCfgStatus_Type(Integer32):
    """Custom type dhcpServerCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DhcpServerCfgStatus_Type.__name__ = "Integer32"
_DhcpServerCfgStatus_Object = MibTableColumn
dhcpServerCfgStatus = _DhcpServerCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 2),
    _DhcpServerCfgStatus_Type()
)
dhcpServerCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgStatus.setStatus("current")
_DhcpServerCfgLowIPAddr_Type = IpAddress
_DhcpServerCfgLowIPAddr_Object = MibTableColumn
dhcpServerCfgLowIPAddr = _DhcpServerCfgLowIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 3),
    _DhcpServerCfgLowIPAddr_Type()
)
dhcpServerCfgLowIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgLowIPAddr.setStatus("current")
_DhcpServerCfgHighIPAddr_Type = IpAddress
_DhcpServerCfgHighIPAddr_Object = MibTableColumn
dhcpServerCfgHighIPAddr = _DhcpServerCfgHighIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 4),
    _DhcpServerCfgHighIPAddr_Type()
)
dhcpServerCfgHighIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgHighIPAddr.setStatus("current")
_DhcpServerCfgSubMask_Type = IpAddress
_DhcpServerCfgSubMask_Object = MibTableColumn
dhcpServerCfgSubMask = _DhcpServerCfgSubMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 5),
    _DhcpServerCfgSubMask_Type()
)
dhcpServerCfgSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgSubMask.setStatus("current")
_DhcpServerCfgGateway_Type = IpAddress
_DhcpServerCfgGateway_Object = MibTableColumn
dhcpServerCfgGateway = _DhcpServerCfgGateway_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 6),
    _DhcpServerCfgGateway_Type()
)
dhcpServerCfgGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgGateway.setStatus("current")
_DhcpServerCfgDNS_Type = IpAddress
_DhcpServerCfgDNS_Object = MibTableColumn
dhcpServerCfgDNS = _DhcpServerCfgDNS_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 7),
    _DhcpServerCfgDNS_Type()
)
dhcpServerCfgDNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgDNS.setStatus("current")
_DhcpServerCfgLeaseTime_Type = Integer32
_DhcpServerCfgLeaseTime_Object = MibTableColumn
dhcpServerCfgLeaseTime = _DhcpServerCfgLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 1, 1, 8),
    _DhcpServerCfgLeaseTime_Type()
)
dhcpServerCfgLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerCfgLeaseTime.setStatus("current")
_DhcpServerClientInfoTable_Object = MibTable
dhcpServerClientInfoTable = _DhcpServerClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2)
)
if mibBuilder.loadTexts:
    dhcpServerClientInfoTable.setStatus("current")
_DhcpServerClientInfoEntry_Object = MibTableRow
dhcpServerClientInfoEntry = _DhcpServerClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1)
)
dhcpServerClientInfoEntry.setIndexNames(
    (0, "IES-2206FII", "dhcpServerClientInfoIndex"),
)
if mibBuilder.loadTexts:
    dhcpServerClientInfoEntry.setStatus("current")
_DhcpServerClientInfoIndex_Type = Integer32
_DhcpServerClientInfoIndex_Object = MibTableColumn
dhcpServerClientInfoIndex = _DhcpServerClientInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1, 1),
    _DhcpServerClientInfoIndex_Type()
)
dhcpServerClientInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerClientInfoIndex.setStatus("current")


class _DhcpServerClientInfoIPAddr_Type(DisplayString):
    """Custom type dhcpServerClientInfoIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DhcpServerClientInfoIPAddr_Type.__name__ = "DisplayString"
_DhcpServerClientInfoIPAddr_Object = MibTableColumn
dhcpServerClientInfoIPAddr = _DhcpServerClientInfoIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1, 2),
    _DhcpServerClientInfoIPAddr_Type()
)
dhcpServerClientInfoIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerClientInfoIPAddr.setStatus("current")


class _DhcpServerClientInfoID_Type(DisplayString):
    """Custom type dhcpServerClientInfoID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_DhcpServerClientInfoID_Type.__name__ = "DisplayString"
_DhcpServerClientInfoID_Object = MibTableColumn
dhcpServerClientInfoID = _DhcpServerClientInfoID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1, 3),
    _DhcpServerClientInfoID_Type()
)
dhcpServerClientInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerClientInfoID.setStatus("current")


class _DhcpServerClientInfoType_Type(DisplayString):
    """Custom type dhcpServerClientInfoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DhcpServerClientInfoType_Type.__name__ = "DisplayString"
_DhcpServerClientInfoType_Object = MibTableColumn
dhcpServerClientInfoType = _DhcpServerClientInfoType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1, 4),
    _DhcpServerClientInfoType_Type()
)
dhcpServerClientInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerClientInfoType.setStatus("current")


class _DhcpServerClientInfoStatus_Type(DisplayString):
    """Custom type dhcpServerClientInfoStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DhcpServerClientInfoStatus_Type.__name__ = "DisplayString"
_DhcpServerClientInfoStatus_Object = MibTableColumn
dhcpServerClientInfoStatus = _DhcpServerClientInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1, 5),
    _DhcpServerClientInfoStatus_Type()
)
dhcpServerClientInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerClientInfoStatus.setStatus("current")
_DhcpServerClientInfoLease_Type = Integer32
_DhcpServerClientInfoLease_Object = MibTableColumn
dhcpServerClientInfoLease = _DhcpServerClientInfoLease_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 2, 1, 6),
    _DhcpServerClientInfoLease_Type()
)
dhcpServerClientInfoLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerClientInfoLease.setStatus("current")
_DhcpServerIPBindingTable_Object = MibTable
dhcpServerIPBindingTable = _DhcpServerIPBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 3)
)
if mibBuilder.loadTexts:
    dhcpServerIPBindingTable.setStatus("current")
_DhcpServerIPBindingEntry_Object = MibTableRow
dhcpServerIPBindingEntry = _DhcpServerIPBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 3, 1)
)
dhcpServerIPBindingEntry.setIndexNames(
    (0, "IES-2206FII", "dhcpServerIPBindingPortNum"),
)
if mibBuilder.loadTexts:
    dhcpServerIPBindingEntry.setStatus("current")
_DhcpServerIPBindingPortNum_Type = Integer32
_DhcpServerIPBindingPortNum_Object = MibTableColumn
dhcpServerIPBindingPortNum = _DhcpServerIPBindingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 3, 1, 1),
    _DhcpServerIPBindingPortNum_Type()
)
dhcpServerIPBindingPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerIPBindingPortNum.setStatus("current")
_DhcpServerIPBindingAddr_Type = IpAddress
_DhcpServerIPBindingAddr_Object = MibTableColumn
dhcpServerIPBindingAddr = _DhcpServerIPBindingAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 3, 3, 1, 2),
    _DhcpServerIPBindingAddr_Type()
)
dhcpServerIPBindingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerIPBindingAddr.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4)
)
_PortControl_ObjectIdentity = ObjectIdentity
portControl = _PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1)
)
_PortCtrlTable_Object = MibTable
portCtrlTable = _PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    portCtrlTable.setStatus("current")
_PortCtrlEntry_Object = MibTableRow
portCtrlEntry = _PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1)
)
portCtrlEntry.setIndexNames(
    (0, "IES-2206FII", "portCtrlIndex"),
)
if mibBuilder.loadTexts:
    portCtrlEntry.setStatus("current")
_PortCtrlIndex_Type = Integer32
_PortCtrlIndex_Object = MibTableColumn
portCtrlIndex = _PortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 1),
    _PortCtrlIndex_Type()
)
portCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portCtrlIndex.setStatus("current")


class _PortCtrlPortName_Type(DisplayString):
    """Custom type portCtrlPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PortCtrlPortName_Type.__name__ = "DisplayString"
_PortCtrlPortName_Object = MibTableColumn
portCtrlPortName = _PortCtrlPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 2),
    _PortCtrlPortName_Type()
)
portCtrlPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCtrlPortName.setStatus("current")


class _PortCtrlPortStatus_Type(Integer32):
    """Custom type portCtrlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortCtrlPortStatus_Type.__name__ = "Integer32"
_PortCtrlPortStatus_Object = MibTableColumn
portCtrlPortStatus = _PortCtrlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 3),
    _PortCtrlPortStatus_Type()
)
portCtrlPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlPortStatus.setStatus("current")


class _PortCtrlNegotiation_Type(Integer32):
    """Custom type portCtrlNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("force", 2))
    )


_PortCtrlNegotiation_Type.__name__ = "Integer32"
_PortCtrlNegotiation_Object = MibTableColumn
portCtrlNegotiation = _PortCtrlNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 4),
    _PortCtrlNegotiation_Type()
)
portCtrlNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlNegotiation.setStatus("current")


class _PortCtrlSpeed_Type(Integer32):
    """Custom type portCtrlSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("speed_10M", 1),
          ("speed_100M", 2),
          ("speed_1000M", 3))
    )


_PortCtrlSpeed_Type.__name__ = "Integer32"
_PortCtrlSpeed_Object = MibTableColumn
portCtrlSpeed = _PortCtrlSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 5),
    _PortCtrlSpeed_Type()
)
portCtrlSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlSpeed.setStatus("current")


class _PortCtrlDuplex_Type(Integer32):
    """Custom type portCtrlDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 1),
          ("halfduplex", 2))
    )


_PortCtrlDuplex_Type.__name__ = "Integer32"
_PortCtrlDuplex_Object = MibTableColumn
portCtrlDuplex = _PortCtrlDuplex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 6),
    _PortCtrlDuplex_Type()
)
portCtrlDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlDuplex.setStatus("current")


class _PortCtrlFlowControl_Type(Integer32):
    """Custom type portCtrlFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("symmetric", 2),
          ("asymmetric", 3))
    )


_PortCtrlFlowControl_Type.__name__ = "Integer32"
_PortCtrlFlowControl_Object = MibTableColumn
portCtrlFlowControl = _PortCtrlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 7),
    _PortCtrlFlowControl_Type()
)
portCtrlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlFlowControl.setStatus("current")


class _PortCtrlSecurity_Type(Integer32):
    """Custom type portCtrlSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortCtrlSecurity_Type.__name__ = "Integer32"
_PortCtrlSecurity_Object = MibTableColumn
portCtrlSecurity = _PortCtrlSecurity_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 1, 1, 1, 8),
    _PortCtrlSecurity_Type()
)
portCtrlSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlSecurity.setStatus("current")
_RateLimiting_ObjectIdentity = ObjectIdentity
rateLimiting = _RateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2)
)
_RateLimitingTable_Object = MibTable
rateLimitingTable = _RateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2, 1)
)
if mibBuilder.loadTexts:
    rateLimitingTable.setStatus("current")
_RateLimitingEntry_Object = MibTableRow
rateLimitingEntry = _RateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2, 1, 1)
)
rateLimitingEntry.setIndexNames(
    (0, "IES-2206FII", "rateLimitingPortNum"),
)
if mibBuilder.loadTexts:
    rateLimitingEntry.setStatus("current")
_RateLimitingPortNum_Type = Integer32
_RateLimitingPortNum_Object = MibTableColumn
rateLimitingPortNum = _RateLimitingPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2, 1, 1, 1),
    _RateLimitingPortNum_Type()
)
rateLimitingPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateLimitingPortNum.setStatus("current")


class _RateLimitingPortType_Type(Integer32):
    """Custom type rateLimitingPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("broadcast_multicast_floodedunicast", 2),
          ("broadcast_multicast", 3),
          ("broadcastonly", 4))
    )


_RateLimitingPortType_Type.__name__ = "Integer32"
_RateLimitingPortType_Object = MibTableColumn
rateLimitingPortType = _RateLimitingPortType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2, 1, 1, 2),
    _RateLimitingPortType_Type()
)
rateLimitingPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitingPortType.setStatus("current")
_RateLimitingIngressRate_Type = Integer32
_RateLimitingIngressRate_Object = MibTableColumn
rateLimitingIngressRate = _RateLimitingIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2, 1, 1, 3),
    _RateLimitingIngressRate_Type()
)
rateLimitingIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitingIngressRate.setStatus("current")
_RateLimitingEgressRate_Type = Integer32
_RateLimitingEgressRate_Object = MibTableColumn
rateLimitingEgressRate = _RateLimitingEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 2, 1, 1, 4),
    _RateLimitingEgressRate_Type()
)
rateLimitingEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitingEgressRate.setStatus("current")
_PortTrunk_ObjectIdentity = ObjectIdentity
portTrunk = _PortTrunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3)
)
_AggregatorSetting_ObjectIdentity = ObjectIdentity
aggregatorSetting = _AggregatorSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1)
)
_PortTrunkSysPri_Type = Integer32
_PortTrunkSysPri_Object = MibScalar
portTrunkSysPri = _PortTrunkSysPri_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 1),
    _PortTrunkSysPri_Type()
)
portTrunkSysPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkSysPri.setStatus("current")
_PortTrunkAggregatorTable_Object = MibTable
portTrunkAggregatorTable = _PortTrunkAggregatorTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    portTrunkAggregatorTable.setStatus("current")
_PortTrunkAggregatorEntry_Object = MibTableRow
portTrunkAggregatorEntry = _PortTrunkAggregatorEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2, 1)
)
portTrunkAggregatorEntry.setIndexNames(
    (0, "IES-2206FII", "portTrunkAggregatorIndex"),
)
if mibBuilder.loadTexts:
    portTrunkAggregatorEntry.setStatus("current")
_PortTrunkAggregatorIndex_Type = Integer32
_PortTrunkAggregatorIndex_Object = MibTableColumn
portTrunkAggregatorIndex = _PortTrunkAggregatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2, 1, 1),
    _PortTrunkAggregatorIndex_Type()
)
portTrunkAggregatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkAggregatorIndex.setStatus("current")


class _PortTrunkAggregatorGroupName_Type(DisplayString):
    """Custom type portTrunkAggregatorGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PortTrunkAggregatorGroupName_Type.__name__ = "DisplayString"
_PortTrunkAggregatorGroupName_Object = MibTableColumn
portTrunkAggregatorGroupName = _PortTrunkAggregatorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2, 1, 2),
    _PortTrunkAggregatorGroupName_Type()
)
portTrunkAggregatorGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkAggregatorGroupName.setStatus("current")
_PortTrunkAggregatorMemberPorts_Type = PortList
_PortTrunkAggregatorMemberPorts_Object = MibTableColumn
portTrunkAggregatorMemberPorts = _PortTrunkAggregatorMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2, 1, 3),
    _PortTrunkAggregatorMemberPorts_Type()
)
portTrunkAggregatorMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkAggregatorMemberPorts.setStatus("current")


class _PortTrunkAggregatorLACPStatus_Type(Integer32):
    """Custom type portTrunkAggregatorLACPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_PortTrunkAggregatorLACPStatus_Type.__name__ = "Integer32"
_PortTrunkAggregatorLACPStatus_Object = MibTableColumn
portTrunkAggregatorLACPStatus = _PortTrunkAggregatorLACPStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2, 1, 4),
    _PortTrunkAggregatorLACPStatus_Type()
)
portTrunkAggregatorLACPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkAggregatorLACPStatus.setStatus("current")
_PortTrunkAggregatorWorkPorts_Type = Integer32
_PortTrunkAggregatorWorkPorts_Object = MibTableColumn
portTrunkAggregatorWorkPorts = _PortTrunkAggregatorWorkPorts_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 1, 2, 1, 5),
    _PortTrunkAggregatorWorkPorts_Type()
)
portTrunkAggregatorWorkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkAggregatorWorkPorts.setStatus("current")
_AggregatorStatus_ObjectIdentity = ObjectIdentity
aggregatorStatus = _AggregatorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 2)
)
_PortTrunkAggregatorInfoTable_Object = MibTable
portTrunkAggregatorInfoTable = _PortTrunkAggregatorInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    portTrunkAggregatorInfoTable.setStatus("current")
_PortTrunkAggregatorInfoEntry_Object = MibTableRow
portTrunkAggregatorInfoEntry = _PortTrunkAggregatorInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 2, 1, 1)
)
portTrunkAggregatorInfoEntry.setIndexNames(
    (0, "IES-2206FII", "portTrunkAggregatorInfoIndex"),
)
if mibBuilder.loadTexts:
    portTrunkAggregatorInfoEntry.setStatus("current")
_PortTrunkAggregatorInfoIndex_Type = Integer32
_PortTrunkAggregatorInfoIndex_Object = MibTableColumn
portTrunkAggregatorInfoIndex = _PortTrunkAggregatorInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 2, 1, 1, 1),
    _PortTrunkAggregatorInfoIndex_Type()
)
portTrunkAggregatorInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkAggregatorInfoIndex.setStatus("current")


class _PortTrunkAggregatorInfoGroupName_Type(DisplayString):
    """Custom type portTrunkAggregatorInfoGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PortTrunkAggregatorInfoGroupName_Type.__name__ = "DisplayString"
_PortTrunkAggregatorInfoGroupName_Object = MibTableColumn
portTrunkAggregatorInfoGroupName = _PortTrunkAggregatorInfoGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 2, 1, 1, 2),
    _PortTrunkAggregatorInfoGroupName_Type()
)
portTrunkAggregatorInfoGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkAggregatorInfoGroupName.setStatus("current")


class _PortTrunkAggregatorInfoDescription_Type(DisplayString):
    """Custom type portTrunkAggregatorInfoDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortTrunkAggregatorInfoDescription_Type.__name__ = "DisplayString"
_PortTrunkAggregatorInfoDescription_Object = MibTableColumn
portTrunkAggregatorInfoDescription = _PortTrunkAggregatorInfoDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 2, 1, 1, 3),
    _PortTrunkAggregatorInfoDescription_Type()
)
portTrunkAggregatorInfoDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkAggregatorInfoDescription.setStatus("current")
_StateActivity_ObjectIdentity = ObjectIdentity
stateActivity = _StateActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 3)
)
_PortTrunkLACPStateActTable_Object = MibTable
portTrunkLACPStateActTable = _PortTrunkLACPStateActTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    portTrunkLACPStateActTable.setStatus("current")
_PortTrunkLACPStateActEntry_Object = MibTableRow
portTrunkLACPStateActEntry = _PortTrunkLACPStateActEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 3, 1, 1)
)
portTrunkLACPStateActEntry.setIndexNames(
    (0, "IES-2206FII", "portTrunkLACPStateActPortNum"),
)
if mibBuilder.loadTexts:
    portTrunkLACPStateActEntry.setStatus("current")
_PortTrunkLACPStateActPortNum_Type = Integer32
_PortTrunkLACPStateActPortNum_Object = MibTableColumn
portTrunkLACPStateActPortNum = _PortTrunkLACPStateActPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 3, 1, 1, 1),
    _PortTrunkLACPStateActPortNum_Type()
)
portTrunkLACPStateActPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkLACPStateActPortNum.setStatus("current")


class _PortTrunkLACPStateActStatus_Type(Integer32):
    """Custom type portTrunkLACPStateActStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passtive", 2),
          ("disabled", 3))
    )


_PortTrunkLACPStateActStatus_Type.__name__ = "Integer32"
_PortTrunkLACPStateActStatus_Object = MibTableColumn
portTrunkLACPStateActStatus = _PortTrunkLACPStateActStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 4, 3, 3, 1, 1, 2),
    _PortTrunkLACPStateActStatus_Type()
)
portTrunkLACPStateActStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkLACPStateActStatus.setStatus("current")
_Redunadancy_ObjectIdentity = ObjectIdentity
redunadancy = _Redunadancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5)
)
_RedundantRing_ObjectIdentity = ObjectIdentity
redundantRing = _RedundantRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1)
)


class _RedundantRingStatus_Type(Integer32):
    """Custom type redundantRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RedundantRingStatus_Type.__name__ = "Integer32"
_RedundantRingStatus_Object = MibScalar
redundantRingStatus = _RedundantRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 1),
    _RedundantRingStatus_Type()
)
redundantRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingStatus.setStatus("current")


class _RedundantRingRingMasterStatus_Type(Integer32):
    """Custom type redundantRingRingMasterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RedundantRingRingMasterStatus_Type.__name__ = "Integer32"
_RedundantRingRingMasterStatus_Object = MibScalar
redundantRingRingMasterStatus = _RedundantRingRingMasterStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 2),
    _RedundantRingRingMasterStatus_Type()
)
redundantRingRingMasterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingRingMasterStatus.setStatus("current")
_RedundantRingRingPort1_Type = Integer32
_RedundantRingRingPort1_Object = MibScalar
redundantRingRingPort1 = _RedundantRingRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 3),
    _RedundantRingRingPort1_Type()
)
redundantRingRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingRingPort1.setStatus("current")
_RedundantRingRingPort2_Type = Integer32
_RedundantRingRingPort2_Object = MibScalar
redundantRingRingPort2 = _RedundantRingRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 4),
    _RedundantRingRingPort2_Type()
)
redundantRingRingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingRingPort2.setStatus("current")


class _RedundantRingCoupleRingStatus_Type(Integer32):
    """Custom type redundantRingCoupleRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RedundantRingCoupleRingStatus_Type.__name__ = "Integer32"
_RedundantRingCoupleRingStatus_Object = MibScalar
redundantRingCoupleRingStatus = _RedundantRingCoupleRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 5),
    _RedundantRingCoupleRingStatus_Type()
)
redundantRingCoupleRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingCoupleRingStatus.setStatus("current")
_RedundantRingCouplingPort_Type = Integer32
_RedundantRingCouplingPort_Object = MibScalar
redundantRingCouplingPort = _RedundantRingCouplingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 6),
    _RedundantRingCouplingPort_Type()
)
redundantRingCouplingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingCouplingPort.setStatus("current")


class _RedundantRingDualHomingStatus_Type(Integer32):
    """Custom type redundantRingDualHomingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RedundantRingDualHomingStatus_Type.__name__ = "Integer32"
_RedundantRingDualHomingStatus_Object = MibScalar
redundantRingDualHomingStatus = _RedundantRingDualHomingStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 7),
    _RedundantRingDualHomingStatus_Type()
)
redundantRingDualHomingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingDualHomingStatus.setStatus("current")
_RedundantRingHomingPort_Type = Integer32
_RedundantRingHomingPort_Object = MibScalar
redundantRingHomingPort = _RedundantRingHomingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 8),
    _RedundantRingHomingPort_Type()
)
redundantRingHomingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingHomingPort.setStatus("current")


class _RedundantRingRingMasterHStatus_Type(Integer32):
    """Custom type redundantRingRingMasterHStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RedundantRingRingMasterHStatus_Type.__name__ = "Integer32"
_RedundantRingRingMasterHStatus_Object = MibScalar
redundantRingRingMasterHStatus = _RedundantRingRingMasterHStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 1, 9),
    _RedundantRingRingMasterHStatus_Type()
)
redundantRingRingMasterHStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundantRingRingMasterHStatus.setStatus("current")
_Rstp_ObjectIdentity = ObjectIdentity
rstp = _Rstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3)
)


class _RstpStatus_Type(Integer32):
    """Custom type rstpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enalbed", 1),
          ("disabled", 2))
    )


_RstpStatus_Type.__name__ = "Integer32"
_RstpStatus_Object = MibScalar
rstpStatus = _RstpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 1),
    _RstpStatus_Type()
)
rstpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpStatus.setStatus("current")
_RstpPriority_Type = Integer32
_RstpPriority_Object = MibScalar
rstpPriority = _RstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 2),
    _RstpPriority_Type()
)
rstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPriority.setStatus("current")
_RstpMaxAge_Type = Integer32
_RstpMaxAge_Object = MibScalar
rstpMaxAge = _RstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 3),
    _RstpMaxAge_Type()
)
rstpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpMaxAge.setStatus("current")
_RstpHelloTime_Type = Integer32
_RstpHelloTime_Object = MibScalar
rstpHelloTime = _RstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 4),
    _RstpHelloTime_Type()
)
rstpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpHelloTime.setStatus("current")
_RstpForwardDelayTime_Type = Integer32
_RstpForwardDelayTime_Object = MibScalar
rstpForwardDelayTime = _RstpForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 5),
    _RstpForwardDelayTime_Type()
)
rstpForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpForwardDelayTime.setStatus("current")
_RstpPerPortCfgTable_Object = MibTable
rstpPerPortCfgTable = _RstpPerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6)
)
if mibBuilder.loadTexts:
    rstpPerPortCfgTable.setStatus("current")
_RstpPerPortCfgEntry_Object = MibTableRow
rstpPerPortCfgEntry = _RstpPerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1)
)
rstpPerPortCfgEntry.setIndexNames(
    (0, "IES-2206FII", "rstpPerPortCfgPortNum"),
)
if mibBuilder.loadTexts:
    rstpPerPortCfgEntry.setStatus("current")
_RstpPerPortCfgPortNum_Type = Integer32
_RstpPerPortCfgPortNum_Object = MibTableColumn
rstpPerPortCfgPortNum = _RstpPerPortCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1, 1),
    _RstpPerPortCfgPortNum_Type()
)
rstpPerPortCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortCfgPortNum.setStatus("current")
_RstpPerPortCfgPathCost_Type = Integer32
_RstpPerPortCfgPathCost_Object = MibTableColumn
rstpPerPortCfgPathCost = _RstpPerPortCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1, 2),
    _RstpPerPortCfgPathCost_Type()
)
rstpPerPortCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgPathCost.setStatus("current")
_RstpPerPortCfgPriority_Type = Integer32
_RstpPerPortCfgPriority_Object = MibTableColumn
rstpPerPortCfgPriority = _RstpPerPortCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1, 3),
    _RstpPerPortCfgPriority_Type()
)
rstpPerPortCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgPriority.setStatus("current")


class _RstpPerPortCfgAdminP2P_Type(Integer32):
    """Custom type rstpPerPortCfgAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("auto", 3))
    )


_RstpPerPortCfgAdminP2P_Type.__name__ = "Integer32"
_RstpPerPortCfgAdminP2P_Object = MibTableColumn
rstpPerPortCfgAdminP2P = _RstpPerPortCfgAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1, 4),
    _RstpPerPortCfgAdminP2P_Type()
)
rstpPerPortCfgAdminP2P.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminP2P.setStatus("current")


class _RstpPerPortCfgAdminEdge_Type(Integer32):
    """Custom type rstpPerPortCfgAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortCfgAdminEdge_Type.__name__ = "Integer32"
_RstpPerPortCfgAdminEdge_Object = MibTableColumn
rstpPerPortCfgAdminEdge = _RstpPerPortCfgAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1, 5),
    _RstpPerPortCfgAdminEdge_Type()
)
rstpPerPortCfgAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminEdge.setStatus("current")


class _RstpPerPortCfgAdminNonStp_Type(Integer32):
    """Custom type rstpPerPortCfgAdminNonStp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortCfgAdminNonStp_Type.__name__ = "Integer32"
_RstpPerPortCfgAdminNonStp_Object = MibTableColumn
rstpPerPortCfgAdminNonStp = _RstpPerPortCfgAdminNonStp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 6, 1, 6),
    _RstpPerPortCfgAdminNonStp_Type()
)
rstpPerPortCfgAdminNonStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminNonStp.setStatus("current")
_RstpRootBridgeInformationTable_Object = MibTable
rstpRootBridgeInformationTable = _RstpRootBridgeInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7)
)
if mibBuilder.loadTexts:
    rstpRootBridgeInformationTable.setStatus("current")
_RstpRootBridgeInformationEntry_Object = MibTableRow
rstpRootBridgeInformationEntry = _RstpRootBridgeInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1)
)
rstpRootBridgeInformationEntry.setIndexNames(
    (0, "IES-2206FII", "rstpRootBridgeInformationIndex"),
)
if mibBuilder.loadTexts:
    rstpRootBridgeInformationEntry.setStatus("current")
_RstpRootBridgeInformationIndex_Type = Integer32
_RstpRootBridgeInformationIndex_Object = MibTableColumn
rstpRootBridgeInformationIndex = _RstpRootBridgeInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 1),
    _RstpRootBridgeInformationIndex_Type()
)
rstpRootBridgeInformationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationIndex.setStatus("current")


class _RstpRootBridgeInformationBridgeID_Type(DisplayString):
    """Custom type rstpRootBridgeInformationBridgeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RstpRootBridgeInformationBridgeID_Type.__name__ = "DisplayString"
_RstpRootBridgeInformationBridgeID_Object = MibTableColumn
rstpRootBridgeInformationBridgeID = _RstpRootBridgeInformationBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 2),
    _RstpRootBridgeInformationBridgeID_Type()
)
rstpRootBridgeInformationBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationBridgeID.setStatus("current")
_RstpRootBridgeInformationRootPriority_Type = Integer32
_RstpRootBridgeInformationRootPriority_Object = MibTableColumn
rstpRootBridgeInformationRootPriority = _RstpRootBridgeInformationRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 3),
    _RstpRootBridgeInformationRootPriority_Type()
)
rstpRootBridgeInformationRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPriority.setStatus("current")


class _RstpRootBridgeInformationRootPort_Type(DisplayString):
    """Custom type rstpRootBridgeInformationRootPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RstpRootBridgeInformationRootPort_Type.__name__ = "DisplayString"
_RstpRootBridgeInformationRootPort_Object = MibTableColumn
rstpRootBridgeInformationRootPort = _RstpRootBridgeInformationRootPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 4),
    _RstpRootBridgeInformationRootPort_Type()
)
rstpRootBridgeInformationRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPort.setStatus("current")
_RstpRootBridgeInformationRootPathCost_Type = Integer32
_RstpRootBridgeInformationRootPathCost_Object = MibTableColumn
rstpRootBridgeInformationRootPathCost = _RstpRootBridgeInformationRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 5),
    _RstpRootBridgeInformationRootPathCost_Type()
)
rstpRootBridgeInformationRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPathCost.setStatus("current")
_RstpRootBridgeInformationMaxAge_Type = Integer32
_RstpRootBridgeInformationMaxAge_Object = MibTableColumn
rstpRootBridgeInformationMaxAge = _RstpRootBridgeInformationMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 6),
    _RstpRootBridgeInformationMaxAge_Type()
)
rstpRootBridgeInformationMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationMaxAge.setStatus("current")
_RstpRootBridgeInformationHelloTime_Type = Integer32
_RstpRootBridgeInformationHelloTime_Object = MibTableColumn
rstpRootBridgeInformationHelloTime = _RstpRootBridgeInformationHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 7),
    _RstpRootBridgeInformationHelloTime_Type()
)
rstpRootBridgeInformationHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationHelloTime.setStatus("current")
_RstpRootBridgeInformationForwardDelay_Type = Integer32
_RstpRootBridgeInformationForwardDelay_Object = MibTableColumn
rstpRootBridgeInformationForwardDelay = _RstpRootBridgeInformationForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 7, 1, 8),
    _RstpRootBridgeInformationForwardDelay_Type()
)
rstpRootBridgeInformationForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationForwardDelay.setStatus("current")
_RstpPerPortInfoTable_Object = MibTable
rstpPerPortInfoTable = _RstpPerPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8)
)
if mibBuilder.loadTexts:
    rstpPerPortInfoTable.setStatus("current")
_RstpPerPortInfoEntry_Object = MibTableRow
rstpPerPortInfoEntry = _RstpPerPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1)
)
rstpPerPortInfoEntry.setIndexNames(
    (0, "IES-2206FII", "rstpPerPortInfoPortNum"),
)
if mibBuilder.loadTexts:
    rstpPerPortInfoEntry.setStatus("current")
_RstpPerPortInfoPortNum_Type = Integer32
_RstpPerPortInfoPortNum_Object = MibTableColumn
rstpPerPortInfoPortNum = _RstpPerPortInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 1),
    _RstpPerPortInfoPortNum_Type()
)
rstpPerPortInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPortNum.setStatus("current")
_RstpPerPortInfoPathCost_Type = Integer32
_RstpPerPortInfoPathCost_Object = MibTableColumn
rstpPerPortInfoPathCost = _RstpPerPortInfoPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 2),
    _RstpPerPortInfoPathCost_Type()
)
rstpPerPortInfoPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPathCost.setStatus("current")
_RstpPerPortInfoPriority_Type = Integer32
_RstpPerPortInfoPriority_Object = MibTableColumn
rstpPerPortInfoPriority = _RstpPerPortInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 3),
    _RstpPerPortInfoPriority_Type()
)
rstpPerPortInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPriority.setStatus("current")


class _RstpPerPortInfoAdminP2P_Type(Integer32):
    """Custom type rstpPerPortInfoAdminP2P based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("true", 2),
          ("false", 3))
    )


_RstpPerPortInfoAdminP2P_Type.__name__ = "Integer32"
_RstpPerPortInfoAdminP2P_Object = MibTableColumn
rstpPerPortInfoAdminP2P = _RstpPerPortInfoAdminP2P_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 4),
    _RstpPerPortInfoAdminP2P_Type()
)
rstpPerPortInfoAdminP2P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoAdminP2P.setStatus("current")


class _RstpPerPortInfoAdminEdge_Type(Integer32):
    """Custom type rstpPerPortInfoAdminEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortInfoAdminEdge_Type.__name__ = "Integer32"
_RstpPerPortInfoAdminEdge_Object = MibTableColumn
rstpPerPortInfoAdminEdge = _RstpPerPortInfoAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 5),
    _RstpPerPortInfoAdminEdge_Type()
)
rstpPerPortInfoAdminEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoAdminEdge.setStatus("current")


class _RstpPerPortInfoStpNeighbor_Type(Integer32):
    """Custom type rstpPerPortInfoStpNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_RstpPerPortInfoStpNeighbor_Type.__name__ = "Integer32"
_RstpPerPortInfoStpNeighbor_Object = MibTableColumn
rstpPerPortInfoStpNeighbor = _RstpPerPortInfoStpNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 6),
    _RstpPerPortInfoStpNeighbor_Type()
)
rstpPerPortInfoStpNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoStpNeighbor.setStatus("current")


class _RstpPerPortInfoState_Type(Integer32):
    """Custom type rstpPerPortInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nonStp", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("disabled", 4),
          ("discarding", 5),
          ("unknown", 6))
    )


_RstpPerPortInfoState_Type.__name__ = "Integer32"
_RstpPerPortInfoState_Object = MibTableColumn
rstpPerPortInfoState = _RstpPerPortInfoState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 7),
    _RstpPerPortInfoState_Type()
)
rstpPerPortInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoState.setStatus("current")


class _RstpPerPortInfoRole_Type(Integer32):
    """Custom type rstpPerPortInfoRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternated", 4),
          ("backup", 5),
          ("nonStp", 6),
          ("unknown", 7))
    )


_RstpPerPortInfoRole_Type.__name__ = "Integer32"
_RstpPerPortInfoRole_Object = MibTableColumn
rstpPerPortInfoRole = _RstpPerPortInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 3, 8, 1, 8),
    _RstpPerPortInfoRole_Type()
)
rstpPerPortInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoRole.setStatus("current")
_Mstp_ObjectIdentity = ObjectIdentity
mstp = _Mstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4)
)


class _MstpStatus_Type(Integer32):
    """Custom type mstpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enalbed", 1),
          ("disabled", 2))
    )


_MstpStatus_Type.__name__ = "Integer32"
_MstpStatus_Object = MibScalar
mstpStatus = _MstpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 1),
    _MstpStatus_Type()
)
mstpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpStatus.setStatus("current")


class _MstpForceVersion_Type(Integer32):
    """Custom type mstpForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("rstp", 2),
          ("mstp", 3))
    )


_MstpForceVersion_Type.__name__ = "Integer32"
_MstpForceVersion_Object = MibScalar
mstpForceVersion = _MstpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 2),
    _MstpForceVersion_Type()
)
mstpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpForceVersion.setStatus("current")


class _MstpConfigurationName_Type(DisplayString):
    """Custom type mstpConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MstpConfigurationName_Type.__name__ = "DisplayString"
_MstpConfigurationName_Object = MibScalar
mstpConfigurationName = _MstpConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 3),
    _MstpConfigurationName_Type()
)
mstpConfigurationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpConfigurationName.setStatus("current")
_MstpRevisionLevel_Type = Integer32
_MstpRevisionLevel_Object = MibScalar
mstpRevisionLevel = _MstpRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 4),
    _MstpRevisionLevel_Type()
)
mstpRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpRevisionLevel.setStatus("current")
_MstpPriority_Type = Integer32
_MstpPriority_Object = MibScalar
mstpPriority = _MstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 5),
    _MstpPriority_Type()
)
mstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPriority.setStatus("current")
_MstpMaxAgeTime_Type = Integer32
_MstpMaxAgeTime_Object = MibScalar
mstpMaxAgeTime = _MstpMaxAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 6),
    _MstpMaxAgeTime_Type()
)
mstpMaxAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpMaxAgeTime.setStatus("current")
_MstpHelloTime_Type = Integer32
_MstpHelloTime_Object = MibScalar
mstpHelloTime = _MstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 7),
    _MstpHelloTime_Type()
)
mstpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpHelloTime.setStatus("current")
_MstpForwardDelayTime_Type = Integer32
_MstpForwardDelayTime_Object = MibScalar
mstpForwardDelayTime = _MstpForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 8),
    _MstpForwardDelayTime_Type()
)
mstpForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpForwardDelayTime.setStatus("current")
_MstpMaxHops_Type = Integer32
_MstpMaxHops_Object = MibScalar
mstpMaxHops = _MstpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 9),
    _MstpMaxHops_Type()
)
mstpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpMaxHops.setStatus("current")
_MstpRootBridgeInformationTable_Object = MibTable
mstpRootBridgeInformationTable = _MstpRootBridgeInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10)
)
if mibBuilder.loadTexts:
    mstpRootBridgeInformationTable.setStatus("current")
_MstpRootBridgeInformationEntry_Object = MibTableRow
mstpRootBridgeInformationEntry = _MstpRootBridgeInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1)
)
mstpRootBridgeInformationEntry.setIndexNames(
    (0, "IES-2206FII", "mstpRootBridgeInformationIndex"),
)
if mibBuilder.loadTexts:
    mstpRootBridgeInformationEntry.setStatus("current")
_MstpRootBridgeInformationIndex_Type = Integer32
_MstpRootBridgeInformationIndex_Object = MibTableColumn
mstpRootBridgeInformationIndex = _MstpRootBridgeInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 1),
    _MstpRootBridgeInformationIndex_Type()
)
mstpRootBridgeInformationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationIndex.setStatus("current")


class _MstpRootBridgeInformationMac_Type(DisplayString):
    """Custom type mstpRootBridgeInformationMac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpRootBridgeInformationMac_Type.__name__ = "DisplayString"
_MstpRootBridgeInformationMac_Object = MibTableColumn
mstpRootBridgeInformationMac = _MstpRootBridgeInformationMac_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 2),
    _MstpRootBridgeInformationMac_Type()
)
mstpRootBridgeInformationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationMac.setStatus("current")
_MstpRootBridgeInformationPriority_Type = Integer32
_MstpRootBridgeInformationPriority_Object = MibTableColumn
mstpRootBridgeInformationPriority = _MstpRootBridgeInformationPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 3),
    _MstpRootBridgeInformationPriority_Type()
)
mstpRootBridgeInformationPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationPriority.setStatus("current")


class _MstpRootBridgeInformationConfigurationName_Type(DisplayString):
    """Custom type mstpRootBridgeInformationConfigurationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpRootBridgeInformationConfigurationName_Type.__name__ = "DisplayString"
_MstpRootBridgeInformationConfigurationName_Object = MibTableColumn
mstpRootBridgeInformationConfigurationName = _MstpRootBridgeInformationConfigurationName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 4),
    _MstpRootBridgeInformationConfigurationName_Type()
)
mstpRootBridgeInformationConfigurationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationConfigurationName.setStatus("current")
_MstpRootBridgeInformationForceVersion_Type = Integer32
_MstpRootBridgeInformationForceVersion_Object = MibTableColumn
mstpRootBridgeInformationForceVersion = _MstpRootBridgeInformationForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 5),
    _MstpRootBridgeInformationForceVersion_Type()
)
mstpRootBridgeInformationForceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationForceVersion.setStatus("current")
_MstpRootBridgeInformationRevisionLevel_Type = Integer32
_MstpRootBridgeInformationRevisionLevel_Object = MibTableColumn
mstpRootBridgeInformationRevisionLevel = _MstpRootBridgeInformationRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 6),
    _MstpRootBridgeInformationRevisionLevel_Type()
)
mstpRootBridgeInformationRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationRevisionLevel.setStatus("current")
_MstpRootBridgeInformationMaxAge_Type = Integer32
_MstpRootBridgeInformationMaxAge_Object = MibTableColumn
mstpRootBridgeInformationMaxAge = _MstpRootBridgeInformationMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 7),
    _MstpRootBridgeInformationMaxAge_Type()
)
mstpRootBridgeInformationMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationMaxAge.setStatus("current")
_MstpRootBridgeInformationHelloTime_Type = Integer32
_MstpRootBridgeInformationHelloTime_Object = MibTableColumn
mstpRootBridgeInformationHelloTime = _MstpRootBridgeInformationHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 8),
    _MstpRootBridgeInformationHelloTime_Type()
)
mstpRootBridgeInformationHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationHelloTime.setStatus("current")
_MstpRootBridgeInformationForwardDelay_Type = Integer32
_MstpRootBridgeInformationForwardDelay_Object = MibTableColumn
mstpRootBridgeInformationForwardDelay = _MstpRootBridgeInformationForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 9),
    _MstpRootBridgeInformationForwardDelay_Type()
)
mstpRootBridgeInformationForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationForwardDelay.setStatus("current")
_MstpRootBridgeInformationMaxHops_Type = Integer32
_MstpRootBridgeInformationMaxHops_Object = MibTableColumn
mstpRootBridgeInformationMaxHops = _MstpRootBridgeInformationMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 10),
    _MstpRootBridgeInformationMaxHops_Type()
)
mstpRootBridgeInformationMaxHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationMaxHops.setStatus("current")
_MstpRootBridgeInformationRootPort_Type = Integer32
_MstpRootBridgeInformationRootPort_Object = MibTableColumn
mstpRootBridgeInformationRootPort = _MstpRootBridgeInformationRootPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 11),
    _MstpRootBridgeInformationRootPort_Type()
)
mstpRootBridgeInformationRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationRootPort.setStatus("current")
_MstpRootBridgeInformationRootPathCost_Type = Integer32
_MstpRootBridgeInformationRootPathCost_Object = MibTableColumn
mstpRootBridgeInformationRootPathCost = _MstpRootBridgeInformationRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 10, 1, 12),
    _MstpRootBridgeInformationRootPathCost_Type()
)
mstpRootBridgeInformationRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpRootBridgeInformationRootPathCost.setStatus("current")
_MstpPerportCfgTable_Object = MibTable
mstpPerportCfgTable = _MstpPerportCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11)
)
if mibBuilder.loadTexts:
    mstpPerportCfgTable.setStatus("current")
_MstpPerportCfgEntry_Object = MibTableRow
mstpPerportCfgEntry = _MstpPerportCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1)
)
mstpPerportCfgEntry.setIndexNames(
    (0, "IES-2206FII", "mstpPerportCfgNum"),
)
if mibBuilder.loadTexts:
    mstpPerportCfgEntry.setStatus("current")
_MstpPerportCfgNum_Type = Integer32
_MstpPerportCfgNum_Object = MibTableColumn
mstpPerportCfgNum = _MstpPerportCfgNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1, 1),
    _MstpPerportCfgNum_Type()
)
mstpPerportCfgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportCfgNum.setStatus("current")
_MstpPerportCfgPriority_Type = Integer32
_MstpPerportCfgPriority_Object = MibTableColumn
mstpPerportCfgPriority = _MstpPerportCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1, 2),
    _MstpPerportCfgPriority_Type()
)
mstpPerportCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPerportCfgPriority.setStatus("current")
_MstpPerportCfgPathCost_Type = Integer32
_MstpPerportCfgPathCost_Object = MibTableColumn
mstpPerportCfgPathCost = _MstpPerportCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1, 3),
    _MstpPerportCfgPathCost_Type()
)
mstpPerportCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPerportCfgPathCost.setStatus("current")
_MstpPerportCfgAdminP2p_Type = Integer32
_MstpPerportCfgAdminP2p_Object = MibTableColumn
mstpPerportCfgAdminP2p = _MstpPerportCfgAdminP2p_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1, 4),
    _MstpPerportCfgAdminP2p_Type()
)
mstpPerportCfgAdminP2p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPerportCfgAdminP2p.setStatus("current")
_MstpPerportCfgAdminEdge_Type = Integer32
_MstpPerportCfgAdminEdge_Object = MibTableColumn
mstpPerportCfgAdminEdge = _MstpPerportCfgAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1, 5),
    _MstpPerportCfgAdminEdge_Type()
)
mstpPerportCfgAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPerportCfgAdminEdge.setStatus("current")
_MstpPerportCfgAdminNonstp_Type = Integer32
_MstpPerportCfgAdminNonstp_Object = MibTableColumn
mstpPerportCfgAdminNonstp = _MstpPerportCfgAdminNonstp_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 11, 1, 6),
    _MstpPerportCfgAdminNonstp_Type()
)
mstpPerportCfgAdminNonstp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPerportCfgAdminNonstp.setStatus("current")
_MstpPerportInfoTable_Object = MibTable
mstpPerportInfoTable = _MstpPerportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12)
)
if mibBuilder.loadTexts:
    mstpPerportInfoTable.setStatus("current")
_MstpPerportInfoEntry_Object = MibTableRow
mstpPerportInfoEntry = _MstpPerportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1)
)
mstpPerportInfoEntry.setIndexNames(
    (0, "IES-2206FII", "mstpPerportInfoNum"),
)
if mibBuilder.loadTexts:
    mstpPerportInfoEntry.setStatus("current")
_MstpPerportInfoNum_Type = Integer32
_MstpPerportInfoNum_Object = MibTableColumn
mstpPerportInfoNum = _MstpPerportInfoNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 1),
    _MstpPerportInfoNum_Type()
)
mstpPerportInfoNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoNum.setStatus("current")
_MstpPerportInfoPriority_Type = Integer32
_MstpPerportInfoPriority_Object = MibTableColumn
mstpPerportInfoPriority = _MstpPerportInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 2),
    _MstpPerportInfoPriority_Type()
)
mstpPerportInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoPriority.setStatus("current")


class _MstpPerportInfoPathCostAdmin_Type(DisplayString):
    """Custom type mstpPerportInfoPathCostAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpPerportInfoPathCostAdmin_Type.__name__ = "DisplayString"
_MstpPerportInfoPathCostAdmin_Object = MibTableColumn
mstpPerportInfoPathCostAdmin = _MstpPerportInfoPathCostAdmin_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 3),
    _MstpPerportInfoPathCostAdmin_Type()
)
mstpPerportInfoPathCostAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoPathCostAdmin.setStatus("current")
_MstpPerportInfoPathCostOper_Type = Integer32
_MstpPerportInfoPathCostOper_Object = MibTableColumn
mstpPerportInfoPathCostOper = _MstpPerportInfoPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 4),
    _MstpPerportInfoPathCostOper_Type()
)
mstpPerportInfoPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoPathCostOper.setStatus("current")


class _MstpPerportInfoP2pAdmin_Type(DisplayString):
    """Custom type mstpPerportInfoP2pAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpPerportInfoP2pAdmin_Type.__name__ = "DisplayString"
_MstpPerportInfoP2pAdmin_Object = MibTableColumn
mstpPerportInfoP2pAdmin = _MstpPerportInfoP2pAdmin_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 5),
    _MstpPerportInfoP2pAdmin_Type()
)
mstpPerportInfoP2pAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoP2pAdmin.setStatus("current")


class _MstpPerportInfoP2pOper_Type(Integer32):
    """Custom type mstpPerportInfoP2pOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MstpPerportInfoP2pOper_Type.__name__ = "Integer32"
_MstpPerportInfoP2pOper_Object = MibTableColumn
mstpPerportInfoP2pOper = _MstpPerportInfoP2pOper_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 6),
    _MstpPerportInfoP2pOper_Type()
)
mstpPerportInfoP2pOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoP2pOper.setStatus("current")


class _MstpPerportInfoEdgeAdmin_Type(Integer32):
    """Custom type mstpPerportInfoEdgeAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MstpPerportInfoEdgeAdmin_Type.__name__ = "Integer32"
_MstpPerportInfoEdgeAdmin_Object = MibTableColumn
mstpPerportInfoEdgeAdmin = _MstpPerportInfoEdgeAdmin_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 7),
    _MstpPerportInfoEdgeAdmin_Type()
)
mstpPerportInfoEdgeAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoEdgeAdmin.setStatus("current")


class _MstpPerportInfoEdgeOper_Type(Integer32):
    """Custom type mstpPerportInfoEdgeOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MstpPerportInfoEdgeOper_Type.__name__ = "Integer32"
_MstpPerportInfoEdgeOper_Object = MibTableColumn
mstpPerportInfoEdgeOper = _MstpPerportInfoEdgeOper_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 8),
    _MstpPerportInfoEdgeOper_Type()
)
mstpPerportInfoEdgeOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoEdgeOper.setStatus("current")


class _MstpPerportInfoNonstpAdmin_Type(Integer32):
    """Custom type mstpPerportInfoNonstpAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_MstpPerportInfoNonstpAdmin_Type.__name__ = "Integer32"
_MstpPerportInfoNonstpAdmin_Object = MibTableColumn
mstpPerportInfoNonstpAdmin = _MstpPerportInfoNonstpAdmin_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 12, 1, 9),
    _MstpPerportInfoNonstpAdmin_Type()
)
mstpPerportInfoNonstpAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPerportInfoNonstpAdmin.setStatus("current")
_MstpInstanceTable_Object = MibTable
mstpInstanceTable = _MstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 13)
)
if mibBuilder.loadTexts:
    mstpInstanceTable.setStatus("current")
_MstpInstanceEntry_Object = MibTableRow
mstpInstanceEntry = _MstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 13, 1)
)
mstpInstanceEntry.setIndexNames(
    (0, "IES-2206FII", "mstpInstanceNum"),
)
if mibBuilder.loadTexts:
    mstpInstanceEntry.setStatus("current")
_MstpInstanceNum_Type = Integer32
_MstpInstanceNum_Object = MibTableColumn
mstpInstanceNum = _MstpInstanceNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 13, 1, 1),
    _MstpInstanceNum_Type()
)
mstpInstanceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceNum.setStatus("current")


class _MstpInstanceState_Type(Integer32):
    """Custom type mstpInstanceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enalbed", 1),
          ("disabled", 2))
    )


_MstpInstanceState_Type.__name__ = "Integer32"
_MstpInstanceState_Object = MibTableColumn
mstpInstanceState = _MstpInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 13, 1, 2),
    _MstpInstanceState_Type()
)
mstpInstanceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpInstanceState.setStatus("current")


class _MstpInstanceVlans_Type(DisplayString):
    """Custom type mstpInstanceVlans based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpInstanceVlans_Type.__name__ = "DisplayString"
_MstpInstanceVlans_Object = MibTableColumn
mstpInstanceVlans = _MstpInstanceVlans_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 13, 1, 3),
    _MstpInstanceVlans_Type()
)
mstpInstanceVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpInstanceVlans.setStatus("current")
_MstpInstancePriority_Type = Integer32
_MstpInstancePriority_Object = MibTableColumn
mstpInstancePriority = _MstpInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 13, 1, 4),
    _MstpInstancePriority_Type()
)
mstpInstancePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpInstancePriority.setStatus("current")
_MstpInstanceInfoTable_Object = MibTable
mstpInstanceInfoTable = _MstpInstanceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14)
)
if mibBuilder.loadTexts:
    mstpInstanceInfoTable.setStatus("current")
_MstpInstanceInfoEntry_Object = MibTableRow
mstpInstanceInfoEntry = _MstpInstanceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1)
)
mstpInstanceInfoEntry.setIndexNames(
    (0, "IES-2206FII", "mstpInstanceInfonNum"),
)
if mibBuilder.loadTexts:
    mstpInstanceInfoEntry.setStatus("current")
_MstpInstanceInfonNum_Type = Integer32
_MstpInstanceInfonNum_Object = MibTableColumn
mstpInstanceInfonNum = _MstpInstanceInfonNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1, 1),
    _MstpInstanceInfonNum_Type()
)
mstpInstanceInfonNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceInfonNum.setStatus("current")


class _MstpInstanceInfoVlans_Type(DisplayString):
    """Custom type mstpInstanceInfoVlans based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpInstanceInfoVlans_Type.__name__ = "DisplayString"
_MstpInstanceInfoVlans_Object = MibTableColumn
mstpInstanceInfoVlans = _MstpInstanceInfoVlans_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1, 2),
    _MstpInstanceInfoVlans_Type()
)
mstpInstanceInfoVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceInfoVlans.setStatus("current")
_MstpInstanceInfoPriority_Type = Integer32
_MstpInstanceInfoPriority_Object = MibTableColumn
mstpInstanceInfoPriority = _MstpInstanceInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1, 3),
    _MstpInstanceInfoPriority_Type()
)
mstpInstanceInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceInfoPriority.setStatus("current")


class _MstpInstanceInfoRegionalRootBridgeId_Type(DisplayString):
    """Custom type mstpInstanceInfoRegionalRootBridgeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpInstanceInfoRegionalRootBridgeId_Type.__name__ = "DisplayString"
_MstpInstanceInfoRegionalRootBridgeId_Object = MibTableColumn
mstpInstanceInfoRegionalRootBridgeId = _MstpInstanceInfoRegionalRootBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1, 4),
    _MstpInstanceInfoRegionalRootBridgeId_Type()
)
mstpInstanceInfoRegionalRootBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceInfoRegionalRootBridgeId.setStatus("current")
_MstpInstanceInfoPathCost_Type = Integer32
_MstpInstanceInfoPathCost_Object = MibTableColumn
mstpInstanceInfoPathCost = _MstpInstanceInfoPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1, 5),
    _MstpInstanceInfoPathCost_Type()
)
mstpInstanceInfoPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceInfoPathCost.setStatus("current")


class _MstpInstanceInfoRootPort_Type(DisplayString):
    """Custom type mstpInstanceInfoRootPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpInstanceInfoRootPort_Type.__name__ = "DisplayString"
_MstpInstanceInfoRootPort_Object = MibTableColumn
mstpInstanceInfoRootPort = _MstpInstanceInfoRootPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 14, 1, 6),
    _MstpInstanceInfoRootPort_Type()
)
mstpInstanceInfoRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstanceInfoRootPort.setStatus("current")
_MstpInstancePortTable_Object = MibTable
mstpInstancePortTable = _MstpInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 15)
)
if mibBuilder.loadTexts:
    mstpInstancePortTable.setStatus("current")
_MstpInstancePortEntry_Object = MibTableRow
mstpInstancePortEntry = _MstpInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 15, 1)
)
mstpInstancePortEntry.setIndexNames(
    (0, "IES-2206FII", "mstpInstancePortNum"),
    (0, "IES-2206FII", "mstpInstancePortPortId"),
)
if mibBuilder.loadTexts:
    mstpInstancePortEntry.setStatus("current")
_MstpInstancePortNum_Type = Integer32
_MstpInstancePortNum_Object = MibTableColumn
mstpInstancePortNum = _MstpInstancePortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 15, 1, 1),
    _MstpInstancePortNum_Type()
)
mstpInstancePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortNum.setStatus("current")
_MstpInstancePortPortId_Type = Integer32
_MstpInstancePortPortId_Object = MibTableColumn
mstpInstancePortPortId = _MstpInstancePortPortId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 15, 1, 2),
    _MstpInstancePortPortId_Type()
)
mstpInstancePortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortPortId.setStatus("current")
_MstpInstancePortPriority_Type = Integer32
_MstpInstancePortPriority_Object = MibTableColumn
mstpInstancePortPriority = _MstpInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 15, 1, 3),
    _MstpInstancePortPriority_Type()
)
mstpInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpInstancePortPriority.setStatus("current")
_MstpInstancePortPathCost_Type = Integer32
_MstpInstancePortPathCost_Object = MibTableColumn
mstpInstancePortPathCost = _MstpInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 15, 1, 4),
    _MstpInstancePortPathCost_Type()
)
mstpInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpInstancePortPathCost.setStatus("current")
_MstpInstancePortInformationTable_Object = MibTable
mstpInstancePortInformationTable = _MstpInstancePortInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16)
)
if mibBuilder.loadTexts:
    mstpInstancePortInformationTable.setStatus("current")
_MstpInstancePortInformationEntry_Object = MibTableRow
mstpInstancePortInformationEntry = _MstpInstancePortInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1)
)
mstpInstancePortInformationEntry.setIndexNames(
    (0, "IES-2206FII", "mstpInstancePortInformationNum"),
    (0, "IES-2206FII", "mstpInstancePortInformationPortId"),
)
if mibBuilder.loadTexts:
    mstpInstancePortInformationEntry.setStatus("current")
_MstpInstancePortInformationNum_Type = Integer32
_MstpInstancePortInformationNum_Object = MibTableColumn
mstpInstancePortInformationNum = _MstpInstancePortInformationNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 1),
    _MstpInstancePortInformationNum_Type()
)
mstpInstancePortInformationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationNum.setStatus("current")
_MstpInstancePortInformationPortId_Type = Integer32
_MstpInstancePortInformationPortId_Object = MibTableColumn
mstpInstancePortInformationPortId = _MstpInstancePortInformationPortId_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 2),
    _MstpInstancePortInformationPortId_Type()
)
mstpInstancePortInformationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationPortId.setStatus("current")
_MstpInstancePortInformationPriority_Type = Integer32
_MstpInstancePortInformationPriority_Object = MibTableColumn
mstpInstancePortInformationPriority = _MstpInstancePortInformationPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 3),
    _MstpInstancePortInformationPriority_Type()
)
mstpInstancePortInformationPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationPriority.setStatus("current")
_MstpInstancePortInformationPathCostAdmin_Type = Integer32
_MstpInstancePortInformationPathCostAdmin_Object = MibTableColumn
mstpInstancePortInformationPathCostAdmin = _MstpInstancePortInformationPathCostAdmin_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 4),
    _MstpInstancePortInformationPathCostAdmin_Type()
)
mstpInstancePortInformationPathCostAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationPathCostAdmin.setStatus("current")
_MstpInstancePortInformationPathCostOper_Type = Integer32
_MstpInstancePortInformationPathCostOper_Object = MibTableColumn
mstpInstancePortInformationPathCostOper = _MstpInstancePortInformationPathCostOper_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 5),
    _MstpInstancePortInformationPathCostOper_Type()
)
mstpInstancePortInformationPathCostOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationPathCostOper.setStatus("current")


class _MstpInstancePortInformationState_Type(Integer32):
    """Custom type mstpInstancePortInformationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("discarding", 1),
          ("learning", 2),
          ("forwarding", 3),
          ("nonStp", 4))
    )


_MstpInstancePortInformationState_Type.__name__ = "Integer32"
_MstpInstancePortInformationState_Object = MibTableColumn
mstpInstancePortInformationState = _MstpInstancePortInformationState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 6),
    _MstpInstancePortInformationState_Type()
)
mstpInstancePortInformationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationState.setStatus("current")


class _MstpInstancePortInformationRole_Type(DisplayString):
    """Custom type mstpInstancePortInformationRole based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MstpInstancePortInformationRole_Type.__name__ = "DisplayString"
_MstpInstancePortInformationRole_Object = MibTableColumn
mstpInstancePortInformationRole = _MstpInstancePortInformationRole_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 5, 4, 16, 1, 7),
    _MstpInstancePortInformationRole_Type()
)
mstpInstancePortInformationRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpInstancePortInformationRole.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6)
)


class _VlanOperationMode_Type(Integer32):
    """Custom type vlanOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021q", 1),
          ("portbased", 2),
          ("disabled", 3))
    )


_VlanOperationMode_Type.__name__ = "Integer32"
_VlanOperationMode_Object = MibScalar
vlanOperationMode = _VlanOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 1),
    _VlanOperationMode_Type()
)
vlanOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanOperationMode.setStatus("current")


class _VlanGVRP_Type(Integer32):
    """Custom type vlanGVRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_VlanGVRP_Type.__name__ = "Integer32"
_VlanGVRP_Object = MibScalar
vlanGVRP = _VlanGVRP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 2),
    _VlanGVRP_Type()
)
vlanGVRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanGVRP.setStatus("current")
_VlanIEEE8021QTable_Object = MibTable
vlanIEEE8021QTable = _VlanIEEE8021QTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3)
)
if mibBuilder.loadTexts:
    vlanIEEE8021QTable.setStatus("current")
_VlanIEEE8021QEntry_Object = MibTableRow
vlanIEEE8021QEntry = _VlanIEEE8021QEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3, 1)
)
vlanIEEE8021QEntry.setIndexNames(
    (0, "IES-2206FII", "vlanIEEE8021QIndex"),
)
if mibBuilder.loadTexts:
    vlanIEEE8021QEntry.setStatus("current")
_VlanIEEE8021QIndex_Type = Integer32
_VlanIEEE8021QIndex_Object = MibTableColumn
vlanIEEE8021QIndex = _VlanIEEE8021QIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3, 1, 1),
    _VlanIEEE8021QIndex_Type()
)
vlanIEEE8021QIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIEEE8021QIndex.setStatus("current")


class _VlanIEEE8021QPortName_Type(DisplayString):
    """Custom type vlanIEEE8021QPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanIEEE8021QPortName_Type.__name__ = "DisplayString"
_VlanIEEE8021QPortName_Object = MibTableColumn
vlanIEEE8021QPortName = _VlanIEEE8021QPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3, 1, 2),
    _VlanIEEE8021QPortName_Type()
)
vlanIEEE8021QPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIEEE8021QPortName.setStatus("current")


class _VlanIEEE8021QLinkType_Type(Integer32):
    """Custom type vlanIEEE8021QLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accesslink", 1),
          ("trunklink", 2),
          ("hybridlink", 3))
    )


_VlanIEEE8021QLinkType_Type.__name__ = "Integer32"
_VlanIEEE8021QLinkType_Object = MibTableColumn
vlanIEEE8021QLinkType = _VlanIEEE8021QLinkType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3, 1, 3),
    _VlanIEEE8021QLinkType_Type()
)
vlanIEEE8021QLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QLinkType.setStatus("current")
_VlanIEEE8021QUntaggedVid_Type = Integer32
_VlanIEEE8021QUntaggedVid_Object = MibTableColumn
vlanIEEE8021QUntaggedVid = _VlanIEEE8021QUntaggedVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3, 1, 4),
    _VlanIEEE8021QUntaggedVid_Type()
)
vlanIEEE8021QUntaggedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QUntaggedVid.setStatus("current")


class _VlanIEEE8021QTaggedVids_Type(DisplayString):
    """Custom type vlanIEEE8021QTaggedVids based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanIEEE8021QTaggedVids_Type.__name__ = "DisplayString"
_VlanIEEE8021QTaggedVids_Object = MibTableColumn
vlanIEEE8021QTaggedVids = _VlanIEEE8021QTaggedVids_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 3, 1, 5),
    _VlanIEEE8021QTaggedVids_Type()
)
vlanIEEE8021QTaggedVids.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QTaggedVids.setStatus("current")
_VlanIEEE8021QGroupTable_Object = MibTable
vlanIEEE8021QGroupTable = _VlanIEEE8021QGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 4)
)
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupTable.setStatus("current")
_VlanIEEE8021QGroupEntry_Object = MibTableRow
vlanIEEE8021QGroupEntry = _VlanIEEE8021QGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 4, 1)
)
vlanIEEE8021QGroupEntry.setIndexNames(
    (0, "IES-2206FII", "vlanIEEE8021QGroupVid"),
)
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupEntry.setStatus("current")
_VlanIEEE8021QGroupVid_Type = Integer32
_VlanIEEE8021QGroupVid_Object = MibTableColumn
vlanIEEE8021QGroupVid = _VlanIEEE8021QGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 4, 1, 1),
    _VlanIEEE8021QGroupVid_Type()
)
vlanIEEE8021QGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupVid.setStatus("current")


class _VlanIEEE8021QGroupName_Type(DisplayString):
    """Custom type vlanIEEE8021QGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanIEEE8021QGroupName_Type.__name__ = "DisplayString"
_VlanIEEE8021QGroupName_Object = MibTableColumn
vlanIEEE8021QGroupName = _VlanIEEE8021QGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 4, 1, 2),
    _VlanIEEE8021QGroupName_Type()
)
vlanIEEE8021QGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupName.setStatus("current")


class _VlanIEEE8021QGroupStatus_Type(Integer32):
    """Custom type vlanIEEE8021QGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_VlanIEEE8021QGroupStatus_Type.__name__ = "Integer32"
_VlanIEEE8021QGroupStatus_Object = MibTableColumn
vlanIEEE8021QGroupStatus = _VlanIEEE8021QGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 4, 1, 3),
    _VlanIEEE8021QGroupStatus_Type()
)
vlanIEEE8021QGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIEEE8021QGroupStatus.setStatus("current")
_VlanPortBasedTable_Object = MibTable
vlanPortBasedTable = _VlanPortBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5)
)
if mibBuilder.loadTexts:
    vlanPortBasedTable.setStatus("current")
_VlanPortBasedEntry_Object = MibTableRow
vlanPortBasedEntry = _VlanPortBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5, 1)
)
vlanPortBasedEntry.setIndexNames(
    (0, "IES-2206FII", "vlanPortBasedIndex"),
)
if mibBuilder.loadTexts:
    vlanPortBasedEntry.setStatus("current")
_VlanPortBasedIndex_Type = Integer32
_VlanPortBasedIndex_Object = MibTableColumn
vlanPortBasedIndex = _VlanPortBasedIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5, 1, 1),
    _VlanPortBasedIndex_Type()
)
vlanPortBasedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortBasedIndex.setStatus("current")


class _VlanPortBasedGroupName_Type(DisplayString):
    """Custom type vlanPortBasedGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlanPortBasedGroupName_Type.__name__ = "DisplayString"
_VlanPortBasedGroupName_Object = MibTableColumn
vlanPortBasedGroupName = _VlanPortBasedGroupName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5, 1, 2),
    _VlanPortBasedGroupName_Type()
)
vlanPortBasedGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedGroupName.setStatus("current")
_VlanPortBasedVid_Type = Integer32
_VlanPortBasedVid_Object = MibTableColumn
vlanPortBasedVid = _VlanPortBasedVid_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5, 1, 3),
    _VlanPortBasedVid_Type()
)
vlanPortBasedVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedVid.setStatus("current")
_VlanPortBasedMembers_Type = PortList
_VlanPortBasedMembers_Object = MibTableColumn
vlanPortBasedMembers = _VlanPortBasedMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5, 1, 4),
    _VlanPortBasedMembers_Type()
)
vlanPortBasedMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedMembers.setStatus("current")


class _VlanPortBasedStatus_Type(Integer32):
    """Custom type vlanPortBasedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_VlanPortBasedStatus_Type.__name__ = "Integer32"
_VlanPortBasedStatus_Object = MibTableColumn
vlanPortBasedStatus = _VlanPortBasedStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 6, 5, 1, 5),
    _VlanPortBasedStatus_Type()
)
vlanPortBasedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedStatus.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7)
)


class _SnmpAgentMode_Type(Integer32):
    """Custom type snmpAgentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1v2Conly", 1),
          ("v3", 2))
    )


_SnmpAgentMode_Type.__name__ = "Integer32"
_SnmpAgentMode_Object = MibScalar
snmpAgentMode = _SnmpAgentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 1),
    _SnmpAgentMode_Type()
)
snmpAgentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentMode.setStatus("current")


class _SnmpSystemName_Type(DisplayString):
    """Custom type snmpSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpSystemName_Type.__name__ = "DisplayString"
_SnmpSystemName_Object = MibScalar
snmpSystemName = _SnmpSystemName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 2),
    _SnmpSystemName_Type()
)
snmpSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemName.setStatus("current")


class _SnmpSystemLocation_Type(DisplayString):
    """Custom type snmpSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpSystemLocation_Type.__name__ = "DisplayString"
_SnmpSystemLocation_Object = MibScalar
snmpSystemLocation = _SnmpSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 3),
    _SnmpSystemLocation_Type()
)
snmpSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemLocation.setStatus("current")


class _SnmpSystemContact_Type(DisplayString):
    """Custom type snmpSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SnmpSystemContact_Type.__name__ = "DisplayString"
_SnmpSystemContact_Object = MibScalar
snmpSystemContact = _SnmpSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 4),
    _SnmpSystemContact_Type()
)
snmpSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemContact.setStatus("current")
_SnmpCommunityStringTable_Object = MibTable
snmpCommunityStringTable = _SnmpCommunityStringTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 5)
)
if mibBuilder.loadTexts:
    snmpCommunityStringTable.setStatus("current")
_SnmpCommunityStringEntry_Object = MibTableRow
snmpCommunityStringEntry = _SnmpCommunityStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 5, 1)
)
snmpCommunityStringEntry.setIndexNames(
    (0, "IES-2206FII", "snmpCommunityStringIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityStringEntry.setStatus("current")
_SnmpCommunityStringIndex_Type = Integer32
_SnmpCommunityStringIndex_Object = MibTableColumn
snmpCommunityStringIndex = _SnmpCommunityStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 5, 1, 1),
    _SnmpCommunityStringIndex_Type()
)
snmpCommunityStringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpCommunityStringIndex.setStatus("current")


class _SnmpCommunityStringName_Type(DisplayString):
    """Custom type snmpCommunityStringName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpCommunityStringName_Type.__name__ = "DisplayString"
_SnmpCommunityStringName_Object = MibTableColumn
snmpCommunityStringName = _SnmpCommunityStringName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 5, 1, 2),
    _SnmpCommunityStringName_Type()
)
snmpCommunityStringName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityStringName.setStatus("current")


class _SnmpCommunityStringAttribute_Type(Integer32):
    """Custom type snmpCommunityStringAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ro", 1),
          ("rw", 2))
    )


_SnmpCommunityStringAttribute_Type.__name__ = "Integer32"
_SnmpCommunityStringAttribute_Object = MibTableColumn
snmpCommunityStringAttribute = _SnmpCommunityStringAttribute_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 5, 1, 3),
    _SnmpCommunityStringAttribute_Type()
)
snmpCommunityStringAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpCommunityStringAttribute.setStatus("current")


class _SnmpCommunityStringStatus_Type(Integer32):
    """Custom type snmpCommunityStringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_SnmpCommunityStringStatus_Type.__name__ = "Integer32"
_SnmpCommunityStringStatus_Object = MibTableColumn
snmpCommunityStringStatus = _SnmpCommunityStringStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 5, 1, 4),
    _SnmpCommunityStringStatus_Type()
)
snmpCommunityStringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStringStatus.setStatus("current")
_SnmpTrapServerTable_Object = MibTable
snmpTrapServerTable = _SnmpTrapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6)
)
if mibBuilder.loadTexts:
    snmpTrapServerTable.setStatus("current")
_SnmpTrapServerEntry_Object = MibTableRow
snmpTrapServerEntry = _SnmpTrapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6, 1)
)
snmpTrapServerEntry.setIndexNames(
    (0, "IES-2206FII", "snmpTrapServerIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapServerEntry.setStatus("current")
_SnmpTrapServerIndex_Type = Integer32
_SnmpTrapServerIndex_Object = MibTableColumn
snmpTrapServerIndex = _SnmpTrapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6, 1, 1),
    _SnmpTrapServerIndex_Type()
)
snmpTrapServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapServerIndex.setStatus("current")
_SnmpTrapServerIPAddr_Type = IpAddress
_SnmpTrapServerIPAddr_Object = MibTableColumn
snmpTrapServerIPAddr = _SnmpTrapServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6, 1, 2),
    _SnmpTrapServerIPAddr_Type()
)
snmpTrapServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerIPAddr.setStatus("current")


class _SnmpTrapServerTrapComm_Type(DisplayString):
    """Custom type snmpTrapServerTrapComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpTrapServerTrapComm_Type.__name__ = "DisplayString"
_SnmpTrapServerTrapComm_Object = MibTableColumn
snmpTrapServerTrapComm = _SnmpTrapServerTrapComm_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6, 1, 3),
    _SnmpTrapServerTrapComm_Type()
)
snmpTrapServerTrapComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerTrapComm.setStatus("current")


class _SnmpTrapServerTrapVer_Type(Integer32):
    """Custom type snmpTrapServerTrapVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2))
    )


_SnmpTrapServerTrapVer_Type.__name__ = "Integer32"
_SnmpTrapServerTrapVer_Object = MibTableColumn
snmpTrapServerTrapVer = _SnmpTrapServerTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6, 1, 4),
    _SnmpTrapServerTrapVer_Type()
)
snmpTrapServerTrapVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapServerTrapVer.setStatus("current")


class _SnmpTrapServerStatus_Type(Integer32):
    """Custom type snmpTrapServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_SnmpTrapServerStatus_Type.__name__ = "Integer32"
_SnmpTrapServerStatus_Object = MibTableColumn
snmpTrapServerStatus = _SnmpTrapServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 7, 6, 1, 5),
    _SnmpTrapServerStatus_Type()
)
snmpTrapServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapServerStatus.setStatus("current")
_TrafficPrioritization_ObjectIdentity = ObjectIdentity
trafficPrioritization = _TrafficPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8)
)


class _QosPolicy_Type(Integer32):
    """Custom type qosPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("an_8_4_2_1_weighted_fair_queuing_scheme", 1),
          ("a_strict_priority_scheme", 2))
    )


_QosPolicy_Type.__name__ = "Integer32"
_QosPolicy_Object = MibScalar
qosPolicy = _QosPolicy_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 1),
    _QosPolicy_Type()
)
qosPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPolicy.setStatus("current")


class _QosPriorityType_Type(Integer32):
    """Custom type qosPriorityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("port-base", 1),
          ("cos-only", 2),
          ("tos-only", 3),
          ("cos-first", 4),
          ("tos-first", 5),
          ("disabled", 6))
    )


_QosPriorityType_Type.__name__ = "Integer32"
_QosPriorityType_Object = MibScalar
qosPriorityType = _QosPriorityType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 2),
    _QosPriorityType_Type()
)
qosPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityType.setStatus("current")
_QosPortBasedPriorityTable_Object = MibTable
qosPortBasedPriorityTable = _QosPortBasedPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 3)
)
if mibBuilder.loadTexts:
    qosPortBasedPriorityTable.setStatus("current")
_QosPortBasedPriorityEntry_Object = MibTableRow
qosPortBasedPriorityEntry = _QosPortBasedPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 3, 1)
)
qosPortBasedPriorityEntry.setIndexNames(
    (0, "IES-2206FII", "qosPortBasedPriorityPortNum"),
)
if mibBuilder.loadTexts:
    qosPortBasedPriorityEntry.setStatus("current")
_QosPortBasedPriorityPortNum_Type = Integer32
_QosPortBasedPriorityPortNum_Object = MibTableColumn
qosPortBasedPriorityPortNum = _QosPortBasedPriorityPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 3, 1, 1),
    _QosPortBasedPriorityPortNum_Type()
)
qosPortBasedPriorityPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosPortBasedPriorityPortNum.setStatus("current")


class _QosPortBasedPriority_Type(Integer32):
    """Custom type qosPortBasedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lowest", 1),
          ("low", 2),
          ("middle", 3),
          ("high", 4))
    )


_QosPortBasedPriority_Type.__name__ = "Integer32"
_QosPortBasedPriority_Object = MibTableColumn
qosPortBasedPriority = _QosPortBasedPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 3, 1, 2),
    _QosPortBasedPriority_Type()
)
qosPortBasedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortBasedPriority.setStatus("current")
_QosCOSTable_Object = MibTable
qosCOSTable = _QosCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 4)
)
if mibBuilder.loadTexts:
    qosCOSTable.setStatus("current")
_QosCOSEntry_Object = MibTableRow
qosCOSEntry = _QosCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 4, 1)
)
qosCOSEntry.setIndexNames(
    (0, "IES-2206FII", "qosCOSPriority"),
)
if mibBuilder.loadTexts:
    qosCOSEntry.setStatus("current")
_QosCOSPriority_Type = Integer32
_QosCOSPriority_Object = MibTableColumn
qosCOSPriority = _QosCOSPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 4, 1, 1),
    _QosCOSPriority_Type()
)
qosCOSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCOSPriority.setStatus("current")


class _QosCOS_Type(Integer32):
    """Custom type qosCOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lowest", 1),
          ("low", 2),
          ("middle", 3),
          ("high", 4))
    )


_QosCOS_Type.__name__ = "Integer32"
_QosCOS_Object = MibTableColumn
qosCOS = _QosCOS_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 4, 1, 2),
    _QosCOS_Type()
)
qosCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCOS.setStatus("current")
_QosCOSPortDefaultTable_Object = MibTable
qosCOSPortDefaultTable = _QosCOSPortDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 5)
)
if mibBuilder.loadTexts:
    qosCOSPortDefaultTable.setStatus("current")
_QosCOSPortDefaultEntry_Object = MibTableRow
qosCOSPortDefaultEntry = _QosCOSPortDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 5, 1)
)
qosCOSPortDefaultEntry.setIndexNames(
    (0, "IES-2206FII", "qosCOSPriority"),
)
if mibBuilder.loadTexts:
    qosCOSPortDefaultEntry.setStatus("current")
_QosCOSPort_Type = Integer32
_QosCOSPort_Object = MibTableColumn
qosCOSPort = _QosCOSPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 5, 1, 1),
    _QosCOSPort_Type()
)
qosCOSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCOSPort.setStatus("current")
_QosCOSPortDefault_Type = Integer32
_QosCOSPortDefault_Object = MibTableColumn
qosCOSPortDefault = _QosCOSPortDefault_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 5, 1, 2),
    _QosCOSPortDefault_Type()
)
qosCOSPortDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCOSPortDefault.setStatus("current")
_QosTOSTable_Object = MibTable
qosTOSTable = _QosTOSTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 6)
)
if mibBuilder.loadTexts:
    qosTOSTable.setStatus("current")
_QosTOSEntry_Object = MibTableRow
qosTOSEntry = _QosTOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 6, 1)
)
qosTOSEntry.setIndexNames(
    (0, "IES-2206FII", "qosTOSPriority"),
)
if mibBuilder.loadTexts:
    qosTOSEntry.setStatus("current")
_QosTOSPriority_Type = Integer32
_QosTOSPriority_Object = MibTableColumn
qosTOSPriority = _QosTOSPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 6, 1, 1),
    _QosTOSPriority_Type()
)
qosTOSPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTOSPriority.setStatus("current")


class _QosTOS_Type(Integer32):
    """Custom type qosTOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lowest", 1),
          ("low", 2),
          ("middle", 3),
          ("high", 4))
    )


_QosTOS_Type.__name__ = "Integer32"
_QosTOS_Object = MibTableColumn
qosTOS = _QosTOS_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 8, 6, 1, 2),
    _QosTOS_Type()
)
qosTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOS.setStatus("current")
_Multicast_ObjectIdentity = ObjectIdentity
multicast = _Multicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9)
)
_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1)
)


class _IgmpStatus_Type(Integer32):
    """Custom type igmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpv2", 1),
          ("igmpv3", 2),
          ("disabled", 3))
    )


_IgmpStatus_Type.__name__ = "Integer32"
_IgmpStatus_Object = MibScalar
igmpStatus = _IgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 1),
    _IgmpStatus_Type()
)
igmpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpStatus.setStatus("current")


class _IgmpQuery_Type(Integer32):
    """Custom type igmpQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_IgmpQuery_Type.__name__ = "Integer32"
_IgmpQuery_Object = MibScalar
igmpQuery = _IgmpQuery_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 2),
    _IgmpQuery_Type()
)
igmpQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpQuery.setStatus("current")
_IgmpEntriesTable_Object = MibTable
igmpEntriesTable = _IgmpEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 3)
)
if mibBuilder.loadTexts:
    igmpEntriesTable.setStatus("current")
_IgmpEntriesEntry_Object = MibTableRow
igmpEntriesEntry = _IgmpEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 3, 1)
)
igmpEntriesEntry.setIndexNames(
    (0, "IES-2206FII", "igmpEntriesEntryIndex"),
)
if mibBuilder.loadTexts:
    igmpEntriesEntry.setStatus("current")
_IgmpEntriesEntryIndex_Type = Integer32
_IgmpEntriesEntryIndex_Object = MibTableColumn
igmpEntriesEntryIndex = _IgmpEntriesEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 3, 1, 1),
    _IgmpEntriesEntryIndex_Type()
)
igmpEntriesEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryIndex.setStatus("current")
_IgmpEntriesEntryIPAddr_Type = IpAddress
_IgmpEntriesEntryIPAddr_Object = MibTableColumn
igmpEntriesEntryIPAddr = _IgmpEntriesEntryIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 3, 1, 2),
    _IgmpEntriesEntryIPAddr_Type()
)
igmpEntriesEntryIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryIPAddr.setStatus("current")
_IgmpEntriesEntryVID_Type = Integer32
_IgmpEntriesEntryVID_Object = MibTableColumn
igmpEntriesEntryVID = _IgmpEntriesEntryVID_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 3, 1, 3),
    _IgmpEntriesEntryVID_Type()
)
igmpEntriesEntryVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryVID.setStatus("current")
_IgmpEntriesEntryMembers_Type = PortList
_IgmpEntriesEntryMembers_Object = MibTableColumn
igmpEntriesEntryMembers = _IgmpEntriesEntryMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 1, 3, 1, 4),
    _IgmpEntriesEntryMembers_Type()
)
igmpEntriesEntryMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpEntriesEntryMembers.setStatus("current")
_Multicastfiltering_ObjectIdentity = ObjectIdentity
multicastfiltering = _Multicastfiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3)
)
_MulticastfilteringEntriesTable_Object = MibTable
multicastfilteringEntriesTable = _MulticastfilteringEntriesTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3, 1)
)
if mibBuilder.loadTexts:
    multicastfilteringEntriesTable.setStatus("current")
_MulticastfilteringEntriesEntry_Object = MibTableRow
multicastfilteringEntriesEntry = _MulticastfilteringEntriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3, 1, 1)
)
multicastfilteringEntriesEntry.setIndexNames(
    (0, "IES-2206FII", "multicastFilteringIndex"),
)
if mibBuilder.loadTexts:
    multicastfilteringEntriesEntry.setStatus("current")
_MulticastFilteringIndex_Type = Integer32
_MulticastFilteringIndex_Object = MibTableColumn
multicastFilteringIndex = _MulticastFilteringIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3, 1, 1, 1),
    _MulticastFilteringIndex_Type()
)
multicastFilteringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    multicastFilteringIndex.setStatus("current")
_MulticastFilteringAddr_Type = IpAddress
_MulticastFilteringAddr_Object = MibTableColumn
multicastFilteringAddr = _MulticastFilteringAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3, 1, 1, 2),
    _MulticastFilteringAddr_Type()
)
multicastFilteringAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastFilteringAddr.setStatus("current")
_MulticastFilteringMemberports_Type = PortList
_MulticastFilteringMemberports_Object = MibTableColumn
multicastFilteringMemberports = _MulticastFilteringMemberports_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3, 1, 1, 3),
    _MulticastFilteringMemberports_Type()
)
multicastFilteringMemberports.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastFilteringMemberports.setStatus("current")


class _MulticastFilteringStatus_Type(Integer32):
    """Custom type multicastFilteringStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_MulticastFilteringStatus_Type.__name__ = "Integer32"
_MulticastFilteringStatus_Object = MibTableColumn
multicastFilteringStatus = _MulticastFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 9, 3, 1, 1, 4),
    _MulticastFilteringStatus_Type()
)
multicastFilteringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastFilteringStatus.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10)
)
_IpSecurityMgt_ObjectIdentity = ObjectIdentity
ipSecurityMgt = _IpSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1)
)


class _IpSecurityStatus_Type(Integer32):
    """Custom type ipSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityStatus_Type.__name__ = "Integer32"
_IpSecurityStatus_Object = MibScalar
ipSecurityStatus = _IpSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 1),
    _IpSecurityStatus_Type()
)
ipSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityStatus.setStatus("current")


class _IpSecurityHTTPServerStatus_Type(Integer32):
    """Custom type ipSecurityHTTPServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityHTTPServerStatus_Type.__name__ = "Integer32"
_IpSecurityHTTPServerStatus_Object = MibScalar
ipSecurityHTTPServerStatus = _IpSecurityHTTPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 2),
    _IpSecurityHTTPServerStatus_Type()
)
ipSecurityHTTPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityHTTPServerStatus.setStatus("current")


class _IpSecurityTelnetServerStatus_Type(Integer32):
    """Custom type ipSecurityTelnetServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecurityTelnetServerStatus_Type.__name__ = "Integer32"
_IpSecurityTelnetServerStatus_Object = MibScalar
ipSecurityTelnetServerStatus = _IpSecurityTelnetServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 3),
    _IpSecurityTelnetServerStatus_Type()
)
ipSecurityTelnetServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecurityTelnetServerStatus.setStatus("current")


class _IpSecuritySNMPServerStatus_Type(Integer32):
    """Custom type ipSecuritySNMPServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_IpSecuritySNMPServerStatus_Type.__name__ = "Integer32"
_IpSecuritySNMPServerStatus_Object = MibScalar
ipSecuritySNMPServerStatus = _IpSecuritySNMPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 4),
    _IpSecuritySNMPServerStatus_Type()
)
ipSecuritySNMPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySNMPServerStatus.setStatus("current")
_IpSecuritySecurityIP1_Type = IpAddress
_IpSecuritySecurityIP1_Object = MibScalar
ipSecuritySecurityIP1 = _IpSecuritySecurityIP1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 5),
    _IpSecuritySecurityIP1_Type()
)
ipSecuritySecurityIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP1.setStatus("current")
_IpSecuritySecurityIP2_Type = IpAddress
_IpSecuritySecurityIP2_Object = MibScalar
ipSecuritySecurityIP2 = _IpSecuritySecurityIP2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 6),
    _IpSecuritySecurityIP2_Type()
)
ipSecuritySecurityIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP2.setStatus("current")
_IpSecuritySecurityIP3_Type = IpAddress
_IpSecuritySecurityIP3_Object = MibScalar
ipSecuritySecurityIP3 = _IpSecuritySecurityIP3_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 7),
    _IpSecuritySecurityIP3_Type()
)
ipSecuritySecurityIP3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP3.setStatus("current")
_IpSecuritySecurityIP4_Type = IpAddress
_IpSecuritySecurityIP4_Object = MibScalar
ipSecuritySecurityIP4 = _IpSecuritySecurityIP4_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 8),
    _IpSecuritySecurityIP4_Type()
)
ipSecuritySecurityIP4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP4.setStatus("current")
_IpSecuritySecurityIP5_Type = IpAddress
_IpSecuritySecurityIP5_Object = MibScalar
ipSecuritySecurityIP5 = _IpSecuritySecurityIP5_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 9),
    _IpSecuritySecurityIP5_Type()
)
ipSecuritySecurityIP5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP5.setStatus("current")
_IpSecuritySecurityIP6_Type = IpAddress
_IpSecuritySecurityIP6_Object = MibScalar
ipSecuritySecurityIP6 = _IpSecuritySecurityIP6_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 10),
    _IpSecuritySecurityIP6_Type()
)
ipSecuritySecurityIP6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP6.setStatus("current")
_IpSecuritySecurityIP7_Type = IpAddress
_IpSecuritySecurityIP7_Object = MibScalar
ipSecuritySecurityIP7 = _IpSecuritySecurityIP7_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 11),
    _IpSecuritySecurityIP7_Type()
)
ipSecuritySecurityIP7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP7.setStatus("current")
_IpSecuritySecurityIP8_Type = IpAddress
_IpSecuritySecurityIP8_Object = MibScalar
ipSecuritySecurityIP8 = _IpSecuritySecurityIP8_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 12),
    _IpSecuritySecurityIP8_Type()
)
ipSecuritySecurityIP8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP8.setStatus("current")
_IpSecuritySecurityIP9_Type = IpAddress
_IpSecuritySecurityIP9_Object = MibScalar
ipSecuritySecurityIP9 = _IpSecuritySecurityIP9_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 13),
    _IpSecuritySecurityIP9_Type()
)
ipSecuritySecurityIP9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP9.setStatus("current")
_IpSecuritySecurityIP10_Type = IpAddress
_IpSecuritySecurityIP10_Object = MibScalar
ipSecuritySecurityIP10 = _IpSecuritySecurityIP10_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 1, 14),
    _IpSecuritySecurityIP10_Type()
)
ipSecuritySecurityIP10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSecuritySecurityIP10.setStatus("current")
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2)
)
_PortSecurityTable_Object = MibTable
portSecurityTable = _PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2, 1)
)
if mibBuilder.loadTexts:
    portSecurityTable.setStatus("current")
_PortSecurityEntry_Object = MibTableRow
portSecurityEntry = _PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2, 1, 1)
)
portSecurityEntry.setIndexNames(
    (0, "IES-2206FII", "portSecurityIndex"),
)
if mibBuilder.loadTexts:
    portSecurityEntry.setStatus("current")
_PortSecurityIndex_Type = Integer32
_PortSecurityIndex_Object = MibTableColumn
portSecurityIndex = _PortSecurityIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2, 1, 1, 1),
    _PortSecurityIndex_Type()
)
portSecurityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecurityIndex.setStatus("current")


class _PortSecurityPortName_Type(DisplayString):
    """Custom type portSecurityPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_PortSecurityPortName_Type.__name__ = "DisplayString"
_PortSecurityPortName_Object = MibTableColumn
portSecurityPortName = _PortSecurityPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2, 1, 1, 2),
    _PortSecurityPortName_Type()
)
portSecurityPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortName.setStatus("current")
_PortSecurityAddr_Type = MacAddress
_PortSecurityAddr_Object = MibTableColumn
portSecurityAddr = _PortSecurityAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2, 1, 1, 3),
    _PortSecurityAddr_Type()
)
portSecurityAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityAddr.setStatus("current")


class _PortSecurityStatus_Type(Integer32):
    """Custom type portSecurityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_PortSecurityStatus_Type.__name__ = "Integer32"
_PortSecurityStatus_Object = MibTableColumn
portSecurityStatus = _PortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 2, 1, 1, 4),
    _PortSecurityStatus_Type()
)
portSecurityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityStatus.setStatus("current")
_MacBlacklist_ObjectIdentity = ObjectIdentity
macBlacklist = _MacBlacklist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 3)
)
_MacBlacklistTable_Object = MibTable
macBlacklistTable = _MacBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 3, 1)
)
if mibBuilder.loadTexts:
    macBlacklistTable.setStatus("current")
_MacBlacklistEntry_Object = MibTableRow
macBlacklistEntry = _MacBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 3, 1, 1)
)
macBlacklistEntry.setIndexNames(
    (0, "IES-2206FII", "macBlacklistIndex"),
)
if mibBuilder.loadTexts:
    macBlacklistEntry.setStatus("current")
_MacBlacklistIndex_Type = Integer32
_MacBlacklistIndex_Object = MibTableColumn
macBlacklistIndex = _MacBlacklistIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 3, 1, 1, 1),
    _MacBlacklistIndex_Type()
)
macBlacklistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macBlacklistIndex.setStatus("current")
_MacBlacklistAddr_Type = MacAddress
_MacBlacklistAddr_Object = MibTableColumn
macBlacklistAddr = _MacBlacklistAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 3, 1, 1, 2),
    _MacBlacklistAddr_Type()
)
macBlacklistAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macBlacklistAddr.setStatus("current")


class _MacBlacklistStatus_Type(Integer32):
    """Custom type macBlacklistStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("creatrequest", 2),
          ("undercreation", 3),
          ("invalid", 4))
    )


_MacBlacklistStatus_Type.__name__ = "Integer32"
_MacBlacklistStatus_Object = MibTableColumn
macBlacklistStatus = _MacBlacklistStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 3, 1, 1, 3),
    _MacBlacklistStatus_Type()
)
macBlacklistStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macBlacklistStatus.setStatus("current")
_Ieee8021x_ObjectIdentity = ObjectIdentity
ieee8021x = _Ieee8021x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4)
)
_RadiusServerSetting_ObjectIdentity = ObjectIdentity
radiusServerSetting = _RadiusServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1)
)


class _Radius8021xProtocolStatus_Type(Integer32):
    """Custom type radius8021xProtocolStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Radius8021xProtocolStatus_Type.__name__ = "Integer32"
_Radius8021xProtocolStatus_Object = MibScalar
radius8021xProtocolStatus = _Radius8021xProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 1),
    _Radius8021xProtocolStatus_Type()
)
radius8021xProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radius8021xProtocolStatus.setStatus("current")
_RadiusServerIP_Type = IpAddress
_RadiusServerIP_Object = MibScalar
radiusServerIP = _RadiusServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 2),
    _RadiusServerIP_Type()
)
radiusServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerIP.setStatus("current")
_RadiusServerPort_Type = Integer32
_RadiusServerPort_Object = MibScalar
radiusServerPort = _RadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 3),
    _RadiusServerPort_Type()
)
radiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPort.setStatus("current")
_RadiusAccountingPort_Type = Integer32
_RadiusAccountingPort_Object = MibScalar
radiusAccountingPort = _RadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 4),
    _RadiusAccountingPort_Type()
)
radiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAccountingPort.setStatus("current")


class _RadiusSharedKey_Type(DisplayString):
    """Custom type radiusSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RadiusSharedKey_Type.__name__ = "DisplayString"
_RadiusSharedKey_Object = MibScalar
radiusSharedKey = _RadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 5),
    _RadiusSharedKey_Type()
)
radiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSharedKey.setStatus("current")


class _RadiusNASIdentifier_Type(DisplayString):
    """Custom type radiusNASIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RadiusNASIdentifier_Type.__name__ = "DisplayString"
_RadiusNASIdentifier_Object = MibScalar
radiusNASIdentifier = _RadiusNASIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 6),
    _RadiusNASIdentifier_Type()
)
radiusNASIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusNASIdentifier.setStatus("current")
_RadiusMiscQuietPeriod_Type = Integer32
_RadiusMiscQuietPeriod_Object = MibScalar
radiusMiscQuietPeriod = _RadiusMiscQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 7),
    _RadiusMiscQuietPeriod_Type()
)
radiusMiscQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscQuietPeriod.setStatus("current")
_RadiusMiscTxPeriod_Type = Integer32
_RadiusMiscTxPeriod_Object = MibScalar
radiusMiscTxPeriod = _RadiusMiscTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 8),
    _RadiusMiscTxPeriod_Type()
)
radiusMiscTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscTxPeriod.setStatus("current")
_RadiusMiscSupplicantTimeout_Type = Integer32
_RadiusMiscSupplicantTimeout_Object = MibScalar
radiusMiscSupplicantTimeout = _RadiusMiscSupplicantTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 9),
    _RadiusMiscSupplicantTimeout_Type()
)
radiusMiscSupplicantTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscSupplicantTimeout.setStatus("current")
_RadiusMiscServerTimeout_Type = Integer32
_RadiusMiscServerTimeout_Object = MibScalar
radiusMiscServerTimeout = _RadiusMiscServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 10),
    _RadiusMiscServerTimeout_Type()
)
radiusMiscServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscServerTimeout.setStatus("current")
_RadiusMiscReAuthMax_Type = Integer32
_RadiusMiscReAuthMax_Object = MibScalar
radiusMiscReAuthMax = _RadiusMiscReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 11),
    _RadiusMiscReAuthMax_Type()
)
radiusMiscReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscReAuthMax.setStatus("current")
_RadiusMiscReauthPeriod_Type = Integer32
_RadiusMiscReauthPeriod_Object = MibScalar
radiusMiscReauthPeriod = _RadiusMiscReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 1, 12),
    _RadiusMiscReauthPeriod_Type()
)
radiusMiscReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMiscReauthPeriod.setStatus("current")
_PortAuthConfiguration_ObjectIdentity = ObjectIdentity
portAuthConfiguration = _PortAuthConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 2)
)
_RadiusPerPortCfgTable_Object = MibTable
radiusPerPortCfgTable = _RadiusPerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 2, 1)
)
if mibBuilder.loadTexts:
    radiusPerPortCfgTable.setStatus("current")
_RadiusPerPortCfgEntry_Object = MibTableRow
radiusPerPortCfgEntry = _RadiusPerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 2, 1, 1)
)
radiusPerPortCfgEntry.setIndexNames(
    (0, "IES-2206FII", "radiusPerPortCfgIndex"),
)
if mibBuilder.loadTexts:
    radiusPerPortCfgEntry.setStatus("current")
_RadiusPerPortCfgIndex_Type = Integer32
_RadiusPerPortCfgIndex_Object = MibTableColumn
radiusPerPortCfgIndex = _RadiusPerPortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 2, 1, 1, 1),
    _RadiusPerPortCfgIndex_Type()
)
radiusPerPortCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusPerPortCfgIndex.setStatus("current")


class _RadiusPerPortCfgPortName_Type(DisplayString):
    """Custom type radiusPerPortCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RadiusPerPortCfgPortName_Type.__name__ = "DisplayString"
_RadiusPerPortCfgPortName_Object = MibTableColumn
radiusPerPortCfgPortName = _RadiusPerPortCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 2, 1, 1, 2),
    _RadiusPerPortCfgPortName_Type()
)
radiusPerPortCfgPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusPerPortCfgPortName.setStatus("current")


class _RadiusPerPortCfgState_Type(Integer32):
    """Custom type radiusPerPortCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("reject", 1),
          ("accept", 2),
          ("authorize", 3),
          ("disabled", 4))
    )


_RadiusPerPortCfgState_Type.__name__ = "Integer32"
_RadiusPerPortCfgState_Object = MibTableColumn
radiusPerPortCfgState = _RadiusPerPortCfgState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 10, 4, 2, 1, 1, 3),
    _RadiusPerPortCfgState_Type()
)
radiusPerPortCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusPerPortCfgState.setStatus("current")
_Warning_ObjectIdentity = ObjectIdentity
warning = _Warning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11)
)
_FaultAlarm_ObjectIdentity = ObjectIdentity
faultAlarm = _FaultAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1)
)


class _FaultAlarmPwr1_Type(Integer32):
    """Custom type faultAlarmPwr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FaultAlarmPwr1_Type.__name__ = "Integer32"
_FaultAlarmPwr1_Object = MibScalar
faultAlarmPwr1 = _FaultAlarmPwr1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1, 1),
    _FaultAlarmPwr1_Type()
)
faultAlarmPwr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultAlarmPwr1.setStatus("current")


class _FaultAlarmPwr2_Type(Integer32):
    """Custom type faultAlarmPwr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FaultAlarmPwr2_Type.__name__ = "Integer32"
_FaultAlarmPwr2_Object = MibScalar
faultAlarmPwr2 = _FaultAlarmPwr2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1, 2),
    _FaultAlarmPwr2_Type()
)
faultAlarmPwr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultAlarmPwr2.setStatus("current")
_FaultAlarmPortCfgTable_Object = MibTable
faultAlarmPortCfgTable = _FaultAlarmPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1, 3)
)
if mibBuilder.loadTexts:
    faultAlarmPortCfgTable.setStatus("current")
_FaultAlarmPortCfgEntry_Object = MibTableRow
faultAlarmPortCfgEntry = _FaultAlarmPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1, 3, 1)
)
faultAlarmPortCfgEntry.setIndexNames(
    (0, "IES-2206FII", "faultAlarmPortCfgNum"),
)
if mibBuilder.loadTexts:
    faultAlarmPortCfgEntry.setStatus("current")
_FaultAlarmPortCfgNum_Type = Integer32
_FaultAlarmPortCfgNum_Object = MibTableColumn
faultAlarmPortCfgNum = _FaultAlarmPortCfgNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1, 3, 1, 1),
    _FaultAlarmPortCfgNum_Type()
)
faultAlarmPortCfgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultAlarmPortCfgNum.setStatus("current")


class _FaultAlarmPortLinkStatus_Type(Integer32):
    """Custom type faultAlarmPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FaultAlarmPortLinkStatus_Type.__name__ = "Integer32"
_FaultAlarmPortLinkStatus_Object = MibTableColumn
faultAlarmPortLinkStatus = _FaultAlarmPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 1, 3, 1, 2),
    _FaultAlarmPortLinkStatus_Type()
)
faultAlarmPortLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultAlarmPortLinkStatus.setStatus("current")
_SysLogConfiguration_ObjectIdentity = ObjectIdentity
sysLogConfiguration = _SysLogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 2)
)


class _SyslogStatus_Type(Integer32):
    """Custom type syslogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("clientOnly", 1),
          ("serverOnly", 2),
          ("bothClientAndServer", 3),
          ("disabled", 4))
    )


_SyslogStatus_Type.__name__ = "Integer32"
_SyslogStatus_Object = MibScalar
syslogStatus = _SyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 2, 1),
    _SyslogStatus_Type()
)
syslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogStatus.setStatus("current")
_EventServerAddr_Type = IpAddress
_EventServerAddr_Object = MibScalar
eventServerAddr = _EventServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 2, 2),
    _EventServerAddr_Type()
)
eventServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventServerAddr.setStatus("current")
_SmtpConfiguration_ObjectIdentity = ObjectIdentity
smtpConfiguration = _SmtpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3)
)


class _EventEmailAlertStatus_Type(Integer32):
    """Custom type eventEmailAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EventEmailAlertStatus_Type.__name__ = "Integer32"
_EventEmailAlertStatus_Object = MibScalar
eventEmailAlertStatus = _EventEmailAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 1),
    _EventEmailAlertStatus_Type()
)
eventEmailAlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertStatus.setStatus("current")
_EventEmailAlertAddr_Type = IpAddress
_EventEmailAlertAddr_Object = MibScalar
eventEmailAlertAddr = _EventEmailAlertAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 2),
    _EventEmailAlertAddr_Type()
)
eventEmailAlertAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertAddr.setStatus("current")


class _EventEmailAlertAuthentication_Type(Integer32):
    """Custom type eventEmailAlertAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EventEmailAlertAuthentication_Type.__name__ = "Integer32"
_EventEmailAlertAuthentication_Object = MibScalar
eventEmailAlertAuthentication = _EventEmailAlertAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 3),
    _EventEmailAlertAuthentication_Type()
)
eventEmailAlertAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertAuthentication.setStatus("current")


class _EventEmailAlertAccount_Type(DisplayString):
    """Custom type eventEmailAlertAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_EventEmailAlertAccount_Type.__name__ = "DisplayString"
_EventEmailAlertAccount_Object = MibScalar
eventEmailAlertAccount = _EventEmailAlertAccount_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 4),
    _EventEmailAlertAccount_Type()
)
eventEmailAlertAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertAccount.setStatus("current")


class _EventEmailAlertPassword_Type(DisplayString):
    """Custom type eventEmailAlertPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_EventEmailAlertPassword_Type.__name__ = "DisplayString"
_EventEmailAlertPassword_Object = MibScalar
eventEmailAlertPassword = _EventEmailAlertPassword_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 5),
    _EventEmailAlertPassword_Type()
)
eventEmailAlertPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    eventEmailAlertPassword.setStatus("current")
_EmailAlertRcptTable_Object = MibTable
emailAlertRcptTable = _EmailAlertRcptTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 6)
)
if mibBuilder.loadTexts:
    emailAlertRcptTable.setStatus("current")
_EmailAlertRcptEntry_Object = MibTableRow
emailAlertRcptEntry = _EmailAlertRcptEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 6, 1)
)
emailAlertRcptEntry.setIndexNames(
    (0, "IES-2206FII", "eventEmailAlertRcptIndex"),
)
if mibBuilder.loadTexts:
    emailAlertRcptEntry.setStatus("current")
_EventEmailAlertRcptIndex_Type = Integer32
_EventEmailAlertRcptIndex_Object = MibTableColumn
eventEmailAlertRcptIndex = _EventEmailAlertRcptIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 6, 1, 1),
    _EventEmailAlertRcptIndex_Type()
)
eventEmailAlertRcptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventEmailAlertRcptIndex.setStatus("current")


class _EventEmailAlertRcptEmailAddr_Type(DisplayString):
    """Custom type eventEmailAlertRcptEmailAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_EventEmailAlertRcptEmailAddr_Type.__name__ = "DisplayString"
_EventEmailAlertRcptEmailAddr_Object = MibTableColumn
eventEmailAlertRcptEmailAddr = _EventEmailAlertRcptEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 3, 6, 1, 2),
    _EventEmailAlertRcptEmailAddr_Type()
)
eventEmailAlertRcptEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertRcptEmailAddr.setStatus("current")
_EventSelection_ObjectIdentity = ObjectIdentity
eventSelection = _EventSelection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4)
)
_SystemEventsTable_Object = MibTable
systemEventsTable = _SystemEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1)
)
if mibBuilder.loadTexts:
    systemEventsTable.setStatus("current")
_SystemEventsEntry_Object = MibTableRow
systemEventsEntry = _SystemEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1, 1)
)
systemEventsEntry.setIndexNames(
    (0, "IES-2206FII", "eventSystemEventsIndex"),
)
if mibBuilder.loadTexts:
    systemEventsEntry.setStatus("current")
_EventSystemEventsIndex_Type = Integer32
_EventSystemEventsIndex_Object = MibTableColumn
eventSystemEventsIndex = _EventSystemEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1, 1, 1),
    _EventSystemEventsIndex_Type()
)
eventSystemEventsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventSystemEventsIndex.setStatus("current")


class _EventDeviceColdStartEvent_Type(Integer32):
    """Custom type eventDeviceColdStartEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_EventDeviceColdStartEvent_Type.__name__ = "Integer32"
_EventDeviceColdStartEvent_Object = MibTableColumn
eventDeviceColdStartEvent = _EventDeviceColdStartEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1, 1, 2),
    _EventDeviceColdStartEvent_Type()
)
eventDeviceColdStartEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDeviceColdStartEvent.setStatus("current")


class _EventDeviceWarmStartEvent_Type(Integer32):
    """Custom type eventDeviceWarmStartEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_EventDeviceWarmStartEvent_Type.__name__ = "Integer32"
_EventDeviceWarmStartEvent_Object = MibTableColumn
eventDeviceWarmStartEvent = _EventDeviceWarmStartEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1, 1, 3),
    _EventDeviceWarmStartEvent_Type()
)
eventDeviceWarmStartEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDeviceWarmStartEvent.setStatus("current")


class _EventAuthenticationFailureEvent_Type(Integer32):
    """Custom type eventAuthenticationFailureEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_EventAuthenticationFailureEvent_Type.__name__ = "Integer32"
_EventAuthenticationFailureEvent_Object = MibTableColumn
eventAuthenticationFailureEvent = _EventAuthenticationFailureEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1, 1, 4),
    _EventAuthenticationFailureEvent_Type()
)
eventAuthenticationFailureEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAuthenticationFailureEvent.setStatus("current")


class _EventRingTopologyChangeEvent_Type(Integer32):
    """Custom type eventRingTopologyChangeEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("smtp", 2),
          ("logandsmtp", 3),
          ("disabled", 4))
    )


_EventRingTopologyChangeEvent_Type.__name__ = "Integer32"
_EventRingTopologyChangeEvent_Object = MibTableColumn
eventRingTopologyChangeEvent = _EventRingTopologyChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 1, 1, 5),
    _EventRingTopologyChangeEvent_Type()
)
eventRingTopologyChangeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventRingTopologyChangeEvent.setStatus("current")
_PortEventsTable_Object = MibTable
portEventsTable = _PortEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 2)
)
if mibBuilder.loadTexts:
    portEventsTable.setStatus("current")
_PortEventsEntry_Object = MibTableRow
portEventsEntry = _PortEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 2, 1)
)
portEventsEntry.setIndexNames(
    (0, "IES-2206FII", "eventPortNumber"),
)
if mibBuilder.loadTexts:
    portEventsEntry.setStatus("current")
_EventPortNumber_Type = Integer32
_EventPortNumber_Object = MibTableColumn
eventPortNumber = _EventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 2, 1, 1),
    _EventPortNumber_Type()
)
eventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventPortNumber.setStatus("current")


class _EventPortEventLog_Type(Integer32):
    """Custom type eventPortEventLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2),
          ("linkupandlinkdown", 3),
          ("disabled", 4))
    )


_EventPortEventLog_Type.__name__ = "Integer32"
_EventPortEventLog_Object = MibTableColumn
eventPortEventLog = _EventPortEventLog_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 2, 1, 2),
    _EventPortEventLog_Type()
)
eventPortEventLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventPortEventLog.setStatus("current")


class _EventPortEventSMTP_Type(Integer32):
    """Custom type eventPortEventSMTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2),
          ("linkupandlinkdown", 3),
          ("disabled", 4))
    )


_EventPortEventSMTP_Type.__name__ = "Integer32"
_EventPortEventSMTP_Object = MibTableColumn
eventPortEventSMTP = _EventPortEventSMTP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 11, 4, 2, 1, 3),
    _EventPortEventSMTP_Type()
)
eventPortEventSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventPortEventSMTP.setStatus("current")
_MonitorAndDiag_ObjectIdentity = ObjectIdentity
monitorAndDiag = _MonitorAndDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12)
)
_MacAddressTable_ObjectIdentity = ObjectIdentity
macAddressTable = _MacAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1)
)
_AgingTimeSetting_Type = Integer32
_AgingTimeSetting_Object = MibScalar
agingTimeSetting = _AgingTimeSetting_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 1),
    _AgingTimeSetting_Type()
)
agingTimeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agingTimeSetting.setStatus("current")


class _FlushMACStatus_Type(Integer32):
    """Custom type flushMACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FlushMACStatus_Type.__name__ = "Integer32"
_FlushMACStatus_Object = MibScalar
flushMACStatus = _FlushMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 2),
    _FlushMACStatus_Type()
)
flushMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flushMACStatus.setStatus("current")
_MacAddrTable_Object = MibTable
macAddrTable = _MacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 3)
)
if mibBuilder.loadTexts:
    macAddrTable.setStatus("current")
_MacAddrEntry_Object = MibTableRow
macAddrEntry = _MacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 3, 1)
)
macAddrEntry.setIndexNames(
    (0, "IES-2206FII", "macAddressIndex"),
)
if mibBuilder.loadTexts:
    macAddrEntry.setStatus("current")
_MacAddressIndex_Type = Integer32
_MacAddressIndex_Object = MibTableColumn
macAddressIndex = _MacAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 3, 1, 1),
    _MacAddressIndex_Type()
)
macAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressIndex.setStatus("current")


class _MacAddressPortName_Type(DisplayString):
    """Custom type macAddressPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_MacAddressPortName_Type.__name__ = "DisplayString"
_MacAddressPortName_Object = MibTableColumn
macAddressPortName = _MacAddressPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 3, 1, 2),
    _MacAddressPortName_Type()
)
macAddressPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressPortName.setStatus("current")
_MacAddressAddr_Type = MacAddress
_MacAddressAddr_Object = MibTableColumn
macAddressAddr = _MacAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 3, 1, 3),
    _MacAddressAddr_Type()
)
macAddressAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressAddr.setStatus("current")


class _MacAddressType_Type(Integer32):
    """Custom type macAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_MacAddressType_Type.__name__ = "Integer32"
_MacAddressType_Object = MibTableColumn
macAddressType = _MacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 3, 1, 4),
    _MacAddressType_Type()
)
macAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressType.setStatus("current")


class _PortSecurityClearMACTable_Type(Integer32):
    """Custom type portSecurityClearMACTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_PortSecurityClearMACTable_Type.__name__ = "Integer32"
_PortSecurityClearMACTable_Object = MibScalar
portSecurityClearMACTable = _PortSecurityClearMACTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 1, 4),
    _PortSecurityClearMACTable_Type()
)
portSecurityClearMACTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityClearMACTable.setStatus("current")
_PortStatistic_ObjectIdentity = ObjectIdentity
portStatistic = _PortStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2)
)
_SwitchPortStatTable_Object = MibTable
switchPortStatTable = _SwitchPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1)
)
if mibBuilder.loadTexts:
    switchPortStatTable.setStatus("current")
_SwitchPortStatEntry_Object = MibTableRow
switchPortStatEntry = _SwitchPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1)
)
switchPortStatEntry.setIndexNames(
    (0, "IES-2206FII", "swPortStatIndex"),
)
if mibBuilder.loadTexts:
    switchPortStatEntry.setStatus("current")
_SwPortStatIndex_Type = Integer32
_SwPortStatIndex_Object = MibTableColumn
swPortStatIndex = _SwPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 1),
    _SwPortStatIndex_Type()
)
swPortStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortStatIndex.setStatus("current")


class _SwPortStatType_Type(DisplayString):
    """Custom type swPortStatType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SwPortStatType_Type.__name__ = "DisplayString"
_SwPortStatType_Object = MibTableColumn
swPortStatType = _SwPortStatType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 2),
    _SwPortStatType_Type()
)
swPortStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatType.setStatus("current")


class _SwPortStatLink_Type(Integer32):
    """Custom type swPortStatLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_SwPortStatLink_Type.__name__ = "Integer32"
_SwPortStatLink_Object = MibTableColumn
swPortStatLink = _SwPortStatLink_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 3),
    _SwPortStatLink_Type()
)
swPortStatLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatLink.setStatus("current")


class _SwPortStatState_Type(Integer32):
    """Custom type swPortStatState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("blocking", 3))
    )


_SwPortStatState_Type.__name__ = "Integer32"
_SwPortStatState_Object = MibTableColumn
swPortStatState = _SwPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 4),
    _SwPortStatState_Type()
)
swPortStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatState.setStatus("current")
_SwPortStatTXGoodPkt_Type = Integer32
_SwPortStatTXGoodPkt_Object = MibTableColumn
swPortStatTXGoodPkt = _SwPortStatTXGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 5),
    _SwPortStatTXGoodPkt_Type()
)
swPortStatTXGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatTXGoodPkt.setStatus("current")
_SwPortStatTXBadPkt_Type = Integer32
_SwPortStatTXBadPkt_Object = MibTableColumn
swPortStatTXBadPkt = _SwPortStatTXBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 6),
    _SwPortStatTXBadPkt_Type()
)
swPortStatTXBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatTXBadPkt.setStatus("current")
_SwPortStatRXGoodPkt_Type = Integer32
_SwPortStatRXGoodPkt_Object = MibTableColumn
swPortStatRXGoodPkt = _SwPortStatRXGoodPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 7),
    _SwPortStatRXGoodPkt_Type()
)
swPortStatRXGoodPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatRXGoodPkt.setStatus("current")
_SwPortStatRXBadPkt_Type = Integer32
_SwPortStatRXBadPkt_Object = MibTableColumn
swPortStatRXBadPkt = _SwPortStatRXBadPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 8),
    _SwPortStatRXBadPkt_Type()
)
swPortStatRXBadPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatRXBadPkt.setStatus("current")
_SwPortStatTXAbortPkt_Type = Integer32
_SwPortStatTXAbortPkt_Object = MibTableColumn
swPortStatTXAbortPkt = _SwPortStatTXAbortPkt_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 9),
    _SwPortStatTXAbortPkt_Type()
)
swPortStatTXAbortPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatTXAbortPkt.setStatus("current")
_SwPortStatPacketCollision_Type = Integer32
_SwPortStatPacketCollision_Object = MibTableColumn
swPortStatPacketCollision = _SwPortStatPacketCollision_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 2, 1, 1, 10),
    _SwPortStatPacketCollision_Type()
)
swPortStatPacketCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatPacketCollision.setStatus("current")
_Portmirroring_ObjectIdentity = ObjectIdentity
portmirroring = _Portmirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3)
)
_SwPortMirrorDestinationPortTX_Type = Integer32
_SwPortMirrorDestinationPortTX_Object = MibScalar
swPortMirrorDestinationPortTX = _SwPortMirrorDestinationPortTX_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3, 1),
    _SwPortMirrorDestinationPortTX_Type()
)
swPortMirrorDestinationPortTX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorDestinationPortTX.setStatus("current")
_SwPortMirrorDestinationPortRX_Type = Integer32
_SwPortMirrorDestinationPortRX_Object = MibScalar
swPortMirrorDestinationPortRX = _SwPortMirrorDestinationPortRX_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3, 2),
    _SwPortMirrorDestinationPortRX_Type()
)
swPortMirrorDestinationPortRX.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorDestinationPortRX.setStatus("current")
_SwitchPortMirrorSourceTable_Object = MibTable
switchPortMirrorSourceTable = _SwitchPortMirrorSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3, 3)
)
if mibBuilder.loadTexts:
    switchPortMirrorSourceTable.setStatus("current")
_SwitchPortMirrorSourceEntry_Object = MibTableRow
switchPortMirrorSourceEntry = _SwitchPortMirrorSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3, 3, 1)
)
switchPortMirrorSourceEntry.setIndexNames(
    (0, "IES-2206FII", "swPortMirrorPortNum"),
)
if mibBuilder.loadTexts:
    switchPortMirrorSourceEntry.setStatus("current")
_SwPortMirrorPortNum_Type = Integer32
_SwPortMirrorPortNum_Object = MibTableColumn
swPortMirrorPortNum = _SwPortMirrorPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3, 3, 1, 1),
    _SwPortMirrorPortNum_Type()
)
swPortMirrorPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMirrorPortNum.setStatus("current")


class _SwPortMirrorSourcePort_Type(Integer32):
    """Custom type swPortMirrorSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("txonly", 1),
          ("rxonly", 2),
          ("rxandtx", 3),
          ("disabled", 4))
    )


_SwPortMirrorSourcePort_Type.__name__ = "Integer32"
_SwPortMirrorSourcePort_Object = MibTableColumn
swPortMirrorSourcePort = _SwPortMirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 3, 3, 1, 2),
    _SwPortMirrorSourcePort_Type()
)
swPortMirrorSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorSourcePort.setStatus("current")
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 4)
)
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 4, 1)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 4, 1, 1)
)
eventLogEntry.setIndexNames(
    (0, "IES-2206FII", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")
_EventLogIndex_Type = Integer32
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 4, 1, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("current")


class _EventLogDescription_Type(DisplayString):
    """Custom type eventLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_EventLogDescription_Type.__name__ = "DisplayString"
_EventLogDescription_Object = MibTableColumn
eventLogDescription = _EventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 12, 4, 1, 1, 2),
    _EventLogDescription_Type()
)
eventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDescription.setStatus("current")
_SaveConfiguration_ObjectIdentity = ObjectIdentity
saveConfiguration = _SaveConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 13)
)


class _SaveCfgMgtAction_Type(Integer32):
    """Custom type saveCfgMgtAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_SaveCfgMgtAction_Type.__name__ = "Integer32"
_SaveCfgMgtAction_Object = MibScalar
saveCfgMgtAction = _SaveCfgMgtAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 13, 1),
    _SaveCfgMgtAction_Type()
)
saveCfgMgtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveCfgMgtAction.setStatus("current")
_FactoryDefault_ObjectIdentity = ObjectIdentity
factoryDefault = _FactoryDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 14)
)


class _FactoryDefaultAction_Type(Integer32):
    """Custom type factoryDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("keep_ip_and_username_password", 1),
          ("keep_ip", 2),
          ("keep_username_password", 3),
          ("keep_nothing", 4),
          ("notActive", 5))
    )


_FactoryDefaultAction_Type.__name__ = "Integer32"
_FactoryDefaultAction_Object = MibScalar
factoryDefaultAction = _FactoryDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 14, 1),
    _FactoryDefaultAction_Type()
)
factoryDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    factoryDefaultAction.setStatus("current")
_SystemReboot_ObjectIdentity = ObjectIdentity
systemReboot = _SystemReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 15)
)


class _SystemRebootAction_Type(Integer32):
    """Custom type systemRebootAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2))
    )


_SystemRebootAction_Type.__name__ = "Integer32"
_SystemRebootAction_Object = MibScalar
systemRebootAction = _SystemRebootAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 15, 1),
    _SystemRebootAction_Type()
)
systemRebootAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRebootAction.setStatus("current")
_Misc_ObjectIdentity = ObjectIdentity
misc = _Misc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 1)
)


class _TrapPowerStatus_Type(Integer32):
    """Custom type trapPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("power1On_power2On", 1),
          ("power1On_power2Off", 2),
          ("power1Off_power2On", 3),
          ("power1Off_power2Off", 4))
    )


_TrapPowerStatus_Type.__name__ = "Integer32"
_TrapPowerStatus_Object = MibScalar
trapPowerStatus = _TrapPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 1, 1),
    _TrapPowerStatus_Type()
)
trapPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPowerStatus.setStatus("current")
_TrapTopologyChange_Type = Integer32
_TrapTopologyChange_Object = MibScalar
trapTopologyChange = _TrapTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 1, 2),
    _TrapTopologyChange_Type()
)
trapTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTopologyChange.setStatus("current")
_SwitchCurrentPortNameListTable_Object = MibTable
switchCurrentPortNameListTable = _SwitchCurrentPortNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 2)
)
if mibBuilder.loadTexts:
    switchCurrentPortNameListTable.setStatus("current")
_SwitchCurrentPortNameListEntry_Object = MibTableRow
switchCurrentPortNameListEntry = _SwitchCurrentPortNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 2, 1)
)
switchCurrentPortNameListEntry.setIndexNames(
    (0, "IES-2206FII", "swCurrentPortNameListIndex"),
)
if mibBuilder.loadTexts:
    switchCurrentPortNameListEntry.setStatus("current")
_SwCurrentPortNameListIndex_Type = Integer32
_SwCurrentPortNameListIndex_Object = MibTableColumn
swCurrentPortNameListIndex = _SwCurrentPortNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 2, 1, 1),
    _SwCurrentPortNameListIndex_Type()
)
swCurrentPortNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swCurrentPortNameListIndex.setStatus("current")


class _SwCurrentPortNameListPortName_Type(DisplayString):
    """Custom type swCurrentPortNameListPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_SwCurrentPortNameListPortName_Type.__name__ = "DisplayString"
_SwCurrentPortNameListPortName_Object = MibTableColumn
swCurrentPortNameListPortName = _SwCurrentPortNameListPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 2, 1, 2),
    _SwCurrentPortNameListPortName_Type()
)
swCurrentPortNameListPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentPortNameListPortName.setStatus("current")


class _SwCurrentPortNameListPortNumber_Type(DisplayString):
    """Custom type swCurrentPortNameListPortNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SwCurrentPortNameListPortNumber_Type.__name__ = "DisplayString"
_SwCurrentPortNameListPortNumber_Object = MibTableColumn
swCurrentPortNameListPortNumber = _SwCurrentPortNameListPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 0, 0, 4, 24, 2, 1, 3),
    _SwCurrentPortNameListPortNumber_Type()
)
swCurrentPortNameListPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCurrentPortNameListPortNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IES-2206FII",
    **{"DisplayString": DisplayString,
       "MacAddress": MacAddress,
       "PortList": PortList,
       "private": private,
       "enterprises": enterprises,
       "switches": switches,
       "products": products,
       "managedSwitch": managedSwitch,
       "ies2206fii": ies2206fii,
       "contact": contact,
       "systemInfo": systemInfo,
       "systemName": systemName,
       "systemLocation": systemLocation,
       "systemContact": systemContact,
       "systemDescr": systemDescr,
       "systemFwVer": systemFwVer,
       "systemMacAddress": systemMacAddress,
       "basicSetting": basicSetting,
       "switchSetting": switchSetting,
       "switchSettingSystemName": switchSettingSystemName,
       "switchSettingSystemLocation": switchSettingSystemLocation,
       "switchSettingSystemContact": switchSettingSystemContact,
       "switchSettingLocationAlert": switchSettingLocationAlert,
       "adminPassword": adminPassword,
       "adminPasswordUserName": adminPasswordUserName,
       "adminPassword_Password": adminPassword_Password,
       "ipConfiguration": ipConfiguration,
       "ipConfigurationTable": ipConfigurationTable,
       "ipConfigurationEntry": ipConfigurationEntry,
       "ipConfigurationIndex": ipConfigurationIndex,
       "ipConfigurationDHCPStatus": ipConfigurationDHCPStatus,
       "ipConfigurationAddress": ipConfigurationAddress,
       "ipConfigurationSubMask": ipConfigurationSubMask,
       "ipConfigurationGateway": ipConfigurationGateway,
       "ipConfigurationDNS1": ipConfigurationDNS1,
       "ipConfigurationDNS2": ipConfigurationDNS2,
       "sntp": sntp,
       "sntpClientStatus": sntpClientStatus,
       "sntpDaylightSavingTime": sntpDaylightSavingTime,
       "sntpUTCTimezone": sntpUTCTimezone,
       "sntpServerAddress": sntpServerAddress,
       "sntpSwitchTimer": sntpSwitchTimer,
       "sntpDaylightSavingPeriodStart": sntpDaylightSavingPeriodStart,
       "sntpDaylightSavingPeriodEnd": sntpDaylightSavingPeriodEnd,
       "sntpDaylightSavingOffset": sntpDaylightSavingOffset,
       "lldp": lldp,
       "lldpStatus": lldpStatus,
       "lldpInterval": lldpInterval,
       "autoProvision": autoProvision,
       "autoProvisionConfigurationStatus": autoProvisionConfigurationStatus,
       "autoProvisionConfigurationServerip": autoProvisionConfigurationServerip,
       "autoProvisionConfigurationFilename": autoProvisionConfigurationFilename,
       "autoProvisionImageStatus": autoProvisionImageStatus,
       "autoProvisionImageServerip": autoProvisionImageServerip,
       "autoProvisionImageFilename": autoProvisionImageFilename,
       "backupAndRestore": backupAndRestore,
       "backupServerIP": backupServerIP,
       "backupAgentBoardFwFileName": backupAgentBoardFwFileName,
       "backupStatus": backupStatus,
       "restoreServerIP": restoreServerIP,
       "restoreAgentBoardFwFileName": restoreAgentBoardFwFileName,
       "restoreStatus": restoreStatus,
       "upgradeFirmware": upgradeFirmware,
       "tftpDownloadServerIP": tftpDownloadServerIP,
       "tftpDownloadAgentBoardFwFileName": tftpDownloadAgentBoardFwFileName,
       "tftpDownloadStatus": tftpDownloadStatus,
       "dhcpServer": dhcpServer,
       "dhcpServerCfgTable": dhcpServerCfgTable,
       "dhcpServerCfgEntry": dhcpServerCfgEntry,
       "dhcpServerCfgIndex": dhcpServerCfgIndex,
       "dhcpServerCfgStatus": dhcpServerCfgStatus,
       "dhcpServerCfgLowIPAddr": dhcpServerCfgLowIPAddr,
       "dhcpServerCfgHighIPAddr": dhcpServerCfgHighIPAddr,
       "dhcpServerCfgSubMask": dhcpServerCfgSubMask,
       "dhcpServerCfgGateway": dhcpServerCfgGateway,
       "dhcpServerCfgDNS": dhcpServerCfgDNS,
       "dhcpServerCfgLeaseTime": dhcpServerCfgLeaseTime,
       "dhcpServerClientInfoTable": dhcpServerClientInfoTable,
       "dhcpServerClientInfoEntry": dhcpServerClientInfoEntry,
       "dhcpServerClientInfoIndex": dhcpServerClientInfoIndex,
       "dhcpServerClientInfoIPAddr": dhcpServerClientInfoIPAddr,
       "dhcpServerClientInfoID": dhcpServerClientInfoID,
       "dhcpServerClientInfoType": dhcpServerClientInfoType,
       "dhcpServerClientInfoStatus": dhcpServerClientInfoStatus,
       "dhcpServerClientInfoLease": dhcpServerClientInfoLease,
       "dhcpServerIPBindingTable": dhcpServerIPBindingTable,
       "dhcpServerIPBindingEntry": dhcpServerIPBindingEntry,
       "dhcpServerIPBindingPortNum": dhcpServerIPBindingPortNum,
       "dhcpServerIPBindingAddr": dhcpServerIPBindingAddr,
       "portSetting": portSetting,
       "portControl": portControl,
       "portCtrlTable": portCtrlTable,
       "portCtrlEntry": portCtrlEntry,
       "portCtrlIndex": portCtrlIndex,
       "portCtrlPortName": portCtrlPortName,
       "portCtrlPortStatus": portCtrlPortStatus,
       "portCtrlNegotiation": portCtrlNegotiation,
       "portCtrlSpeed": portCtrlSpeed,
       "portCtrlDuplex": portCtrlDuplex,
       "portCtrlFlowControl": portCtrlFlowControl,
       "portCtrlSecurity": portCtrlSecurity,
       "rateLimiting": rateLimiting,
       "rateLimitingTable": rateLimitingTable,
       "rateLimitingEntry": rateLimitingEntry,
       "rateLimitingPortNum": rateLimitingPortNum,
       "rateLimitingPortType": rateLimitingPortType,
       "rateLimitingIngressRate": rateLimitingIngressRate,
       "rateLimitingEgressRate": rateLimitingEgressRate,
       "portTrunk": portTrunk,
       "aggregatorSetting": aggregatorSetting,
       "portTrunkSysPri": portTrunkSysPri,
       "portTrunkAggregatorTable": portTrunkAggregatorTable,
       "portTrunkAggregatorEntry": portTrunkAggregatorEntry,
       "portTrunkAggregatorIndex": portTrunkAggregatorIndex,
       "portTrunkAggregatorGroupName": portTrunkAggregatorGroupName,
       "portTrunkAggregatorMemberPorts": portTrunkAggregatorMemberPorts,
       "portTrunkAggregatorLACPStatus": portTrunkAggregatorLACPStatus,
       "portTrunkAggregatorWorkPorts": portTrunkAggregatorWorkPorts,
       "aggregatorStatus": aggregatorStatus,
       "portTrunkAggregatorInfoTable": portTrunkAggregatorInfoTable,
       "portTrunkAggregatorInfoEntry": portTrunkAggregatorInfoEntry,
       "portTrunkAggregatorInfoIndex": portTrunkAggregatorInfoIndex,
       "portTrunkAggregatorInfoGroupName": portTrunkAggregatorInfoGroupName,
       "portTrunkAggregatorInfoDescription": portTrunkAggregatorInfoDescription,
       "stateActivity": stateActivity,
       "portTrunkLACPStateActTable": portTrunkLACPStateActTable,
       "portTrunkLACPStateActEntry": portTrunkLACPStateActEntry,
       "portTrunkLACPStateActPortNum": portTrunkLACPStateActPortNum,
       "portTrunkLACPStateActStatus": portTrunkLACPStateActStatus,
       "redunadancy": redunadancy,
       "redundantRing": redundantRing,
       "redundantRingStatus": redundantRingStatus,
       "redundantRingRingMasterStatus": redundantRingRingMasterStatus,
       "redundantRingRingPort1": redundantRingRingPort1,
       "redundantRingRingPort2": redundantRingRingPort2,
       "redundantRingCoupleRingStatus": redundantRingCoupleRingStatus,
       "redundantRingCouplingPort": redundantRingCouplingPort,
       "redundantRingDualHomingStatus": redundantRingDualHomingStatus,
       "redundantRingHomingPort": redundantRingHomingPort,
       "redundantRingRingMasterHStatus": redundantRingRingMasterHStatus,
       "rstp": rstp,
       "rstpStatus": rstpStatus,
       "rstpPriority": rstpPriority,
       "rstpMaxAge": rstpMaxAge,
       "rstpHelloTime": rstpHelloTime,
       "rstpForwardDelayTime": rstpForwardDelayTime,
       "rstpPerPortCfgTable": rstpPerPortCfgTable,
       "rstpPerPortCfgEntry": rstpPerPortCfgEntry,
       "rstpPerPortCfgPortNum": rstpPerPortCfgPortNum,
       "rstpPerPortCfgPathCost": rstpPerPortCfgPathCost,
       "rstpPerPortCfgPriority": rstpPerPortCfgPriority,
       "rstpPerPortCfgAdminP2P": rstpPerPortCfgAdminP2P,
       "rstpPerPortCfgAdminEdge": rstpPerPortCfgAdminEdge,
       "rstpPerPortCfgAdminNonStp": rstpPerPortCfgAdminNonStp,
       "rstpRootBridgeInformationTable": rstpRootBridgeInformationTable,
       "rstpRootBridgeInformationEntry": rstpRootBridgeInformationEntry,
       "rstpRootBridgeInformationIndex": rstpRootBridgeInformationIndex,
       "rstpRootBridgeInformationBridgeID": rstpRootBridgeInformationBridgeID,
       "rstpRootBridgeInformationRootPriority": rstpRootBridgeInformationRootPriority,
       "rstpRootBridgeInformationRootPort": rstpRootBridgeInformationRootPort,
       "rstpRootBridgeInformationRootPathCost": rstpRootBridgeInformationRootPathCost,
       "rstpRootBridgeInformationMaxAge": rstpRootBridgeInformationMaxAge,
       "rstpRootBridgeInformationHelloTime": rstpRootBridgeInformationHelloTime,
       "rstpRootBridgeInformationForwardDelay": rstpRootBridgeInformationForwardDelay,
       "rstpPerPortInfoTable": rstpPerPortInfoTable,
       "rstpPerPortInfoEntry": rstpPerPortInfoEntry,
       "rstpPerPortInfoPortNum": rstpPerPortInfoPortNum,
       "rstpPerPortInfoPathCost": rstpPerPortInfoPathCost,
       "rstpPerPortInfoPriority": rstpPerPortInfoPriority,
       "rstpPerPortInfoAdminP2P": rstpPerPortInfoAdminP2P,
       "rstpPerPortInfoAdminEdge": rstpPerPortInfoAdminEdge,
       "rstpPerPortInfoStpNeighbor": rstpPerPortInfoStpNeighbor,
       "rstpPerPortInfoState": rstpPerPortInfoState,
       "rstpPerPortInfoRole": rstpPerPortInfoRole,
       "mstp": mstp,
       "mstpStatus": mstpStatus,
       "mstpForceVersion": mstpForceVersion,
       "mstpConfigurationName": mstpConfigurationName,
       "mstpRevisionLevel": mstpRevisionLevel,
       "mstpPriority": mstpPriority,
       "mstpMaxAgeTime": mstpMaxAgeTime,
       "mstpHelloTime": mstpHelloTime,
       "mstpForwardDelayTime": mstpForwardDelayTime,
       "mstpMaxHops": mstpMaxHops,
       "mstpRootBridgeInformationTable": mstpRootBridgeInformationTable,
       "mstpRootBridgeInformationEntry": mstpRootBridgeInformationEntry,
       "mstpRootBridgeInformationIndex": mstpRootBridgeInformationIndex,
       "mstpRootBridgeInformationMac": mstpRootBridgeInformationMac,
       "mstpRootBridgeInformationPriority": mstpRootBridgeInformationPriority,
       "mstpRootBridgeInformationConfigurationName": mstpRootBridgeInformationConfigurationName,
       "mstpRootBridgeInformationForceVersion": mstpRootBridgeInformationForceVersion,
       "mstpRootBridgeInformationRevisionLevel": mstpRootBridgeInformationRevisionLevel,
       "mstpRootBridgeInformationMaxAge": mstpRootBridgeInformationMaxAge,
       "mstpRootBridgeInformationHelloTime": mstpRootBridgeInformationHelloTime,
       "mstpRootBridgeInformationForwardDelay": mstpRootBridgeInformationForwardDelay,
       "mstpRootBridgeInformationMaxHops": mstpRootBridgeInformationMaxHops,
       "mstpRootBridgeInformationRootPort": mstpRootBridgeInformationRootPort,
       "mstpRootBridgeInformationRootPathCost": mstpRootBridgeInformationRootPathCost,
       "mstpPerportCfgTable": mstpPerportCfgTable,
       "mstpPerportCfgEntry": mstpPerportCfgEntry,
       "mstpPerportCfgNum": mstpPerportCfgNum,
       "mstpPerportCfgPriority": mstpPerportCfgPriority,
       "mstpPerportCfgPathCost": mstpPerportCfgPathCost,
       "mstpPerportCfgAdminP2p": mstpPerportCfgAdminP2p,
       "mstpPerportCfgAdminEdge": mstpPerportCfgAdminEdge,
       "mstpPerportCfgAdminNonstp": mstpPerportCfgAdminNonstp,
       "mstpPerportInfoTable": mstpPerportInfoTable,
       "mstpPerportInfoEntry": mstpPerportInfoEntry,
       "mstpPerportInfoNum": mstpPerportInfoNum,
       "mstpPerportInfoPriority": mstpPerportInfoPriority,
       "mstpPerportInfoPathCostAdmin": mstpPerportInfoPathCostAdmin,
       "mstpPerportInfoPathCostOper": mstpPerportInfoPathCostOper,
       "mstpPerportInfoP2pAdmin": mstpPerportInfoP2pAdmin,
       "mstpPerportInfoP2pOper": mstpPerportInfoP2pOper,
       "mstpPerportInfoEdgeAdmin": mstpPerportInfoEdgeAdmin,
       "mstpPerportInfoEdgeOper": mstpPerportInfoEdgeOper,
       "mstpPerportInfoNonstpAdmin": mstpPerportInfoNonstpAdmin,
       "mstpInstanceTable": mstpInstanceTable,
       "mstpInstanceEntry": mstpInstanceEntry,
       "mstpInstanceNum": mstpInstanceNum,
       "mstpInstanceState": mstpInstanceState,
       "mstpInstanceVlans": mstpInstanceVlans,
       "mstpInstancePriority": mstpInstancePriority,
       "mstpInstanceInfoTable": mstpInstanceInfoTable,
       "mstpInstanceInfoEntry": mstpInstanceInfoEntry,
       "mstpInstanceInfonNum": mstpInstanceInfonNum,
       "mstpInstanceInfoVlans": mstpInstanceInfoVlans,
       "mstpInstanceInfoPriority": mstpInstanceInfoPriority,
       "mstpInstanceInfoRegionalRootBridgeId": mstpInstanceInfoRegionalRootBridgeId,
       "mstpInstanceInfoPathCost": mstpInstanceInfoPathCost,
       "mstpInstanceInfoRootPort": mstpInstanceInfoRootPort,
       "mstpInstancePortTable": mstpInstancePortTable,
       "mstpInstancePortEntry": mstpInstancePortEntry,
       "mstpInstancePortNum": mstpInstancePortNum,
       "mstpInstancePortPortId": mstpInstancePortPortId,
       "mstpInstancePortPriority": mstpInstancePortPriority,
       "mstpInstancePortPathCost": mstpInstancePortPathCost,
       "mstpInstancePortInformationTable": mstpInstancePortInformationTable,
       "mstpInstancePortInformationEntry": mstpInstancePortInformationEntry,
       "mstpInstancePortInformationNum": mstpInstancePortInformationNum,
       "mstpInstancePortInformationPortId": mstpInstancePortInformationPortId,
       "mstpInstancePortInformationPriority": mstpInstancePortInformationPriority,
       "mstpInstancePortInformationPathCostAdmin": mstpInstancePortInformationPathCostAdmin,
       "mstpInstancePortInformationPathCostOper": mstpInstancePortInformationPathCostOper,
       "mstpInstancePortInformationState": mstpInstancePortInformationState,
       "mstpInstancePortInformationRole": mstpInstancePortInformationRole,
       "vlan": vlan,
       "vlanOperationMode": vlanOperationMode,
       "vlanGVRP": vlanGVRP,
       "vlanIEEE8021QTable": vlanIEEE8021QTable,
       "vlanIEEE8021QEntry": vlanIEEE8021QEntry,
       "vlanIEEE8021QIndex": vlanIEEE8021QIndex,
       "vlanIEEE8021QPortName": vlanIEEE8021QPortName,
       "vlanIEEE8021QLinkType": vlanIEEE8021QLinkType,
       "vlanIEEE8021QUntaggedVid": vlanIEEE8021QUntaggedVid,
       "vlanIEEE8021QTaggedVids": vlanIEEE8021QTaggedVids,
       "vlanIEEE8021QGroupTable": vlanIEEE8021QGroupTable,
       "vlanIEEE8021QGroupEntry": vlanIEEE8021QGroupEntry,
       "vlanIEEE8021QGroupVid": vlanIEEE8021QGroupVid,
       "vlanIEEE8021QGroupName": vlanIEEE8021QGroupName,
       "vlanIEEE8021QGroupStatus": vlanIEEE8021QGroupStatus,
       "vlanPortBasedTable": vlanPortBasedTable,
       "vlanPortBasedEntry": vlanPortBasedEntry,
       "vlanPortBasedIndex": vlanPortBasedIndex,
       "vlanPortBasedGroupName": vlanPortBasedGroupName,
       "vlanPortBasedVid": vlanPortBasedVid,
       "vlanPortBasedMembers": vlanPortBasedMembers,
       "vlanPortBasedStatus": vlanPortBasedStatus,
       "snmp": snmp,
       "snmpAgentMode": snmpAgentMode,
       "snmpSystemName": snmpSystemName,
       "snmpSystemLocation": snmpSystemLocation,
       "snmpSystemContact": snmpSystemContact,
       "snmpCommunityStringTable": snmpCommunityStringTable,
       "snmpCommunityStringEntry": snmpCommunityStringEntry,
       "snmpCommunityStringIndex": snmpCommunityStringIndex,
       "snmpCommunityStringName": snmpCommunityStringName,
       "snmpCommunityStringAttribute": snmpCommunityStringAttribute,
       "snmpCommunityStringStatus": snmpCommunityStringStatus,
       "snmpTrapServerTable": snmpTrapServerTable,
       "snmpTrapServerEntry": snmpTrapServerEntry,
       "snmpTrapServerIndex": snmpTrapServerIndex,
       "snmpTrapServerIPAddr": snmpTrapServerIPAddr,
       "snmpTrapServerTrapComm": snmpTrapServerTrapComm,
       "snmpTrapServerTrapVer": snmpTrapServerTrapVer,
       "snmpTrapServerStatus": snmpTrapServerStatus,
       "trafficPrioritization": trafficPrioritization,
       "qosPolicy": qosPolicy,
       "qosPriorityType": qosPriorityType,
       "qosPortBasedPriorityTable": qosPortBasedPriorityTable,
       "qosPortBasedPriorityEntry": qosPortBasedPriorityEntry,
       "qosPortBasedPriorityPortNum": qosPortBasedPriorityPortNum,
       "qosPortBasedPriority": qosPortBasedPriority,
       "qosCOSTable": qosCOSTable,
       "qosCOSEntry": qosCOSEntry,
       "qosCOSPriority": qosCOSPriority,
       "qosCOS": qosCOS,
       "qosCOSPortDefaultTable": qosCOSPortDefaultTable,
       "qosCOSPortDefaultEntry": qosCOSPortDefaultEntry,
       "qosCOSPort": qosCOSPort,
       "qosCOSPortDefault": qosCOSPortDefault,
       "qosTOSTable": qosTOSTable,
       "qosTOSEntry": qosTOSEntry,
       "qosTOSPriority": qosTOSPriority,
       "qosTOS": qosTOS,
       "multicast": multicast,
       "igmp": igmp,
       "igmpStatus": igmpStatus,
       "igmpQuery": igmpQuery,
       "igmpEntriesTable": igmpEntriesTable,
       "igmpEntriesEntry": igmpEntriesEntry,
       "igmpEntriesEntryIndex": igmpEntriesEntryIndex,
       "igmpEntriesEntryIPAddr": igmpEntriesEntryIPAddr,
       "igmpEntriesEntryVID": igmpEntriesEntryVID,
       "igmpEntriesEntryMembers": igmpEntriesEntryMembers,
       "multicastfiltering": multicastfiltering,
       "multicastfilteringEntriesTable": multicastfilteringEntriesTable,
       "multicastfilteringEntriesEntry": multicastfilteringEntriesEntry,
       "multicastFilteringIndex": multicastFilteringIndex,
       "multicastFilteringAddr": multicastFilteringAddr,
       "multicastFilteringMemberports": multicastFilteringMemberports,
       "multicastFilteringStatus": multicastFilteringStatus,
       "security": security,
       "ipSecurityMgt": ipSecurityMgt,
       "ipSecurityStatus": ipSecurityStatus,
       "ipSecurityHTTPServerStatus": ipSecurityHTTPServerStatus,
       "ipSecurityTelnetServerStatus": ipSecurityTelnetServerStatus,
       "ipSecuritySNMPServerStatus": ipSecuritySNMPServerStatus,
       "ipSecuritySecurityIP1": ipSecuritySecurityIP1,
       "ipSecuritySecurityIP2": ipSecuritySecurityIP2,
       "ipSecuritySecurityIP3": ipSecuritySecurityIP3,
       "ipSecuritySecurityIP4": ipSecuritySecurityIP4,
       "ipSecuritySecurityIP5": ipSecuritySecurityIP5,
       "ipSecuritySecurityIP6": ipSecuritySecurityIP6,
       "ipSecuritySecurityIP7": ipSecuritySecurityIP7,
       "ipSecuritySecurityIP8": ipSecuritySecurityIP8,
       "ipSecuritySecurityIP9": ipSecuritySecurityIP9,
       "ipSecuritySecurityIP10": ipSecuritySecurityIP10,
       "portSecurityMgt": portSecurityMgt,
       "portSecurityTable": portSecurityTable,
       "portSecurityEntry": portSecurityEntry,
       "portSecurityIndex": portSecurityIndex,
       "portSecurityPortName": portSecurityPortName,
       "portSecurityAddr": portSecurityAddr,
       "portSecurityStatus": portSecurityStatus,
       "macBlacklist": macBlacklist,
       "macBlacklistTable": macBlacklistTable,
       "macBlacklistEntry": macBlacklistEntry,
       "macBlacklistIndex": macBlacklistIndex,
       "macBlacklistAddr": macBlacklistAddr,
       "macBlacklistStatus": macBlacklistStatus,
       "ieee8021x": ieee8021x,
       "radiusServerSetting": radiusServerSetting,
       "radius8021xProtocolStatus": radius8021xProtocolStatus,
       "radiusServerIP": radiusServerIP,
       "radiusServerPort": radiusServerPort,
       "radiusAccountingPort": radiusAccountingPort,
       "radiusSharedKey": radiusSharedKey,
       "radiusNASIdentifier": radiusNASIdentifier,
       "radiusMiscQuietPeriod": radiusMiscQuietPeriod,
       "radiusMiscTxPeriod": radiusMiscTxPeriod,
       "radiusMiscSupplicantTimeout": radiusMiscSupplicantTimeout,
       "radiusMiscServerTimeout": radiusMiscServerTimeout,
       "radiusMiscReAuthMax": radiusMiscReAuthMax,
       "radiusMiscReauthPeriod": radiusMiscReauthPeriod,
       "portAuthConfiguration": portAuthConfiguration,
       "radiusPerPortCfgTable": radiusPerPortCfgTable,
       "radiusPerPortCfgEntry": radiusPerPortCfgEntry,
       "radiusPerPortCfgIndex": radiusPerPortCfgIndex,
       "radiusPerPortCfgPortName": radiusPerPortCfgPortName,
       "radiusPerPortCfgState": radiusPerPortCfgState,
       "warning": warning,
       "faultAlarm": faultAlarm,
       "faultAlarmPwr1": faultAlarmPwr1,
       "faultAlarmPwr2": faultAlarmPwr2,
       "faultAlarmPortCfgTable": faultAlarmPortCfgTable,
       "faultAlarmPortCfgEntry": faultAlarmPortCfgEntry,
       "faultAlarmPortCfgNum": faultAlarmPortCfgNum,
       "faultAlarmPortLinkStatus": faultAlarmPortLinkStatus,
       "sysLogConfiguration": sysLogConfiguration,
       "syslogStatus": syslogStatus,
       "eventServerAddr": eventServerAddr,
       "smtpConfiguration": smtpConfiguration,
       "eventEmailAlertStatus": eventEmailAlertStatus,
       "eventEmailAlertAddr": eventEmailAlertAddr,
       "eventEmailAlertAuthentication": eventEmailAlertAuthentication,
       "eventEmailAlertAccount": eventEmailAlertAccount,
       "eventEmailAlertPassword": eventEmailAlertPassword,
       "emailAlertRcptTable": emailAlertRcptTable,
       "emailAlertRcptEntry": emailAlertRcptEntry,
       "eventEmailAlertRcptIndex": eventEmailAlertRcptIndex,
       "eventEmailAlertRcptEmailAddr": eventEmailAlertRcptEmailAddr,
       "eventSelection": eventSelection,
       "systemEventsTable": systemEventsTable,
       "systemEventsEntry": systemEventsEntry,
       "eventSystemEventsIndex": eventSystemEventsIndex,
       "eventDeviceColdStartEvent": eventDeviceColdStartEvent,
       "eventDeviceWarmStartEvent": eventDeviceWarmStartEvent,
       "eventAuthenticationFailureEvent": eventAuthenticationFailureEvent,
       "eventRingTopologyChangeEvent": eventRingTopologyChangeEvent,
       "portEventsTable": portEventsTable,
       "portEventsEntry": portEventsEntry,
       "eventPortNumber": eventPortNumber,
       "eventPortEventLog": eventPortEventLog,
       "eventPortEventSMTP": eventPortEventSMTP,
       "monitorAndDiag": monitorAndDiag,
       "macAddressTable": macAddressTable,
       "agingTimeSetting": agingTimeSetting,
       "flushMACStatus": flushMACStatus,
       "macAddrTable": macAddrTable,
       "macAddrEntry": macAddrEntry,
       "macAddressIndex": macAddressIndex,
       "macAddressPortName": macAddressPortName,
       "macAddressAddr": macAddressAddr,
       "macAddressType": macAddressType,
       "portSecurityClearMACTable": portSecurityClearMACTable,
       "portStatistic": portStatistic,
       "switchPortStatTable": switchPortStatTable,
       "switchPortStatEntry": switchPortStatEntry,
       "swPortStatIndex": swPortStatIndex,
       "swPortStatType": swPortStatType,
       "swPortStatLink": swPortStatLink,
       "swPortStatState": swPortStatState,
       "swPortStatTXGoodPkt": swPortStatTXGoodPkt,
       "swPortStatTXBadPkt": swPortStatTXBadPkt,
       "swPortStatRXGoodPkt": swPortStatRXGoodPkt,
       "swPortStatRXBadPkt": swPortStatRXBadPkt,
       "swPortStatTXAbortPkt": swPortStatTXAbortPkt,
       "swPortStatPacketCollision": swPortStatPacketCollision,
       "portmirroring": portmirroring,
       "swPortMirrorDestinationPortTX": swPortMirrorDestinationPortTX,
       "swPortMirrorDestinationPortRX": swPortMirrorDestinationPortRX,
       "switchPortMirrorSourceTable": switchPortMirrorSourceTable,
       "switchPortMirrorSourceEntry": switchPortMirrorSourceEntry,
       "swPortMirrorPortNum": swPortMirrorPortNum,
       "swPortMirrorSourcePort": swPortMirrorSourcePort,
       "eventLog": eventLog,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogDescription": eventLogDescription,
       "saveConfiguration": saveConfiguration,
       "saveCfgMgtAction": saveCfgMgtAction,
       "factoryDefault": factoryDefault,
       "factoryDefaultAction": factoryDefaultAction,
       "systemReboot": systemReboot,
       "systemRebootAction": systemRebootAction,
       "misc": misc,
       "specificTrap": specificTrap,
       "trapPowerStatus": trapPowerStatus,
       "trapTopologyChange": trapTopologyChange,
       "switchCurrentPortNameListTable": switchCurrentPortNameListTable,
       "switchCurrentPortNameListEntry": switchCurrentPortNameListEntry,
       "swCurrentPortNameListIndex": swCurrentPortNameListIndex,
       "swCurrentPortNameListPortName": swCurrentPortNameListPortName,
       "swCurrentPortNameListPortNumber": swCurrentPortNameListPortNumber}
)
