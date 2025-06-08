# SNMP MIB module (CISCO-LWAPP-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-RRM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cLApName,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName")

(cldcApMacAddress,
 cldcClientMacAddress,
 cldcIfType) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcApMacAddress",
    "cldcClientMacAddress",
    "cldcIfType")

(CLApIfType,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLApIfType")

(cLWlanChdEnable,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanChdEnable")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappRrmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615)
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIB.setRevisions(
        ("2020-10-12 00:00",
         "2020-03-26 00:00",
         "2019-07-30 00:00",
         "2018-09-25 00:00",
         "2017-06-09 00:00",
         "2017-03-28 00:00",
         "2011-03-08 00:00",
         "2007-11-13 00:00",
         "2007-02-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClrRrmTupleTuningRange(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLwappRrmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBNotifs = _CiscoLwappRrmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0)
)
_CiscoLwappRrmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBObjects = _CiscoLwappRrmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1)
)
_ClrRrmConfig_ObjectIdentity = ObjectIdentity
clrRrmConfig = _ClrRrmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1)
)
_ClrRrmParametersTable_Object = MibTable
clrRrmParametersTable = _ClrRrmParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clrRrmParametersTable.setStatus("current")
_ClrRrmParametersEntry_Object = MibTableRow
clrRrmParametersEntry = _ClrRrmParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1)
)
clrRrmParametersEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmParametersEntry.setStatus("current")
_ClrRrmParametersType_Type = CLApIfType
_ClrRrmParametersType_Object = MibTableColumn
clrRrmParametersType = _ClrRrmParametersType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 1),
    _ClrRrmParametersType_Type()
)
clrRrmParametersType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmParametersType.setStatus("current")


class _ClrRrmParametersPicoCellMode_Type(Integer32):
    """Custom type clrRrmParametersPicoCellMode based on Integer32"""
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
        *(("disable", 1),
          ("picoCellv1", 2),
          ("picoCellv2", 3))
    )


_ClrRrmParametersPicoCellMode_Type.__name__ = "Integer32"
_ClrRrmParametersPicoCellMode_Object = MibTableColumn
clrRrmParametersPicoCellMode = _ClrRrmParametersPicoCellMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 2),
    _ClrRrmParametersPicoCellMode_Type()
)
clrRrmParametersPicoCellMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersPicoCellMode.setStatus("deprecated")


class _ClrRrmParametersChdEnable_Type(TruthValue):
    """Custom type clrRrmParametersChdEnable based on TruthValue"""
    defaultValue = 2


_ClrRrmParametersChdEnable_Type.__name__ = "TruthValue"
_ClrRrmParametersChdEnable_Object = MibTableColumn
clrRrmParametersChdEnable = _ClrRrmParametersChdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 3),
    _ClrRrmParametersChdEnable_Type()
)
clrRrmParametersChdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdEnable.setStatus("current")


class _ClrRrmParametersVoicePktCountThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersVoicePktCountThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClrRrmParametersVoicePktCountThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersVoicePktCountThreshold_Object = MibTableColumn
clrRrmParametersVoicePktCountThreshold = _ClrRrmParametersVoicePktCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 4),
    _ClrRrmParametersVoicePktCountThreshold_Type()
)
clrRrmParametersVoicePktCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktCountThreshold.setUnits("packets")


class _ClrRrmParametersVoicePktPercentThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersVoicePktPercentThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClrRrmParametersVoicePktPercentThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersVoicePktPercentThreshold_Object = MibTableColumn
clrRrmParametersVoicePktPercentThreshold = _ClrRrmParametersVoicePktPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 5),
    _ClrRrmParametersVoicePktPercentThreshold_Type()
)
clrRrmParametersVoicePktPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktPercentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersVoicePktPercentThreshold.setUnits("percent")


class _ClrRrmParametersVoiceRssiThreshold_Type(Integer32):
    """Custom type clrRrmParametersVoiceRssiThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_ClrRrmParametersVoiceRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmParametersVoiceRssiThreshold_Object = MibTableColumn
clrRrmParametersVoiceRssiThreshold = _ClrRrmParametersVoiceRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 6),
    _ClrRrmParametersVoiceRssiThreshold_Type()
)
clrRrmParametersVoiceRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersVoiceRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersVoiceRssiThreshold.setUnits("dbm")


class _ClrRrmParametersDataPktCountThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersDataPktCountThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClrRrmParametersDataPktCountThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersDataPktCountThreshold_Object = MibTableColumn
clrRrmParametersDataPktCountThreshold = _ClrRrmParametersDataPktCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 7),
    _ClrRrmParametersDataPktCountThreshold_Type()
)
clrRrmParametersDataPktCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktCountThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktCountThreshold.setUnits("packets")


class _ClrRrmParametersDataPktPercentThreshold_Type(Unsigned32):
    """Custom type clrRrmParametersDataPktPercentThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClrRrmParametersDataPktPercentThreshold_Type.__name__ = "Unsigned32"
_ClrRrmParametersDataPktPercentThreshold_Object = MibTableColumn
clrRrmParametersDataPktPercentThreshold = _ClrRrmParametersDataPktPercentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 8),
    _ClrRrmParametersDataPktPercentThreshold_Type()
)
clrRrmParametersDataPktPercentThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktPercentThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersDataPktPercentThreshold.setUnits("percent")


class _ClrRrmParametersDataRssiThreshold_Type(Integer32):
    """Custom type clrRrmParametersDataRssiThreshold based on Integer32"""
    defaultValue = -74

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_ClrRrmParametersDataRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmParametersDataRssiThreshold_Object = MibTableColumn
clrRrmParametersDataRssiThreshold = _ClrRrmParametersDataRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 9),
    _ClrRrmParametersDataRssiThreshold_Type()
)
clrRrmParametersDataRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDataRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersDataRssiThreshold.setUnits("dbm")


class _ClrRrmParametersDcaChannelWidth_Type(Integer32):
    """Custom type clrRrmParametersDcaChannelWidth based on Integer32"""
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
        *(("twenty", 1),
          ("forty", 2),
          ("eighty", 3),
          ("best", 4),
          ("oneSixty", 5))
    )


_ClrRrmParametersDcaChannelWidth_Type.__name__ = "Integer32"
_ClrRrmParametersDcaChannelWidth_Object = MibTableColumn
clrRrmParametersDcaChannelWidth = _ClrRrmParametersDcaChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 10),
    _ClrRrmParametersDcaChannelWidth_Type()
)
clrRrmParametersDcaChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersDcaChannelWidth.setStatus("current")


class _ClrRrmParametersMaxTxPower_Type(Integer32):
    """Custom type clrRrmParametersMaxTxPower based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 30),
    )


_ClrRrmParametersMaxTxPower_Type.__name__ = "Integer32"
_ClrRrmParametersMaxTxPower_Object = MibTableColumn
clrRrmParametersMaxTxPower = _ClrRrmParametersMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 11),
    _ClrRrmParametersMaxTxPower_Type()
)
clrRrmParametersMaxTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersMaxTxPower.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersMaxTxPower.setUnits("dBm")


class _ClrRrmParametersMinTxPower_Type(Integer32):
    """Custom type clrRrmParametersMinTxPower based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 30),
    )


_ClrRrmParametersMinTxPower_Type.__name__ = "Integer32"
_ClrRrmParametersMinTxPower_Object = MibTableColumn
clrRrmParametersMinTxPower = _ClrRrmParametersMinTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 12),
    _ClrRrmParametersMinTxPower_Type()
)
clrRrmParametersMinTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersMinTxPower.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersMinTxPower.setUnits("dBm")


class _ClrRrmParametersTpcVersion_Type(Integer32):
    """Custom type clrRrmParametersTpcVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("versionOne", 1),
          ("versionTwo", 2))
    )


_ClrRrmParametersTpcVersion_Type.__name__ = "Integer32"
_ClrRrmParametersTpcVersion_Object = MibTableColumn
clrRrmParametersTpcVersion = _ClrRrmParametersTpcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 13),
    _ClrRrmParametersTpcVersion_Type()
)
clrRrmParametersTpcVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersTpcVersion.setStatus("current")
_ClrRrmParametersChdNoise_Type = TruthValue
_ClrRrmParametersChdNoise_Object = MibTableColumn
clrRrmParametersChdNoise = _ClrRrmParametersChdNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 14),
    _ClrRrmParametersChdNoise_Type()
)
clrRrmParametersChdNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdNoise.setStatus("current")
_ClrRrmParametersChdInterference_Type = TruthValue
_ClrRrmParametersChdInterference_Object = MibTableColumn
clrRrmParametersChdInterference = _ClrRrmParametersChdInterference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 15),
    _ClrRrmParametersChdInterference_Type()
)
clrRrmParametersChdInterference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdInterference.setStatus("current")
_ClrRrmParametersChdLoad_Type = TruthValue
_ClrRrmParametersChdLoad_Object = MibTableColumn
clrRrmParametersChdLoad = _ClrRrmParametersChdLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 16),
    _ClrRrmParametersChdLoad_Type()
)
clrRrmParametersChdLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdLoad.setStatus("current")
_ClrRrmParametersChdSignal_Type = TruthValue
_ClrRrmParametersChdSignal_Object = MibTableColumn
clrRrmParametersChdSignal = _ClrRrmParametersChdSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 17),
    _ClrRrmParametersChdSignal_Type()
)
clrRrmParametersChdSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdSignal.setStatus("current")
_ClrRrmParametersChdDevice_Type = TruthValue
_ClrRrmParametersChdDevice_Object = MibTableColumn
clrRrmParametersChdDevice = _ClrRrmParametersChdDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 18),
    _ClrRrmParametersChdDevice_Type()
)
clrRrmParametersChdDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersChdDevice.setStatus("current")
_ClrRrmParametersMaxClients_Type = Unsigned32
_ClrRrmParametersMaxClients_Object = MibTableColumn
clrRrmParametersMaxClients = _ClrRrmParametersMaxClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 19),
    _ClrRrmParametersMaxClients_Type()
)
clrRrmParametersMaxClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersMaxClients.setStatus("current")


class _ClrRrmParametersRssiCheckEnable_Type(TruthValue):
    """Custom type clrRrmParametersRssiCheckEnable based on TruthValue"""
    defaultValue = 2


_ClrRrmParametersRssiCheckEnable_Type.__name__ = "TruthValue"
_ClrRrmParametersRssiCheckEnable_Object = MibTableColumn
clrRrmParametersRssiCheckEnable = _ClrRrmParametersRssiCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 20),
    _ClrRrmParametersRssiCheckEnable_Type()
)
clrRrmParametersRssiCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersRssiCheckEnable.setStatus("current")


class _ClrRrmParametersRssiThreshold_Type(Integer32):
    """Custom type clrRrmParametersRssiThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_ClrRrmParametersRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmParametersRssiThreshold_Object = MibTableColumn
