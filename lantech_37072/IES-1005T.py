# SNMP MIB module (IES-1005T) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/lantech_37072/IES-1005T.mib
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 0)
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
_Lantech_ObjectIdentity = ObjectIdentity
lantech = _Lantech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1)
)
_Ies_1005t_ObjectIdentity = ObjectIdentity
ies_1005t = _Ies_1005t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56)
)
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1, 5),
    _SystemFwVer_Type()
)
systemFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFwVer.setStatus("current")
_SystemMacAddress_Type = MacAddress
_SystemMacAddress_Object = MibScalar
systemMacAddress = _SystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 1, 6),
    _SystemMacAddress_Type()
)
systemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMacAddress.setStatus("current")
_BasicSetting_ObjectIdentity = ObjectIdentity
basicSetting = _BasicSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2)
)
_SwitchSetting_ObjectIdentity = ObjectIdentity
switchSetting = _SwitchSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 1, 1),
    _SwitchSettingSystemName_Type()
)
switchSettingSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingSystemName.setStatus("current")


class _SwitchSettingDescr_Type(DisplayString):
    """Custom type switchSettingDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchSettingDescr_Type.__name__ = "DisplayString"
_SwitchSettingDescr_Object = MibScalar
switchSettingDescr = _SwitchSettingDescr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 1, 2),
    _SwitchSettingDescr_Type()
)
switchSettingDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingDescr.setStatus("current")


class _SwitchSettingSystemLocation_Type(DisplayString):
    """Custom type switchSettingSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchSettingSystemLocation_Type.__name__ = "DisplayString"
_SwitchSettingSystemLocation_Object = MibScalar
switchSettingSystemLocation = _SwitchSettingSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 1, 3),
    _SwitchSettingSystemLocation_Type()
)
switchSettingSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingSystemLocation.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 1, 4),
    _SwitchSettingLocationAlert_Type()
)
switchSettingLocationAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingLocationAlert.setStatus("current")


class _SwitchSettingSystemContact_Type(DisplayString):
    """Custom type switchSettingSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchSettingSystemContact_Type.__name__ = "DisplayString"
_SwitchSettingSystemContact_Object = MibScalar
switchSettingSystemContact = _SwitchSettingSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 1, 5),
    _SwitchSettingSystemContact_Type()
)
switchSettingSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchSettingSystemContact.setStatus("current")
_AdminPassword_ObjectIdentity = ObjectIdentity
adminPassword = _AdminPassword_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 2, 2),
    _AdminPassword_Password_Type()
)
adminPassword_Password.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    adminPassword_Password.setStatus("current")
_IpConfiguration_ObjectIdentity = ObjectIdentity
ipConfiguration = _IpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3)
)
_IpConfigurationTable_Object = MibTable
ipConfigurationTable = _IpConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ipConfigurationTable.setStatus("current")
_IpConfigurationEntry_Object = MibTableRow
ipConfigurationEntry = _IpConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1)
)
ipConfigurationEntry.setIndexNames(
    (0, "IES-1005T", "ipConfigurationIndex"),
)
if mibBuilder.loadTexts:
    ipConfigurationEntry.setStatus("current")
_IpConfigurationIndex_Type = Integer32
_IpConfigurationIndex_Object = MibTableColumn
ipConfigurationIndex = _IpConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 2),
    _IpConfigurationDHCPStatus_Type()
)
ipConfigurationDHCPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationDHCPStatus.setStatus("current")
_IpConfigurationAddress_Type = IpAddress
_IpConfigurationAddress_Object = MibTableColumn
ipConfigurationAddress = _IpConfigurationAddress_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 3),
    _IpConfigurationAddress_Type()
)
ipConfigurationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationAddress.setStatus("current")
_IpConfigurationSubMask_Type = IpAddress
_IpConfigurationSubMask_Object = MibTableColumn
ipConfigurationSubMask = _IpConfigurationSubMask_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 4),
    _IpConfigurationSubMask_Type()
)
ipConfigurationSubMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationSubMask.setStatus("current")
_IpConfigurationGateway_Type = IpAddress
_IpConfigurationGateway_Object = MibTableColumn
ipConfigurationGateway = _IpConfigurationGateway_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 5),
    _IpConfigurationGateway_Type()
)
ipConfigurationGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationGateway.setStatus("current")
_IpConfigurationDNS1_Type = IpAddress
_IpConfigurationDNS1_Object = MibTableColumn
ipConfigurationDNS1 = _IpConfigurationDNS1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 6),
    _IpConfigurationDNS1_Type()
)
ipConfigurationDNS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationDNS1.setStatus("current")
_IpConfigurationDNS2_Type = IpAddress
_IpConfigurationDNS2_Object = MibTableColumn
ipConfigurationDNS2 = _IpConfigurationDNS2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 3, 1, 1, 7),
    _IpConfigurationDNS2_Type()
)
ipConfigurationDNS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipConfigurationDNS2.setStatus("current")
_Sntp_ObjectIdentity = ObjectIdentity
sntp = _Sntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 3),
    _SntpUTCTimezone_Type()
)
sntpUTCTimezone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpUTCTimezone.setStatus("current")
_SntpServerIP_Type = IpAddress
_SntpServerIP_Object = MibScalar
sntpServerIP = _SntpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 4),
    _SntpServerIP_Type()
)
sntpServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIP.setStatus("current")


class _SntpSwitchTimer_Type(DisplayString):
    """Custom type sntpSwitchTimer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SntpSwitchTimer_Type.__name__ = "DisplayString"
