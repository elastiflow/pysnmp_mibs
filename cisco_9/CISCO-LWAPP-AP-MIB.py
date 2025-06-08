# SNMP MIB module (CISCO-LWAPP-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-AP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:34 2025
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

(cldRegulatoryDomain,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-MIB",
    "cldRegulatoryDomain")

(cLRFProfileHDClientTrapThreshold,
 cLRFProfileHighDensityMaxRadioClients) = mibBuilder.importSymbols(
    "CISCO-LWAPP-RF-MIB",
    "cLRFProfileHDClientTrapThreshold",
    "cLRFProfileHighDensityMaxRadioClients")

(CLApAssocFailureReason,
 CLApDot11RadioRole,
 CLApDot11RadioSubband,
 CLApIfType,
 CLApMode,
 CLApNtpStatus,
 CLDot11Band,
 CLDot11Channel) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApAssocFailureReason",
    "CLApDot11RadioRole",
    "CLApDot11RadioSubband",
    "CLApIfType",
    "CLApMode",
    "CLApNtpStatus",
    "CLDot11Band",
    "CLDot11Channel")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Unsigned64,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned64")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513)
)
if mibBuilder.loadTexts:
    ciscoLwappApMIB.setRevisions(
        ("2022-06-06 00:00",
         "2022-01-01 00:00",
         "2021-10-01 00:00",
         "2021-06-06 00:00",
         "2020-10-26 00:00",
         "2020-10-08 00:00",
         "2020-09-29 00:00",
         "2020-04-28 00:00",
         "2020-03-31 00:00",
         "2019-11-08 00:00",
         "2019-10-16 00:00",
         "2019-06-25 00:00",
         "2019-04-08 00:00",
         "2018-09-17 00:00",
         "2018-07-26 00:00",
         "2018-06-26 00:00",
         "2018-04-24 01:01",
         "2018-04-24 00:00",
         "2018-03-28 00:00",
         "2017-07-07 00:00",
         "2017-05-07 00:00",
         "2016-08-30 00:00",
         "2016-04-07 00:00",
         "2015-09-21 00:00",
         "2014-07-15 00:00",
         "2012-06-13 00:00",
         "2011-02-07 00:00",
         "2011-01-21 00:00",
         "2011-01-10 00:00",
         "2010-12-13 00:00",
         "2010-08-19 00:00",
         "2007-01-03 00:00",
         "2006-07-18 00:00",
         "2006-03-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappApMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBNotifs = _CiscoLwappApMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0)
)
_CiscoLwappApMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBObjects = _CiscoLwappApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1)
)
_CiscoLwappAp_ObjectIdentity = ObjectIdentity
ciscoLwappAp = _CiscoLwappAp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1)
)
_CLApTable_Object = MibTable
cLApTable = _CLApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLApTable.setStatus("current")
_CLApEntry_Object = MibTableRow
cLApEntry = _CLApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1)
)
cLApEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApEntry.setStatus("current")
_CLApSysMacAddress_Type = MacAddress
_CLApSysMacAddress_Object = MibTableColumn
cLApSysMacAddress = _CLApSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 1),
    _CLApSysMacAddress_Type()
)
cLApSysMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApSysMacAddress.setStatus("current")
_CLApIfMacAddress_Type = MacAddress
_CLApIfMacAddress_Object = MibTableColumn
cLApIfMacAddress = _CLApIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 2),
    _CLApIfMacAddress_Type()
)
cLApIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApIfMacAddress.setStatus("current")
_CLApMaxNumberOfDot11Slots_Type = Unsigned32
_CLApMaxNumberOfDot11Slots_Object = MibTableColumn
cLApMaxNumberOfDot11Slots = _CLApMaxNumberOfDot11Slots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 3),
    _CLApMaxNumberOfDot11Slots_Type()
)
cLApMaxNumberOfDot11Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxNumberOfDot11Slots.setStatus("current")
_CLApEntPhysicalIndex_Type = PhysicalIndex
_CLApEntPhysicalIndex_Object = MibTableColumn
cLApEntPhysicalIndex = _CLApEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 4),
    _CLApEntPhysicalIndex_Type()
)
cLApEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEntPhysicalIndex.setStatus("current")


class _CLApName_Type(SnmpAdminString):
    """Custom type cLApName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApName_Type.__name__ = "SnmpAdminString"
_CLApName_Object = MibTableColumn
cLApName = _CLApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 5),
    _CLApName_Type()
)
cLApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApName.setStatus("current")
_CLApUpTime_Type = TimeTicks
_CLApUpTime_Object = MibTableColumn
cLApUpTime = _CLApUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 6),
    _CLApUpTime_Type()
)
cLApUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUpTime.setStatus("current")
_CLLwappUpTime_Type = TimeTicks
_CLLwappUpTime_Object = MibTableColumn
cLLwappUpTime = _CLLwappUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 7),
    _CLLwappUpTime_Type()
)
cLLwappUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLwappUpTime.setStatus("current")
_CLLwappJoinTakenTime_Type = TimeTicks
_CLLwappJoinTakenTime_Object = MibTableColumn
cLLwappJoinTakenTime = _CLLwappJoinTakenTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 8),
    _CLLwappJoinTakenTime_Type()
)
cLLwappJoinTakenTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLLwappJoinTakenTime.setStatus("current")
_CLApMaxNumberOfEthernetSlots_Type = Unsigned32
_CLApMaxNumberOfEthernetSlots_Object = MibTableColumn
cLApMaxNumberOfEthernetSlots = _CLApMaxNumberOfEthernetSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 9),
    _CLApMaxNumberOfEthernetSlots_Type()
)
cLApMaxNumberOfEthernetSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxNumberOfEthernetSlots.setStatus("current")
_CLApPrimaryControllerAddressType_Type = InetAddressType
_CLApPrimaryControllerAddressType_Object = MibTableColumn
cLApPrimaryControllerAddressType = _CLApPrimaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 10),
    _CLApPrimaryControllerAddressType_Type()
)
cLApPrimaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimaryControllerAddressType.setStatus("current")
_CLApPrimaryControllerAddress_Type = InetAddress
_CLApPrimaryControllerAddress_Object = MibTableColumn
cLApPrimaryControllerAddress = _CLApPrimaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 11),
    _CLApPrimaryControllerAddress_Type()
)
cLApPrimaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimaryControllerAddress.setStatus("current")
_CLApSecondaryControllerAddressType_Type = InetAddressType
_CLApSecondaryControllerAddressType_Object = MibTableColumn
cLApSecondaryControllerAddressType = _CLApSecondaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 12),
    _CLApSecondaryControllerAddressType_Type()
)
cLApSecondaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSecondaryControllerAddressType.setStatus("current")
_CLApSecondaryControllerAddress_Type = InetAddress
_CLApSecondaryControllerAddress_Object = MibTableColumn
cLApSecondaryControllerAddress = _CLApSecondaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 13),
    _CLApSecondaryControllerAddress_Type()
)
cLApSecondaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSecondaryControllerAddress.setStatus("current")
_CLApTertiaryControllerAddressType_Type = InetAddressType
_CLApTertiaryControllerAddressType_Object = MibTableColumn
cLApTertiaryControllerAddressType = _CLApTertiaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 14),
    _CLApTertiaryControllerAddressType_Type()
)
cLApTertiaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTertiaryControllerAddressType.setStatus("current")
_CLApTertiaryControllerAddress_Type = InetAddress
_CLApTertiaryControllerAddress_Object = MibTableColumn
cLApTertiaryControllerAddress = _CLApTertiaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 15),
    _CLApTertiaryControllerAddress_Type()
)
cLApTertiaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTertiaryControllerAddress.setStatus("current")


class _CLApLastRebootReason_Type(Integer32):
    """Custom type cLApLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dot11gModeChange", 1),
          ("ipAddressSet", 2),
          ("ipAddressReset", 3),
          ("rebootFromController", 4),
          ("dhcpFallbackFail", 5),
          ("discoveryFail", 6),
          ("noJoinResponse", 7),
          ("denyJoin", 8),
          ("noConfigResponse", 9),
          ("configController", 10),
          ("imageUpgradeSuccess", 11),
          ("imageOpcodeInvalid", 12),
          ("imageCheckSumInvalid", 13),
          ("imageDataTimeout", 14),
          ("configFileInvalid", 15),
          ("imageDownloadError", 16),
          ("rebootFromConsole", 17),
          ("rapOverAir", 18),
          ("powerLow", 19),
          ("crash", 20),
          ("powerHigh", 21),
          ("powerLoss", 22),
          ("powerChange", 23),
          ("componentFailure", 24),
          ("watchdog", 25),
          ("lscEnabled", 26),
          ("lscDisabled", 27),
          ("lscProvTimeout", 28),
          ("lscMaxProvReqRetries", 29),
          ("lscLoadFailure", 30),
          ("lscJoinFailure", 31),
          ("capwapTimerFailure", 32),
          ("staticIpFailover", 33),
          ("vlanTagFailover", 34),
          ("capwapDiscoveryRequest", 35),
          ("capwapDiscoveryResponse", 36),
          ("capwapJoinRequest", 37),
          ("capwapJoinResponse", 38),
          ("capwapConfigurationStatus", 39),
          ("capwapConfigurationStatusResponse", 40),
          ("capwapConfigurationUpdateRequest", 41),
          ("capwapConfigurationUpdateResponse", 42),
          ("capwapWtpEventRequest", 43),
          ("capwapWtpEventResponse", 44),
          ("capwapChangeStateEventRequest", 45),
          ("capwapChangeStateEventResponse", 46),
          ("capwapEchoRequest", 47),
          ("capwapEchoResponse", 48),
          ("capwapImageDataRequest", 49),
          ("capwapImageDataResponse", 50),
          ("capwapResetRequest", 51),
          ("capwapResetResponse", 52),
          ("capwapPrimaryDiscoveryRequest", 53),
          ("capwapPrimaryDiscoveryResponse", 54),
          ("capwapDataTransferRequest", 55),
          ("capwapDataTransferResponse", 56),
          ("capwapClearConfigurationRequest", 57),
          ("capwapClearConfigurationResponse", 58),
          ("capwapMobileConfigurationRequest", 59),
          ("capwapMobileConfigurationResponse", 60),
          ("capwapPathMtuRequest", 61),
          ("capwapPathMtuResponse", 62),
          ("vlanTagRetry", 63),
          ("ipv6AddrSet", 64),
          ("modeChange", 65),
          ("typeChangedToCapwap", 66),
          ("typeChangedToMe", 67),
          ("eraseCfgCommand", 68),
          ("oeapModeCfgUpload", 69),
          ("lagCfg", 70),
          ("fipsModeChange", 71),
          ("diminishedPowerChange", 72),
          ("slubDebug", 73),
          ("lscModeCapwap", 74),
          ("lscModeDot1x", 75),
          ("lscModeAll", 76),
          ("apTypeCloud", 77),
          ("dtlsInitFailure", 78),
          ("pnpNoCapwapBackOff", 79),
          ("day0CfgFail", 80),
          ("day1CfgFail", 81),
          ("pnpTriggeredReload", 82),
          ("triRadioSupport", 83),
          ("indoorDeployment", 84),
          ("apTypeWgbToCapwap", 85),
          ("apTypeCloudToCapwap", 86),
          ("apTypeWgb", 87))
    )


_CLApLastRebootReason_Type.__name__ = "Integer32"
_CLApLastRebootReason_Object = MibTableColumn
cLApLastRebootReason = _CLApLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 16),
    _CLApLastRebootReason_Type()
)
cLApLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLastRebootReason.setStatus("current")


class _CLApEncryptionEnable_Type(TruthValue):
    """Custom type cLApEncryptionEnable based on TruthValue"""
    defaultValue = 2


_CLApEncryptionEnable_Type.__name__ = "TruthValue"
_CLApEncryptionEnable_Object = MibTableColumn
cLApEncryptionEnable = _CLApEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 18),
    _CLApEncryptionEnable_Type()
)
cLApEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEncryptionEnable.setStatus("current")


class _CLApFailoverPriority_Type(Integer32):
    """Custom type cLApFailoverPriority based on Integer32"""
    defaultValue = 1

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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("critical", 4))
    )


_CLApFailoverPriority_Type.__name__ = "Integer32"
_CLApFailoverPriority_Object = MibTableColumn
cLApFailoverPriority = _CLApFailoverPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 19),
    _CLApFailoverPriority_Type()
)
cLApFailoverPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFailoverPriority.setStatus("current")


class _CLApPowerStatus_Type(Integer32):
    """Custom type cLApPowerStatus based on Integer32"""
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
        *(("low", 1),
          ("fifteendotfour", 2),
          ("sixteendoteight", 3),
          ("full", 4),
          ("external", 5),
          ("twentyfivedotfive", 6),
          ("mixedmode", 7))
    )


_CLApPowerStatus_Type.__name__ = "Integer32"
_CLApPowerStatus_Object = MibTableColumn
cLApPowerStatus = _CLApPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 20),
    _CLApPowerStatus_Type()
)
cLApPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPowerStatus.setStatus("current")


class _CLApTelnetEnable_Type(TruthValue):
    """Custom type cLApTelnetEnable based on TruthValue"""
    defaultValue = 2


_CLApTelnetEnable_Type.__name__ = "TruthValue"
_CLApTelnetEnable_Object = MibTableColumn
cLApTelnetEnable = _CLApTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 21),
    _CLApTelnetEnable_Type()
)
cLApTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTelnetEnable.setStatus("current")


class _CLApSshEnable_Type(TruthValue):
    """Custom type cLApSshEnable based on TruthValue"""
    defaultValue = 2


_CLApSshEnable_Type.__name__ = "TruthValue"
_CLApSshEnable_Object = MibTableColumn
cLApSshEnable = _CLApSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 22),
    _CLApSshEnable_Type()
)
cLApSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSshEnable.setStatus("current")
_CLApPreStdStateEnabled_Type = TruthValue
_CLApPreStdStateEnabled_Object = MibTableColumn
cLApPreStdStateEnabled = _CLApPreStdStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 23),
    _CLApPreStdStateEnabled_Type()
)
cLApPreStdStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPreStdStateEnabled.setStatus("current")
_CLApPwrInjectorStateEnabled_Type = TruthValue
_CLApPwrInjectorStateEnabled_Object = MibTableColumn
cLApPwrInjectorStateEnabled = _CLApPwrInjectorStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 24),
    _CLApPwrInjectorStateEnabled_Type()
)
cLApPwrInjectorStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPwrInjectorStateEnabled.setStatus("current")


class _CLApPwrInjectorSelection_Type(Integer32):
    """Custom type cLApPwrInjectorSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("installed", 2),
          ("override", 3))
    )


_CLApPwrInjectorSelection_Type.__name__ = "Integer32"
_CLApPwrInjectorSelection_Object = MibTableColumn
cLApPwrInjectorSelection = _CLApPwrInjectorSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 25),
    _CLApPwrInjectorSelection_Type()
)
cLApPwrInjectorSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPwrInjectorSelection.setStatus("current")
_CLApPwrInjectorSwMacAddr_Type = MacAddress
_CLApPwrInjectorSwMacAddr_Object = MibTableColumn
cLApPwrInjectorSwMacAddr = _CLApPwrInjectorSwMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 26),
    _CLApPwrInjectorSwMacAddr_Type()
)
cLApPwrInjectorSwMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPwrInjectorSwMacAddr.setStatus("current")


class _CLApWipsEnable_Type(TruthValue):
    """Custom type cLApWipsEnable based on TruthValue"""
    defaultValue = 2


_CLApWipsEnable_Type.__name__ = "TruthValue"
_CLApWipsEnable_Object = MibTableColumn
cLApWipsEnable = _CLApWipsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 27),
    _CLApWipsEnable_Type()
)
cLApWipsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApWipsEnable.setStatus("deprecated")


class _CLApMonitorModeOptimization_Type(Integer32):
    """Custom type cLApMonitorModeOptimization based on Integer32"""
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
          ("tracking", 2),
          ("wips", 3),
          ("none", 4))
    )


_CLApMonitorModeOptimization_Type.__name__ = "Integer32"
_CLApMonitorModeOptimization_Object = MibTableColumn
cLApMonitorModeOptimization = _CLApMonitorModeOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 28),
    _CLApMonitorModeOptimization_Type()
)
cLApMonitorModeOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApMonitorModeOptimization.setStatus("current")
_CLApDomainName_Type = SnmpAdminString
_CLApDomainName_Object = MibTableColumn
cLApDomainName = _CLApDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 29),
    _CLApDomainName_Type()
)
cLApDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDomainName.setStatus("current")
_CLApNameServerAddressType_Type = InetAddressType
_CLApNameServerAddressType_Object = MibTableColumn
cLApNameServerAddressType = _CLApNameServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 30),
    _CLApNameServerAddressType_Type()
)
cLApNameServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNameServerAddressType.setStatus("current")
_CLApNameServerAddress_Type = InetAddress
_CLApNameServerAddress_Object = MibTableColumn
cLApNameServerAddress = _CLApNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 31),
    _CLApNameServerAddress_Type()
)
cLApNameServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNameServerAddress.setStatus("current")


class _CLApAMSDUEnable_Type(TruthValue):
    """Custom type cLApAMSDUEnable based on TruthValue"""
    defaultValue = 2


_CLApAMSDUEnable_Type.__name__ = "TruthValue"
_CLApAMSDUEnable_Object = MibTableColumn
cLApAMSDUEnable = _CLApAMSDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 32),
    _CLApAMSDUEnable_Type()
)
cLApAMSDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAMSDUEnable.setStatus("current")


class _CLApEncryptionSupported_Type(TruthValue):
    """Custom type cLApEncryptionSupported based on TruthValue"""
    defaultValue = 2


_CLApEncryptionSupported_Type.__name__ = "TruthValue"
_CLApEncryptionSupported_Object = MibTableColumn
cLApEncryptionSupported = _CLApEncryptionSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 33),
    _CLApEncryptionSupported_Type()
)
cLApEncryptionSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEncryptionSupported.setStatus("current")


class _CLApRogueDetectionEnabled_Type(TruthValue):
    """Custom type cLApRogueDetectionEnabled based on TruthValue"""
    defaultValue = 2


_CLApRogueDetectionEnabled_Type.__name__ = "TruthValue"
_CLApRogueDetectionEnabled_Object = MibTableColumn
cLApRogueDetectionEnabled = _CLApRogueDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 34),
    _CLApRogueDetectionEnabled_Type()
)
cLApRogueDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRogueDetectionEnabled.setStatus("current")


class _CLApTcpMss_Type(Integer32):
    """Custom type cLApTcpMss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(536, 1363),
    )


_CLApTcpMss_Type.__name__ = "Integer32"
_CLApTcpMss_Object = MibTableColumn
cLApTcpMss = _CLApTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 35),
    _CLApTcpMss_Type()
)
cLApTcpMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTcpMss.setStatus("current")


class _CLApDataEncryptionStatus_Type(TruthValue):
    """Custom type cLApDataEncryptionStatus based on TruthValue"""
    defaultValue = 2


_CLApDataEncryptionStatus_Type.__name__ = "TruthValue"
_CLApDataEncryptionStatus_Object = MibTableColumn
cLApDataEncryptionStatus = _CLApDataEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 36),
    _CLApDataEncryptionStatus_Type()
)
cLApDataEncryptionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataEncryptionStatus.setStatus("current")


class _CLApNsiKey_Type(SnmpAdminString):
    """Custom type cLApNsiKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApNsiKey_Type.__name__ = "SnmpAdminString"
_CLApNsiKey_Object = MibTableColumn
cLApNsiKey = _CLApNsiKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 37),
    _CLApNsiKey_Type()
)
cLApNsiKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApNsiKey.setStatus("current")


class _CLApAdminStatus_Type(TruthValue):
    """Custom type cLApAdminStatus based on TruthValue"""
    defaultValue = 2


_CLApAdminStatus_Type.__name__ = "TruthValue"
_CLApAdminStatus_Object = MibTableColumn
cLApAdminStatus = _CLApAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 38),
    _CLApAdminStatus_Type()
)
cLApAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAdminStatus.setStatus("current")
_CLApPortNumber_Type = InetPortNumber
_CLApPortNumber_Object = MibTableColumn
cLApPortNumber = _CLApPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 39),
    _CLApPortNumber_Type()
)
cLApPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPortNumber.setStatus("current")
_CLApRetransmitCount_Type = Unsigned32
_CLApRetransmitCount_Object = MibTableColumn
cLApRetransmitCount = _CLApRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 40),
    _CLApRetransmitCount_Type()
)
cLApRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRetransmitCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApRetransmitCount.setUnits("retries")
_CLApRetransmitTimeout_Type = Unsigned32
_CLApRetransmitTimeout_Object = MibTableColumn
cLApRetransmitTimeout = _CLApRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 41),
    _CLApRetransmitTimeout_Type()
)
cLApRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRetransmitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApRetransmitTimeout.setUnits("seconds")


class _CLApVenueConfigVenueGroup_Type(Integer32):
    """Custom type cLApVenueConfigVenueGroup based on Integer32"""
    defaultValue = 1

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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("assembly", 2),
          ("business", 3),
          ("educational", 4),
          ("factoryAndIndustrial", 5),
          ("institutional", 6),
          ("mercantile", 7),
          ("residential", 8),
          ("storage", 9),
          ("utilityAndMisc", 10),
          ("vehicular", 11),
          ("outdoor", 12))
    )


_CLApVenueConfigVenueGroup_Type.__name__ = "Integer32"
_CLApVenueConfigVenueGroup_Object = MibTableColumn
cLApVenueConfigVenueGroup = _CLApVenueConfigVenueGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 42),
    _CLApVenueConfigVenueGroup_Type()
)
cLApVenueConfigVenueGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVenueConfigVenueGroup.setStatus("current")


class _CLApVenueConfigVenueType_Type(Integer32):
    """Custom type cLApVenueConfigVenueType based on Integer32"""
    defaultValue = 1

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
              63,
              64,
              65,
              66)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("unspecifiedAssembly", 2),
          ("arena", 3),
          ("stadium", 4),
          ("passengerTerminal", 5),
          ("amphitheater", 6),
          ("amusementPark", 7),
          ("placeOfWorship", 8),
          ("conventionCenter", 9),
          ("library", 10),
          ("museum", 11),
          ("restaurant", 12),
          ("theater", 13),
          ("bar", 14),
          ("coffeeShop", 15),
          ("zooOrAquarium", 16),
          ("emergencyCoordinationCenter", 17),
          ("unspecifiedBusiness", 18),
          ("doctorOrDentistOffice", 19),
          ("bank", 20),
          ("fireStation", 21),
          ("policeStation", 22),
          ("postOffice", 23),
          ("professionalOffice", 24),
          ("researchAndDevelopmentFacility", 25),
          ("attorneyOffice", 26),
          ("unspecifiedEducational", 27),
          ("schoolPrimary", 28),
          ("schoolSecondary", 29),
          ("universityOrCollege", 30),
          ("unspecifiedFactoryAndIndustrial", 31),
          ("factory", 32),
          ("unspecifiedInstitutional", 33),
          ("hospital", 34),
          ("longTermCareFacility", 35),
          ("alcoholAndDrugRehabilitationCenter", 36),
          ("groupHome", 37),
          ("prisonOrJail", 38),
          ("unspecifiedMercantile", 39),
          ("retailStore", 40),
          ("groceryMarket", 41),
          ("atomotiveServiceStation", 42),
          ("shoppingMall", 43),
          ("gasStation", 44),
          ("unspecifiedResidential", 45),
          ("privateResidence", 46),
          ("hotelOrMotel", 47),
          ("dormitory", 48),
          ("boardingHouse", 49),
          ("unspecifiedStorage", 50),
          ("unspecifiedUtility", 51),
          ("unspecifiedVehicular", 52),
          ("automobileOrTruck", 53),
          ("airplane", 54),
          ("bus", 55),
          ("ferry", 56),
          ("shipOrBoat", 57),
          ("train", 58),
          ("motorBike", 59),
          ("unspecifiedOutdoor", 60),
          ("muniMeshNetwork", 61),
          ("cityPark", 62),
          ("restArea", 63),
          ("trafficControl", 64),
          ("busStop", 65),
          ("kiosk", 66))
    )


_CLApVenueConfigVenueType_Type.__name__ = "Integer32"
_CLApVenueConfigVenueType_Object = MibTableColumn
cLApVenueConfigVenueType = _CLApVenueConfigVenueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 43),
    _CLApVenueConfigVenueType_Type()
)
cLApVenueConfigVenueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVenueConfigVenueType.setStatus("current")
_CLApVenueConfigVenueName_Type = SnmpAdminString
_CLApVenueConfigVenueName_Object = MibTableColumn
cLApVenueConfigVenueName = _CLApVenueConfigVenueName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 44),
    _CLApVenueConfigVenueName_Type()
)
cLApVenueConfigVenueName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVenueConfigVenueName.setStatus("current")
_CLApVenueConfigLanguage_Type = SnmpAdminString
_CLApVenueConfigLanguage_Object = MibTableColumn
cLApVenueConfigLanguage = _CLApVenueConfigLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 45),
    _CLApVenueConfigLanguage_Type()
)
cLApVenueConfigLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVenueConfigLanguage.setStatus("current")
_CLApLEDState_Type = TruthValue
_CLApLEDState_Object = MibTableColumn
cLApLEDState = _CLApLEDState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 46),
    _CLApLEDState_Type()
)
cLApLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLEDState.setStatus("current")
_CLApTrunkVlan_Type = Unsigned32
_CLApTrunkVlan_Object = MibTableColumn
cLApTrunkVlan = _CLApTrunkVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 47),
    _CLApTrunkVlan_Type()
)
cLApTrunkVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApTrunkVlan.setStatus("current")
_CLApTrunkVlanStatus_Type = TruthValue
_CLApTrunkVlanStatus_Object = MibTableColumn
cLApTrunkVlanStatus = _CLApTrunkVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 48),
    _CLApTrunkVlanStatus_Type()
)
cLApTrunkVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApTrunkVlanStatus.setStatus("current")
_CLApLocation_Type = SnmpAdminString
_CLApLocation_Object = MibTableColumn
cLApLocation = _CLApLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 49),
    _CLApLocation_Type()
)
cLApLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLocation.setStatus("current")


class _CLApSubMode_Type(Integer32):
    """Custom type cLApSubMode based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("wips", 2),
          ("pppoe", 3),
          ("pppoeWips", 4))
    )


_CLApSubMode_Type.__name__ = "Integer32"
_CLApSubMode_Object = MibTableColumn
cLApSubMode = _CLApSubMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 50),
    _CLApSubMode_Type()
)
cLApSubMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSubMode.setStatus("current")
_CLApAssocCount_Type = Unsigned32
_CLApAssocCount_Object = MibTableColumn
cLApAssocCount = _CLApAssocCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 51),
    _CLApAssocCount_Type()
)
cLApAssocCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAssocCount.setStatus("current")
_CLApAssocFailResourceCount_Type = Unsigned32
_CLApAssocFailResourceCount_Object = MibTableColumn
cLApAssocFailResourceCount = _CLApAssocFailResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 52),
    _CLApAssocFailResourceCount_Type()
)
cLApAssocFailResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAssocFailResourceCount.setStatus("current")


class _CLApRealTimeStatsModeEnabled_Type(TruthValue):
    """Custom type cLApRealTimeStatsModeEnabled based on TruthValue"""
    defaultValue = 2


_CLApRealTimeStatsModeEnabled_Type.__name__ = "TruthValue"
_CLApRealTimeStatsModeEnabled_Object = MibTableColumn
cLApRealTimeStatsModeEnabled = _CLApRealTimeStatsModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 53),
    _CLApRealTimeStatsModeEnabled_Type()
)
cLApRealTimeStatsModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRealTimeStatsModeEnabled.setStatus("current")
_CLApAssociatedClientCount_Type = Unsigned32
_CLApAssociatedClientCount_Object = MibTableColumn
cLApAssociatedClientCount = _CLApAssociatedClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 54),
    _CLApAssociatedClientCount_Type()
)
cLApAssociatedClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAssociatedClientCount.setStatus("current")
_CLApMemoryCurrentUsage_Type = Unsigned32
_CLApMemoryCurrentUsage_Object = MibTableColumn
cLApMemoryCurrentUsage = _CLApMemoryCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 55),
    _CLApMemoryCurrentUsage_Type()
)
cLApMemoryCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMemoryCurrentUsage.setStatus("current")
_CLApMemoryAverageUsage_Type = Unsigned32
_CLApMemoryAverageUsage_Object = MibTableColumn
cLApMemoryAverageUsage = _CLApMemoryAverageUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 56),
    _CLApMemoryAverageUsage_Type()
)
cLApMemoryAverageUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMemoryAverageUsage.setStatus("current")
_CLApCpuCurrentUsage_Type = Unsigned32
_CLApCpuCurrentUsage_Object = MibTableColumn
cLApCpuCurrentUsage = _CLApCpuCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 57),
    _CLApCpuCurrentUsage_Type()
)
cLApCpuCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCpuCurrentUsage.setStatus("current")
_CLApCpuAverageUsage_Type = Unsigned32
_CLApCpuAverageUsage_Object = MibTableColumn
cLApCpuAverageUsage = _CLApCpuAverageUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 58),
    _CLApCpuAverageUsage_Type()
)
cLApCpuAverageUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCpuAverageUsage.setStatus("current")
_CLApUpgradeFromVersion_Type = SnmpAdminString
_CLApUpgradeFromVersion_Object = MibTableColumn
cLApUpgradeFromVersion = _CLApUpgradeFromVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 59),
    _CLApUpgradeFromVersion_Type()
)
cLApUpgradeFromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUpgradeFromVersion.setStatus("current")
_CLApUpgradeToVersion_Type = SnmpAdminString
_CLApUpgradeToVersion_Object = MibTableColumn
cLApUpgradeToVersion = _CLApUpgradeToVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 60),
    _CLApUpgradeToVersion_Type()
)
cLApUpgradeToVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUpgradeToVersion.setStatus("current")
_CLApUpgradeFailureCause_Type = SnmpAdminString
_CLApUpgradeFailureCause_Object = MibTableColumn
cLApUpgradeFailureCause = _CLApUpgradeFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 61),
    _CLApUpgradeFailureCause_Type()
)
cLApUpgradeFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUpgradeFailureCause.setStatus("current")
_CLApMaxClientLimitNumberTrap_Type = Unsigned32
_CLApMaxClientLimitNumberTrap_Object = MibTableColumn
cLApMaxClientLimitNumberTrap = _CLApMaxClientLimitNumberTrap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 62),
    _CLApMaxClientLimitNumberTrap_Type()
)
cLApMaxClientLimitNumberTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxClientLimitNumberTrap.setStatus("current")
_CLApMaxClientLimitCause_Type = SnmpAdminString
_CLApMaxClientLimitCause_Object = MibTableColumn
cLApMaxClientLimitCause = _CLApMaxClientLimitCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 63),
    _CLApMaxClientLimitCause_Type()
)
cLApMaxClientLimitCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxClientLimitCause.setStatus("current")
_CLApMaxClientLimitSet_Type = TruthValue
_CLApMaxClientLimitSet_Object = MibTableColumn
cLApMaxClientLimitSet = _CLApMaxClientLimitSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 64),
    _CLApMaxClientLimitSet_Type()
)
cLApMaxClientLimitSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMaxClientLimitSet.setStatus("current")
_CLApFloorLabel_Type = Unsigned64
_CLApFloorLabel_Object = MibTableColumn
cLApFloorLabel = _CLApFloorLabel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 65),
    _CLApFloorLabel_Type()
)
cLApFloorLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFloorLabel.setStatus("current")
_CLApConnectCount_Type = Unsigned32
_CLApConnectCount_Object = MibTableColumn
cLApConnectCount = _CLApConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 66),
    _CLApConnectCount_Type()
)
cLApConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApConnectCount.setStatus("deprecated")
_CLApReassocSuccCount_Type = Counter32
_CLApReassocSuccCount_Object = MibTableColumn
cLApReassocSuccCount = _CLApReassocSuccCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 67),
    _CLApReassocSuccCount_Type()
)
cLApReassocSuccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApReassocSuccCount.setStatus("current")
_CLApReassocFailCount_Type = Counter32
_CLApReassocFailCount_Object = MibTableColumn
cLApReassocFailCount = _CLApReassocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 68),
    _CLApReassocFailCount_Type()
)
cLApReassocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApReassocFailCount.setStatus("current")
_CLAdjChannelRogueEnabled_Type = TruthValue
_CLAdjChannelRogueEnabled_Object = MibTableColumn
cLAdjChannelRogueEnabled = _CLAdjChannelRogueEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 69),
    _CLAdjChannelRogueEnabled_Type()
)
cLAdjChannelRogueEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAdjChannelRogueEnabled.setStatus("deprecated")
_CLApAssocFailCountByRate_Type = Unsigned32
_CLApAssocFailCountByRate_Object = MibTableColumn
cLApAssocFailCountByRate = _CLApAssocFailCountByRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 70),
    _CLApAssocFailCountByRate_Type()
)
cLApAssocFailCountByRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAssocFailCountByRate.setStatus("current")
_CLApAbnormalOfflineCount_Type = Unsigned32
_CLApAbnormalOfflineCount_Object = MibTableColumn
cLApAbnormalOfflineCount = _CLApAbnormalOfflineCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 71),
    _CLApAbnormalOfflineCount_Type()
)
cLApAbnormalOfflineCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAbnormalOfflineCount.setStatus("current")
_CLApActiveClientCount_Type = Unsigned32
_CLApActiveClientCount_Object = MibTableColumn
cLApActiveClientCount = _CLApActiveClientCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 72),
    _CLApActiveClientCount_Type()
)
cLApActiveClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApActiveClientCount.setStatus("current")
_CLApAssocFailCountForRssiLow_Type = Unsigned32
_CLApAssocFailCountForRssiLow_Object = MibTableColumn
cLApAssocFailCountForRssiLow = _CLApAssocFailCountForRssiLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 73),
    _CLApAssocFailCountForRssiLow_Type()
)
cLApAssocFailCountForRssiLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAssocFailCountForRssiLow.setStatus("current")
_CLApSysNetId_Type = SnmpAdminString
_CLApSysNetId_Object = MibTableColumn
cLApSysNetId = _CLApSysNetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 74),
    _CLApSysNetId_Type()
)
cLApSysNetId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSysNetId.setStatus("current")
_CLApAssocFailTimes_Type = Counter32
_CLApAssocFailTimes_Object = MibTableColumn
cLApAssocFailTimes = _CLApAssocFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 75),
    _CLApAssocFailTimes_Type()
)
cLApAssocFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApAssocFailTimes.setStatus("current")


class _CLApAntennaBandMode_Type(Integer32):
    """Custom type cLApAntennaBandMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("single", 2),
          ("dual", 3))
    )


_CLApAntennaBandMode_Type.__name__ = "Integer32"
_CLApAntennaBandMode_Object = MibTableColumn
cLApAntennaBandMode = _CLApAntennaBandMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 76),
    _CLApAntennaBandMode_Type()
)
cLApAntennaBandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAntennaBandMode.setStatus("current")


class _CLApHeartBeatRspAvgTime_Type(Integer32):
    """Custom type cLApHeartBeatRspAvgTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_CLApHeartBeatRspAvgTime_Type.__name__ = "Integer32"
_CLApHeartBeatRspAvgTime_Object = MibTableColumn
cLApHeartBeatRspAvgTime = _CLApHeartBeatRspAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 77),
    _CLApHeartBeatRspAvgTime_Type()
)
cLApHeartBeatRspAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApHeartBeatRspAvgTime.setStatus("current")
if mibBuilder.loadTexts:
    cLApHeartBeatRspAvgTime.setUnits("milliseconds")
_CLApEchoRequestCount_Type = Counter32
_CLApEchoRequestCount_Object = MibTableColumn
cLApEchoRequestCount = _CLApEchoRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 78),
    _CLApEchoRequestCount_Type()
)
cLApEchoRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEchoRequestCount.setStatus("current")
_CLApEchoResponseLossCount_Type = Counter32
_CLApEchoResponseLossCount_Object = MibTableColumn
cLApEchoResponseLossCount = _CLApEchoResponseLossCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 79),
    _CLApEchoResponseLossCount_Type()
)
cLApEchoResponseLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEchoResponseLossCount.setStatus("current")
_CLApModuleInserted_Type = SnmpAdminString
_CLApModuleInserted_Object = MibTableColumn
cLApModuleInserted = _CLApModuleInserted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 80),
    _CLApModuleInserted_Type()
)
cLApModuleInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApModuleInserted.setStatus("current")
_CLApEnableModule_Type = TruthValue
_CLApEnableModule_Object = MibTableColumn
cLApEnableModule = _CLApEnableModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 81),
    _CLApEnableModule_Type()
)
cLApEnableModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEnableModule.setStatus("current")
_CLApIsUniversal_Type = TruthValue
_CLApIsUniversal_Object = MibTableColumn
cLApIsUniversal = _CLApIsUniversal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 82),
    _CLApIsUniversal_Type()
)
cLApIsUniversal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApIsUniversal.setStatus("current")
_CLApUniversalPrimeStatus_Type = SnmpAdminString
_CLApUniversalPrimeStatus_Object = MibTableColumn
cLApUniversalPrimeStatus = _CLApUniversalPrimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 83),
    _CLApUniversalPrimeStatus_Type()
)
cLApUniversalPrimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUniversalPrimeStatus.setStatus("current")
_CLApIsMaster_Type = TruthValue
_CLApIsMaster_Object = MibTableColumn
cLApIsMaster = _CLApIsMaster_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 84),
    _CLApIsMaster_Type()
)
cLApIsMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApIsMaster.setStatus("current")
_CLApBleFWDownloadStatus_Type = TruthValue
_CLApBleFWDownloadStatus_Object = MibTableColumn
cLApBleFWDownloadStatus = _CLApBleFWDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 85),
    _CLApBleFWDownloadStatus_Type()
)
cLApBleFWDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApBleFWDownloadStatus.setStatus("current")
_CLApDot11XorDartConnectorStatus_Type = SnmpAdminString
_CLApDot11XorDartConnectorStatus_Object = MibTableColumn
cLApDot11XorDartConnectorStatus = _CLApDot11XorDartConnectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 86),
    _CLApDot11XorDartConnectorStatus_Type()
)
cLApDot11XorDartConnectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11XorDartConnectorStatus.setStatus("current")


class _CLApCtsSxpDefaultPassword_Type(SnmpAdminString):
    """Custom type cLApCtsSxpDefaultPassword based on SnmpAdminString"""
    defaultValue = OctetString("")


_CLApCtsSxpDefaultPassword_Type.__name__ = "SnmpAdminString"
_CLApCtsSxpDefaultPassword_Object = MibTableColumn
cLApCtsSxpDefaultPassword = _CLApCtsSxpDefaultPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 87),
    _CLApCtsSxpDefaultPassword_Type()
)
cLApCtsSxpDefaultPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpDefaultPassword.setStatus("current")


class _CLApCtsSxpState_Type(TruthValue):
    """Custom type cLApCtsSxpState based on TruthValue"""
    defaultValue = 2


_CLApCtsSxpState_Type.__name__ = "TruthValue"
_CLApCtsSxpState_Object = MibTableColumn
cLApCtsSxpState = _CLApCtsSxpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 88),
    _CLApCtsSxpState_Type()
)
cLApCtsSxpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpState.setStatus("current")


class _CLApCtsSxpMode_Type(TruthValue):
    """Custom type cLApCtsSxpMode based on TruthValue"""
    defaultValue = 2


_CLApCtsSxpMode_Type.__name__ = "TruthValue"
_CLApCtsSxpMode_Object = MibTableColumn
cLApCtsSxpMode = _CLApCtsSxpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 89),
    _CLApCtsSxpMode_Type()
)
cLApCtsSxpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpMode.setStatus("current")


class _CLApCtsSxpListenerMinHoldtime_Type(Unsigned32):
    """Custom type cLApCtsSxpListenerMinHoldtime based on Unsigned32"""
    defaultValue = 90


_CLApCtsSxpListenerMinHoldtime_Type.__name__ = "Unsigned32"
_CLApCtsSxpListenerMinHoldtime_Object = MibTableColumn
cLApCtsSxpListenerMinHoldtime = _CLApCtsSxpListenerMinHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 90),
    _CLApCtsSxpListenerMinHoldtime_Type()
)
cLApCtsSxpListenerMinHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpListenerMinHoldtime.setStatus("current")


class _CLApCtsSxpListenerMaxHoldtime_Type(Unsigned32):
    """Custom type cLApCtsSxpListenerMaxHoldtime based on Unsigned32"""
    defaultValue = 180


_CLApCtsSxpListenerMaxHoldtime_Type.__name__ = "Unsigned32"
_CLApCtsSxpListenerMaxHoldtime_Object = MibTableColumn
cLApCtsSxpListenerMaxHoldtime = _CLApCtsSxpListenerMaxHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 91),
    _CLApCtsSxpListenerMaxHoldtime_Type()
)
cLApCtsSxpListenerMaxHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpListenerMaxHoldtime.setStatus("current")


class _CLApCtsSxpReconcilePeriod_Type(Unsigned32):
    """Custom type cLApCtsSxpReconcilePeriod based on Unsigned32"""
    defaultValue = 120


_CLApCtsSxpReconcilePeriod_Type.__name__ = "Unsigned32"
_CLApCtsSxpReconcilePeriod_Object = MibTableColumn
cLApCtsSxpReconcilePeriod = _CLApCtsSxpReconcilePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 92),
    _CLApCtsSxpReconcilePeriod_Type()
)
cLApCtsSxpReconcilePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpReconcilePeriod.setStatus("current")


class _CLApCtsSxpRetryPeriod_Type(Unsigned32):
    """Custom type cLApCtsSxpRetryPeriod based on Unsigned32"""
    defaultValue = 120


_CLApCtsSxpRetryPeriod_Type.__name__ = "Unsigned32"
_CLApCtsSxpRetryPeriod_Object = MibTableColumn
cLApCtsSxpRetryPeriod = _CLApCtsSxpRetryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 93),
    _CLApCtsSxpRetryPeriod_Type()
)
cLApCtsSxpRetryPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpRetryPeriod.setStatus("current")


class _CLApCtsSxpSpeakerHoldTime_Type(Unsigned32):
    """Custom type cLApCtsSxpSpeakerHoldTime based on Unsigned32"""
    defaultValue = 120


_CLApCtsSxpSpeakerHoldTime_Type.__name__ = "Unsigned32"
_CLApCtsSxpSpeakerHoldTime_Object = MibTableColumn
cLApCtsSxpSpeakerHoldTime = _CLApCtsSxpSpeakerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 94),
    _CLApCtsSxpSpeakerHoldTime_Type()
)
cLApCtsSxpSpeakerHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpSpeakerHoldTime.setStatus("current")


class _CLApCtsSxpSpeakerKeepAlive_Type(Unsigned32):
    """Custom type cLApCtsSxpSpeakerKeepAlive based on Unsigned32"""
    defaultValue = 0


_CLApCtsSxpSpeakerKeepAlive_Type.__name__ = "Unsigned32"
_CLApCtsSxpSpeakerKeepAlive_Object = MibTableColumn
cLApCtsSxpSpeakerKeepAlive = _CLApCtsSxpSpeakerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 95),
    _CLApCtsSxpSpeakerKeepAlive_Type()
)
cLApCtsSxpSpeakerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSxpSpeakerKeepAlive.setStatus("current")


class _CLApCtsInlineTagStatus_Type(TruthValue):
    """Custom type cLApCtsInlineTagStatus based on TruthValue"""
    defaultValue = 2


_CLApCtsInlineTagStatus_Type.__name__ = "TruthValue"
_CLApCtsInlineTagStatus_Object = MibTableColumn
cLApCtsInlineTagStatus = _CLApCtsInlineTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 96),
    _CLApCtsInlineTagStatus_Type()
)
cLApCtsInlineTagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsInlineTagStatus.setStatus("current")


class _CLApCtsSgaclStatus_Type(TruthValue):
    """Custom type cLApCtsSgaclStatus based on TruthValue"""
    defaultValue = 2


_CLApCtsSgaclStatus_Type.__name__ = "TruthValue"
_CLApCtsSgaclStatus_Object = MibTableColumn
cLApCtsSgaclStatus = _CLApCtsSgaclStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 97),
    _CLApCtsSgaclStatus_Type()
)
cLApCtsSgaclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsSgaclStatus.setStatus("current")


class _CLApCtsOverrideStatus_Type(TruthValue):
    """Custom type cLApCtsOverrideStatus based on TruthValue"""
    defaultValue = 2


_CLApCtsOverrideStatus_Type.__name__ = "TruthValue"
_CLApCtsOverrideStatus_Object = MibTableColumn
cLApCtsOverrideStatus = _CLApCtsOverrideStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 98),
    _CLApCtsOverrideStatus_Type()
)
cLApCtsOverrideStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCtsOverrideStatus.setStatus("current")
_CLApModeClear_Type = TruthValue
_CLApModeClear_Object = MibTableColumn
cLApModeClear = _CLApModeClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 103),
    _CLApModeClear_Type()
)
cLApModeClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApModeClear.setStatus("current")


class _CLApSiteTagName_Type(SnmpAdminString):
    """Custom type cLApSiteTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApSiteTagName_Type.__name__ = "SnmpAdminString"
_CLApSiteTagName_Object = MibTableColumn
cLApSiteTagName = _CLApSiteTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 104),
    _CLApSiteTagName_Type()
)
cLApSiteTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSiteTagName.setStatus("current")


class _CLApRfTagName_Type(SnmpAdminString):
    """Custom type cLApRfTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApRfTagName_Type.__name__ = "SnmpAdminString"
_CLApRfTagName_Object = MibTableColumn
cLApRfTagName = _CLApRfTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 105),
    _CLApRfTagName_Type()
)
cLApRfTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApRfTagName.setStatus("current")


class _CLApPolicyTagName_Type(SnmpAdminString):
    """Custom type cLApPolicyTagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApPolicyTagName_Type.__name__ = "SnmpAdminString"
_CLApPolicyTagName_Object = MibTableColumn
cLApPolicyTagName = _CLApPolicyTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 106),
    _CLApPolicyTagName_Type()
)
cLApPolicyTagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPolicyTagName.setStatus("current")


class _CLApTagSource_Type(Integer32):
    """Custom type cLApTagSource based on Integer32"""
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
        *(("none", 1),
          ("static", 2),
          ("filterengine", 3),
          ("pnpserver", 4),
          ("default", 5),
          ("location", 6))
    )


_CLApTagSource_Type.__name__ = "Integer32"
_CLApTagSource_Object = MibTableColumn
cLApTagSource = _CLApTagSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 107),
    _CLApTagSource_Type()
)
cLApTagSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApTagSource.setStatus("current")


class _CLApUsbModuleName_Type(SnmpAdminString):
    """Custom type cLApUsbModuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_CLApUsbModuleName_Type.__name__ = "SnmpAdminString"
_CLApUsbModuleName_Object = MibTableColumn
cLApUsbModuleName = _CLApUsbModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 108),
    _CLApUsbModuleName_Type()
)
cLApUsbModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUsbModuleName.setStatus("current")


class _CLApUsbModuleState_Type(SnmpAdminString):
    """Custom type cLApUsbModuleState based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_CLApUsbModuleState_Type.__name__ = "SnmpAdminString"
_CLApUsbModuleState_Object = MibTableColumn
cLApUsbModuleState = _CLApUsbModuleState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 109),
    _CLApUsbModuleState_Type()
)
cLApUsbModuleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUsbModuleState.setStatus("current")


class _CLApUsbModuleProductId_Type(SnmpAdminString):
    """Custom type cLApUsbModuleProductId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_CLApUsbModuleProductId_Type.__name__ = "SnmpAdminString"
_CLApUsbModuleProductId_Object = MibTableColumn
cLApUsbModuleProductId = _CLApUsbModuleProductId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 110),
    _CLApUsbModuleProductId_Type()
)
cLApUsbModuleProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUsbModuleProductId.setStatus("current")


class _CLApUsbDescription_Type(SnmpAdminString):
    """Custom type cLApUsbDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_CLApUsbDescription_Type.__name__ = "SnmpAdminString"
_CLApUsbDescription_Object = MibTableColumn
cLApUsbDescription = _CLApUsbDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 111),
    _CLApUsbDescription_Type()
)
cLApUsbDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUsbDescription.setStatus("current")
_CLApUsbStateInfo_Type = TruthValue
_CLApUsbStateInfo_Object = MibTableColumn
cLApUsbStateInfo = _CLApUsbStateInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 112),
    _CLApUsbStateInfo_Type()
)
cLApUsbStateInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApUsbStateInfo.setStatus("current")
_CLApUsbOverride_Type = TruthValue
_CLApUsbOverride_Object = MibTableColumn
cLApUsbOverride = _CLApUsbOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 113),
    _CLApUsbOverride_Type()
)
cLApUsbOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApUsbOverride.setStatus("current")


class _CLApUsbSerialNumber_Type(SnmpAdminString):
    """Custom type cLApUsbSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_CLApUsbSerialNumber_Type.__name__ = "SnmpAdminString"
_CLApUsbSerialNumber_Object = MibTableColumn
cLApUsbSerialNumber = _CLApUsbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 114),
    _CLApUsbSerialNumber_Type()
)
cLApUsbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUsbSerialNumber.setStatus("current")
_CLApUsbMaxPower_Type = Unsigned32
_CLApUsbMaxPower_Object = MibTableColumn
cLApUsbMaxPower = _CLApUsbMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 115),
    _CLApUsbMaxPower_Type()
)
cLApUsbMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApUsbMaxPower.setStatus("current")
_CLApLagConfigStatus_Type = TruthValue
_CLApLagConfigStatus_Object = MibTableColumn
cLApLagConfigStatus = _CLApLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 116),
    _CLApLagConfigStatus_Type()
)
cLApLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLagConfigStatus.setStatus("current")
_CLApMonitorModeOptStatus_Type = TruthValue
_CLApMonitorModeOptStatus_Object = MibTableColumn
cLApMonitorModeOptStatus = _CLApMonitorModeOptStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 117),
    _CLApMonitorModeOptStatus_Type()
)
cLApMonitorModeOptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApMonitorModeOptStatus.setStatus("current")


class _CLApFilterName_Type(SnmpAdminString):
    """Custom type cLApFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApFilterName_Type.__name__ = "SnmpAdminString"
_CLApFilterName_Object = MibTableColumn
cLApFilterName = _CLApFilterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 1, 1, 118),
    _CLApFilterName_Type()
)
cLApFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApFilterName.setStatus("current")
_CLApIfSmtParamTable_Object = MibTable
cLApIfSmtParamTable = _CLApIfSmtParamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLApIfSmtParamTable.setStatus("current")
_CLApIfSmtParamEntry_Object = MibTableRow
cLApIfSmtParamEntry = _CLApIfSmtParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 2, 1)
)
cLApIfSmtParamEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApIfSmtParamEntry.setStatus("current")
_CLApIfSmtDot11Bssid_Type = MacAddress
_CLApIfSmtDot11Bssid_Object = MibTableColumn
cLApIfSmtDot11Bssid = _CLApIfSmtDot11Bssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 2, 1, 1),
    _CLApIfSmtDot11Bssid_Type()
)
cLApIfSmtDot11Bssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApIfSmtDot11Bssid.setStatus("current")
_CLApCountryTable_Object = MibTable
cLApCountryTable = _CLApCountryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cLApCountryTable.setStatus("current")
_CLApCountryEntry_Object = MibTableRow
cLApCountryEntry = _CLApCountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3, 1)
)
cLApCountryEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApCountryEntry.setStatus("current")


class _CLApCountryCode_Type(SnmpAdminString):
    """Custom type cLApCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLApCountryCode_Type.__name__ = "SnmpAdminString"
_CLApCountryCode_Object = MibTableColumn
cLApCountryCode = _CLApCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3, 1, 1),
    _CLApCountryCode_Type()
)
cLApCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCountryCode.setStatus("current")


class _CLApCountryAllowed_Type(SnmpAdminString):
    """Custom type cLApCountryAllowed based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLApCountryAllowed_Type.__name__ = "SnmpAdminString"
_CLApCountryAllowed_Object = MibTableColumn
cLApCountryAllowed = _CLApCountryAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 3, 1, 2),
    _CLApCountryAllowed_Type()
)
cLApCountryAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCountryAllowed.setStatus("current")


class _CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Type(TruthValue):
    """Custom type ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled based on TruthValue"""
    defaultValue = 1


_CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Type.__name__ = "TruthValue"
_CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Object = MibScalar
ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled = _CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 4),
    _CiscoLwappApIfRegulatoryDomainMismatchNotifEnabled_Type()
)
ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled.setStatus("current")


class _CiscoLwappApCrashEnabled_Type(TruthValue):
    """Custom type ciscoLwappApCrashEnabled based on TruthValue"""
    defaultValue = 1


_CiscoLwappApCrashEnabled_Type.__name__ = "TruthValue"
_CiscoLwappApCrashEnabled_Object = MibScalar
ciscoLwappApCrashEnabled = _CiscoLwappApCrashEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 5),
    _CiscoLwappApCrashEnabled_Type()
)
ciscoLwappApCrashEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApCrashEnabled.setStatus("current")


class _CiscoLwappApUnsupportedEnabled_Type(TruthValue):
    """Custom type ciscoLwappApUnsupportedEnabled based on TruthValue"""
    defaultValue = 1


_CiscoLwappApUnsupportedEnabled_Type.__name__ = "TruthValue"
_CiscoLwappApUnsupportedEnabled_Object = MibScalar
ciscoLwappApUnsupportedEnabled = _CiscoLwappApUnsupportedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 6),
    _CiscoLwappApUnsupportedEnabled_Type()
)
ciscoLwappApUnsupportedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApUnsupportedEnabled.setStatus("current")


class _CiscoLwappApAssociatedEnabled_Type(TruthValue):
    """Custom type ciscoLwappApAssociatedEnabled based on TruthValue"""
    defaultValue = 1


_CiscoLwappApAssociatedEnabled_Type.__name__ = "TruthValue"
_CiscoLwappApAssociatedEnabled_Object = MibScalar
ciscoLwappApAssociatedEnabled = _CiscoLwappApAssociatedEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 7),
    _CiscoLwappApAssociatedEnabled_Type()
)
ciscoLwappApAssociatedEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappApAssociatedEnabled.setStatus("current")
_CLApCrashInfoTable_Object = MibTable
cLApCrashInfoTable = _CLApCrashInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cLApCrashInfoTable.setStatus("current")
_CLApCrashInfoEntry_Object = MibTableRow
cLApCrashInfoEntry = _CLApCrashInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 8, 1)
)
cLApCrashInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApCrashInfoEntry.setStatus("current")


class _CLApCrashFileName_Type(SnmpAdminString):
    """Custom type cLApCrashFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 28),
    )


_CLApCrashFileName_Type.__name__ = "SnmpAdminString"
_CLApCrashFileName_Object = MibTableColumn
cLApCrashFileName = _CLApCrashFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 8, 1, 1),
    _CLApCrashFileName_Type()
)
cLApCrashFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCrashFileName.setStatus("current")
_CLApCrashFileSize_Type = Unsigned32
_CLApCrashFileSize_Object = MibTableColumn
cLApCrashFileSize = _CLApCrashFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 8, 1, 2),
    _CLApCrashFileSize_Type()
)
cLApCrashFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCrashFileSize.setStatus("current")
_CLApCrashFileTimeStamp_Type = DateAndTime
_CLApCrashFileTimeStamp_Object = MibTableColumn
cLApCrashFileTimeStamp = _CLApCrashFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 8, 1, 3),
    _CLApCrashFileTimeStamp_Type()
)
cLApCrashFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCrashFileTimeStamp.setStatus("current")
_CLApSysInfoTable_Object = MibTable
cLApSysInfoTable = _CLApSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cLApSysInfoTable.setStatus("current")
_CLApSysInfoEntry_Object = MibTableRow
cLApSysInfoEntry = _CLApSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9, 1)
)
cLApSysInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApSysInfoEntry.setStatus("current")
_CLApSysMemType_Type = SnmpAdminString
_CLApSysMemType_Object = MibTableColumn
cLApSysMemType = _CLApSysMemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9, 1, 1),
    _CLApSysMemType_Type()
)
cLApSysMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSysMemType.setStatus("current")
_CLApSysMemSize_Type = Unsigned32
_CLApSysMemSize_Object = MibTableColumn
cLApSysMemSize = _CLApSysMemSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9, 1, 2),
    _CLApSysMemSize_Type()
)
cLApSysMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSysMemSize.setStatus("current")
if mibBuilder.loadTexts:
    cLApSysMemSize.setUnits("KBytes")
_CLApSysFlashSize_Type = Unsigned32
_CLApSysFlashSize_Object = MibTableColumn
cLApSysFlashSize = _CLApSysFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9, 1, 3),
    _CLApSysFlashSize_Type()
)
cLApSysFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSysFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    cLApSysFlashSize.setUnits("KBytes")
_CLApSysCpuType_Type = SnmpAdminString
_CLApSysCpuType_Object = MibTableColumn
cLApSysCpuType = _CLApSysCpuType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9, 1, 4),
    _CLApSysCpuType_Type()
)
cLApSysCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSysCpuType.setStatus("current")
_CLApSysFlashType_Type = SnmpAdminString
_CLApSysFlashType_Object = MibTableColumn
cLApSysFlashType = _CLApSysFlashType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 9, 1, 5),
    _CLApSysFlashType_Type()
)
cLApSysFlashType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSysFlashType.setStatus("current")
_CLApExtTable_Object = MibTable
cLApExtTable = _CLApExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cLApExtTable.setStatus("current")
_CLApExtEntry_Object = MibTableRow
cLApExtEntry = _CLApExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1)
)
cLApExtEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApExtEntry.setStatus("current")
_CLApLEDFlashStatus_Type = TruthValue
_CLApLEDFlashStatus_Object = MibTableColumn
cLApLEDFlashStatus = _CLApLEDFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 1),
    _CLApLEDFlashStatus_Type()
)
cLApLEDFlashStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLEDFlashStatus.setStatus("current")
_CLApLEDFlashDuration_Type = Unsigned32
_CLApLEDFlashDuration_Object = MibTableColumn
cLApLEDFlashDuration = _CLApLEDFlashDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 2),
    _CLApLEDFlashDuration_Type()
)
cLApLEDFlashDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLEDFlashDuration.setStatus("current")
if mibBuilder.loadTexts:
    cLApLEDFlashDuration.setUnits("seconds")
_CLApInetAddressType_Type = InetAddressType
_CLApInetAddressType_Object = MibTableColumn
cLApInetAddressType = _CLApInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 3),
    _CLApInetAddressType_Type()
)
cLApInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApInetAddressType.setStatus("current")
_CLApInetAddress_Type = InetAddress
_CLApInetAddress_Object = MibTableColumn
cLApInetAddress = _CLApInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 4),
    _CLApInetAddress_Type()
)
cLApInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApInetAddress.setStatus("current")
_CLApStaticIpv6AddressEnabled_Type = TruthValue
_CLApStaticIpv6AddressEnabled_Object = MibTableColumn
cLApStaticIpv6AddressEnabled = _CLApStaticIpv6AddressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 5),
    _CLApStaticIpv6AddressEnabled_Type()
)
cLApStaticIpv6AddressEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpv6AddressEnabled.setStatus("current")
_CLApStaticIpv6InetAddressType_Type = InetAddressType
_CLApStaticIpv6InetAddressType_Object = MibTableColumn
cLApStaticIpv6InetAddressType = _CLApStaticIpv6InetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 6),
    _CLApStaticIpv6InetAddressType_Type()
)
cLApStaticIpv6InetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpv6InetAddressType.setStatus("current")
_CLApStaticIpv6InetAddress_Type = InetAddress
_CLApStaticIpv6InetAddress_Object = MibTableColumn
cLApStaticIpv6InetAddress = _CLApStaticIpv6InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 7),
    _CLApStaticIpv6InetAddress_Type()
)
cLApStaticIpv6InetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpv6InetAddress.setStatus("current")


class _CLApStaticIpv6PrefixLength_Type(Unsigned32):
    """Custom type cLApStaticIpv6PrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CLApStaticIpv6PrefixLength_Type.__name__ = "Unsigned32"
_CLApStaticIpv6PrefixLength_Object = MibTableColumn
cLApStaticIpv6PrefixLength = _CLApStaticIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 8),
    _CLApStaticIpv6PrefixLength_Type()
)
cLApStaticIpv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpv6PrefixLength.setStatus("current")
_CLApStaticIpv6GatewayInetAddressType_Type = InetAddressType
_CLApStaticIpv6GatewayInetAddressType_Object = MibTableColumn
cLApStaticIpv6GatewayInetAddressType = _CLApStaticIpv6GatewayInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 9),
    _CLApStaticIpv6GatewayInetAddressType_Type()
)
cLApStaticIpv6GatewayInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpv6GatewayInetAddressType.setStatus("current")
_CLApStaticIpv6GatewayInetAddress_Type = InetAddress
_CLApStaticIpv6GatewayInetAddress_Object = MibTableColumn
cLApStaticIpv6GatewayInetAddress = _CLApStaticIpv6GatewayInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 10),
    _CLApStaticIpv6GatewayInetAddress_Type()
)
cLApStaticIpv6GatewayInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpv6GatewayInetAddress.setStatus("current")
_CLApStaticIpNetmaskType_Type = InetAddressType
_CLApStaticIpNetmaskType_Object = MibTableColumn
cLApStaticIpNetmaskType = _CLApStaticIpNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 11),
    _CLApStaticIpNetmaskType_Type()
)
cLApStaticIpNetmaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpNetmaskType.setStatus("current")
_CLApStaticIpNetmask_Type = InetAddress
_CLApStaticIpNetmask_Object = MibTableColumn
cLApStaticIpNetmask = _CLApStaticIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 12),
    _CLApStaticIpNetmask_Type()
)
cLApStaticIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApStaticIpNetmask.setStatus("current")


class _CLApPreferMode_Type(Integer32):
    """Custom type cLApPreferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CLApPreferMode_Type.__name__ = "Integer32"
_CLApPreferMode_Object = MibTableColumn
cLApPreferMode = _CLApPreferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 13),
    _CLApPreferMode_Type()
)
cLApPreferMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPreferMode.setStatus("current")


class _CLApPreferModeApplied_Type(Integer32):
    """Custom type cLApPreferModeApplied based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apgroup", 1),
          ("global", 2))
    )


_CLApPreferModeApplied_Type.__name__ = "Integer32"
_CLApPreferModeApplied_Object = MibTableColumn
cLApPreferModeApplied = _CLApPreferModeApplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 14),
    _CLApPreferModeApplied_Type()
)
cLApPreferModeApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPreferModeApplied.setStatus("current")
_CLApIndoorMode_Type = TruthValue
_CLApIndoorMode_Object = MibTableColumn
cLApIndoorMode = _CLApIndoorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 10, 1, 17),
    _CLApIndoorMode_Type()
)
cLApIndoorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApIndoorMode.setStatus("current")
_CLApEnvInfoTable_Object = MibTable
cLApEnvInfoTable = _CLApEnvInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cLApEnvInfoTable.setStatus("current")
_CLApEnvInfoEntry_Object = MibTableRow
cLApEnvInfoEntry = _CLApEnvInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 11, 1)
)
cLApEnvInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApEnvInfoEntry.setStatus("current")
_CLApEnvTemperatureDegree_Type = SnmpAdminString
_CLApEnvTemperatureDegree_Object = MibTableColumn
cLApEnvTemperatureDegree = _CLApEnvTemperatureDegree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 11, 1, 1),
    _CLApEnvTemperatureDegree_Type()
)
cLApEnvTemperatureDegree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEnvTemperatureDegree.setStatus("current")


class _CLApEnvTemperatureState_Type(Integer32):
    """Custom type cLApEnvTemperatureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )


_CLApEnvTemperatureState_Type.__name__ = "Integer32"
_CLApEnvTemperatureState_Object = MibTableColumn
cLApEnvTemperatureState = _CLApEnvTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 11, 1, 2),
    _CLApEnvTemperatureState_Type()
)
cLApEnvTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEnvTemperatureState.setStatus("current")


class _CLApEnvOrientation_Type(Integer32):
    """Custom type cLApEnvOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vertical", 1),
          ("horizontal", 2))
    )


_CLApEnvOrientation_Type.__name__ = "Integer32"
_CLApEnvOrientation_Object = MibTableColumn
cLApEnvOrientation = _CLApEnvOrientation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 11, 1, 3),
    _CLApEnvOrientation_Type()
)
cLApEnvOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEnvOrientation.setStatus("current")


class _CLApEnvPoeOutStatus_Type(Integer32):
    """Custom type cLApEnvPoeOutStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("off", 3))
    )


_CLApEnvPoeOutStatus_Type.__name__ = "Integer32"
_CLApEnvPoeOutStatus_Object = MibTableColumn
cLApEnvPoeOutStatus = _CLApEnvPoeOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 11, 1, 4),
    _CLApEnvPoeOutStatus_Type()
)
cLApEnvPoeOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEnvPoeOutStatus.setStatus("current")
_CLApGpsInfoTable_Object = MibTable
cLApGpsInfoTable = _CLApGpsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cLApGpsInfoTable.setStatus("current")
_CLApGpsInfoEntry_Object = MibTableRow
cLApGpsInfoEntry = _CLApGpsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1)
)
cLApGpsInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApGpsInfoEntry.setStatus("current")
_CLApGpsLocationPresent_Type = TruthValue
_CLApGpsLocationPresent_Object = MibTableColumn
cLApGpsLocationPresent = _CLApGpsLocationPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1, 1),
    _CLApGpsLocationPresent_Type()
)
cLApGpsLocationPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGpsLocationPresent.setStatus("current")
_CLApGpsLocationValid_Type = TruthValue
_CLApGpsLocationValid_Object = MibTableColumn
cLApGpsLocationValid = _CLApGpsLocationValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1, 2),
    _CLApGpsLocationValid_Type()
)
cLApGpsLocationValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGpsLocationValid.setStatus("current")
_CLApGpsLatitude_Type = SnmpAdminString
_CLApGpsLatitude_Object = MibTableColumn
cLApGpsLatitude = _CLApGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1, 3),
    _CLApGpsLatitude_Type()
)
cLApGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGpsLatitude.setStatus("current")
_CLApGpsLongitude_Type = SnmpAdminString
_CLApGpsLongitude_Object = MibTableColumn
cLApGpsLongitude = _CLApGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1, 4),
    _CLApGpsLongitude_Type()
)
cLApGpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGpsLongitude.setStatus("current")
_CLApGpsAltitude_Type = SnmpAdminString
_CLApGpsAltitude_Object = MibTableColumn
cLApGpsAltitude = _CLApGpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1, 5),
    _CLApGpsAltitude_Type()
)
cLApGpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGpsAltitude.setStatus("current")
_CLApGpsCollectionTime_Type = TimeStamp
_CLApGpsCollectionTime_Object = MibTableColumn
cLApGpsCollectionTime = _CLApGpsCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 12, 1, 6),
    _CLApGpsCollectionTime_Type()
)
cLApGpsCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGpsCollectionTime.setStatus("current")


class _CiscoLwappXorRadioRoleChangeEnabled_Type(TruthValue):
    """Custom type ciscoLwappXorRadioRoleChangeEnabled based on TruthValue"""
    defaultValue = 1


_CiscoLwappXorRadioRoleChangeEnabled_Type.__name__ = "TruthValue"
_CiscoLwappXorRadioRoleChangeEnabled_Object = MibScalar
ciscoLwappXorRadioRoleChangeEnabled = _CiscoLwappXorRadioRoleChangeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 1, 13),
    _CiscoLwappXorRadioRoleChangeEnabled_Type()
)
ciscoLwappXorRadioRoleChangeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLwappXorRadioRoleChangeEnabled.setStatus("current")
_CiscoLwappApIf_ObjectIdentity = ObjectIdentity
ciscoLwappApIf = _CiscoLwappApIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2)
)
_CLApDot11IfTable_Object = MibTable
cLApDot11IfTable = _CLApDot11IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLApDot11IfTable.setStatus("current")
_CLApDot11IfEntry_Object = MibTableRow
cLApDot11IfEntry = _CLApDot11IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1)
)
cLApDot11IfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApDot11IfEntry.setStatus("current")
_CLApDot11IfSlotId_Type = Unsigned32
_CLApDot11IfSlotId_Object = MibTableColumn
cLApDot11IfSlotId = _CLApDot11IfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 1),
    _CLApDot11IfSlotId_Type()
)
cLApDot11IfSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApDot11IfSlotId.setStatus("current")
_CLApDot11IfType_Type = CLApIfType
_CLApDot11IfType_Object = MibTableColumn
cLApDot11IfType = _CLApDot11IfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 2),
    _CLApDot11IfType_Type()
)
cLApDot11IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfType.setStatus("current")


class _CLApDot11IfRegDomain_Type(SnmpAdminString):
    """Custom type cLApDot11IfRegDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLApDot11IfRegDomain_Type.__name__ = "SnmpAdminString"
_CLApDot11IfRegDomain_Object = MibTableColumn
cLApDot11IfRegDomain = _CLApDot11IfRegDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 3),
    _CLApDot11IfRegDomain_Type()
)
cLApDot11IfRegDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfRegDomain.setStatus("current")
_CLApDot11nSupport_Type = TruthValue
_CLApDot11nSupport_Object = MibTableColumn
cLApDot11nSupport = _CLApDot11nSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 4),
    _CLApDot11nSupport_Type()
)
cLApDot11nSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11nSupport.setStatus("current")


class _CLAp11nChannelBandwidth_Type(Integer32):
    """Custom type cLAp11nChannelBandwidth based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("forty", 4))
    )


_CLAp11nChannelBandwidth_Type.__name__ = "Integer32"
_CLAp11nChannelBandwidth_Object = MibTableColumn
cLAp11nChannelBandwidth = _CLAp11nChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 5),
    _CLAp11nChannelBandwidth_Type()
)
cLAp11nChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11nChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLAp11nChannelBandwidth.setUnits("mhz")


class _CLApLomEnabled_Type(TruthValue):
    """Custom type cLApLomEnabled based on TruthValue"""
    defaultValue = 2


_CLApLomEnabled_Type.__name__ = "TruthValue"
_CLApLomEnabled_Object = MibTableColumn
cLApLomEnabled = _CLApLomEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 6),
    _CLApLomEnabled_Type()
)
cLApLomEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomEnabled.setStatus("deprecated")
_CLApLomFirstChannel_Type = CLDot11Channel
_CLApLomFirstChannel_Object = MibTableColumn
cLApLomFirstChannel = _CLApLomFirstChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 7),
    _CLApLomFirstChannel_Type()
)
cLApLomFirstChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomFirstChannel.setStatus("current")
_CLApLomSecondChannel_Type = CLDot11Channel
_CLApLomSecondChannel_Object = MibTableColumn
cLApLomSecondChannel = _CLApLomSecondChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 8),
    _CLApLomSecondChannel_Type()
)
cLApLomSecondChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomSecondChannel.setStatus("current")
_CLApLomThirdChannel_Type = CLDot11Channel
_CLApLomThirdChannel_Object = MibTableColumn
cLApLomThirdChannel = _CLApLomThirdChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 9),
    _CLApLomThirdChannel_Type()
)
cLApLomThirdChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomThirdChannel.setStatus("current")
_CLApLomFourthChannel_Type = CLDot11Channel
_CLApLomFourthChannel_Object = MibTableColumn
cLApLomFourthChannel = _CLApLomFourthChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 10),
    _CLApLomFourthChannel_Type()
)
cLApLomFourthChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLomFourthChannel.setStatus("current")
_CLApExtensionChannel_Type = CLDot11Channel
_CLApExtensionChannel_Object = MibTableColumn
cLApExtensionChannel = _CLApExtensionChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 11),
    _CLApExtensionChannel_Type()
)
cLApExtensionChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApExtensionChannel.setStatus("deprecated")


class _CLApLegacyBeamForming_Type(Integer32):
    """Custom type cLApLegacyBeamForming based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notApplicable", 3))
    )


_CLApLegacyBeamForming_Type.__name__ = "Integer32"
_CLApLegacyBeamForming_Object = MibTableColumn
cLApLegacyBeamForming = _CLApLegacyBeamForming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 12),
    _CLApLegacyBeamForming_Type()
)
cLApLegacyBeamForming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLegacyBeamForming.setStatus("current")
_CLApCdpOverAirEnabled_Type = TruthValue
_CLApCdpOverAirEnabled_Object = MibTableColumn
cLApCdpOverAirEnabled = _CLApCdpOverAirEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 13),
    _CLApCdpOverAirEnabled_Type()
)
cLApCdpOverAirEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCdpOverAirEnabled.setStatus("current")
_CLApDot11IfAdminStatus_Type = TruthValue
_CLApDot11IfAdminStatus_Object = MibTableColumn
cLApDot11IfAdminStatus = _CLApDot11IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 14),
    _CLApDot11IfAdminStatus_Type()
)
cLApDot11IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAdminStatus.setStatus("current")
_CLApDot11IfLinkChangeCount_Type = Unsigned32
_CLApDot11IfLinkChangeCount_Object = MibTableColumn
cLApDot11IfLinkChangeCount = _CLApDot11IfLinkChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 15),
    _CLApDot11IfLinkChangeCount_Type()
)
cLApDot11IfLinkChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfLinkChangeCount.setStatus("current")


class _CLApDot11MaxClients_Type(Unsigned32):
    """Custom type cLApDot11MaxClients based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CLApDot11MaxClients_Type.__name__ = "Unsigned32"
_CLApDot11MaxClients_Object = MibTableColumn
cLApDot11MaxClients = _CLApDot11MaxClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 16),
    _CLApDot11MaxClients_Type()
)
cLApDot11MaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11MaxClients.setStatus("current")
_CLApPromiscuousModeDwelling_Type = Unsigned32
_CLApPromiscuousModeDwelling_Object = MibTableColumn
cLApPromiscuousModeDwelling = _CLApPromiscuousModeDwelling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 17),
    _CLApPromiscuousModeDwelling_Type()
)
cLApPromiscuousModeDwelling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPromiscuousModeDwelling.setStatus("current")
if mibBuilder.loadTexts:
    cLApPromiscuousModeDwelling.setUnits("percentage")
_CLApDot11IfStaKeepingTime_Type = TimeTicks
_CLApDot11IfStaKeepingTime_Object = MibTableColumn
cLApDot11IfStaKeepingTime = _CLApDot11IfStaKeepingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 18),
    _CLApDot11IfStaKeepingTime_Type()
)
cLApDot11IfStaKeepingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfStaKeepingTime.setStatus("current")
_CLApDot11IfLinkSpeed_Type = Gauge32
_CLApDot11IfLinkSpeed_Object = MibTableColumn
cLApDot11IfLinkSpeed = _CLApDot11IfLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 19),
    _CLApDot11IfLinkSpeed_Type()
)
cLApDot11IfLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfLinkSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11IfLinkSpeed.setUnits("bps")
_CLApDot11IfMtu_Type = Unsigned32
_CLApDot11IfMtu_Object = MibTableColumn
cLApDot11IfMtu = _CLApDot11IfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 20),
    _CLApDot11IfMtu_Type()
)
cLApDot11IfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfMtu.setStatus("current")
_CLApDot11IfDesc_Type = SnmpAdminString
_CLApDot11IfDesc_Object = MibTableColumn
cLApDot11IfDesc = _CLApDot11IfDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 21),
    _CLApDot11IfDesc_Type()
)
cLApDot11IfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfDesc.setStatus("current")
_CLApDot11acSupport_Type = TruthValue
_CLApDot11acSupport_Object = MibTableColumn
cLApDot11acSupport = _CLApDot11acSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 22),
    _CLApDot11acSupport_Type()
)
cLApDot11acSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11acSupport.setStatus("current")


class _CLAp11ChannelBandwidth_Type(Integer32):
    """Custom type cLAp11ChannelBandwidth based on Integer32"""
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
        *(("five", 1),
          ("ten", 2),
          ("twenty", 3),
          ("fourty", 4),
          ("eighty", 5),
          ("onesixty", 6),
          ("eightyeighty", 7))
    )


_CLAp11ChannelBandwidth_Type.__name__ = "Integer32"
_CLAp11ChannelBandwidth_Object = MibTableColumn
cLAp11ChannelBandwidth = _CLAp11ChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 23),
    _CLAp11ChannelBandwidth_Type()
)
cLAp11ChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11ChannelBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cLAp11ChannelBandwidth.setUnits("mhz")
_CLApExtensionChannels_Type = SnmpAdminString
_CLApExtensionChannels_Object = MibTableColumn
cLApExtensionChannels = _CLApExtensionChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 24),
    _CLApExtensionChannels_Type()
)
cLApExtensionChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApExtensionChannels.setStatus("current")
_CLAPDot11IfMinTxPowerStep_Type = Unsigned32
_CLAPDot11IfMinTxPowerStep_Object = MibTableColumn
cLAPDot11IfMinTxPowerStep = _CLAPDot11IfMinTxPowerStep_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 25),
    _CLAPDot11IfMinTxPowerStep_Type()
)
cLAPDot11IfMinTxPowerStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPDot11IfMinTxPowerStep.setStatus("current")
if mibBuilder.loadTexts:
    cLAPDot11IfMinTxPowerStep.setUnits("dbm")


class _CLApDot11XorRadioMode_Type(Integer32):
    """Custom type cLApDot11XorRadioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("servingClients", 1),
          ("monitor", 2),
          ("sensor", 3))
    )


_CLApDot11XorRadioMode_Type.__name__ = "Integer32"
_CLApDot11XorRadioMode_Object = MibTableColumn
cLApDot11XorRadioMode = _CLApDot11XorRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 26),
    _CLApDot11XorRadioMode_Type()
)
cLApDot11XorRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11XorRadioMode.setStatus("current")


class _CLApDot11XorRadioBand_Type(Integer32):
    """Custom type cLApDot11XorRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radioband24G", 1),
          ("radioband5G", 2),
          ("radioband6G", 3))
    )


_CLApDot11XorRadioBand_Type.__name__ = "Integer32"
_CLApDot11XorRadioBand_Object = MibTableColumn
cLApDot11XorRadioBand = _CLApDot11XorRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 27),
    _CLApDot11XorRadioBand_Type()
)
cLApDot11XorRadioBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11XorRadioBand.setStatus("current")


class _CLApDot11XorRadioRoleAssignment_Type(Integer32):
    """Custom type cLApDot11XorRadioRoleAssignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_CLApDot11XorRadioRoleAssignment_Type.__name__ = "Integer32"
_CLApDot11XorRadioRoleAssignment_Object = MibTableColumn
cLApDot11XorRadioRoleAssignment = _CLApDot11XorRadioRoleAssignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 28),
    _CLApDot11XorRadioRoleAssignment_Type()
)
cLApDot11XorRadioRoleAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11XorRadioRoleAssignment.setStatus("current")
_CLApDot11IfMaxDataRate_Type = Unsigned32
_CLApDot11IfMaxDataRate_Object = MibTableColumn
cLApDot11IfMaxDataRate = _CLApDot11IfMaxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 29),
    _CLApDot11IfMaxDataRate_Type()
)
cLApDot11IfMaxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfMaxDataRate.setStatus("current")
_CLApDot11IfSensorReachability_Type = Unsigned32
_CLApDot11IfSensorReachability_Object = MibTableColumn
cLApDot11IfSensorReachability = _CLApDot11IfSensorReachability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 30),
    _CLApDot11IfSensorReachability_Type()
)
cLApDot11IfSensorReachability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfSensorReachability.setStatus("current")
_CLApDot11axSupport_Type = TruthValue
_CLApDot11axSupport_Object = MibTableColumn
cLApDot11axSupport = _CLApDot11axSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 31),
    _CLApDot11axSupport_Type()
)
cLApDot11axSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11axSupport.setStatus("current")
_CLApFraCoverageOverlapFactor_Type = Integer32
_CLApFraCoverageOverlapFactor_Object = MibTableColumn
cLApFraCoverageOverlapFactor = _CLApFraCoverageOverlapFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 32),
    _CLApFraCoverageOverlapFactor_Type()
)
cLApFraCoverageOverlapFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApFraCoverageOverlapFactor.setStatus("current")
if mibBuilder.loadTexts:
    cLApFraCoverageOverlapFactor.setUnits("percentage")


class _CLApFraSuggestedMode_Type(Integer32):
    """Custom type cLApFraSuggestedMode based on Integer32"""
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
        *(("static", 1),
          ("none", 2),
          ("radioBand5GMonitor", 3),
          ("radioBand24G", 4),
          ("notApplicable", 5))
    )


_CLApFraSuggestedMode_Type.__name__ = "Integer32"
_CLApFraSuggestedMode_Object = MibTableColumn
cLApFraSuggestedMode = _CLApFraSuggestedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 33),
    _CLApFraSuggestedMode_Type()
)
cLApFraSuggestedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApFraSuggestedMode.setStatus("current")


class _CLApDot11IfDualRadioMode_Type(Integer32):
    """Custom type cLApDot11IfDualRadioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_CLApDot11IfDualRadioMode_Type.__name__ = "Integer32"
_CLApDot11IfDualRadioMode_Object = MibTableColumn
cLApDot11IfDualRadioMode = _CLApDot11IfDualRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 34),
    _CLApDot11IfDualRadioMode_Type()
)
cLApDot11IfDualRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfDualRadioMode.setStatus("deprecated")


class _CLApDot11IfDualRadioCapable_Type(Integer32):
    """Custom type cLApDot11IfDualRadioCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notcapable", 0),
          ("dualmodecapable", 1))
    )


_CLApDot11IfDualRadioCapable_Type.__name__ = "Integer32"
_CLApDot11IfDualRadioCapable_Object = MibTableColumn
cLApDot11IfDualRadioCapable = _CLApDot11IfDualRadioCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 35),
    _CLApDot11IfDualRadioCapable_Type()
)
cLApDot11IfDualRadioCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfDualRadioCapable.setStatus("deprecated")


class _CLApDot11IfRadioFRACapable_Type(Integer32):
    """Custom type cLApDot11IfRadioFRACapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notcapable", 0),
          ("capable", 1))
    )


_CLApDot11IfRadioFRACapable_Type.__name__ = "Integer32"
_CLApDot11IfRadioFRACapable_Object = MibTableColumn
cLApDot11IfRadioFRACapable = _CLApDot11IfRadioFRACapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 36),
    _CLApDot11IfRadioFRACapable_Type()
)
cLApDot11IfRadioFRACapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfRadioFRACapable.setStatus("deprecated")
_CLApDot11IfPhyS80EightyChannelNumber_Type = Integer32
_CLApDot11IfPhyS80EightyChannelNumber_Object = MibTableColumn
cLApDot11IfPhyS80EightyChannelNumber = _CLApDot11IfPhyS80EightyChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 37),
    _CLApDot11IfPhyS80EightyChannelNumber_Type()
)
cLApDot11IfPhyS80EightyChannelNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfPhyS80EightyChannelNumber.setStatus("current")


class _CLApDot11IfDualRadioOperation_Type(Integer32):
    """Custom type cLApDot11IfDualRadioOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto", 2),
          ("manual", 3))
    )


_CLApDot11IfDualRadioOperation_Type.__name__ = "Integer32"
_CLApDot11IfDualRadioOperation_Object = MibTableColumn
cLApDot11IfDualRadioOperation = _CLApDot11IfDualRadioOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 39),
    _CLApDot11IfDualRadioOperation_Type()
)
cLApDot11IfDualRadioOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfDualRadioOperation.setStatus("deprecated")


class _CLApDot11IfRadioRoleOperation_Type(Integer32):
    """Custom type cLApDot11IfRadioRoleOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto", 2),
          ("manual", 3))
    )


_CLApDot11IfRadioRoleOperation_Type.__name__ = "Integer32"
_CLApDot11IfRadioRoleOperation_Object = MibTableColumn
cLApDot11IfRadioRoleOperation = _CLApDot11IfRadioRoleOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 40),
    _CLApDot11IfRadioRoleOperation_Type()
)
cLApDot11IfRadioRoleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfRadioRoleOperation.setStatus("deprecated")


class _CLApDot11IfRadioRole_Type(Integer32):
    """Custom type cLApDot11IfRadioRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("local", 2),
          ("monitor", 3))
    )


_CLApDot11IfRadioRole_Type.__name__ = "Integer32"
_CLApDot11IfRadioRole_Object = MibTableColumn
cLApDot11IfRadioRole = _CLApDot11IfRadioRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 41),
    _CLApDot11IfRadioRole_Type()
)
cLApDot11IfRadioRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfRadioRole.setStatus("deprecated")
_CLApDot11IfRptncPresent_Type = TruthValue
_CLApDot11IfRptncPresent_Object = MibTableColumn
cLApDot11IfRptncPresent = _CLApDot11IfRptncPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 42),
    _CLApDot11IfRptncPresent_Type()
)
cLApDot11IfRptncPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfRptncPresent.setStatus("current")
_CLApDot11IfDartPresent_Type = TruthValue
_CLApDot11IfDartPresent_Object = MibTableColumn
cLApDot11IfDartPresent = _CLApDot11IfDartPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 1, 1, 43),
    _CLApDot11IfDartPresent_Type()
)
cLApDot11IfDartPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IfDartPresent.setStatus("current")
_CLApEthernetIfTable_Object = MibTable
cLApEthernetIfTable = _CLApEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cLApEthernetIfTable.setStatus("current")
_CLApEthernetIfEntry_Object = MibTableRow
cLApEthernetIfEntry = _CLApEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1)
)
cLApEthernetIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
)
if mibBuilder.loadTexts:
    cLApEthernetIfEntry.setStatus("current")
_CLApEthernetIfSlotId_Type = Unsigned32
_CLApEthernetIfSlotId_Object = MibTableColumn
cLApEthernetIfSlotId = _CLApEthernetIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 1),
    _CLApEthernetIfSlotId_Type()
)
cLApEthernetIfSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApEthernetIfSlotId.setStatus("current")


class _CLApEthernetIfName_Type(SnmpAdminString):
    """Custom type cLApEthernetIfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApEthernetIfName_Type.__name__ = "SnmpAdminString"
_CLApEthernetIfName_Object = MibTableColumn
cLApEthernetIfName = _CLApEthernetIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 2),
    _CLApEthernetIfName_Type()
)
cLApEthernetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfName.setStatus("current")
_CLApEthernetIfMacAddress_Type = MacAddress
_CLApEthernetIfMacAddress_Object = MibTableColumn
cLApEthernetIfMacAddress = _CLApEthernetIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 3),
    _CLApEthernetIfMacAddress_Type()
)
cLApEthernetIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfMacAddress.setStatus("current")


class _CLApEthernetIfAdminStatus_Type(Integer32):
    """Custom type cLApEthernetIfAdminStatus based on Integer32"""
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


_CLApEthernetIfAdminStatus_Type.__name__ = "Integer32"
_CLApEthernetIfAdminStatus_Object = MibTableColumn
cLApEthernetIfAdminStatus = _CLApEthernetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 4),
    _CLApEthernetIfAdminStatus_Type()
)
cLApEthernetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEthernetIfAdminStatus.setStatus("current")


class _CLApEthernetIfOperStatus_Type(Integer32):
    """Custom type cLApEthernetIfOperStatus based on Integer32"""
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


_CLApEthernetIfOperStatus_Type.__name__ = "Integer32"
_CLApEthernetIfOperStatus_Object = MibTableColumn
cLApEthernetIfOperStatus = _CLApEthernetIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 5),
    _CLApEthernetIfOperStatus_Type()
)
cLApEthernetIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOperStatus.setStatus("current")
_CLApEthernetIfRxUcastPkts_Type = Counter32
_CLApEthernetIfRxUcastPkts_Object = MibTableColumn
cLApEthernetIfRxUcastPkts = _CLApEthernetIfRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 6),
    _CLApEthernetIfRxUcastPkts_Type()
)
cLApEthernetIfRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRxUcastPkts.setUnits("packets")
_CLApEthernetIfRxNUcastPkts_Type = Counter32
_CLApEthernetIfRxNUcastPkts_Object = MibTableColumn
cLApEthernetIfRxNUcastPkts = _CLApEthernetIfRxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 7),
    _CLApEthernetIfRxNUcastPkts_Type()
)
cLApEthernetIfRxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRxNUcastPkts.setUnits("packets")
_CLApEthernetIfTxUcastPkts_Type = Counter32
_CLApEthernetIfTxUcastPkts_Object = MibTableColumn
cLApEthernetIfTxUcastPkts = _CLApEthernetIfTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 8),
    _CLApEthernetIfTxUcastPkts_Type()
)
cLApEthernetIfTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfTxUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfTxUcastPkts.setUnits("packets")
_CLApEthernetIfTxNUcastPkts_Type = Counter32
_CLApEthernetIfTxNUcastPkts_Object = MibTableColumn
cLApEthernetIfTxNUcastPkts = _CLApEthernetIfTxNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 9),
    _CLApEthernetIfTxNUcastPkts_Type()
)
cLApEthernetIfTxNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfTxNUcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfTxNUcastPkts.setUnits("packets")


class _CLApEthernetIfDuplex_Type(Integer32):
    """Custom type cLApEthernetIfDuplex based on Integer32"""
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
        *(("unknown", 1),
          ("halfduplex", 2),
          ("fullduplex", 3),
          ("auto", 4))
    )


_CLApEthernetIfDuplex_Type.__name__ = "Integer32"
_CLApEthernetIfDuplex_Object = MibTableColumn
cLApEthernetIfDuplex = _CLApEthernetIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 10),
    _CLApEthernetIfDuplex_Type()
)
cLApEthernetIfDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfDuplex.setStatus("current")
_CLApEthernetIfLinkSpeed_Type = Gauge32
_CLApEthernetIfLinkSpeed_Object = MibTableColumn
cLApEthernetIfLinkSpeed = _CLApEthernetIfLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 11),
    _CLApEthernetIfLinkSpeed_Type()
)
cLApEthernetIfLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfLinkSpeed.setStatus("current")


class _CLApEthernetIfPOEPower_Type(Integer32):
    """Custom type cLApEthernetIfPOEPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("drawn", 2),
          ("notdrawn", 3))
    )


_CLApEthernetIfPOEPower_Type.__name__ = "Integer32"
_CLApEthernetIfPOEPower_Object = MibTableColumn
cLApEthernetIfPOEPower = _CLApEthernetIfPOEPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 12),
    _CLApEthernetIfPOEPower_Type()
)
cLApEthernetIfPOEPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfPOEPower.setStatus("current")
_CLApEthernetIfRxTotalBytes_Type = Counter32
_CLApEthernetIfRxTotalBytes_Object = MibTableColumn
cLApEthernetIfRxTotalBytes = _CLApEthernetIfRxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 13),
    _CLApEthernetIfRxTotalBytes_Type()
)
cLApEthernetIfRxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRxTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRxTotalBytes.setUnits("Bytes")
_CLApEthernetIfTxTotalBytes_Type = Counter32
_CLApEthernetIfTxTotalBytes_Object = MibTableColumn
cLApEthernetIfTxTotalBytes = _CLApEthernetIfTxTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 14),
    _CLApEthernetIfTxTotalBytes_Type()
)
cLApEthernetIfTxTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfTxTotalBytes.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfTxTotalBytes.setUnits("Bytes")
_CLApEthernetIfInputCrc_Type = Counter32
_CLApEthernetIfInputCrc_Object = MibTableColumn
cLApEthernetIfInputCrc = _CLApEthernetIfInputCrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 15),
    _CLApEthernetIfInputCrc_Type()
)
cLApEthernetIfInputCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputCrc.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputCrc.setUnits("packets")
_CLApEthernetIfInputAborts_Type = Counter32
_CLApEthernetIfInputAborts_Object = MibTableColumn
cLApEthernetIfInputAborts = _CLApEthernetIfInputAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 16),
    _CLApEthernetIfInputAborts_Type()
)
cLApEthernetIfInputAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputAborts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputAborts.setUnits("packets")
_CLApEthernetIfInputErrors_Type = Counter32
_CLApEthernetIfInputErrors_Object = MibTableColumn
cLApEthernetIfInputErrors = _CLApEthernetIfInputErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 17),
    _CLApEthernetIfInputErrors_Type()
)
cLApEthernetIfInputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputErrors.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputErrors.setUnits("packets")
_CLApEthernetIfInputFrames_Type = Counter32
_CLApEthernetIfInputFrames_Object = MibTableColumn
cLApEthernetIfInputFrames = _CLApEthernetIfInputFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 18),
    _CLApEthernetIfInputFrames_Type()
)
cLApEthernetIfInputFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputFrames.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputFrames.setUnits("packets")
_CLApEthernetIfInputOverrun_Type = Counter32
_CLApEthernetIfInputOverrun_Object = MibTableColumn
cLApEthernetIfInputOverrun = _CLApEthernetIfInputOverrun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 19),
    _CLApEthernetIfInputOverrun_Type()
)
cLApEthernetIfInputOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputOverrun.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputOverrun.setUnits("packets")
_CLApEthernetIfInputDrops_Type = Counter32
_CLApEthernetIfInputDrops_Object = MibTableColumn
cLApEthernetIfInputDrops = _CLApEthernetIfInputDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 20),
    _CLApEthernetIfInputDrops_Type()
)
cLApEthernetIfInputDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputDrops.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputDrops.setUnits("packets")
_CLApEthernetIfInputResource_Type = Counter32
_CLApEthernetIfInputResource_Object = MibTableColumn
cLApEthernetIfInputResource = _CLApEthernetIfInputResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 21),
    _CLApEthernetIfInputResource_Type()
)
cLApEthernetIfInputResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfInputResource.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfInputResource.setUnits("packets")
_CLApEthernetIfUnknownProtocol_Type = Counter32
_CLApEthernetIfUnknownProtocol_Object = MibTableColumn
cLApEthernetIfUnknownProtocol = _CLApEthernetIfUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 22),
    _CLApEthernetIfUnknownProtocol_Type()
)
cLApEthernetIfUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfUnknownProtocol.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfUnknownProtocol.setUnits("packets")
_CLApEthernetIfRunts_Type = Counter32
_CLApEthernetIfRunts_Object = MibTableColumn
cLApEthernetIfRunts = _CLApEthernetIfRunts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 23),
    _CLApEthernetIfRunts_Type()
)
cLApEthernetIfRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfRunts.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfRunts.setUnits("packets")
_CLApEthernetIfGiants_Type = Counter32
_CLApEthernetIfGiants_Object = MibTableColumn
cLApEthernetIfGiants = _CLApEthernetIfGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 24),
    _CLApEthernetIfGiants_Type()
)
cLApEthernetIfGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfGiants.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfGiants.setUnits("packets")
_CLApEthernetIfThrottle_Type = Counter32
_CLApEthernetIfThrottle_Object = MibTableColumn
cLApEthernetIfThrottle = _CLApEthernetIfThrottle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 25),
    _CLApEthernetIfThrottle_Type()
)
cLApEthernetIfThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfThrottle.setStatus("current")
_CLApEthernetIfResets_Type = Counter32
_CLApEthernetIfResets_Object = MibTableColumn
cLApEthernetIfResets = _CLApEthernetIfResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 26),
    _CLApEthernetIfResets_Type()
)
cLApEthernetIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfResets.setStatus("current")
_CLApEthernetIfOutputCollision_Type = Counter32
_CLApEthernetIfOutputCollision_Object = MibTableColumn
cLApEthernetIfOutputCollision = _CLApEthernetIfOutputCollision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 27),
    _CLApEthernetIfOutputCollision_Type()
)
cLApEthernetIfOutputCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputCollision.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputCollision.setUnits("packets")
_CLApEthernetIfOutputNoBuffer_Type = Counter32
_CLApEthernetIfOutputNoBuffer_Object = MibTableColumn
cLApEthernetIfOutputNoBuffer = _CLApEthernetIfOutputNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 28),
    _CLApEthernetIfOutputNoBuffer_Type()
)
cLApEthernetIfOutputNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputNoBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputNoBuffer.setUnits("packets")
_CLApEthernetIfOutputResource_Type = Counter32
_CLApEthernetIfOutputResource_Object = MibTableColumn
cLApEthernetIfOutputResource = _CLApEthernetIfOutputResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 29),
    _CLApEthernetIfOutputResource_Type()
)
cLApEthernetIfOutputResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputResource.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputResource.setUnits("packets")
_CLApEthernetIfOutputUnderrun_Type = Counter32
_CLApEthernetIfOutputUnderrun_Object = MibTableColumn
cLApEthernetIfOutputUnderrun = _CLApEthernetIfOutputUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 30),
    _CLApEthernetIfOutputUnderrun_Type()
)
cLApEthernetIfOutputUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputUnderrun.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputUnderrun.setUnits("packets")
_CLApEthernetIfOutputErrors_Type = Counter32
_CLApEthernetIfOutputErrors_Object = MibTableColumn
cLApEthernetIfOutputErrors = _CLApEthernetIfOutputErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 31),
    _CLApEthernetIfOutputErrors_Type()
)
cLApEthernetIfOutputErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputErrors.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputErrors.setUnits("packets")
_CLApEthernetIfOutputTotalDrops_Type = Counter32
_CLApEthernetIfOutputTotalDrops_Object = MibTableColumn
cLApEthernetIfOutputTotalDrops = _CLApEthernetIfOutputTotalDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 32),
    _CLApEthernetIfOutputTotalDrops_Type()
)
cLApEthernetIfOutputTotalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputTotalDrops.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetIfOutputTotalDrops.setUnits("packets")


class _CLApEthernetIfCdpEnabled_Type(TruthValue):
    """Custom type cLApEthernetIfCdpEnabled based on TruthValue"""
    defaultValue = 1


_CLApEthernetIfCdpEnabled_Type.__name__ = "TruthValue"
_CLApEthernetIfCdpEnabled_Object = MibTableColumn
cLApEthernetIfCdpEnabled = _CLApEthernetIfCdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 33),
    _CLApEthernetIfCdpEnabled_Type()
)
cLApEthernetIfCdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEthernetIfCdpEnabled.setStatus("current")
_CLApEthernetIfMtu_Type = Unsigned32
_CLApEthernetIfMtu_Object = MibTableColumn
cLApEthernetIfMtu = _CLApEthernetIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 34),
    _CLApEthernetIfMtu_Type()
)
cLApEthernetIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfMtu.setStatus("current")
_CLApEthernetIfType_Type = IANAifType
_CLApEthernetIfType_Object = MibTableColumn
cLApEthernetIfType = _CLApEthernetIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 35),
    _CLApEthernetIfType_Type()
)
cLApEthernetIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfType.setStatus("current")
_CLApEthernetIfLinkChangeCount_Type = Counter32
_CLApEthernetIfLinkChangeCount_Object = MibTableColumn
cLApEthernetIfLinkChangeCount = _CLApEthernetIfLinkChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 2, 1, 36),
    _CLApEthernetIfLinkChangeCount_Type()
)
cLApEthernetIfLinkChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetIfLinkChangeCount.setStatus("current")
_CLApDot11RadioTable_Object = MibTable
cLApDot11RadioTable = _CLApDot11RadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cLApDot11RadioTable.setStatus("current")
_CLApDot11RadioEntry_Object = MibTableRow
cLApDot11RadioEntry = _CLApDot11RadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1)
)
cLApDot11RadioEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApDot11RadioEntry.setStatus("current")
_CLApDot11RadioMACAddress_Type = MacAddress
_CLApDot11RadioMACAddress_Object = MibTableColumn
cLApDot11RadioMACAddress = _CLApDot11RadioMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 1),
    _CLApDot11RadioMACAddress_Type()
)
cLApDot11RadioMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioMACAddress.setStatus("current")
_CLApDot11RadioSubBand_Type = CLApDot11RadioSubband
_CLApDot11RadioSubBand_Object = MibTableColumn
cLApDot11RadioSubBand = _CLApDot11RadioSubBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 2),
    _CLApDot11RadioSubBand_Type()
)
cLApDot11RadioSubBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioSubBand.setStatus("current")


class _CLApDot11RadioVersion_Type(SnmpAdminString):
    """Custom type cLApDot11RadioVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_CLApDot11RadioVersion_Type.__name__ = "SnmpAdminString"
_CLApDot11RadioVersion_Object = MibTableColumn
cLApDot11RadioVersion = _CLApDot11RadioVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 3),
    _CLApDot11RadioVersion_Type()
)
cLApDot11RadioVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioVersion.setStatus("current")
_CLApDot11IsBackhaul_Type = TruthValue
_CLApDot11IsBackhaul_Object = MibTableColumn
cLApDot11IsBackhaul = _CLApDot11IsBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 4),
    _CLApDot11IsBackhaul_Type()
)
cLApDot11IsBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11IsBackhaul.setStatus("current")
_CLApDot11RadioRole_Type = CLApDot11RadioRole
_CLApDot11RadioRole_Object = MibTableColumn
cLApDot11RadioRole = _CLApDot11RadioRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 5),
    _CLApDot11RadioRole_Type()
)
cLApDot11RadioRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRole.setStatus("current")


class _CLApDot11RadioMode_Type(Integer32):
    """Custom type cLApDot11RadioMode based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("monitor", 2),
          ("remote", 3),
          ("rogueDetector", 4),
          ("sniffer", 5),
          ("bridge", 6),
          ("seConnect", 7),
          ("remoteBridge", 8),
          ("hybridRemote", 9),
          ("sensor", 10))
    )


_CLApDot11RadioMode_Type.__name__ = "Integer32"
_CLApDot11RadioMode_Object = MibTableColumn
cLApDot11RadioMode = _CLApDot11RadioMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 6),
    _CLApDot11RadioMode_Type()
)
cLApDot11RadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioMode.setStatus("current")


class _CLApDot11RadioSubType_Type(Integer32):
    """Custom type cLApDot11RadioSubType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("rxOnly", 2),
          ("slaveAc", 3),
          ("remoteLan", 4),
          ("xorTxRx", 5),
          ("bleTxRx", 6),
          ("bleRxOnly", 7),
          ("slave", 8))
    )


_CLApDot11RadioSubType_Type.__name__ = "Integer32"
_CLApDot11RadioSubType_Object = MibTableColumn
cLApDot11RadioSubType = _CLApDot11RadioSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 3, 1, 7),
    _CLApDot11RadioSubType_Type()
)
cLApDot11RadioSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioSubType.setStatus("current")
_CLApDot11IfAntennaTable_Object = MibTable
cLApDot11IfAntennaTable = _CLApDot11IfAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cLApDot11IfAntennaTable.setStatus("current")
_CLApDot11IfAntennaEntry_Object = MibTableRow
cLApDot11IfAntennaEntry = _CLApDot11IfAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1)
)
cLApDot11IfAntennaEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaId"),
)
if mibBuilder.loadTexts:
    cLApDot11IfAntennaEntry.setStatus("current")


class _CLApDot11IfAntennaId_Type(Unsigned32):
    """Custom type cLApDot11IfAntennaId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CLApDot11IfAntennaId_Type.__name__ = "Unsigned32"
_CLApDot11IfAntennaId_Object = MibTableColumn
cLApDot11IfAntennaId = _CLApDot11IfAntennaId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 1),
    _CLApDot11IfAntennaId_Type()
)
cLApDot11IfAntennaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaId.setStatus("current")


class _CLApDot11IfAntennaTxEnable_Type(TruthValue):
    """Custom type cLApDot11IfAntennaTxEnable based on TruthValue"""
    defaultValue = 1


_CLApDot11IfAntennaTxEnable_Type.__name__ = "TruthValue"
_CLApDot11IfAntennaTxEnable_Object = MibTableColumn
cLApDot11IfAntennaTxEnable = _CLApDot11IfAntennaTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 2),
    _CLApDot11IfAntennaTxEnable_Type()
)
cLApDot11IfAntennaTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaTxEnable.setStatus("current")


class _CLApDot11IfAntennaRxEnable_Type(TruthValue):
    """Custom type cLApDot11IfAntennaRxEnable based on TruthValue"""
    defaultValue = 1


_CLApDot11IfAntennaRxEnable_Type.__name__ = "TruthValue"
_CLApDot11IfAntennaRxEnable_Object = MibTableColumn
cLApDot11IfAntennaRxEnable = _CLApDot11IfAntennaRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 3),
    _CLApDot11IfAntennaRxEnable_Type()
)
cLApDot11IfAntennaRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaRxEnable.setStatus("current")


class _CLApDot11IfAntennaEnable_Type(TruthValue):
    """Custom type cLApDot11IfAntennaEnable based on TruthValue"""
    defaultValue = 1


_CLApDot11IfAntennaEnable_Type.__name__ = "TruthValue"
_CLApDot11IfAntennaEnable_Object = MibTableColumn
cLApDot11IfAntennaEnable = _CLApDot11IfAntennaEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 4, 1, 4),
    _CLApDot11IfAntennaEnable_Type()
)
cLApDot11IfAntennaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApDot11IfAntennaEnable.setStatus("current")
_CLApVlanIfTable_Object = MibTable
cLApVlanIfTable = _CLApVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cLApVlanIfTable.setStatus("current")
_CLApVlanIfEntry_Object = MibTableRow
cLApVlanIfEntry = _CLApVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1)
)
cLApVlanIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApVlanIfEthernetId"),
)
if mibBuilder.loadTexts:
    cLApVlanIfEntry.setStatus("current")


class _CLApVlanIfEthernetId_Type(Unsigned32):
    """Custom type cLApVlanIfEthernetId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CLApVlanIfEthernetId_Type.__name__ = "Unsigned32"
_CLApVlanIfEthernetId_Object = MibTableColumn
cLApVlanIfEthernetId = _CLApVlanIfEthernetId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 1),
    _CLApVlanIfEthernetId_Type()
)
cLApVlanIfEthernetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApVlanIfEthernetId.setStatus("current")


class _CLApVlanIfMode_Type(Integer32):
    """Custom type cLApVlanIfMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("access", 2),
          ("trunk", 3))
    )


_CLApVlanIfMode_Type.__name__ = "Integer32"
_CLApVlanIfMode_Object = MibTableColumn
cLApVlanIfMode = _CLApVlanIfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 2),
    _CLApVlanIfMode_Type()
)
cLApVlanIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVlanIfMode.setStatus("current")


class _CLApVlanIfEnable_Type(TruthValue):
    """Custom type cLApVlanIfEnable based on TruthValue"""
    defaultValue = 1


_CLApVlanIfEnable_Type.__name__ = "TruthValue"
_CLApVlanIfEnable_Object = MibTableColumn
cLApVlanIfEnable = _CLApVlanIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 3),
    _CLApVlanIfEnable_Type()
)
cLApVlanIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVlanIfEnable.setStatus("current")
_CLApVlanIfNativeVlanId_Type = Unsigned32
_CLApVlanIfNativeVlanId_Object = MibTableColumn
cLApVlanIfNativeVlanId = _CLApVlanIfNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 5, 1, 4),
    _CLApVlanIfNativeVlanId_Type()
)
cLApVlanIfNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApVlanIfNativeVlanId.setStatus("current")
_CLApVlanListTable_Object = MibTable
cLApVlanListTable = _CLApVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cLApVlanListTable.setStatus("current")
_CLApVlanListEntry_Object = MibTableRow
cLApVlanListEntry = _CLApVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6, 1)
)
cLApVlanListEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApVlanIfEthernetId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApVlanListVlanId"),
)
if mibBuilder.loadTexts:
    cLApVlanListEntry.setStatus("current")
_CLApVlanListVlanId_Type = Unsigned32
_CLApVlanListVlanId_Object = MibTableColumn
cLApVlanListVlanId = _CLApVlanListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6, 1, 1),
    _CLApVlanListVlanId_Type()
)
cLApVlanListVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApVlanListVlanId.setStatus("current")
_CLApVlanListRowStatus_Type = RowStatus
_CLApVlanListRowStatus_Object = MibTableColumn
cLApVlanListRowStatus = _CLApVlanListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 6, 1, 2),
    _CLApVlanListRowStatus_Type()
)
cLApVlanListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApVlanListRowStatus.setStatus("current")
_CLApDot11GlobalConfigTable_Object = MibTable
cLApDot11GlobalConfigTable = _CLApDot11GlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cLApDot11GlobalConfigTable.setStatus("current")
_CLApDot11GlobalConfigEntry_Object = MibTableRow
cLApDot11GlobalConfigEntry = _CLApDot11GlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1)
)
cLApDot11GlobalConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
)
if mibBuilder.loadTexts:
    cLApDot11GlobalConfigEntry.setStatus("current")


class _CLApNwLegacyBeamForming_Type(Integer32):
    """Custom type cLApNwLegacyBeamForming based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("notApplicable", 3))
    )


_CLApNwLegacyBeamForming_Type.__name__ = "Integer32"
_CLApNwLegacyBeamForming_Object = MibTableColumn
cLApNwLegacyBeamForming = _CLApNwLegacyBeamForming_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1, 1),
    _CLApNwLegacyBeamForming_Type()
)
cLApNwLegacyBeamForming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNwLegacyBeamForming.setStatus("deprecated")


class _CLApNwTxPowerThreshold_Type(Integer32):
    """Custom type cLApNwTxPowerThreshold based on Integer32"""
    defaultValue = -70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -50),
    )


_CLApNwTxPowerThreshold_Type.__name__ = "Integer32"
_CLApNwTxPowerThreshold_Object = MibTableColumn
cLApNwTxPowerThreshold = _CLApNwTxPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1, 2),
    _CLApNwTxPowerThreshold_Type()
)
cLApNwTxPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNwTxPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLApNwTxPowerThreshold.setUnits("dbm")


class _CLApNwTxPowerThresholdVer2_Type(Integer32):
    """Custom type cLApNwTxPowerThresholdVer2 based on Integer32"""
    defaultValue = -67

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, -50),
    )


_CLApNwTxPowerThresholdVer2_Type.__name__ = "Integer32"
_CLApNwTxPowerThresholdVer2_Object = MibTableColumn
cLApNwTxPowerThresholdVer2 = _CLApNwTxPowerThresholdVer2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 7, 1, 3),
    _CLApNwTxPowerThresholdVer2_Type()
)
cLApNwTxPowerThresholdVer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApNwTxPowerThresholdVer2.setStatus("current")
if mibBuilder.loadTexts:
    cLApNwTxPowerThresholdVer2.setUnits("dbm")
_CLApDot11RadioStatsTable_Object = MibTable
cLApDot11RadioStatsTable = _CLApDot11RadioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8)
)
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTable.setStatus("current")
_CLApDot11RadioStatsEntry_Object = MibTableRow
cLApDot11RadioStatsEntry = _CLApDot11RadioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1)
)
cLApDot11RadioStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApDot11RadioStatsEntry.setStatus("current")
_CLApDot11RadioStatsRxErrorFrameCount_Type = Counter32
_CLApDot11RadioStatsRxErrorFrameCount_Object = MibTableColumn
cLApDot11RadioStatsRxErrorFrameCount = _CLApDot11RadioStatsRxErrorFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 1),
    _CLApDot11RadioStatsRxErrorFrameCount_Type()
)
cLApDot11RadioStatsRxErrorFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxErrorFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxErrorFrameCount.setUnits("frames")
_CLApDot11RadioStatsMacMicErrFrameCount_Type = Counter32
_CLApDot11RadioStatsMacMicErrFrameCount_Object = MibTableColumn
cLApDot11RadioStatsMacMicErrFrameCount = _CLApDot11RadioStatsMacMicErrFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 2),
    _CLApDot11RadioStatsMacMicErrFrameCount_Type()
)
cLApDot11RadioStatsMacMicErrFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsMacMicErrFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsMacMicErrFrameCount.setUnits("frames")
_CLApDot11RadioStatsMacDecryptErrFrameCount_Type = Counter32
_CLApDot11RadioStatsMacDecryptErrFrameCount_Object = MibTableColumn
cLApDot11RadioStatsMacDecryptErrFrameCount = _CLApDot11RadioStatsMacDecryptErrFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 3),
    _CLApDot11RadioStatsMacDecryptErrFrameCount_Type()
)
cLApDot11RadioStatsMacDecryptErrFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsMacDecryptErrFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsMacDecryptErrFrameCount.setUnits("frames")
_CLApDot11RadioStatsRxMgmtFrameCount_Type = Counter32
_CLApDot11RadioStatsRxMgmtFrameCount_Object = MibTableColumn
cLApDot11RadioStatsRxMgmtFrameCount = _CLApDot11RadioStatsRxMgmtFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 4),
    _CLApDot11RadioStatsRxMgmtFrameCount_Type()
)
cLApDot11RadioStatsRxMgmtFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxMgmtFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxMgmtFrameCount.setUnits("frames")
_CLApDot11RadioStatsRxCtrlFrameCount_Type = Counter32
_CLApDot11RadioStatsRxCtrlFrameCount_Object = MibTableColumn
cLApDot11RadioStatsRxCtrlFrameCount = _CLApDot11RadioStatsRxCtrlFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 5),
    _CLApDot11RadioStatsRxCtrlFrameCount_Type()
)
cLApDot11RadioStatsRxCtrlFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxCtrlFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxCtrlFrameCount.setUnits("frames")
_CLApDot11RadioStatsRxDataFrameCount_Type = Counter32
_CLApDot11RadioStatsRxDataFrameCount_Object = MibTableColumn
cLApDot11RadioStatsRxDataFrameCount = _CLApDot11RadioStatsRxDataFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 6),
    _CLApDot11RadioStatsRxDataFrameCount_Type()
)
cLApDot11RadioStatsRxDataFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxDataFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxDataFrameCount.setUnits("frames")
_CLApDot11RadioStatsTxMgmtFrameCount_Type = Counter32
_CLApDot11RadioStatsTxMgmtFrameCount_Object = MibTableColumn
cLApDot11RadioStatsTxMgmtFrameCount = _CLApDot11RadioStatsTxMgmtFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 7),
    _CLApDot11RadioStatsTxMgmtFrameCount_Type()
)
cLApDot11RadioStatsTxMgmtFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxMgmtFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxMgmtFrameCount.setUnits("frames")
_CLApDot11RadioStatsTxCtrlFrameCount_Type = Counter32
_CLApDot11RadioStatsTxCtrlFrameCount_Object = MibTableColumn
cLApDot11RadioStatsTxCtrlFrameCount = _CLApDot11RadioStatsTxCtrlFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 8),
    _CLApDot11RadioStatsTxCtrlFrameCount_Type()
)
cLApDot11RadioStatsTxCtrlFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxCtrlFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxCtrlFrameCount.setUnits("frames")
_CLApDot11RadioStatsTxDataFrameCount_Type = Counter32
_CLApDot11RadioStatsTxDataFrameCount_Object = MibTableColumn
cLApDot11RadioStatsTxDataFrameCount = _CLApDot11RadioStatsTxDataFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 9),
    _CLApDot11RadioStatsTxDataFrameCount_Type()
)
cLApDot11RadioStatsTxDataFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxDataFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxDataFrameCount.setUnits("frames")
_CLApDot11RadioStatsRxDataPacketCount_Type = Counter32
_CLApDot11RadioStatsRxDataPacketCount_Object = MibTableColumn
cLApDot11RadioStatsRxDataPacketCount = _CLApDot11RadioStatsRxDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 10),
    _CLApDot11RadioStatsRxDataPacketCount_Type()
)
cLApDot11RadioStatsRxDataPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxDataPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRxDataPacketCount.setUnits("packets")
_CLApDot11RadioStatsTxDataPacketCount_Type = Counter32
_CLApDot11RadioStatsTxDataPacketCount_Object = MibTableColumn
cLApDot11RadioStatsTxDataPacketCount = _CLApDot11RadioStatsTxDataPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 11),
    _CLApDot11RadioStatsTxDataPacketCount_Type()
)
cLApDot11RadioStatsTxDataPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxDataPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsTxDataPacketCount.setUnits("packets")
_CLApDot11RadioStatsRetryFrameCount_Type = Counter32
_CLApDot11RadioStatsRetryFrameCount_Object = MibTableColumn
cLApDot11RadioStatsRetryFrameCount = _CLApDot11RadioStatsRetryFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 12),
    _CLApDot11RadioStatsRetryFrameCount_Type()
)
cLApDot11RadioStatsRetryFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRetryFrameCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRetryFrameCount.setUnits("frames")
_CLApDot11RadioStatsRetryPacketCount_Type = Counter32
_CLApDot11RadioStatsRetryPacketCount_Object = MibTableColumn
cLApDot11RadioStatsRetryPacketCount = _CLApDot11RadioStatsRetryPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 8, 1, 13),
    _CLApDot11RadioStatsRetryPacketCount_Type()
)
cLApDot11RadioStatsRetryPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRetryPacketCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioStatsRetryPacketCount.setUnits("packets")
_CLApDot11RadioRssiTable_Object = MibTable
cLApDot11RadioRssiTable = _CLApDot11RadioRssiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cLApDot11RadioRssiTable.setStatus("current")
_CLApDot11RadioRssiEntry_Object = MibTableRow
cLApDot11RadioRssiEntry = _CLApDot11RadioRssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 9, 1)
)
cLApDot11RadioRssiEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
)
if mibBuilder.loadTexts:
    cLApDot11RadioRssiEntry.setStatus("current")
_CLApDot11RadioRssiHighest_Type = Integer32
_CLApDot11RadioRssiHighest_Object = MibTableColumn
cLApDot11RadioRssiHighest = _CLApDot11RadioRssiHighest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 9, 1, 1),
    _CLApDot11RadioRssiHighest_Type()
)
cLApDot11RadioRssiHighest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRssiHighest.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioRssiHighest.setUnits("dbm")
_CLApDot11RadioRssiLowest_Type = Integer32
_CLApDot11RadioRssiLowest_Object = MibTableColumn
cLApDot11RadioRssiLowest = _CLApDot11RadioRssiLowest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 9, 1, 2),
    _CLApDot11RadioRssiLowest_Type()
)
cLApDot11RadioRssiLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRssiLowest.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioRssiLowest.setUnits("dbm")
_CLApDot11RadioRssiAverage_Type = Integer32
_CLApDot11RadioRssiAverage_Object = MibTableColumn
cLApDot11RadioRssiAverage = _CLApDot11RadioRssiAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 9, 1, 3),
    _CLApDot11RadioRssiAverage_Type()
)
cLApDot11RadioRssiAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRssiAverage.setStatus("current")
if mibBuilder.loadTexts:
    cLApDot11RadioRssiAverage.setUnits("dbm")
_CLApDot11RadioRateStatsTable_Object = MibTable
cLApDot11RadioRateStatsTable = _CLApDot11RadioRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10)
)
if mibBuilder.loadTexts:
    cLApDot11RadioRateStatsTable.setStatus("current")
_CLApDot11RadioRateStatsEntry_Object = MibTableRow
cLApDot11RadioRateStatsEntry = _CLApDot11RadioRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1)
)
cLApDot11RadioRateStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11RadioRate"),
)
if mibBuilder.loadTexts:
    cLApDot11RadioRateStatsEntry.setStatus("current")
_CLApDot11RadioRate_Type = Unsigned32
_CLApDot11RadioRate_Object = MibTableColumn
cLApDot11RadioRate = _CLApDot11RadioRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1, 1),
    _CLApDot11RadioRate_Type()
)
cLApDot11RadioRate.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApDot11RadioRate.setStatus("current")
_CLApDot11RadioRateStatsRxPackets_Type = Counter32
_CLApDot11RadioRateStatsRxPackets_Object = MibTableColumn
cLApDot11RadioRateStatsRxPackets = _CLApDot11RadioRateStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1, 2),
    _CLApDot11RadioRateStatsRxPackets_Type()
)
cLApDot11RadioRateStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRateStatsRxPackets.setStatus("current")
_CLApDot11RadioRateStatsRxBytes_Type = Counter32
_CLApDot11RadioRateStatsRxBytes_Object = MibTableColumn
cLApDot11RadioRateStatsRxBytes = _CLApDot11RadioRateStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1, 3),
    _CLApDot11RadioRateStatsRxBytes_Type()
)
cLApDot11RadioRateStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRateStatsRxBytes.setStatus("current")
_CLApDot11RadioRateStatsTxPackets_Type = Counter32
_CLApDot11RadioRateStatsTxPackets_Object = MibTableColumn
cLApDot11RadioRateStatsTxPackets = _CLApDot11RadioRateStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1, 4),
    _CLApDot11RadioRateStatsTxPackets_Type()
)
cLApDot11RadioRateStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRateStatsTxPackets.setStatus("current")
_CLApDot11RadioRateStatsTxBytes_Type = Counter32
_CLApDot11RadioRateStatsTxBytes_Object = MibTableColumn
cLApDot11RadioRateStatsTxBytes = _CLApDot11RadioRateStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1, 5),
    _CLApDot11RadioRateStatsTxBytes_Type()
)
cLApDot11RadioRateStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRateStatsTxBytes.setStatus("current")
_CLApDot11RadioRateString_Type = SnmpAdminString
_CLApDot11RadioRateString_Object = MibTableColumn
cLApDot11RadioRateString = _CLApDot11RadioRateString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 10, 1, 6),
    _CLApDot11RadioRateString_Type()
)
cLApDot11RadioRateString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioRateString.setStatus("current")
_CLApDot11RadioSsidTable_Object = MibTable
cLApDot11RadioSsidTable = _CLApDot11RadioSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 11)
)
if mibBuilder.loadTexts:
    cLApDot11RadioSsidTable.setStatus("current")
_CLApDot11RadioSsidEntry_Object = MibTableRow
cLApDot11RadioSsidEntry = _CLApDot11RadioSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 11, 1)
)
cLApDot11RadioSsidEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSsidIndex"),
)
if mibBuilder.loadTexts:
    cLApDot11RadioSsidEntry.setStatus("current")
_CLApSsidIndex_Type = Unsigned32
_CLApSsidIndex_Object = MibTableColumn
cLApSsidIndex = _CLApSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 11, 1, 1),
    _CLApSsidIndex_Type()
)
cLApSsidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApSsidIndex.setStatus("current")


class _CLApDot11RadioSsidName_Type(OctetString):
    """Custom type cLApDot11RadioSsidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApDot11RadioSsidName_Type.__name__ = "OctetString"
_CLApDot11RadioSsidName_Object = MibTableColumn
cLApDot11RadioSsidName = _CLApDot11RadioSsidName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 11, 1, 2),
    _CLApDot11RadioSsidName_Type()
)
cLApDot11RadioSsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDot11RadioSsidName.setStatus("current")
_CLApCableModemIfStatsTable_Object = MibTable
cLApCableModemIfStatsTable = _CLApCableModemIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12)
)
if mibBuilder.loadTexts:
    cLApCableModemIfStatsTable.setStatus("current")
_CLApCableModemIfStatsEntry_Object = MibTableRow
cLApCableModemIfStatsEntry = _CLApCableModemIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1)
)
cLApCableModemIfStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApCableModemIfStatsEntry.setStatus("current")
_CLApCmMacAddress_Type = MacAddress
_CLApCmMacAddress_Object = MibTableColumn
cLApCmMacAddress = _CLApCmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 1),
    _CLApCmMacAddress_Type()
)
cLApCmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmMacAddress.setStatus("current")
_CLApCmApMacAddress_Type = MacAddress
_CLApCmApMacAddress_Object = MibTableColumn
cLApCmApMacAddress = _CLApCmApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 2),
    _CLApCmApMacAddress_Type()
)
cLApCmApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmApMacAddress.setStatus("current")
_CLApCmSwVersion_Type = SnmpAdminString
_CLApCmSwVersion_Object = MibTableColumn
cLApCmSwVersion = _CLApCmSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 3),
    _CLApCmSwVersion_Type()
)
cLApCmSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmSwVersion.setStatus("current")
_CLApEthernetSpeed_Type = SnmpAdminString
_CLApEthernetSpeed_Object = MibTableColumn
cLApEthernetSpeed = _CLApEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 4),
    _CLApEthernetSpeed_Type()
)
cLApEthernetSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetSpeed.setStatus("current")
_CLApEthernetStatus_Type = SnmpAdminString
_CLApEthernetStatus_Object = MibTableColumn
cLApEthernetStatus = _CLApEthernetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 5),
    _CLApEthernetStatus_Type()
)
cLApEthernetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApEthernetStatus.setStatus("current")
_CLApCmStatus_Type = SnmpAdminString
_CLApCmStatus_Object = MibTableColumn
cLApCmStatus = _CLApCmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 6),
    _CLApCmStatus_Type()
)
cLApCmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmStatus.setStatus("current")
_CLApCmSerialNumber_Type = SnmpAdminString
_CLApCmSerialNumber_Object = MibTableColumn
cLApCmSerialNumber = _CLApCmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 7),
    _CLApCmSerialNumber_Type()
)
cLApCmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmSerialNumber.setStatus("current")
_CLApCmUsChannelStatus_Type = SnmpAdminString
_CLApCmUsChannelStatus_Object = MibTableColumn
cLApCmUsChannelStatus = _CLApCmUsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 8),
    _CLApCmUsChannelStatus_Type()
)
cLApCmUsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmUsChannelStatus.setStatus("current")
_CLApCmDsChannelStatus_Type = SnmpAdminString
_CLApCmDsChannelStatus_Object = MibTableColumn
cLApCmDsChannelStatus = _CLApCmDsChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 9),
    _CLApCmDsChannelStatus_Type()
)
cLApCmDsChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmDsChannelStatus.setStatus("current")
_CLApCmMaskBit_Type = SnmpAdminString
_CLApCmMaskBit_Object = MibTableColumn
cLApCmMaskBit = _CLApCmMaskBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 2, 12, 1, 10),
    _CLApCmMaskBit_Type()
)
cLApCmMaskBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApCmMaskBit.setStatus("current")
_CiscoLwappApGlobal_ObjectIdentity = ObjectIdentity
ciscoLwappApGlobal = _CiscoLwappApGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3)
)
_CLApFastHbTimerTable_Object = MibTable
cLApFastHbTimerTable = _CLApFastHbTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cLApFastHbTimerTable.setStatus("current")
_CLApFastHbTimerEntry_Object = MibTableRow
cLApFastHbTimerEntry = _CLApFastHbTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1)
)
cLApFastHbTimerEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApFastHbTimerApType"),
)
if mibBuilder.loadTexts:
    cLApFastHbTimerEntry.setStatus("current")


class _CLApFastHbTimerApType_Type(Integer32):
    """Custom type cLApFastHbTimerApType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("hreap", 2))
    )


_CLApFastHbTimerApType_Type.__name__ = "Integer32"
_CLApFastHbTimerApType_Object = MibTableColumn
cLApFastHbTimerApType = _CLApFastHbTimerApType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1, 1),
    _CLApFastHbTimerApType_Type()
)
cLApFastHbTimerApType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApFastHbTimerApType.setStatus("current")


class _CLApFastHbTimerTimeout_Type(Unsigned32):
    """Custom type cLApFastHbTimerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CLApFastHbTimerTimeout_Type.__name__ = "Unsigned32"
_CLApFastHbTimerTimeout_Object = MibTableColumn
cLApFastHbTimerTimeout = _CLApFastHbTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1, 2),
    _CLApFastHbTimerTimeout_Type()
)
cLApFastHbTimerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFastHbTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApFastHbTimerTimeout.setUnits("seconds")
_CLApFastHbTimerEnabled_Type = TruthValue
_CLApFastHbTimerEnabled_Object = MibTableColumn
cLApFastHbTimerEnabled = _CLApFastHbTimerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 1, 1, 3),
    _CLApFastHbTimerEnabled_Type()
)
cLApFastHbTimerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApFastHbTimerEnabled.setStatus("current")


class _CLApPrimaryDiscoveryTimeout_Type(Unsigned32):
    """Custom type cLApPrimaryDiscoveryTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_CLApPrimaryDiscoveryTimeout_Type.__name__ = "Unsigned32"
_CLApPrimaryDiscoveryTimeout_Object = MibScalar
cLApPrimaryDiscoveryTimeout = _CLApPrimaryDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 3),
    _CLApPrimaryDiscoveryTimeout_Type()
)
cLApPrimaryDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimaryDiscoveryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApPrimaryDiscoveryTimeout.setUnits("seconds")
_CLApGlobalPrimaryControllerAddressType_Type = InetAddressType
_CLApGlobalPrimaryControllerAddressType_Object = MibScalar
cLApGlobalPrimaryControllerAddressType = _CLApGlobalPrimaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 4),
    _CLApGlobalPrimaryControllerAddressType_Type()
)
cLApGlobalPrimaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPrimaryControllerAddressType.setStatus("current")
_CLApGlobalPrimaryControllerAddress_Type = InetAddress
_CLApGlobalPrimaryControllerAddress_Object = MibScalar
cLApGlobalPrimaryControllerAddress = _CLApGlobalPrimaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 5),
    _CLApGlobalPrimaryControllerAddress_Type()
)
cLApGlobalPrimaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPrimaryControllerAddress.setStatus("current")


class _CLApGlobalPrimaryControllerName_Type(SnmpAdminString):
    """Custom type cLApGlobalPrimaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApGlobalPrimaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApGlobalPrimaryControllerName_Object = MibScalar
cLApGlobalPrimaryControllerName = _CLApGlobalPrimaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 6),
    _CLApGlobalPrimaryControllerName_Type()
)
cLApGlobalPrimaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPrimaryControllerName.setStatus("current")
_CLApGlobalSecondaryControllerAddressType_Type = InetAddressType
_CLApGlobalSecondaryControllerAddressType_Object = MibScalar
cLApGlobalSecondaryControllerAddressType = _CLApGlobalSecondaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 7),
    _CLApGlobalSecondaryControllerAddressType_Type()
)
cLApGlobalSecondaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalSecondaryControllerAddressType.setStatus("current")
_CLApGlobalSecondaryControllerAddress_Type = InetAddress
_CLApGlobalSecondaryControllerAddress_Object = MibScalar
cLApGlobalSecondaryControllerAddress = _CLApGlobalSecondaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 8),
    _CLApGlobalSecondaryControllerAddress_Type()
)
cLApGlobalSecondaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalSecondaryControllerAddress.setStatus("current")


class _CLApGlobalSecondaryControllerName_Type(SnmpAdminString):
    """Custom type cLApGlobalSecondaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApGlobalSecondaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApGlobalSecondaryControllerName_Object = MibScalar
cLApGlobalSecondaryControllerName = _CLApGlobalSecondaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 9),
    _CLApGlobalSecondaryControllerName_Type()
)
cLApGlobalSecondaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalSecondaryControllerName.setStatus("current")


class _CLApGlobalFailoverPriority_Type(TruthValue):
    """Custom type cLApGlobalFailoverPriority based on TruthValue"""
    defaultValue = 2


_CLApGlobalFailoverPriority_Type.__name__ = "TruthValue"
_CLApGlobalFailoverPriority_Object = MibScalar
cLApGlobalFailoverPriority = _CLApGlobalFailoverPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 10),
    _CLApGlobalFailoverPriority_Type()
)
cLApGlobalFailoverPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalFailoverPriority.setStatus("current")


class _CLApGlobalTcpMss_Type(Integer32):
    """Custom type cLApGlobalTcpMss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(536, 1363),
    )


_CLApGlobalTcpMss_Type.__name__ = "Integer32"
_CLApGlobalTcpMss_Object = MibScalar
cLApGlobalTcpMss = _CLApGlobalTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 11),
    _CLApGlobalTcpMss_Type()
)
cLApGlobalTcpMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalTcpMss.setStatus("current")
_CLApGlobalDot11IfTable_Object = MibTable
cLApGlobalDot11IfTable = _CLApGlobalDot11IfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 12)
)
if mibBuilder.loadTexts:
    cLApGlobalDot11IfTable.setStatus("current")
_CLApGlobalDot11IfEntry_Object = MibTableRow
cLApGlobalDot11IfEntry = _CLApGlobalDot11IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 12, 1)
)
cLApGlobalDot11IfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLApGlobalDot11IfEntry.setStatus("current")
_CLApGlobalDot11IfCdpEnabled_Type = TruthValue
_CLApGlobalDot11IfCdpEnabled_Object = MibTableColumn
cLApGlobalDot11IfCdpEnabled = _CLApGlobalDot11IfCdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 12, 1, 1),
    _CLApGlobalDot11IfCdpEnabled_Type()
)
cLApGlobalDot11IfCdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalDot11IfCdpEnabled.setStatus("current")
_CLApGlobalEthernetIfTable_Object = MibTable
cLApGlobalEthernetIfTable = _CLApGlobalEthernetIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 13)
)
if mibBuilder.loadTexts:
    cLApGlobalEthernetIfTable.setStatus("current")
_CLApGlobalEthernetIfEntry_Object = MibTableRow
cLApGlobalEthernetIfEntry = _CLApGlobalEthernetIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 13, 1)
)
cLApGlobalEthernetIfEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
)
if mibBuilder.loadTexts:
    cLApGlobalEthernetIfEntry.setStatus("current")
_CLApGlobalEthernetIfCdpEnabled_Type = TruthValue
_CLApGlobalEthernetIfCdpEnabled_Object = MibTableColumn
cLApGlobalEthernetIfCdpEnabled = _CLApGlobalEthernetIfCdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 13, 1, 1),
    _CLApGlobalEthernetIfCdpEnabled_Type()
)
cLApGlobalEthernetIfCdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalEthernetIfCdpEnabled.setStatus("current")
_CLApGlobalRetransmitCount_Type = Unsigned32
_CLApGlobalRetransmitCount_Object = MibScalar
cLApGlobalRetransmitCount = _CLApGlobalRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 14),
    _CLApGlobalRetransmitCount_Type()
)
cLApGlobalRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitCount.setUnits("retries")
_CLApGlobalRetransmitTimeout_Type = Unsigned32
_CLApGlobalRetransmitTimeout_Object = MibScalar
cLApGlobalRetransmitTimeout = _CLApGlobalRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 15),
    _CLApGlobalRetransmitTimeout_Type()
)
cLApGlobalRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApGlobalRetransmitTimeout.setUnits("seconds")
_CLApOeapDisableLocalAccess_Type = TruthValue
_CLApOeapDisableLocalAccess_Object = MibScalar
cLApOeapDisableLocalAccess = _CLApOeapDisableLocalAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 16),
    _CLApOeapDisableLocalAccess_Type()
)
cLApOeapDisableLocalAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApOeapDisableLocalAccess.setStatus("current")
_CLApGlobalLEDState_Type = TruthValue
_CLApGlobalLEDState_Object = MibScalar
cLApGlobalLEDState = _CLApGlobalLEDState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 17),
    _CLApGlobalLEDState_Type()
)
cLApGlobalLEDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalLEDState.setStatus("current")
_CLApRadioInterfaceShutdownEnabled_Type = TruthValue
_CLApRadioInterfaceShutdownEnabled_Object = MibScalar
cLApRadioInterfaceShutdownEnabled = _CLApRadioInterfaceShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 18),
    _CLApRadioInterfaceShutdownEnabled_Type()
)
cLApRadioInterfaceShutdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApRadioInterfaceShutdownEnabled.setStatus("current")
_CLApEthernetInterfaceDowntime_Type = Unsigned32
_CLApEthernetInterfaceDowntime_Object = MibScalar
cLApEthernetInterfaceDowntime = _CLApEthernetInterfaceDowntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 19),
    _CLApEthernetInterfaceDowntime_Type()
)
cLApEthernetInterfaceDowntime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApEthernetInterfaceDowntime.setStatus("current")
if mibBuilder.loadTexts:
    cLApEthernetInterfaceDowntime.setUnits("Seconds")
_CLAPMulticastGroupAddressType_Type = InetAddressType
_CLAPMulticastGroupAddressType_Object = MibScalar
cLAPMulticastGroupAddressType = _CLAPMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 20),
    _CLAPMulticastGroupAddressType_Type()
)
cLAPMulticastGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPMulticastGroupAddressType.setStatus("current")
_CLAPMulticastGroupAddress_Type = InetAddress
_CLAPMulticastGroupAddress_Object = MibScalar
cLAPMulticastGroupAddress = _CLAPMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 21),
    _CLAPMulticastGroupAddress_Type()
)
cLAPMulticastGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPMulticastGroupAddress.setStatus("current")


class _CLAPMulticastMode_Type(Integer32):
    """Custom type cLAPMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_CLAPMulticastMode_Type.__name__ = "Integer32"
_CLAPMulticastMode_Object = MibScalar
cLAPMulticastMode = _CLAPMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 22),
    _CLAPMulticastMode_Type()
)
cLAPMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAPMulticastMode.setStatus("current")


class _CLApPrimedDiscoveryTimeout_Type(Integer32):
    """Custom type cLApPrimedDiscoveryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 43200),
    )


_CLApPrimedDiscoveryTimeout_Type.__name__ = "Integer32"
_CLApPrimedDiscoveryTimeout_Object = MibScalar
cLApPrimedDiscoveryTimeout = _CLApPrimedDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 23),
    _CLApPrimedDiscoveryTimeout_Type()
)
cLApPrimedDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPrimedDiscoveryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApPrimedDiscoveryTimeout.setUnits("seconds")


class _CLApGlobalPreferMode_Type(Integer32):
    """Custom type cLApGlobalPreferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_CLApGlobalPreferMode_Type.__name__ = "Integer32"
_CLApGlobalPreferMode_Object = MibScalar
cLApGlobalPreferMode = _CLApGlobalPreferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 24),
    _CLApGlobalPreferMode_Type()
)
cLApGlobalPreferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalPreferMode.setStatus("current")
_CLApGlobalAPLagCapability_Type = TruthValue
_CLApGlobalAPLagCapability_Object = MibScalar
cLApGlobalAPLagCapability = _CLApGlobalAPLagCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 25),
    _CLApGlobalAPLagCapability_Type()
)
cLApGlobalAPLagCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalAPLagCapability.setStatus("current")


class _CLApGlobalAPDtlsVersion_Type(Integer32):
    """Custom type cLApGlobalAPDtlsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dtls10", 1),
          ("dtls12", 2),
          ("dtlsall", 3))
    )


_CLApGlobalAPDtlsVersion_Type.__name__ = "Integer32"
_CLApGlobalAPDtlsVersion_Object = MibScalar
cLApGlobalAPDtlsVersion = _CLApGlobalAPDtlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 26),
    _CLApGlobalAPDtlsVersion_Type()
)
cLApGlobalAPDtlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalAPDtlsVersion.setStatus("current")


class _CLApGlobalAPDtlsCipherSuite_Type(Integer32):
    """Custom type cLApGlobalAPDtlsCipherSuite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(47,
              51,
              53,
              57,
              61,
              156,
              157,
              49195,
              49196,
              49197)
        )
    )
    namedValues = NamedValues(
        *(("rsaaes128sha1", 47),
          ("dhersaaes128cbcsha", 51),
          ("rsaaes256sha1", 53),
          ("dhersaaes256cbcsha", 57),
          ("rsaaes256sha256", 61),
          ("rsagcm128sha256", 156),
          ("rsagcm256sha384", 157),
          ("ecdsaaes128gcmsha256", 49195),
          ("ecdsaaes256gcmsha384", 49196),
          ("dhersaaes256cbcsha256", 49197))
    )


_CLApGlobalAPDtlsCipherSuite_Type.__name__ = "Integer32"
_CLApGlobalAPDtlsCipherSuite_Object = MibScalar
cLApGlobalAPDtlsCipherSuite = _CLApGlobalAPDtlsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 27),
    _CLApGlobalAPDtlsCipherSuite_Type()
)
cLApGlobalAPDtlsCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalAPDtlsCipherSuite.setStatus("current")
_CLApGlobalMaxApsSupported_Type = Integer32
_CLApGlobalMaxApsSupported_Object = MibScalar
cLApGlobalMaxApsSupported = _CLApGlobalMaxApsSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 28),
    _CLApGlobalMaxApsSupported_Type()
)
cLApGlobalMaxApsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGlobalMaxApsSupported.setStatus("current")
_CLApAuthorizeApMacAuth_Type = TruthValue
_CLApAuthorizeApMacAuth_Object = MibScalar
cLApAuthorizeApMacAuth = _CLApAuthorizeApMacAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 30),
    _CLApAuthorizeApMacAuth_Type()
)
cLApAuthorizeApMacAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAuthorizeApMacAuth.setStatus("current")
_CLApAuthorizeApSerialNumAuth_Type = TruthValue
_CLApAuthorizeApSerialNumAuth_Object = MibScalar
cLApAuthorizeApSerialNumAuth = _CLApAuthorizeApSerialNumAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 31),
    _CLApAuthorizeApSerialNumAuth_Type()
)
cLApAuthorizeApSerialNumAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAuthorizeApSerialNumAuth.setStatus("current")
_CLApAuthorizeApMethodList_Type = SnmpAdminString
_CLApAuthorizeApMethodList_Object = MibScalar
cLApAuthorizeApMethodList = _CLApAuthorizeApMethodList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 32),
    _CLApAuthorizeApMethodList_Type()
)
cLApAuthorizeApMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAuthorizeApMethodList.setStatus("current")
_CLApGlobalAPAuditReport_Type = TruthValue
_CLApGlobalAPAuditReport_Object = MibScalar
cLApGlobalAPAuditReport = _CLApGlobalAPAuditReport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 33),
    _CLApGlobalAPAuditReport_Type()
)
cLApGlobalAPAuditReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalAPAuditReport.setStatus("current")


class _CLApGlobalAPAuditReportInterval_Type(Unsigned32):
    """Custom type cLApGlobalAPAuditReportInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 43200),
    )


_CLApGlobalAPAuditReportInterval_Type.__name__ = "Unsigned32"
_CLApGlobalAPAuditReportInterval_Object = MibScalar
cLApGlobalAPAuditReportInterval = _CLApGlobalAPAuditReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 34),
    _CLApGlobalAPAuditReportInterval_Type()
)
cLApGlobalAPAuditReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobalAPAuditReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLApGlobalAPAuditReportInterval.setUnits("Minutes")
_CLApGlobalAPConnectCount_Type = Unsigned32
_CLApGlobalAPConnectCount_Object = MibScalar
cLApGlobalAPConnectCount = _CLApGlobalAPConnectCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 35),
    _CLApGlobalAPConnectCount_Type()
)
cLApGlobalAPConnectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApGlobalAPConnectCount.setStatus("current")
_CLApAuthorizeApMacMethodList_Type = SnmpAdminString
_CLApAuthorizeApMacMethodList_Object = MibScalar
cLApAuthorizeApMacMethodList = _CLApAuthorizeApMacMethodList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 36),
    _CLApAuthorizeApMacMethodList_Type()
)
cLApAuthorizeApMacMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAuthorizeApMacMethodList.setStatus("current")
_CLApAuthorizeApSerialNumMethodList_Type = SnmpAdminString
_CLApAuthorizeApSerialNumMethodList_Object = MibScalar
cLApAuthorizeApSerialNumMethodList = _CLApAuthorizeApSerialNumMethodList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 37),
    _CLApAuthorizeApSerialNumMethodList_Type()
)
cLApAuthorizeApSerialNumMethodList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApAuthorizeApSerialNumMethodList.setStatus("current")
_ClApImageUpgradeConfig_ObjectIdentity = ObjectIdentity
clApImageUpgradeConfig = _ClApImageUpgradeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 38)
)


class _ClApImageUpgradeHttpsEnable_Type(TruthValue):
    """Custom type clApImageUpgradeHttpsEnable based on TruthValue"""
    defaultValue = 2


_ClApImageUpgradeHttpsEnable_Type.__name__ = "TruthValue"
_ClApImageUpgradeHttpsEnable_Object = MibScalar
clApImageUpgradeHttpsEnable = _ClApImageUpgradeHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 3, 38, 1),
    _ClApImageUpgradeHttpsEnable_Type()
)
clApImageUpgradeHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clApImageUpgradeHttpsEnable.setStatus("current")
_CiscoLwappApCredentials_ObjectIdentity = ObjectIdentity
ciscoLwappApCredentials = _CiscoLwappApCredentials_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4)
)
_CLApCredentialGlobalUserName_Type = SnmpAdminString
_CLApCredentialGlobalUserName_Object = MibScalar
cLApCredentialGlobalUserName = _CLApCredentialGlobalUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 1),
    _CLApCredentialGlobalUserName_Type()
)
cLApCredentialGlobalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCredentialGlobalUserName.setStatus("current")
_CLApCredentialGlobalPassword_Type = SnmpAdminString
_CLApCredentialGlobalPassword_Object = MibScalar
cLApCredentialGlobalPassword = _CLApCredentialGlobalPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 2),
    _CLApCredentialGlobalPassword_Type()
)
cLApCredentialGlobalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCredentialGlobalPassword.setStatus("current")
_CLApCredentialGlobalSecret_Type = SnmpAdminString
_CLApCredentialGlobalSecret_Object = MibScalar
cLApCredentialGlobalSecret = _CLApCredentialGlobalSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 3),
    _CLApCredentialGlobalSecret_Type()
)
cLApCredentialGlobalSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApCredentialGlobalSecret.setStatus("current")
_CLApCredentialsTable_Object = MibTable
cLApCredentialsTable = _CLApCredentialsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cLApCredentialsTable.setStatus("current")
_CLApCredentialsEntry_Object = MibTableRow
cLApCredentialsEntry = _CLApCredentialsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1)
)
cLApCredentialsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApCredentialsEntry.setStatus("current")
_CLApCredentialUserName_Type = SnmpAdminString
_CLApCredentialUserName_Object = MibTableColumn
cLApCredentialUserName = _CLApCredentialUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 1),
    _CLApCredentialUserName_Type()
)
cLApCredentialUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialUserName.setStatus("current")
_CLApCredentialPassword_Type = SnmpAdminString
_CLApCredentialPassword_Object = MibTableColumn
cLApCredentialPassword = _CLApCredentialPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 2),
    _CLApCredentialPassword_Type()
)
cLApCredentialPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialPassword.setStatus("current")
_CLApCredentialSecret_Type = SnmpAdminString
_CLApCredentialSecret_Object = MibTableColumn
cLApCredentialSecret = _CLApCredentialSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 3),
    _CLApCredentialSecret_Type()
)
cLApCredentialSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialSecret.setStatus("current")
_CLApCredentialEnableGlobalCredentials_Type = TruthValue
_CLApCredentialEnableGlobalCredentials_Object = MibTableColumn
cLApCredentialEnableGlobalCredentials = _CLApCredentialEnableGlobalCredentials_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 4, 4, 1, 4),
    _CLApCredentialEnableGlobalCredentials_Type()
)
cLApCredentialEnableGlobalCredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApCredentialEnableGlobalCredentials.setStatus("current")
_CiscoLwappLinkLatency_ObjectIdentity = ObjectIdentity
ciscoLwappLinkLatency = _CiscoLwappLinkLatency_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5)
)
_CLApLinkLatencyTable_Object = MibTable
cLApLinkLatencyTable = _CLApLinkLatencyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cLApLinkLatencyTable.setStatus("current")
_CLApLinkLatencyEntry_Object = MibTableRow
cLApLinkLatencyEntry = _CLApLinkLatencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1, 1)
)
cLApLinkLatencyEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApLinkLatencyEntry.setStatus("current")


class _CLApLinkLatencyEnable_Type(TruthValue):
    """Custom type cLApLinkLatencyEnable based on TruthValue"""
    defaultValue = 2


_CLApLinkLatencyEnable_Type.__name__ = "TruthValue"
_CLApLinkLatencyEnable_Object = MibTableColumn
cLApLinkLatencyEnable = _CLApLinkLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1, 1, 1),
    _CLApLinkLatencyEnable_Type()
)
cLApLinkLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLinkLatencyEnable.setStatus("current")


class _CLApLinkLatencyReset_Type(TruthValue):
    """Custom type cLApLinkLatencyReset based on TruthValue"""
    defaultValue = 2


_CLApLinkLatencyReset_Type.__name__ = "TruthValue"
_CLApLinkLatencyReset_Object = MibTableColumn
cLApLinkLatencyReset = _CLApLinkLatencyReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 1, 1, 2),
    _CLApLinkLatencyReset_Type()
)
cLApLinkLatencyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLinkLatencyReset.setStatus("current")
_CLApLinkLatencyStatsTable_Object = MibTable
cLApLinkLatencyStatsTable = _CLApLinkLatencyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsTable.setStatus("current")
_CLApLinkLatencyStatsEntry_Object = MibTableRow
cLApLinkLatencyStatsEntry = _CLApLinkLatencyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1)
)
cLApLinkLatencyStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsEntry.setStatus("current")
_CLApLinkLatencyStatsCurrent_Type = TimeInterval
_CLApLinkLatencyStatsCurrent_Object = MibTableColumn
cLApLinkLatencyStatsCurrent = _CLApLinkLatencyStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 1),
    _CLApLinkLatencyStatsCurrent_Type()
)
cLApLinkLatencyStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsCurrent.setUnits("milliseconds")
_CLApLinkLatencyStatsMin_Type = TimeInterval
_CLApLinkLatencyStatsMin_Object = MibTableColumn
cLApLinkLatencyStatsMin = _CLApLinkLatencyStatsMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 2),
    _CLApLinkLatencyStatsMin_Type()
)
cLApLinkLatencyStatsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMin.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMin.setUnits("milliseconds")
_CLApLinkLatencyStatsMax_Type = TimeInterval
_CLApLinkLatencyStatsMax_Object = MibTableColumn
cLApLinkLatencyStatsMax = _CLApLinkLatencyStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 3),
    _CLApLinkLatencyStatsMax_Type()
)
cLApLinkLatencyStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMax.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyStatsMax.setUnits("milliseconds")
_CLApLinkLatencyTimeStamp_Type = TimeStamp
_CLApLinkLatencyTimeStamp_Object = MibTableColumn
cLApLinkLatencyTimeStamp = _CLApLinkLatencyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 4),
    _CLApLinkLatencyTimeStamp_Type()
)
cLApLinkLatencyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLinkLatencyTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    cLApLinkLatencyTimeStamp.setUnits("seconds")
_CLApDataLinkLatencyStatsCurrent_Type = TimeInterval
_CLApDataLinkLatencyStatsCurrent_Object = MibTableColumn
cLApDataLinkLatencyStatsCurrent = _CLApDataLinkLatencyStatsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 5),
    _CLApDataLinkLatencyStatsCurrent_Type()
)
cLApDataLinkLatencyStatsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsCurrent.setUnits("milliseconds")
_CLApDataLinkLatencyStatsMin_Type = TimeInterval
_CLApDataLinkLatencyStatsMin_Object = MibTableColumn
cLApDataLinkLatencyStatsMin = _CLApDataLinkLatencyStatsMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 6),
    _CLApDataLinkLatencyStatsMin_Type()
)
cLApDataLinkLatencyStatsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMin.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMin.setUnits("milliseconds")
_CLApDataLinkLatencyStatsMax_Type = TimeInterval
_CLApDataLinkLatencyStatsMax_Object = MibTableColumn
cLApDataLinkLatencyStatsMax = _CLApDataLinkLatencyStatsMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 7),
    _CLApDataLinkLatencyStatsMax_Type()
)
cLApDataLinkLatencyStatsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMax.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyStatsMax.setUnits("milliseconds")
_CLApDataLinkLatencyTimeStamp_Type = TimeStamp
_CLApDataLinkLatencyTimeStamp_Object = MibTableColumn
cLApDataLinkLatencyTimeStamp = _CLApDataLinkLatencyTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 5, 2, 1, 8),
    _CLApDataLinkLatencyTimeStamp_Type()
)
cLApDataLinkLatencyTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyTimeStamp.setStatus("current")
if mibBuilder.loadTexts:
    cLApDataLinkLatencyTimeStamp.setUnits("seconds")
_CiscoLwappSpectrum_ObjectIdentity = ObjectIdentity
ciscoLwappSpectrum = _CiscoLwappSpectrum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 6)
)
_CiscoLwappAp802dot1xSupplicant_ObjectIdentity = ObjectIdentity
ciscoLwappAp802dot1xSupplicant = _CiscoLwappAp802dot1xSupplicant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7)
)


class _CLApGlobal802dot1xAuthenticationEnabled_Type(TruthValue):
    """Custom type cLApGlobal802dot1xAuthenticationEnabled based on TruthValue"""
    defaultValue = 2


_CLApGlobal802dot1xAuthenticationEnabled_Type.__name__ = "TruthValue"
_CLApGlobal802dot1xAuthenticationEnabled_Object = MibScalar
cLApGlobal802dot1xAuthenticationEnabled = _CLApGlobal802dot1xAuthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 1),
    _CLApGlobal802dot1xAuthenticationEnabled_Type()
)
cLApGlobal802dot1xAuthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xAuthenticationEnabled.setStatus("current")
_CLApGlobal802dot1xSupplicantUsername_Type = SnmpAdminString
_CLApGlobal802dot1xSupplicantUsername_Object = MibScalar
cLApGlobal802dot1xSupplicantUsername = _CLApGlobal802dot1xSupplicantUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 2),
    _CLApGlobal802dot1xSupplicantUsername_Type()
)
cLApGlobal802dot1xSupplicantUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xSupplicantUsername.setStatus("current")
_CLApGlobal802dot1xSupplicantPassword_Type = SnmpAdminString
_CLApGlobal802dot1xSupplicantPassword_Object = MibScalar
cLApGlobal802dot1xSupplicantPassword = _CLApGlobal802dot1xSupplicantPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 3),
    _CLApGlobal802dot1xSupplicantPassword_Type()
)
cLApGlobal802dot1xSupplicantPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xSupplicantPassword.setStatus("current")
_CLAp802dot1xSupplicantTable_Object = MibTable
cLAp802dot1xSupplicantTable = _CLAp802dot1xSupplicantTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantTable.setStatus("current")
_CLAp802dot1xSupplicantEntry_Object = MibTableRow
cLAp802dot1xSupplicantEntry = _CLAp802dot1xSupplicantEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1)
)
cLAp802dot1xSupplicantEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantEntry.setStatus("current")


class _CLAp802dot1xSupplicantOverrideEnabled_Type(TruthValue):
    """Custom type cLAp802dot1xSupplicantOverrideEnabled based on TruthValue"""
    defaultValue = 2


_CLAp802dot1xSupplicantOverrideEnabled_Type.__name__ = "TruthValue"
_CLAp802dot1xSupplicantOverrideEnabled_Object = MibTableColumn
cLAp802dot1xSupplicantOverrideEnabled = _CLAp802dot1xSupplicantOverrideEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 1),
    _CLAp802dot1xSupplicantOverrideEnabled_Type()
)
cLAp802dot1xSupplicantOverrideEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverrideEnabled.setStatus("current")
_CLAp802dot1xSupplicantOverrideUsername_Type = SnmpAdminString
_CLAp802dot1xSupplicantOverrideUsername_Object = MibTableColumn
cLAp802dot1xSupplicantOverrideUsername = _CLAp802dot1xSupplicantOverrideUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 2),
    _CLAp802dot1xSupplicantOverrideUsername_Type()
)
cLAp802dot1xSupplicantOverrideUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverrideUsername.setStatus("current")
_CLAp802dot1xSupplicantOverridePassword_Type = SnmpAdminString
_CLAp802dot1xSupplicantOverridePassword_Object = MibTableColumn
cLAp802dot1xSupplicantOverridePassword = _CLAp802dot1xSupplicantOverridePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 3),
    _CLAp802dot1xSupplicantOverridePassword_Type()
)
cLAp802dot1xSupplicantOverridePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverridePassword.setStatus("current")


class _CLAp802dot1xSupplicantOverrideEapType_Type(Integer32):
    """Custom type cLAp802dot1xSupplicantOverrideEapType based on Integer32"""
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
        *(("none", 1),
          ("eapFast", 2),
          ("eapTls", 3),
          ("peap", 4))
    )


_CLAp802dot1xSupplicantOverrideEapType_Type.__name__ = "Integer32"
_CLAp802dot1xSupplicantOverrideEapType_Object = MibTableColumn
cLAp802dot1xSupplicantOverrideEapType = _CLAp802dot1xSupplicantOverrideEapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 4, 1, 4),
    _CLAp802dot1xSupplicantOverrideEapType_Type()
)
cLAp802dot1xSupplicantOverrideEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp802dot1xSupplicantOverrideEapType.setStatus("current")


class _CLApGlobal802dot1xSupplicantEapType_Type(Integer32):
    """Custom type cLApGlobal802dot1xSupplicantEapType based on Integer32"""
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
        *(("none", 1),
          ("eapFast", 2),
          ("eapTls", 3),
          ("peap", 4))
    )


_CLApGlobal802dot1xSupplicantEapType_Type.__name__ = "Integer32"
_CLApGlobal802dot1xSupplicantEapType_Object = MibScalar
cLApGlobal802dot1xSupplicantEapType = _CLApGlobal802dot1xSupplicantEapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 7, 5),
    _CLApGlobal802dot1xSupplicantEapType_Type()
)
cLApGlobal802dot1xSupplicantEapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApGlobal802dot1xSupplicantEapType.setStatus("current")
_CLApSeClientTable_Object = MibTable
cLApSeClientTable = _CLApSeClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8)
)
if mibBuilder.loadTexts:
    cLApSeClientTable.setStatus("current")
_CLApSeClientEntry_Object = MibTableRow
cLApSeClientEntry = _CLApSeClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1)
)
cLApSeClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApSeIndex"),
)
if mibBuilder.loadTexts:
    cLApSeClientEntry.setStatus("current")


class _CLApSeIndex_Type(Integer32):
    """Custom type cLApSeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_CLApSeIndex_Type.__name__ = "Integer32"
_CLApSeIndex_Object = MibTableColumn
cLApSeIndex = _CLApSeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 1),
    _CLApSeIndex_Type()
)
cLApSeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApSeIndex.setStatus("current")
_CLApSeClientUserName_Type = SnmpAdminString
_CLApSeClientUserName_Object = MibTableColumn
cLApSeClientUserName = _CLApSeClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 2),
    _CLApSeClientUserName_Type()
)
cLApSeClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientUserName.setStatus("current")
_CLApSeClientIPAddrType_Type = InetAddressType
_CLApSeClientIPAddrType_Object = MibTableColumn
cLApSeClientIPAddrType = _CLApSeClientIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 3),
    _CLApSeClientIPAddrType_Type()
)
cLApSeClientIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientIPAddrType.setStatus("current")
_CLApSeClientIPAddr_Type = InetAddress
_CLApSeClientIPAddr_Object = MibTableColumn
cLApSeClientIPAddr = _CLApSeClientIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 4),
    _CLApSeClientIPAddr_Type()
)
cLApSeClientIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientIPAddr.setStatus("current")
_CLApSeClientDuration_Type = TimeInterval
_CLApSeClientDuration_Object = MibTableColumn
cLApSeClientDuration = _CLApSeClientDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 5),
    _CLApSeClientDuration_Type()
)
cLApSeClientDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientDuration.setStatus("current")
_CLApSeClientPort_Type = InetPortNumber
_CLApSeClientPort_Object = MibTableColumn
cLApSeClientPort = _CLApSeClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 8, 1, 6),
    _CLApSeClientPort_Type()
)
cLApSeClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSeClientPort.setStatus("current")
_CiscoLwappApWlanStats_ObjectIdentity = ObjectIdentity
ciscoLwappApWlanStats = _CiscoLwappApWlanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9)
)
_CLApWlanStatsTable_Object = MibTable
cLApWlanStatsTable = _CLApWlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cLApWlanStatsTable.setStatus("current")
_CLApWlanStatsEntry_Object = MibTableRow
cLApWlanStatsEntry = _CLApWlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1)
)
cLApWlanStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLApWlanStatsEntry.setStatus("current")
_CLApWlanStatsTxPktNum_Type = Counter64
_CLApWlanStatsTxPktNum_Object = MibTableColumn
cLApWlanStatsTxPktNum = _CLApWlanStatsTxPktNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 1),
    _CLApWlanStatsTxPktNum_Type()
)
cLApWlanStatsTxPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsTxPktNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApWlanStatsTxPktNum.setUnits("packets")
_CLApWlanStatsTxOctetNum_Type = Counter64
_CLApWlanStatsTxOctetNum_Object = MibTableColumn
cLApWlanStatsTxOctetNum = _CLApWlanStatsTxOctetNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 2),
    _CLApWlanStatsTxOctetNum_Type()
)
cLApWlanStatsTxOctetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsTxOctetNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApWlanStatsTxOctetNum.setUnits("packets")
_CLApWlanStatsRxPktNum_Type = Counter64
_CLApWlanStatsRxPktNum_Object = MibTableColumn
cLApWlanStatsRxPktNum = _CLApWlanStatsRxPktNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 3),
    _CLApWlanStatsRxPktNum_Type()
)
cLApWlanStatsRxPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsRxPktNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApWlanStatsRxPktNum.setUnits("packets")
_CLApWlanStatsRxOctetNum_Type = Counter64
_CLApWlanStatsRxOctetNum_Object = MibTableColumn
cLApWlanStatsRxOctetNum = _CLApWlanStatsRxOctetNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 4),
    _CLApWlanStatsRxOctetNum_Type()
)
cLApWlanStatsRxOctetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsRxOctetNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApWlanStatsRxOctetNum.setUnits("packets")
_CLApWlanStatsRetransmitNum_Type = Counter64
_CLApWlanStatsRetransmitNum_Object = MibTableColumn
cLApWlanStatsRetransmitNum = _CLApWlanStatsRetransmitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 5),
    _CLApWlanStatsRetransmitNum_Type()
)
cLApWlanStatsRetransmitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsRetransmitNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApWlanStatsRetransmitNum.setUnits("packets")
_CLApWlanStatsAssocClientNum_Type = Unsigned32
_CLApWlanStatsAssocClientNum_Object = MibTableColumn
cLApWlanStatsAssocClientNum = _CLApWlanStatsAssocClientNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 6),
    _CLApWlanStatsAssocClientNum_Type()
)
cLApWlanStatsAssocClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsAssocClientNum.setStatus("current")
_CLApWlanStatsOnlineUserNum_Type = Unsigned32
_CLApWlanStatsOnlineUserNum_Object = MibTableColumn
cLApWlanStatsOnlineUserNum = _CLApWlanStatsOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 9, 1, 1, 7),
    _CLApWlanStatsOnlineUserNum_Type()
)
cLApWlanStatsOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWlanStatsOnlineUserNum.setStatus("current")
_CiscoLwappApWlanInfo_ObjectIdentity = ObjectIdentity
ciscoLwappApWlanInfo = _CiscoLwappApWlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10)
)
_CLApWlanInfoTable_Object = MibTable
cLApWlanInfoTable = _CLApWlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cLApWlanInfoTable.setStatus("current")
_CLApWlanInfoEntry_Object = MibTableRow
cLApWlanInfoEntry = _CLApWlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 1, 1)
)
cLApWlanInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLApWlanInfoEntry.setStatus("current")


class _CLApWlanInfoMaxClients_Type(Unsigned32):
    """Custom type cLApWlanInfoMaxClients based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_CLApWlanInfoMaxClients_Type.__name__ = "Unsigned32"
_CLApWlanInfoMaxClients_Object = MibTableColumn
cLApWlanInfoMaxClients = _CLApWlanInfoMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 1, 1, 1),
    _CLApWlanInfoMaxClients_Type()
)
cLApWlanInfoMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApWlanInfoMaxClients.setStatus("current")
_CLApRadioWlanInfoTable_Object = MibTable
cLApRadioWlanInfoTable = _CLApRadioWlanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 2)
)
if mibBuilder.loadTexts:
    cLApRadioWlanInfoTable.setStatus("current")
_CLApRadioWlanInfoEntry_Object = MibTableRow
cLApRadioWlanInfoEntry = _CLApRadioWlanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 2, 1)
)
cLApRadioWlanInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLApRadioWlanInfoEntry.setStatus("current")
_CLApRadioWlanSsid_Type = SnmpAdminString
_CLApRadioWlanSsid_Object = MibTableColumn
cLApRadioWlanSsid = _CLApRadioWlanSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 2, 1, 1),
    _CLApRadioWlanSsid_Type()
)
cLApRadioWlanSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApRadioWlanSsid.setStatus("current")
_CLApRadioWlanBssid_Type = MacAddress
_CLApRadioWlanBssid_Object = MibTableColumn
cLApRadioWlanBssid = _CLApRadioWlanBssid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 10, 2, 1, 2),
    _CLApRadioWlanBssid_Type()
)
cLApRadioWlanBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApRadioWlanBssid.setStatus("current")
_CiscoLwappPacketDumpInfo_ObjectIdentity = ObjectIdentity
ciscoLwappPacketDumpInfo = _CiscoLwappPacketDumpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11)
)
_CLApPacketDumpFtpServerAddressType_Type = InetAddressType
_CLApPacketDumpFtpServerAddressType_Object = MibScalar
cLApPacketDumpFtpServerAddressType = _CLApPacketDumpFtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 1),
    _CLApPacketDumpFtpServerAddressType_Type()
)
cLApPacketDumpFtpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpFtpServerAddressType.setStatus("current")
_CLApPacketDumpFtpServerAddress_Type = InetAddress
_CLApPacketDumpFtpServerAddress_Object = MibScalar
cLApPacketDumpFtpServerAddress = _CLApPacketDumpFtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 2),
    _CLApPacketDumpFtpServerAddress_Type()
)
cLApPacketDumpFtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpFtpServerAddress.setStatus("current")
_CLApPacketDumpFtpServerPath_Type = SnmpAdminString
_CLApPacketDumpFtpServerPath_Object = MibScalar
cLApPacketDumpFtpServerPath = _CLApPacketDumpFtpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 3),
    _CLApPacketDumpFtpServerPath_Type()
)
cLApPacketDumpFtpServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpFtpServerPath.setStatus("current")
_CLApPacketDumpFtpUsername_Type = SnmpAdminString
_CLApPacketDumpFtpUsername_Object = MibScalar
cLApPacketDumpFtpUsername = _CLApPacketDumpFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 4),
    _CLApPacketDumpFtpUsername_Type()
)
cLApPacketDumpFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpFtpUsername.setStatus("current")
_CLApPacketDumpFtpPassword_Type = SnmpAdminString
_CLApPacketDumpFtpPassword_Object = MibScalar
cLApPacketDumpFtpPassword = _CLApPacketDumpFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 5),
    _CLApPacketDumpFtpPassword_Type()
)
cLApPacketDumpFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpFtpPassword.setStatus("current")


class _CLApPacketDumpClassifier_Type(Bits):
    """Custom type cLApPacketDumpClassifier based on Bits"""
    namedValues = NamedValues(
        *(("management", 0),
          ("data", 1),
          ("control", 2),
          ("dot1x", 3))
    )

_CLApPacketDumpClassifier_Type.__name__ = "Bits"
_CLApPacketDumpClassifier_Object = MibScalar
cLApPacketDumpClassifier = _CLApPacketDumpClassifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 6),
    _CLApPacketDumpClassifier_Type()
)
cLApPacketDumpClassifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpClassifier.setStatus("current")
_CLApPacketDumpBufferSize_Type = Unsigned32
_CLApPacketDumpBufferSize_Object = MibScalar
cLApPacketDumpBufferSize = _CLApPacketDumpBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 7),
    _CLApPacketDumpBufferSize_Type()
)
cLApPacketDumpBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpBufferSize.setStatus("current")
_CLApPacketDumpCaptureTime_Type = Unsigned32
_CLApPacketDumpCaptureTime_Object = MibScalar
cLApPacketDumpCaptureTime = _CLApPacketDumpCaptureTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 8),
    _CLApPacketDumpCaptureTime_Type()
)
cLApPacketDumpCaptureTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpCaptureTime.setStatus("current")
if mibBuilder.loadTexts:
    cLApPacketDumpCaptureTime.setUnits("minutes")
_CLApPacketDumpTruncation_Type = Unsigned32
_CLApPacketDumpTruncation_Object = MibScalar
cLApPacketDumpTruncation = _CLApPacketDumpTruncation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 9),
    _CLApPacketDumpTruncation_Type()
)
cLApPacketDumpTruncation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpTruncation.setStatus("current")
if mibBuilder.loadTexts:
    cLApPacketDumpTruncation.setUnits("bytes")
_CLApPacketDumpApName_Type = SnmpAdminString
_CLApPacketDumpApName_Object = MibScalar
cLApPacketDumpApName = _CLApPacketDumpApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 10),
    _CLApPacketDumpApName_Type()
)
cLApPacketDumpApName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpApName.setStatus("current")
_CLApPacketDumpDeviceMacAddress_Type = MacAddress
_CLApPacketDumpDeviceMacAddress_Object = MibScalar
cLApPacketDumpDeviceMacAddress = _CLApPacketDumpDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 11),
    _CLApPacketDumpDeviceMacAddress_Type()
)
cLApPacketDumpDeviceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpDeviceMacAddress.setStatus("current")


class _CLApPacketDumpStartStop_Type(Integer32):
    """Custom type cLApPacketDumpStartStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("none", 3))
    )


_CLApPacketDumpStartStop_Type.__name__ = "Integer32"
_CLApPacketDumpStartStop_Object = MibScalar
cLApPacketDumpStartStop = _CLApPacketDumpStartStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 11, 12),
    _CLApPacketDumpStartStop_Type()
)
cLApPacketDumpStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketDumpStartStop.setStatus("current")
_CiscoLwappAplanStats_ObjectIdentity = ObjectIdentity
ciscoLwappAplanStats = _CiscoLwappAplanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12)
)
_CLAplanStatsTable_Object = MibTable
cLAplanStatsTable = _CLAplanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cLAplanStatsTable.setStatus("current")
_CLAplanStatsEntry_Object = MibTableRow
cLAplanStatsEntry = _CLAplanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1)
)
cLAplanStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApLanPortId"),
)
if mibBuilder.loadTexts:
    cLAplanStatsEntry.setStatus("current")


class _CLApLanPortId_Type(Integer32):
    """Custom type cLApLanPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CLApLanPortId_Type.__name__ = "Integer32"
_CLApLanPortId_Object = MibTableColumn
cLApLanPortId = _CLApLanPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1, 1),
    _CLApLanPortId_Type()
)
cLApLanPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApLanPortId.setStatus("current")


class _CLApLanPortState_Type(TruthValue):
    """Custom type cLApLanPortState based on TruthValue"""
    defaultValue = 2


_CLApLanPortState_Type.__name__ = "TruthValue"
_CLApLanPortState_Object = MibTableColumn
cLApLanPortState = _CLApLanPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1, 2),
    _CLApLanPortState_Type()
)
cLApLanPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLanPortState.setStatus("current")


class _CLApLanPortVlanId_Type(Unsigned32):
    """Custom type cLApLanPortVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CLApLanPortVlanId_Type.__name__ = "Unsigned32"
_CLApLanPortVlanId_Object = MibTableColumn
cLApLanPortVlanId = _CLApLanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1, 3),
    _CLApLanPortVlanId_Type()
)
cLApLanPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLanPortVlanId.setStatus("current")


class _CLApLanPortVlanIdValid_Type(TruthValue):
    """Custom type cLApLanPortVlanIdValid based on TruthValue"""
    defaultValue = 2


_CLApLanPortVlanIdValid_Type.__name__ = "TruthValue"
_CLApLanPortVlanIdValid_Object = MibTableColumn
cLApLanPortVlanIdValid = _CLApLanPortVlanIdValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1, 4),
    _CLApLanPortVlanIdValid_Type()
)
cLApLanPortVlanIdValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApLanPortVlanIdValid.setStatus("current")


class _CLApLanPoeState_Type(TruthValue):
    """Custom type cLApLanPoeState based on TruthValue"""
    defaultValue = 2


_CLApLanPoeState_Type.__name__ = "TruthValue"
_CLApLanPoeState_Object = MibTableColumn
cLApLanPoeState = _CLApLanPoeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1, 5),
    _CLApLanPoeState_Type()
)
cLApLanPoeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLanPoeState.setStatus("current")


class _CLApLanPowerLevelId_Type(Unsigned32):
    """Custom type cLApLanPowerLevelId based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CLApLanPowerLevelId_Type.__name__ = "Unsigned32"
_CLApLanPowerLevelId_Object = MibTableColumn
cLApLanPowerLevelId = _CLApLanPowerLevelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 1, 1, 6),
    _CLApLanPowerLevelId_Type()
)
cLApLanPowerLevelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLanPowerLevelId.setStatus("current")
_CLAplanOverrideTable_Object = MibTable
cLAplanOverrideTable = _CLAplanOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 2)
)
if mibBuilder.loadTexts:
    cLAplanOverrideTable.setStatus("current")
_CLAplanOverrideEntry_Object = MibTableRow
cLAplanOverrideEntry = _CLAplanOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 2, 1)
)
cLAplanOverrideEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLAplanOverrideEntry.setStatus("current")


class _CLApLanOverride_Type(TruthValue):
    """Custom type cLApLanOverride based on TruthValue"""
    defaultValue = 2


_CLApLanOverride_Type.__name__ = "TruthValue"
_CLApLanOverride_Object = MibTableColumn
cLApLanOverride = _CLApLanOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 12, 2, 1, 1),
    _CLApLanOverride_Type()
)
cLApLanOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApLanOverride.setStatus("current")
_CiscoLwappApGlobalBleBeacon_ObjectIdentity = ObjectIdentity
ciscoLwappApGlobalBleBeacon = _CiscoLwappApGlobalBleBeacon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13)
)


class _CLHaloGlobalBleBeaconInterval_Type(Unsigned32):
    """Custom type cLHaloGlobalBleBeaconInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLHaloGlobalBleBeaconInterval_Type.__name__ = "Unsigned32"
_CLHaloGlobalBleBeaconInterval_Object = MibScalar
cLHaloGlobalBleBeaconInterval = _CLHaloGlobalBleBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 1),
    _CLHaloGlobalBleBeaconInterval_Type()
)
cLHaloGlobalBleBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconInterval.setUnits("Hz")
_CLHaloBleBeaconTable_Object = MibTable
cLHaloBleBeaconTable = _CLHaloBleBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 2)
)
if mibBuilder.loadTexts:
    cLHaloBleBeaconTable.setStatus("current")
_CLHaloBleBeaconEntry_Object = MibTableRow
cLHaloBleBeaconEntry = _CLHaloBleBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 2, 1)
)
cLHaloBleBeaconEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLHaloGlobalBleBeaconId"),
)
if mibBuilder.loadTexts:
    cLHaloBleBeaconEntry.setStatus("current")
_CLHaloGlobalBleBeaconId_Type = Unsigned32
_CLHaloGlobalBleBeaconId_Object = MibTableColumn
cLHaloGlobalBleBeaconId = _CLHaloGlobalBleBeaconId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 2, 1, 1),
    _CLHaloGlobalBleBeaconId_Type()
)
cLHaloGlobalBleBeaconId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconId.setStatus("current")


class _CLHaloGlobalBleBeaconUuid_Type(SnmpAdminString):
    """Custom type cLHaloGlobalBleBeaconUuid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLHaloGlobalBleBeaconUuid_Type.__name__ = "SnmpAdminString"
_CLHaloGlobalBleBeaconUuid_Object = MibTableColumn
cLHaloGlobalBleBeaconUuid = _CLHaloGlobalBleBeaconUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 2, 1, 2),
    _CLHaloGlobalBleBeaconUuid_Type()
)
cLHaloGlobalBleBeaconUuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconUuid.setStatus("current")


class _CLHaloGlobalBleBeaconTxPower_Type(Unsigned32):
    """Custom type cLHaloGlobalBleBeaconTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CLHaloGlobalBleBeaconTxPower_Type.__name__ = "Unsigned32"
_CLHaloGlobalBleBeaconTxPower_Object = MibTableColumn
cLHaloGlobalBleBeaconTxPower = _CLHaloGlobalBleBeaconTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 2, 1, 3),
    _CLHaloGlobalBleBeaconTxPower_Type()
)
cLHaloGlobalBleBeaconTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconTxPower.setUnits("dBm")
_CLHaloGlobalBleBeaconEnable_Type = TruthValue
_CLHaloGlobalBleBeaconEnable_Object = MibTableColumn
cLHaloGlobalBleBeaconEnable = _CLHaloGlobalBleBeaconEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 2, 1, 4),
    _CLHaloGlobalBleBeaconEnable_Type()
)
cLHaloGlobalBleBeaconEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaloGlobalBleBeaconEnable.setStatus("current")
_CLApBleBeaconTable_Object = MibTable
cLApBleBeaconTable = _CLApBleBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3)
)
if mibBuilder.loadTexts:
    cLApBleBeaconTable.setStatus("current")
_CLApBleBeaconEntry_Object = MibTableRow
cLApBleBeaconEntry = _CLApBleBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1)
)
cLApBleBeaconEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLHaloGlobalBleBeaconId"),
)
if mibBuilder.loadTexts:
    cLApBleBeaconEntry.setStatus("current")
_CLApBleBeaconMajorField_Type = Unsigned32
_CLApBleBeaconMajorField_Object = MibTableColumn
cLApBleBeaconMajorField = _CLApBleBeaconMajorField_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 1),
    _CLApBleBeaconMajorField_Type()
)
cLApBleBeaconMajorField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconMajorField.setStatus("current")
_CLApBleBeaconMinorField_Type = Unsigned32
_CLApBleBeaconMinorField_Object = MibTableColumn
cLApBleBeaconMinorField = _CLApBleBeaconMinorField_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 2),
    _CLApBleBeaconMinorField_Type()
)
cLApBleBeaconMinorField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconMinorField.setStatus("current")


class _CLApBleBeaconTxPower_Type(Unsigned32):
    """Custom type cLApBleBeaconTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CLApBleBeaconTxPower_Type.__name__ = "Unsigned32"
_CLApBleBeaconTxPower_Object = MibTableColumn
cLApBleBeaconTxPower = _CLApBleBeaconTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 3),
    _CLApBleBeaconTxPower_Type()
)
cLApBleBeaconTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cLApBleBeaconTxPower.setUnits("dBm")
_CLApBleBeaconStatus_Type = TruthValue
_CLApBleBeaconStatus_Object = MibTableColumn
cLApBleBeaconStatus = _CLApBleBeaconStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 4),
    _CLApBleBeaconStatus_Type()
)
cLApBleBeaconStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconStatus.setStatus("current")


class _CLApBleBeaconUuid_Type(SnmpAdminString):
    """Custom type cLApBleBeaconUuid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLApBleBeaconUuid_Type.__name__ = "SnmpAdminString"
_CLApBleBeaconUuid_Object = MibTableColumn
cLApBleBeaconUuid = _CLApBleBeaconUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 5),
    _CLApBleBeaconUuid_Type()
)
cLApBleBeaconUuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconUuid.setStatus("current")


class _CLApBleBeaconInterval_Type(Unsigned32):
    """Custom type cLApBleBeaconInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLApBleBeaconInterval_Type.__name__ = "Unsigned32"
_CLApBleBeaconInterval_Object = MibTableColumn
cLApBleBeaconInterval = _CLApBleBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 6),
    _CLApBleBeaconInterval_Type()
)
cLApBleBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLApBleBeaconInterval.setUnits("Hz")


class _CLApBleBeaconApplyGlobal_Type(TruthValue):
    """Custom type cLApBleBeaconApplyGlobal based on TruthValue"""
    defaultValue = 2


_CLApBleBeaconApplyGlobal_Type.__name__ = "TruthValue"
_CLApBleBeaconApplyGlobal_Object = MibTableColumn
cLApBleBeaconApplyGlobal = _CLApBleBeaconApplyGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 7),
    _CLApBleBeaconApplyGlobal_Type()
)
cLApBleBeaconApplyGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconApplyGlobal.setStatus("current")


class _CLApBleBeaconAdvTxPower_Type(Unsigned32):
    """Custom type cLApBleBeaconAdvTxPower based on Unsigned32"""
    defaultValue = 59

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_CLApBleBeaconAdvTxPower_Type.__name__ = "Unsigned32"
_CLApBleBeaconAdvTxPower_Object = MibTableColumn
cLApBleBeaconAdvTxPower = _CLApBleBeaconAdvTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 13, 3, 1, 8),
    _CLApBleBeaconAdvTxPower_Type()
)
cLApBleBeaconAdvTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApBleBeaconAdvTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cLApBleBeaconAdvTxPower.setUnits("Hz")
_CiscoLwappApHyperlocation_ObjectIdentity = ObjectIdentity
ciscoLwappApHyperlocation = _CiscoLwappApHyperlocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 14)
)
_CLApHyperlocationTable_Object = MibTable
cLApHyperlocationTable = _CLApHyperlocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cLApHyperlocationTable.setStatus("current")
_CLApHyperlocationEntry_Object = MibTableRow
cLApHyperlocationEntry = _CLApHyperlocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 14, 1, 1)
)
cLApHyperlocationEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApHyperlocationEntry.setStatus("current")
_CLApHyperlocationAdminState_Type = TruthValue
_CLApHyperlocationAdminState_Object = MibTableColumn
cLApHyperlocationAdminState = _CLApHyperlocationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 14, 1, 1, 1),
    _CLApHyperlocationAdminState_Type()
)
cLApHyperlocationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApHyperlocationAdminState.setStatus("current")
_CLApHyperlocationUnsetFlag_Type = TruthValue
_CLApHyperlocationUnsetFlag_Object = MibTableColumn
cLApHyperlocationUnsetFlag = _CLApHyperlocationUnsetFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 14, 1, 1, 2),
    _CLApHyperlocationUnsetFlag_Type()
)
cLApHyperlocationUnsetFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApHyperlocationUnsetFlag.setStatus("current")
_CiscoLwappApSecureCipher_ObjectIdentity = ObjectIdentity
ciscoLwappApSecureCipher = _CiscoLwappApSecureCipher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 15)
)


class _CLApSecureCipher_Type(Integer32):
    """Custom type cLApSecureCipher based on Integer32"""
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
          ("aes256sha1", 2),
          ("aes256sha2", 3))
    )


_CLApSecureCipher_Type.__name__ = "Integer32"
_CLApSecureCipher_Object = MibScalar
cLApSecureCipher = _CLApSecureCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 15, 1),
    _CLApSecureCipher_Type()
)
cLApSecureCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApSecureCipher.setStatus("current")
_CiscoLwappApProfile_ObjectIdentity = ObjectIdentity
ciscoLwappApProfile = _CiscoLwappApProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16)
)
_CLApProfileTable_Object = MibTable
cLApProfileTable = _CLApProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cLApProfileTable.setStatus("current")
_CLApProfileEntry_Object = MibTableRow
cLApProfileEntry = _CLApProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1)
)
cLApProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileName"),
)
if mibBuilder.loadTexts:
    cLApProfileEntry.setStatus("current")


class _CLApProfileName_Type(SnmpAdminString):
    """Custom type cLApProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileName_Type.__name__ = "SnmpAdminString"
_CLApProfileName_Object = MibTableColumn
cLApProfileName = _CLApProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 1),
    _CLApProfileName_Type()
)
cLApProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApProfileName.setStatus("current")
_CLApProfileRowStatus_Type = RowStatus
_CLApProfileRowStatus_Object = MibTableColumn
cLApProfileRowStatus = _CLApProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 2),
    _CLApProfileRowStatus_Type()
)
cLApProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileRowStatus.setStatus("current")


class _CLApProfileCredentialGlobalUserName_Type(SnmpAdminString):
    """Custom type cLApProfileCredentialGlobalUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileCredentialGlobalUserName_Type.__name__ = "SnmpAdminString"
_CLApProfileCredentialGlobalUserName_Object = MibTableColumn
cLApProfileCredentialGlobalUserName = _CLApProfileCredentialGlobalUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 3),
    _CLApProfileCredentialGlobalUserName_Type()
)
cLApProfileCredentialGlobalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCredentialGlobalUserName.setStatus("current")


class _CLApProfileCredentialGlobalPassword_Type(SnmpAdminString):
    """Custom type cLApProfileCredentialGlobalPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileCredentialGlobalPassword_Type.__name__ = "SnmpAdminString"
_CLApProfileCredentialGlobalPassword_Object = MibTableColumn
cLApProfileCredentialGlobalPassword = _CLApProfileCredentialGlobalPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 4),
    _CLApProfileCredentialGlobalPassword_Type()
)
cLApProfileCredentialGlobalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCredentialGlobalPassword.setStatus("current")


class _CLApProfileCredentialGlobalSecret_Type(SnmpAdminString):
    """Custom type cLApProfileCredentialGlobalSecret based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileCredentialGlobalSecret_Type.__name__ = "SnmpAdminString"
_CLApProfileCredentialGlobalSecret_Object = MibTableColumn
cLApProfileCredentialGlobalSecret = _CLApProfileCredentialGlobalSecret_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 5),
    _CLApProfileCredentialGlobalSecret_Type()
)
cLApProfileCredentialGlobalSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCredentialGlobalSecret.setStatus("current")
_CLApProfileCredentialEnableGlobalCredentials_Type = TruthValue
_CLApProfileCredentialEnableGlobalCredentials_Object = MibTableColumn
cLApProfileCredentialEnableGlobalCredentials = _CLApProfileCredentialEnableGlobalCredentials_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 6),
    _CLApProfileCredentialEnableGlobalCredentials_Type()
)
cLApProfileCredentialEnableGlobalCredentials.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileCredentialEnableGlobalCredentials.setStatus("deprecated")


class _CLApProfileLinkLatencyEnable_Type(Integer32):
    """Custom type cLApProfileLinkLatencyEnable based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("data", 3),
          ("reset", 4))
    )


_CLApProfileLinkLatencyEnable_Type.__name__ = "Integer32"
_CLApProfileLinkLatencyEnable_Object = MibTableColumn
cLApProfileLinkLatencyEnable = _CLApProfileLinkLatencyEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 7),
    _CLApProfileLinkLatencyEnable_Type()
)
cLApProfileLinkLatencyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileLinkLatencyEnable.setStatus("current")


class _CLApProfileHaloBleBeaconInterval_Type(Unsigned32):
    """Custom type cLApProfileHaloBleBeaconInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLApProfileHaloBleBeaconInterval_Type.__name__ = "Unsigned32"
_CLApProfileHaloBleBeaconInterval_Object = MibTableColumn
cLApProfileHaloBleBeaconInterval = _CLApProfileHaloBleBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 8),
    _CLApProfileHaloBleBeaconInterval_Type()
)
cLApProfileHaloBleBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconInterval.setUnits("Hz")


class _CLApProfileFastHbTimerTimeout_Type(Unsigned32):
    """Custom type cLApProfileFastHbTimerTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLApProfileFastHbTimerTimeout_Type.__name__ = "Unsigned32"
_CLApProfileFastHbTimerTimeout_Object = MibTableColumn
cLApProfileFastHbTimerTimeout = _CLApProfileFastHbTimerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 12),
    _CLApProfileFastHbTimerTimeout_Type()
)
cLApProfileFastHbTimerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileFastHbTimerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileFastHbTimerTimeout.setUnits("seconds")
_CLApProfileFastHbTimerEnabled_Type = TruthValue
_CLApProfileFastHbTimerEnabled_Object = MibTableColumn
cLApProfileFastHbTimerEnabled = _CLApProfileFastHbTimerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 13),
    _CLApProfileFastHbTimerEnabled_Type()
)
cLApProfileFastHbTimerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileFastHbTimerEnabled.setStatus("deprecated")


class _CLApProfilePrimaryDiscoveryTimeout_Type(Unsigned32):
    """Custom type cLApProfilePrimaryDiscoveryTimeout based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3000),
    )


_CLApProfilePrimaryDiscoveryTimeout_Type.__name__ = "Unsigned32"
_CLApProfilePrimaryDiscoveryTimeout_Object = MibTableColumn
cLApProfilePrimaryDiscoveryTimeout = _CLApProfilePrimaryDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 14),
    _CLApProfilePrimaryDiscoveryTimeout_Type()
)
cLApProfilePrimaryDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePrimaryDiscoveryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfilePrimaryDiscoveryTimeout.setUnits("seconds")
_CLApProfileBackupPrimaryControllerAddressType_Type = InetAddressType
_CLApProfileBackupPrimaryControllerAddressType_Object = MibTableColumn
cLApProfileBackupPrimaryControllerAddressType = _CLApProfileBackupPrimaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 15),
    _CLApProfileBackupPrimaryControllerAddressType_Type()
)
cLApProfileBackupPrimaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupPrimaryControllerAddressType.setStatus("current")
_CLApProfileBackupPrimaryControllerAddress_Type = InetAddress
_CLApProfileBackupPrimaryControllerAddress_Object = MibTableColumn
cLApProfileBackupPrimaryControllerAddress = _CLApProfileBackupPrimaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 16),
    _CLApProfileBackupPrimaryControllerAddress_Type()
)
cLApProfileBackupPrimaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupPrimaryControllerAddress.setStatus("current")


class _CLApProfileBackupPrimaryControllerName_Type(SnmpAdminString):
    """Custom type cLApProfileBackupPrimaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileBackupPrimaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApProfileBackupPrimaryControllerName_Object = MibTableColumn
cLApProfileBackupPrimaryControllerName = _CLApProfileBackupPrimaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 17),
    _CLApProfileBackupPrimaryControllerName_Type()
)
cLApProfileBackupPrimaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupPrimaryControllerName.setStatus("current")
_CLApProfileBackupSecondaryControllerAddressType_Type = InetAddressType
_CLApProfileBackupSecondaryControllerAddressType_Object = MibTableColumn
cLApProfileBackupSecondaryControllerAddressType = _CLApProfileBackupSecondaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 18),
    _CLApProfileBackupSecondaryControllerAddressType_Type()
)
cLApProfileBackupSecondaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupSecondaryControllerAddressType.setStatus("current")
_CLApProfileBackupSecondaryControllerAddress_Type = InetAddress
_CLApProfileBackupSecondaryControllerAddress_Object = MibTableColumn
cLApProfileBackupSecondaryControllerAddress = _CLApProfileBackupSecondaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 19),
    _CLApProfileBackupSecondaryControllerAddress_Type()
)
cLApProfileBackupSecondaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupSecondaryControllerAddress.setStatus("current")


class _CLApProfileBackupSecondaryControllerName_Type(SnmpAdminString):
    """Custom type cLApProfileBackupSecondaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileBackupSecondaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApProfileBackupSecondaryControllerName_Object = MibTableColumn
cLApProfileBackupSecondaryControllerName = _CLApProfileBackupSecondaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 20),
    _CLApProfileBackupSecondaryControllerName_Type()
)
cLApProfileBackupSecondaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupSecondaryControllerName.setStatus("current")
_CLApProfileBackupTertiaryControllerAddressType_Type = InetAddressType
_CLApProfileBackupTertiaryControllerAddressType_Object = MibTableColumn
cLApProfileBackupTertiaryControllerAddressType = _CLApProfileBackupTertiaryControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 21),
    _CLApProfileBackupTertiaryControllerAddressType_Type()
)
cLApProfileBackupTertiaryControllerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupTertiaryControllerAddressType.setStatus("current")
_CLApProfileBackupTertiaryControllerAddress_Type = InetAddress
_CLApProfileBackupTertiaryControllerAddress_Object = MibTableColumn
cLApProfileBackupTertiaryControllerAddress = _CLApProfileBackupTertiaryControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 22),
    _CLApProfileBackupTertiaryControllerAddress_Type()
)
cLApProfileBackupTertiaryControllerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupTertiaryControllerAddress.setStatus("current")


class _CLApProfileBackupTertiaryControllerName_Type(SnmpAdminString):
    """Custom type cLApProfileBackupTertiaryControllerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileBackupTertiaryControllerName_Type.__name__ = "SnmpAdminString"
_CLApProfileBackupTertiaryControllerName_Object = MibTableColumn
cLApProfileBackupTertiaryControllerName = _CLApProfileBackupTertiaryControllerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 23),
    _CLApProfileBackupTertiaryControllerName_Type()
)
cLApProfileBackupTertiaryControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupTertiaryControllerName.setStatus("current")


class _CLApProfileTcpMss_Type(Unsigned32):
    """Custom type cLApProfileTcpMss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(536, 1363),
    )


_CLApProfileTcpMss_Type.__name__ = "Unsigned32"
_CLApProfileTcpMss_Object = MibTableColumn
cLApProfileTcpMss = _CLApProfileTcpMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 25),
    _CLApProfileTcpMss_Type()
)
cLApProfileTcpMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileTcpMss.setStatus("current")


class _CLApProfileRetransmitCount_Type(Unsigned32):
    """Custom type cLApProfileRetransmitCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_CLApProfileRetransmitCount_Type.__name__ = "Unsigned32"
_CLApProfileRetransmitCount_Object = MibTableColumn
cLApProfileRetransmitCount = _CLApProfileRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 26),
    _CLApProfileRetransmitCount_Type()
)
cLApProfileRetransmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRetransmitCount.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileRetransmitCount.setUnits("retries")


class _CLApProfileRetransmitTimeout_Type(Unsigned32):
    """Custom type cLApProfileRetransmitTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_CLApProfileRetransmitTimeout_Type.__name__ = "Unsigned32"
_CLApProfileRetransmitTimeout_Object = MibTableColumn
cLApProfileRetransmitTimeout = _CLApProfileRetransmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 27),
    _CLApProfileRetransmitTimeout_Type()
)
cLApProfileRetransmitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRetransmitTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileRetransmitTimeout.setUnits("seconds")
_CLApProfileOeapDisableLocalAccess_Type = TruthValue
_CLApProfileOeapDisableLocalAccess_Object = MibTableColumn
cLApProfileOeapDisableLocalAccess = _CLApProfileOeapDisableLocalAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 28),
    _CLApProfileOeapDisableLocalAccess_Type()
)
cLApProfileOeapDisableLocalAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileOeapDisableLocalAccess.setStatus("deprecated")
_CLApProfileLedState_Type = TruthValue
_CLApProfileLedState_Object = MibTableColumn
cLApProfileLedState = _CLApProfileLedState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 29),
    _CLApProfileLedState_Type()
)
cLApProfileLedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileLedState.setStatus("current")
_CLApProfileRadioInterfaceShutdownEnabled_Type = TruthValue
_CLApProfileRadioInterfaceShutdownEnabled_Object = MibTableColumn
cLApProfileRadioInterfaceShutdownEnabled = _CLApProfileRadioInterfaceShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 30),
    _CLApProfileRadioInterfaceShutdownEnabled_Type()
)
cLApProfileRadioInterfaceShutdownEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRadioInterfaceShutdownEnabled.setStatus("deprecated")
_CLApProfileEthernetInterfaceDowntime_Type = Unsigned32
_CLApProfileEthernetInterfaceDowntime_Object = MibTableColumn
cLApProfileEthernetInterfaceDowntime = _CLApProfileEthernetInterfaceDowntime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 31),
    _CLApProfileEthernetInterfaceDowntime_Type()
)
cLApProfileEthernetInterfaceDowntime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileEthernetInterfaceDowntime.setStatus("deprecated")
if mibBuilder.loadTexts:
    cLApProfileEthernetInterfaceDowntime.setUnits("Seconds")
_CLApProfileMulticastGroupAddressType_Type = InetAddressType
_CLApProfileMulticastGroupAddressType_Object = MibTableColumn
cLApProfileMulticastGroupAddressType = _CLApProfileMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 32),
    _CLApProfileMulticastGroupAddressType_Type()
)
cLApProfileMulticastGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileMulticastGroupAddressType.setStatus("current")
_CLApProfileMulticastGroupAddress_Type = InetAddress
_CLApProfileMulticastGroupAddress_Object = MibTableColumn
cLApProfileMulticastGroupAddress = _CLApProfileMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 33),
    _CLApProfileMulticastGroupAddress_Type()
)
cLApProfileMulticastGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileMulticastGroupAddress.setStatus("current")


class _CLApProfileMulticastMode_Type(Integer32):
    """Custom type cLApProfileMulticastMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_CLApProfileMulticastMode_Type.__name__ = "Integer32"
_CLApProfileMulticastMode_Object = MibTableColumn
cLApProfileMulticastMode = _CLApProfileMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 34),
    _CLApProfileMulticastMode_Type()
)
cLApProfileMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileMulticastMode.setStatus("current")


class _CLApProfilePrimedJoinTimeout_Type(Unsigned32):
    """Custom type cLApProfilePrimedJoinTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 43200),
    )


_CLApProfilePrimedJoinTimeout_Type.__name__ = "Unsigned32"
_CLApProfilePrimedJoinTimeout_Object = MibTableColumn
cLApProfilePrimedJoinTimeout = _CLApProfilePrimedJoinTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 35),
    _CLApProfilePrimedJoinTimeout_Type()
)
cLApProfilePrimedJoinTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePrimedJoinTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfilePrimedJoinTimeout.setUnits("seconds")


class _CLApProfilePreferMode_Type(Integer32):
    """Custom type cLApProfilePreferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unconfig", 1),
          ("ipv4", 2),
          ("ipv6", 3))
    )


_CLApProfilePreferMode_Type.__name__ = "Integer32"
_CLApProfilePreferMode_Object = MibTableColumn
cLApProfilePreferMode = _CLApProfilePreferMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 36),
    _CLApProfilePreferMode_Type()
)
cLApProfilePreferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePreferMode.setStatus("current")
_CLApProfileApLagEnabled_Type = TruthValue
_CLApProfileApLagEnabled_Object = MibTableColumn
cLApProfileApLagEnabled = _CLApProfileApLagEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 37),
    _CLApProfileApLagEnabled_Type()
)
cLApProfileApLagEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileApLagEnabled.setStatus("current")


class _CLApProfile802dot1xAuthenticationEnabled_Type(TruthValue):
    """Custom type cLApProfile802dot1xAuthenticationEnabled based on TruthValue"""
    defaultValue = 2


_CLApProfile802dot1xAuthenticationEnabled_Type.__name__ = "TruthValue"
_CLApProfile802dot1xAuthenticationEnabled_Object = MibTableColumn
cLApProfile802dot1xAuthenticationEnabled = _CLApProfile802dot1xAuthenticationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 38),
    _CLApProfile802dot1xAuthenticationEnabled_Type()
)
cLApProfile802dot1xAuthenticationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfile802dot1xAuthenticationEnabled.setStatus("deprecated")


class _CLApProfile802dot1xSupplicantUsername_Type(SnmpAdminString):
    """Custom type cLApProfile802dot1xSupplicantUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfile802dot1xSupplicantUsername_Type.__name__ = "SnmpAdminString"
_CLApProfile802dot1xSupplicantUsername_Object = MibTableColumn
cLApProfile802dot1xSupplicantUsername = _CLApProfile802dot1xSupplicantUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 39),
    _CLApProfile802dot1xSupplicantUsername_Type()
)
cLApProfile802dot1xSupplicantUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfile802dot1xSupplicantUsername.setStatus("current")


class _CLApProfile802dot1xSupplicantPassword_Type(SnmpAdminString):
    """Custom type cLApProfile802dot1xSupplicantPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfile802dot1xSupplicantPassword_Type.__name__ = "SnmpAdminString"
_CLApProfile802dot1xSupplicantPassword_Object = MibTableColumn
cLApProfile802dot1xSupplicantPassword = _CLApProfile802dot1xSupplicantPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 40),
    _CLApProfile802dot1xSupplicantPassword_Type()
)
cLApProfile802dot1xSupplicantPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfile802dot1xSupplicantPassword.setStatus("current")


class _CLApProfileEncryptionEnable_Type(TruthValue):
    """Custom type cLApProfileEncryptionEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileEncryptionEnable_Type.__name__ = "TruthValue"
_CLApProfileEncryptionEnable_Object = MibTableColumn
cLApProfileEncryptionEnable = _CLApProfileEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 41),
    _CLApProfileEncryptionEnable_Type()
)
cLApProfileEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileEncryptionEnable.setStatus("current")


class _CLApProfileTelnetEnable_Type(TruthValue):
    """Custom type cLApProfileTelnetEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileTelnetEnable_Type.__name__ = "TruthValue"
_CLApProfileTelnetEnable_Object = MibTableColumn
cLApProfileTelnetEnable = _CLApProfileTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 42),
    _CLApProfileTelnetEnable_Type()
)
cLApProfileTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileTelnetEnable.setStatus("current")


class _CLApProfileSshEnable_Type(TruthValue):
    """Custom type cLApProfileSshEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileSshEnable_Type.__name__ = "TruthValue"
_CLApProfileSshEnable_Object = MibTableColumn
cLApProfileSshEnable = _CLApProfileSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 43),
    _CLApProfileSshEnable_Type()
)
cLApProfileSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileSshEnable.setStatus("current")


class _CLApProfileHyperlocationEnable_Type(TruthValue):
    """Custom type cLApProfileHyperlocationEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileHyperlocationEnable_Type.__name__ = "TruthValue"
_CLApProfileHyperlocationEnable_Object = MibTableColumn
cLApProfileHyperlocationEnable = _CLApProfileHyperlocationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 44),
    _CLApProfileHyperlocationEnable_Type()
)
cLApProfileHyperlocationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationEnable.setStatus("current")


class _CLApProfileHyperlocationDetectionThreshold_Type(Integer32):
    """Custom type cLApProfileHyperlocationDetectionThreshold based on Integer32"""
    defaultValue = -100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -50),
    )


_CLApProfileHyperlocationDetectionThreshold_Type.__name__ = "Integer32"
_CLApProfileHyperlocationDetectionThreshold_Object = MibTableColumn
cLApProfileHyperlocationDetectionThreshold = _CLApProfileHyperlocationDetectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 45),
    _CLApProfileHyperlocationDetectionThreshold_Type()
)
cLApProfileHyperlocationDetectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationDetectionThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationDetectionThreshold.setUnits("dBm")


class _CLApProfileHyperlocationResetThreshold_Type(Unsigned32):
    """Custom type cLApProfileHyperlocationResetThreshold based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CLApProfileHyperlocationResetThreshold_Type.__name__ = "Unsigned32"
_CLApProfileHyperlocationResetThreshold_Object = MibTableColumn
cLApProfileHyperlocationResetThreshold = _CLApProfileHyperlocationResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 46),
    _CLApProfileHyperlocationResetThreshold_Type()
)
cLApProfileHyperlocationResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationResetThreshold.setStatus("current")


class _CLApProfileHyperlocationTriggerThreshold_Type(Unsigned32):
    """Custom type cLApProfileHyperlocationTriggerThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLApProfileHyperlocationTriggerThreshold_Type.__name__ = "Unsigned32"
_CLApProfileHyperlocationTriggerThreshold_Object = MibTableColumn
cLApProfileHyperlocationTriggerThreshold = _CLApProfileHyperlocationTriggerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 47),
    _CLApProfileHyperlocationTriggerThreshold_Type()
)
cLApProfileHyperlocationTriggerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationTriggerThreshold.setStatus("current")
_CLApProfileHyperlocationNtpIpAddressType_Type = InetAddressType
_CLApProfileHyperlocationNtpIpAddressType_Object = MibTableColumn
cLApProfileHyperlocationNtpIpAddressType = _CLApProfileHyperlocationNtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 48),
    _CLApProfileHyperlocationNtpIpAddressType_Type()
)
cLApProfileHyperlocationNtpIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationNtpIpAddressType.setStatus("current")
_CLApProfileHyperlocationNtpIpAddress_Type = InetAddress
_CLApProfileHyperlocationNtpIpAddress_Object = MibTableColumn
cLApProfileHyperlocationNtpIpAddress = _CLApProfileHyperlocationNtpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 49),
    _CLApProfileHyperlocationNtpIpAddress_Type()
)
cLApProfileHyperlocationNtpIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHyperlocationNtpIpAddress.setStatus("current")


class _CLApProfileAdjustMss_Type(TruthValue):
    """Custom type cLApProfileAdjustMss based on TruthValue"""
    defaultValue = 2


_CLApProfileAdjustMss_Type.__name__ = "TruthValue"
_CLApProfileAdjustMss_Object = MibTableColumn
cLApProfileAdjustMss = _CLApProfileAdjustMss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 50),
    _CLApProfileAdjustMss_Type()
)
cLApProfileAdjustMss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileAdjustMss.setStatus("current")


class _CLApProfileDiscoveryTimeout_Type(Unsigned32):
    """Custom type cLApProfileDiscoveryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CLApProfileDiscoveryTimeout_Type.__name__ = "Unsigned32"
_CLApProfileDiscoveryTimeout_Object = MibTableColumn
cLApProfileDiscoveryTimeout = _CLApProfileDiscoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 51),
    _CLApProfileDiscoveryTimeout_Type()
)
cLApProfileDiscoveryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileDiscoveryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileDiscoveryTimeout.setUnits("seconds")


class _CLApProfileHeartBeatTimeout_Type(Unsigned32):
    """Custom type cLApProfileHeartBeatTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CLApProfileHeartBeatTimeout_Type.__name__ = "Unsigned32"
_CLApProfileHeartBeatTimeout_Object = MibTableColumn
cLApProfileHeartBeatTimeout = _CLApProfileHeartBeatTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 52),
    _CLApProfileHeartBeatTimeout_Type()
)
cLApProfileHeartBeatTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHeartBeatTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileHeartBeatTimeout.setUnits("seconds")


class _CLApProfileCdpEnable_Type(TruthValue):
    """Custom type cLApProfileCdpEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileCdpEnable_Type.__name__ = "TruthValue"
_CLApProfileCdpEnable_Object = MibTableColumn
cLApProfileCdpEnable = _CLApProfileCdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 53),
    _CLApProfileCdpEnable_Type()
)
cLApProfileCdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCdpEnable.setStatus("current")


class _CLApProfileApPacketCaptureProfile_Type(SnmpAdminString):
    """Custom type cLApProfileApPacketCaptureProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileApPacketCaptureProfile_Type.__name__ = "SnmpAdminString"
_CLApProfileApPacketCaptureProfile_Object = MibTableColumn
cLApProfileApPacketCaptureProfile = _CLApProfileApPacketCaptureProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 54),
    _CLApProfileApPacketCaptureProfile_Type()
)
cLApProfileApPacketCaptureProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileApPacketCaptureProfile.setStatus("current")


class _CLApProfileRogueReportInterval_Type(Unsigned32):
    """Custom type cLApProfileRogueReportInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CLApProfileRogueReportInterval_Type.__name__ = "Unsigned32"
_CLApProfileRogueReportInterval_Object = MibTableColumn
cLApProfileRogueReportInterval = _CLApProfileRogueReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 55),
    _CLApProfileRogueReportInterval_Type()
)
cLApProfileRogueReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRogueReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileRogueReportInterval.setUnits("seconds")


class _CLApProfileRogueMinimumRssi_Type(Integer32):
    """Custom type cLApProfileRogueMinimumRssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, -70),
    )


_CLApProfileRogueMinimumRssi_Type.__name__ = "Integer32"
_CLApProfileRogueMinimumRssi_Object = MibTableColumn
cLApProfileRogueMinimumRssi = _CLApProfileRogueMinimumRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 56),
    _CLApProfileRogueMinimumRssi_Type()
)
cLApProfileRogueMinimumRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRogueMinimumRssi.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileRogueMinimumRssi.setUnits("dBm")


class _CLApProfileRogueTransientInterval_Type(Unsigned32):
    """Custom type cLApProfileRogueTransientInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(120, 1800),
    )


_CLApProfileRogueTransientInterval_Type.__name__ = "Unsigned32"
_CLApProfileRogueTransientInterval_Object = MibTableColumn
cLApProfileRogueTransientInterval = _CLApProfileRogueTransientInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 57),
    _CLApProfileRogueTransientInterval_Type()
)
cLApProfileRogueTransientInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRogueTransientInterval.setStatus("current")


class _CLApProfileRogueContainFlexconnect_Type(TruthValue):
    """Custom type cLApProfileRogueContainFlexconnect based on TruthValue"""
    defaultValue = 2


_CLApProfileRogueContainFlexconnect_Type.__name__ = "TruthValue"
_CLApProfileRogueContainFlexconnect_Object = MibTableColumn
cLApProfileRogueContainFlexconnect = _CLApProfileRogueContainFlexconnect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 58),
    _CLApProfileRogueContainFlexconnect_Type()
)
cLApProfileRogueContainFlexconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRogueContainFlexconnect.setStatus("current")


class _CLApProfileRogueContainAutoRateEnable_Type(TruthValue):
    """Custom type cLApProfileRogueContainAutoRateEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileRogueContainAutoRateEnable_Type.__name__ = "TruthValue"
_CLApProfileRogueContainAutoRateEnable_Object = MibTableColumn
cLApProfileRogueContainAutoRateEnable = _CLApProfileRogueContainAutoRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 59),
    _CLApProfileRogueContainAutoRateEnable_Type()
)
cLApProfileRogueContainAutoRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRogueContainAutoRateEnable.setStatus("current")


class _CLApProfileRogueDetectionEnable_Type(TruthValue):
    """Custom type cLApProfileRogueDetectionEnable based on TruthValue"""
    defaultValue = 1


_CLApProfileRogueDetectionEnable_Type.__name__ = "TruthValue"
_CLApProfileRogueDetectionEnable_Object = MibTableColumn
cLApProfileRogueDetectionEnable = _CLApProfileRogueDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 60),
    _CLApProfileRogueDetectionEnable_Type()
)
cLApProfileRogueDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileRogueDetectionEnable.setStatus("current")


class _CLApProfileReportInterval24ghz_Type(Integer32):
    """Custom type cLApProfileReportInterval24ghz based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 90),
    )


_CLApProfileReportInterval24ghz_Type.__name__ = "Integer32"
_CLApProfileReportInterval24ghz_Object = MibTableColumn
cLApProfileReportInterval24ghz = _CLApProfileReportInterval24ghz_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 61),
    _CLApProfileReportInterval24ghz_Type()
)
cLApProfileReportInterval24ghz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileReportInterval24ghz.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileReportInterval24ghz.setUnits("seconds")


class _CLApProfileReportInterval5ghz_Type(Integer32):
    """Custom type cLApProfileReportInterval5ghz based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 90),
    )


_CLApProfileReportInterval5ghz_Type.__name__ = "Integer32"
_CLApProfileReportInterval5ghz_Object = MibTableColumn
cLApProfileReportInterval5ghz = _CLApProfileReportInterval5ghz_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 62),
    _CLApProfileReportInterval5ghz_Type()
)
cLApProfileReportInterval5ghz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileReportInterval5ghz.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileReportInterval5ghz.setUnits("seconds")


class _CLApProfileDot1xApSwitchEapAuth_Type(Integer32):
    """Custom type cLApProfileDot1xApSwitchEapAuth based on Integer32"""
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
        *(("eapNone", 1),
          ("eapFast", 2),
          ("eapTls", 3),
          ("peap", 4))
    )


_CLApProfileDot1xApSwitchEapAuth_Type.__name__ = "Integer32"
_CLApProfileDot1xApSwitchEapAuth_Object = MibTableColumn
cLApProfileDot1xApSwitchEapAuth = _CLApProfileDot1xApSwitchEapAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 63),
    _CLApProfileDot1xApSwitchEapAuth_Type()
)
cLApProfileDot1xApSwitchEapAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileDot1xApSwitchEapAuth.setStatus("current")


class _CLApProfileDot1xApSwtichLscAuth_Type(Integer32):
    """Custom type cLApProfileDot1xApSwtichLscAuth based on Integer32"""
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
        *(("authNone", 1),
          ("authCapwapDtls", 2),
          ("authDot1xPort", 3),
          ("authBoth", 4))
    )


_CLApProfileDot1xApSwtichLscAuth_Type.__name__ = "Integer32"
_CLApProfileDot1xApSwtichLscAuth_Object = MibTableColumn
cLApProfileDot1xApSwtichLscAuth = _CLApProfileDot1xApSwtichLscAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 64),
    _CLApProfileDot1xApSwtichLscAuth_Type()
)
cLApProfileDot1xApSwtichLscAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileDot1xApSwtichLscAuth.setStatus("current")


class _CLApProfileMeshProfileName_Type(SnmpAdminString):
    """Custom type cLApProfileMeshProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApProfileMeshProfileName_Type.__name__ = "SnmpAdminString"
_CLApProfileMeshProfileName_Object = MibTableColumn
cLApProfileMeshProfileName = _CLApProfileMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 65),
    _CLApProfileMeshProfileName_Type()
)
cLApProfileMeshProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileMeshProfileName.setStatus("current")


class _CLApProfileUsbStatus_Type(TruthValue):
    """Custom type cLApProfileUsbStatus based on TruthValue"""
    defaultValue = 1


_CLApProfileUsbStatus_Type.__name__ = "TruthValue"
_CLApProfileUsbStatus_Object = MibTableColumn
cLApProfileUsbStatus = _CLApProfileUsbStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 66),
    _CLApProfileUsbStatus_Type()
)
cLApProfileUsbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileUsbStatus.setStatus("current")


class _CLApProfileVlanTagging_Type(TruthValue):
    """Custom type cLApProfileVlanTagging based on TruthValue"""
    defaultValue = 2


_CLApProfileVlanTagging_Type.__name__ = "TruthValue"
_CLApProfileVlanTagging_Object = MibTableColumn
cLApProfileVlanTagging = _CLApProfileVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 67),
    _CLApProfileVlanTagging_Type()
)
cLApProfileVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileVlanTagging.setStatus("deprecated")


class _CLApProfileApCountryCode_Type(SnmpAdminString):
    """Custom type cLApProfileApCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileApCountryCode_Type.__name__ = "SnmpAdminString"
_CLApProfileApCountryCode_Object = MibTableColumn
cLApProfileApCountryCode = _CLApProfileApCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 68),
    _CLApProfileApCountryCode_Type()
)
cLApProfileApCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileApCountryCode.setStatus("deprecated")
_CLApProfileExtModuleEnable_Type = TruthValue
_CLApProfileExtModuleEnable_Object = MibTableColumn
cLApProfileExtModuleEnable = _CLApProfileExtModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 69),
    _CLApProfileExtModuleEnable_Type()
)
cLApProfileExtModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileExtModuleEnable.setStatus("current")


class _CLApProfileStatsTimer_Type(Unsigned32):
    """Custom type cLApProfileStatsTimer based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLApProfileStatsTimer_Type.__name__ = "Unsigned32"
_CLApProfileStatsTimer_Object = MibTableColumn
cLApProfileStatsTimer = _CLApProfileStatsTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 70),
    _CLApProfileStatsTimer_Type()
)
cLApProfileStatsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileStatsTimer.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileStatsTimer.setUnits("seconds")
_CLApProfilePoePreStandardSwitchFlag_Type = TruthValue
_CLApProfilePoePreStandardSwitchFlag_Object = MibTableColumn
cLApProfilePoePreStandardSwitchFlag = _CLApProfilePoePreStandardSwitchFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 71),
    _CLApProfilePoePreStandardSwitchFlag_Type()
)
cLApProfilePoePreStandardSwitchFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePoePreStandardSwitchFlag.setStatus("current")


class _CLApProfilePoePowerInjectorSelection_Type(Integer32):
    """Custom type cLApProfilePoePowerInjectorSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("installed", 2),
          ("override", 3))
    )


_CLApProfilePoePowerInjectorSelection_Type.__name__ = "Integer32"
_CLApProfilePoePowerInjectorSelection_Object = MibTableColumn
cLApProfilePoePowerInjectorSelection = _CLApProfilePoePowerInjectorSelection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 72),
    _CLApProfilePoePowerInjectorSelection_Type()
)
cLApProfilePoePowerInjectorSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePoePowerInjectorSelection.setStatus("current")
_CLApProfilePoeInjectorSwitchMac_Type = MacAddress
_CLApProfilePoeInjectorSwitchMac_Object = MibTableColumn
cLApProfilePoeInjectorSwitchMac = _CLApProfilePoeInjectorSwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 73),
    _CLApProfilePoeInjectorSwitchMac_Type()
)
cLApProfilePoeInjectorSwitchMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePoeInjectorSwitchMac.setStatus("current")


class _CLApProfileHaloBleBeaconAdvertisedPwr_Type(Unsigned32):
    """Custom type cLApProfileHaloBleBeaconAdvertisedPwr based on Unsigned32"""
    defaultValue = 59

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_CLApProfileHaloBleBeaconAdvertisedPwr_Type.__name__ = "Unsigned32"
_CLApProfileHaloBleBeaconAdvertisedPwr_Object = MibTableColumn
cLApProfileHaloBleBeaconAdvertisedPwr = _CLApProfileHaloBleBeaconAdvertisedPwr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 74),
    _CLApProfileHaloBleBeaconAdvertisedPwr_Type()
)
cLApProfileHaloBleBeaconAdvertisedPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconAdvertisedPwr.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconAdvertisedPwr.setUnits("dBm")
_CLApProfileTftpDownGradeAddressType_Type = InetAddressType
_CLApProfileTftpDownGradeAddressType_Object = MibTableColumn
cLApProfileTftpDownGradeAddressType = _CLApProfileTftpDownGradeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 75),
    _CLApProfileTftpDownGradeAddressType_Type()
)
cLApProfileTftpDownGradeAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileTftpDownGradeAddressType.setStatus("current")
_CLApProfileTftpDownGradeAddress_Type = InetAddress
_CLApProfileTftpDownGradeAddress_Object = MibTableColumn
cLApProfileTftpDownGradeAddress = _CLApProfileTftpDownGradeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 76),
    _CLApProfileTftpDownGradeAddress_Type()
)
cLApProfileTftpDownGradeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileTftpDownGradeAddress.setStatus("current")


class _CLApProfileTftpDownGradeFileName_Type(SnmpAdminString):
    """Custom type cLApProfileTftpDownGradeFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileTftpDownGradeFileName_Type.__name__ = "SnmpAdminString"
_CLApProfileTftpDownGradeFileName_Object = MibTableColumn
cLApProfileTftpDownGradeFileName = _CLApProfileTftpDownGradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 77),
    _CLApProfileTftpDownGradeFileName_Type()
)
cLApProfileTftpDownGradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileTftpDownGradeFileName.setStatus("current")


class _CLApProfileCoreDumpType_Type(Integer32):
    """Custom type cLApProfileCoreDumpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uncompress", 1),
          ("compress", 2),
          ("disable", 3))
    )


_CLApProfileCoreDumpType_Type.__name__ = "Integer32"
_CLApProfileCoreDumpType_Object = MibTableColumn
cLApProfileCoreDumpType = _CLApProfileCoreDumpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 78),
    _CLApProfileCoreDumpType_Type()
)
cLApProfileCoreDumpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCoreDumpType.setStatus("current")
_CLApProfileCoreDumpTftpAddressType_Type = InetAddressType
_CLApProfileCoreDumpTftpAddressType_Object = MibTableColumn
cLApProfileCoreDumpTftpAddressType = _CLApProfileCoreDumpTftpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 79),
    _CLApProfileCoreDumpTftpAddressType_Type()
)
cLApProfileCoreDumpTftpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCoreDumpTftpAddressType.setStatus("current")
_CLApProfileCoreDumpTftpAddress_Type = InetAddress
_CLApProfileCoreDumpTftpAddress_Object = MibTableColumn
cLApProfileCoreDumpTftpAddress = _CLApProfileCoreDumpTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 80),
    _CLApProfileCoreDumpTftpAddress_Type()
)
cLApProfileCoreDumpTftpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCoreDumpTftpAddress.setStatus("current")


class _CLApProfileCoreDumpCoreFileName_Type(SnmpAdminString):
    """Custom type cLApProfileCoreDumpCoreFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApProfileCoreDumpCoreFileName_Type.__name__ = "SnmpAdminString"
_CLApProfileCoreDumpCoreFileName_Object = MibTableColumn
cLApProfileCoreDumpCoreFileName = _CLApProfileCoreDumpCoreFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 81),
    _CLApProfileCoreDumpCoreFileName_Type()
)
cLApProfileCoreDumpCoreFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCoreDumpCoreFileName.setStatus("current")
_CLApProfileBackupFallbackEnabled_Type = TruthValue
_CLApProfileBackupFallbackEnabled_Object = MibTableColumn
cLApProfileBackupFallbackEnabled = _CLApProfileBackupFallbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 82),
    _CLApProfileBackupFallbackEnabled_Type()
)
cLApProfileBackupFallbackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBackupFallbackEnabled.setStatus("current")


class _CLApProfileClientRssiStatsEnabled_Type(TruthValue):
    """Custom type cLApProfileClientRssiStatsEnabled based on TruthValue"""
    defaultValue = 1


_CLApProfileClientRssiStatsEnabled_Type.__name__ = "TruthValue"
_CLApProfileClientRssiStatsEnabled_Object = MibTableColumn
cLApProfileClientRssiStatsEnabled = _CLApProfileClientRssiStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 83),
    _CLApProfileClientRssiStatsEnabled_Type()
)
cLApProfileClientRssiStatsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileClientRssiStatsEnabled.setStatus("current")


class _CLApProfileClientRssiStatsReportInterval_Type(Unsigned32):
    """Custom type cLApProfileClientRssiStatsReportInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_CLApProfileClientRssiStatsReportInterval_Type.__name__ = "Unsigned32"
_CLApProfileClientRssiStatsReportInterval_Object = MibTableColumn
cLApProfileClientRssiStatsReportInterval = _CLApProfileClientRssiStatsReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 84),
    _CLApProfileClientRssiStatsReportInterval_Type()
)
cLApProfileClientRssiStatsReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileClientRssiStatsReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileClientRssiStatsReportInterval.setUnits("seconds")
_CLApProfileGasRateLimitEnable_Type = TruthValue
_CLApProfileGasRateLimitEnable_Object = MibTableColumn
cLApProfileGasRateLimitEnable = _CLApProfileGasRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 85),
    _CLApProfileGasRateLimitEnable_Type()
)
cLApProfileGasRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileGasRateLimitEnable.setStatus("current")


class _CLApProfileGasRateLimitNumReqPerInterval_Type(Integer32):
    """Custom type cLApProfileGasRateLimitNumReqPerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CLApProfileGasRateLimitNumReqPerInterval_Type.__name__ = "Integer32"
_CLApProfileGasRateLimitNumReqPerInterval_Object = MibTableColumn
cLApProfileGasRateLimitNumReqPerInterval = _CLApProfileGasRateLimitNumReqPerInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 86),
    _CLApProfileGasRateLimitNumReqPerInterval_Type()
)
cLApProfileGasRateLimitNumReqPerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileGasRateLimitNumReqPerInterval.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileGasRateLimitNumReqPerInterval.setUnits("packets")


class _CLApProfileGasRateLimitIntervalMsec_Type(Integer32):
    """Custom type cLApProfileGasRateLimitIntervalMsec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_CLApProfileGasRateLimitIntervalMsec_Type.__name__ = "Integer32"
_CLApProfileGasRateLimitIntervalMsec_Object = MibTableColumn
cLApProfileGasRateLimitIntervalMsec = _CLApProfileGasRateLimitIntervalMsec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 87),
    _CLApProfileGasRateLimitIntervalMsec_Type()
)
cLApProfileGasRateLimitIntervalMsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileGasRateLimitIntervalMsec.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileGasRateLimitIntervalMsec.setUnits("milliseconds")
_CLApProfileQoSMapApTrustsUpstreamDSCP_Type = TruthValue
_CLApProfileQoSMapApTrustsUpstreamDSCP_Object = MibTableColumn
cLApProfileQoSMapApTrustsUpstreamDSCP = _CLApProfileQoSMapApTrustsUpstreamDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 88),
    _CLApProfileQoSMapApTrustsUpstreamDSCP_Type()
)
cLApProfileQoSMapApTrustsUpstreamDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileQoSMapApTrustsUpstreamDSCP.setStatus("current")


class _CLApProfileUdpliteState_Type(Integer32):
    """Custom type cLApProfileUdpliteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unconfig", 1),
          ("udpliteenabled", 2),
          ("udplitedisabled", 3))
    )


_CLApProfileUdpliteState_Type.__name__ = "Integer32"
_CLApProfileUdpliteState_Object = MibTableColumn
cLApProfileUdpliteState = _CLApProfileUdpliteState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 89),
    _CLApProfileUdpliteState_Type()
)
cLApProfileUdpliteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileUdpliteState.setStatus("current")
_CLApProfileMethodListName_Type = SnmpAdminString
_CLApProfileMethodListName_Object = MibTableColumn
cLApProfileMethodListName = _CLApProfileMethodListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 90),
    _CLApProfileMethodListName_Type()
)
cLApProfileMethodListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileMethodListName.setStatus("current")


class _CLApProfileWindowSize_Type(Integer32):
    """Custom type cLApProfileWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_CLApProfileWindowSize_Type.__name__ = "Integer32"
_CLApProfileWindowSize_Object = MibTableColumn
cLApProfileWindowSize = _CLApProfileWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 91),
    _CLApProfileWindowSize_Type()
)
cLApProfileWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileWindowSize.setStatus("current")


class _CLApProfileCredentialGlobalSecretType_Type(Integer32):
    """Custom type cLApProfileCredentialGlobalSecretType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("aes", 8))
    )


_CLApProfileCredentialGlobalSecretType_Type.__name__ = "Integer32"
_CLApProfileCredentialGlobalSecretType_Object = MibTableColumn
cLApProfileCredentialGlobalSecretType = _CLApProfileCredentialGlobalSecretType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 92),
    _CLApProfileCredentialGlobalSecretType_Type()
)
cLApProfileCredentialGlobalSecretType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCredentialGlobalSecretType.setStatus("current")


class _CLApProfileCredentialGlobalPasswordType_Type(Integer32):
    """Custom type cLApProfileCredentialGlobalPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("aes", 8))
    )


_CLApProfileCredentialGlobalPasswordType_Type.__name__ = "Integer32"
_CLApProfileCredentialGlobalPasswordType_Object = MibTableColumn
cLApProfileCredentialGlobalPasswordType = _CLApProfileCredentialGlobalPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 93),
    _CLApProfileCredentialGlobalPasswordType_Type()
)
cLApProfileCredentialGlobalPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCredentialGlobalPasswordType.setStatus("current")


class _CLApProfile802dot1xSupplicantPasswordType_Type(Integer32):
    """Custom type cLApProfile802dot1xSupplicantPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("aes", 8))
    )


_CLApProfile802dot1xSupplicantPasswordType_Type.__name__ = "Integer32"
_CLApProfile802dot1xSupplicantPasswordType_Object = MibTableColumn
cLApProfile802dot1xSupplicantPasswordType = _CLApProfile802dot1xSupplicantPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 94),
    _CLApProfile802dot1xSupplicantPasswordType_Type()
)
cLApProfile802dot1xSupplicantPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfile802dot1xSupplicantPasswordType.setStatus("current")
_CLApProfileBssidEnableStats_Type = TruthValue
_CLApProfileBssidEnableStats_Object = MibTableColumn
cLApProfileBssidEnableStats = _CLApProfileBssidEnableStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 95),
    _CLApProfileBssidEnableStats_Type()
)
cLApProfileBssidEnableStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBssidEnableStats.setStatus("current")
_CLApProfileBssidStatsFrequency_Type = Integer32
_CLApProfileBssidStatsFrequency_Object = MibTableColumn
cLApProfileBssidStatsFrequency = _CLApProfileBssidStatsFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 96),
    _CLApProfileBssidStatsFrequency_Type()
)
cLApProfileBssidStatsFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileBssidStatsFrequency.setStatus("current")
_CLApProfilePersistentSsidBroadcastEnable_Type = TruthValue
_CLApProfilePersistentSsidBroadcastEnable_Object = MibTableColumn
cLApProfilePersistentSsidBroadcastEnable = _CLApProfilePersistentSsidBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 97),
    _CLApProfilePersistentSsidBroadcastEnable_Type()
)
cLApProfilePersistentSsidBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfilePersistentSsidBroadcastEnable.setStatus("current")
_CLApProfileDhcpFallback_Type = TruthValue
_CLApProfileDhcpFallback_Object = MibTableColumn
cLApProfileDhcpFallback = _CLApProfileDhcpFallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 98),
    _CLApProfileDhcpFallback_Type()
)
cLApProfileDhcpFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileDhcpFallback.setStatus("current")


class _CLApProfileOeapRogueDetectionEnable_Type(TruthValue):
    """Custom type cLApProfileOeapRogueDetectionEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileOeapRogueDetectionEnable_Type.__name__ = "TruthValue"
_CLApProfileOeapRogueDetectionEnable_Object = MibTableColumn
cLApProfileOeapRogueDetectionEnable = _CLApProfileOeapRogueDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 99),
    _CLApProfileOeapRogueDetectionEnable_Type()
)
cLApProfileOeapRogueDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileOeapRogueDetectionEnable.setStatus("current")


class _CLApProfileOeapEncryptionEnable_Type(TruthValue):
    """Custom type cLApProfileOeapEncryptionEnable based on TruthValue"""
    defaultValue = 1


_CLApProfileOeapEncryptionEnable_Type.__name__ = "TruthValue"
_CLApProfileOeapEncryptionEnable_Object = MibTableColumn
cLApProfileOeapEncryptionEnable = _CLApProfileOeapEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 100),
    _CLApProfileOeapEncryptionEnable_Type()
)
cLApProfileOeapEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileOeapEncryptionEnable.setStatus("current")


class _CLApProfileOeapLocalAccessEnable_Type(TruthValue):
    """Custom type cLApProfileOeapLocalAccessEnable based on TruthValue"""
    defaultValue = 1


_CLApProfileOeapLocalAccessEnable_Type.__name__ = "TruthValue"
_CLApProfileOeapLocalAccessEnable_Object = MibTableColumn
cLApProfileOeapLocalAccessEnable = _CLApProfileOeapLocalAccessEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 101),
    _CLApProfileOeapLocalAccessEnable_Type()
)
cLApProfileOeapLocalAccessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileOeapLocalAccessEnable.setStatus("current")


class _CLApProfileOeapProvSsidEnable_Type(TruthValue):
    """Custom type cLApProfileOeapProvSsidEnable based on TruthValue"""
    defaultValue = 2


_CLApProfileOeapProvSsidEnable_Type.__name__ = "TruthValue"
_CLApProfileOeapProvSsidEnable_Object = MibTableColumn
cLApProfileOeapProvSsidEnable = _CLApProfileOeapProvSsidEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 102),
    _CLApProfileOeapProvSsidEnable_Type()
)
cLApProfileOeapProvSsidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileOeapProvSsidEnable.setStatus("current")


class _CLApProfileCountryCode_Type(Integer32):
    """Custom type cLApProfileCountryCode based on Integer32"""
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
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("ae", 1),
          ("al", 2),
          ("ar", 3),
          ("at", 4),
          ("au", 5),
          ("ba", 6),
          ("bb", 7),
          ("bd", 8),
          ("be", 9),
          ("bg", 10),
          ("bh", 11),
          ("bm", 12),
          ("bn", 13),
          ("bo", 14),
          ("br", 15),
          ("belarus", 16),
          ("ca", 17),
          ("ch", 18),
          ("cl", 19),
          ("cm", 20),
          ("cn", 21),
          ("co", 22),
          ("cr", 23),
          ("cu", 24),
          ("cy", 25),
          ("cz", 26),
          ("de", 27),
          ("dk", 28),
          ("do", 29),
          ("dz", 30),
          ("ec", 31),
          ("ee", 32),
          ("eg", 33),
          ("el", 34),
          ("es", 35),
          ("fi", 36),
          ("fj", 37),
          ("fr", 38),
          ("gb", 39),
          ("gh", 40),
          ("gi", 41),
          ("gr", 42),
          ("hk", 43),
          ("hr", 44),
          ("hu", 45),
          ("id", 46),
          ("ie", 47),
          ("il", 48),
          ("in", 49),
          ("io", 50),
          ("iq", 51),
          ("is", 52),
          ("it", 53),
          ("j2", 54),
          ("j4", 55),
          ("jm", 56),
          ("jo", 57),
          ("ke", 58),
          ("kn", 59),
          ("kw", 60),
          ("kz", 61),
          ("lb", 62),
          ("li", 63),
          ("lk", 64),
          ("lt", 65),
          ("lu", 66),
          ("lv", 67),
          ("ly", 68),
          ("ma", 69),
          ("mc", 70),
          ("me", 71),
          ("mk", 72),
          ("mn", 73),
          ("mo", 74),
          ("mt", 75),
          ("mx", 76),
          ("my", 77),
          ("ng", 78),
          ("nl", 79),
          ("no", 80),
          ("nz", 81),
          ("om", 82),
          ("pa", 83),
          ("pe", 84),
          ("ph", 85),
          ("pk", 86),
          ("pl", 87),
          ("pr", 88),
          ("pt", 89),
          ("py", 90),
          ("qa", 91),
          ("ro", 92),
          ("rs", 93),
          ("ru", 94),
          ("sa", 95),
          ("se", 96),
          ("sg", 97),
          ("si", 98),
          ("sk", 99),
          ("th", 100),
          ("ti", 101),
          ("tn", 102),
          ("tr", 103),
          ("tw", 104),
          ("ua", 105),
          ("us", 106),
          ("uy", 107),
          ("ve", 108),
          ("vn", 109),
          ("za", 110),
          ("unconfigured", 111))
    )


_CLApProfileCountryCode_Type.__name__ = "Integer32"
_CLApProfileCountryCode_Object = MibTableColumn
cLApProfileCountryCode = _CLApProfileCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 1, 1, 103),
    _CLApProfileCountryCode_Type()
)
cLApProfileCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileCountryCode.setStatus("current")
_CLApProfileHaloBleBeaconTable_Object = MibTable
cLApProfileHaloBleBeaconTable = _CLApProfileHaloBleBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2)
)
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconTable.setStatus("current")
_CLApProfileHaloBleBeaconEntry_Object = MibTableRow
cLApProfileHaloBleBeaconEntry = _CLApProfileHaloBleBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2, 1)
)
cLApProfileHaloBleBeaconEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileName"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconId"),
)
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconEntry.setStatus("current")


class _CLApProfileHaloBleBeaconId_Type(Unsigned32):
    """Custom type cLApProfileHaloBleBeaconId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_CLApProfileHaloBleBeaconId_Type.__name__ = "Unsigned32"
_CLApProfileHaloBleBeaconId_Object = MibTableColumn
cLApProfileHaloBleBeaconId = _CLApProfileHaloBleBeaconId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2, 1, 1),
    _CLApProfileHaloBleBeaconId_Type()
)
cLApProfileHaloBleBeaconId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconId.setStatus("current")


class _CLApProfileHaloBleBeaconUuid_Type(SnmpAdminString):
    """Custom type cLApProfileHaloBleBeaconUuid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CLApProfileHaloBleBeaconUuid_Type.__name__ = "SnmpAdminString"
_CLApProfileHaloBleBeaconUuid_Object = MibTableColumn
cLApProfileHaloBleBeaconUuid = _CLApProfileHaloBleBeaconUuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2, 1, 2),
    _CLApProfileHaloBleBeaconUuid_Type()
)
cLApProfileHaloBleBeaconUuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconUuid.setStatus("current")


class _CLApProfileHaloBleBeaconTxPower_Type(Unsigned32):
    """Custom type cLApProfileHaloBleBeaconTxPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52),
    )


_CLApProfileHaloBleBeaconTxPower_Type.__name__ = "Unsigned32"
_CLApProfileHaloBleBeaconTxPower_Object = MibTableColumn
cLApProfileHaloBleBeaconTxPower = _CLApProfileHaloBleBeaconTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2, 1, 3),
    _CLApProfileHaloBleBeaconTxPower_Type()
)
cLApProfileHaloBleBeaconTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconTxPower.setUnits("dBm")
_CLApProfileHaloBleBeaconEnabled_Type = TruthValue
_CLApProfileHaloBleBeaconEnabled_Object = MibTableColumn
cLApProfileHaloBleBeaconEnabled = _CLApProfileHaloBleBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2, 1, 4),
    _CLApProfileHaloBleBeaconEnabled_Type()
)
cLApProfileHaloBleBeaconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconEnabled.setStatus("current")
_CLApProfileHaloBleBeaconRowStatus_Type = RowStatus
_CLApProfileHaloBleBeaconRowStatus_Object = MibTableColumn
cLApProfileHaloBleBeaconRowStatus = _CLApProfileHaloBleBeaconRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 2, 1, 5),
    _CLApProfileHaloBleBeaconRowStatus_Type()
)
cLApProfileHaloBleBeaconRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileHaloBleBeaconRowStatus.setStatus("current")
_CLApProfileQosMapRangeTable_Object = MibTable
cLApProfileQosMapRangeTable = _CLApProfileQosMapRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3)
)
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeTable.setStatus("current")
_CLApProfileQosMapRangeEntry_Object = MibTableRow
cLApProfileQosMapRangeEntry = _CLApProfileQosMapRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3, 1)
)
cLApProfileQosMapRangeEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileName"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileQosMapRangeUP"),
)
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeEntry.setStatus("current")


class _CLApProfileQosMapRangeUP_Type(Integer32):
    """Custom type cLApProfileQosMapRangeUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CLApProfileQosMapRangeUP_Type.__name__ = "Integer32"
_CLApProfileQosMapRangeUP_Object = MibTableColumn
cLApProfileQosMapRangeUP = _CLApProfileQosMapRangeUP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3, 1, 1),
    _CLApProfileQosMapRangeUP_Type()
)
cLApProfileQosMapRangeUP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeUP.setStatus("current")


class _CLApProfileQosMapRangeDSCPLower_Type(Integer32):
    """Custom type cLApProfileQosMapRangeDSCPLower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLApProfileQosMapRangeDSCPLower_Type.__name__ = "Integer32"
_CLApProfileQosMapRangeDSCPLower_Object = MibTableColumn
cLApProfileQosMapRangeDSCPLower = _CLApProfileQosMapRangeDSCPLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3, 1, 2),
    _CLApProfileQosMapRangeDSCPLower_Type()
)
cLApProfileQosMapRangeDSCPLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeDSCPLower.setStatus("current")


class _CLApProfileQosMapRangeDSCPUpper_Type(Integer32):
    """Custom type cLApProfileQosMapRangeDSCPUpper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLApProfileQosMapRangeDSCPUpper_Type.__name__ = "Integer32"
_CLApProfileQosMapRangeDSCPUpper_Object = MibTableColumn
cLApProfileQosMapRangeDSCPUpper = _CLApProfileQosMapRangeDSCPUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3, 1, 3),
    _CLApProfileQosMapRangeDSCPUpper_Type()
)
cLApProfileQosMapRangeDSCPUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeDSCPUpper.setStatus("current")


class _CLApProfileQosMapRangeUPToDSCP_Type(Integer32):
    """Custom type cLApProfileQosMapRangeUPToDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLApProfileQosMapRangeUPToDSCP_Type.__name__ = "Integer32"
_CLApProfileQosMapRangeUPToDSCP_Object = MibTableColumn
cLApProfileQosMapRangeUPToDSCP = _CLApProfileQosMapRangeUPToDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3, 1, 4),
    _CLApProfileQosMapRangeUPToDSCP_Type()
)
cLApProfileQosMapRangeUPToDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeUPToDSCP.setStatus("current")
_CLApProfileQosMapRangeRowStatus_Type = RowStatus
_CLApProfileQosMapRangeRowStatus_Object = MibTableColumn
cLApProfileQosMapRangeRowStatus = _CLApProfileQosMapRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 3, 1, 5),
    _CLApProfileQosMapRangeRowStatus_Type()
)
cLApProfileQosMapRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileQosMapRangeRowStatus.setStatus("current")
_CLApProfileQosMapExceptionTable_Object = MibTable
cLApProfileQosMapExceptionTable = _CLApProfileQosMapExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 4)
)
if mibBuilder.loadTexts:
    cLApProfileQosMapExceptionTable.setStatus("current")
_CLApProfileQosMapExceptionEntry_Object = MibTableRow
cLApProfileQosMapExceptionEntry = _CLApProfileQosMapExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 4, 1)
)
cLApProfileQosMapExceptionEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileName"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApProfileQosMapExceptionDSCP"),
)
if mibBuilder.loadTexts:
    cLApProfileQosMapExceptionEntry.setStatus("current")


class _CLApProfileQosMapExceptionDSCP_Type(Integer32):
    """Custom type cLApProfileQosMapExceptionDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLApProfileQosMapExceptionDSCP_Type.__name__ = "Integer32"
_CLApProfileQosMapExceptionDSCP_Object = MibTableColumn
cLApProfileQosMapExceptionDSCP = _CLApProfileQosMapExceptionDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 4, 1, 1),
    _CLApProfileQosMapExceptionDSCP_Type()
)
cLApProfileQosMapExceptionDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApProfileQosMapExceptionDSCP.setStatus("current")


class _CLApProfileQosMapExceptionUP_Type(Integer32):
    """Custom type cLApProfileQosMapExceptionUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CLApProfileQosMapExceptionUP_Type.__name__ = "Integer32"
_CLApProfileQosMapExceptionUP_Object = MibTableColumn
cLApProfileQosMapExceptionUP = _CLApProfileQosMapExceptionUP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 4, 1, 2),
    _CLApProfileQosMapExceptionUP_Type()
)
cLApProfileQosMapExceptionUP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileQosMapExceptionUP.setStatus("current")
_CLApProfileQosMapExceptionRowStatus_Type = RowStatus
_CLApProfileQosMapExceptionRowStatus_Object = MibTableColumn
cLApProfileQosMapExceptionRowStatus = _CLApProfileQosMapExceptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 16, 4, 1, 3),
    _CLApProfileQosMapExceptionRowStatus_Type()
)
cLApProfileQosMapExceptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApProfileQosMapExceptionRowStatus.setStatus("current")
_CiscoLwappApPacketCapture_ObjectIdentity = ObjectIdentity
ciscoLwappApPacketCapture = _CiscoLwappApPacketCapture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17)
)
_CLApPacketCaptureProfileTable_Object = MibTable
cLApPacketCaptureProfileTable = _CLApPacketCaptureProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1)
)
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileTable.setStatus("current")
_CLApPacketCaptureProfileEntry_Object = MibTableRow
cLApPacketCaptureProfileEntry = _CLApPacketCaptureProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1)
)
cLApPacketCaptureProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileName"),
)
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileEntry.setStatus("current")


class _CLApPacketCaptureProfileName_Type(SnmpAdminString):
    """Custom type cLApPacketCaptureProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApPacketCaptureProfileName_Type.__name__ = "SnmpAdminString"
_CLApPacketCaptureProfileName_Object = MibTableColumn
cLApPacketCaptureProfileName = _CLApPacketCaptureProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 1),
    _CLApPacketCaptureProfileName_Type()
)
cLApPacketCaptureProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileName.setStatus("current")
_CLApPacketCaptureProfileRowStatus_Type = RowStatus
_CLApPacketCaptureProfileRowStatus_Object = MibTableColumn
cLApPacketCaptureProfileRowStatus = _CLApPacketCaptureProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 2),
    _CLApPacketCaptureProfileRowStatus_Type()
)
cLApPacketCaptureProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileRowStatus.setStatus("current")


class _CLApPacketCaptureProfileBufferSize_Type(Unsigned32):
    """Custom type cLApPacketCaptureProfileBufferSize based on Unsigned32"""
    defaultValue = 2048

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 4096),
    )


_CLApPacketCaptureProfileBufferSize_Type.__name__ = "Unsigned32"
_CLApPacketCaptureProfileBufferSize_Object = MibTableColumn
cLApPacketCaptureProfileBufferSize = _CLApPacketCaptureProfileBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 3),
    _CLApPacketCaptureProfileBufferSize_Type()
)
cLApPacketCaptureProfileBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileBufferSize.setUnits("kilobytes")


class _CLApPacketCaptureProfileDuration_Type(Unsigned32):
    """Custom type cLApPacketCaptureProfileDuration based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CLApPacketCaptureProfileDuration_Type.__name__ = "Unsigned32"
_CLApPacketCaptureProfileDuration_Object = MibTableColumn
cLApPacketCaptureProfileDuration = _CLApPacketCaptureProfileDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 4),
    _CLApPacketCaptureProfileDuration_Type()
)
cLApPacketCaptureProfileDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileDuration.setStatus("current")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileDuration.setUnits("Minutes")


class _CLApPacketCaptureProfileTruncation_Type(Unsigned32):
    """Custom type cLApPacketCaptureProfileTruncation based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CLApPacketCaptureProfileTruncation_Type.__name__ = "Unsigned32"
_CLApPacketCaptureProfileTruncation_Object = MibTableColumn
cLApPacketCaptureProfileTruncation = _CLApPacketCaptureProfileTruncation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 5),
    _CLApPacketCaptureProfileTruncation_Type()
)
cLApPacketCaptureProfileTruncation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileTruncation.setStatus("current")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileTruncation.setUnits("bytes")
_CLApPacketCaptureProfileFtpServerAddressType_Type = InetAddressType
_CLApPacketCaptureProfileFtpServerAddressType_Object = MibTableColumn
cLApPacketCaptureProfileFtpServerAddressType = _CLApPacketCaptureProfileFtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 6),
    _CLApPacketCaptureProfileFtpServerAddressType_Type()
)
cLApPacketCaptureProfileFtpServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileFtpServerAddressType.setStatus("current")
_CLApPacketCaptureProfileFtpServerAddress_Type = InetAddress
_CLApPacketCaptureProfileFtpServerAddress_Object = MibTableColumn
cLApPacketCaptureProfileFtpServerAddress = _CLApPacketCaptureProfileFtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 7),
    _CLApPacketCaptureProfileFtpServerAddress_Type()
)
cLApPacketCaptureProfileFtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileFtpServerAddress.setStatus("current")
_CLApPacketCaptureProfileFtpServerPath_Type = SnmpAdminString
_CLApPacketCaptureProfileFtpServerPath_Object = MibTableColumn
cLApPacketCaptureProfileFtpServerPath = _CLApPacketCaptureProfileFtpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 8),
    _CLApPacketCaptureProfileFtpServerPath_Type()
)
cLApPacketCaptureProfileFtpServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileFtpServerPath.setStatus("current")
_CLApPacketCaptureProfileFtpUsername_Type = SnmpAdminString
_CLApPacketCaptureProfileFtpUsername_Object = MibTableColumn
cLApPacketCaptureProfileFtpUsername = _CLApPacketCaptureProfileFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 9),
    _CLApPacketCaptureProfileFtpUsername_Type()
)
cLApPacketCaptureProfileFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileFtpUsername.setStatus("current")
_CLApPacketCaptureProfileFtpPassword_Type = SnmpAdminString
_CLApPacketCaptureProfileFtpPassword_Object = MibTableColumn
cLApPacketCaptureProfileFtpPassword = _CLApPacketCaptureProfileFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 10),
    _CLApPacketCaptureProfileFtpPassword_Type()
)
cLApPacketCaptureProfileFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileFtpPassword.setStatus("current")


class _CLApPacketCaptureProfileClassifierArp_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierArp based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierArp_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierArp_Object = MibTableColumn
cLApPacketCaptureProfileClassifierArp = _CLApPacketCaptureProfileClassifierArp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 11),
    _CLApPacketCaptureProfileClassifierArp_Type()
)
cLApPacketCaptureProfileClassifierArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierArp.setStatus("current")


class _CLApPacketCaptureProfileClassifierBroadcast_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierBroadcast based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierBroadcast_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierBroadcast_Object = MibTableColumn
cLApPacketCaptureProfileClassifierBroadcast = _CLApPacketCaptureProfileClassifierBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 12),
    _CLApPacketCaptureProfileClassifierBroadcast_Type()
)
cLApPacketCaptureProfileClassifierBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierBroadcast.setStatus("current")


class _CLApPacketCaptureProfileClassifierControl_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierControl based on TruthValue"""
    defaultValue = 1


_CLApPacketCaptureProfileClassifierControl_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierControl_Object = MibTableColumn
cLApPacketCaptureProfileClassifierControl = _CLApPacketCaptureProfileClassifierControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 13),
    _CLApPacketCaptureProfileClassifierControl_Type()
)
cLApPacketCaptureProfileClassifierControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierControl.setStatus("current")


class _CLApPacketCaptureProfileClassifierData_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierData based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierData_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierData_Object = MibTableColumn
cLApPacketCaptureProfileClassifierData = _CLApPacketCaptureProfileClassifierData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 14),
    _CLApPacketCaptureProfileClassifierData_Type()
)
cLApPacketCaptureProfileClassifierData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierData.setStatus("current")


class _CLApPacketCaptureProfileClassifierDot1x_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierDot1x based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierDot1x_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierDot1x_Object = MibTableColumn
cLApPacketCaptureProfileClassifierDot1x = _CLApPacketCaptureProfileClassifierDot1x_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 15),
    _CLApPacketCaptureProfileClassifierDot1x_Type()
)
cLApPacketCaptureProfileClassifierDot1x.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierDot1x.setStatus("current")


class _CLApPacketCaptureProfileClassifierIapp_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierIapp based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierIapp_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierIapp_Object = MibTableColumn
cLApPacketCaptureProfileClassifierIapp = _CLApPacketCaptureProfileClassifierIapp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 16),
    _CLApPacketCaptureProfileClassifierIapp_Type()
)
cLApPacketCaptureProfileClassifierIapp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierIapp.setStatus("current")


class _CLApPacketCaptureProfileClassifierIp_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierIp based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierIp_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierIp_Object = MibTableColumn
cLApPacketCaptureProfileClassifierIp = _CLApPacketCaptureProfileClassifierIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 17),
    _CLApPacketCaptureProfileClassifierIp_Type()
)
cLApPacketCaptureProfileClassifierIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierIp.setStatus("current")


class _CLApPacketCaptureProfileClassifierManagement_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierManagement based on TruthValue"""
    defaultValue = 1


_CLApPacketCaptureProfileClassifierManagement_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierManagement_Object = MibTableColumn
cLApPacketCaptureProfileClassifierManagement = _CLApPacketCaptureProfileClassifierManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 18),
    _CLApPacketCaptureProfileClassifierManagement_Type()
)
cLApPacketCaptureProfileClassifierManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierManagement.setStatus("current")


class _CLApPacketCaptureProfileClassifierMulticast_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierMulticast based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierMulticast_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierMulticast_Object = MibTableColumn
cLApPacketCaptureProfileClassifierMulticast = _CLApPacketCaptureProfileClassifierMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 19),
    _CLApPacketCaptureProfileClassifierMulticast_Type()
)
cLApPacketCaptureProfileClassifierMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierMulticast.setStatus("current")


class _CLApPacketCaptureProfileClassifierTcp_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierTcp based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierTcp_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierTcp_Object = MibTableColumn
cLApPacketCaptureProfileClassifierTcp = _CLApPacketCaptureProfileClassifierTcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 20),
    _CLApPacketCaptureProfileClassifierTcp_Type()
)
cLApPacketCaptureProfileClassifierTcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierTcp.setStatus("current")


class _CLApPacketCaptureProfileClassifierUdp_Type(TruthValue):
    """Custom type cLApPacketCaptureProfileClassifierUdp based on TruthValue"""
    defaultValue = 2


_CLApPacketCaptureProfileClassifierUdp_Type.__name__ = "TruthValue"
_CLApPacketCaptureProfileClassifierUdp_Object = MibTableColumn
cLApPacketCaptureProfileClassifierUdp = _CLApPacketCaptureProfileClassifierUdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 21),
    _CLApPacketCaptureProfileClassifierUdp_Type()
)
cLApPacketCaptureProfileClassifierUdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierUdp.setStatus("current")


class _CLApPacketCaptureProfileClassifierTcpPort_Type(InetPortNumber):
    """Custom type cLApPacketCaptureProfileClassifierTcpPort based on InetPortNumber"""
    defaultValue = 0

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLApPacketCaptureProfileClassifierTcpPort_Type.__name__ = "InetPortNumber"
_CLApPacketCaptureProfileClassifierTcpPort_Object = MibTableColumn
cLApPacketCaptureProfileClassifierTcpPort = _CLApPacketCaptureProfileClassifierTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 22),
    _CLApPacketCaptureProfileClassifierTcpPort_Type()
)
cLApPacketCaptureProfileClassifierTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierTcpPort.setStatus("current")


class _CLApPacketCaptureProfileClassifierUdpPort_Type(InetPortNumber):
    """Custom type cLApPacketCaptureProfileClassifierUdpPort based on InetPortNumber"""
    defaultValue = 0

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLApPacketCaptureProfileClassifierUdpPort_Type.__name__ = "InetPortNumber"
_CLApPacketCaptureProfileClassifierUdpPort_Object = MibTableColumn
cLApPacketCaptureProfileClassifierUdpPort = _CLApPacketCaptureProfileClassifierUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 1, 1, 23),
    _CLApPacketCaptureProfileClassifierUdpPort_Type()
)
cLApPacketCaptureProfileClassifierUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureProfileClassifierUdpPort.setStatus("current")
_CLApPacketCaptureClientTable_Object = MibTable
cLApPacketCaptureClientTable = _CLApPacketCaptureClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2)
)
if mibBuilder.loadTexts:
    cLApPacketCaptureClientTable.setStatus("current")
_CLApPacketCaptureClientEntry_Object = MibTableRow
cLApPacketCaptureClientEntry = _CLApPacketCaptureClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1)
)
cLApPacketCaptureClientEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApPacketCaptureClientDeviceMac"),
)
if mibBuilder.loadTexts:
    cLApPacketCaptureClientEntry.setStatus("current")
_CLApPacketCaptureClientDeviceMac_Type = MacAddress
_CLApPacketCaptureClientDeviceMac_Object = MibTableColumn
cLApPacketCaptureClientDeviceMac = _CLApPacketCaptureClientDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1, 1),
    _CLApPacketCaptureClientDeviceMac_Type()
)
cLApPacketCaptureClientDeviceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLApPacketCaptureClientDeviceMac.setStatus("current")
_CLApPacketCaptureClientApMacAddress_Type = MacAddress
_CLApPacketCaptureClientApMacAddress_Object = MibTableColumn
cLApPacketCaptureClientApMacAddress = _CLApPacketCaptureClientApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1, 2),
    _CLApPacketCaptureClientApMacAddress_Type()
)
cLApPacketCaptureClientApMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureClientApMacAddress.setStatus("current")
_CLApPacketCaptureClientAutoMode_Type = TruthValue
_CLApPacketCaptureClientAutoMode_Object = MibTableColumn
cLApPacketCaptureClientAutoMode = _CLApPacketCaptureClientAutoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1, 3),
    _CLApPacketCaptureClientAutoMode_Type()
)
cLApPacketCaptureClientAutoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureClientAutoMode.setStatus("current")


class _CLApPacketCaptureClientStartStop_Type(Integer32):
    """Custom type cLApPacketCaptureClientStartStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("start", 2),
          ("stop", 3))
    )


_CLApPacketCaptureClientStartStop_Type.__name__ = "Integer32"
_CLApPacketCaptureClientStartStop_Object = MibTableColumn
cLApPacketCaptureClientStartStop = _CLApPacketCaptureClientStartStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1, 4),
    _CLApPacketCaptureClientStartStop_Type()
)
cLApPacketCaptureClientStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLApPacketCaptureClientStartStop.setStatus("current")


class _CLApPacketCaptureClientSiteName_Type(SnmpAdminString):
    """Custom type cLApPacketCaptureClientSiteName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApPacketCaptureClientSiteName_Type.__name__ = "SnmpAdminString"
_CLApPacketCaptureClientSiteName_Object = MibTableColumn
cLApPacketCaptureClientSiteName = _CLApPacketCaptureClientSiteName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1, 5),
    _CLApPacketCaptureClientSiteName_Type()
)
cLApPacketCaptureClientSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPacketCaptureClientSiteName.setStatus("current")
_CLApPacketCaptureClientRowStatus_Type = RowStatus
_CLApPacketCaptureClientRowStatus_Object = MibTableColumn
cLApPacketCaptureClientRowStatus = _CLApPacketCaptureClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 2, 1, 6),
    _CLApPacketCaptureClientRowStatus_Type()
)
cLApPacketCaptureClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLApPacketCaptureClientRowStatus.setStatus("current")
_CLApPacketCaptureApTable_Object = MibTable
cLApPacketCaptureApTable = _CLApPacketCaptureApTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 3)
)
if mibBuilder.loadTexts:
    cLApPacketCaptureApTable.setStatus("current")
_CLApPacketCaptureApEntry_Object = MibTableRow
cLApPacketCaptureApEntry = _CLApPacketCaptureApEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 3, 1)
)
cLApPacketCaptureApEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLApPacketCaptureApEntry.setStatus("current")
_CLApPacketCaptureApDeviceMac_Type = MacAddress
_CLApPacketCaptureApDeviceMac_Object = MibTableColumn
cLApPacketCaptureApDeviceMac = _CLApPacketCaptureApDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 3, 1, 1),
    _CLApPacketCaptureApDeviceMac_Type()
)
cLApPacketCaptureApDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPacketCaptureApDeviceMac.setStatus("current")
_CLApPacketCaptureApMacAddress_Type = MacAddress
_CLApPacketCaptureApMacAddress_Object = MibTableColumn
cLApPacketCaptureApMacAddress = _CLApPacketCaptureApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 3, 1, 2),
    _CLApPacketCaptureApMacAddress_Type()
)
cLApPacketCaptureApMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPacketCaptureApMacAddress.setStatus("current")
_CLApPacketCaptureApStatus_Type = TruthValue
_CLApPacketCaptureApStatus_Object = MibTableColumn
cLApPacketCaptureApStatus = _CLApPacketCaptureApStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 17, 3, 1, 3),
    _CLApPacketCaptureApStatus_Type()
)
cLApPacketCaptureApStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApPacketCaptureApStatus.setStatus("current")
_CiscoLwappApNtpInfo_ObjectIdentity = ObjectIdentity
ciscoLwappApNtpInfo = _CiscoLwappApNtpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18)
)
_CLAPNtpInfoTable_Object = MibTable
cLAPNtpInfoTable = _CLAPNtpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1)
)
if mibBuilder.loadTexts:
    cLAPNtpInfoTable.setStatus("current")
_CLAPNtpInfoEntry_Object = MibTableRow
cLAPNtpInfoEntry = _CLAPNtpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1)
)
cLAPNtpInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLAPNtpInfoEntry.setStatus("current")
_CLAPNtpInfoState_Type = TruthValue
_CLAPNtpInfoState_Object = MibTableColumn
cLAPNtpInfoState = _CLAPNtpInfoState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 1),
    _CLAPNtpInfoState_Type()
)
cLAPNtpInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPNtpInfoState.setStatus("current")
_CLApNtpInfoStatus_Type = CLApNtpStatus
_CLApNtpInfoStatus_Object = MibTableColumn
cLApNtpInfoStatus = _CLApNtpInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 2),
    _CLApNtpInfoStatus_Type()
)
cLApNtpInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApNtpInfoStatus.setStatus("current")


class _CLAPNtpInfoStratum_Type(Unsigned32):
    """Custom type cLAPNtpInfoStratum based on Unsigned32"""
    defaultValue = 0


_CLAPNtpInfoStratum_Type.__name__ = "Unsigned32"
_CLAPNtpInfoStratum_Object = MibTableColumn
cLAPNtpInfoStratum = _CLAPNtpInfoStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 3),
    _CLAPNtpInfoStratum_Type()
)
cLAPNtpInfoStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPNtpInfoStratum.setStatus("current")


class _CLAPNtpInfoLastSync_Type(Unsigned32):
    """Custom type cLAPNtpInfoLastSync based on Unsigned32"""
    defaultValue = 0


_CLAPNtpInfoLastSync_Type.__name__ = "Unsigned32"
_CLAPNtpInfoLastSync_Object = MibTableColumn
cLAPNtpInfoLastSync = _CLAPNtpInfoLastSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 4),
    _CLAPNtpInfoLastSync_Type()
)
cLAPNtpInfoLastSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPNtpInfoLastSync.setStatus("current")


class _CLAPNtpInfoOffset_Type(Integer32):
    """Custom type cLAPNtpInfoOffset based on Integer32"""
    defaultValue = 0


_CLAPNtpInfoOffset_Type.__name__ = "Integer32"
_CLAPNtpInfoOffset_Object = MibTableColumn
cLAPNtpInfoOffset = _CLAPNtpInfoOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 5),
    _CLAPNtpInfoOffset_Type()
)
cLAPNtpInfoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPNtpInfoOffset.setStatus("current")


class _CLAPNtpInfoIPAddressType_Type(InetAddressType):
    """Custom type cLAPNtpInfoIPAddressType based on InetAddressType"""
    defaultValue = 0


_CLAPNtpInfoIPAddressType_Type.__name__ = "InetAddressType"
_CLAPNtpInfoIPAddressType_Object = MibTableColumn
cLAPNtpInfoIPAddressType = _CLAPNtpInfoIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 6),
    _CLAPNtpInfoIPAddressType_Type()
)
cLAPNtpInfoIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPNtpInfoIPAddressType.setStatus("current")


class _CLAPNtpInfoIPAddress_Type(InetAddress):
    """Custom type cLAPNtpInfoIPAddress based on InetAddress"""
    defaultValue = OctetString("")


_CLAPNtpInfoIPAddress_Type.__name__ = "InetAddress"
_CLAPNtpInfoIPAddress_Object = MibTableColumn
cLAPNtpInfoIPAddress = _CLAPNtpInfoIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 18, 1, 1, 7),
    _CLAPNtpInfoIPAddress_Type()
)
cLAPNtpInfoIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAPNtpInfoIPAddress.setStatus("current")
_CiscoLwappAp11axRadioConfig_ObjectIdentity = ObjectIdentity
ciscoLwappAp11axRadioConfig = _CiscoLwappAp11axRadioConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21)
)
_CLAp11axRadioConfigTable_Object = MibTable
cLAp11axRadioConfigTable = _CLAp11axRadioConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1)
)
if mibBuilder.loadTexts:
    cLAp11axRadioConfigTable.setStatus("current")
_CLAp11axRadioConfigEntry_Object = MibTableRow
cLAp11axRadioConfigEntry = _CLAp11axRadioConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1)
)
cLAp11axRadioConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cLAp11axRadioConfigEntry.setStatus("current")
_CLAp11axDualRadioCapable_Type = TruthValue
_CLAp11axDualRadioCapable_Object = MibTableColumn
cLAp11axDualRadioCapable = _CLAp11axDualRadioCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 1),
    _CLAp11axDualRadioCapable_Type()
)
cLAp11axDualRadioCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAp11axDualRadioCapable.setStatus("current")
_CLAp11axRadioFRACapable_Type = TruthValue
_CLAp11axRadioFRACapable_Object = MibTableColumn
cLAp11axRadioFRACapable = _CLAp11axRadioFRACapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 2),
    _CLAp11axRadioFRACapable_Type()
)
cLAp11axRadioFRACapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAp11axRadioFRACapable.setStatus("current")


class _CLAp11axDualRadioOperation_Type(Integer32):
    """Custom type cLAp11axDualRadioOperation based on Integer32"""
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
          ("manual", 2),
          ("none", 3))
    )


_CLAp11axDualRadioOperation_Type.__name__ = "Integer32"
_CLAp11axDualRadioOperation_Object = MibTableColumn
cLAp11axDualRadioOperation = _CLAp11axDualRadioOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 3),
    _CLAp11axDualRadioOperation_Type()
)
cLAp11axDualRadioOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11axDualRadioOperation.setStatus("current")


class _CLAp11axDualRadioMode_Type(Integer32):
    """Custom type cLAp11axDualRadioMode based on Integer32"""
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
          ("none", 3))
    )


_CLAp11axDualRadioMode_Type.__name__ = "Integer32"
_CLAp11axDualRadioMode_Object = MibTableColumn
cLAp11axDualRadioMode = _CLAp11axDualRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 4),
    _CLAp11axDualRadioMode_Type()
)
cLAp11axDualRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11axDualRadioMode.setStatus("current")


class _CLAp11axRadioRoleOperation_Type(Integer32):
    """Custom type cLAp11axRadioRoleOperation based on Integer32"""
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
          ("manual", 2),
          ("none", 3))
    )


_CLAp11axRadioRoleOperation_Type.__name__ = "Integer32"
_CLAp11axRadioRoleOperation_Object = MibTableColumn
cLAp11axRadioRoleOperation = _CLAp11axRadioRoleOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 5),
    _CLAp11axRadioRoleOperation_Type()
)
cLAp11axRadioRoleOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11axRadioRoleOperation.setStatus("current")


class _CLAp11axRadioRole_Type(Integer32):
    """Custom type cLAp11axRadioRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientserving", 1),
          ("monitor", 2),
          ("none", 3))
    )


_CLAp11axRadioRole_Type.__name__ = "Integer32"
_CLAp11axRadioRole_Object = MibTableColumn
cLAp11axRadioRole = _CLAp11axRadioRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 6),
    _CLAp11axRadioRole_Type()
)
cLAp11axRadioRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLAp11axRadioRole.setStatus("current")
_CLAp11axObssPdCapable_Type = TruthValue
_CLAp11axObssPdCapable_Object = MibTableColumn
cLAp11axObssPdCapable = _CLAp11axObssPdCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 7),
    _CLAp11axObssPdCapable_Type()
)
cLAp11axObssPdCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAp11axObssPdCapable.setStatus("current")
_CLAp11axObssPdSrgCapable_Type = TruthValue
_CLAp11axObssPdSrgCapable_Object = MibTableColumn
cLAp11axObssPdSrgCapable = _CLAp11axObssPdSrgCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 21, 1, 1, 8),
    _CLAp11axObssPdSrgCapable_Type()
)
cLAp11axObssPdSrgCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLAp11axObssPdSrgCapable.setStatus("current")
_CiscoLwappApSlotWlanStats_ObjectIdentity = ObjectIdentity
ciscoLwappApSlotWlanStats = _CiscoLwappApSlotWlanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22)
)
_CLApSlotWlanStatsTable_Object = MibTable
cLApSlotWlanStatsTable = _CLApSlotWlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1)
)
if mibBuilder.loadTexts:
    cLApSlotWlanStatsTable.setStatus("current")
_CLApSlotWlanStatsEntry_Object = MibTableRow
cLApSlotWlanStatsEntry = _CLApSlotWlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1)
)
cLApSlotWlanStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLApSlotWlanStatsEntry.setStatus("current")
_CLApSlotWlanStatsTxPktNum_Type = Counter64
_CLApSlotWlanStatsTxPktNum_Object = MibTableColumn
cLApSlotWlanStatsTxPktNum = _CLApSlotWlanStatsTxPktNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 1),
    _CLApSlotWlanStatsTxPktNum_Type()
)
cLApSlotWlanStatsTxPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsTxPktNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsTxPktNum.setUnits("packets")
_CLApSlotWlanStatsTxOctetNum_Type = Counter64
_CLApSlotWlanStatsTxOctetNum_Object = MibTableColumn
cLApSlotWlanStatsTxOctetNum = _CLApSlotWlanStatsTxOctetNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 2),
    _CLApSlotWlanStatsTxOctetNum_Type()
)
cLApSlotWlanStatsTxOctetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsTxOctetNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsTxOctetNum.setUnits("packets")
_CLApSlotWlanStatsRxPktNum_Type = Counter64
_CLApSlotWlanStatsRxPktNum_Object = MibTableColumn
cLApSlotWlanStatsRxPktNum = _CLApSlotWlanStatsRxPktNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 3),
    _CLApSlotWlanStatsRxPktNum_Type()
)
cLApSlotWlanStatsRxPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsRxPktNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsRxPktNum.setUnits("packets")
_CLApSlotWlanStatsRxOctetNum_Type = Counter64
_CLApSlotWlanStatsRxOctetNum_Object = MibTableColumn
cLApSlotWlanStatsRxOctetNum = _CLApSlotWlanStatsRxOctetNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 4),
    _CLApSlotWlanStatsRxOctetNum_Type()
)
cLApSlotWlanStatsRxOctetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsRxOctetNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsRxOctetNum.setUnits("packets")
_CLApSlotWlanStatsRetransmitNum_Type = Counter64
_CLApSlotWlanStatsRetransmitNum_Object = MibTableColumn
cLApSlotWlanStatsRetransmitNum = _CLApSlotWlanStatsRetransmitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 5),
    _CLApSlotWlanStatsRetransmitNum_Type()
)
cLApSlotWlanStatsRetransmitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsRetransmitNum.setStatus("current")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsRetransmitNum.setUnits("packets")
_CLApSlotWlanStatsAssocClientNum_Type = Unsigned32
_CLApSlotWlanStatsAssocClientNum_Object = MibTableColumn
cLApSlotWlanStatsAssocClientNum = _CLApSlotWlanStatsAssocClientNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 6),
    _CLApSlotWlanStatsAssocClientNum_Type()
)
cLApSlotWlanStatsAssocClientNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsAssocClientNum.setStatus("current")
_CLApSlotWlanStatsOnlineUserNum_Type = Unsigned32
_CLApSlotWlanStatsOnlineUserNum_Object = MibTableColumn
cLApSlotWlanStatsOnlineUserNum = _CLApSlotWlanStatsOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 1, 22, 1, 1, 7),
    _CLApSlotWlanStatsOnlineUserNum_Type()
)
cLApSlotWlanStatsOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApSlotWlanStatsOnlineUserNum.setStatus("current")
_CiscoLwappApMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBConform = _CiscoLwappApMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2)
)
_CiscoLwappApMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBCompliances = _CiscoLwappApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1)
)
_CiscoLwappApMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBGroups = _CiscoLwappApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2)
)
_CiscoLwappApMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappApMIBNotifObjects = _CiscoLwappApMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3)
)
_CLApAssocFailureReason_Type = CLApAssocFailureReason
_CLApAssocFailureReason_Object = MibScalar
cLApAssocFailureReason = _CLApAssocFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 1),
    _CLApAssocFailureReason_Type()
)
cLApAssocFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApAssocFailureReason.setStatus("current")
_CLApRogueApMacAddress_Type = MacAddress
_CLApRogueApMacAddress_Object = MibScalar
cLApRogueApMacAddress = _CLApRogueApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 2),
    _CLApRogueApMacAddress_Type()
)
cLApRogueApMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueApMacAddress.setStatus("current")
_CLApDot11RadioChannelNumber_Type = CLDot11Channel
_CLApDot11RadioChannelNumber_Object = MibScalar
cLApDot11RadioChannelNumber = _CLApDot11RadioChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 3),
    _CLApDot11RadioChannelNumber_Type()
)
cLApDot11RadioChannelNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApDot11RadioChannelNumber.setStatus("current")
_CLApRogueApSsid_Type = SnmpAdminString
_CLApRogueApSsid_Object = MibScalar
cLApRogueApSsid = _CLApRogueApSsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 4),
    _CLApRogueApSsid_Type()
)
cLApRogueApSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueApSsid.setStatus("current")


class _CLApRogueType_Type(Integer32):
    """Custom type cLApRogueType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asleap", 1),
          ("honeypot", 2),
          ("other", 3))
    )


_CLApRogueType_Type.__name__ = "Integer32"
_CLApRogueType_Object = MibScalar
cLApRogueType = _CLApRogueType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 5),
    _CLApRogueType_Type()
)
cLApRogueType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueType.setStatus("current")


class _CLApWipsReason_Type(Integer32):
    """Custom type cLApWipsReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("noMonitoringDevice", 1)
    )


_CLApWipsReason_Type.__name__ = "Integer32"
_CLApWipsReason_Object = MibScalar
cLApWipsReason = _CLApWipsReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 6),
    _CLApWipsReason_Type()
)
cLApWipsReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApWipsReason.setStatus("current")
_CLApWipsClear_Type = TruthValue
_CLApWipsClear_Object = MibScalar
cLApWipsClear = _CLApWipsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 7),
    _CLApWipsClear_Type()
)
cLApWipsClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApWipsClear.setStatus("current")


class _CLApIfUpDownFailureType_Type(Integer32):
    """Custom type cLApIfUpDownFailureType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detectedFailure", 1),
          ("configuredReset", 2))
    )


_CLApIfUpDownFailureType_Type.__name__ = "Integer32"
_CLApIfUpDownFailureType_Object = MibScalar
cLApIfUpDownFailureType = _CLApIfUpDownFailureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 8),
    _CLApIfUpDownFailureType_Type()
)
cLApIfUpDownFailureType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfUpDownFailureType.setStatus("current")
_CLApIfUpDownCause_Type = SnmpAdminString
_CLApIfUpDownCause_Object = MibScalar
cLApIfUpDownCause = _CLApIfUpDownCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 9),
    _CLApIfUpDownCause_Type()
)
cLApIfUpDownCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfUpDownCause.setStatus("current")
_CLApIfUpDownFailureCode_Type = SnmpAdminString
_CLApIfUpDownFailureCode_Object = MibScalar
cLApIfUpDownFailureCode = _CLApIfUpDownFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 10),
    _CLApIfUpDownFailureCode_Type()
)
cLApIfUpDownFailureCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfUpDownFailureCode.setStatus("current")
_CLApAlarmSet_Type = TruthValue
_CLApAlarmSet_Object = MibScalar
cLApAlarmSet = _CLApAlarmSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 11),
    _CLApAlarmSet_Type()
)
cLApAlarmSet.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApAlarmSet.setStatus("current")


class _CLApRogueClassType_Type(Integer32):
    """Custom type cLApRogueClassType based on Integer32"""
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
        *(("pending", 0),
          ("friendly", 1),
          ("malicious", 2),
          ("unclassified", 3),
          ("custom", 4))
    )


_CLApRogueClassType_Type.__name__ = "Integer32"
_CLApRogueClassType_Object = MibScalar
cLApRogueClassType = _CLApRogueClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 12),
    _CLApRogueClassType_Type()
)
cLApRogueClassType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueClassType.setStatus("current")
_CLApRogueDetectedChannel_Type = CLDot11Channel
_CLApRogueDetectedChannel_Object = MibScalar
cLApRogueDetectedChannel = _CLApRogueDetectedChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 13),
    _CLApRogueDetectedChannel_Type()
)
cLApRogueDetectedChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueDetectedChannel.setStatus("current")
_CLApRSSI_Type = Integer32
_CLApRSSI_Object = MibScalar
cLApRSSI = _CLApRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 14),
    _CLApRSSI_Type()
)
cLApRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRSSI.setStatus("current")
_CLApSNR_Type = Integer32
_CLApSNR_Object = MibScalar
cLApSNR = _CLApSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 15),
    _CLApSNR_Type()
)
cLApSNR.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApSNR.setStatus("current")
_CLApDot11RadioCurrentChannel_Type = CLDot11Channel
_CLApDot11RadioCurrentChannel_Object = MibScalar
cLApDot11RadioCurrentChannel = _CLApDot11RadioCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 16),
    _CLApDot11RadioCurrentChannel_Type()
)
cLApDot11RadioCurrentChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApDot11RadioCurrentChannel.setStatus("current")
_CLApAdhocRogue_Type = TruthValue
_CLApAdhocRogue_Object = MibScalar
cLApAdhocRogue = _CLApAdhocRogue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 17),
    _CLApAdhocRogue_Type()
)
cLApAdhocRogue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApAdhocRogue.setStatus("current")
_CLApRogueAPOnWiredNetwork_Type = TruthValue
_CLApRogueAPOnWiredNetwork_Object = MibScalar
cLApRogueAPOnWiredNetwork = _CLApRogueAPOnWiredNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 18),
    _CLApRogueAPOnWiredNetwork_Type()
)
cLApRogueAPOnWiredNetwork.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueAPOnWiredNetwork.setStatus("current")


class _CLApRogueMode_Type(Integer32):
    """Custom type cLApRogueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("initializing", 0),
          ("pending", 1),
          ("alert", 2),
          ("detectedLrad", 3),
          ("known", 4),
          ("acknowledge", 5),
          ("contained", 6),
          ("threat", 7),
          ("containedPending", 8),
          ("knownContained", 9),
          ("trustedMissing", 10))
    )


_CLApRogueMode_Type.__name__ = "Integer32"
_CLApRogueMode_Object = MibScalar
cLApRogueMode = _CLApRogueMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 19),
    _CLApRogueMode_Type()
)
cLApRogueMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueMode.setStatus("current")
_CLApRogueIsClassifiedByRule_Type = TruthValue
_CLApRogueIsClassifiedByRule_Object = MibScalar
cLApRogueIsClassifiedByRule = _CLApRogueIsClassifiedByRule_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 20),
    _CLApRogueIsClassifiedByRule_Type()
)
cLApRogueIsClassifiedByRule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueIsClassifiedByRule.setStatus("current")
_CLApRogueClassifiedApMacAddress_Type = MacAddress
_CLApRogueClassifiedApMacAddress_Object = MibScalar
cLApRogueClassifiedApMacAddress = _CLApRogueClassifiedApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 21),
    _CLApRogueClassifiedApMacAddress_Type()
)
cLApRogueClassifiedApMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueClassifiedApMacAddress.setStatus("current")
_CLApRogueClassifiedRSSI_Type = Integer32
_CLApRogueClassifiedRSSI_Object = MibScalar
cLApRogueClassifiedRSSI = _CLApRogueClassifiedRSSI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 22),
    _CLApRogueClassifiedRSSI_Type()
)
cLApRogueClassifiedRSSI.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueClassifiedRSSI.setStatus("current")
_CLAPPreviousMonitorMode_Type = CLApMode
_CLAPPreviousMonitorMode_Object = MibScalar
cLAPPreviousMonitorMode = _CLAPPreviousMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 23),
    _CLAPPreviousMonitorMode_Type()
)
cLAPPreviousMonitorMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLAPPreviousMonitorMode.setStatus("current")
_CLAPCurrentMonitorMode_Type = CLApMode
_CLAPCurrentMonitorMode_Object = MibScalar
cLAPCurrentMonitorMode = _CLAPCurrentMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 24),
    _CLAPCurrentMonitorMode_Type()
)
cLAPCurrentMonitorMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLAPCurrentMonitorMode.setStatus("current")
_CLApSsidKeyConfSsidA_Type = SnmpAdminString
_CLApSsidKeyConfSsidA_Object = MibScalar
cLApSsidKeyConfSsidA = _CLApSsidKeyConfSsidA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 25),
    _CLApSsidKeyConfSsidA_Type()
)
cLApSsidKeyConfSsidA.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApSsidKeyConfSsidA.setStatus("current")
_CLApSsidKeyConfKeyIdxA_Type = Unsigned32
_CLApSsidKeyConfKeyIdxA_Object = MibScalar
cLApSsidKeyConfKeyIdxA = _CLApSsidKeyConfKeyIdxA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 26),
    _CLApSsidKeyConfKeyIdxA_Type()
)
cLApSsidKeyConfKeyIdxA.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApSsidKeyConfKeyIdxA.setStatus("current")
_CLApSsidKeyConfSsidB_Type = SnmpAdminString
_CLApSsidKeyConfSsidB_Object = MibScalar
cLApSsidKeyConfSsidB = _CLApSsidKeyConfSsidB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 27),
    _CLApSsidKeyConfSsidB_Type()
)
cLApSsidKeyConfSsidB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApSsidKeyConfSsidB.setStatus("current")
_CLApSsidKeyConfKeyIdxB_Type = Unsigned32
_CLApSsidKeyConfKeyIdxB_Object = MibScalar
cLApSsidKeyConfKeyIdxB = _CLApSsidKeyConfKeyIdxB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 28),
    _CLApSsidKeyConfKeyIdxB_Type()
)
cLApSsidKeyConfKeyIdxB.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApSsidKeyConfKeyIdxB.setStatus("current")
_CLApPreviousChannel_Type = Unsigned32
_CLApPreviousChannel_Object = MibScalar
cLApPreviousChannel = _CLApPreviousChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 29),
    _CLApPreviousChannel_Type()
)
cLApPreviousChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApPreviousChannel.setStatus("current")
_CLApCurrentChannel_Type = Unsigned32
_CLApCurrentChannel_Object = MibScalar
cLApCurrentChannel = _CLApCurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 30),
    _CLApCurrentChannel_Type()
)
cLApCurrentChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApCurrentChannel.setStatus("current")


class _CLApChannelCustomize_Type(Integer32):
    """Custom type cLApChannelCustomize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("customized", 2))
    )


_CLApChannelCustomize_Type.__name__ = "Integer32"
_CLApChannelCustomize_Object = MibScalar
cLApChannelCustomize = _CLApChannelCustomize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 31),
    _CLApChannelCustomize_Type()
)
cLApChannelCustomize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApChannelCustomize.setStatus("current")


class _CLApIfLoadChannelUtilization_Type(Integer32):
    """Custom type cLApIfLoadChannelUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CLApIfLoadChannelUtilization_Type.__name__ = "Integer32"
_CLApIfLoadChannelUtilization_Object = MibScalar
cLApIfLoadChannelUtilization = _CLApIfLoadChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 32),
    _CLApIfLoadChannelUtilization_Type()
)
cLApIfLoadChannelUtilization.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApIfLoadChannelUtilization.setStatus("current")


class _CLAPGroupVlanName_Type(OctetString):
    """Custom type cLAPGroupVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CLAPGroupVlanName_Type.__name__ = "OctetString"
_CLAPGroupVlanName_Object = MibScalar
cLAPGroupVlanName = _CLAPGroupVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 33),
    _CLAPGroupVlanName_Type()
)
cLAPGroupVlanName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLAPGroupVlanName.setStatus("current")


class _CLApRuleName_Type(SnmpAdminString):
    """Custom type cLApRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLApRuleName_Type.__name__ = "SnmpAdminString"
_CLApRuleName_Object = MibScalar
cLApRuleName = _CLApRuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 34),
    _CLApRuleName_Type()
)
cLApRuleName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRuleName.setStatus("current")
_CLApSeverityScore_Type = Unsigned32
_CLApSeverityScore_Object = MibScalar
cLApSeverityScore = _CLApSeverityScore_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 35),
    _CLApSeverityScore_Type()
)
cLApSeverityScore.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApSeverityScore.setStatus("current")


class _CLApDot11XorRadioRoleChangeReason_Type(Integer32):
    """Custom type cLApDot11XorRadioRoleChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto", 2),
          ("manual", 3))
    )


_CLApDot11XorRadioRoleChangeReason_Type.__name__ = "Integer32"
_CLApDot11XorRadioRoleChangeReason_Object = MibScalar
cLApDot11XorRadioRoleChangeReason = _CLApDot11XorRadioRoleChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 36),
    _CLApDot11XorRadioRoleChangeReason_Type()
)
cLApDot11XorRadioRoleChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApDot11XorRadioRoleChangeReason.setStatus("current")


class _CLApDot11XorRadioBandChangeReason_Type(Integer32):
    """Custom type cLApDot11XorRadioBandChangeReason based on Integer32"""
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
        *(("none", 1),
          ("coverageHole", 2),
          ("hyperlocation", 3),
          ("revert", 4),
          ("fra", 5),
          ("manual", 6))
    )


_CLApDot11XorRadioBandChangeReason_Type.__name__ = "Integer32"
_CLApDot11XorRadioBandChangeReason_Object = MibScalar
cLApDot11XorRadioBandChangeReason = _CLApDot11XorRadioBandChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 37),
    _CLApDot11XorRadioBandChangeReason_Type()
)
cLApDot11XorRadioBandChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApDot11XorRadioBandChangeReason.setStatus("current")


class _CLApBrokenAntApName_Type(OctetString):
    """Custom type cLApBrokenAntApName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApBrokenAntApName_Type.__name__ = "OctetString"
_CLApBrokenAntApName_Object = MibScalar
cLApBrokenAntApName = _CLApBrokenAntApName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 38),
    _CLApBrokenAntApName_Type()
)
cLApBrokenAntApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApBrokenAntApName.setStatus("current")


class _CLApBrokenAntInfo_Type(OctetString):
    """Custom type cLApBrokenAntInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CLApBrokenAntInfo_Type.__name__ = "OctetString"
_CLApBrokenAntInfo_Object = MibScalar
cLApBrokenAntInfo = _CLApBrokenAntInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 39),
    _CLApBrokenAntInfo_Type()
)
cLApBrokenAntInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApBrokenAntInfo.setStatus("current")
_CLApRogueDot11RadioBand_Type = CLDot11Band
_CLApRogueDot11RadioBand_Object = MibScalar
cLApRogueDot11RadioBand = _CLApRogueDot11RadioBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 3, 40),
    _CLApRogueDot11RadioBand_Type()
)
cLApRogueDot11RadioBand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLApRogueDot11RadioBand.setStatus("current")

# Managed Objects groups

ciscoLwappApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 1)
)
ciscoLwappApGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxNumberOfDot11Slots"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfSmtDot11Bssid"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroup.setStatus("current")

ciscoLwappApIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 2)
)
ciscoLwappApIfGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType")
)
if mibBuilder.loadTexts:
    ciscoLwappApIfGroup.setStatus("current")

ciscoLwappApGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 3)
)
ciscoLwappApGroupSup1.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApEntPhysicalIndex")
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup1.setStatus("current")

ciscoLwappApGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 4)
)
ciscoLwappApGroupSup2.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup2.setStatus("current")

ciscoLwappApGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 5)
)
ciscoLwappApGroupSup3.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11IfRegDomain"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11nSupport"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11nChannelBandwidth"),
        ("CISCO-LWAPP-AP-MIB", "cLApCountryCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApCountryAllowed"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup3.setStatus("current")

ciscoLwappApNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 6)
)
ciscoLwappApNotifObjsGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApAssocFailureReason")
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifObjsGroup.setStatus("current")

ciscoLwappApGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 8)
)
ciscoLwappApGroupSup4.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappJoinTakenTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxNumberOfEthernetSlots"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFirstChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomSecondChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomThirdChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFourthChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialEnableGlobalCredentials"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCrashEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupportedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociatedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimedDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApExtensionChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLAdjChannelRogueEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwLegacyBeamForming"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileFastHbTimerEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup4.setStatus("deprecated")

ciscoLwappApEthernetIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 9)
)
ciscoLwappApEthernetIfGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApEthernetIfName"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOperStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxUcastPkts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxNUcastPkts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxUcastPkts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxNUcastPkts"))
)
if mibBuilder.loadTexts:
    ciscoLwappApEthernetIfGroup.setStatus("current")

ciscoLwappApRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 10)
)
ciscoLwappApRadioGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMACAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSubBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IsBackhaul"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRole"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSubType"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRadioGroup.setStatus("current")

ciscoLwappApGroupSup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 11)
)
ciscoLwappApGroupSup5.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApGlobalFailoverPriority"),
        ("CISCO-LWAPP-AP-MIB", "cLApFailoverPriority"),
        ("CISCO-LWAPP-AP-MIB", "cLApEncryptionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyReset"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyStatsCurrent"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyStatsMin"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyStatsMax"),
        ("CISCO-LWAPP-AP-MIB", "cLApLinkLatencyTimeStamp"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup5.setStatus("current")

ciscoLwappSeClientSup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 12)
)
ciscoLwappSeClientSup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSeClientUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientIPAddrType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientIPAddr"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientDuration"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeClientPort"))
)
if mibBuilder.loadTexts:
    ciscoLwappSeClientSup.setStatus("current")

ciscoLwappDot11IfAntennaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 13)
)
ciscoLwappDot11IfAntennaGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaEnable")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11IfAntennaGroup.setStatus("current")

ciscoLwappRetransmitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 14)
)
ciscoLwappRetransmitGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApRetransmitTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalRetransmitTimeout"))
)
if mibBuilder.loadTexts:
    ciscoLwappRetransmitGroup.setStatus("current")

ciscoLwappApGroupSup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 15)
)
ciscoLwappApGroupSup6.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappUpTime"),
        ("CISCO-LWAPP-AP-MIB", "cLLwappJoinTakenTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxNumberOfEthernetSlots"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFirstChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomSecondChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomThirdChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApLomFourthChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApCredentialEnableGlobalCredentials"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApFastHbTimerEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCrashEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupportedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociatedEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApPrimedDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalPreferMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup6.setStatus("current")

ciscoLwappApGroupSup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 17)
)
ciscoLwappApGroupSup7.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApTelnetEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApSshEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreStdStateEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPwrInjectorStateEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApPwrInjectorSelection"),
        ("CISCO-LWAPP-AP-MIB", "cLApPwrInjectorSwMacAddr"),
        ("CISCO-LWAPP-AP-MIB", "cLApMonitorModeOptimization"),
        ("CISCO-LWAPP-AP-MIB", "cLApDomainName"),
        ("CISCO-LWAPP-AP-MIB", "cLApNameServerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApAMSDUEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApEncryptionSupported"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectionEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCdpOverAirEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfCdpEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalDot11IfCdpEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalEthernetIfCdpEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanIfMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanIfEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanIfNativeVlanId"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xAuthenticationEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xSupplicantPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xSupplicantUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobal802dot1xSupplicantEapType"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverrideEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverrideUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverridePassword"),
        ("CISCO-LWAPP-AP-MIB", "cLAp802dot1xSupplicantOverrideEapType"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwTxPowerThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApVlanListRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup7.setStatus("current")

ciscoLwappApGroupSup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 18)
)
ciscoLwappApGroupSup8.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11acSupport"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11ChannelBandwidth"),
        ("CISCO-LWAPP-AP-MIB", "cLApExtensionChannels"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalMaxApsSupported"),
        ("CISCO-LWAPP-AP-MIB", "cLApAuthorizeApMacAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApAuthorizeApSerialNumAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApAuthorizeApMethodList"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPAuditReport"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPAuditReportInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPConnectCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAuthorizeApMacMethodList"),
        ("CISCO-LWAPP-AP-MIB", "cLApAuthorizeApSerialNumMethodList"),
        ("CISCO-LWAPP-AP-MIB", "clApImageUpgradeHttpsEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup8.setStatus("current")

ciscoLwappApGroupSup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 20)
)
ciscoLwappApGroupSup9.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSecureCipher"),
        ("CISCO-LWAPP-AP-MIB", "cLApAntennaBandMode"),
        ("CISCO-LWAPP-AP-MIB", "cLAPNtpInfoState"),
        ("CISCO-LWAPP-AP-MIB", "cLApNtpInfoStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLAPNtpInfoStratum"),
        ("CISCO-LWAPP-AP-MIB", "cLAPNtpInfoLastSync"),
        ("CISCO-LWAPP-AP-MIB", "cLAPNtpInfoOffset"),
        ("CISCO-LWAPP-AP-MIB", "cLAPNtpInfoIPAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLAPNtpInfoIPAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup9.setStatus("current")

ciscoLwappApRadioGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 21)
)
ciscoLwappApRadioGroupSup1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11RadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSubType"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRadioGroupSup1.setStatus("current")

ciscoLwappHaloBleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 22)
)
ciscoLwappHaloBleGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLHaloGlobalBleBeaconInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLHaloGlobalBleBeaconUuid"),
        ("CISCO-LWAPP-AP-MIB", "cLHaloGlobalBleBeaconTxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLHaloGlobalBleBeaconEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaloBleGroup.setStatus("current")

ciscoLwappApBleBeaconGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 23)
)
ciscoLwappApBleBeaconGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApBleBeaconMajorField"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconMinorField"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconTxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconUuid"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconApplyGlobal"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleBeaconAdvTxPower"))
)
if mibBuilder.loadTexts:
    ciscoLwappApBleBeaconGroup.setStatus("current")

ciscoLwappApLanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 24)
)
ciscoLwappApLanStatsGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApLanPortState"),
        ("CISCO-LWAPP-AP-MIB", "cLApLanPortVlanId"),
        ("CISCO-LWAPP-AP-MIB", "cLApLanPortVlanIdValid"),
        ("CISCO-LWAPP-AP-MIB", "cLApLanPoeState"),
        ("CISCO-LWAPP-AP-MIB", "cLApLanOverride"))
)
if mibBuilder.loadTexts:
    ciscoLwappApLanStatsGroup.setStatus("current")

ciscoLwappApGroupSup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 25)
)
ciscoLwappApGroupSup10.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApPowerStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApNameServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataEncryptionStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApNsiKey"),
        ("CISCO-LWAPP-AP-MIB", "cLApPortNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueGroup"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueName"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigLanguage"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDState"),
        ("CISCO-LWAPP-AP-MIB", "cLApRealTimeStatsModeEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApTrunkVlan"),
        ("CISCO-LWAPP-AP-MIB", "cLApTrunkVlanStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLocation"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailResourceCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssociatedClientCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryAverageUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuAverageUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFromVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeToVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFailureCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitNumberTrap"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitSet"),
        ("CISCO-LWAPP-AP-MIB", "cLApFloorLabel"),
        ("CISCO-LWAPP-AP-MIB", "cLApConnectCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApReassocSuccCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApReassocFailCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailCountByRate"),
        ("CISCO-LWAPP-AP-MIB", "cLApAbnormalOfflineCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApActiveClientCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailCountForRssiLow"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysNetId"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailTimes"),
        ("CISCO-LWAPP-AP-MIB", "cLApHeartBeatRspAvgTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApEchoRequestCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApEchoResponseLossCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApModuleInserted"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnableModule"),
        ("CISCO-LWAPP-AP-MIB", "cLApIsUniversal"),
        ("CISCO-LWAPP-AP-MIB", "cLApUniversalPrimeStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApIsMaster"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleFWDownloadStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorDartConnectorStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaTxEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaRxEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfDuplex"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfLinkSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfPOEPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxTotalBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxTotalBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputCrc"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputAborts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputErrors"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputFrames"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputOverrun"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputDrops"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputResource"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfUnknownProtocol"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRunts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfGiants"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfThrottle"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfResets"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputCollision"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputNoBuffer"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputResource"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputUnderrun"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputErrors"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputTotalDrops"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsCurrent"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsMin"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsMax"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyTimeStamp"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpDefaultPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpState"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpListenerMinHoldtime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpListenerMaxHoldtime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpReconcilePeriod"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpRetryPeriod"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpSpeakerHoldTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpSpeakerKeepAlive"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsInlineTagStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSgaclStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsOverrideStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApModeClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApSiteTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRfTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPolicyTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApTagSource"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleState"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleProductId"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbDescription"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbStateInfo"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbOverride"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbSerialNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbMaxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApLagConfigStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApMonitorModeOptStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLegacyBeamForming"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfLinkChangeCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11MaxClients"),
        ("CISCO-LWAPP-AP-MIB", "cLApPromiscuousModeDwelling"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfStaKeepingTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfLinkSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfMtu"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDesc"),
        ("CISCO-LWAPP-AP-MIB", "cLAPDot11IfMinTxPowerStep"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfMaxDataRate"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfMtu"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfLinkChangeCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsTxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsTxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRetransmitNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsAssocClientNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsOnlineUserNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApHyperlocationAdminState"),
        ("CISCO-LWAPP-AP-MIB", "cLApHyperlocationUnsetFlag"),
        ("CISCO-LWAPP-AP-MIB", "cLApOeapDisableLocalAccess"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalLEDState"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioInterfaceShutdownEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetInterfaceDowntime"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastGroupAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastGroupAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPLagCapability"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPDtlsVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPDtlsCipherSuite"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanInfoMaxClients"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioWlanSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioWlanBssid"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwTxPowerThresholdVer2"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxErrorFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsMacMicErrFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsMacDecryptErrFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxMgmtFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxCtrlFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxDataFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxMgmtFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxCtrlFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRetryFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRetryPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiHighest"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiLowest"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiAverage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileTimeStamp"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDFlashStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDFlashDuration"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6AddressEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6InetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6InetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6PrefixLength"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6GatewayInetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6GatewayInetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpNetmaskType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpNetmask"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreferMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreferModeApplied"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMemType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMemSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysFlashSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysCpuType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysFlashType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsRxPackets"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsRxBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsTxPackets"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsTxBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateString"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerPath"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpClassifier"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpBufferSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpCaptureTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpTruncation"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpDeviceMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpStartStop"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSsidName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmSwVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmSerialNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmUsChannelStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmDsChannelStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmMaskBit"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvTemperatureDegree"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvTemperatureState"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvOrientation"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvPoeOutStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLocationPresent"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLocationValid"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLatitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLongitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsAltitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsCollectionTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApAlarmSet"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApSNR"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdhocRogue"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueAPOnWiredNetwork"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueIsClassifiedByRule"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLAPPreviousMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLAPCurrentMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidB"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxB"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreviousChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApChannelCustomize"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLAPGroupVlanName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeverityScore"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleChangeReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBandChangeReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup10.setStatus("deprecated")

ciscoLwappApXorRadioGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 26)
)
ciscoLwappApXorRadioGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleAssignment"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappXorRadioRoleChangeEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSensorReachability"),
        ("CISCO-LWAPP-AP-MIB", "cLApFraCoverageOverlapFactor"),
        ("CISCO-LWAPP-AP-MIB", "cLApFraSuggestedMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappApXorRadioGroup.setStatus("deprecated")

ciscoLwappApGroupSup11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 28)
)
ciscoLwappApGroupSup11.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApDot11axSupport")
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup11.setStatus("current")

ciscoLwappApProfileHaloBleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 29)
)
ciscoLwappApProfileHaloBleGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconTxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconUuid"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconTxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconAdvertisedPwr"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileHaloBleGroup.setStatus("current")

ciscoLwappApProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 30)
)
ciscoLwappApProfileGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileRowStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialEnableGlobalCredentials"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileLinkLatencyEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRetransmitTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileOeapDisableLocalAccess"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileLedState"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRadioInterfaceShutdownEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileEthernetInterfaceDowntime"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastGroupAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastGroupAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePrimedJoinTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePreferMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApLagEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xAuthenticationEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileEncryptionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTelnetEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileSshEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationDetectionThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationResetThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationTriggerThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationNtpIpAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationNtpIpAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileAdjustMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHeartBeatTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCdpEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApPacketCaptureProfile"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueReportInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueMinimumRssi"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueTransientInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueContainFlexconnect"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueContainAutoRateEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueDetectionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileReportInterval24ghz"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileReportInterval5ghz"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDot1xApSwitchEapAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDot1xApSwtichLscAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMeshProfileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileUsbStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileVlanTagging"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApCountryCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileExtModuleEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileStatsTimer"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoePreStandardSwitchFlag"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoePowerInjectorSelection"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoeInjectorSwitchMac"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconAdvertisedPwr"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpTftpAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpTftpAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpCoreFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupFallbackEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileGroup.setStatus("deprecated")

ciscoLwappApPacketCaptureProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 31)
)
ciscoLwappApPacketCaptureProfileGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileRowStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileBufferSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileDuration"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileTruncation"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileFtpServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileFtpServerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileFtpServerPath"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileFtpUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileFtpPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierArp"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierBroadcast"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierControl"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierData"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierDot1x"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierIapp"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierIp"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierManagement"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierMulticast"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierTcp"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierUdp"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierTcpPort"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureProfileClassifierUdpPort"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureApDeviceMac"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureApStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApPacketCaptureProfileGroup.setStatus("current")

ciscoLwappApPacketCaptureClientProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 32)
)
ciscoLwappApPacketCaptureClientProfileGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureClientApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureClientAutoMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureClientStartStop"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureClientSiteName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketCaptureClientRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApPacketCaptureClientProfileGroup.setStatus("current")

ciscoLwappApProfileGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 33)
)
ciscoLwappApProfileGroupSup1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileRowStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileLinkLatencyEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRetransmitTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileLedState"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastGroupAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastGroupAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePrimedJoinTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePreferMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApLagEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileEncryptionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTelnetEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileSshEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationDetectionThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationResetThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationTriggerThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationNtpIpAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationNtpIpAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileAdjustMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHeartBeatTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCdpEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApPacketCaptureProfile"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueReportInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueMinimumRssi"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueTransientInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueContainFlexconnect"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueContainAutoRateEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueDetectionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileReportInterval24ghz"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileReportInterval5ghz"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDot1xApSwitchEapAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDot1xApSwtichLscAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMeshProfileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileUsbStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileExtModuleEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileStatsTimer"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoePreStandardSwitchFlag"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoePowerInjectorSelection"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoeInjectorSwitchMac"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconAdvertisedPwr"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpTftpAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpTftpAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpCoreFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupFallbackEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileGroupSup1.setStatus("deprecated")

ciscoLwappApProfileQosMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 34)
)
ciscoLwappApProfileQosMapGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapRangeUP"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapRangeDSCPLower"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapRangeDSCPUpper"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapRangeUPToDSCP"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapRangeRowStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapExceptionDSCP"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapExceptionUP"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQosMapExceptionRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileQosMapGroup.setStatus("current")

ciscoLwappApProfileGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 35)
)
ciscoLwappApProfileGroupSup2.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileRowStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalUserName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalSecret"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileLinkLatencyEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileFastHbTimerTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePrimaryDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupPrimaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupSecondaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupTertiaryControllerName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTcpMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRetransmitCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRetransmitTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileLedState"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastGroupAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastGroupAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMulticastMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePrimedJoinTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePreferMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApLagEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileEncryptionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTelnetEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileSshEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationDetectionThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationResetThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationTriggerThreshold"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationNtpIpAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHyperlocationNtpIpAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileAdjustMss"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDiscoveryTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHeartBeatTimeout"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCdpEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileApPacketCaptureProfile"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueReportInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueMinimumRssi"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueTransientInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueContainFlexconnect"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueContainAutoRateEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileRogueDetectionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileReportInterval24ghz"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileReportInterval5ghz"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDot1xApSwitchEapAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDot1xApSwtichLscAuth"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMeshProfileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileUsbStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileExtModuleEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileStatsTimer"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoePreStandardSwitchFlag"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoePowerInjectorSelection"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePoeInjectorSwitchMac"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconAdvertisedPwr"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileTftpDownGradeFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpTftpAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpTftpAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCoreDumpCoreFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBackupFallbackEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileClientRssiStatsEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileClientRssiStatsReportInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileGasRateLimitEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileGasRateLimitNumReqPerInterval"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileGasRateLimitIntervalMsec"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileQoSMapApTrustsUpstreamDSCP"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileGroupSup2.setStatus("current")

ciscoLwappApGroupSup12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 36)
)
ciscoLwappApGroupSup12.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApPowerStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApNameServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataEncryptionStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApNsiKey"),
        ("CISCO-LWAPP-AP-MIB", "cLApPortNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueGroup"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueName"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigLanguage"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDState"),
        ("CISCO-LWAPP-AP-MIB", "cLApRealTimeStatsModeEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApTrunkVlan"),
        ("CISCO-LWAPP-AP-MIB", "cLApTrunkVlanStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLocation"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailResourceCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssociatedClientCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryAverageUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuAverageUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFromVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeToVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFailureCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitNumberTrap"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitSet"),
        ("CISCO-LWAPP-AP-MIB", "cLApFloorLabel"),
        ("CISCO-LWAPP-AP-MIB", "cLApConnectCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApReassocSuccCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApReassocFailCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailCountByRate"),
        ("CISCO-LWAPP-AP-MIB", "cLApAbnormalOfflineCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApActiveClientCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailCountForRssiLow"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysNetId"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailTimes"),
        ("CISCO-LWAPP-AP-MIB", "cLApHeartBeatRspAvgTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApEchoRequestCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApEchoResponseLossCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApModuleInserted"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnableModule"),
        ("CISCO-LWAPP-AP-MIB", "cLApIsUniversal"),
        ("CISCO-LWAPP-AP-MIB", "cLApUniversalPrimeStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApIsMaster"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleFWDownloadStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorDartConnectorStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaTxEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaRxEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfDuplex"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfLinkSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfPOEPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxTotalBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxTotalBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputCrc"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputAborts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputErrors"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputFrames"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputOverrun"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputDrops"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputResource"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfUnknownProtocol"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRunts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfGiants"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfThrottle"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfResets"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputCollision"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputNoBuffer"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputResource"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputUnderrun"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputErrors"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputTotalDrops"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsCurrent"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsMin"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsMax"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyTimeStamp"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpDefaultPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpState"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpListenerMinHoldtime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpListenerMaxHoldtime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpReconcilePeriod"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpRetryPeriod"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpSpeakerHoldTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpSpeakerKeepAlive"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsInlineTagStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSgaclStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsOverrideStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApModeClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApSiteTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRfTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPolicyTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApTagSource"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleState"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleProductId"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbDescription"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbStateInfo"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbOverride"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbSerialNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbMaxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApLagConfigStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApMonitorModeOptStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLegacyBeamForming"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfLinkChangeCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11MaxClients"),
        ("CISCO-LWAPP-AP-MIB", "cLApPromiscuousModeDwelling"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfStaKeepingTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfLinkSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfMtu"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDesc"),
        ("CISCO-LWAPP-AP-MIB", "cLAPDot11IfMinTxPowerStep"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfMaxDataRate"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfMtu"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfLinkChangeCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsTxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsTxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRetransmitNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsAssocClientNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsOnlineUserNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApHyperlocationAdminState"),
        ("CISCO-LWAPP-AP-MIB", "cLApHyperlocationUnsetFlag"),
        ("CISCO-LWAPP-AP-MIB", "cLApOeapDisableLocalAccess"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalLEDState"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioInterfaceShutdownEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetInterfaceDowntime"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastGroupAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastGroupAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPLagCapability"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPDtlsVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPDtlsCipherSuite"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanInfoMaxClients"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioWlanSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioWlanBssid"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwTxPowerThresholdVer2"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxErrorFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsMacMicErrFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsMacDecryptErrFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxMgmtFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxCtrlFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxDataFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxMgmtFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxCtrlFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRetryFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRetryPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiHighest"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiLowest"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiAverage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileTimeStamp"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDFlashStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDFlashDuration"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6AddressEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6InetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6InetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6PrefixLength"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6GatewayInetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6GatewayInetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpNetmaskType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpNetmask"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreferMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreferModeApplied"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMemType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMemSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysFlashSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysCpuType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysFlashType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsRxPackets"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsRxBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsTxPackets"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsTxBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateString"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerPath"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpClassifier"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpBufferSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpCaptureTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpTruncation"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpDeviceMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpStartStop"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSsidName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmSwVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmSerialNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmUsChannelStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmDsChannelStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmMaskBit"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvTemperatureDegree"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvTemperatureState"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvOrientation"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvPoeOutStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLocationPresent"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLocationValid"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLatitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLongitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsAltitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsCollectionTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApAlarmSet"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApSNR"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdhocRogue"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueAPOnWiredNetwork"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueIsClassifiedByRule"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLAPPreviousMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLAPCurrentMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidB"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxB"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreviousChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApChannelCustomize"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLAPGroupVlanName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeverityScore"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleChangeReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBandChangeReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup12.setStatus("deprecated")

ciscoLwappApGroupSup13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 37)
)
ciscoLwappApGroupSup13.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11IfPhyS80EightyChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfRptncPresent"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDartPresent"),
        ("CISCO-LWAPP-AP-MIB", "cLApFilterName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup13.setStatus("current")

ciscoLwappApLanStatsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 38)
)
ciscoLwappApLanStatsGroupSup1.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApLanPowerLevelId")
)
if mibBuilder.loadTexts:
    ciscoLwappApLanStatsGroupSup1.setStatus("current")

ciscoLwappApProfileGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 39)
)
ciscoLwappApProfileGroupSup3.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileUdpliteState"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMethodListName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileGroupSup3.setStatus("deprecated")

ciscoLwappApProfileHaloBleGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 40)
)
ciscoLwappApProfileHaloBleGroupSup1.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApProfileHaloBleBeaconRowStatus")
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileHaloBleGroupSup1.setStatus("current")

ciscoLwappAp11axGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 41)
)
ciscoLwappAp11axGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLAp11axDualRadioCapable"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axRadioFRACapable"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axDualRadioOperation"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axDualRadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axRadioRoleOperation"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axRadioRole"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axObssPdCapable"),
        ("CISCO-LWAPP-AP-MIB", "cLAp11axObssPdSrgCapable"))
)
if mibBuilder.loadTexts:
    ciscoLwappAp11axGroup.setStatus("current")

ciscoLwappApXorRadioGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 42)
)
ciscoLwappApXorRadioGroupSup1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleAssignment"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappXorRadioRoleChangeEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSensorReachability"),
        ("CISCO-LWAPP-AP-MIB", "cLApFraCoverageOverlapFactor"),
        ("CISCO-LWAPP-AP-MIB", "cLApFraSuggestedMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDualRadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDualRadioCapable"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfRadioFRACapable"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDualRadioOperation"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfRadioRoleOperation"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfRadioRole"))
)
if mibBuilder.loadTexts:
    ciscoLwappApXorRadioGroupSup1.setStatus("deprecated")

ciscoLwappApProfileGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 43)
)
ciscoLwappApProfileGroupSup4.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApProfileUdpliteState"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileMethodListName"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileWindowSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalSecretType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCredentialGlobalPasswordType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfile802dot1xSupplicantPasswordType"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBssidEnableStats"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileBssidStatsFrequency"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfilePersistentSsidBroadcastEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileDhcpFallback"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileOeapRogueDetectionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileOeapEncryptionEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileOeapLocalAccessEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileOeapProvSsidEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApProfileCountryCode"))
)
if mibBuilder.loadTexts:
    ciscoLwappApProfileGroupSup4.setStatus("current")

ciscoLwappApGroupSup14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 44)
)
ciscoLwappApGroupSup14.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApPowerStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApNameServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataEncryptionStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApNsiKey"),
        ("CISCO-LWAPP-AP-MIB", "cLApPortNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueGroup"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigVenueName"),
        ("CISCO-LWAPP-AP-MIB", "cLApVenueConfigLanguage"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDState"),
        ("CISCO-LWAPP-AP-MIB", "cLApRealTimeStatsModeEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApTrunkVlan"),
        ("CISCO-LWAPP-AP-MIB", "cLApTrunkVlanStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLocation"),
        ("CISCO-LWAPP-AP-MIB", "cLApSubMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailResourceCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssociatedClientCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryAverageUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuAverageUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFromVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeToVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFailureCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitNumberTrap"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitSet"),
        ("CISCO-LWAPP-AP-MIB", "cLApFloorLabel"),
        ("CISCO-LWAPP-AP-MIB", "cLApReassocSuccCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApReassocFailCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailCountByRate"),
        ("CISCO-LWAPP-AP-MIB", "cLApAbnormalOfflineCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApActiveClientCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailCountForRssiLow"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysNetId"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailTimes"),
        ("CISCO-LWAPP-AP-MIB", "cLApHeartBeatRspAvgTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApEchoRequestCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApEchoResponseLossCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApModuleInserted"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnableModule"),
        ("CISCO-LWAPP-AP-MIB", "cLApIsUniversal"),
        ("CISCO-LWAPP-AP-MIB", "cLApUniversalPrimeStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApIsMaster"),
        ("CISCO-LWAPP-AP-MIB", "cLApBleFWDownloadStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorDartConnectorStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaTxEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAntennaRxEnable"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfDuplex"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfLinkSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfPOEPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRxTotalBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfTxTotalBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputCrc"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputAborts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputErrors"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputFrames"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputOverrun"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputDrops"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfInputResource"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfUnknownProtocol"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfRunts"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfGiants"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfThrottle"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfResets"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputCollision"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputNoBuffer"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputResource"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputUnderrun"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputErrors"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfOutputTotalDrops"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsCurrent"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsMin"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyStatsMax"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataLinkLatencyTimeStamp"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpDefaultPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpState"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpListenerMinHoldtime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpListenerMaxHoldtime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpReconcilePeriod"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpRetryPeriod"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpSpeakerHoldTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSxpSpeakerKeepAlive"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsInlineTagStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsSgaclStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCtsOverrideStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApModeClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApSiteTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRfTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPolicyTagName"),
        ("CISCO-LWAPP-AP-MIB", "cLApTagSource"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleState"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbModuleProductId"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbDescription"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbStateInfo"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbOverride"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbSerialNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApUsbMaxPower"),
        ("CISCO-LWAPP-AP-MIB", "cLApLagConfigStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApMonitorModeOptStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLegacyBeamForming"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfLinkChangeCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11MaxClients"),
        ("CISCO-LWAPP-AP-MIB", "cLApPromiscuousModeDwelling"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfStaKeepingTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfLinkSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfMtu"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfDesc"),
        ("CISCO-LWAPP-AP-MIB", "cLAPDot11IfMinTxPowerStep"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfMaxDataRate"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfMtu"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfLinkChangeCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsTxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsTxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsRetransmitNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsAssocClientNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanStatsOnlineUserNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApHyperlocationAdminState"),
        ("CISCO-LWAPP-AP-MIB", "cLApHyperlocationUnsetFlag"),
        ("CISCO-LWAPP-AP-MIB", "cLApOeapDisableLocalAccess"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalLEDState"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioInterfaceShutdownEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetInterfaceDowntime"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastGroupAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastGroupAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLAPMulticastMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPLagCapability"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPDtlsVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApGlobalAPDtlsCipherSuite"),
        ("CISCO-LWAPP-AP-MIB", "cLApWlanInfoMaxClients"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioWlanSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRadioWlanBssid"),
        ("CISCO-LWAPP-AP-MIB", "cLApNwTxPowerThresholdVer2"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxErrorFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsMacMicErrFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsMacDecryptErrFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxMgmtFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxCtrlFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxDataFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxMgmtFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxCtrlFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsTxDataPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRetryFrameCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioStatsRetryPacketCount"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiHighest"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiLowest"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRssiAverage"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApCrashFileTimeStamp"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDFlashStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApLEDFlashDuration"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApInetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6AddressEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6InetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6InetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6PrefixLength"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6GatewayInetAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpv6GatewayInetAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpNetmaskType"),
        ("CISCO-LWAPP-AP-MIB", "cLApStaticIpNetmask"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreferMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreferModeApplied"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMemType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysMemSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysFlashSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysCpuType"),
        ("CISCO-LWAPP-AP-MIB", "cLApSysFlashType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsRxPackets"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsRxBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsTxPackets"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateStatsTxBytes"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioRateString"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerAddressType"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpServerPath"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpUsername"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpFtpPassword"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpClassifier"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpBufferSize"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpCaptureTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpTruncation"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpDeviceMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApPacketDumpStartStop"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioSsidName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmSwVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetSpeed"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmSerialNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmUsChannelStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmDsChannelStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApCmMaskBit"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvTemperatureDegree"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvTemperatureState"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvOrientation"),
        ("CISCO-LWAPP-AP-MIB", "cLApEnvPoeOutStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLocationPresent"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLocationValid"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLatitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsLongitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsAltitude"),
        ("CISCO-LWAPP-AP-MIB", "cLApGpsCollectionTime"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDot11RadioBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsClear"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApAlarmSet"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApSNR"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdhocRogue"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueAPOnWiredNetwork"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueIsClassifiedByRule"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLAPPreviousMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLAPCurrentMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidB"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxB"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreviousChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApChannelCustomize"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfLoadChannelUtilization"),
        ("CISCO-LWAPP-AP-MIB", "cLAPGroupVlanName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeverityScore"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleChangeReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBandChangeReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApBrokenAntApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApBrokenAntInfo"),
        ("CISCO-LWAPP-AP-MIB", "cLApIndoorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsTxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsTxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsRxPktNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsRxOctetNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsRetransmitNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsAssocClientNum"),
        ("CISCO-LWAPP-AP-MIB", "cLApSlotWlanStatsOnlineUserNum"))
)
if mibBuilder.loadTexts:
    ciscoLwappApGroupSup14.setStatus("current")

ciscoLwappApXorRadioGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 45)
)
ciscoLwappApXorRadioGroupSup2.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleAssignment"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappXorRadioRoleChangeEnabled"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSensorReachability"),
        ("CISCO-LWAPP-AP-MIB", "cLApFraCoverageOverlapFactor"),
        ("CISCO-LWAPP-AP-MIB", "cLApFraSuggestedMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappApXorRadioGroupSup2.setStatus("current")


# Notification objects

ciscoLwappApIfRegulatoryDomainMismatchNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 1)
)
ciscoLwappApIfRegulatoryDomainMismatchNotif.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfRegDomain"),
        ("CISCO-LWAPP-DOT11-MIB", "cldRegulatoryDomain"))
)
if mibBuilder.loadTexts:
    ciscoLwappApIfRegulatoryDomainMismatchNotif.setStatus(
        "current"
    )

ciscoLwappApCrash = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 2)
)
ciscoLwappApCrash.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappApCrash.setStatus(
        "obsolete"
    )

ciscoLwappApUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 3)
)
ciscoLwappApUnsupported.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApAssocFailureReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApUnsupported.setStatus(
        "current"
    )

ciscoLwappApAssociated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 4)
)
ciscoLwappApAssociated.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApLastRebootReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApDataEncryptionStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApAssociated.setStatus(
        "current"
    )

ciscoLwappApPower = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 5)
)
ciscoLwappApPower.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApPowerStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappApPower.setStatus(
        "current"
    )

ciscoLwappApRogueApDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 6)
)
ciscoLwappApRogueApDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDot11RadioBand"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRogueApDetected.setStatus(
        "current"
    )

ciscoLwappApRogueApCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 7)
)
ciscoLwappApRogueApCleared.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioChannelNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDot11RadioBand"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRogueApCleared.setStatus(
        "current"
    )

ciscoLwappApWipsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 8)
)
ciscoLwappApWipsNotification.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsReason"),
        ("CISCO-LWAPP-AP-MIB", "cLApWipsClear"))
)
if mibBuilder.loadTexts:
    ciscoLwappApWipsNotification.setStatus(
        "current"
    )

ciscoLwappApNoDownlinkChannelNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 9)
)
ciscoLwappApNoDownlinkChannelNotify.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappApNoDownlinkChannelNotify.setStatus(
        "current"
    )

ciscoLwappApIfUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 10)
)
ciscoLwappApIfUpNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApPortNumber"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApIfUpNotify.setStatus(
        "current"
    )

ciscoLwappApIfDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 11)
)
ciscoLwappApIfDownNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfAdminStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureType"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfUpDownFailureCode"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApIfDownNotify.setStatus(
        "current"
    )

ciscoLwappApClientThresholdNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 12)
)
ciscoLwappApClientThresholdNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileHighDensityMaxRadioClients"),
        ("CISCO-LWAPP-RF-MIB", "cLRFProfileHDClientTrapThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappApClientThresholdNotify.setStatus(
        "current"
    )

ciscoLwappApUpgradeFailureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 13)
)
ciscoLwappApUpgradeFailureNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFromVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeToVersion"),
        ("CISCO-LWAPP-AP-MIB", "cLApUpgradeFailureCause"))
)
if mibBuilder.loadTexts:
    ciscoLwappApUpgradeFailureNotify.setStatus(
        "current"
    )

ciscoLwappApCpuUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 14)
)
ciscoLwappApCpuUsageHigh.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApCpuCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappApCpuUsageHigh.setStatus(
        "current"
    )

ciscoLwappApMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 15)
)
ciscoLwappApMemoryUsageHigh.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApMemoryCurrentUsage"),
        ("CISCO-LWAPP-AP-MIB", "cLApAlarmSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMemoryUsageHigh.setStatus(
        "current"
    )

ciscoLwappApMaxClientLimitNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 16)
)
ciscoLwappApMaxClientLimitNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitNumberTrap"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitCause"),
        ("CISCO-LWAPP-AP-MIB", "cLApMaxClientLimitSet"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMaxClientLimitNotify.setStatus(
        "current"
    )

ciscoLwappApAdjChannelRogueDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 17)
)
ciscoLwappApAdjChannelRogueDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApSNR"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdhocRogue"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassType"))
)
if mibBuilder.loadTexts:
    ciscoLwappApAdjChannelRogueDetected.setStatus(
        "current"
    )

ciscoLwappApAdjChannelRogueCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 18)
)
ciscoLwappApAdjChannelRogueCleared.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappApAdjChannelRogueCleared.setStatus(
        "current"
    )

ciscoLwappApRogueDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 19)
)
ciscoLwappApRogueDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApSNR"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueAPOnWiredNetwork"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdhocRogue"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueMode"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueIsClassifiedByRule"),
        ("CISCO-LWAPP-AP-MIB", "cLApSeverityScore"),
        ("CISCO-LWAPP-AP-MIB", "cLApRuleName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassifiedRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDot11RadioBand"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRogueDetected.setStatus(
        "current"
    )

ciscoLwappApCurrentChannelRogueDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 20)
)
ciscoLwappApCurrentChannelRogueDetected.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApRSSI"),
        ("CISCO-LWAPP-AP-MIB", "cLApSNR"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApAdhocRogue"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApSsid"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueClassType"))
)
if mibBuilder.loadTexts:
    ciscoLwappApCurrentChannelRogueDetected.setStatus(
        "current"
    )

ciscoLwappApCurrentChannelRogueCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 21)
)
ciscoLwappApCurrentChannelRogueCleared.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueApMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApEthernetIfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApRogueDetectedChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11RadioCurrentChannel"))
)
if mibBuilder.loadTexts:
    ciscoLwappApCurrentChannelRogueCleared.setStatus(
        "current"
    )

ciscoLwappApMonitorModeChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 22)
)
ciscoLwappApMonitorModeChangeNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLAPPreviousMonitorMode"),
        ("CISCO-LWAPP-AP-MIB", "cLAPCurrentMonitorMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMonitorModeChangeNotify.setStatus(
        "current"
    )

ciscoLwappApAcTimeSyncFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 23)
)
ciscoLwappApAcTimeSyncFailureTrap.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappApAcTimeSyncFailureTrap.setStatus(
        "current"
    )

ciscoLwappApSsidKeyConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 24)
)
ciscoLwappApSsidKeyConflict.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApIfMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxA"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfSsidB"),
        ("CISCO-LWAPP-AP-MIB", "cLApSsidKeyConfKeyIdxB"))
)
if mibBuilder.loadTexts:
    ciscoLwappApSsidKeyConflict.setStatus(
        "current"
    )

ciscoLwappApCurrChannelChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 25)
)
ciscoLwappApCurrChannelChanged.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApPreviousChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApCurrentChannel"),
        ("CISCO-LWAPP-AP-MIB", "cLApChannelCustomize"))
)
if mibBuilder.loadTexts:
    ciscoLwappApCurrChannelChanged.setStatus(
        "current"
    )

ciscoLwappApCapwapRetransmissionQueueFullEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 26)
)
ciscoLwappApCapwapRetransmissionQueueFullEvent.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress")
)
if mibBuilder.loadTexts:
    ciscoLwappApCapwapRetransmissionQueueFullEvent.setStatus(
        "current"
    )

ciscoLwappApSystemBootupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 27)
)
ciscoLwappApSystemBootupEvent.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress")
)
if mibBuilder.loadTexts:
    ciscoLwappApSystemBootupEvent.setStatus(
        "current"
    )

ciscoLwappXmFilterCheckWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 28)
)
ciscoLwappXmFilterCheckWarning.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApName")
)
if mibBuilder.loadTexts:
    ciscoLwappXmFilterCheckWarning.setStatus(
        "current"
    )

ciscoLwappApModeUnsupportedOnFlexExpressEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 29)
)
ciscoLwappApModeUnsupportedOnFlexExpressEvent.setObjects(
    ("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress")
)
if mibBuilder.loadTexts:
    ciscoLwappApModeUnsupportedOnFlexExpressEvent.setStatus(
        "current"
    )

ciscoLwappApXorRadioRoleChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 30)
)
ciscoLwappApXorRadioRoleChangeNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioRoleChangeReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappApXorRadioRoleChangeNotify.setStatus(
        "current"
    )

ciscoLwappRadioBandChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 31)
)
ciscoLwappRadioBandChangeNotify.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBand"),
        ("CISCO-LWAPP-AP-MIB", "cLApDot11XorRadioBandChangeReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappRadioBandChangeNotify.setStatus(
        "current"
    )

ciscoLwappBrokenAntennaDetails = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 33)
)
ciscoLwappBrokenAntennaDetails.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApBrokenAntApName"),
        ("CISCO-LWAPP-AP-MIB", "cLApBrokenAntInfo"))
)
if mibBuilder.loadTexts:
    ciscoLwappBrokenAntennaDetails.setStatus(
        "current"
    )

ciscoLwappApRadioStuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 0, 34)
)
ciscoLwappApRadioStuck.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-AP-MIB", "bsnStationAPIfSlotId"))
)
if mibBuilder.loadTexts:
    ciscoLwappApRadioStuck.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappApNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 7)
)
ciscoLwappApNotifsGroup.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotif"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupported"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCrash"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociated"))
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifsGroup.setStatus(
        "deprecated"
    )

ciscoLwappApNotifsGroupVer1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 16)
)
ciscoLwappApNotifsGroupVer1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfRegulatoryDomainMismatchNotif"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUnsupported"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAssociated"))
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifsGroupVer1.setStatus(
        "current"
    )

ciscoLwappApNotifsGroupVer2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 19)
)
ciscoLwappApNotifsGroupVer2.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApPower"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRogueApDetected"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRogueApCleared"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApWipsNotification"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNoDownlinkChannelNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfUpNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfDownNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRadioBandChangeNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApModeUnsupportedOnFlexExpressEvent"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappXmFilterCheckWarning"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApSystemBootupEvent"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCapwapRetransmissionQueueFullEvent"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCurrChannelChanged"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApSsidKeyConflict"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAcTimeSyncFailureTrap"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApMonitorModeChangeNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCurrentChannelRogueCleared"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCurrentChannelRogueDetected"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRogueDetected"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAdjChannelRogueCleared"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApAdjChannelRogueDetected"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApMaxClientLimitNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApMemoryUsageHigh"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApCpuUsageHigh"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApUpgradeFailureNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApClientThresholdNotify"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappBrokenAntennaDetails"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioStuck"))
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifsGroupVer2.setStatus(
        "current"
    )

ciscoLwappApNotifsXorGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 2, 27)
)
ciscoLwappApNotifsXorGroup.setObjects(
    ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioRoleChangeNotify")
)
if mibBuilder.loadTexts:
    ciscoLwappApNotifsXorGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 1)
)
ciscoLwappApMIBCompliance.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 2)
)
ciscoLwappApMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 3)
)
ciscoLwappApMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 4)
)
ciscoLwappApMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup4"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup4"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 5)
)
ciscoLwappApMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup4"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 6)
)
ciscoLwappApMIBComplianceRev5.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup4"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 7)
)
ciscoLwappApMIBComplianceRev6.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup4"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 8)
)
ciscoLwappApMIBComplianceRev7.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup10"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev7.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 9)
)
ciscoLwappApMIBComplianceRev8.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup10"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev8.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 10)
)
ciscoLwappApMIBComplianceRev9.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup10"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev9.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 11)
)
ciscoLwappApMIBComplianceRev10.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup12"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileQosMapGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev10.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 12)
)
ciscoLwappApMIBComplianceRev11.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup11"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup12"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileQosMapGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup13"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappAp11axGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev11.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 13)
)
ciscoLwappApMIBComplianceRev12.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup11"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup12"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileQosMapGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup13"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappAp11axGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup4"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev12.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 14)
)
ciscoLwappApMIBComplianceRev13.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup11"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup14"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileQosMapGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup13"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappAp11axGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup4"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev13.setStatus(
        "deprecated"
    )

ciscoLwappApMIBComplianceRev14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 513, 2, 1, 15)
)
ciscoLwappApMIBComplianceRev14.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup3"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifObjsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup6"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup7"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApEthernetIfGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup5"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappSeClientSup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappDot11IfAntennaGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappRetransmitGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsGroupVer2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup8"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup9"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApRadioGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApBleBeaconGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup11"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup14"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApNotifsXorGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApPacketCaptureClientProfileGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileQosMapGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApGroupSup13"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappAp11axGroup"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileHaloBleGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApLanStatsGroupSup1"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApXorRadioGroupSup2"),
        ("CISCO-LWAPP-AP-MIB", "ciscoLwappApProfileGroupSup4"))
)
if mibBuilder.loadTexts:
    ciscoLwappApMIBComplianceRev14.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-AP-MIB",
    **{"ciscoLwappApMIB": ciscoLwappApMIB,
       "ciscoLwappApMIBNotifs": ciscoLwappApMIBNotifs,
       "ciscoLwappApIfRegulatoryDomainMismatchNotif": ciscoLwappApIfRegulatoryDomainMismatchNotif,
       "ciscoLwappApCrash": ciscoLwappApCrash,
       "ciscoLwappApUnsupported": ciscoLwappApUnsupported,
       "ciscoLwappApAssociated": ciscoLwappApAssociated,
       "ciscoLwappApPower": ciscoLwappApPower,
       "ciscoLwappApRogueApDetected": ciscoLwappApRogueApDetected,
       "ciscoLwappApRogueApCleared": ciscoLwappApRogueApCleared,
       "ciscoLwappApWipsNotification": ciscoLwappApWipsNotification,
       "ciscoLwappApNoDownlinkChannelNotify": ciscoLwappApNoDownlinkChannelNotify,
       "ciscoLwappApIfUpNotify": ciscoLwappApIfUpNotify,
       "ciscoLwappApIfDownNotify": ciscoLwappApIfDownNotify,
       "ciscoLwappApClientThresholdNotify": ciscoLwappApClientThresholdNotify,
       "ciscoLwappApUpgradeFailureNotify": ciscoLwappApUpgradeFailureNotify,
       "ciscoLwappApCpuUsageHigh": ciscoLwappApCpuUsageHigh,
       "ciscoLwappApMemoryUsageHigh": ciscoLwappApMemoryUsageHigh,
       "ciscoLwappApMaxClientLimitNotify": ciscoLwappApMaxClientLimitNotify,
       "ciscoLwappApAdjChannelRogueDetected": ciscoLwappApAdjChannelRogueDetected,
       "ciscoLwappApAdjChannelRogueCleared": ciscoLwappApAdjChannelRogueCleared,
       "ciscoLwappApRogueDetected": ciscoLwappApRogueDetected,
       "ciscoLwappApCurrentChannelRogueDetected": ciscoLwappApCurrentChannelRogueDetected,
       "ciscoLwappApCurrentChannelRogueCleared": ciscoLwappApCurrentChannelRogueCleared,
       "ciscoLwappApMonitorModeChangeNotify": ciscoLwappApMonitorModeChangeNotify,
       "ciscoLwappApAcTimeSyncFailureTrap": ciscoLwappApAcTimeSyncFailureTrap,
       "ciscoLwappApSsidKeyConflict": ciscoLwappApSsidKeyConflict,
       "ciscoLwappApCurrChannelChanged": ciscoLwappApCurrChannelChanged,
       "ciscoLwappApCapwapRetransmissionQueueFullEvent": ciscoLwappApCapwapRetransmissionQueueFullEvent,
       "ciscoLwappApSystemBootupEvent": ciscoLwappApSystemBootupEvent,
       "ciscoLwappXmFilterCheckWarning": ciscoLwappXmFilterCheckWarning,
       "ciscoLwappApModeUnsupportedOnFlexExpressEvent": ciscoLwappApModeUnsupportedOnFlexExpressEvent,
       "ciscoLwappApXorRadioRoleChangeNotify": ciscoLwappApXorRadioRoleChangeNotify,
       "ciscoLwappRadioBandChangeNotify": ciscoLwappRadioBandChangeNotify,
       "ciscoLwappBrokenAntennaDetails": ciscoLwappBrokenAntennaDetails,
       "ciscoLwappApRadioStuck": ciscoLwappApRadioStuck,
       "ciscoLwappApMIBObjects": ciscoLwappApMIBObjects,
       "ciscoLwappAp": ciscoLwappAp,
       "cLApTable": cLApTable,
       "cLApEntry": cLApEntry,
       "cLApSysMacAddress": cLApSysMacAddress,
       "cLApIfMacAddress": cLApIfMacAddress,
       "cLApMaxNumberOfDot11Slots": cLApMaxNumberOfDot11Slots,
       "cLApEntPhysicalIndex": cLApEntPhysicalIndex,
       "cLApName": cLApName,
       "cLApUpTime": cLApUpTime,
       "cLLwappUpTime": cLLwappUpTime,
       "cLLwappJoinTakenTime": cLLwappJoinTakenTime,
       "cLApMaxNumberOfEthernetSlots": cLApMaxNumberOfEthernetSlots,
       "cLApPrimaryControllerAddressType": cLApPrimaryControllerAddressType,
       "cLApPrimaryControllerAddress": cLApPrimaryControllerAddress,
       "cLApSecondaryControllerAddressType": cLApSecondaryControllerAddressType,
       "cLApSecondaryControllerAddress": cLApSecondaryControllerAddress,
       "cLApTertiaryControllerAddressType": cLApTertiaryControllerAddressType,
       "cLApTertiaryControllerAddress": cLApTertiaryControllerAddress,
       "cLApLastRebootReason": cLApLastRebootReason,
       "cLApEncryptionEnable": cLApEncryptionEnable,
       "cLApFailoverPriority": cLApFailoverPriority,
       "cLApPowerStatus": cLApPowerStatus,
       "cLApTelnetEnable": cLApTelnetEnable,
       "cLApSshEnable": cLApSshEnable,
       "cLApPreStdStateEnabled": cLApPreStdStateEnabled,
       "cLApPwrInjectorStateEnabled": cLApPwrInjectorStateEnabled,
       "cLApPwrInjectorSelection": cLApPwrInjectorSelection,
       "cLApPwrInjectorSwMacAddr": cLApPwrInjectorSwMacAddr,
       "cLApWipsEnable": cLApWipsEnable,
       "cLApMonitorModeOptimization": cLApMonitorModeOptimization,
       "cLApDomainName": cLApDomainName,
       "cLApNameServerAddressType": cLApNameServerAddressType,
       "cLApNameServerAddress": cLApNameServerAddress,
       "cLApAMSDUEnable": cLApAMSDUEnable,
       "cLApEncryptionSupported": cLApEncryptionSupported,
       "cLApRogueDetectionEnabled": cLApRogueDetectionEnabled,
       "cLApTcpMss": cLApTcpMss,
       "cLApDataEncryptionStatus": cLApDataEncryptionStatus,
       "cLApNsiKey": cLApNsiKey,
       "cLApAdminStatus": cLApAdminStatus,
       "cLApPortNumber": cLApPortNumber,
       "cLApRetransmitCount": cLApRetransmitCount,
       "cLApRetransmitTimeout": cLApRetransmitTimeout,
       "cLApVenueConfigVenueGroup": cLApVenueConfigVenueGroup,
       "cLApVenueConfigVenueType": cLApVenueConfigVenueType,
       "cLApVenueConfigVenueName": cLApVenueConfigVenueName,
       "cLApVenueConfigLanguage": cLApVenueConfigLanguage,
       "cLApLEDState": cLApLEDState,
       "cLApTrunkVlan": cLApTrunkVlan,
       "cLApTrunkVlanStatus": cLApTrunkVlanStatus,
       "cLApLocation": cLApLocation,
       "cLApSubMode": cLApSubMode,
       "cLApAssocCount": cLApAssocCount,
       "cLApAssocFailResourceCount": cLApAssocFailResourceCount,
       "cLApRealTimeStatsModeEnabled": cLApRealTimeStatsModeEnabled,
       "cLApAssociatedClientCount": cLApAssociatedClientCount,
       "cLApMemoryCurrentUsage": cLApMemoryCurrentUsage,
       "cLApMemoryAverageUsage": cLApMemoryAverageUsage,
       "cLApCpuCurrentUsage": cLApCpuCurrentUsage,
       "cLApCpuAverageUsage": cLApCpuAverageUsage,
       "cLApUpgradeFromVersion": cLApUpgradeFromVersion,
       "cLApUpgradeToVersion": cLApUpgradeToVersion,
       "cLApUpgradeFailureCause": cLApUpgradeFailureCause,
       "cLApMaxClientLimitNumberTrap": cLApMaxClientLimitNumberTrap,
       "cLApMaxClientLimitCause": cLApMaxClientLimitCause,
       "cLApMaxClientLimitSet": cLApMaxClientLimitSet,
       "cLApFloorLabel": cLApFloorLabel,
       "cLApConnectCount": cLApConnectCount,
       "cLApReassocSuccCount": cLApReassocSuccCount,
       "cLApReassocFailCount": cLApReassocFailCount,
       "cLAdjChannelRogueEnabled": cLAdjChannelRogueEnabled,
       "cLApAssocFailCountByRate": cLApAssocFailCountByRate,
       "cLApAbnormalOfflineCount": cLApAbnormalOfflineCount,
       "cLApActiveClientCount": cLApActiveClientCount,
       "cLApAssocFailCountForRssiLow": cLApAssocFailCountForRssiLow,
       "cLApSysNetId": cLApSysNetId,
       "cLApAssocFailTimes": cLApAssocFailTimes,
       "cLApAntennaBandMode": cLApAntennaBandMode,
       "cLApHeartBeatRspAvgTime": cLApHeartBeatRspAvgTime,
       "cLApEchoRequestCount": cLApEchoRequestCount,
       "cLApEchoResponseLossCount": cLApEchoResponseLossCount,
       "cLApModuleInserted": cLApModuleInserted,
       "cLApEnableModule": cLApEnableModule,
       "cLApIsUniversal": cLApIsUniversal,
       "cLApUniversalPrimeStatus": cLApUniversalPrimeStatus,
       "cLApIsMaster": cLApIsMaster,
       "cLApBleFWDownloadStatus": cLApBleFWDownloadStatus,
       "cLApDot11XorDartConnectorStatus": cLApDot11XorDartConnectorStatus,
       "cLApCtsSxpDefaultPassword": cLApCtsSxpDefaultPassword,
       "cLApCtsSxpState": cLApCtsSxpState,
       "cLApCtsSxpMode": cLApCtsSxpMode,
       "cLApCtsSxpListenerMinHoldtime": cLApCtsSxpListenerMinHoldtime,
       "cLApCtsSxpListenerMaxHoldtime": cLApCtsSxpListenerMaxHoldtime,
       "cLApCtsSxpReconcilePeriod": cLApCtsSxpReconcilePeriod,
       "cLApCtsSxpRetryPeriod": cLApCtsSxpRetryPeriod,
       "cLApCtsSxpSpeakerHoldTime": cLApCtsSxpSpeakerHoldTime,
       "cLApCtsSxpSpeakerKeepAlive": cLApCtsSxpSpeakerKeepAlive,
       "cLApCtsInlineTagStatus": cLApCtsInlineTagStatus,
       "cLApCtsSgaclStatus": cLApCtsSgaclStatus,
       "cLApCtsOverrideStatus": cLApCtsOverrideStatus,
       "cLApModeClear": cLApModeClear,
       "cLApSiteTagName": cLApSiteTagName,
       "cLApRfTagName": cLApRfTagName,
       "cLApPolicyTagName": cLApPolicyTagName,
       "cLApTagSource": cLApTagSource,
       "cLApUsbModuleName": cLApUsbModuleName,
       "cLApUsbModuleState": cLApUsbModuleState,
       "cLApUsbModuleProductId": cLApUsbModuleProductId,
       "cLApUsbDescription": cLApUsbDescription,
       "cLApUsbStateInfo": cLApUsbStateInfo,
       "cLApUsbOverride": cLApUsbOverride,
       "cLApUsbSerialNumber": cLApUsbSerialNumber,
       "cLApUsbMaxPower": cLApUsbMaxPower,
       "cLApLagConfigStatus": cLApLagConfigStatus,
       "cLApMonitorModeOptStatus": cLApMonitorModeOptStatus,
       "cLApFilterName": cLApFilterName,
       "cLApIfSmtParamTable": cLApIfSmtParamTable,
       "cLApIfSmtParamEntry": cLApIfSmtParamEntry,
       "cLApIfSmtDot11Bssid": cLApIfSmtDot11Bssid,
       "cLApCountryTable": cLApCountryTable,
       "cLApCountryEntry": cLApCountryEntry,
       "cLApCountryCode": cLApCountryCode,
       "cLApCountryAllowed": cLApCountryAllowed,
       "ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled": ciscoLwappApIfRegulatoryDomainMismatchNotifEnabled,
       "ciscoLwappApCrashEnabled": ciscoLwappApCrashEnabled,
       "ciscoLwappApUnsupportedEnabled": ciscoLwappApUnsupportedEnabled,
       "ciscoLwappApAssociatedEnabled": ciscoLwappApAssociatedEnabled,
       "cLApCrashInfoTable": cLApCrashInfoTable,
       "cLApCrashInfoEntry": cLApCrashInfoEntry,
       "cLApCrashFileName": cLApCrashFileName,
       "cLApCrashFileSize": cLApCrashFileSize,
       "cLApCrashFileTimeStamp": cLApCrashFileTimeStamp,
       "cLApSysInfoTable": cLApSysInfoTable,
       "cLApSysInfoEntry": cLApSysInfoEntry,
       "cLApSysMemType": cLApSysMemType,
       "cLApSysMemSize": cLApSysMemSize,
       "cLApSysFlashSize": cLApSysFlashSize,
       "cLApSysCpuType": cLApSysCpuType,
       "cLApSysFlashType": cLApSysFlashType,
       "cLApExtTable": cLApExtTable,
       "cLApExtEntry": cLApExtEntry,
       "cLApLEDFlashStatus": cLApLEDFlashStatus,
       "cLApLEDFlashDuration": cLApLEDFlashDuration,
       "cLApInetAddressType": cLApInetAddressType,
       "cLApInetAddress": cLApInetAddress,
       "cLApStaticIpv6AddressEnabled": cLApStaticIpv6AddressEnabled,
       "cLApStaticIpv6InetAddressType": cLApStaticIpv6InetAddressType,
       "cLApStaticIpv6InetAddress": cLApStaticIpv6InetAddress,
       "cLApStaticIpv6PrefixLength": cLApStaticIpv6PrefixLength,
       "cLApStaticIpv6GatewayInetAddressType": cLApStaticIpv6GatewayInetAddressType,
       "cLApStaticIpv6GatewayInetAddress": cLApStaticIpv6GatewayInetAddress,
       "cLApStaticIpNetmaskType": cLApStaticIpNetmaskType,
       "cLApStaticIpNetmask": cLApStaticIpNetmask,
       "cLApPreferMode": cLApPreferMode,
       "cLApPreferModeApplied": cLApPreferModeApplied,
       "cLApIndoorMode": cLApIndoorMode,
       "cLApEnvInfoTable": cLApEnvInfoTable,
       "cLApEnvInfoEntry": cLApEnvInfoEntry,
       "cLApEnvTemperatureDegree": cLApEnvTemperatureDegree,
       "cLApEnvTemperatureState": cLApEnvTemperatureState,
       "cLApEnvOrientation": cLApEnvOrientation,
       "cLApEnvPoeOutStatus": cLApEnvPoeOutStatus,
       "cLApGpsInfoTable": cLApGpsInfoTable,
       "cLApGpsInfoEntry": cLApGpsInfoEntry,
       "cLApGpsLocationPresent": cLApGpsLocationPresent,
       "cLApGpsLocationValid": cLApGpsLocationValid,
       "cLApGpsLatitude": cLApGpsLatitude,
       "cLApGpsLongitude": cLApGpsLongitude,
       "cLApGpsAltitude": cLApGpsAltitude,
       "cLApGpsCollectionTime": cLApGpsCollectionTime,
       "ciscoLwappXorRadioRoleChangeEnabled": ciscoLwappXorRadioRoleChangeEnabled,
       "ciscoLwappApIf": ciscoLwappApIf,
       "cLApDot11IfTable": cLApDot11IfTable,
       "cLApDot11IfEntry": cLApDot11IfEntry,
       "cLApDot11IfSlotId": cLApDot11IfSlotId,
       "cLApDot11IfType": cLApDot11IfType,
       "cLApDot11IfRegDomain": cLApDot11IfRegDomain,
       "cLApDot11nSupport": cLApDot11nSupport,
       "cLAp11nChannelBandwidth": cLAp11nChannelBandwidth,
       "cLApLomEnabled": cLApLomEnabled,
       "cLApLomFirstChannel": cLApLomFirstChannel,
       "cLApLomSecondChannel": cLApLomSecondChannel,
       "cLApLomThirdChannel": cLApLomThirdChannel,
       "cLApLomFourthChannel": cLApLomFourthChannel,
       "cLApExtensionChannel": cLApExtensionChannel,
       "cLApLegacyBeamForming": cLApLegacyBeamForming,
       "cLApCdpOverAirEnabled": cLApCdpOverAirEnabled,
       "cLApDot11IfAdminStatus": cLApDot11IfAdminStatus,
       "cLApDot11IfLinkChangeCount": cLApDot11IfLinkChangeCount,
       "cLApDot11MaxClients": cLApDot11MaxClients,
       "cLApPromiscuousModeDwelling": cLApPromiscuousModeDwelling,
       "cLApDot11IfStaKeepingTime": cLApDot11IfStaKeepingTime,
       "cLApDot11IfLinkSpeed": cLApDot11IfLinkSpeed,
       "cLApDot11IfMtu": cLApDot11IfMtu,
       "cLApDot11IfDesc": cLApDot11IfDesc,
       "cLApDot11acSupport": cLApDot11acSupport,
       "cLAp11ChannelBandwidth": cLAp11ChannelBandwidth,
       "cLApExtensionChannels": cLApExtensionChannels,
       "cLAPDot11IfMinTxPowerStep": cLAPDot11IfMinTxPowerStep,
       "cLApDot11XorRadioMode": cLApDot11XorRadioMode,
       "cLApDot11XorRadioBand": cLApDot11XorRadioBand,
       "cLApDot11XorRadioRoleAssignment": cLApDot11XorRadioRoleAssignment,
       "cLApDot11IfMaxDataRate": cLApDot11IfMaxDataRate,
       "cLApDot11IfSensorReachability": cLApDot11IfSensorReachability,
       "cLApDot11axSupport": cLApDot11axSupport,
       "cLApFraCoverageOverlapFactor": cLApFraCoverageOverlapFactor,
       "cLApFraSuggestedMode": cLApFraSuggestedMode,
       "cLApDot11IfDualRadioMode": cLApDot11IfDualRadioMode,
       "cLApDot11IfDualRadioCapable": cLApDot11IfDualRadioCapable,
       "cLApDot11IfRadioFRACapable": cLApDot11IfRadioFRACapable,
       "cLApDot11IfPhyS80EightyChannelNumber": cLApDot11IfPhyS80EightyChannelNumber,
       "cLApDot11IfDualRadioOperation": cLApDot11IfDualRadioOperation,
       "cLApDot11IfRadioRoleOperation": cLApDot11IfRadioRoleOperation,
       "cLApDot11IfRadioRole": cLApDot11IfRadioRole,
       "cLApDot11IfRptncPresent": cLApDot11IfRptncPresent,
       "cLApDot11IfDartPresent": cLApDot11IfDartPresent,
       "cLApEthernetIfTable": cLApEthernetIfTable,
       "cLApEthernetIfEntry": cLApEthernetIfEntry,
       "cLApEthernetIfSlotId": cLApEthernetIfSlotId,
       "cLApEthernetIfName": cLApEthernetIfName,
       "cLApEthernetIfMacAddress": cLApEthernetIfMacAddress,
       "cLApEthernetIfAdminStatus": cLApEthernetIfAdminStatus,
       "cLApEthernetIfOperStatus": cLApEthernetIfOperStatus,
       "cLApEthernetIfRxUcastPkts": cLApEthernetIfRxUcastPkts,
       "cLApEthernetIfRxNUcastPkts": cLApEthernetIfRxNUcastPkts,
       "cLApEthernetIfTxUcastPkts": cLApEthernetIfTxUcastPkts,
       "cLApEthernetIfTxNUcastPkts": cLApEthernetIfTxNUcastPkts,
       "cLApEthernetIfDuplex": cLApEthernetIfDuplex,
       "cLApEthernetIfLinkSpeed": cLApEthernetIfLinkSpeed,
       "cLApEthernetIfPOEPower": cLApEthernetIfPOEPower,
       "cLApEthernetIfRxTotalBytes": cLApEthernetIfRxTotalBytes,
       "cLApEthernetIfTxTotalBytes": cLApEthernetIfTxTotalBytes,
       "cLApEthernetIfInputCrc": cLApEthernetIfInputCrc,
       "cLApEthernetIfInputAborts": cLApEthernetIfInputAborts,
       "cLApEthernetIfInputErrors": cLApEthernetIfInputErrors,
       "cLApEthernetIfInputFrames": cLApEthernetIfInputFrames,
       "cLApEthernetIfInputOverrun": cLApEthernetIfInputOverrun,
       "cLApEthernetIfInputDrops": cLApEthernetIfInputDrops,
       "cLApEthernetIfInputResource": cLApEthernetIfInputResource,
       "cLApEthernetIfUnknownProtocol": cLApEthernetIfUnknownProtocol,
       "cLApEthernetIfRunts": cLApEthernetIfRunts,
       "cLApEthernetIfGiants": cLApEthernetIfGiants,
       "cLApEthernetIfThrottle": cLApEthernetIfThrottle,
       "cLApEthernetIfResets": cLApEthernetIfResets,
       "cLApEthernetIfOutputCollision": cLApEthernetIfOutputCollision,
       "cLApEthernetIfOutputNoBuffer": cLApEthernetIfOutputNoBuffer,
       "cLApEthernetIfOutputResource": cLApEthernetIfOutputResource,
       "cLApEthernetIfOutputUnderrun": cLApEthernetIfOutputUnderrun,
       "cLApEthernetIfOutputErrors": cLApEthernetIfOutputErrors,
       "cLApEthernetIfOutputTotalDrops": cLApEthernetIfOutputTotalDrops,
       "cLApEthernetIfCdpEnabled": cLApEthernetIfCdpEnabled,
       "cLApEthernetIfMtu": cLApEthernetIfMtu,
       "cLApEthernetIfType": cLApEthernetIfType,
       "cLApEthernetIfLinkChangeCount": cLApEthernetIfLinkChangeCount,
       "cLApDot11RadioTable": cLApDot11RadioTable,
       "cLApDot11RadioEntry": cLApDot11RadioEntry,
       "cLApDot11RadioMACAddress": cLApDot11RadioMACAddress,
       "cLApDot11RadioSubBand": cLApDot11RadioSubBand,
       "cLApDot11RadioVersion": cLApDot11RadioVersion,
       "cLApDot11IsBackhaul": cLApDot11IsBackhaul,
       "cLApDot11RadioRole": cLApDot11RadioRole,
       "cLApDot11RadioMode": cLApDot11RadioMode,
       "cLApDot11RadioSubType": cLApDot11RadioSubType,
       "cLApDot11IfAntennaTable": cLApDot11IfAntennaTable,
       "cLApDot11IfAntennaEntry": cLApDot11IfAntennaEntry,
       "cLApDot11IfAntennaId": cLApDot11IfAntennaId,
       "cLApDot11IfAntennaTxEnable": cLApDot11IfAntennaTxEnable,
       "cLApDot11IfAntennaRxEnable": cLApDot11IfAntennaRxEnable,
       "cLApDot11IfAntennaEnable": cLApDot11IfAntennaEnable,
       "cLApVlanIfTable": cLApVlanIfTable,
       "cLApVlanIfEntry": cLApVlanIfEntry,
       "cLApVlanIfEthernetId": cLApVlanIfEthernetId,
       "cLApVlanIfMode": cLApVlanIfMode,
       "cLApVlanIfEnable": cLApVlanIfEnable,
       "cLApVlanIfNativeVlanId": cLApVlanIfNativeVlanId,
       "cLApVlanListTable": cLApVlanListTable,
       "cLApVlanListEntry": cLApVlanListEntry,
       "cLApVlanListVlanId": cLApVlanListVlanId,
       "cLApVlanListRowStatus": cLApVlanListRowStatus,
       "cLApDot11GlobalConfigTable": cLApDot11GlobalConfigTable,
       "cLApDot11GlobalConfigEntry": cLApDot11GlobalConfigEntry,
       "cLApNwLegacyBeamForming": cLApNwLegacyBeamForming,
       "cLApNwTxPowerThreshold": cLApNwTxPowerThreshold,
       "cLApNwTxPowerThresholdVer2": cLApNwTxPowerThresholdVer2,
       "cLApDot11RadioStatsTable": cLApDot11RadioStatsTable,
       "cLApDot11RadioStatsEntry": cLApDot11RadioStatsEntry,
       "cLApDot11RadioStatsRxErrorFrameCount": cLApDot11RadioStatsRxErrorFrameCount,
       "cLApDot11RadioStatsMacMicErrFrameCount": cLApDot11RadioStatsMacMicErrFrameCount,
       "cLApDot11RadioStatsMacDecryptErrFrameCount": cLApDot11RadioStatsMacDecryptErrFrameCount,
       "cLApDot11RadioStatsRxMgmtFrameCount": cLApDot11RadioStatsRxMgmtFrameCount,
       "cLApDot11RadioStatsRxCtrlFrameCount": cLApDot11RadioStatsRxCtrlFrameCount,
       "cLApDot11RadioStatsRxDataFrameCount": cLApDot11RadioStatsRxDataFrameCount,
       "cLApDot11RadioStatsTxMgmtFrameCount": cLApDot11RadioStatsTxMgmtFrameCount,
       "cLApDot11RadioStatsTxCtrlFrameCount": cLApDot11RadioStatsTxCtrlFrameCount,
       "cLApDot11RadioStatsTxDataFrameCount": cLApDot11RadioStatsTxDataFrameCount,
       "cLApDot11RadioStatsRxDataPacketCount": cLApDot11RadioStatsRxDataPacketCount,
       "cLApDot11RadioStatsTxDataPacketCount": cLApDot11RadioStatsTxDataPacketCount,
       "cLApDot11RadioStatsRetryFrameCount": cLApDot11RadioStatsRetryFrameCount,
       "cLApDot11RadioStatsRetryPacketCount": cLApDot11RadioStatsRetryPacketCount,
       "cLApDot11RadioRssiTable": cLApDot11RadioRssiTable,
       "cLApDot11RadioRssiEntry": cLApDot11RadioRssiEntry,
       "cLApDot11RadioRssiHighest": cLApDot11RadioRssiHighest,
       "cLApDot11RadioRssiLowest": cLApDot11RadioRssiLowest,
       "cLApDot11RadioRssiAverage": cLApDot11RadioRssiAverage,
       "cLApDot11RadioRateStatsTable": cLApDot11RadioRateStatsTable,
       "cLApDot11RadioRateStatsEntry": cLApDot11RadioRateStatsEntry,
       "cLApDot11RadioRate": cLApDot11RadioRate,
       "cLApDot11RadioRateStatsRxPackets": cLApDot11RadioRateStatsRxPackets,
       "cLApDot11RadioRateStatsRxBytes": cLApDot11RadioRateStatsRxBytes,
       "cLApDot11RadioRateStatsTxPackets": cLApDot11RadioRateStatsTxPackets,
       "cLApDot11RadioRateStatsTxBytes": cLApDot11RadioRateStatsTxBytes,
       "cLApDot11RadioRateString": cLApDot11RadioRateString,
       "cLApDot11RadioSsidTable": cLApDot11RadioSsidTable,
       "cLApDot11RadioSsidEntry": cLApDot11RadioSsidEntry,
       "cLApSsidIndex": cLApSsidIndex,
       "cLApDot11RadioSsidName": cLApDot11RadioSsidName,
       "cLApCableModemIfStatsTable": cLApCableModemIfStatsTable,
       "cLApCableModemIfStatsEntry": cLApCableModemIfStatsEntry,
       "cLApCmMacAddress": cLApCmMacAddress,
       "cLApCmApMacAddress": cLApCmApMacAddress,
       "cLApCmSwVersion": cLApCmSwVersion,
       "cLApEthernetSpeed": cLApEthernetSpeed,
       "cLApEthernetStatus": cLApEthernetStatus,
       "cLApCmStatus": cLApCmStatus,
       "cLApCmSerialNumber": cLApCmSerialNumber,
       "cLApCmUsChannelStatus": cLApCmUsChannelStatus,
       "cLApCmDsChannelStatus": cLApCmDsChannelStatus,
       "cLApCmMaskBit": cLApCmMaskBit,
       "ciscoLwappApGlobal": ciscoLwappApGlobal,
       "cLApFastHbTimerTable": cLApFastHbTimerTable,
       "cLApFastHbTimerEntry": cLApFastHbTimerEntry,
       "cLApFastHbTimerApType": cLApFastHbTimerApType,
       "cLApFastHbTimerTimeout": cLApFastHbTimerTimeout,
       "cLApFastHbTimerEnabled": cLApFastHbTimerEnabled,
       "cLApPrimaryDiscoveryTimeout": cLApPrimaryDiscoveryTimeout,
       "cLApGlobalPrimaryControllerAddressType": cLApGlobalPrimaryControllerAddressType,
       "cLApGlobalPrimaryControllerAddress": cLApGlobalPrimaryControllerAddress,
       "cLApGlobalPrimaryControllerName": cLApGlobalPrimaryControllerName,
       "cLApGlobalSecondaryControllerAddressType": cLApGlobalSecondaryControllerAddressType,
       "cLApGlobalSecondaryControllerAddress": cLApGlobalSecondaryControllerAddress,
       "cLApGlobalSecondaryControllerName": cLApGlobalSecondaryControllerName,
       "cLApGlobalFailoverPriority": cLApGlobalFailoverPriority,
       "cLApGlobalTcpMss": cLApGlobalTcpMss,
       "cLApGlobalDot11IfTable": cLApGlobalDot11IfTable,
       "cLApGlobalDot11IfEntry": cLApGlobalDot11IfEntry,
       "cLApGlobalDot11IfCdpEnabled": cLApGlobalDot11IfCdpEnabled,
       "cLApGlobalEthernetIfTable": cLApGlobalEthernetIfTable,
       "cLApGlobalEthernetIfEntry": cLApGlobalEthernetIfEntry,
       "cLApGlobalEthernetIfCdpEnabled": cLApGlobalEthernetIfCdpEnabled,
       "cLApGlobalRetransmitCount": cLApGlobalRetransmitCount,
       "cLApGlobalRetransmitTimeout": cLApGlobalRetransmitTimeout,
       "cLApOeapDisableLocalAccess": cLApOeapDisableLocalAccess,
       "cLApGlobalLEDState": cLApGlobalLEDState,
       "cLApRadioInterfaceShutdownEnabled": cLApRadioInterfaceShutdownEnabled,
       "cLApEthernetInterfaceDowntime": cLApEthernetInterfaceDowntime,
       "cLAPMulticastGroupAddressType": cLAPMulticastGroupAddressType,
       "cLAPMulticastGroupAddress": cLAPMulticastGroupAddress,
       "cLAPMulticastMode": cLAPMulticastMode,
       "cLApPrimedDiscoveryTimeout": cLApPrimedDiscoveryTimeout,
       "cLApGlobalPreferMode": cLApGlobalPreferMode,
       "cLApGlobalAPLagCapability": cLApGlobalAPLagCapability,
       "cLApGlobalAPDtlsVersion": cLApGlobalAPDtlsVersion,
       "cLApGlobalAPDtlsCipherSuite": cLApGlobalAPDtlsCipherSuite,
       "cLApGlobalMaxApsSupported": cLApGlobalMaxApsSupported,
       "cLApAuthorizeApMacAuth": cLApAuthorizeApMacAuth,
       "cLApAuthorizeApSerialNumAuth": cLApAuthorizeApSerialNumAuth,
       "cLApAuthorizeApMethodList": cLApAuthorizeApMethodList,
       "cLApGlobalAPAuditReport": cLApGlobalAPAuditReport,
       "cLApGlobalAPAuditReportInterval": cLApGlobalAPAuditReportInterval,
       "cLApGlobalAPConnectCount": cLApGlobalAPConnectCount,
       "cLApAuthorizeApMacMethodList": cLApAuthorizeApMacMethodList,
       "cLApAuthorizeApSerialNumMethodList": cLApAuthorizeApSerialNumMethodList,
       "clApImageUpgradeConfig": clApImageUpgradeConfig,
       "clApImageUpgradeHttpsEnable": clApImageUpgradeHttpsEnable,
       "ciscoLwappApCredentials": ciscoLwappApCredentials,
       "cLApCredentialGlobalUserName": cLApCredentialGlobalUserName,
       "cLApCredentialGlobalPassword": cLApCredentialGlobalPassword,
       "cLApCredentialGlobalSecret": cLApCredentialGlobalSecret,
       "cLApCredentialsTable": cLApCredentialsTable,
       "cLApCredentialsEntry": cLApCredentialsEntry,
       "cLApCredentialUserName": cLApCredentialUserName,
       "cLApCredentialPassword": cLApCredentialPassword,
       "cLApCredentialSecret": cLApCredentialSecret,
       "cLApCredentialEnableGlobalCredentials": cLApCredentialEnableGlobalCredentials,
       "ciscoLwappLinkLatency": ciscoLwappLinkLatency,
       "cLApLinkLatencyTable": cLApLinkLatencyTable,
       "cLApLinkLatencyEntry": cLApLinkLatencyEntry,
       "cLApLinkLatencyEnable": cLApLinkLatencyEnable,
       "cLApLinkLatencyReset": cLApLinkLatencyReset,
       "cLApLinkLatencyStatsTable": cLApLinkLatencyStatsTable,
       "cLApLinkLatencyStatsEntry": cLApLinkLatencyStatsEntry,
       "cLApLinkLatencyStatsCurrent": cLApLinkLatencyStatsCurrent,
       "cLApLinkLatencyStatsMin": cLApLinkLatencyStatsMin,
       "cLApLinkLatencyStatsMax": cLApLinkLatencyStatsMax,
       "cLApLinkLatencyTimeStamp": cLApLinkLatencyTimeStamp,
       "cLApDataLinkLatencyStatsCurrent": cLApDataLinkLatencyStatsCurrent,
       "cLApDataLinkLatencyStatsMin": cLApDataLinkLatencyStatsMin,
       "cLApDataLinkLatencyStatsMax": cLApDataLinkLatencyStatsMax,
       "cLApDataLinkLatencyTimeStamp": cLApDataLinkLatencyTimeStamp,
       "ciscoLwappSpectrum": ciscoLwappSpectrum,
       "ciscoLwappAp802dot1xSupplicant": ciscoLwappAp802dot1xSupplicant,
       "cLApGlobal802dot1xAuthenticationEnabled": cLApGlobal802dot1xAuthenticationEnabled,
       "cLApGlobal802dot1xSupplicantUsername": cLApGlobal802dot1xSupplicantUsername,
       "cLApGlobal802dot1xSupplicantPassword": cLApGlobal802dot1xSupplicantPassword,
       "cLAp802dot1xSupplicantTable": cLAp802dot1xSupplicantTable,
       "cLAp802dot1xSupplicantEntry": cLAp802dot1xSupplicantEntry,
       "cLAp802dot1xSupplicantOverrideEnabled": cLAp802dot1xSupplicantOverrideEnabled,
       "cLAp802dot1xSupplicantOverrideUsername": cLAp802dot1xSupplicantOverrideUsername,
       "cLAp802dot1xSupplicantOverridePassword": cLAp802dot1xSupplicantOverridePassword,
       "cLAp802dot1xSupplicantOverrideEapType": cLAp802dot1xSupplicantOverrideEapType,
       "cLApGlobal802dot1xSupplicantEapType": cLApGlobal802dot1xSupplicantEapType,
       "cLApSeClientTable": cLApSeClientTable,
       "cLApSeClientEntry": cLApSeClientEntry,
       "cLApSeIndex": cLApSeIndex,
       "cLApSeClientUserName": cLApSeClientUserName,
       "cLApSeClientIPAddrType": cLApSeClientIPAddrType,
       "cLApSeClientIPAddr": cLApSeClientIPAddr,
       "cLApSeClientDuration": cLApSeClientDuration,
       "cLApSeClientPort": cLApSeClientPort,
       "ciscoLwappApWlanStats": ciscoLwappApWlanStats,
       "cLApWlanStatsTable": cLApWlanStatsTable,
       "cLApWlanStatsEntry": cLApWlanStatsEntry,
       "cLApWlanStatsTxPktNum": cLApWlanStatsTxPktNum,
       "cLApWlanStatsTxOctetNum": cLApWlanStatsTxOctetNum,
       "cLApWlanStatsRxPktNum": cLApWlanStatsRxPktNum,
       "cLApWlanStatsRxOctetNum": cLApWlanStatsRxOctetNum,
       "cLApWlanStatsRetransmitNum": cLApWlanStatsRetransmitNum,
       "cLApWlanStatsAssocClientNum": cLApWlanStatsAssocClientNum,
       "cLApWlanStatsOnlineUserNum": cLApWlanStatsOnlineUserNum,
       "ciscoLwappApWlanInfo": ciscoLwappApWlanInfo,
       "cLApWlanInfoTable": cLApWlanInfoTable,
       "cLApWlanInfoEntry": cLApWlanInfoEntry,
       "cLApWlanInfoMaxClients": cLApWlanInfoMaxClients,
       "cLApRadioWlanInfoTable": cLApRadioWlanInfoTable,
       "cLApRadioWlanInfoEntry": cLApRadioWlanInfoEntry,
       "cLApRadioWlanSsid": cLApRadioWlanSsid,
       "cLApRadioWlanBssid": cLApRadioWlanBssid,
       "ciscoLwappPacketDumpInfo": ciscoLwappPacketDumpInfo,
       "cLApPacketDumpFtpServerAddressType": cLApPacketDumpFtpServerAddressType,
       "cLApPacketDumpFtpServerAddress": cLApPacketDumpFtpServerAddress,
       "cLApPacketDumpFtpServerPath": cLApPacketDumpFtpServerPath,
       "cLApPacketDumpFtpUsername": cLApPacketDumpFtpUsername,
       "cLApPacketDumpFtpPassword": cLApPacketDumpFtpPassword,
       "cLApPacketDumpClassifier": cLApPacketDumpClassifier,
       "cLApPacketDumpBufferSize": cLApPacketDumpBufferSize,
       "cLApPacketDumpCaptureTime": cLApPacketDumpCaptureTime,
       "cLApPacketDumpTruncation": cLApPacketDumpTruncation,
       "cLApPacketDumpApName": cLApPacketDumpApName,
       "cLApPacketDumpDeviceMacAddress": cLApPacketDumpDeviceMacAddress,
       "cLApPacketDumpStartStop": cLApPacketDumpStartStop,
       "ciscoLwappAplanStats": ciscoLwappAplanStats,
       "cLAplanStatsTable": cLAplanStatsTable,
       "cLAplanStatsEntry": cLAplanStatsEntry,
       "cLApLanPortId": cLApLanPortId,
       "cLApLanPortState": cLApLanPortState,
       "cLApLanPortVlanId": cLApLanPortVlanId,
       "cLApLanPortVlanIdValid": cLApLanPortVlanIdValid,
       "cLApLanPoeState": cLApLanPoeState,
       "cLApLanPowerLevelId": cLApLanPowerLevelId,
       "cLAplanOverrideTable": cLAplanOverrideTable,
       "cLAplanOverrideEntry": cLAplanOverrideEntry,
       "cLApLanOverride": cLApLanOverride,
       "ciscoLwappApGlobalBleBeacon": ciscoLwappApGlobalBleBeacon,
       "cLHaloGlobalBleBeaconInterval": cLHaloGlobalBleBeaconInterval,
       "cLHaloBleBeaconTable": cLHaloBleBeaconTable,
       "cLHaloBleBeaconEntry": cLHaloBleBeaconEntry,
       "cLHaloGlobalBleBeaconId": cLHaloGlobalBleBeaconId,
       "cLHaloGlobalBleBeaconUuid": cLHaloGlobalBleBeaconUuid,
       "cLHaloGlobalBleBeaconTxPower": cLHaloGlobalBleBeaconTxPower,
       "cLHaloGlobalBleBeaconEnable": cLHaloGlobalBleBeaconEnable,
       "cLApBleBeaconTable": cLApBleBeaconTable,
       "cLApBleBeaconEntry": cLApBleBeaconEntry,
       "cLApBleBeaconMajorField": cLApBleBeaconMajorField,
       "cLApBleBeaconMinorField": cLApBleBeaconMinorField,
       "cLApBleBeaconTxPower": cLApBleBeaconTxPower,
       "cLApBleBeaconStatus": cLApBleBeaconStatus,
       "cLApBleBeaconUuid": cLApBleBeaconUuid,
       "cLApBleBeaconInterval": cLApBleBeaconInterval,
       "cLApBleBeaconApplyGlobal": cLApBleBeaconApplyGlobal,
       "cLApBleBeaconAdvTxPower": cLApBleBeaconAdvTxPower,
       "ciscoLwappApHyperlocation": ciscoLwappApHyperlocation,
       "cLApHyperlocationTable": cLApHyperlocationTable,
       "cLApHyperlocationEntry": cLApHyperlocationEntry,
       "cLApHyperlocationAdminState": cLApHyperlocationAdminState,
       "cLApHyperlocationUnsetFlag": cLApHyperlocationUnsetFlag,
       "ciscoLwappApSecureCipher": ciscoLwappApSecureCipher,
       "cLApSecureCipher": cLApSecureCipher,
       "ciscoLwappApProfile": ciscoLwappApProfile,
       "cLApProfileTable": cLApProfileTable,
       "cLApProfileEntry": cLApProfileEntry,
       "cLApProfileName": cLApProfileName,
       "cLApProfileRowStatus": cLApProfileRowStatus,
       "cLApProfileCredentialGlobalUserName": cLApProfileCredentialGlobalUserName,
       "cLApProfileCredentialGlobalPassword": cLApProfileCredentialGlobalPassword,
       "cLApProfileCredentialGlobalSecret": cLApProfileCredentialGlobalSecret,
       "cLApProfileCredentialEnableGlobalCredentials": cLApProfileCredentialEnableGlobalCredentials,
       "cLApProfileLinkLatencyEnable": cLApProfileLinkLatencyEnable,
       "cLApProfileHaloBleBeaconInterval": cLApProfileHaloBleBeaconInterval,
       "cLApProfileFastHbTimerTimeout": cLApProfileFastHbTimerTimeout,
       "cLApProfileFastHbTimerEnabled": cLApProfileFastHbTimerEnabled,
       "cLApProfilePrimaryDiscoveryTimeout": cLApProfilePrimaryDiscoveryTimeout,
       "cLApProfileBackupPrimaryControllerAddressType": cLApProfileBackupPrimaryControllerAddressType,
       "cLApProfileBackupPrimaryControllerAddress": cLApProfileBackupPrimaryControllerAddress,
       "cLApProfileBackupPrimaryControllerName": cLApProfileBackupPrimaryControllerName,
       "cLApProfileBackupSecondaryControllerAddressType": cLApProfileBackupSecondaryControllerAddressType,
       "cLApProfileBackupSecondaryControllerAddress": cLApProfileBackupSecondaryControllerAddress,
       "cLApProfileBackupSecondaryControllerName": cLApProfileBackupSecondaryControllerName,
       "cLApProfileBackupTertiaryControllerAddressType": cLApProfileBackupTertiaryControllerAddressType,
       "cLApProfileBackupTertiaryControllerAddress": cLApProfileBackupTertiaryControllerAddress,
       "cLApProfileBackupTertiaryControllerName": cLApProfileBackupTertiaryControllerName,
       "cLApProfileTcpMss": cLApProfileTcpMss,
       "cLApProfileRetransmitCount": cLApProfileRetransmitCount,
       "cLApProfileRetransmitTimeout": cLApProfileRetransmitTimeout,
       "cLApProfileOeapDisableLocalAccess": cLApProfileOeapDisableLocalAccess,
       "cLApProfileLedState": cLApProfileLedState,
       "cLApProfileRadioInterfaceShutdownEnabled": cLApProfileRadioInterfaceShutdownEnabled,
       "cLApProfileEthernetInterfaceDowntime": cLApProfileEthernetInterfaceDowntime,
       "cLApProfileMulticastGroupAddressType": cLApProfileMulticastGroupAddressType,
       "cLApProfileMulticastGroupAddress": cLApProfileMulticastGroupAddress,
       "cLApProfileMulticastMode": cLApProfileMulticastMode,
       "cLApProfilePrimedJoinTimeout": cLApProfilePrimedJoinTimeout,
       "cLApProfilePreferMode": cLApProfilePreferMode,
       "cLApProfileApLagEnabled": cLApProfileApLagEnabled,
       "cLApProfile802dot1xAuthenticationEnabled": cLApProfile802dot1xAuthenticationEnabled,
       "cLApProfile802dot1xSupplicantUsername": cLApProfile802dot1xSupplicantUsername,
       "cLApProfile802dot1xSupplicantPassword": cLApProfile802dot1xSupplicantPassword,
       "cLApProfileEncryptionEnable": cLApProfileEncryptionEnable,
       "cLApProfileTelnetEnable": cLApProfileTelnetEnable,
       "cLApProfileSshEnable": cLApProfileSshEnable,
       "cLApProfileHyperlocationEnable": cLApProfileHyperlocationEnable,
       "cLApProfileHyperlocationDetectionThreshold": cLApProfileHyperlocationDetectionThreshold,
       "cLApProfileHyperlocationResetThreshold": cLApProfileHyperlocationResetThreshold,
       "cLApProfileHyperlocationTriggerThreshold": cLApProfileHyperlocationTriggerThreshold,
       "cLApProfileHyperlocationNtpIpAddressType": cLApProfileHyperlocationNtpIpAddressType,
       "cLApProfileHyperlocationNtpIpAddress": cLApProfileHyperlocationNtpIpAddress,
       "cLApProfileAdjustMss": cLApProfileAdjustMss,
       "cLApProfileDiscoveryTimeout": cLApProfileDiscoveryTimeout,
       "cLApProfileHeartBeatTimeout": cLApProfileHeartBeatTimeout,
       "cLApProfileCdpEnable": cLApProfileCdpEnable,
       "cLApProfileApPacketCaptureProfile": cLApProfileApPacketCaptureProfile,
       "cLApProfileRogueReportInterval": cLApProfileRogueReportInterval,
       "cLApProfileRogueMinimumRssi": cLApProfileRogueMinimumRssi,
       "cLApProfileRogueTransientInterval": cLApProfileRogueTransientInterval,
       "cLApProfileRogueContainFlexconnect": cLApProfileRogueContainFlexconnect,
       "cLApProfileRogueContainAutoRateEnable": cLApProfileRogueContainAutoRateEnable,
       "cLApProfileRogueDetectionEnable": cLApProfileRogueDetectionEnable,
       "cLApProfileReportInterval24ghz": cLApProfileReportInterval24ghz,
       "cLApProfileReportInterval5ghz": cLApProfileReportInterval5ghz,
       "cLApProfileDot1xApSwitchEapAuth": cLApProfileDot1xApSwitchEapAuth,
       "cLApProfileDot1xApSwtichLscAuth": cLApProfileDot1xApSwtichLscAuth,
       "cLApProfileMeshProfileName": cLApProfileMeshProfileName,
       "cLApProfileUsbStatus": cLApProfileUsbStatus,
       "cLApProfileVlanTagging": cLApProfileVlanTagging,
       "cLApProfileApCountryCode": cLApProfileApCountryCode,
       "cLApProfileExtModuleEnable": cLApProfileExtModuleEnable,
       "cLApProfileStatsTimer": cLApProfileStatsTimer,
       "cLApProfilePoePreStandardSwitchFlag": cLApProfilePoePreStandardSwitchFlag,
       "cLApProfilePoePowerInjectorSelection": cLApProfilePoePowerInjectorSelection,
       "cLApProfilePoeInjectorSwitchMac": cLApProfilePoeInjectorSwitchMac,
       "cLApProfileHaloBleBeaconAdvertisedPwr": cLApProfileHaloBleBeaconAdvertisedPwr,
       "cLApProfileTftpDownGradeAddressType": cLApProfileTftpDownGradeAddressType,
       "cLApProfileTftpDownGradeAddress": cLApProfileTftpDownGradeAddress,
       "cLApProfileTftpDownGradeFileName": cLApProfileTftpDownGradeFileName,
       "cLApProfileCoreDumpType": cLApProfileCoreDumpType,
       "cLApProfileCoreDumpTftpAddressType": cLApProfileCoreDumpTftpAddressType,
       "cLApProfileCoreDumpTftpAddress": cLApProfileCoreDumpTftpAddress,
       "cLApProfileCoreDumpCoreFileName": cLApProfileCoreDumpCoreFileName,
       "cLApProfileBackupFallbackEnabled": cLApProfileBackupFallbackEnabled,
       "cLApProfileClientRssiStatsEnabled": cLApProfileClientRssiStatsEnabled,
       "cLApProfileClientRssiStatsReportInterval": cLApProfileClientRssiStatsReportInterval,
       "cLApProfileGasRateLimitEnable": cLApProfileGasRateLimitEnable,
       "cLApProfileGasRateLimitNumReqPerInterval": cLApProfileGasRateLimitNumReqPerInterval,
       "cLApProfileGasRateLimitIntervalMsec": cLApProfileGasRateLimitIntervalMsec,
       "cLApProfileQoSMapApTrustsUpstreamDSCP": cLApProfileQoSMapApTrustsUpstreamDSCP,
       "cLApProfileUdpliteState": cLApProfileUdpliteState,
       "cLApProfileMethodListName": cLApProfileMethodListName,
       "cLApProfileWindowSize": cLApProfileWindowSize,
       "cLApProfileCredentialGlobalSecretType": cLApProfileCredentialGlobalSecretType,
       "cLApProfileCredentialGlobalPasswordType": cLApProfileCredentialGlobalPasswordType,
       "cLApProfile802dot1xSupplicantPasswordType": cLApProfile802dot1xSupplicantPasswordType,
       "cLApProfileBssidEnableStats": cLApProfileBssidEnableStats,
       "cLApProfileBssidStatsFrequency": cLApProfileBssidStatsFrequency,
       "cLApProfilePersistentSsidBroadcastEnable": cLApProfilePersistentSsidBroadcastEnable,
       "cLApProfileDhcpFallback": cLApProfileDhcpFallback,
       "cLApProfileOeapRogueDetectionEnable": cLApProfileOeapRogueDetectionEnable,
       "cLApProfileOeapEncryptionEnable": cLApProfileOeapEncryptionEnable,
       "cLApProfileOeapLocalAccessEnable": cLApProfileOeapLocalAccessEnable,
       "cLApProfileOeapProvSsidEnable": cLApProfileOeapProvSsidEnable,
       "cLApProfileCountryCode": cLApProfileCountryCode,
       "cLApProfileHaloBleBeaconTable": cLApProfileHaloBleBeaconTable,
       "cLApProfileHaloBleBeaconEntry": cLApProfileHaloBleBeaconEntry,
       "cLApProfileHaloBleBeaconId": cLApProfileHaloBleBeaconId,
       "cLApProfileHaloBleBeaconUuid": cLApProfileHaloBleBeaconUuid,
       "cLApProfileHaloBleBeaconTxPower": cLApProfileHaloBleBeaconTxPower,
       "cLApProfileHaloBleBeaconEnabled": cLApProfileHaloBleBeaconEnabled,
       "cLApProfileHaloBleBeaconRowStatus": cLApProfileHaloBleBeaconRowStatus,
       "cLApProfileQosMapRangeTable": cLApProfileQosMapRangeTable,
       "cLApProfileQosMapRangeEntry": cLApProfileQosMapRangeEntry,
       "cLApProfileQosMapRangeUP": cLApProfileQosMapRangeUP,
       "cLApProfileQosMapRangeDSCPLower": cLApProfileQosMapRangeDSCPLower,
       "cLApProfileQosMapRangeDSCPUpper": cLApProfileQosMapRangeDSCPUpper,
       "cLApProfileQosMapRangeUPToDSCP": cLApProfileQosMapRangeUPToDSCP,
       "cLApProfileQosMapRangeRowStatus": cLApProfileQosMapRangeRowStatus,
       "cLApProfileQosMapExceptionTable": cLApProfileQosMapExceptionTable,
       "cLApProfileQosMapExceptionEntry": cLApProfileQosMapExceptionEntry,
       "cLApProfileQosMapExceptionDSCP": cLApProfileQosMapExceptionDSCP,
       "cLApProfileQosMapExceptionUP": cLApProfileQosMapExceptionUP,
       "cLApProfileQosMapExceptionRowStatus": cLApProfileQosMapExceptionRowStatus,
       "ciscoLwappApPacketCapture": ciscoLwappApPacketCapture,
       "cLApPacketCaptureProfileTable": cLApPacketCaptureProfileTable,
       "cLApPacketCaptureProfileEntry": cLApPacketCaptureProfileEntry,
       "cLApPacketCaptureProfileName": cLApPacketCaptureProfileName,
       "cLApPacketCaptureProfileRowStatus": cLApPacketCaptureProfileRowStatus,
       "cLApPacketCaptureProfileBufferSize": cLApPacketCaptureProfileBufferSize,
       "cLApPacketCaptureProfileDuration": cLApPacketCaptureProfileDuration,
       "cLApPacketCaptureProfileTruncation": cLApPacketCaptureProfileTruncation,
       "cLApPacketCaptureProfileFtpServerAddressType": cLApPacketCaptureProfileFtpServerAddressType,
       "cLApPacketCaptureProfileFtpServerAddress": cLApPacketCaptureProfileFtpServerAddress,
       "cLApPacketCaptureProfileFtpServerPath": cLApPacketCaptureProfileFtpServerPath,
       "cLApPacketCaptureProfileFtpUsername": cLApPacketCaptureProfileFtpUsername,
       "cLApPacketCaptureProfileFtpPassword": cLApPacketCaptureProfileFtpPassword,
       "cLApPacketCaptureProfileClassifierArp": cLApPacketCaptureProfileClassifierArp,
       "cLApPacketCaptureProfileClassifierBroadcast": cLApPacketCaptureProfileClassifierBroadcast,
       "cLApPacketCaptureProfileClassifierControl": cLApPacketCaptureProfileClassifierControl,
       "cLApPacketCaptureProfileClassifierData": cLApPacketCaptureProfileClassifierData,
       "cLApPacketCaptureProfileClassifierDot1x": cLApPacketCaptureProfileClassifierDot1x,
       "cLApPacketCaptureProfileClassifierIapp": cLApPacketCaptureProfileClassifierIapp,
       "cLApPacketCaptureProfileClassifierIp": cLApPacketCaptureProfileClassifierIp,
       "cLApPacketCaptureProfileClassifierManagement": cLApPacketCaptureProfileClassifierManagement,
       "cLApPacketCaptureProfileClassifierMulticast": cLApPacketCaptureProfileClassifierMulticast,
       "cLApPacketCaptureProfileClassifierTcp": cLApPacketCaptureProfileClassifierTcp,
       "cLApPacketCaptureProfileClassifierUdp": cLApPacketCaptureProfileClassifierUdp,
       "cLApPacketCaptureProfileClassifierTcpPort": cLApPacketCaptureProfileClassifierTcpPort,
       "cLApPacketCaptureProfileClassifierUdpPort": cLApPacketCaptureProfileClassifierUdpPort,
       "cLApPacketCaptureClientTable": cLApPacketCaptureClientTable,
       "cLApPacketCaptureClientEntry": cLApPacketCaptureClientEntry,
       "cLApPacketCaptureClientDeviceMac": cLApPacketCaptureClientDeviceMac,
       "cLApPacketCaptureClientApMacAddress": cLApPacketCaptureClientApMacAddress,
       "cLApPacketCaptureClientAutoMode": cLApPacketCaptureClientAutoMode,
       "cLApPacketCaptureClientStartStop": cLApPacketCaptureClientStartStop,
       "cLApPacketCaptureClientSiteName": cLApPacketCaptureClientSiteName,
       "cLApPacketCaptureClientRowStatus": cLApPacketCaptureClientRowStatus,
       "cLApPacketCaptureApTable": cLApPacketCaptureApTable,
       "cLApPacketCaptureApEntry": cLApPacketCaptureApEntry,
       "cLApPacketCaptureApDeviceMac": cLApPacketCaptureApDeviceMac,
       "cLApPacketCaptureApMacAddress": cLApPacketCaptureApMacAddress,
       "cLApPacketCaptureApStatus": cLApPacketCaptureApStatus,
       "ciscoLwappApNtpInfo": ciscoLwappApNtpInfo,
       "cLAPNtpInfoTable": cLAPNtpInfoTable,
       "cLAPNtpInfoEntry": cLAPNtpInfoEntry,
       "cLAPNtpInfoState": cLAPNtpInfoState,
       "cLApNtpInfoStatus": cLApNtpInfoStatus,
       "cLAPNtpInfoStratum": cLAPNtpInfoStratum,
       "cLAPNtpInfoLastSync": cLAPNtpInfoLastSync,
       "cLAPNtpInfoOffset": cLAPNtpInfoOffset,
       "cLAPNtpInfoIPAddressType": cLAPNtpInfoIPAddressType,
       "cLAPNtpInfoIPAddress": cLAPNtpInfoIPAddress,
       "ciscoLwappAp11axRadioConfig": ciscoLwappAp11axRadioConfig,
       "cLAp11axRadioConfigTable": cLAp11axRadioConfigTable,
       "cLAp11axRadioConfigEntry": cLAp11axRadioConfigEntry,
       "cLAp11axDualRadioCapable": cLAp11axDualRadioCapable,
       "cLAp11axRadioFRACapable": cLAp11axRadioFRACapable,
       "cLAp11axDualRadioOperation": cLAp11axDualRadioOperation,
       "cLAp11axDualRadioMode": cLAp11axDualRadioMode,
       "cLAp11axRadioRoleOperation": cLAp11axRadioRoleOperation,
       "cLAp11axRadioRole": cLAp11axRadioRole,
       "cLAp11axObssPdCapable": cLAp11axObssPdCapable,
       "cLAp11axObssPdSrgCapable": cLAp11axObssPdSrgCapable,
       "ciscoLwappApSlotWlanStats": ciscoLwappApSlotWlanStats,
       "cLApSlotWlanStatsTable": cLApSlotWlanStatsTable,
       "cLApSlotWlanStatsEntry": cLApSlotWlanStatsEntry,
       "cLApSlotWlanStatsTxPktNum": cLApSlotWlanStatsTxPktNum,
       "cLApSlotWlanStatsTxOctetNum": cLApSlotWlanStatsTxOctetNum,
       "cLApSlotWlanStatsRxPktNum": cLApSlotWlanStatsRxPktNum,
       "cLApSlotWlanStatsRxOctetNum": cLApSlotWlanStatsRxOctetNum,
       "cLApSlotWlanStatsRetransmitNum": cLApSlotWlanStatsRetransmitNum,
       "cLApSlotWlanStatsAssocClientNum": cLApSlotWlanStatsAssocClientNum,
       "cLApSlotWlanStatsOnlineUserNum": cLApSlotWlanStatsOnlineUserNum,
       "ciscoLwappApMIBConform": ciscoLwappApMIBConform,
       "ciscoLwappApMIBCompliances": ciscoLwappApMIBCompliances,
       "ciscoLwappApMIBCompliance": ciscoLwappApMIBCompliance,
       "ciscoLwappApMIBComplianceRev1": ciscoLwappApMIBComplianceRev1,
       "ciscoLwappApMIBComplianceRev2": ciscoLwappApMIBComplianceRev2,
       "ciscoLwappApMIBComplianceRev3": ciscoLwappApMIBComplianceRev3,
       "ciscoLwappApMIBComplianceRev4": ciscoLwappApMIBComplianceRev4,
       "ciscoLwappApMIBComplianceRev5": ciscoLwappApMIBComplianceRev5,
       "ciscoLwappApMIBComplianceRev6": ciscoLwappApMIBComplianceRev6,
       "ciscoLwappApMIBComplianceRev7": ciscoLwappApMIBComplianceRev7,
       "ciscoLwappApMIBComplianceRev8": ciscoLwappApMIBComplianceRev8,
       "ciscoLwappApMIBComplianceRev9": ciscoLwappApMIBComplianceRev9,
       "ciscoLwappApMIBComplianceRev10": ciscoLwappApMIBComplianceRev10,
       "ciscoLwappApMIBComplianceRev11": ciscoLwappApMIBComplianceRev11,
       "ciscoLwappApMIBComplianceRev12": ciscoLwappApMIBComplianceRev12,
       "ciscoLwappApMIBComplianceRev13": ciscoLwappApMIBComplianceRev13,
       "ciscoLwappApMIBComplianceRev14": ciscoLwappApMIBComplianceRev14,
       "ciscoLwappApMIBGroups": ciscoLwappApMIBGroups,
       "ciscoLwappApGroup": ciscoLwappApGroup,
       "ciscoLwappApIfGroup": ciscoLwappApIfGroup,
       "ciscoLwappApGroupSup1": ciscoLwappApGroupSup1,
       "ciscoLwappApGroupSup2": ciscoLwappApGroupSup2,
       "ciscoLwappApGroupSup3": ciscoLwappApGroupSup3,
       "ciscoLwappApNotifObjsGroup": ciscoLwappApNotifObjsGroup,
       "ciscoLwappApNotifsGroup": ciscoLwappApNotifsGroup,
       "ciscoLwappApGroupSup4": ciscoLwappApGroupSup4,
       "ciscoLwappApEthernetIfGroup": ciscoLwappApEthernetIfGroup,
       "ciscoLwappApRadioGroup": ciscoLwappApRadioGroup,
       "ciscoLwappApGroupSup5": ciscoLwappApGroupSup5,
       "ciscoLwappSeClientSup": ciscoLwappSeClientSup,
       "ciscoLwappDot11IfAntennaGroup": ciscoLwappDot11IfAntennaGroup,
       "ciscoLwappRetransmitGroup": ciscoLwappRetransmitGroup,
       "ciscoLwappApGroupSup6": ciscoLwappApGroupSup6,
       "ciscoLwappApNotifsGroupVer1": ciscoLwappApNotifsGroupVer1,
       "ciscoLwappApGroupSup7": ciscoLwappApGroupSup7,
       "ciscoLwappApGroupSup8": ciscoLwappApGroupSup8,
       "ciscoLwappApNotifsGroupVer2": ciscoLwappApNotifsGroupVer2,
       "ciscoLwappApGroupSup9": ciscoLwappApGroupSup9,
       "ciscoLwappApRadioGroupSup1": ciscoLwappApRadioGroupSup1,
       "ciscoLwappHaloBleGroup": ciscoLwappHaloBleGroup,
       "ciscoLwappApBleBeaconGroup": ciscoLwappApBleBeaconGroup,
       "ciscoLwappApLanStatsGroup": ciscoLwappApLanStatsGroup,
       "ciscoLwappApGroupSup10": ciscoLwappApGroupSup10,
       "ciscoLwappApXorRadioGroup": ciscoLwappApXorRadioGroup,
       "ciscoLwappApNotifsXorGroup": ciscoLwappApNotifsXorGroup,
       "ciscoLwappApGroupSup11": ciscoLwappApGroupSup11,
       "ciscoLwappApProfileHaloBleGroup": ciscoLwappApProfileHaloBleGroup,
       "ciscoLwappApProfileGroup": ciscoLwappApProfileGroup,
       "ciscoLwappApPacketCaptureProfileGroup": ciscoLwappApPacketCaptureProfileGroup,
       "ciscoLwappApPacketCaptureClientProfileGroup": ciscoLwappApPacketCaptureClientProfileGroup,
       "ciscoLwappApProfileGroupSup1": ciscoLwappApProfileGroupSup1,
       "ciscoLwappApProfileQosMapGroup": ciscoLwappApProfileQosMapGroup,
       "ciscoLwappApProfileGroupSup2": ciscoLwappApProfileGroupSup2,
       "ciscoLwappApGroupSup12": ciscoLwappApGroupSup12,
       "ciscoLwappApGroupSup13": ciscoLwappApGroupSup13,
       "ciscoLwappApLanStatsGroupSup1": ciscoLwappApLanStatsGroupSup1,
       "ciscoLwappApProfileGroupSup3": ciscoLwappApProfileGroupSup3,
       "ciscoLwappApProfileHaloBleGroupSup1": ciscoLwappApProfileHaloBleGroupSup1,
       "ciscoLwappAp11axGroup": ciscoLwappAp11axGroup,
       "ciscoLwappApXorRadioGroupSup1": ciscoLwappApXorRadioGroupSup1,
       "ciscoLwappApProfileGroupSup4": ciscoLwappApProfileGroupSup4,
       "ciscoLwappApGroupSup14": ciscoLwappApGroupSup14,
       "ciscoLwappApXorRadioGroupSup2": ciscoLwappApXorRadioGroupSup2,
       "ciscoLwappApMIBNotifObjects": ciscoLwappApMIBNotifObjects,
       "cLApAssocFailureReason": cLApAssocFailureReason,
       "cLApRogueApMacAddress": cLApRogueApMacAddress,
       "cLApDot11RadioChannelNumber": cLApDot11RadioChannelNumber,
       "cLApRogueApSsid": cLApRogueApSsid,
       "cLApRogueType": cLApRogueType,
       "cLApWipsReason": cLApWipsReason,
       "cLApWipsClear": cLApWipsClear,
       "cLApIfUpDownFailureType": cLApIfUpDownFailureType,
       "cLApIfUpDownCause": cLApIfUpDownCause,
       "cLApIfUpDownFailureCode": cLApIfUpDownFailureCode,
       "cLApAlarmSet": cLApAlarmSet,
       "cLApRogueClassType": cLApRogueClassType,
       "cLApRogueDetectedChannel": cLApRogueDetectedChannel,
       "cLApRSSI": cLApRSSI,
       "cLApSNR": cLApSNR,
       "cLApDot11RadioCurrentChannel": cLApDot11RadioCurrentChannel,
       "cLApAdhocRogue": cLApAdhocRogue,
       "cLApRogueAPOnWiredNetwork": cLApRogueAPOnWiredNetwork,
       "cLApRogueMode": cLApRogueMode,
       "cLApRogueIsClassifiedByRule": cLApRogueIsClassifiedByRule,
       "cLApRogueClassifiedApMacAddress": cLApRogueClassifiedApMacAddress,
       "cLApRogueClassifiedRSSI": cLApRogueClassifiedRSSI,
       "cLAPPreviousMonitorMode": cLAPPreviousMonitorMode,
       "cLAPCurrentMonitorMode": cLAPCurrentMonitorMode,
       "cLApSsidKeyConfSsidA": cLApSsidKeyConfSsidA,
       "cLApSsidKeyConfKeyIdxA": cLApSsidKeyConfKeyIdxA,
       "cLApSsidKeyConfSsidB": cLApSsidKeyConfSsidB,
       "cLApSsidKeyConfKeyIdxB": cLApSsidKeyConfKeyIdxB,
       "cLApPreviousChannel": cLApPreviousChannel,
       "cLApCurrentChannel": cLApCurrentChannel,
       "cLApChannelCustomize": cLApChannelCustomize,
       "cLApIfLoadChannelUtilization": cLApIfLoadChannelUtilization,
       "cLAPGroupVlanName": cLAPGroupVlanName,
       "cLApRuleName": cLApRuleName,
       "cLApSeverityScore": cLApSeverityScore,
       "cLApDot11XorRadioRoleChangeReason": cLApDot11XorRadioRoleChangeReason,
       "cLApDot11XorRadioBandChangeReason": cLApDot11XorRadioBandChangeReason,
       "cLApBrokenAntApName": cLApBrokenAntApName,
       "cLApBrokenAntInfo": cLApBrokenAntInfo,
       "cLApRogueDot11RadioBand": cLApRogueDot11RadioBand}
)