clrRrmParametersRssiThreshold = _ClrRrmParametersRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 21),
    _ClrRrmParametersRssiThreshold_Type()
)
clrRrmParametersRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersRssiThreshold.setUnits("dbm")


class _ClrRrmParametersOptRoamEnable_Type(TruthValue):
    """Custom type clrRrmParametersOptRoamEnable based on TruthValue"""
    defaultValue = 2


_ClrRrmParametersOptRoamEnable_Type.__name__ = "TruthValue"
_ClrRrmParametersOptRoamEnable_Object = MibTableColumn
clrRrmParametersOptRoamEnable = _ClrRrmParametersOptRoamEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 22),
    _ClrRrmParametersOptRoamEnable_Type()
)
clrRrmParametersOptRoamEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamEnable.setStatus("current")


class _ClrRrmParametersOptRoamDataRate_Type(Integer32):
    """Custom type clrRrmParametersOptRoamDataRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_ClrRrmParametersOptRoamDataRate_Type.__name__ = "Integer32"
_ClrRrmParametersOptRoamDataRate_Object = MibTableColumn
clrRrmParametersOptRoamDataRate = _ClrRrmParametersOptRoamDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 23),
    _ClrRrmParametersOptRoamDataRate_Type()
)
clrRrmParametersOptRoamDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamDataRate.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamDataRate.setUnits("mbps")


class _ClrRrmParametersOptRoamInterval_Type(Integer32):
    """Custom type clrRrmParametersOptRoamInterval based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 90),
    )


_ClrRrmParametersOptRoamInterval_Type.__name__ = "Integer32"
_ClrRrmParametersOptRoamInterval_Object = MibTableColumn
clrRrmParametersOptRoamInterval = _ClrRrmParametersOptRoamInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 24),
    _ClrRrmParametersOptRoamInterval_Type()
)
clrRrmParametersOptRoamInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamInterval.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmParametersOptRoamInterval.setUnits("seconds")


class _ClrRrmParametersClientNetworkPreference_Type(Integer32):
    """Custom type clrRrmParametersClientNetworkPreference based on Integer32"""
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
        *(("default", 1),
          ("connectivity", 2),
          ("throughput", 3))
    )


_ClrRrmParametersClientNetworkPreference_Type.__name__ = "Integer32"
_ClrRrmParametersClientNetworkPreference_Object = MibTableColumn
clrRrmParametersClientNetworkPreference = _ClrRrmParametersClientNetworkPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 1, 1, 25),
    _ClrRrmParametersClientNetworkPreference_Type()
)
clrRrmParametersClientNetworkPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmParametersClientNetworkPreference.setStatus("current")
_ClrRrmTupleTable_Object = MibTable
clrRrmTupleTable = _ClrRrmTupleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2)
)
if mibBuilder.loadTexts:
    clrRrmTupleTable.setStatus("deprecated")
_ClrRrmTupleEntry_Object = MibTableRow
clrRrmTupleEntry = _ClrRrmTupleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1)
)
clrRrmTupleEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmTupleEntry.setStatus("deprecated")


class _ClrRrmTupleRxSenseThresholdMin_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleRxSenseThresholdMin based on ClrRrmTupleTuningRange"""
    defaultValue = -127


_ClrRrmTupleRxSenseThresholdMin_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleRxSenseThresholdMin_Object = MibTableColumn
clrRrmTupleRxSenseThresholdMin = _ClrRrmTupleRxSenseThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 1),
    _ClrRrmTupleRxSenseThresholdMin_Type()
)
clrRrmTupleRxSenseThresholdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMin.setUnits("dbm")


class _ClrRrmTupleRxSenseThresholdMax_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleRxSenseThresholdMax based on ClrRrmTupleTuningRange"""
    defaultValue = 127


_ClrRrmTupleRxSenseThresholdMax_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleRxSenseThresholdMax_Object = MibTableColumn
clrRrmTupleRxSenseThresholdMax = _ClrRrmTupleRxSenseThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 2),
    _ClrRrmTupleRxSenseThresholdMax_Type()
)
clrRrmTupleRxSenseThresholdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThresholdMax.setUnits("dbm")


class _ClrRrmTupleRxSenseThreshold_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleRxSenseThreshold based on ClrRrmTupleTuningRange"""
    defaultValue = -80


_ClrRrmTupleRxSenseThreshold_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleRxSenseThreshold_Object = MibTableColumn
clrRrmTupleRxSenseThreshold = _ClrRrmTupleRxSenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 3),
    _ClrRrmTupleRxSenseThreshold_Type()
)
clrRrmTupleRxSenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleRxSenseThreshold.setUnits("dbm")


class _ClrRrmTupleCcaSenseThresholdMin_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleCcaSenseThresholdMin based on ClrRrmTupleTuningRange"""
    defaultValue = -127


_ClrRrmTupleCcaSenseThresholdMin_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleCcaSenseThresholdMin_Object = MibTableColumn
clrRrmTupleCcaSenseThresholdMin = _ClrRrmTupleCcaSenseThresholdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 4),
    _ClrRrmTupleCcaSenseThresholdMin_Type()
)
clrRrmTupleCcaSenseThresholdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMin.setUnits("dbm")


class _ClrRrmTupleCcaSenseThresholdMax_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleCcaSenseThresholdMax based on ClrRrmTupleTuningRange"""
    defaultValue = 127


_ClrRrmTupleCcaSenseThresholdMax_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleCcaSenseThresholdMax_Object = MibTableColumn
clrRrmTupleCcaSenseThresholdMax = _ClrRrmTupleCcaSenseThresholdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 5),
    _ClrRrmTupleCcaSenseThresholdMax_Type()
)
clrRrmTupleCcaSenseThresholdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThresholdMax.setUnits("dbm")


class _ClrRrmTupleCcaSenseThreshold_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleCcaSenseThreshold based on ClrRrmTupleTuningRange"""
    defaultValue = -60


_ClrRrmTupleCcaSenseThreshold_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleCcaSenseThreshold_Object = MibTableColumn
clrRrmTupleCcaSenseThreshold = _ClrRrmTupleCcaSenseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 6),
    _ClrRrmTupleCcaSenseThreshold_Type()
)
clrRrmTupleCcaSenseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleCcaSenseThreshold.setUnits("dbm")


class _ClrRrmTupleTransmitPowerLevelMin_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleTransmitPowerLevelMin based on ClrRrmTupleTuningRange"""
    defaultValue = -127


_ClrRrmTupleTransmitPowerLevelMin_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleTransmitPowerLevelMin_Object = MibTableColumn
clrRrmTupleTransmitPowerLevelMin = _ClrRrmTupleTransmitPowerLevelMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 7),
    _ClrRrmTupleTransmitPowerLevelMin_Type()
)
clrRrmTupleTransmitPowerLevelMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMin.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMin.setUnits("dbm")


class _ClrRrmTupleTransmitPowerLevelMax_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleTransmitPowerLevelMax based on ClrRrmTupleTuningRange"""
    defaultValue = 127


_ClrRrmTupleTransmitPowerLevelMax_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleTransmitPowerLevelMax_Object = MibTableColumn
clrRrmTupleTransmitPowerLevelMax = _ClrRrmTupleTransmitPowerLevelMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 8),
    _ClrRrmTupleTransmitPowerLevelMax_Type()
)
clrRrmTupleTransmitPowerLevelMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMax.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevelMax.setUnits("dbm")


class _ClrRrmTupleTransmitPowerLevel_Type(ClrRrmTupleTuningRange):
    """Custom type clrRrmTupleTransmitPowerLevel based on ClrRrmTupleTuningRange"""
    defaultValue = 10


_ClrRrmTupleTransmitPowerLevel_Type.__name__ = "ClrRrmTupleTuningRange"
_ClrRrmTupleTransmitPowerLevel_Object = MibTableColumn
clrRrmTupleTransmitPowerLevel = _ClrRrmTupleTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 9),
    _ClrRrmTupleTransmitPowerLevel_Type()
)
clrRrmTupleTransmitPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevel.setStatus("deprecated")
if mibBuilder.loadTexts:
    clrRrmTupleTransmitPowerLevel.setUnits("dbm")
_ClrRrmTupleSetDefault_Type = TruthValue
_ClrRrmTupleSetDefault_Object = MibTableColumn
clrRrmTupleSetDefault = _ClrRrmTupleSetDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 2, 1, 10),
    _ClrRrmTupleSetDefault_Type()
)
clrRrmTupleSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTupleSetDefault.setStatus("deprecated")
_ClrRrmChannelTable_Object = MibTable
clrRrmChannelTable = _ClrRrmChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4)
)
if mibBuilder.loadTexts:
    clrRrmChannelTable.setStatus("current")
_ClrRrmChannelEntry_Object = MibTableRow
clrRrmChannelEntry = _ClrRrmChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1)
)
clrRrmChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmChannelNum"),
)
if mibBuilder.loadTexts:
    clrRrmChannelEntry.setStatus("current")
_ClrRrmChannelNum_Type = Unsigned32
_ClrRrmChannelNum_Object = MibTableColumn
clrRrmChannelNum = _ClrRrmChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1, 1),
    _ClrRrmChannelNum_Type()
)
clrRrmChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmChannelNum.setStatus("current")


class _ClrRrmChannelDcaState_Type(TruthValue):
    """Custom type clrRrmChannelDcaState based on TruthValue"""
    defaultValue = 2


_ClrRrmChannelDcaState_Type.__name__ = "TruthValue"
_ClrRrmChannelDcaState_Object = MibTableColumn
clrRrmChannelDcaState = _ClrRrmChannelDcaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1, 2),
    _ClrRrmChannelDcaState_Type()
)
clrRrmChannelDcaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmChannelDcaState.setStatus("current")
_ClrRrmChannelRowStatus_Type = RowStatus
_ClrRrmChannelRowStatus_Object = MibTableColumn
clrRrmChannelRowStatus = _ClrRrmChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 4, 1, 3),
    _ClrRrmChannelRowStatus_Type()
)
clrRrmChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmChannelRowStatus.setStatus("current")
_ClrRrmDot11BandGrpTable_Object = MibTable
clrRrmDot11BandGrpTable = _ClrRrmDot11BandGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5)
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpTable.setStatus("current")
_ClrRrmDot11BandGrpEntry_Object = MibTableRow
clrRrmDot11BandGrpEntry = _ClrRrmDot11BandGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1)
)
clrRrmDot11BandGrpEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpEntry.setStatus("current")
_ClrRrmDot11BandGrpLeaderIpAddressType_Type = InetAddressType
_ClrRrmDot11BandGrpLeaderIpAddressType_Object = MibTableColumn
clrRrmDot11BandGrpLeaderIpAddressType = _ClrRrmDot11BandGrpLeaderIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 1),
    _ClrRrmDot11BandGrpLeaderIpAddressType_Type()
)
clrRrmDot11BandGrpLeaderIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderIpAddressType.setStatus("current")
_ClrRrmDot11BandGrpLeaderIpAddress_Type = InetAddress
_ClrRrmDot11BandGrpLeaderIpAddress_Object = MibTableColumn
clrRrmDot11BandGrpLeaderIpAddress = _ClrRrmDot11BandGrpLeaderIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 2),
    _ClrRrmDot11BandGrpLeaderIpAddress_Type()
)
clrRrmDot11BandGrpLeaderIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderIpAddress.setStatus("current")