_SntpSwitchTimer_Object = MibScalar
sntpSwitchTimer = _SntpSwitchTimer_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 5),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 6),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 7),
    _SntpDaylightSavingPeriodEnd_Type()
)
sntpDaylightSavingPeriodEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingPeriodEnd.setStatus("current")
_SntpDaylightSavingOffset_Type = Integer32
_SntpDaylightSavingOffset_Object = MibScalar
sntpDaylightSavingOffset = _SntpDaylightSavingOffset_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 4, 8),
    _SntpDaylightSavingOffset_Type()
)
sntpDaylightSavingOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpDaylightSavingOffset.setStatus("current")
_Lldp_ObjectIdentity = ObjectIdentity
lldp = _Lldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 5)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 5, 1),
    _LldpStatus_Type()
)
lldpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpStatus.setStatus("current")
_LldpInterval_Type = Integer32
_LldpInterval_Object = MibScalar
lldpInterval = _LldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 5, 2),
    _LldpInterval_Type()
)
lldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpInterval.setStatus("current")
_BackupAndRestore_ObjectIdentity = ObjectIdentity
backupAndRestore = _BackupAndRestore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6)
)


class _BackupServerIP_Type(IpAddress):
    """Custom type backupServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_BackupServerIP_Type.__name__ = "IpAddress"
_BackupServerIP_Object = MibScalar
backupServerIP = _BackupServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6, 5),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 6, 6),
    _RestoreStatus_Type()
)
restoreStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restoreStatus.setStatus("current")
_TftpUpgrade_ObjectIdentity = ObjectIdentity
tftpUpgrade = _TftpUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 7)
)


class _TftpDownloadServerIP_Type(IpAddress):
    """Custom type tftpDownloadServerIP based on IpAddress"""
    defaultHexValue = "00000000"


_TftpDownloadServerIP_Type.__name__ = "IpAddress"
_TftpDownloadServerIP_Object = MibScalar
tftpDownloadServerIP = _TftpDownloadServerIP_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 2, 7, 3),
    _TftpDownloadStatus_Type()
)
tftpDownloadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpDownloadStatus.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3)
)
_PortControl_ObjectIdentity = ObjectIdentity
portControl = _PortControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1)
)
_PortCtrlTable_Object = MibTable
portCtrlTable = _PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1)
)
if mibBuilder.loadTexts:
    portCtrlTable.setStatus("current")
_PortCtrlEntry_Object = MibTableRow
portCtrlEntry = _PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1)
)
portCtrlEntry.setIndexNames(
    (0, "IES-1005T", "portCtrlIndex"),
)
if mibBuilder.loadTexts:
    portCtrlEntry.setStatus("current")
_PortCtrlIndex_Type = Integer32
_PortCtrlIndex_Object = MibTableColumn
portCtrlIndex = _PortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 6),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PortCtrlFlowControl_Type.__name__ = "Integer32"
_PortCtrlFlowControl_Object = MibTableColumn
portCtrlFlowControl = _PortCtrlFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 1, 1, 1, 7),
    _PortCtrlFlowControl_Type()
)
portCtrlFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCtrlFlowControl.setStatus("current")
_PortStatus_ObjectIdentity = ObjectIdentity
portStatus = _PortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2)
)
_SwitchPortStatTable_Object = MibTable
switchPortStatTable = _SwitchPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1)
)
if mibBuilder.loadTexts:
    switchPortStatTable.setStatus("current")
_SwitchPortStatEntry_Object = MibTableRow
switchPortStatEntry = _SwitchPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1)
)
switchPortStatEntry.setIndexNames(
    (0, "IES-1005T", "swPortStatIndex"),
)
if mibBuilder.loadTexts:
    switchPortStatEntry.setStatus("current")
_SwPortStatIndex_Type = Integer32
_SwPortStatIndex_Object = MibTableColumn
swPortStatIndex = _SwPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 1),
    _SwPortStatIndex_Type()
)
swPortStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPortStatIndex.setStatus("current")


class _SwPortStatType_Type(Integer32):
    """Custom type swPortStatType based on Integer32"""
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
        *(("hundredBaseTX", 1),
          ("hundredBaseFX", 2),
          ("thousandBaseSX", 3),
          ("thousandBaseGBIC", 4),
          ("other", 5),
          ("notPresent", 6))
    )


_SwPortStatType_Type.__name__ = "Integer32"
_SwPortStatType_Object = MibTableColumn
swPortStatType = _SwPortStatType_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 4),
    _SwPortStatState_Type()
)
swPortStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatState.setStatus("current")


class _SwPortStatSpeed_Type(Integer32):
    """Custom type swPortStatSpeed based on Integer32"""
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


_SwPortStatSpeed_Type.__name__ = "Integer32"
_SwPortStatSpeed_Object = MibTableColumn
swPortStatSpeed = _SwPortStatSpeed_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 5),
    _SwPortStatSpeed_Type()
)
swPortStatSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatSpeed.setStatus("current")


class _SwPortStatDuplex_Type(Integer32):
    """Custom type swPortStatDuplex based on Integer32"""
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


_SwPortStatDuplex_Type.__name__ = "Integer32"
_SwPortStatDuplex_Object = MibTableColumn
swPortStatDuplex = _SwPortStatDuplex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 6),
    _SwPortStatDuplex_Type()
)
swPortStatDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatDuplex.setStatus("current")


class _SwPortStatFlowControl_Type(Integer32):
    """Custom type swPortStatFlowControl based on Integer32"""
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


_SwPortStatFlowControl_Type.__name__ = "Integer32"
_SwPortStatFlowControl_Object = MibTableColumn
swPortStatFlowControl = _SwPortStatFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 3, 2, 1, 1, 7),
    _SwPortStatFlowControl_Type()
)
swPortStatFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortStatFlowControl.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 4)
)
_VlanPortBasedTable_Object = MibTable
vlanPortBasedTable = _VlanPortBasedTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 4, 1)
)
if mibBuilder.loadTexts:
    vlanPortBasedTable.setStatus("current")
_VlanPortBasedEntry_Object = MibTableRow
vlanPortBasedEntry = _VlanPortBasedEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 4, 1, 1)
)
vlanPortBasedEntry.setIndexNames(
    (0, "IES-1005T", "vlanPortBasedIndex"),
)
if mibBuilder.loadTexts:
    vlanPortBasedEntry.setStatus("current")
_VlanPortBasedIndex_Type = Integer32
_VlanPortBasedIndex_Object = MibTableColumn
vlanPortBasedIndex = _VlanPortBasedIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 4, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 4, 1, 1, 2),
    _VlanPortBasedGroupName_Type()
)
vlanPortBasedGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortBasedGroupName.setStatus("current")
_VlanPortBasedMembers_Type = PortList
_VlanPortBasedMembers_Object = MibTableColumn
vlanPortBasedMembers = _VlanPortBasedMembers_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 4, 1, 1, 3),
    _VlanPortBasedMembers_Type()
)
vlanPortBasedMembers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortBasedMembers.setStatus("current")
_Redundancy_ObjectIdentity = ObjectIdentity
redundancy = _Redundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5)
)
_RedundantRing_ObjectIdentity = ObjectIdentity
redundantRing = _RedundantRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 2),
    _RedundantRingRingMasterStatus_Type()
)
redundantRingRingMasterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingRingMasterStatus.setStatus("current")
_RedundantRingRingPort1_Type = Integer32
_RedundantRingRingPort1_Object = MibScalar
redundantRingRingPort1 = _RedundantRingRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 3),
    _RedundantRingRingPort1_Type()
)
redundantRingRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingRingPort1.setStatus("current")
_RedundantRingRingPort2_Type = Integer32
_RedundantRingRingPort2_Object = MibScalar
redundantRingRingPort2 = _RedundantRingRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 5),
    _RedundantRingCoupleRingStatus_Type()
)
redundantRingCoupleRingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingCoupleRingStatus.setStatus("current")
_RedundantRingCouplingPort_Type = Integer32
_RedundantRingCouplingPort_Object = MibScalar
redundantRingCouplingPort = _RedundantRingCouplingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 8),
    _RedundantRingDualHomingStatus_Type()
)
redundantRingDualHomingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingDualHomingStatus.setStatus("current")
_RedundantRingHomingPort_Type = Integer32
_RedundantRingHomingPort_Object = MibScalar
redundantRingHomingPort = _RedundantRingHomingPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 1, 9),
    _RedundantRingHomingPort_Type()
)
redundantRingHomingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundantRingHomingPort.setStatus("current")
_Rstp_ObjectIdentity = ObjectIdentity
rstp = _Rstp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 1),
    _RstpStatus_Type()
)
rstpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpStatus.setStatus("current")
_RstpPriority_Type = Integer32
_RstpPriority_Object = MibScalar
rstpPriority = _RstpPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 2),
    _RstpPriority_Type()
)
rstpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPriority.setStatus("current")
_RstpMaxAge_Type = Integer32
_RstpMaxAge_Object = MibScalar
rstpMaxAge = _RstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 3),
    _RstpMaxAge_Type()
)
rstpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpMaxAge.setStatus("current")
_RstpHelloTime_Type = Integer32
_RstpHelloTime_Object = MibScalar
rstpHelloTime = _RstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 4),
    _RstpHelloTime_Type()
)
rstpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpHelloTime.setStatus("current")
_RstpForwardDelayTime_Type = Integer32
_RstpForwardDelayTime_Object = MibScalar
rstpForwardDelayTime = _RstpForwardDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 5),
    _RstpForwardDelayTime_Type()
)
rstpForwardDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpForwardDelayTime.setStatus("current")
_RstpPerPortCfgTable_Object = MibTable
rstpPerPortCfgTable = _RstpPerPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6)
)
if mibBuilder.loadTexts:
    rstpPerPortCfgTable.setStatus("current")
_RstpPerPortCfgEntry_Object = MibTableRow
rstpPerPortCfgEntry = _RstpPerPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1)
)
rstpPerPortCfgEntry.setIndexNames(
    (0, "IES-1005T", "rstpPerPortCfgPortNum"),
)
if mibBuilder.loadTexts:
    rstpPerPortCfgEntry.setStatus("current")
_RstpPerPortCfgPortNum_Type = Integer32
_RstpPerPortCfgPortNum_Object = MibTableColumn
rstpPerPortCfgPortNum = _RstpPerPortCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1, 1),
    _RstpPerPortCfgPortNum_Type()
)
rstpPerPortCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortCfgPortNum.setStatus("current")
_RstpPerPortCfgPathCost_Type = Integer32
_RstpPerPortCfgPathCost_Object = MibTableColumn
rstpPerPortCfgPathCost = _RstpPerPortCfgPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1, 2),
    _RstpPerPortCfgPathCost_Type()
)
rstpPerPortCfgPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgPathCost.setStatus("current")
_RstpPerPortCfgPriority_Type = Integer32
_RstpPerPortCfgPriority_Object = MibTableColumn
rstpPerPortCfgPriority = _RstpPerPortCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 2, 6, 1, 6),
    _RstpPerPortCfgAdminNonStp_Type()
)
rstpPerPortCfgAdminNonStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rstpPerPortCfgAdminNonStp.setStatus("current")
_BridgeInformation_ObjectIdentity = ObjectIdentity
bridgeInformation = _BridgeInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3)
)
_RstpRootBridgeInformationTable_Object = MibTable
rstpRootBridgeInformationTable = _RstpRootBridgeInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1)
)
if mibBuilder.loadTexts:
    rstpRootBridgeInformationTable.setStatus("current")
_RstpRootBridgeInformationEntry_Object = MibTableRow
rstpRootBridgeInformationEntry = _RstpRootBridgeInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1)
)
rstpRootBridgeInformationEntry.setIndexNames(
    (0, "IES-1005T", "rstpRootBridgeInformationIndex"),
)
if mibBuilder.loadTexts:
    rstpRootBridgeInformationEntry.setStatus("current")
_RstpRootBridgeInformationIndex_Type = Integer32
_RstpRootBridgeInformationIndex_Object = MibTableColumn
rstpRootBridgeInformationIndex = _RstpRootBridgeInformationIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 2),
    _RstpRootBridgeInformationBridgeID_Type()
)
rstpRootBridgeInformationBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationBridgeID.setStatus("current")
_RstpRootBridgeInformationRootPriority_Type = Integer32
_RstpRootBridgeInformationRootPriority_Object = MibTableColumn
rstpRootBridgeInformationRootPriority = _RstpRootBridgeInformationRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 4),
    _RstpRootBridgeInformationRootPort_Type()
)
rstpRootBridgeInformationRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPort.setStatus("current")
_RstpRootBridgeInformationRootPathCost_Type = Integer32
_RstpRootBridgeInformationRootPathCost_Object = MibTableColumn
rstpRootBridgeInformationRootPathCost = _RstpRootBridgeInformationRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 5),
    _RstpRootBridgeInformationRootPathCost_Type()
)
rstpRootBridgeInformationRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationRootPathCost.setStatus("current")
_RstpRootBridgeInformationMaxAge_Type = Integer32
_RstpRootBridgeInformationMaxAge_Object = MibTableColumn
rstpRootBridgeInformationMaxAge = _RstpRootBridgeInformationMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 6),
    _RstpRootBridgeInformationMaxAge_Type()
)
rstpRootBridgeInformationMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationMaxAge.setStatus("current")
_RstpRootBridgeInformationHelloTime_Type = Integer32
_RstpRootBridgeInformationHelloTime_Object = MibTableColumn
rstpRootBridgeInformationHelloTime = _RstpRootBridgeInformationHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 7),
    _RstpRootBridgeInformationHelloTime_Type()
)
rstpRootBridgeInformationHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationHelloTime.setStatus("current")
_RstpRootBridgeInformationForwardDelay_Type = Integer32
_RstpRootBridgeInformationForwardDelay_Object = MibTableColumn
rstpRootBridgeInformationForwardDelay = _RstpRootBridgeInformationForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 1, 1, 8),
    _RstpRootBridgeInformationForwardDelay_Type()
)
rstpRootBridgeInformationForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpRootBridgeInformationForwardDelay.setStatus("current")
_RstpPerPortInfoTable_Object = MibTable
rstpPerPortInfoTable = _RstpPerPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2)
)
if mibBuilder.loadTexts:
    rstpPerPortInfoTable.setStatus("current")
_RstpPerPortInfoEntry_Object = MibTableRow
rstpPerPortInfoEntry = _RstpPerPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1)
)
rstpPerPortInfoEntry.setIndexNames(
    (0, "IES-1005T", "rstpPerPortInfoPortNum"),
)
if mibBuilder.loadTexts:
    rstpPerPortInfoEntry.setStatus("current")
_RstpPerPortInfoPortNum_Type = Integer32
_RstpPerPortInfoPortNum_Object = MibTableColumn
rstpPerPortInfoPortNum = _RstpPerPortInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 1),
    _RstpPerPortInfoPortNum_Type()
)
rstpPerPortInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPortNum.setStatus("current")
_RstpPerPortInfoPathCost_Type = Integer32
_RstpPerPortInfoPathCost_Object = MibTableColumn
rstpPerPortInfoPathCost = _RstpPerPortInfoPathCost_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 2),
    _RstpPerPortInfoPathCost_Type()
)
rstpPerPortInfoPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoPathCost.setStatus("current")
_RstpPerPortInfoPriority_Type = Integer32
_RstpPerPortInfoPriority_Object = MibTableColumn
rstpPerPortInfoPriority = _RstpPerPortInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 3, 2, 1, 8),
    _RstpPerPortInfoRole_Type()
)
rstpPerPortInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rstpPerPortInfoRole.setStatus("current")
_FastRecovery_ObjectIdentity = ObjectIdentity
fastRecovery = _FastRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 4)
)


class _FastRecoveryStatus_Type(Integer32):
    """Custom type fastRecoveryStatus based on Integer32"""
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


_FastRecoveryStatus_Type.__name__ = "Integer32"
_FastRecoveryStatus_Object = MibScalar
fastRecoveryStatus = _FastRecoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 4, 1),
    _FastRecoveryStatus_Type()
)
fastRecoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRecoveryStatus.setStatus("current")
_FastRecoveryCfgTable_Object = MibTable
fastRecoveryCfgTable = _FastRecoveryCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 4, 2)
)
if mibBuilder.loadTexts:
    fastRecoveryCfgTable.setStatus("current")
_FastRecoveryCfgEntry_Object = MibTableRow
fastRecoveryCfgEntry = _FastRecoveryCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 4, 2, 1)
)
fastRecoveryCfgEntry.setIndexNames(
    (0, "IES-1005T", "fastRecoveryCfgPortNum"),
)
if mibBuilder.loadTexts:
    fastRecoveryCfgEntry.setStatus("current")
_FastRecoveryCfgPortNum_Type = Integer32
_FastRecoveryCfgPortNum_Object = MibTableColumn
fastRecoveryCfgPortNum = _FastRecoveryCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 4, 2, 1, 1),
    _FastRecoveryCfgPortNum_Type()
)
fastRecoveryCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastRecoveryCfgPortNum.setStatus("current")


class _FastRecoveryCfgMode_Type(Integer32):
    """Custom type fastRecoveryCfgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("not_included", 0),
          ("p1", 1),
          ("p2", 2),
          ("p3", 3),
          ("p4", 4),
          ("p5", 5))
    )


_FastRecoveryCfgMode_Type.__name__ = "Integer32"
_FastRecoveryCfgMode_Object = MibTableColumn
fastRecoveryCfgMode = _FastRecoveryCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 5, 4, 2, 1, 2),
    _FastRecoveryCfgMode_Type()
)
fastRecoveryCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fastRecoveryCfgMode.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6)
)


class _SnmpAgentMode_Type(Integer32):
    """Custom type snmpAgentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1v2Conly", 1),
          ("v3", 2),
          ("v1v2Cv3", 3))
    )


_SnmpAgentMode_Type.__name__ = "Integer32"
_SnmpAgentMode_Object = MibScalar
snmpAgentMode = _SnmpAgentMode_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 4),
    _SnmpSystemContact_Type()
)
snmpSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSystemContact.setStatus("current")
_SnmpCommunityStringTable_Object = MibTable
snmpCommunityStringTable = _SnmpCommunityStringTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 5)
)
if mibBuilder.loadTexts:
    snmpCommunityStringTable.setStatus("current")
_SnmpCommunityStringEntry_Object = MibTableRow
snmpCommunityStringEntry = _SnmpCommunityStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 5, 1)
)
snmpCommunityStringEntry.setIndexNames(
    (0, "IES-1005T", "snmpCommunityStringIndex"),
)
if mibBuilder.loadTexts:
    snmpCommunityStringEntry.setStatus("current")
_SnmpCommunityStringIndex_Type = Integer32
_SnmpCommunityStringIndex_Object = MibTableColumn
snmpCommunityStringIndex = _SnmpCommunityStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 5, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 5, 1, 4),
    _SnmpCommunityStringStatus_Type()
)
snmpCommunityStringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStringStatus.setStatus("current")
_SnmpTrapServerTable_Object = MibTable
snmpTrapServerTable = _SnmpTrapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6)
)
if mibBuilder.loadTexts:
    snmpTrapServerTable.setStatus("current")
_SnmpTrapServerEntry_Object = MibTableRow
snmpTrapServerEntry = _SnmpTrapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6, 1)
)
snmpTrapServerEntry.setIndexNames(
    (0, "IES-1005T", "snmpTrapServerIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapServerEntry.setStatus("current")
_SnmpTrapServerIndex_Type = Integer32
_SnmpTrapServerIndex_Object = MibTableColumn
snmpTrapServerIndex = _SnmpTrapServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6, 1, 1),
    _SnmpTrapServerIndex_Type()
)
snmpTrapServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapServerIndex.setStatus("current")
_SnmpTrapServerIPAddr_Type = IpAddress
_SnmpTrapServerIPAddr_Object = MibTableColumn
snmpTrapServerIPAddr = _SnmpTrapServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 6, 6, 1, 5),
    _SnmpTrapServerStatus_Type()
)
snmpTrapServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapServerStatus.setStatus("current")
_Qos_ObjectIdentity = ObjectIdentity
qos = _Qos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 2),
    _QosPriorityType_Type()
)
qosPriorityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPriorityType.setStatus("current")
_QosPortBasedPriorityTable_Object = MibTable
qosPortBasedPriorityTable = _QosPortBasedPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 3)
)
if mibBuilder.loadTexts:
    qosPortBasedPriorityTable.setStatus("current")
_QosPortBasedPriorityEntry_Object = MibTableRow
qosPortBasedPriorityEntry = _QosPortBasedPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 3, 1)
)
qosPortBasedPriorityEntry.setIndexNames(
    (0, "IES-1005T", "qosPortBasedPriorityPortNum"),
)
if mibBuilder.loadTexts:
    qosPortBasedPriorityEntry.setStatus("current")
_QosPortBasedPriorityPortNum_Type = Integer32
_QosPortBasedPriorityPortNum_Object = MibTableColumn
qosPortBasedPriorityPortNum = _QosPortBasedPriorityPortNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 3, 1, 2),
    _QosPortBasedPriority_Type()
)
qosPortBasedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosPortBasedPriority.setStatus("current")
_QosCOSTable_Object = MibTable
qosCOSTable = _QosCOSTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 4)
)
if mibBuilder.loadTexts:
    qosCOSTable.setStatus("current")
_QosCOSEntry_Object = MibTableRow
qosCOSEntry = _QosCOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 4, 1)
)
qosCOSEntry.setIndexNames(
    (0, "IES-1005T", "qosCOSPriority"),
)
if mibBuilder.loadTexts:
    qosCOSEntry.setStatus("current")
_QosCOSPriority_Type = Integer32
_QosCOSPriority_Object = MibTableColumn
qosCOSPriority = _QosCOSPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 4, 1, 2),
    _QosCOS_Type()
)
qosCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCOS.setStatus("current")
_QosCOSPortDefaultTable_Object = MibTable
qosCOSPortDefaultTable = _QosCOSPortDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 5)
)
if mibBuilder.loadTexts:
    qosCOSPortDefaultTable.setStatus("current")
_QosCOSPortDefaultEntry_Object = MibTableRow
qosCOSPortDefaultEntry = _QosCOSPortDefaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 5, 1)
)
qosCOSPortDefaultEntry.setIndexNames(
    (0, "IES-1005T", "qosCOSPriority"),
)
if mibBuilder.loadTexts:
    qosCOSPortDefaultEntry.setStatus("current")
_QosCOSPort_Type = Integer32
_QosCOSPort_Object = MibTableColumn
qosCOSPort = _QosCOSPort_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 5, 1, 1),
    _QosCOSPort_Type()
)
qosCOSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosCOSPort.setStatus("current")
_QosCOSPortDefault_Type = Integer32
_QosCOSPortDefault_Object = MibTableColumn
qosCOSPortDefault = _QosCOSPortDefault_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 5, 1, 2),
    _QosCOSPortDefault_Type()
)
qosCOSPortDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosCOSPortDefault.setStatus("current")
_QosTOSTable_Object = MibTable
qosTOSTable = _QosTOSTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 6)
)
if mibBuilder.loadTexts:
    qosTOSTable.setStatus("current")
_QosTOSEntry_Object = MibTableRow
qosTOSEntry = _QosTOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 6, 1)
)
qosTOSEntry.setIndexNames(
    (0, "IES-1005T", "qosTOSPriority"),
)
if mibBuilder.loadTexts:
    qosTOSEntry.setStatus("current")
_QosTOSPriority_Type = Integer32
_QosTOSPriority_Object = MibTableColumn
qosTOSPriority = _QosTOSPriority_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 7, 6, 1, 2),
    _QosTOS_Type()
)
qosTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTOS.setStatus("current")
_Macfilter_ObjectIdentity = ObjectIdentity
macfilter = _Macfilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8)
)
_StaticMacListMgt_ObjectIdentity = ObjectIdentity
staticMacListMgt = _StaticMacListMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1)
)
_StaticMacListTable_Object = MibTable
staticMacListTable = _StaticMacListTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1, 1)
)
if mibBuilder.loadTexts:
    staticMacListTable.setStatus("current")
_StaticMacListEntry_Object = MibTableRow
staticMacListEntry = _StaticMacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1, 1, 1)
)
staticMacListEntry.setIndexNames(
    (0, "IES-1005T", "staticMacListIndex"),
)
if mibBuilder.loadTexts:
    staticMacListEntry.setStatus("current")
_StaticMacListIndex_Type = Integer32
_StaticMacListIndex_Object = MibTableColumn
staticMacListIndex = _StaticMacListIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1, 1, 1, 1),
    _StaticMacListIndex_Type()
)
staticMacListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticMacListIndex.setStatus("current")


class _StaticMacListPortName_Type(DisplayString):
    """Custom type staticMacListPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_StaticMacListPortName_Type.__name__ = "DisplayString"