class _ClrRrmDot11BandGrpLeaderName_Type(SnmpAdminString):
    """Custom type clrRrmDot11BandGrpLeaderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClrRrmDot11BandGrpLeaderName_Type.__name__ = "SnmpAdminString"
_ClrRrmDot11BandGrpLeaderName_Object = MibTableColumn
clrRrmDot11BandGrpLeaderName = _ClrRrmDot11BandGrpLeaderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 3),
    _ClrRrmDot11BandGrpLeaderName_Type()
)
clrRrmDot11BandGrpLeaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderName.setStatus("current")


class _ClrRrmDot11BandGrpMode_Type(Integer32):
    """Custom type clrRrmDot11BandGrpMode based on Integer32"""
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
        *(("automatic", 1),
          ("off", 2),
          ("leader", 3))
    )


_ClrRrmDot11BandGrpMode_Type.__name__ = "Integer32"
_ClrRrmDot11BandGrpMode_Object = MibTableColumn
clrRrmDot11BandGrpMode = _ClrRrmDot11BandGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 4),
    _ClrRrmDot11BandGrpMode_Type()
)
clrRrmDot11BandGrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpMode.setStatus("current")


class _ClrRrmDot11BandGrpRole_Type(Integer32):
    """Custom type clrRrmDot11BandGrpRole based on Integer32"""
    defaultValue = 2

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
        *(("none", 1),
          ("auto-leader", 2),
          ("auto-member", 3),
          ("static-leader", 4),
          ("static-member", 5))
    )


_ClrRrmDot11BandGrpRole_Type.__name__ = "Integer32"
_ClrRrmDot11BandGrpRole_Object = MibTableColumn
clrRrmDot11BandGrpRole = _ClrRrmDot11BandGrpRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 5),
    _ClrRrmDot11BandGrpRole_Type()
)
clrRrmDot11BandGrpRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpRole.setStatus("current")


class _ClrRrmDot11BandGrpRestart_Type(TruthValue):
    """Custom type clrRrmDot11BandGrpRestart based on TruthValue"""
    defaultValue = 2


_ClrRrmDot11BandGrpRestart_Type.__name__ = "TruthValue"
_ClrRrmDot11BandGrpRestart_Object = MibTableColumn
clrRrmDot11BandGrpRestart = _ClrRrmDot11BandGrpRestart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 6),
    _ClrRrmDot11BandGrpRestart_Type()
)
clrRrmDot11BandGrpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpRestart.setStatus("current")
_ClrRrmDot11BandGrpLastUpdateTime_Type = Unsigned32
_ClrRrmDot11BandGrpLastUpdateTime_Object = MibTableColumn
clrRrmDot11BandGrpLastUpdateTime = _ClrRrmDot11BandGrpLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 7),
    _ClrRrmDot11BandGrpLastUpdateTime_Type()
)
clrRrmDot11BandGrpLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLastUpdateTime.setStatus("current")


class _ClrRrmDot11BandGrpInterval_Type(Unsigned32):
    """Custom type clrRrmDot11BandGrpInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_ClrRrmDot11BandGrpInterval_Type.__name__ = "Unsigned32"
_ClrRrmDot11BandGrpInterval_Object = MibTableColumn
clrRrmDot11BandGrpInterval = _ClrRrmDot11BandGrpInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 8),
    _ClrRrmDot11BandGrpInterval_Type()
)
clrRrmDot11BandGrpInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpInterval.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpInterval.setUnits("seconds")
_ClrRrmDot11BandGrpLeaderIpv6AddressType_Type = InetAddressType
_ClrRrmDot11BandGrpLeaderIpv6AddressType_Object = MibTableColumn
clrRrmDot11BandGrpLeaderIpv6AddressType = _ClrRrmDot11BandGrpLeaderIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 9),
    _ClrRrmDot11BandGrpLeaderIpv6AddressType_Type()
)
clrRrmDot11BandGrpLeaderIpv6AddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderIpv6AddressType.setStatus("current")
_ClrRrmDot11BandGrpLeaderIpv6Address_Type = InetAddress
_ClrRrmDot11BandGrpLeaderIpv6Address_Object = MibTableColumn
clrRrmDot11BandGrpLeaderIpv6Address = _ClrRrmDot11BandGrpLeaderIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 5, 1, 10),
    _ClrRrmDot11BandGrpLeaderIpv6Address_Type()
)
clrRrmDot11BandGrpLeaderIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpLeaderIpv6Address.setStatus("current")
_ClrRrmDot11BandGrpMemberTable_Object = MibTable
clrRrmDot11BandGrpMemberTable = _ClrRrmDot11BandGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6)
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpMemberTable.setStatus("current")
_ClrRrmDot11BandGrpMemberEntry_Object = MibTableRow
clrRrmDot11BandGrpMemberEntry = _ClrRrmDot11BandGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1)
)
clrRrmDot11BandGrpMemberEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberIpAddressType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberIpAddress"),
)
if mibBuilder.loadTexts:
    clrRrmDot11BandGrpMemberEntry.setStatus("current")
_ClrRrmDot11BandMemberIpAddressType_Type = InetAddressType
_ClrRrmDot11BandMemberIpAddressType_Object = MibTableColumn
clrRrmDot11BandMemberIpAddressType = _ClrRrmDot11BandMemberIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 1),
    _ClrRrmDot11BandMemberIpAddressType_Type()
)
clrRrmDot11BandMemberIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberIpAddressType.setStatus("current")
_ClrRrmDot11BandMemberIpAddress_Type = InetAddress
_ClrRrmDot11BandMemberIpAddress_Object = MibTableColumn
clrRrmDot11BandMemberIpAddress = _ClrRrmDot11BandMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 2),
    _ClrRrmDot11BandMemberIpAddress_Type()
)
clrRrmDot11BandMemberIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberIpAddress.setStatus("current")
_ClrRrmDot11BandMemberName_Type = SnmpAdminString
_ClrRrmDot11BandMemberName_Object = MibTableColumn
clrRrmDot11BandMemberName = _ClrRrmDot11BandMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 3),
    _ClrRrmDot11BandMemberName_Type()
)
clrRrmDot11BandMemberName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberName.setStatus("current")


class _ClrRrmDot11BandMemberIsJoined_Type(TruthValue):
    """Custom type clrRrmDot11BandMemberIsJoined based on TruthValue"""
    defaultValue = 1


_ClrRrmDot11BandMemberIsJoined_Type.__name__ = "TruthValue"
_ClrRrmDot11BandMemberIsJoined_Object = MibTableColumn
clrRrmDot11BandMemberIsJoined = _ClrRrmDot11BandMemberIsJoined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 4),
    _ClrRrmDot11BandMemberIsJoined_Type()
)
clrRrmDot11BandMemberIsJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberIsJoined.setStatus("current")


class _ClrRrmDot11BandMemberJoinFailureReason_Type(Integer32):
    """Custom type clrRrmDot11BandMemberJoinFailureReason based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("joinedSuccessfully", 1),
          ("invalidIp", 2),
          ("groupSizeExceeded", 3),
          ("invalidGroupOrder", 4),
          ("nonMatchingGroupID", 5),
          ("unexpectedError", 6),
          ("weakSignalStrength", 7),
          ("joinPending", 8),
          ("notAManager", 9),
          ("groupingDelayed", 10),
          ("groupingDisabled", 11),
          ("invalidProtocolVersion", 12),
          ("countryCodeMismatch", 13),
          ("invalidHierarchy", 14),
          ("alreadyAStaticLeader", 15),
          ("memberOfAnotherGroup", 16),
          ("unconfiguredAsStaticMember", 17),
          ("cntlrNameAndIpMismatch", 18),
          ("unexpectedMemoryError", 19),
          ("rfDomainMismatch", 20),
          ("splitForInvalidStateRequest", 21),
          ("transitioningToStaticFromAuto", 22),
          ("splitDueToUserAction", 23))
    )


_ClrRrmDot11BandMemberJoinFailureReason_Type.__name__ = "Integer32"
_ClrRrmDot11BandMemberJoinFailureReason_Object = MibTableColumn
clrRrmDot11BandMemberJoinFailureReason = _ClrRrmDot11BandMemberJoinFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 5),
    _ClrRrmDot11BandMemberJoinFailureReason_Type()
)
clrRrmDot11BandMemberJoinFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberJoinFailureReason.setStatus("current")
_ClrRrmDot11BandMemberRowStatus_Type = RowStatus
_ClrRrmDot11BandMemberRowStatus_Object = MibTableColumn
clrRrmDot11BandMemberRowStatus = _ClrRrmDot11BandMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 6, 1, 6),
    _ClrRrmDot11BandMemberRowStatus_Type()
)
clrRrmDot11BandMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmDot11BandMemberRowStatus.setStatus("current")
_ClrRrmDcaConfig_ObjectIdentity = ObjectIdentity
clrRrmDcaConfig = _ClrRrmDcaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 7)
)
_ClrRrmDcaDot11aOutdoorAPDca_Type = TruthValue
_ClrRrmDcaDot11aOutdoorAPDca_Object = MibScalar
clrRrmDcaDot11aOutdoorAPDca = _ClrRrmDcaDot11aOutdoorAPDca_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 7, 1),
    _ClrRrmDcaDot11aOutdoorAPDca_Type()
)
clrRrmDcaDot11aOutdoorAPDca.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmDcaDot11aOutdoorAPDca.setStatus("current")
_ClrRrmRfGroupingPriority_Type = Unsigned32
_ClrRrmRfGroupingPriority_Object = MibScalar
clrRrmRfGroupingPriority = _ClrRrmRfGroupingPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 8),
    _ClrRrmRfGroupingPriority_Type()
)
clrRrmRfGroupingPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmRfGroupingPriority.setStatus("current")
_ClrRrmDcaChannelListTable_Object = MibTable
clrRrmDcaChannelListTable = _ClrRrmDcaChannelListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 9)
)
if mibBuilder.loadTexts:
    clrRrmDcaChannelListTable.setStatus("current")
_ClrRrmDcaChannelListEntry_Object = MibTableRow
clrRrmDcaChannelListEntry = _ClrRrmDcaChannelListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 9, 1)
)
clrRrmDcaChannelListEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmDcaChannelListEntry.setStatus("current")
_ClrRrmDcaUsedChannelList_Type = SnmpAdminString
_ClrRrmDcaUsedChannelList_Object = MibTableColumn
clrRrmDcaUsedChannelList = _ClrRrmDcaUsedChannelList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 9, 1, 1),
    _ClrRrmDcaUsedChannelList_Type()
)
clrRrmDcaUsedChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDcaUsedChannelList.setStatus("current")
_ClrRrmDcaUnusedChannelList_Type = SnmpAdminString
_ClrRrmDcaUnusedChannelList_Object = MibTableColumn
clrRrmDcaUnusedChannelList = _ClrRrmDcaUnusedChannelList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 9, 1, 2),
    _ClrRrmDcaUnusedChannelList_Type()
)
clrRrmDcaUnusedChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDcaUnusedChannelList.setStatus("current")
_ClrRrmDcaDefaultChannelList_Type = SnmpAdminString
_ClrRrmDcaDefaultChannelList_Object = MibTableColumn
clrRrmDcaDefaultChannelList = _ClrRrmDcaDefaultChannelList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 9, 1, 3),
    _ClrRrmDcaDefaultChannelList_Type()
)
clrRrmDcaDefaultChannelList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDcaDefaultChannelList.setStatus("current")
_ClrRrmPakRssiConfig_ObjectIdentity = ObjectIdentity
clrRrmPakRssiConfig = _ClrRrmPakRssiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10)
)


class _ClrRrmHyperLocationEnable_Type(TruthValue):
    """Custom type clrRrmHyperLocationEnable based on TruthValue"""
    defaultValue = 2


_ClrRrmHyperLocationEnable_Type.__name__ = "TruthValue"
_ClrRrmHyperLocationEnable_Object = MibScalar
clrRrmHyperLocationEnable = _ClrRrmHyperLocationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 1),
    _ClrRrmHyperLocationEnable_Type()
)
clrRrmHyperLocationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmHyperLocationEnable.setStatus("current")


class _ClrRrmPakRssiThreshold_Type(Integer32):
    """Custom type clrRrmPakRssiThreshold based on Integer32"""
    defaultValue = -100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -50),
    )


_ClrRrmPakRssiThreshold_Type.__name__ = "Integer32"
_ClrRrmPakRssiThreshold_Object = MibScalar
clrRrmPakRssiThreshold = _ClrRrmPakRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 2),
    _ClrRrmPakRssiThreshold_Type()
)
clrRrmPakRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmPakRssiThreshold.setUnits("dbm")


class _ClrRrmPakRssiThresholdTrigger_Type(Integer32):
    """Custom type clrRrmPakRssiThresholdTrigger based on Integer32"""
    defaultValue = 10


_ClrRrmPakRssiThresholdTrigger_Type.__name__ = "Integer32"
_ClrRrmPakRssiThresholdTrigger_Object = MibScalar
clrRrmPakRssiThresholdTrigger = _ClrRrmPakRssiThresholdTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 3),
    _ClrRrmPakRssiThresholdTrigger_Type()
)
clrRrmPakRssiThresholdTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiThresholdTrigger.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmPakRssiThresholdTrigger.setUnits("dbm")


class _ClrRrmPakRssiNtpIpAddressType_Type(InetAddressType):
    """Custom type clrRrmPakRssiNtpIpAddressType based on InetAddressType"""
    defaultValue = 1


_ClrRrmPakRssiNtpIpAddressType_Type.__name__ = "InetAddressType"
_ClrRrmPakRssiNtpIpAddressType_Object = MibScalar
clrRrmPakRssiNtpIpAddressType = _ClrRrmPakRssiNtpIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 4),
    _ClrRrmPakRssiNtpIpAddressType_Type()
)
clrRrmPakRssiNtpIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiNtpIpAddressType.setStatus("deprecated")
_ClrRrmPakRssiNtp_Type = InetAddress
_ClrRrmPakRssiNtp_Object = MibScalar
clrRrmPakRssiNtp = _ClrRrmPakRssiNtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 10, 5),
    _ClrRrmPakRssiNtp_Type()
)
clrRrmPakRssiNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmPakRssiNtp.setStatus("deprecated")
_ClrRrmFraConfig_ObjectIdentity = ObjectIdentity
clrRrmFraConfig = _ClrRrmFraConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11)
)


class _ClrRrmFraEnable_Type(TruthValue):
    """Custom type clrRrmFraEnable based on TruthValue"""
    defaultValue = 2


_ClrRrmFraEnable_Type.__name__ = "TruthValue"
_ClrRrmFraEnable_Object = MibScalar
clrRrmFraEnable = _ClrRrmFraEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 1),
    _ClrRrmFraEnable_Type()
)
clrRrmFraEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmFraEnable.setStatus("current")


class _ClrRrmFraInterval_Type(Integer32):
    """Custom type clrRrmFraInterval based on Integer32"""
    defaultValue = 1


_ClrRrmFraInterval_Type.__name__ = "Integer32"
_ClrRrmFraInterval_Object = MibScalar
clrRrmFraInterval = _ClrRrmFraInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 2),
    _ClrRrmFraInterval_Type()
)
clrRrmFraInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmFraInterval.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmFraInterval.setUnits("hours")


class _ClrRrmFraSensitivity_Type(Integer32):
    """Custom type clrRrmFraSensitivity based on Integer32"""
    defaultValue = 1

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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("higher", 4),
          ("evenhigher", 5),
          ("superhigh", 6))
    )


_ClrRrmFraSensitivity_Type.__name__ = "Integer32"
_ClrRrmFraSensitivity_Object = MibScalar
clrRrmFraSensitivity = _ClrRrmFraSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 3),
    _ClrRrmFraSensitivity_Type()
)
clrRrmFraSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmFraSensitivity.setStatus("current")


class _ClrRrmFraSensorThreshold_Type(Integer32):
    """Custom type clrRrmFraSensorThreshold based on Integer32"""
    defaultValue = 0

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
        *(("clientPriority", 0),
          ("clientPreferred", 1),
          ("balanced", 2),
          ("sensorPreferred", 3),
          ("sensorPriority", 4))
    )


_ClrRrmFraSensorThreshold_Type.__name__ = "Integer32"
_ClrRrmFraSensorThreshold_Object = MibScalar
clrRrmFraSensorThreshold = _ClrRrmFraSensorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 4),
    _ClrRrmFraSensorThreshold_Type()
)
clrRrmFraSensorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmFraSensorThreshold.setStatus("current")


class _ClrRrmFraSensorCoverage_Type(Unsigned32):
    """Custom type clrRrmFraSensorCoverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ClrRrmFraSensorCoverage_Type.__name__ = "Unsigned32"
_ClrRrmFraSensorCoverage_Object = MibScalar
clrRrmFraSensorCoverage = _ClrRrmFraSensorCoverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 5),
    _ClrRrmFraSensorCoverage_Type()
)
clrRrmFraSensorCoverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmFraSensorCoverage.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmFraSensorCoverage.setUnits("percent")


class _ClrRrmFraServicePriority_Type(Integer32):
    """Custom type clrRrmFraServicePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coverage", 0),
          ("clientAware", 1),
          ("serviceAssurance", 2))
    )


_ClrRrmFraServicePriority_Type.__name__ = "Integer32"
_ClrRrmFraServicePriority_Object = MibScalar
clrRrmFraServicePriority = _ClrRrmFraServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 6),
    _ClrRrmFraServicePriority_Type()
)
clrRrmFraServicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmFraServicePriority.setStatus("current")
_ClrRrmFraSensorDensityOptimisationTargetRssi_Type = Integer32
_ClrRrmFraSensorDensityOptimisationTargetRssi_Object = MibScalar
clrRrmFraSensorDensityOptimisationTargetRssi = _ClrRrmFraSensorDensityOptimisationTargetRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 11, 7),
    _ClrRrmFraSensorDensityOptimisationTargetRssi_Type()
)
clrRrmFraSensorDensityOptimisationTargetRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmFraSensorDensityOptimisationTargetRssi.setStatus("current")
if mibBuilder.loadTexts:
    clrRrmFraSensorDensityOptimisationTargetRssi.setUnits("dbm")
_ClrRrm11kConfig_ObjectIdentity = ObjectIdentity
clrRrm11kConfig = _ClrRrm11kConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 12)
)


class _ClrRrm11kDenialMax_Type(Unsigned32):
    """Custom type clrRrm11kDenialMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ClrRrm11kDenialMax_Type.__name__ = "Unsigned32"
_ClrRrm11kDenialMax_Object = MibScalar
clrRrm11kDenialMax = _ClrRrm11kDenialMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 12, 1),
    _ClrRrm11kDenialMax_Type()
)
clrRrm11kDenialMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrm11kDenialMax.setStatus("current")
if mibBuilder.loadTexts:
    clrRrm11kDenialMax.setUnits("count")


class _ClrRrm11kFloorBias_Type(Unsigned32):
    """Custom type clrRrm11kFloorBias based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_ClrRrm11kFloorBias_Type.__name__ = "Unsigned32"
_ClrRrm11kFloorBias_Object = MibScalar
clrRrm11kFloorBias = _ClrRrm11kFloorBias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 12, 2),
    _ClrRrm11kFloorBias_Type()
)
clrRrm11kFloorBias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrm11kFloorBias.setStatus("current")
if mibBuilder.loadTexts:
    clrRrm11kFloorBias.setUnits("dBm")


class _ClrRrm11kPredictionMin_Type(Unsigned32):
    """Custom type clrRrm11kPredictionMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 6),
    )


_ClrRrm11kPredictionMin_Type.__name__ = "Unsigned32"
_ClrRrm11kPredictionMin_Object = MibScalar
clrRrm11kPredictionMin = _ClrRrm11kPredictionMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 12, 3),
    _ClrRrm11kPredictionMin_Type()
)
clrRrm11kPredictionMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrm11kPredictionMin.setStatus("current")
if mibBuilder.loadTexts:
    clrRrm11kPredictionMin.setUnits("count")
_ClrRrmRemoveChannelTable_Object = MibTable
clrRrmRemoveChannelTable = _ClrRrmRemoveChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 13)
)
if mibBuilder.loadTexts:
    clrRrmRemoveChannelTable.setStatus("current")
_ClrRrmRemoveChannelEntry_Object = MibTableRow
clrRrmRemoveChannelEntry = _ClrRrmRemoveChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 13, 1)
)
clrRrmRemoveChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmRemoveChannelNum"),
)
if mibBuilder.loadTexts:
    clrRrmRemoveChannelEntry.setStatus("current")