_StaticMacListPortName_Object = MibTableColumn
staticMacListPortName = _StaticMacListPortName_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1, 1, 1, 2),
    _StaticMacListPortName_Type()
)
staticMacListPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacListPortName.setStatus("current")
_StaticMacListAddr_Type = MacAddress
_StaticMacListAddr_Object = MibTableColumn
staticMacListAddr = _StaticMacListAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1, 1, 1, 3),
    _StaticMacListAddr_Type()
)
staticMacListAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMacListAddr.setStatus("current")


class _StaticMacListStatus_Type(Integer32):
    """Custom type staticMacListStatus based on Integer32"""
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


_StaticMacListStatus_Type.__name__ = "Integer32"
_StaticMacListStatus_Object = MibTableColumn
staticMacListStatus = _StaticMacListStatus_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 1, 1, 1, 4),
    _StaticMacListStatus_Type()
)
staticMacListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMacListStatus.setStatus("current")
_MacBlacklist_ObjectIdentity = ObjectIdentity
macBlacklist = _MacBlacklist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 2)
)
_MacBlacklistTable_Object = MibTable
macBlacklistTable = _MacBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 2, 1)
)
if mibBuilder.loadTexts:
    macBlacklistTable.setStatus("current")
_MacBlacklistEntry_Object = MibTableRow
macBlacklistEntry = _MacBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 2, 1, 1)
)
macBlacklistEntry.setIndexNames(
    (0, "IES-1005T", "macBlacklistIndex"),
)
if mibBuilder.loadTexts:
    macBlacklistEntry.setStatus("current")