_ClrRrmRemoveChannelNum_Type = Unsigned32
_ClrRrmRemoveChannelNum_Object = MibTableColumn
clrRrmRemoveChannelNum = _ClrRrmRemoveChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 13, 1, 1),
    _ClrRrmRemoveChannelNum_Type()
)
clrRrmRemoveChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmRemoveChannelNum.setStatus("current")


class _ClrRrmRemovedChannelDcaState_Type(TruthValue):
    """Custom type clrRrmRemovedChannelDcaState based on TruthValue"""
    defaultValue = 2


_ClrRrmRemovedChannelDcaState_Type.__name__ = "TruthValue"
_ClrRrmRemovedChannelDcaState_Object = MibTableColumn
clrRrmRemovedChannelDcaState = _ClrRrmRemovedChannelDcaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 13, 1, 2),
    _ClrRrmRemovedChannelDcaState_Type()
)
clrRrmRemovedChannelDcaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmRemovedChannelDcaState.setStatus("current")
_ClrRrmRemoveChannelRowStatus_Type = RowStatus
_ClrRrmRemoveChannelRowStatus_Object = MibTableColumn
clrRrmRemoveChannelRowStatus = _ClrRrmRemoveChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 13, 1, 3),
    _ClrRrmRemoveChannelRowStatus_Type()
)
clrRrmRemoveChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmRemoveChannelRowStatus.setStatus("current")
_ClrRrmAddChannelTable_Object = MibTable
clrRrmAddChannelTable = _ClrRrmAddChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 14)
)
if mibBuilder.loadTexts:
    clrRrmAddChannelTable.setStatus("current")
_ClrRrmAddChannelEntry_Object = MibTableRow
clrRrmAddChannelEntry = _ClrRrmAddChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 14, 1)
)
clrRrmAddChannelEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmAddChannelNum"),
)
if mibBuilder.loadTexts:
    clrRrmAddChannelEntry.setStatus("current")
_ClrRrmAddChannelNum_Type = Unsigned32
_ClrRrmAddChannelNum_Object = MibTableColumn
clrRrmAddChannelNum = _ClrRrmAddChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 14, 1, 1),
    _ClrRrmAddChannelNum_Type()
)
clrRrmAddChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmAddChannelNum.setStatus("current")


class _ClrRrmAddedChannelDcaState_Type(TruthValue):
    """Custom type clrRrmAddedChannelDcaState based on TruthValue"""
    defaultValue = 1


_ClrRrmAddedChannelDcaState_Type.__name__ = "TruthValue"
_ClrRrmAddedChannelDcaState_Object = MibTableColumn
clrRrmAddedChannelDcaState = _ClrRrmAddedChannelDcaState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 14, 1, 2),
    _ClrRrmAddedChannelDcaState_Type()
)
clrRrmAddedChannelDcaState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmAddedChannelDcaState.setStatus("current")
_ClrRrmAddChannelRowStatus_Type = RowStatus
_ClrRrmAddChannelRowStatus_Object = MibTableColumn
clrRrmAddChannelRowStatus = _ClrRrmAddChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 14, 1, 3),
    _ClrRrmAddChannelRowStatus_Type()
)
clrRrmAddChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clrRrmAddChannelRowStatus.setStatus("current")
_ClrRrmDot11BandJoinedGrpMemberTable_Object = MibTable
clrRrmDot11BandJoinedGrpMemberTable = _ClrRrmDot11BandJoinedGrpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15)
)
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedGrpMemberTable.setStatus("current")
_ClrRrmDot11BandJoinedGrpMemberEntry_Object = MibTableRow
clrRrmDot11BandJoinedGrpMemberEntry = _ClrRrmDot11BandJoinedGrpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1)
)
clrRrmDot11BandJoinedGrpMemberEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberIpAddressType"),
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberIpAddress"),
)
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedGrpMemberEntry.setStatus("current")
_ClrRrmDot11BandJoinedMemberIpAddressType_Type = InetAddressType
_ClrRrmDot11BandJoinedMemberIpAddressType_Object = MibTableColumn
clrRrmDot11BandJoinedMemberIpAddressType = _ClrRrmDot11BandJoinedMemberIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 1),
    _ClrRrmDot11BandJoinedMemberIpAddressType_Type()
)
clrRrmDot11BandJoinedMemberIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberIpAddressType.setStatus("current")
_ClrRrmDot11BandJoinedMemberIpAddress_Type = InetAddress
_ClrRrmDot11BandJoinedMemberIpAddress_Object = MibTableColumn
clrRrmDot11BandJoinedMemberIpAddress = _ClrRrmDot11BandJoinedMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 2),
    _ClrRrmDot11BandJoinedMemberIpAddress_Type()
)
clrRrmDot11BandJoinedMemberIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberIpAddress.setStatus("current")
_ClrRrmDot11BandJoinedMemberName_Type = SnmpAdminString
_ClrRrmDot11BandJoinedMemberName_Object = MibTableColumn
clrRrmDot11BandJoinedMemberName = _ClrRrmDot11BandJoinedMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 3),
    _ClrRrmDot11BandJoinedMemberName_Type()
)
clrRrmDot11BandJoinedMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberName.setStatus("current")


class _ClrRrmDot11BandJoinedMemberIsJoined_Type(TruthValue):
    """Custom type clrRrmDot11BandJoinedMemberIsJoined based on TruthValue"""
    defaultValue = 1


_ClrRrmDot11BandJoinedMemberIsJoined_Type.__name__ = "TruthValue"
_ClrRrmDot11BandJoinedMemberIsJoined_Object = MibTableColumn
clrRrmDot11BandJoinedMemberIsJoined = _ClrRrmDot11BandJoinedMemberIsJoined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 4),
    _ClrRrmDot11BandJoinedMemberIsJoined_Type()
)
clrRrmDot11BandJoinedMemberIsJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberIsJoined.setStatus("current")


class _ClrRrmDot11BandJoinedMemberJoinFailureReason_Type(Integer32):
    """Custom type clrRrmDot11BandJoinedMemberJoinFailureReason based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("joinedSuccessfully", 1),
          ("invalidIp", 2),
          ("groupSizeExceeded", 3),
          ("invalidGroupOrder", 4),
          ("nonMatchingGroupID", 5),
          ("unexpectedError", 6),
          ("weakSignalStrength", 7),
          ("joinPending", 8),
          ("notAManager", 9),
          ("groupingDelayed", 10),
          ("groupingDisabled", 11),
          ("invalidProtocolVersion", 12),
          ("countryCodeMismatch", 13),
          ("invalidHierarchy", 14),
          ("alreadyAStaticLeader", 15),
          ("memberOfAnotherGroup", 16),
          ("unconfiguredAsStaticMember", 17),
          ("cntlrNameAndIpMismatch", 18),
          ("unexpectedMemoryError", 19),
          ("rfDomainMismatch", 20))
    )


_ClrRrmDot11BandJoinedMemberJoinFailureReason_Type.__name__ = "Integer32"
_ClrRrmDot11BandJoinedMemberJoinFailureReason_Object = MibTableColumn
clrRrmDot11BandJoinedMemberJoinFailureReason = _ClrRrmDot11BandJoinedMemberJoinFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 5),
    _ClrRrmDot11BandJoinedMemberJoinFailureReason_Type()
)
clrRrmDot11BandJoinedMemberJoinFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberJoinFailureReason.setStatus("current")
_ClrRrmDot11BandJoinedMemberIpv6AddressType_Type = InetAddressType
_ClrRrmDot11BandJoinedMemberIpv6AddressType_Object = MibTableColumn
clrRrmDot11BandJoinedMemberIpv6AddressType = _ClrRrmDot11BandJoinedMemberIpv6AddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 6),
    _ClrRrmDot11BandJoinedMemberIpv6AddressType_Type()
)
clrRrmDot11BandJoinedMemberIpv6AddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberIpv6AddressType.setStatus("current")
_ClrRrmDot11BandJoinedMemberIpv6Address_Type = InetAddress
_ClrRrmDot11BandJoinedMemberIpv6Address_Object = MibTableColumn
clrRrmDot11BandJoinedMemberIpv6Address = _ClrRrmDot11BandJoinedMemberIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 15, 1, 7),
    _ClrRrmDot11BandJoinedMemberIpv6Address_Type()
)
clrRrmDot11BandJoinedMemberIpv6Address.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clrRrmDot11BandJoinedMemberIpv6Address.setStatus("current")
_ClrRrmBcoTable_Object = MibTable
clrRrmBcoTable = _ClrRrmBcoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 16)
)
if mibBuilder.loadTexts:
    clrRrmBcoTable.setStatus("current")
_ClrRrmBcoEntry_Object = MibTableRow
clrRrmBcoEntry = _ClrRrmBcoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 16, 1)
)
clrRrmBcoEntry.setIndexNames(
    (0, "CISCO-LWAPP-RRM-MIB", "clrRrmParametersType"),
)
if mibBuilder.loadTexts:
    clrRrmBcoEntry.setStatus("current")


class _ClRrmBcoMode_Type(Integer32):
    """Custom type clRrmBcoMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("static", 2))
    )


_ClRrmBcoMode_Type.__name__ = "Integer32"
_ClRrmBcoMode_Object = MibTableColumn
clRrmBcoMode = _ClRrmBcoMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 16, 1, 1),
    _ClRrmBcoMode_Type()
)
clRrmBcoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clRrmBcoMode.setStatus("current")
_ClrRrmTriRadioConfig_ObjectIdentity = ObjectIdentity
clrRrmTriRadioConfig = _ClrRrmTriRadioConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 17)
)


class _ClrRrmTriRadioMode_Type(TruthValue):
    """Custom type clrRrmTriRadioMode based on TruthValue"""
    defaultValue = 2


_ClrRrmTriRadioMode_Type.__name__ = "TruthValue"
_ClrRrmTriRadioMode_Object = MibScalar
clrRrmTriRadioMode = _ClrRrmTriRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 1, 17, 1),
    _ClrRrmTriRadioMode_Type()
)
clrRrmTriRadioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clrRrmTriRadioMode.setStatus("current")
_ClrRrmNotificationVariable_ObjectIdentity = ObjectIdentity
clrRrmNotificationVariable = _ClrRrmNotificationVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2)
)


class _ClrRrmApTransmitPowerLevel_Type(Integer32):
    """Custom type clrRrmApTransmitPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 200),
    )


_ClrRrmApTransmitPowerLevel_Type.__name__ = "Integer32"
_ClrRrmApTransmitPowerLevel_Object = MibScalar
clrRrmApTransmitPowerLevel = _ClrRrmApTransmitPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 1),
    _ClrRrmApTransmitPowerLevel_Type()
)
clrRrmApTransmitPowerLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmApTransmitPowerLevel.setStatus("current")
_ClrRrmTimeStamp_Type = TimeStamp
_ClrRrmTimeStamp_Object = MibScalar
clrRrmTimeStamp = _ClrRrmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 2),
    _ClrRrmTimeStamp_Type()
)
clrRrmTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmTimeStamp.setStatus("current")


class _ClrRrmClientType_Type(Integer32):
    """Custom type clrRrmClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_ClrRrmClientType_Type.__name__ = "Integer32"