_MacBlacklistIndex_Type = Integer32
_MacBlacklistIndex_Object = MibTableColumn
macBlacklistIndex = _MacBlacklistIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 2, 1, 1, 1),
    _MacBlacklistIndex_Type()
)
macBlacklistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macBlacklistIndex.setStatus("current")
_MacBlacklistAddr_Type = MacAddress
_MacBlacklistAddr_Object = MibTableColumn
macBlacklistAddr = _MacBlacklistAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 8, 2, 1, 1, 3),
    _MacBlacklistStatus_Type()
)
macBlacklistStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macBlacklistStatus.setStatus("current")
_Warning_ObjectIdentity = ObjectIdentity
warning = _Warning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9)
)
_EventAndEmailWarning_ObjectIdentity = ObjectIdentity
eventAndEmailWarning = _EventAndEmailWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1)
)
_EventSelection_ObjectIdentity = ObjectIdentity
eventSelection = _EventSelection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1)
)
_SystemEventsTable_Object = MibTable
systemEventsTable = _SystemEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    systemEventsTable.setStatus("current")
_SystemEventsEntry_Object = MibTableRow
systemEventsEntry = _SystemEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 1, 1)
)
systemEventsEntry.setIndexNames(
    (0, "IES-1005T", "eventSystemEventsIndex"),
)
if mibBuilder.loadTexts:
    systemEventsEntry.setStatus("current")