_ClrRrmClientType_Object = MibScalar
clrRrmClientType = _ClrRrmClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 3),
    _ClrRrmClientType_Type()
)
clrRrmClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmClientType.setStatus("current")
_ClrRrmRssiHistogramLength_Type = Unsigned32
_ClrRrmRssiHistogramLength_Object = MibScalar
clrRrmRssiHistogramLength = _ClrRrmRssiHistogramLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 4),
    _ClrRrmRssiHistogramLength_Type()
)
clrRrmRssiHistogramLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramLength.setStatus("current")
_ClrRrmRssiHistogramMaxIndex_Type = Integer32
_ClrRrmRssiHistogramMaxIndex_Object = MibScalar
clrRrmRssiHistogramMaxIndex = _ClrRrmRssiHistogramMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 5),
    _ClrRrmRssiHistogramMaxIndex_Type()
)
clrRrmRssiHistogramMaxIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramMaxIndex.setStatus("current")
_ClrRrmRssiHistogramMinIndex_Type = Integer32
_ClrRrmRssiHistogramMinIndex_Object = MibScalar
clrRrmRssiHistogramMinIndex = _ClrRrmRssiHistogramMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 6),
    _ClrRrmRssiHistogramMinIndex_Type()
)
clrRrmRssiHistogramMinIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramMinIndex.setStatus("current")
_ClrRrmRssiHistogramValues_Type = SnmpAdminString
_ClrRrmRssiHistogramValues_Object = MibScalar
clrRrmRssiHistogramValues = _ClrRrmRssiHistogramValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 7),
    _ClrRrmRssiHistogramValues_Type()
)
clrRrmRssiHistogramValues.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramValues.setStatus("current")
_ClrRrmNeighborApCount_Type = Unsigned32
_ClrRrmNeighborApCount_Object = MibScalar
clrRrmNeighborApCount = _ClrRrmNeighborApCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 8),
    _ClrRrmNeighborApCount_Type()
)
clrRrmNeighborApCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApCount.setStatus("current")
_ClrRrmNeighborApMacAddress_Type = SnmpAdminString
_ClrRrmNeighborApMacAddress_Object = MibScalar
clrRrmNeighborApMacAddress = _ClrRrmNeighborApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 9),
    _ClrRrmNeighborApMacAddress_Type()
)
clrRrmNeighborApMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApMacAddress.setStatus("current")
_ClrRrmNeighborApRssi_Type = SnmpAdminString
_ClrRrmNeighborApRssi_Object = MibScalar
clrRrmNeighborApRssi = _ClrRrmNeighborApRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 10),
    _ClrRrmNeighborApRssi_Type()
)
clrRrmNeighborApRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApRssi.setStatus("current")
_ClrRrmNeighborApIfType_Type = SnmpAdminString
_ClrRrmNeighborApIfType_Object = MibScalar
clrRrmNeighborApIfType = _ClrRrmNeighborApIfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 11),
    _ClrRrmNeighborApIfType_Type()
)
clrRrmNeighborApIfType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApIfType.setStatus("current")
_ClrRrmSysMacAddress_Type = MacAddress
_ClrRrmSysMacAddress_Object = MibScalar
clrRrmSysMacAddress = _ClrRrmSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 12),
    _ClrRrmSysMacAddress_Type()
)
clrRrmSysMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysMacAddress.setStatus("current")
_ClrRrmSysIdentifier_Type = OctetString
_ClrRrmSysIdentifier_Object = MibScalar
clrRrmSysIdentifier = _ClrRrmSysIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 13),
    _ClrRrmSysIdentifier_Type()
)
clrRrmSysIdentifier.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysIdentifier.setStatus("current")
_ClrRrmRssiHistogramValuesRev_Type = Unsigned32
_ClrRrmRssiHistogramValuesRev_Object = MibScalar
clrRrmRssiHistogramValuesRev = _ClrRrmRssiHistogramValuesRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 14),
    _ClrRrmRssiHistogramValuesRev_Type()
)
clrRrmRssiHistogramValuesRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmRssiHistogramValuesRev.setStatus("current")
_ClrRrmNeighborApCountRev_Type = Unsigned32
_ClrRrmNeighborApCountRev_Object = MibScalar
clrRrmNeighborApCountRev = _ClrRrmNeighborApCountRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 15),
    _ClrRrmNeighborApCountRev_Type()
)
clrRrmNeighborApCountRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApCountRev.setStatus("current")
_ClrRrmNeighborApMacAddressRev_Type = SnmpAdminString
_ClrRrmNeighborApMacAddressRev_Object = MibScalar
clrRrmNeighborApMacAddressRev = _ClrRrmNeighborApMacAddressRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 16),
    _ClrRrmNeighborApMacAddressRev_Type()
)
clrRrmNeighborApMacAddressRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApMacAddressRev.setStatus("current")
_ClrRrmNeighborApRssiRev_Type = SnmpAdminString
_ClrRrmNeighborApRssiRev_Object = MibScalar
clrRrmNeighborApRssiRev = _ClrRrmNeighborApRssiRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 17),
    _ClrRrmNeighborApRssiRev_Type()
)
clrRrmNeighborApRssiRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApRssiRev.setStatus("current")
_ClrRrmNeighborApIfTypeRev_Type = SnmpAdminString
_ClrRrmNeighborApIfTypeRev_Object = MibScalar
clrRrmNeighborApIfTypeRev = _ClrRrmNeighborApIfTypeRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 18),
    _ClrRrmNeighborApIfTypeRev_Type()
)
clrRrmNeighborApIfTypeRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmNeighborApIfTypeRev.setStatus("current")
_ClrRrmSysMacAddressRev_Type = MacAddress
_ClrRrmSysMacAddressRev_Object = MibScalar
clrRrmSysMacAddressRev = _ClrRrmSysMacAddressRev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 19),
    _ClrRrmSysMacAddressRev_Type()
)
clrRrmSysMacAddressRev.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysMacAddressRev.setStatus("current")
_ClrRrmSysIpAddressType_Type = InetAddressType
_ClrRrmSysIpAddressType_Object = MibScalar
clrRrmSysIpAddressType = _ClrRrmSysIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 20),
    _ClrRrmSysIpAddressType_Type()
)
clrRrmSysIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysIpAddressType.setStatus("current")
_ClrRrmSysIpAddress_Type = InetAddress
_ClrRrmSysIpAddress_Object = MibScalar
clrRrmSysIpAddress = _ClrRrmSysIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 1, 2, 21),
    _ClrRrmSysIpAddress_Type()
)
clrRrmSysIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clrRrmSysIpAddress.setStatus("current")
_CiscoLwappRrmMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBConform = _CiscoLwappRrmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2)
)
_CiscoLwappRrmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBCompliances = _CiscoLwappRrmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1)
)
_CiscoLwappRrmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappRrmMIBGroups = _CiscoLwappRrmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2)
)

# Managed Objects groups

ciscoLwappRrmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 1)
)
ciscoLwappRrmConfigGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersPicoCellMode"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleRxSenseThresholdMin"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleRxSenseThresholdMax"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleRxSenseThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleCcaSenseThresholdMin"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleCcaSenseThresholdMax"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleCcaSenseThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleTransmitPowerLevelMin"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleTransmitPowerLevelMax"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleTransmitPowerLevel"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTupleSetDefault"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmChannelDcaState"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroup.setStatus("deprecated")

ciscoLwappRrmConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 2)
)
ciscoLwappRrmConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersVoicePktCountThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersVoicePktPercentThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersVoiceRssiThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDataPktCountThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDataPktPercentThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDataRssiThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup1.setStatus("current")

ciscoLwappRrmConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 3)
)
ciscoLwappRrmConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmChannelDcaState"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersDcaChannelWidth"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDcaDot11aOutdoorAPDca"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup2.setStatus("deprecated")

ciscoLwappRrmConfigGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 4)
)
ciscoLwappRrmConfigGroupSup3.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersMaxTxPower"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersMinTxPower"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup3.setStatus("current")

ciscoLwappRrmConfigGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 5)
)
ciscoLwappRrmConfigGroupSup4.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpMode"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpRestart"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup4.setStatus("current")

ciscoLwappRrmGrpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 6)
)
ciscoLwappRrmGrpStatusGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderIpAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpRole"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLastUpdateTime"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpInterval"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberIsJoined"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberJoinFailureReason"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderIpv6AddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandGrpLeaderIpv6Address"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmGrpStatusGroup.setStatus("current")

ciscoLwappRrmChannelStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 7)
)
ciscoLwappRrmChannelStatusGroup.setObjects(
    ("CISCO-LWAPP-RRM-MIB", "clrRrmChannelRowStatus")
)
if mibBuilder.loadTexts:
    ciscoLwappRrmChannelStatusGroup.setStatus("current")

ciscoLwappRrmParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 8)
)
ciscoLwappRrmParametersGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersTpcVersion"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersMaxClients"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdNoise"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdInterference"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdLoad"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdSignal"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdDevice"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmParametersGroup.setStatus("current")

ciscoLwappRrmDcaChannelListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 10)
)
ciscoLwappRrmDcaChannelListGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmDcaUsedChannelList"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDcaUnusedChannelList"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDcaDefaultChannelList"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmDcaChannelListGroup.setStatus("current")

ciscoLwappRrmConfigGroupSup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 11)
)
ciscoLwappRrmConfigGroupSup5.setObjects(
    ("CISCO-LWAPP-RRM-MIB", "clrRrmRfGroupingPriority")
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup5.setStatus("current")

ciscoLwappRrmFraConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 12)
)
ciscoLwappRrmFraConfigGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmFraEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmFraInterval"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmFraSensitivity"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmFraSensorThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmFraSensorCoverage"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmFraServicePriority"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmFraSensorDensityOptimisationTargetRssi"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmFraConfigGroup.setStatus("current")

ciscoLwappRrmConfigGroupSup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 13)
)
ciscoLwappRrmConfigGroupSup6.setObjects(
    ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersClientNetworkPreference")
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup6.setStatus("current")

ciscoLwappRrmChdConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 14)
)
ciscoLwappRrmChdConfigGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdNoise"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdInterference"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdLoad"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdSignal"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersChdDevice"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmChdConfigGroup.setStatus("current")

ciscoLwappRrmOptRoamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 15)
)
ciscoLwappRrmOptRoamGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmParametersOptRoamEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersOptRoamDataRate"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersOptRoamInterval"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersRssiCheckEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmParametersRssiThreshold"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmOptRoamGroup.setStatus("current")

ciscoLwappRrmPakRssiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 16)
)
ciscoLwappRrmPakRssiConfigGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmHyperLocationEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmPakRssiThreshold"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmPakRssiThresholdTrigger"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmPakRssiNtpIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmPakRssiNtp"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmPakRssiConfigGroup.setStatus("current")

ciscoLwappRrmNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 17)
)
ciscoLwappRrmNotifyObjectsGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmApTransmitPowerLevel"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTimeStamp"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmClientType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramLength"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMaxIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMinIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramValuesRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApCountRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApMacAddressRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApRssiRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApIfTypeRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddressRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmNotifyObjectsGroup.setStatus("current")

ciscoLwappRrmConfigGroupSup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 18)
)
ciscoLwappRrmConfigGroupSup7.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmChannelDcaState"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDcaDot11aOutdoorAPDca"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup7.setStatus("current")

ciscoLwappRrmConfigGroupSup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 19)
)
ciscoLwappRrmConfigGroupSup8.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmRemovedChannelDcaState"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRemoveChannelRowStatus"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmAddedChannelDcaState"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmAddChannelRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup8.setStatus("current")

ciscoLwappRrmConfigGroupSup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 20)
)
ciscoLwappRrmConfigGroupSup9.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberIsJoined"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandMemberName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberJoinFailureReason"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberIpv6AddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmDot11BandJoinedMemberIpv6Address"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmConfigGroupSup9.setStatus("current")


# Notification objects

ciscoLwappDot11ClientCoverageHolePreAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 1)
)
ciscoLwappDot11ClientCoverageHolePreAlarm.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmApTransmitPowerLevel"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTimeStamp"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmClientType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramLength"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMaxIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMinIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramValues"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApCount"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApRssi"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApIfType"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanChdEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientCoverageHolePreAlarm.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupLeaderChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 2)
)
ciscoLwappRrmRfGroupLeaderChange.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIdentifier"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupLeaderChange.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupMemberAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 3)
)
ciscoLwappRrmRfGroupMemberAdded.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIdentifier"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupMemberAdded.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupMemberRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 4)
)
ciscoLwappRrmRfGroupMemberRemoved.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIdentifier"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupMemberRemoved.setStatus(
        "current"
    )

ciscoLwappDot11ClientCoverageHolePreAlarmRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 5)
)
ciscoLwappDot11ClientCoverageHolePreAlarmRev.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcApMacAddress"),
        ("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmApTransmitPowerLevel"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmTimeStamp"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmClientType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramLength"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMaxIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramMinIndex"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApCountRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApMacAddressRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApRssiRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmNeighborApIfTypeRev"),
        ("CISCO-LWAPP-WLAN-MIB", "cLWlanChdEnable"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmRssiHistogramValuesRev"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11ClientCoverageHolePreAlarmRev.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupLeaderChangeRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 6)
)
ciscoLwappRrmRfGroupLeaderChangeRev.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddressRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupLeaderChangeRev.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupMemberAddedRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 7)
)
ciscoLwappRrmRfGroupMemberAddedRev.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddressRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupMemberAddedRev.setStatus(
        "current"
    )

ciscoLwappRrmRfGroupMemberRemovedRev = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 0, 8)
)
ciscoLwappRrmRfGroupMemberRemovedRev.setObjects(
      *(("CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcIfType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysMacAddressRev"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddressType"),
        ("CISCO-LWAPP-RRM-MIB", "clrRrmSysIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmRfGroupMemberRemovedRev.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappRrmNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 2, 9)
)
ciscoLwappRrmNotifsGroup.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "ciscoLwappDot11ClientCoverageHolePreAlarmRev"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmRfGroupLeaderChangeRev"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmRfGroupMemberAddedRev"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmRfGroupMemberRemovedRev"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappRrmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 1)
)
ciscoLwappRrmMIBCompliance.setObjects(
    ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappRrmMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 2)
)
ciscoLwappRrmMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappRrmMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 3)
)
ciscoLwappRrmMIBComplianceRev2.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup2"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup1"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup3"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup4"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmGrpStatusGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBComplianceRev2.setStatus(
        "current"
    )

ciscoLwappRrmMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 4)
)
ciscoLwappRrmMIBComplianceRev3.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup7"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup1"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup3"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup4"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup5"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmGrpStatusGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmChannelStatusGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmParametersGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmDcaChannelListGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmFraConfigGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup6"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmNotifsGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmNotifyObjectsGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmPakRssiConfigGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmChdConfigGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmOptRoamGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBComplianceRev3.setStatus(
        "current"
    )

ciscoLwappRrmMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 615, 2, 1, 5)
)
ciscoLwappRrmMIBComplianceRev4.setObjects(
      *(("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup8"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup1"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup3"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup4"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmGrpStatusGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmChannelStatusGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmParametersGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmDcaChannelListGroup"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup5"),
        ("CISCO-LWAPP-RRM-MIB", "ciscoLwappRrmConfigGroupSup9"))
)
if mibBuilder.loadTexts:
    ciscoLwappRrmMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-RRM-MIB",
    **{"ClrRrmTupleTuningRange": ClrRrmTupleTuningRange,
       "ciscoLwappRrmMIB": ciscoLwappRrmMIB,
       "ciscoLwappRrmMIBNotifs": ciscoLwappRrmMIBNotifs,
       "ciscoLwappDot11ClientCoverageHolePreAlarm": ciscoLwappDot11ClientCoverageHolePreAlarm,
       "ciscoLwappRrmRfGroupLeaderChange": ciscoLwappRrmRfGroupLeaderChange,
       "ciscoLwappRrmRfGroupMemberAdded": ciscoLwappRrmRfGroupMemberAdded,
       "ciscoLwappRrmRfGroupMemberRemoved": ciscoLwappRrmRfGroupMemberRemoved,
       "ciscoLwappDot11ClientCoverageHolePreAlarmRev": ciscoLwappDot11ClientCoverageHolePreAlarmRev,
       "ciscoLwappRrmRfGroupLeaderChangeRev": ciscoLwappRrmRfGroupLeaderChangeRev,
       "ciscoLwappRrmRfGroupMemberAddedRev": ciscoLwappRrmRfGroupMemberAddedRev,
       "ciscoLwappRrmRfGroupMemberRemovedRev": ciscoLwappRrmRfGroupMemberRemovedRev,
       "ciscoLwappRrmMIBObjects": ciscoLwappRrmMIBObjects,
       "clrRrmConfig": clrRrmConfig,
       "clrRrmParametersTable": clrRrmParametersTable,
       "clrRrmParametersEntry": clrRrmParametersEntry,
       "clrRrmParametersType": clrRrmParametersType,
       "clrRrmParametersPicoCellMode": clrRrmParametersPicoCellMode,
       "clrRrmParametersChdEnable": clrRrmParametersChdEnable,
       "clrRrmParametersVoicePktCountThreshold": clrRrmParametersVoicePktCountThreshold,
       "clrRrmParametersVoicePktPercentThreshold": clrRrmParametersVoicePktPercentThreshold,
       "clrRrmParametersVoiceRssiThreshold": clrRrmParametersVoiceRssiThreshold,
       "clrRrmParametersDataPktCountThreshold": clrRrmParametersDataPktCountThreshold,
       "clrRrmParametersDataPktPercentThreshold": clrRrmParametersDataPktPercentThreshold,
       "clrRrmParametersDataRssiThreshold": clrRrmParametersDataRssiThreshold,
       "clrRrmParametersDcaChannelWidth": clrRrmParametersDcaChannelWidth,
       "clrRrmParametersMaxTxPower": clrRrmParametersMaxTxPower,
       "clrRrmParametersMinTxPower": clrRrmParametersMinTxPower,
       "clrRrmParametersTpcVersion": clrRrmParametersTpcVersion,
       "clrRrmParametersChdNoise": clrRrmParametersChdNoise,
       "clrRrmParametersChdInterference": clrRrmParametersChdInterference,
       "clrRrmParametersChdLoad": clrRrmParametersChdLoad,
       "clrRrmParametersChdSignal": clrRrmParametersChdSignal,
       "clrRrmParametersChdDevice": clrRrmParametersChdDevice,
       "clrRrmParametersMaxClients": clrRrmParametersMaxClients,
       "clrRrmParametersRssiCheckEnable": clrRrmParametersRssiCheckEnable,
       "clrRrmParametersRssiThreshold": clrRrmParametersRssiThreshold,
       "clrRrmParametersOptRoamEnable": clrRrmParametersOptRoamEnable,
       "clrRrmParametersOptRoamDataRate": clrRrmParametersOptRoamDataRate,
       "clrRrmParametersOptRoamInterval": clrRrmParametersOptRoamInterval,
       "clrRrmParametersClientNetworkPreference": clrRrmParametersClientNetworkPreference,
       "clrRrmTupleTable": clrRrmTupleTable,
       "clrRrmTupleEntry": clrRrmTupleEntry,
       "clrRrmTupleRxSenseThresholdMin": clrRrmTupleRxSenseThresholdMin,
       "clrRrmTupleRxSenseThresholdMax": clrRrmTupleRxSenseThresholdMax,
       "clrRrmTupleRxSenseThreshold": clrRrmTupleRxSenseThreshold,
       "clrRrmTupleCcaSenseThresholdMin": clrRrmTupleCcaSenseThresholdMin,
       "clrRrmTupleCcaSenseThresholdMax": clrRrmTupleCcaSenseThresholdMax,
       "clrRrmTupleCcaSenseThreshold": clrRrmTupleCcaSenseThreshold,
       "clrRrmTupleTransmitPowerLevelMin": clrRrmTupleTransmitPowerLevelMin,
       "clrRrmTupleTransmitPowerLevelMax": clrRrmTupleTransmitPowerLevelMax,
       "clrRrmTupleTransmitPowerLevel": clrRrmTupleTransmitPowerLevel,
       "clrRrmTupleSetDefault": clrRrmTupleSetDefault,
       "clrRrmChannelTable": clrRrmChannelTable,
       "clrRrmChannelEntry": clrRrmChannelEntry,
       "clrRrmChannelNum": clrRrmChannelNum,
       "clrRrmChannelDcaState": clrRrmChannelDcaState,
       "clrRrmChannelRowStatus": clrRrmChannelRowStatus,
       "clrRrmDot11BandGrpTable": clrRrmDot11BandGrpTable,
       "clrRrmDot11BandGrpEntry": clrRrmDot11BandGrpEntry,
       "clrRrmDot11BandGrpLeaderIpAddressType": clrRrmDot11BandGrpLeaderIpAddressType,
       "clrRrmDot11BandGrpLeaderIpAddress": clrRrmDot11BandGrpLeaderIpAddress,
       "clrRrmDot11BandGrpLeaderName": clrRrmDot11BandGrpLeaderName,
       "clrRrmDot11BandGrpMode": clrRrmDot11BandGrpMode,
       "clrRrmDot11BandGrpRole": clrRrmDot11BandGrpRole,
       "clrRrmDot11BandGrpRestart": clrRrmDot11BandGrpRestart,
       "clrRrmDot11BandGrpLastUpdateTime": clrRrmDot11BandGrpLastUpdateTime,
       "clrRrmDot11BandGrpInterval": clrRrmDot11BandGrpInterval,
       "clrRrmDot11BandGrpLeaderIpv6AddressType": clrRrmDot11BandGrpLeaderIpv6AddressType,
       "clrRrmDot11BandGrpLeaderIpv6Address": clrRrmDot11BandGrpLeaderIpv6Address,
       "clrRrmDot11BandGrpMemberTable": clrRrmDot11BandGrpMemberTable,
       "clrRrmDot11BandGrpMemberEntry": clrRrmDot11BandGrpMemberEntry,
       "clrRrmDot11BandMemberIpAddressType": clrRrmDot11BandMemberIpAddressType,
       "clrRrmDot11BandMemberIpAddress": clrRrmDot11BandMemberIpAddress,
       "clrRrmDot11BandMemberName": clrRrmDot11BandMemberName,
       "clrRrmDot11BandMemberIsJoined": clrRrmDot11BandMemberIsJoined,
       "clrRrmDot11BandMemberJoinFailureReason": clrRrmDot11BandMemberJoinFailureReason,
       "clrRrmDot11BandMemberRowStatus": clrRrmDot11BandMemberRowStatus,
       "clrRrmDcaConfig": clrRrmDcaConfig,
       "clrRrmDcaDot11aOutdoorAPDca": clrRrmDcaDot11aOutdoorAPDca,
       "clrRrmRfGroupingPriority": clrRrmRfGroupingPriority,
       "clrRrmDcaChannelListTable": clrRrmDcaChannelListTable,
       "clrRrmDcaChannelListEntry": clrRrmDcaChannelListEntry,
       "clrRrmDcaUsedChannelList": clrRrmDcaUsedChannelList,
       "clrRrmDcaUnusedChannelList": clrRrmDcaUnusedChannelList,
       "clrRrmDcaDefaultChannelList": clrRrmDcaDefaultChannelList,
       "clrRrmPakRssiConfig": clrRrmPakRssiConfig,
       "clrRrmHyperLocationEnable": clrRrmHyperLocationEnable,
       "clrRrmPakRssiThreshold": clrRrmPakRssiThreshold,
       "clrRrmPakRssiThresholdTrigger": clrRrmPakRssiThresholdTrigger,
       "clrRrmPakRssiNtpIpAddressType": clrRrmPakRssiNtpIpAddressType,
       "clrRrmPakRssiNtp": clrRrmPakRssiNtp,
       "clrRrmFraConfig": clrRrmFraConfig,
       "clrRrmFraEnable": clrRrmFraEnable,
       "clrRrmFraInterval": clrRrmFraInterval,
       "clrRrmFraSensitivity": clrRrmFraSensitivity,
       "clrRrmFraSensorThreshold": clrRrmFraSensorThreshold,
       "clrRrmFraSensorCoverage": clrRrmFraSensorCoverage,
       "clrRrmFraServicePriority": clrRrmFraServicePriority,
       "clrRrmFraSensorDensityOptimisationTargetRssi": clrRrmFraSensorDensityOptimisationTargetRssi,
       "clrRrm11kConfig": clrRrm11kConfig,
       "clrRrm11kDenialMax": clrRrm11kDenialMax,
       "clrRrm11kFloorBias": clrRrm11kFloorBias,
       "clrRrm11kPredictionMin": clrRrm11kPredictionMin,
       "clrRrmRemoveChannelTable": clrRrmRemoveChannelTable,
       "clrRrmRemoveChannelEntry": clrRrmRemoveChannelEntry,
       "clrRrmRemoveChannelNum": clrRrmRemoveChannelNum,
       "clrRrmRemovedChannelDcaState": clrRrmRemovedChannelDcaState,
       "clrRrmRemoveChannelRowStatus": clrRrmRemoveChannelRowStatus,
       "clrRrmAddChannelTable": clrRrmAddChannelTable,
       "clrRrmAddChannelEntry": clrRrmAddChannelEntry,
       "clrRrmAddChannelNum": clrRrmAddChannelNum,
       "clrRrmAddedChannelDcaState": clrRrmAddedChannelDcaState,
       "clrRrmAddChannelRowStatus": clrRrmAddChannelRowStatus,
       "clrRrmDot11BandJoinedGrpMemberTable": clrRrmDot11BandJoinedGrpMemberTable,
       "clrRrmDot11BandJoinedGrpMemberEntry": clrRrmDot11BandJoinedGrpMemberEntry,
       "clrRrmDot11BandJoinedMemberIpAddressType": clrRrmDot11BandJoinedMemberIpAddressType,
       "clrRrmDot11BandJoinedMemberIpAddress": clrRrmDot11BandJoinedMemberIpAddress,
       "clrRrmDot11BandJoinedMemberName": clrRrmDot11BandJoinedMemberName,
       "clrRrmDot11BandJoinedMemberIsJoined": clrRrmDot11BandJoinedMemberIsJoined,
       "clrRrmDot11BandJoinedMemberJoinFailureReason": clrRrmDot11BandJoinedMemberJoinFailureReason,
       "clrRrmDot11BandJoinedMemberIpv6AddressType": clrRrmDot11BandJoinedMemberIpv6AddressType,
       "clrRrmDot11BandJoinedMemberIpv6Address": clrRrmDot11BandJoinedMemberIpv6Address,
       "clrRrmBcoTable": clrRrmBcoTable,
       "clrRrmBcoEntry": clrRrmBcoEntry,
       "clRrmBcoMode": clRrmBcoMode,
       "clrRrmTriRadioConfig": clrRrmTriRadioConfig,
       "clrRrmTriRadioMode": clrRrmTriRadioMode,
       "clrRrmNotificationVariable": clrRrmNotificationVariable,
       "clrRrmApTransmitPowerLevel": clrRrmApTransmitPowerLevel,
       "clrRrmTimeStamp": clrRrmTimeStamp,
       "clrRrmClientType": clrRrmClientType,
       "clrRrmRssiHistogramLength": clrRrmRssiHistogramLength,
       "clrRrmRssiHistogramMaxIndex": clrRrmRssiHistogramMaxIndex,
       "clrRrmRssiHistogramMinIndex": clrRrmRssiHistogramMinIndex,
       "clrRrmRssiHistogramValues": clrRrmRssiHistogramValues,
       "clrRrmNeighborApCount": clrRrmNeighborApCount,
       "clrRrmNeighborApMacAddress": clrRrmNeighborApMacAddress,
       "clrRrmNeighborApRssi": clrRrmNeighborApRssi,
       "clrRrmNeighborApIfType": clrRrmNeighborApIfType,
       "clrRrmSysMacAddress": clrRrmSysMacAddress,
       "clrRrmSysIdentifier": clrRrmSysIdentifier,
       "clrRrmRssiHistogramValuesRev": clrRrmRssiHistogramValuesRev,
       "clrRrmNeighborApCountRev": clrRrmNeighborApCountRev,
       "clrRrmNeighborApMacAddressRev": clrRrmNeighborApMacAddressRev,
       "clrRrmNeighborApRssiRev": clrRrmNeighborApRssiRev,
       "clrRrmNeighborApIfTypeRev": clrRrmNeighborApIfTypeRev,
       "clrRrmSysMacAddressRev": clrRrmSysMacAddressRev,
       "clrRrmSysIpAddressType": clrRrmSysIpAddressType,
       "clrRrmSysIpAddress": clrRrmSysIpAddress,
       "ciscoLwappRrmMIBConform": ciscoLwappRrmMIBConform,
       "ciscoLwappRrmMIBCompliances": ciscoLwappRrmMIBCompliances,
       "ciscoLwappRrmMIBCompliance": ciscoLwappRrmMIBCompliance,
       "ciscoLwappRrmMIBComplianceRev1": ciscoLwappRrmMIBComplianceRev1,
       "ciscoLwappRrmMIBComplianceRev2": ciscoLwappRrmMIBComplianceRev2,
       "ciscoLwappRrmMIBComplianceRev3": ciscoLwappRrmMIBComplianceRev3,
       "ciscoLwappRrmMIBComplianceRev4": ciscoLwappRrmMIBComplianceRev4,
       "ciscoLwappRrmMIBGroups": ciscoLwappRrmMIBGroups,
       "ciscoLwappRrmConfigGroup": ciscoLwappRrmConfigGroup,
       "ciscoLwappRrmConfigGroupSup1": ciscoLwappRrmConfigGroupSup1,
       "ciscoLwappRrmConfigGroupSup2": ciscoLwappRrmConfigGroupSup2,
       "ciscoLwappRrmConfigGroupSup3": ciscoLwappRrmConfigGroupSup3,
       "ciscoLwappRrmConfigGroupSup4": ciscoLwappRrmConfigGroupSup4,
       "ciscoLwappRrmGrpStatusGroup": ciscoLwappRrmGrpStatusGroup,
       "ciscoLwappRrmChannelStatusGroup": ciscoLwappRrmChannelStatusGroup,
       "ciscoLwappRrmParametersGroup": ciscoLwappRrmParametersGroup,
       "ciscoLwappRrmNotifsGroup": ciscoLwappRrmNotifsGroup,
       "ciscoLwappRrmDcaChannelListGroup": ciscoLwappRrmDcaChannelListGroup,
       "ciscoLwappRrmConfigGroupSup5": ciscoLwappRrmConfigGroupSup5,
       "ciscoLwappRrmFraConfigGroup": ciscoLwappRrmFraConfigGroup,
       "ciscoLwappRrmConfigGroupSup6": ciscoLwappRrmConfigGroupSup6,
       "ciscoLwappRrmChdConfigGroup": ciscoLwappRrmChdConfigGroup,
       "ciscoLwappRrmOptRoamGroup": ciscoLwappRrmOptRoamGroup,
       "ciscoLwappRrmPakRssiConfigGroup": ciscoLwappRrmPakRssiConfigGroup,
       "ciscoLwappRrmNotifyObjectsGroup": ciscoLwappRrmNotifyObjectsGroup,
       "ciscoLwappRrmConfigGroupSup7": ciscoLwappRrmConfigGroupSup7,
       "ciscoLwappRrmConfigGroupSup8": ciscoLwappRrmConfigGroupSup8,
       "ciscoLwappRrmConfigGroupSup9": ciscoLwappRrmConfigGroupSup9}
)