_EventSystemEventsIndex_Type = Integer32
_EventSystemEventsIndex_Object = MibTableColumn
eventSystemEventsIndex = _EventSystemEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 1, 1, 2),
    _EventDeviceColdStartEvent_Type()
)
eventDeviceColdStartEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDeviceColdStartEvent.setStatus("current")


class _EventORingTopologyChangeEvent_Type(Integer32):
    """Custom type eventORingTopologyChangeEvent based on Integer32"""
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


_EventORingTopologyChangeEvent_Type.__name__ = "Integer32"
_EventORingTopologyChangeEvent_Object = MibTableColumn
eventORingTopologyChangeEvent = _EventORingTopologyChangeEvent_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 1, 1, 3),
    _EventORingTopologyChangeEvent_Type()
)
eventORingTopologyChangeEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventORingTopologyChangeEvent.setStatus("current")
_PortEventsTable_Object = MibTable
portEventsTable = _PortEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    portEventsTable.setStatus("current")
_PortEventsEntry_Object = MibTableRow
portEventsEntry = _PortEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 2, 1)
)
portEventsEntry.setIndexNames(
    (0, "IES-1005T", "eventPortNumber"),
)
if mibBuilder.loadTexts:
    portEventsEntry.setStatus("current")
_EventPortNumber_Type = Integer32
_EventPortNumber_Object = MibTableColumn
eventPortNumber = _EventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 1, 2, 1, 3),
    _EventPortEventSMTP_Type()
)
eventPortEventSMTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventPortEventSMTP.setStatus("current")
_SysLogConfiguration_ObjectIdentity = ObjectIdentity
sysLogConfiguration = _SysLogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 2, 1),
    _SyslogStatus_Type()
)
syslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogStatus.setStatus("current")
_EventServerAddr_Type = IpAddress
_EventServerAddr_Object = MibScalar
eventServerAddr = _EventServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 2, 2),
    _EventServerAddr_Type()
)
eventServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventServerAddr.setStatus("current")
_SmtpConfiguration_ObjectIdentity = ObjectIdentity
smtpConfiguration = _SmtpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 1),
    _EventEmailAlertStatus_Type()
)
eventEmailAlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertStatus.setStatus("current")
_EventEmailAlertAddr_Type = IpAddress
_EventEmailAlertAddr_Object = MibScalar
eventEmailAlertAddr = _EventEmailAlertAddr_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 5),
    _EventEmailAlertPassword_Type()
)
eventEmailAlertPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    eventEmailAlertPassword.setStatus("current")
_EmailAlertRcptTable_Object = MibTable
emailAlertRcptTable = _EmailAlertRcptTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 6)
)
if mibBuilder.loadTexts:
    emailAlertRcptTable.setStatus("current")
_EmailAlertRcptEntry_Object = MibTableRow
emailAlertRcptEntry = _EmailAlertRcptEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 6, 1)
)
emailAlertRcptEntry.setIndexNames(
    (0, "IES-1005T", "eventEmailAlertRcptIndex"),
)
if mibBuilder.loadTexts:
    emailAlertRcptEntry.setStatus("current")
_EventEmailAlertRcptIndex_Type = Integer32
_EventEmailAlertRcptIndex_Object = MibTableColumn
eventEmailAlertRcptIndex = _EventEmailAlertRcptIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 1, 3, 6, 1, 2),
    _EventEmailAlertRcptEmailAddr_Type()
)
eventEmailAlertRcptEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEmailAlertRcptEmailAddr.setStatus("current")
_EventLog_ObjectIdentity = ObjectIdentity
eventLog = _EventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 2)
)
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 2, 1)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 2, 1, 1)
)
eventLogEntry.setIndexNames(
    (0, "IES-1005T", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")
_EventLogIndex_Type = Integer32
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 2, 1, 1, 2),
    _EventLogDescription_Type()
)
eventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDescription.setStatus("current")
_FaultAlarm_ObjectIdentity = ObjectIdentity
faultAlarm = _FaultAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3, 2),
    _FaultAlarmPwr2_Type()
)
faultAlarmPwr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultAlarmPwr2.setStatus("current")
_FaultAlarmPortCfgTable_Object = MibTable
faultAlarmPortCfgTable = _FaultAlarmPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3, 3)
)
if mibBuilder.loadTexts:
    faultAlarmPortCfgTable.setStatus("current")
_FaultAlarmPortCfgEntry_Object = MibTableRow
faultAlarmPortCfgEntry = _FaultAlarmPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3, 3, 1)
)
faultAlarmPortCfgEntry.setIndexNames(
    (0, "IES-1005T", "faultAlarmPortCfgNum"),
)
if mibBuilder.loadTexts:
    faultAlarmPortCfgEntry.setStatus("current")
_FaultAlarmPortCfgNum_Type = Integer32
_FaultAlarmPortCfgNum_Object = MibTableColumn
faultAlarmPortCfgNum = _FaultAlarmPortCfgNum_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 9, 3, 3, 1, 2),
    _FaultAlarmPortLinkStatus_Type()
)
faultAlarmPortLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultAlarmPortLinkStatus.setStatus("current")
_Save_ObjectIdentity = ObjectIdentity
save = _Save_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 10)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 10, 1),
    _SaveCfgMgtAction_Type()
)
saveCfgMgtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveCfgMgtAction.setStatus("current")
_FactoryDefault_ObjectIdentity = ObjectIdentity
factoryDefault = _FactoryDefault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 11)
)


class _FactoryDefaultAction_Type(Integer32):
    """Custom type factoryDefaultAction based on Integer32"""
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


_FactoryDefaultAction_Type.__name__ = "Integer32"
_FactoryDefaultAction_Object = MibScalar
factoryDefaultAction = _FactoryDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 11, 1),
    _FactoryDefaultAction_Type()
)
factoryDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    factoryDefaultAction.setStatus("current")
_SystemReboot_ObjectIdentity = ObjectIdentity
systemReboot = _SystemReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 12)
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
    (1, 3, 6, 1, 4, 1, 37072, 105, 0, 1, 56, 12, 1),
    _SystemRebootAction_Type()
)
systemRebootAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemRebootAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IES-1005T",
    **{"DisplayString": DisplayString,
       "MacAddress": MacAddress,
       "PortList": PortList,
       "private": private,
       "enterprises": enterprises,
       "switches": switches,
       "lantech": lantech,
       "products": products,
       "switch": switch,
       "ies-1005t": ies_1005t,
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
       "switchSettingDescr": switchSettingDescr,
       "switchSettingSystemLocation": switchSettingSystemLocation,
       "switchSettingLocationAlert": switchSettingLocationAlert,
       "switchSettingSystemContact": switchSettingSystemContact,
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
       "sntpServerIP": sntpServerIP,
       "sntpSwitchTimer": sntpSwitchTimer,
       "sntpDaylightSavingPeriodStart": sntpDaylightSavingPeriodStart,
       "sntpDaylightSavingPeriodEnd": sntpDaylightSavingPeriodEnd,
       "sntpDaylightSavingOffset": sntpDaylightSavingOffset,
       "lldp": lldp,
       "lldpStatus": lldpStatus,
       "lldpInterval": lldpInterval,
       "backupAndRestore": backupAndRestore,
       "backupServerIP": backupServerIP,
       "backupAgentBoardFwFileName": backupAgentBoardFwFileName,
       "backupStatus": backupStatus,
       "restoreServerIP": restoreServerIP,
       "restoreAgentBoardFwFileName": restoreAgentBoardFwFileName,
       "restoreStatus": restoreStatus,
       "tftpUpgrade": tftpUpgrade,
       "tftpDownloadServerIP": tftpDownloadServerIP,
       "tftpDownloadAgentBoardFwFileName": tftpDownloadAgentBoardFwFileName,
       "tftpDownloadStatus": tftpDownloadStatus,
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
       "portStatus": portStatus,
       "switchPortStatTable": switchPortStatTable,
       "switchPortStatEntry": switchPortStatEntry,
       "swPortStatIndex": swPortStatIndex,
       "swPortStatType": swPortStatType,
       "swPortStatLink": swPortStatLink,
       "swPortStatState": swPortStatState,
       "swPortStatSpeed": swPortStatSpeed,
       "swPortStatDuplex": swPortStatDuplex,
       "swPortStatFlowControl": swPortStatFlowControl,
       "vlan": vlan,
       "vlanPortBasedTable": vlanPortBasedTable,
       "vlanPortBasedEntry": vlanPortBasedEntry,
       "vlanPortBasedIndex": vlanPortBasedIndex,
       "vlanPortBasedGroupName": vlanPortBasedGroupName,
       "vlanPortBasedMembers": vlanPortBasedMembers,
       "redundancy": redundancy,
       "redundantRing": redundantRing,
       "redundantRingStatus": redundantRingStatus,
       "redundantRingRingMasterStatus": redundantRingRingMasterStatus,
       "redundantRingRingPort1": redundantRingRingPort1,
       "redundantRingRingPort2": redundantRingRingPort2,
       "redundantRingCoupleRingStatus": redundantRingCoupleRingStatus,
       "redundantRingCouplingPort": redundantRingCouplingPort,
       "redundantRingDualHomingStatus": redundantRingDualHomingStatus,
       "redundantRingHomingPort": redundantRingHomingPort,
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
       "bridgeInformation": bridgeInformation,
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
       "fastRecovery": fastRecovery,
       "fastRecoveryStatus": fastRecoveryStatus,
       "fastRecoveryCfgTable": fastRecoveryCfgTable,
       "fastRecoveryCfgEntry": fastRecoveryCfgEntry,
       "fastRecoveryCfgPortNum": fastRecoveryCfgPortNum,
       "fastRecoveryCfgMode": fastRecoveryCfgMode,
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
       "qos": qos,
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
       "macfilter": macfilter,
       "staticMacListMgt": staticMacListMgt,
       "staticMacListTable": staticMacListTable,
       "staticMacListEntry": staticMacListEntry,
       "staticMacListIndex": staticMacListIndex,
       "staticMacListPortName": staticMacListPortName,
       "staticMacListAddr": staticMacListAddr,
       "staticMacListStatus": staticMacListStatus,
       "macBlacklist": macBlacklist,
       "macBlacklistTable": macBlacklistTable,
       "macBlacklistEntry": macBlacklistEntry,
       "macBlacklistIndex": macBlacklistIndex,
       "macBlacklistAddr": macBlacklistAddr,
       "macBlacklistStatus": macBlacklistStatus,
       "warning": warning,
       "eventAndEmailWarning": eventAndEmailWarning,
       "eventSelection": eventSelection,
       "systemEventsTable": systemEventsTable,
       "systemEventsEntry": systemEventsEntry,
       "eventSystemEventsIndex": eventSystemEventsIndex,
       "eventDeviceColdStartEvent": eventDeviceColdStartEvent,
       "eventORingTopologyChangeEvent": eventORingTopologyChangeEvent,
       "portEventsTable": portEventsTable,
       "portEventsEntry": portEventsEntry,
       "eventPortNumber": eventPortNumber,
       "eventPortEventLog": eventPortEventLog,
       "eventPortEventSMTP": eventPortEventSMTP,
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
       "eventLog": eventLog,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogDescription": eventLogDescription,
       "faultAlarm": faultAlarm,
       "faultAlarmPwr1": faultAlarmPwr1,
       "faultAlarmPwr2": faultAlarmPwr2,
       "faultAlarmPortCfgTable": faultAlarmPortCfgTable,
       "faultAlarmPortCfgEntry": faultAlarmPortCfgEntry,
       "faultAlarmPortCfgNum": faultAlarmPortCfgNum,
       "faultAlarmPortLinkStatus": faultAlarmPortLinkStatus,
       "save": save,
       "saveCfgMgtAction": saveCfgMgtAction,
       "factoryDefault": factoryDefault,
       "factoryDefaultAction": factoryDefaultAction,
       "systemReboot": systemReboot,
       "systemRebootAction": systemRebootAction}
)
