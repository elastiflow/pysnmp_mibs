# SNMP MIB module (CISCO-LWAPP-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-DOT11-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:04 2025
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

(cLApDot11IfSlotId,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApDot11IfSlotId",
    "cLApSysMacAddress")

(CLDot11Band,
 CLDot11ChannelBandwidth) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Band",
    "CLDot11ChannelBandwidth")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIB.setRevisions(
        ("2023-05-30 00:00",
         "2021-04-16 00:00",
         "2021-01-11 00:00",
         "2020-09-02 00:00",
         "2020-08-07 00:00",
         "2019-06-28 00:00",
         "2019-02-13 00:00",
         "2017-05-22 00:00",
         "2010-05-06 00:00",
         "2018-03-28 00:00",
         "2018-03-28 00:00",
         "2007-01-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBNotifs = _CiscoLwappDot11MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 0)
)
_CiscoLwappDot11MIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBObjects = _CiscoLwappDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1)
)
_CldConfig_ObjectIdentity = ObjectIdentity
cldConfig = _CldConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1)
)
_CldHtMacOperationsTable_Object = MibTable
cldHtMacOperationsTable = _CldHtMacOperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldHtMacOperationsTable.setStatus("current")
_CldHtMacOperationsEntry_Object = MibTableRow
cldHtMacOperationsEntry = _CldHtMacOperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1)
)
cldHtMacOperationsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldHtDot11nBand"),
)
if mibBuilder.loadTexts:
    cldHtMacOperationsEntry.setStatus("current")
_CldHtDot11nBand_Type = CLDot11Band
_CldHtDot11nBand_Object = MibTableColumn
cldHtDot11nBand = _CldHtDot11nBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 1),
    _CldHtDot11nBand_Type()
)
cldHtDot11nBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldHtDot11nBand.setStatus("current")


class _CldHtDot11nChannelBandwidth_Type(CLDot11ChannelBandwidth):
    """Custom type cldHtDot11nChannelBandwidth based on CLDot11ChannelBandwidth"""
    defaultValue = 3


_CldHtDot11nChannelBandwidth_Type.__name__ = "CLDot11ChannelBandwidth"
_CldHtDot11nChannelBandwidth_Object = MibTableColumn
cldHtDot11nChannelBandwidth = _CldHtDot11nChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 2),
    _CldHtDot11nChannelBandwidth_Type()
)
cldHtDot11nChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nChannelBandwidth.setStatus("current")


class _CldHtDot11nRifsEnable_Type(TruthValue):
    """Custom type cldHtDot11nRifsEnable based on TruthValue"""
    defaultValue = 1


_CldHtDot11nRifsEnable_Type.__name__ = "TruthValue"
_CldHtDot11nRifsEnable_Object = MibTableColumn
cldHtDot11nRifsEnable = _CldHtDot11nRifsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 3),
    _CldHtDot11nRifsEnable_Type()
)
cldHtDot11nRifsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nRifsEnable.setStatus("current")


class _CldHtDot11nAmsduEnable_Type(TruthValue):
    """Custom type cldHtDot11nAmsduEnable based on TruthValue"""
    defaultValue = 1


_CldHtDot11nAmsduEnable_Type.__name__ = "TruthValue"
_CldHtDot11nAmsduEnable_Object = MibTableColumn
cldHtDot11nAmsduEnable = _CldHtDot11nAmsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 4),
    _CldHtDot11nAmsduEnable_Type()
)
cldHtDot11nAmsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nAmsduEnable.setStatus("current")


class _CldHtDot11nAmpduEnable_Type(TruthValue):
    """Custom type cldHtDot11nAmpduEnable based on TruthValue"""
    defaultValue = 1


_CldHtDot11nAmpduEnable_Type.__name__ = "TruthValue"
_CldHtDot11nAmpduEnable_Object = MibTableColumn
cldHtDot11nAmpduEnable = _CldHtDot11nAmpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 5),
    _CldHtDot11nAmpduEnable_Type()
)
cldHtDot11nAmpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nAmpduEnable.setStatus("current")


class _CldHtDot11nGuardIntervalEnable_Type(TruthValue):
    """Custom type cldHtDot11nGuardIntervalEnable based on TruthValue"""
    defaultValue = 1


_CldHtDot11nGuardIntervalEnable_Type.__name__ = "TruthValue"
_CldHtDot11nGuardIntervalEnable_Object = MibTableColumn
cldHtDot11nGuardIntervalEnable = _CldHtDot11nGuardIntervalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 6),
    _CldHtDot11nGuardIntervalEnable_Type()
)
cldHtDot11nGuardIntervalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nGuardIntervalEnable.setStatus("current")


class _CldHtDot11nEnable_Type(TruthValue):
    """Custom type cldHtDot11nEnable based on TruthValue"""
    defaultValue = 1


_CldHtDot11nEnable_Type.__name__ = "TruthValue"
_CldHtDot11nEnable_Object = MibTableColumn
cldHtDot11nEnable = _CldHtDot11nEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 7),
    _CldHtDot11nEnable_Type()
)
cldHtDot11nEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nEnable.setStatus("current")


class _CldMultipleCountryCode_Type(SnmpAdminString):
    """Custom type cldMultipleCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 600),
    )


_CldMultipleCountryCode_Type.__name__ = "SnmpAdminString"
_CldMultipleCountryCode_Object = MibScalar
cldMultipleCountryCode = _CldMultipleCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 2),
    _CldMultipleCountryCode_Type()
)
cldMultipleCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldMultipleCountryCode.setStatus("current")


class _CldRegulatoryDomain_Type(SnmpAdminString):
    """Custom type cldRegulatoryDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CldRegulatoryDomain_Type.__name__ = "SnmpAdminString"
_CldRegulatoryDomain_Object = MibScalar
cldRegulatoryDomain = _CldRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 3),
    _CldRegulatoryDomain_Type()
)
cldRegulatoryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRegulatoryDomain.setStatus("current")
_Cld11nMcsTable_Object = MibTable
cld11nMcsTable = _Cld11nMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cld11nMcsTable.setStatus("current")
_Cld11nMcsEntry_Object = MibTableRow
cld11nMcsEntry = _Cld11nMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1)
)
cld11nMcsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11nMcsBand"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11nMcsDataRateIndex"),
)
if mibBuilder.loadTexts:
    cld11nMcsEntry.setStatus("current")
_Cld11nMcsBand_Type = CLDot11Band
_Cld11nMcsBand_Object = MibTableColumn
cld11nMcsBand = _Cld11nMcsBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 1),
    _Cld11nMcsBand_Type()
)
cld11nMcsBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11nMcsBand.setStatus("current")
_Cld11nMcsDataRateIndex_Type = Unsigned32
_Cld11nMcsDataRateIndex_Object = MibTableColumn
cld11nMcsDataRateIndex = _Cld11nMcsDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 2),
    _Cld11nMcsDataRateIndex_Type()
)
cld11nMcsDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11nMcsDataRateIndex.setStatus("current")
_Cld11nMcsDataRate_Type = Unsigned32
_Cld11nMcsDataRate_Object = MibTableColumn
cld11nMcsDataRate = _Cld11nMcsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 3),
    _Cld11nMcsDataRate_Type()
)
cld11nMcsDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsDataRate.setStatus("current")


class _Cld11nMcsSupportEnable_Type(TruthValue):
    """Custom type cld11nMcsSupportEnable based on TruthValue"""
    defaultValue = 1


_Cld11nMcsSupportEnable_Type.__name__ = "TruthValue"
_Cld11nMcsSupportEnable_Object = MibTableColumn
cld11nMcsSupportEnable = _Cld11nMcsSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 4),
    _Cld11nMcsSupportEnable_Type()
)
cld11nMcsSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11nMcsSupportEnable.setStatus("current")
_Cld11nMcsChannelWidth_Type = Unsigned32
_Cld11nMcsChannelWidth_Object = MibTableColumn
cld11nMcsChannelWidth = _Cld11nMcsChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 5),
    _Cld11nMcsChannelWidth_Type()
)
cld11nMcsChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cld11nMcsChannelWidth.setUnits("MHz")
_Cld11nMcsGuardInterval_Type = Unsigned32
_Cld11nMcsGuardInterval_Object = MibTableColumn
cld11nMcsGuardInterval = _Cld11nMcsGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 6),
    _Cld11nMcsGuardInterval_Type()
)
cld11nMcsGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsGuardInterval.setStatus("current")
if mibBuilder.loadTexts:
    cld11nMcsGuardInterval.setUnits("ns")


class _Cld11nMcsModulation_Type(OctetString):
    """Custom type cld11nMcsModulation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cld11nMcsModulation_Type.__name__ = "OctetString"
_Cld11nMcsModulation_Object = MibTableColumn
cld11nMcsModulation = _Cld11nMcsModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 7),
    _Cld11nMcsModulation_Type()
)
cld11nMcsModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsModulation.setStatus("current")
_Cld11acConfig_ObjectIdentity = ObjectIdentity
cld11acConfig = _Cld11acConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 5)
)


class _CldVhtDot11acEnable_Type(TruthValue):
    """Custom type cldVhtDot11acEnable based on TruthValue"""
    defaultValue = 1


_CldVhtDot11acEnable_Type.__name__ = "TruthValue"
_CldVhtDot11acEnable_Object = MibScalar
cldVhtDot11acEnable = _CldVhtDot11acEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 5, 1),
    _CldVhtDot11acEnable_Type()
)
cldVhtDot11acEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldVhtDot11acEnable.setStatus("current")
_Cld11acMcsTable_Object = MibTable
cld11acMcsTable = _Cld11acMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cld11acMcsTable.setStatus("current")
_Cld11acMcsEntry_Object = MibTableRow
cld11acMcsEntry = _Cld11acMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1)
)
cld11acMcsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11acMcsSpatialStreamIndex"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11acMcsDataRateIndex"),
)
if mibBuilder.loadTexts:
    cld11acMcsEntry.setStatus("current")
_Cld11acMcsSpatialStreamIndex_Type = Unsigned32
_Cld11acMcsSpatialStreamIndex_Object = MibTableColumn
cld11acMcsSpatialStreamIndex = _Cld11acMcsSpatialStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1, 1),
    _Cld11acMcsSpatialStreamIndex_Type()
)
cld11acMcsSpatialStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11acMcsSpatialStreamIndex.setStatus("current")
_Cld11acMcsDataRateIndex_Type = Unsigned32
_Cld11acMcsDataRateIndex_Object = MibTableColumn
cld11acMcsDataRateIndex = _Cld11acMcsDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1, 2),
    _Cld11acMcsDataRateIndex_Type()
)
cld11acMcsDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11acMcsDataRateIndex.setStatus("current")


class _Cld11acMcsSupportEnable_Type(TruthValue):
    """Custom type cld11acMcsSupportEnable based on TruthValue"""
    defaultValue = 1


_Cld11acMcsSupportEnable_Type.__name__ = "TruthValue"
_Cld11acMcsSupportEnable_Object = MibTableColumn
cld11acMcsSupportEnable = _Cld11acMcsSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1, 3),
    _Cld11acMcsSupportEnable_Type()
)
cld11acMcsSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11acMcsSupportEnable.setStatus("current")


class _CldCountryChangeNotifEnable_Type(TruthValue):
    """Custom type cldCountryChangeNotifEnable based on TruthValue"""
    defaultValue = 1


_CldCountryChangeNotifEnable_Type.__name__ = "TruthValue"
_CldCountryChangeNotifEnable_Object = MibScalar
cldCountryChangeNotifEnable = _CldCountryChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 7),
    _CldCountryChangeNotifEnable_Type()
)
cldCountryChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldCountryChangeNotifEnable.setStatus("current")
_CldLoadBalancing_ObjectIdentity = ObjectIdentity
cldLoadBalancing = _CldLoadBalancing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8)
)


class _CldLoadBalancingEnable_Type(Integer32):
    """Custom type cldLoadBalancingEnable based on Integer32"""
    defaultValue = 1

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


_CldLoadBalancingEnable_Type.__name__ = "Integer32"
_CldLoadBalancingEnable_Object = MibScalar
cldLoadBalancingEnable = _CldLoadBalancingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 1),
    _CldLoadBalancingEnable_Type()
)
cldLoadBalancingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldLoadBalancingEnable.setStatus("current")


class _CldLoadBalancingWindowSize_Type(Integer32):
    """Custom type cldLoadBalancingWindowSize based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CldLoadBalancingWindowSize_Type.__name__ = "Integer32"
_CldLoadBalancingWindowSize_Object = MibScalar
cldLoadBalancingWindowSize = _CldLoadBalancingWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 2),
    _CldLoadBalancingWindowSize_Type()
)
cldLoadBalancingWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingWindowSize.setStatus("current")


class _CldLoadBalancingDenialCount_Type(Integer32):
    """Custom type cldLoadBalancingDenialCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CldLoadBalancingDenialCount_Type.__name__ = "Integer32"
_CldLoadBalancingDenialCount_Object = MibScalar
cldLoadBalancingDenialCount = _CldLoadBalancingDenialCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 3),
    _CldLoadBalancingDenialCount_Type()
)
cldLoadBalancingDenialCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingDenialCount.setStatus("current")


class _CldLoadBalancingTrafficThreshold_Type(Unsigned32):
    """Custom type cldLoadBalancingTrafficThreshold based on Unsigned32"""
    defaultValue = 50


_CldLoadBalancingTrafficThreshold_Type.__name__ = "Unsigned32"
_CldLoadBalancingTrafficThreshold_Object = MibScalar
cldLoadBalancingTrafficThreshold = _CldLoadBalancingTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 4),
    _CldLoadBalancingTrafficThreshold_Type()
)
cldLoadBalancingTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingTrafficThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cldLoadBalancingTrafficThreshold.setUnits("Percent")


class _CldLoadBalancingDot11aWindowSize_Type(Integer32):
    """Custom type cldLoadBalancingDot11aWindowSize based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CldLoadBalancingDot11aWindowSize_Type.__name__ = "Integer32"
_CldLoadBalancingDot11aWindowSize_Object = MibScalar
cldLoadBalancingDot11aWindowSize = _CldLoadBalancingDot11aWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 5),
    _CldLoadBalancingDot11aWindowSize_Type()
)
cldLoadBalancingDot11aWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingDot11aWindowSize.setStatus("current")


class _CldLoadBalancingDot11aDenialCount_Type(Integer32):
    """Custom type cldLoadBalancingDot11aDenialCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CldLoadBalancingDot11aDenialCount_Type.__name__ = "Integer32"
_CldLoadBalancingDot11aDenialCount_Object = MibScalar
cldLoadBalancingDot11aDenialCount = _CldLoadBalancingDot11aDenialCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 6),
    _CldLoadBalancingDot11aDenialCount_Type()
)
cldLoadBalancingDot11aDenialCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingDot11aDenialCount.setStatus("current")


class _CldLoadBalancingDot11bWindowSize_Type(Integer32):
    """Custom type cldLoadBalancingDot11bWindowSize based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CldLoadBalancingDot11bWindowSize_Type.__name__ = "Integer32"
_CldLoadBalancingDot11bWindowSize_Object = MibScalar
cldLoadBalancingDot11bWindowSize = _CldLoadBalancingDot11bWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 7),
    _CldLoadBalancingDot11bWindowSize_Type()
)
cldLoadBalancingDot11bWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingDot11bWindowSize.setStatus("current")


class _CldLoadBalancingDot11bDenialCount_Type(Integer32):
    """Custom type cldLoadBalancingDot11bDenialCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CldLoadBalancingDot11bDenialCount_Type.__name__ = "Integer32"
_CldLoadBalancingDot11bDenialCount_Object = MibScalar
cldLoadBalancingDot11bDenialCount = _CldLoadBalancingDot11bDenialCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 8),
    _CldLoadBalancingDot11bDenialCount_Type()
)
cldLoadBalancingDot11bDenialCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingDot11bDenialCount.setStatus("current")
_CldBandSelect_ObjectIdentity = ObjectIdentity
cldBandSelect = _CldBandSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9)
)


class _CldBandSelectEnable_Type(Integer32):
    """Custom type cldBandSelectEnable based on Integer32"""
    defaultValue = 1

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


_CldBandSelectEnable_Type.__name__ = "Integer32"
_CldBandSelectEnable_Object = MibScalar
cldBandSelectEnable = _CldBandSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 1),
    _CldBandSelectEnable_Type()
)
cldBandSelectEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldBandSelectEnable.setStatus("current")


class _CldBandSelectCycleCount_Type(Integer32):
    """Custom type cldBandSelectCycleCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CldBandSelectCycleCount_Type.__name__ = "Integer32"
_CldBandSelectCycleCount_Object = MibScalar
cldBandSelectCycleCount = _CldBandSelectCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 2),
    _CldBandSelectCycleCount_Type()
)
cldBandSelectCycleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectCycleCount.setStatus("current")


class _CldBandSelectCycleThreshold_Type(Integer32):
    """Custom type cldBandSelectCycleThreshold based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CldBandSelectCycleThreshold_Type.__name__ = "Integer32"
_CldBandSelectCycleThreshold_Object = MibScalar
cldBandSelectCycleThreshold = _CldBandSelectCycleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 3),
    _CldBandSelectCycleThreshold_Type()
)
cldBandSelectCycleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectCycleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectCycleThreshold.setUnits("milliseconds")


class _CldBandSelectAgeOutSuppression_Type(Integer32):
    """Custom type cldBandSelectAgeOutSuppression based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_CldBandSelectAgeOutSuppression_Type.__name__ = "Integer32"
_CldBandSelectAgeOutSuppression_Object = MibScalar
cldBandSelectAgeOutSuppression = _CldBandSelectAgeOutSuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 4),
    _CldBandSelectAgeOutSuppression_Type()
)
cldBandSelectAgeOutSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutSuppression.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutSuppression.setUnits("seconds")


class _CldBandSelectAgeOutDualBand_Type(Integer32):
    """Custom type cldBandSelectAgeOutDualBand based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CldBandSelectAgeOutDualBand_Type.__name__ = "Integer32"
_CldBandSelectAgeOutDualBand_Object = MibScalar
cldBandSelectAgeOutDualBand = _CldBandSelectAgeOutDualBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 5),
    _CldBandSelectAgeOutDualBand_Type()
)
cldBandSelectAgeOutDualBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutDualBand.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutDualBand.setUnits("seconds")


class _CldBandSelectClientRssi_Type(Integer32):
    """Custom type cldBandSelectClientRssi based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -20),
    )


_CldBandSelectClientRssi_Type.__name__ = "Integer32"
_CldBandSelectClientRssi_Object = MibScalar
cldBandSelectClientRssi = _CldBandSelectClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 6),
    _CldBandSelectClientRssi_Type()
)
cldBandSelectClientRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectClientRssi.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectClientRssi.setUnits("dBm")


class _CldBandSelectClientMidRssi_Type(Integer32):
    """Custom type cldBandSelectClientMidRssi based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -20),
    )


_CldBandSelectClientMidRssi_Type.__name__ = "Integer32"
_CldBandSelectClientMidRssi_Object = MibScalar
cldBandSelectClientMidRssi = _CldBandSelectClientMidRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 7),
    _CldBandSelectClientMidRssi_Type()
)
cldBandSelectClientMidRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectClientMidRssi.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectClientMidRssi.setUnits("dBm")
_Cld11axConfigTable_Object = MibTable
cld11axConfigTable = _Cld11axConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cld11axConfigTable.setStatus("current")
_Cld11axConfigEntry_Object = MibTableRow
cld11axConfigEntry = _Cld11axConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 10, 1)
)
cld11axConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldDot11axBandId"),
)
if mibBuilder.loadTexts:
    cld11axConfigEntry.setStatus("current")
_CldDot11axBandId_Type = CLDot11Band
_CldDot11axBandId_Object = MibTableColumn
cldDot11axBandId = _CldDot11axBandId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 10, 1, 1),
    _CldDot11axBandId_Type()
)
cldDot11axBandId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldDot11axBandId.setStatus("current")


class _CldDot11axEnable_Type(TruthValue):
    """Custom type cldDot11axEnable based on TruthValue"""
    defaultValue = 1


_CldDot11axEnable_Type.__name__ = "TruthValue"
_CldDot11axEnable_Object = MibTableColumn
cldDot11axEnable = _CldDot11axEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 10, 1, 2),
    _CldDot11axEnable_Type()
)
cldDot11axEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot11axEnable.setStatus("current")
_Cld11axMcsTable_Object = MibTable
cld11axMcsTable = _Cld11axMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cld11axMcsTable.setStatus("current")
_Cld11axMcsEntry_Object = MibTableRow
cld11axMcsEntry = _Cld11axMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 11, 1)
)
cld11axMcsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldDot11axBand"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11axMcsSpatialStreamIndex"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11axMcsDataRateIndex"),
)
if mibBuilder.loadTexts:
    cld11axMcsEntry.setStatus("current")
_CldDot11axBand_Type = CLDot11Band
_CldDot11axBand_Object = MibTableColumn
cldDot11axBand = _CldDot11axBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 11, 1, 1),
    _CldDot11axBand_Type()
)
cldDot11axBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldDot11axBand.setStatus("current")
_Cld11axMcsSpatialStreamIndex_Type = Unsigned32
_Cld11axMcsSpatialStreamIndex_Object = MibTableColumn
cld11axMcsSpatialStreamIndex = _Cld11axMcsSpatialStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 11, 1, 2),
    _Cld11axMcsSpatialStreamIndex_Type()
)
cld11axMcsSpatialStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11axMcsSpatialStreamIndex.setStatus("current")
_Cld11axMcsDataRateIndex_Type = Unsigned32
_Cld11axMcsDataRateIndex_Object = MibTableColumn
cld11axMcsDataRateIndex = _Cld11axMcsDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 11, 1, 3),
    _Cld11axMcsDataRateIndex_Type()
)
cld11axMcsDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11axMcsDataRateIndex.setStatus("current")


class _Cld11axMcsSupportEnable_Type(TruthValue):
    """Custom type cld11axMcsSupportEnable based on TruthValue"""
    defaultValue = 1


_Cld11axMcsSupportEnable_Type.__name__ = "TruthValue"
_Cld11axMcsSupportEnable_Object = MibTableColumn
cld11axMcsSupportEnable = _Cld11axMcsSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 11, 1, 4),
    _Cld11axMcsSupportEnable_Type()
)
cld11axMcsSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axMcsSupportEnable.setStatus("current")
_CldDot11axHeCapTable_Object = MibTable
cldDot11axHeCapTable = _CldDot11axHeCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cldDot11axHeCapTable.setStatus("current")
_CldDot11axHeCapEntry_Object = MibTableRow
cldDot11axHeCapEntry = _CldDot11axHeCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1)
)
cldDot11axHeCapEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cldDot11axHeCapEntry.setStatus("current")
_CldDot11IsHeCapable_Type = TruthValue
_CldDot11IsHeCapable_Object = MibTableColumn
cldDot11IsHeCapable = _CldDot11IsHeCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 1),
    _CldDot11IsHeCapable_Type()
)
cldDot11IsHeCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11IsHeCapable.setStatus("current")
_CldDot11IsHeEnable_Type = TruthValue
_CldDot11IsHeEnable_Object = MibTableColumn
cldDot11IsHeEnable = _CldDot11IsHeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 2),
    _CldDot11IsHeEnable_Type()
)
cldDot11IsHeEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11IsHeEnable.setStatus("current")
_CldDot11HeSuBF_Type = Unsigned32
_CldDot11HeSuBF_Object = MibTableColumn
cldDot11HeSuBF = _CldDot11HeSuBF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 3),
    _CldDot11HeSuBF_Type()
)
cldDot11HeSuBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11HeSuBF.setStatus("current")
_CldDot11HeMuBF_Type = Unsigned32
_CldDot11HeMuBF_Object = MibTableColumn
cldDot11HeMuBF = _CldDot11HeMuBF_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 4),
    _CldDot11HeMuBF_Type()
)
cldDot11HeMuBF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11HeMuBF.setStatus("current")
_CldDot11HeStbcMode_Type = Unsigned32
_CldDot11HeStbcMode_Object = MibTableColumn
cldDot11HeStbcMode = _CldDot11HeStbcMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 5),
    _CldDot11HeStbcMode_Type()
)
cldDot11HeStbcMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11HeStbcMode.setStatus("current")
_CldDot11HeAmpduTidBmap_Type = Unsigned32
_CldDot11HeAmpduTidBmap_Object = MibTableColumn
cldDot11HeAmpduTidBmap = _CldDot11HeAmpduTidBmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 6),
    _CldDot11HeAmpduTidBmap_Type()
)
cldDot11HeAmpduTidBmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11HeAmpduTidBmap.setStatus("current")
_CldDot11HeCapTxRxMcsNss_Type = Unsigned32
_CldDot11HeCapTxRxMcsNss_Object = MibTableColumn
cldDot11HeCapTxRxMcsNss = _CldDot11HeCapTxRxMcsNss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 12, 1, 7),
    _CldDot11HeCapTxRxMcsNss_Type()
)
cldDot11HeCapTxRxMcsNss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot11HeCapTxRxMcsNss.setStatus("current")
_Cld11axMbssidTable_Object = MibTable
cld11axMbssidTable = _Cld11axMbssidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cld11axMbssidTable.setStatus("current")
_Cld11axMbssidEntry_Object = MibTableRow
cld11axMbssidEntry = _Cld11axMbssidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 13, 1)
)
cld11axMbssidEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldBand"),
)
if mibBuilder.loadTexts:
    cld11axMbssidEntry.setStatus("current")
_CldBand_Type = CLDot11Band
_CldBand_Object = MibTableColumn
cldBand = _CldBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 13, 1, 1),
    _CldBand_Type()
)
cldBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldBand.setStatus("current")
_Cld11axMbssidCap_Type = TruthValue
_Cld11axMbssidCap_Object = MibTableColumn
cld11axMbssidCap = _Cld11axMbssidCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 13, 1, 2),
    _Cld11axMbssidCap_Type()
)
cld11axMbssidCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axMbssidCap.setStatus("current")
_CldDot11RxsopThreshold_ObjectIdentity = ObjectIdentity
cldDot11RxsopThreshold = _CldDot11RxsopThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 14)
)


class _CldDot11bRxSopThresholdCustom_Type(Integer32):
    """Custom type cldDot11bRxSopThresholdCustom based on Integer32"""
    defaultValue = -85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-85, -60),
    )


_CldDot11bRxSopThresholdCustom_Type.__name__ = "Integer32"
_CldDot11bRxSopThresholdCustom_Object = MibScalar
cldDot11bRxSopThresholdCustom = _CldDot11bRxSopThresholdCustom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 14, 1),
    _CldDot11bRxSopThresholdCustom_Type()
)
cldDot11bRxSopThresholdCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot11bRxSopThresholdCustom.setStatus("current")


class _CldDot11aRxSopThresholdCustom_Type(Integer32):
    """Custom type cldDot11aRxSopThresholdCustom based on Integer32"""
    defaultValue = -85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-85, -60),
    )


_CldDot11aRxSopThresholdCustom_Type.__name__ = "Integer32"
_CldDot11aRxSopThresholdCustom_Object = MibScalar
cldDot11aRxSopThresholdCustom = _CldDot11aRxSopThresholdCustom_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 14, 2),
    _CldDot11aRxSopThresholdCustom_Type()
)
cldDot11aRxSopThresholdCustom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot11aRxSopThresholdCustom.setStatus("current")
_Cld11axTargetWakeupTimeTable_Object = MibTable
cld11axTargetWakeupTimeTable = _Cld11axTargetWakeupTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cld11axTargetWakeupTimeTable.setStatus("current")
_Cld11axTargetWakeupTimeEntry_Object = MibTableRow
cld11axTargetWakeupTimeEntry = _Cld11axTargetWakeupTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 15, 1)
)
cld11axTargetWakeupTimeEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldBand"),
)
if mibBuilder.loadTexts:
    cld11axTargetWakeupTimeEntry.setStatus("current")


class _Cld11axTargetWakeupTimeEnable_Type(TruthValue):
    """Custom type cld11axTargetWakeupTimeEnable based on TruthValue"""
    defaultValue = 1


_Cld11axTargetWakeupTimeEnable_Type.__name__ = "TruthValue"
_Cld11axTargetWakeupTimeEnable_Object = MibTableColumn
cld11axTargetWakeupTimeEnable = _Cld11axTargetWakeupTimeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 15, 1, 1),
    _Cld11axTargetWakeupTimeEnable_Type()
)
cld11axTargetWakeupTimeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axTargetWakeupTimeEnable.setStatus("current")
_Cld11axTargetWakeupTimeBroadcastTable_Object = MibTable
cld11axTargetWakeupTimeBroadcastTable = _Cld11axTargetWakeupTimeBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cld11axTargetWakeupTimeBroadcastTable.setStatus("current")
_Cld11axTargetWakeupTimeBroadcastEntry_Object = MibTableRow
cld11axTargetWakeupTimeBroadcastEntry = _Cld11axTargetWakeupTimeBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 16, 1)
)
cld11axTargetWakeupTimeBroadcastEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldBand"),
)
if mibBuilder.loadTexts:
    cld11axTargetWakeupTimeBroadcastEntry.setStatus("current")


class _Cld11axTargetWakeupTimeBroadcastEnable_Type(TruthValue):
    """Custom type cld11axTargetWakeupTimeBroadcastEnable based on TruthValue"""
    defaultValue = 1


_Cld11axTargetWakeupTimeBroadcastEnable_Type.__name__ = "TruthValue"
_Cld11axTargetWakeupTimeBroadcastEnable_Object = MibTableColumn
cld11axTargetWakeupTimeBroadcastEnable = _Cld11axTargetWakeupTimeBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 16, 1, 1),
    _Cld11axTargetWakeupTimeBroadcastEnable_Type()
)
cld11axTargetWakeupTimeBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axTargetWakeupTimeBroadcastEnable.setStatus("current")
_Cld11axBssColorConfigTable_Object = MibTable
cld11axBssColorConfigTable = _Cld11axBssColorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cld11axBssColorConfigTable.setStatus("current")
_Cld11axBssColorConfigEntry_Object = MibTableRow
cld11axBssColorConfigEntry = _Cld11axBssColorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 17, 1)
)
cld11axBssColorConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldBand"),
)
if mibBuilder.loadTexts:
    cld11axBssColorConfigEntry.setStatus("current")
_Cld11axBssColorState_Type = TruthValue
_Cld11axBssColorState_Object = MibTableColumn
cld11axBssColorState = _Cld11axBssColorState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 17, 1, 1),
    _Cld11axBssColorState_Type()
)
cld11axBssColorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axBssColorState.setStatus("current")
_Cld11axBssColorRadioTable_Object = MibTable
cld11axBssColorRadioTable = _Cld11axBssColorRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cld11axBssColorRadioTable.setStatus("current")
_Cld11axBssColorRadioEntry_Object = MibTableRow
cld11axBssColorRadioEntry = _Cld11axBssColorRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 18, 1)
)
cld11axBssColorRadioEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-AP-MIB", "cLApDot11IfSlotId"),
)
if mibBuilder.loadTexts:
    cld11axBssColorRadioEntry.setStatus("current")
_Cld11axIsBssColorCapable_Type = TruthValue
_Cld11axIsBssColorCapable_Object = MibTableColumn
cld11axIsBssColorCapable = _Cld11axIsBssColorCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 18, 1, 1),
    _Cld11axIsBssColorCapable_Type()
)
cld11axIsBssColorCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11axIsBssColorCapable.setStatus("current")


class _Cld11axBssColor_Type(Integer32):
    """Custom type cld11axBssColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Cld11axBssColor_Type.__name__ = "Integer32"
_Cld11axBssColor_Object = MibTableColumn
cld11axBssColor = _Cld11axBssColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 18, 1, 2),
    _Cld11axBssColor_Type()
)
cld11axBssColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axBssColor.setStatus("current")


class _Cld11axBssColorConfigType_Type(Integer32):
    """Custom type cld11axBssColorConfigType based on Integer32"""
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


_Cld11axBssColorConfigType_Type.__name__ = "Integer32"
_Cld11axBssColorConfigType_Object = MibTableColumn
cld11axBssColorConfigType = _Cld11axBssColorConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 18, 1, 3),
    _Cld11axBssColorConfigType_Type()
)
cld11axBssColorConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axBssColorConfigType.setStatus("current")
_CldConfiguredCountryTable_Object = MibTable
cldConfiguredCountryTable = _CldConfiguredCountryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cldConfiguredCountryTable.setStatus("current")
_CldConfiguredCountryEntry_Object = MibTableRow
cldConfiguredCountryEntry = _CldConfiguredCountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 19, 1)
)
cldConfiguredCountryEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldConfiguredCountryCode"),
)
if mibBuilder.loadTexts:
    cldConfiguredCountryEntry.setStatus("current")


class _CldConfiguredCountryCode_Type(Unsigned32):
    """Custom type cldConfiguredCountryCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 252),
    )


_CldConfiguredCountryCode_Type.__name__ = "Unsigned32"
_CldConfiguredCountryCode_Object = MibTableColumn
cldConfiguredCountryCode = _CldConfiguredCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 19, 1, 1),
    _CldConfiguredCountryCode_Type()
)
cldConfiguredCountryCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldConfiguredCountryCode.setStatus("current")
_CldConfiguredCountryRowStatus_Type = RowStatus
_CldConfiguredCountryRowStatus_Object = MibTableColumn
cldConfiguredCountryRowStatus = _CldConfiguredCountryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 19, 1, 2),
    _CldConfiguredCountryRowStatus_Type()
)
cldConfiguredCountryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldConfiguredCountryRowStatus.setStatus("current")
_Cld11axObssPdConfigTable_Object = MibTable
cld11axObssPdConfigTable = _Cld11axObssPdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cld11axObssPdConfigTable.setStatus("current")
_Cld11axObssPdConfigEntry_Object = MibTableRow
cld11axObssPdConfigEntry = _Cld11axObssPdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20, 1)
)
cld11axObssPdConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldBand"),
)
if mibBuilder.loadTexts:
    cld11axObssPdConfigEntry.setStatus("current")


class _Cld11axObssPdEnable_Type(TruthValue):
    """Custom type cld11axObssPdEnable based on TruthValue"""
    defaultValue = 2


_Cld11axObssPdEnable_Type.__name__ = "TruthValue"
_Cld11axObssPdEnable_Object = MibTableColumn
cld11axObssPdEnable = _Cld11axObssPdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20, 1, 1),
    _Cld11axObssPdEnable_Type()
)
cld11axObssPdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axObssPdEnable.setStatus("current")


class _Cld11axNonSrgObssPdMax_Type(Integer32):
    """Custom type cld11axNonSrgObssPdMax based on Integer32"""
    defaultValue = -62

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-82, -62),
    )


_Cld11axNonSrgObssPdMax_Type.__name__ = "Integer32"
_Cld11axNonSrgObssPdMax_Object = MibTableColumn
cld11axNonSrgObssPdMax = _Cld11axNonSrgObssPdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20, 1, 2),
    _Cld11axNonSrgObssPdMax_Type()
)
cld11axNonSrgObssPdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axNonSrgObssPdMax.setStatus("current")


class _Cld11axSrgObssPdEnable_Type(TruthValue):
    """Custom type cld11axSrgObssPdEnable based on TruthValue"""
    defaultValue = 2


_Cld11axSrgObssPdEnable_Type.__name__ = "TruthValue"
_Cld11axSrgObssPdEnable_Object = MibTableColumn
cld11axSrgObssPdEnable = _Cld11axSrgObssPdEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20, 1, 3),
    _Cld11axSrgObssPdEnable_Type()
)
cld11axSrgObssPdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axSrgObssPdEnable.setStatus("current")


class _Cld11axSrgObssPdMin_Type(Integer32):
    """Custom type cld11axSrgObssPdMin based on Integer32"""
    defaultValue = -82

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-82, -62),
    )


_Cld11axSrgObssPdMin_Type.__name__ = "Integer32"
_Cld11axSrgObssPdMin_Object = MibTableColumn
cld11axSrgObssPdMin = _Cld11axSrgObssPdMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20, 1, 4),
    _Cld11axSrgObssPdMin_Type()
)
cld11axSrgObssPdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axSrgObssPdMin.setStatus("current")


class _Cld11axSrgObssPdMax_Type(Integer32):
    """Custom type cld11axSrgObssPdMax based on Integer32"""
    defaultValue = -62

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-82, -62),
    )


_Cld11axSrgObssPdMax_Type.__name__ = "Integer32"
_Cld11axSrgObssPdMax_Object = MibTableColumn
cld11axSrgObssPdMax = _Cld11axSrgObssPdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 20, 1, 5),
    _Cld11axSrgObssPdMax_Type()
)
cld11axSrgObssPdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11axSrgObssPdMax.setStatus("current")
_CldDot11NdpMode_ObjectIdentity = ObjectIdentity
cldDot11NdpMode = _CldDot11NdpMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 21)
)


class _CldDot11bNdpMode_Type(Integer32):
    """Custom type cldDot11bNdpMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CldDot11bNdpMode_Type.__name__ = "Integer32"
_CldDot11bNdpMode_Object = MibScalar
cldDot11bNdpMode = _CldDot11bNdpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 21, 1),
    _CldDot11bNdpMode_Type()
)
cldDot11bNdpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot11bNdpMode.setStatus("current")


class _CldDot11aNdpMode_Type(Integer32):
    """Custom type cldDot11aNdpMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CldDot11aNdpMode_Type.__name__ = "Integer32"
_CldDot11aNdpMode_Object = MibScalar
cldDot11aNdpMode = _CldDot11aNdpMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 21, 2),
    _CldDot11aNdpMode_Type()
)
cldDot11aNdpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot11aNdpMode.setStatus("current")
_CldDot116GHzPhy_ObjectIdentity = ObjectIdentity
cldDot116GHzPhy = _CldDot116GHzPhy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22)
)
_CldDot116GHzMediumOccupancyLimit_Type = Unsigned32
_CldDot116GHzMediumOccupancyLimit_Object = MibScalar
cldDot116GHzMediumOccupancyLimit = _CldDot116GHzMediumOccupancyLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 1),
    _CldDot116GHzMediumOccupancyLimit_Type()
)
cldDot116GHzMediumOccupancyLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzMediumOccupancyLimit.setStatus("current")
_CldDot116GHzCFPPeriod_Type = Unsigned32
_CldDot116GHzCFPPeriod_Object = MibScalar
cldDot116GHzCFPPeriod = _CldDot116GHzCFPPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 2),
    _CldDot116GHzCFPPeriod_Type()
)
cldDot116GHzCFPPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzCFPPeriod.setStatus("current")
_CldDot116GHzCFPMaxDuration_Type = Unsigned32
_CldDot116GHzCFPMaxDuration_Object = MibScalar
cldDot116GHzCFPMaxDuration = _CldDot116GHzCFPMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 3),
    _CldDot116GHzCFPMaxDuration_Type()
)
cldDot116GHzCFPMaxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzCFPMaxDuration.setStatus("current")
_CldDot116GHzCFPollable_Type = TruthValue
_CldDot116GHzCFPollable_Object = MibScalar
cldDot116GHzCFPollable = _CldDot116GHzCFPollable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 4),
    _CldDot116GHzCFPollable_Type()
)
cldDot116GHzCFPollable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzCFPollable.setStatus("current")
_CldDot116GHzCFPollRequest_Type = TruthValue
_CldDot116GHzCFPollRequest_Object = MibScalar
cldDot116GHzCFPollRequest = _CldDot116GHzCFPollRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 5),
    _CldDot116GHzCFPollRequest_Type()
)
cldDot116GHzCFPollRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzCFPollRequest.setStatus("current")
_CldDot116GHzDTIMPeriod_Type = Unsigned32
_CldDot116GHzDTIMPeriod_Object = MibScalar
cldDot116GHzDTIMPeriod = _CldDot116GHzDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 6),
    _CldDot116GHzDTIMPeriod_Type()
)
cldDot116GHzDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzDTIMPeriod.setStatus("current")
_CldDot116GHzRTSThreshold_Type = Unsigned32
_CldDot116GHzRTSThreshold_Object = MibScalar
cldDot116GHzRTSThreshold = _CldDot116GHzRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 7),
    _CldDot116GHzRTSThreshold_Type()
)
cldDot116GHzRTSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzRTSThreshold.setStatus("current")
_CldDot116GHzShortRetryLimit_Type = Unsigned32
_CldDot116GHzShortRetryLimit_Object = MibScalar
cldDot116GHzShortRetryLimit = _CldDot116GHzShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 8),
    _CldDot116GHzShortRetryLimit_Type()
)
cldDot116GHzShortRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzShortRetryLimit.setStatus("current")
_CldDot116GHzLongRetryLimit_Type = Unsigned32
_CldDot116GHzLongRetryLimit_Object = MibScalar
cldDot116GHzLongRetryLimit = _CldDot116GHzLongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 9),
    _CldDot116GHzLongRetryLimit_Type()
)
cldDot116GHzLongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzLongRetryLimit.setStatus("current")


class _CldDot116GHzFragmentationThreshold_Type(Unsigned32):
    """Custom type cldDot116GHzFragmentationThreshold based on Unsigned32"""
    defaultValue = 2346

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_CldDot116GHzFragmentationThreshold_Type.__name__ = "Unsigned32"
_CldDot116GHzFragmentationThreshold_Object = MibScalar
cldDot116GHzFragmentationThreshold = _CldDot116GHzFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 10),
    _CldDot116GHzFragmentationThreshold_Type()
)
cldDot116GHzFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzFragmentationThreshold.setStatus("current")


class _CldDot116GHzMaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type cldDot116GHzMaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CldDot116GHzMaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_CldDot116GHzMaxTransmitMSDULifetime_Object = MibScalar
cldDot116GHzMaxTransmitMSDULifetime = _CldDot116GHzMaxTransmitMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 11),
    _CldDot116GHzMaxTransmitMSDULifetime_Type()
)
cldDot116GHzMaxTransmitMSDULifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzMaxTransmitMSDULifetime.setStatus("current")


class _CldDot116GHzMaxReceiveLifetime_Type(Unsigned32):
    """Custom type cldDot116GHzMaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CldDot116GHzMaxReceiveLifetime_Type.__name__ = "Unsigned32"
_CldDot116GHzMaxReceiveLifetime_Object = MibScalar
cldDot116GHzMaxReceiveLifetime = _CldDot116GHzMaxReceiveLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 12),
    _CldDot116GHzMaxReceiveLifetime_Type()
)
cldDot116GHzMaxReceiveLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzMaxReceiveLifetime.setStatus("current")
_CldDot116GHzChannelAgilityEnabled_Type = TruthValue
_CldDot116GHzChannelAgilityEnabled_Object = MibScalar
cldDot116GHzChannelAgilityEnabled = _CldDot116GHzChannelAgilityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 22, 13),
    _CldDot116GHzChannelAgilityEnabled_Type()
)
cldDot116GHzChannelAgilityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzChannelAgilityEnabled.setStatus("current")
_CldDot116GHzGlobalConfig_ObjectIdentity = ObjectIdentity
cldDot116GHzGlobalConfig = _CldDot116GHzGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23)
)


class _CldDot116GHzNetworkStatus_Type(TruthValue):
    """Custom type cldDot116GHzNetworkStatus based on TruthValue"""
    defaultValue = 1


_CldDot116GHzNetworkStatus_Type.__name__ = "TruthValue"
_CldDot116GHzNetworkStatus_Object = MibScalar
cldDot116GHzNetworkStatus = _CldDot116GHzNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 1),
    _CldDot116GHzNetworkStatus_Type()
)
cldDot116GHzNetworkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzNetworkStatus.setStatus("current")


class _CldDot116GHzBeaconPeriod_Type(Unsigned32):
    """Custom type cldDot116GHzBeaconPeriod based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 1000),
    )


_CldDot116GHzBeaconPeriod_Type.__name__ = "Unsigned32"
_CldDot116GHzBeaconPeriod_Object = MibScalar
cldDot116GHzBeaconPeriod = _CldDot116GHzBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 2),
    _CldDot116GHzBeaconPeriod_Type()
)
cldDot116GHzBeaconPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzBeaconPeriod.setStatus("current")


class _CldDot116GHzDynamicChannelAssignment_Type(Integer32):
    """Custom type cldDot116GHzDynamicChannelAssignment based on Integer32"""
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
          ("runOnce", 2),
          ("static", 3))
    )


_CldDot116GHzDynamicChannelAssignment_Type.__name__ = "Integer32"
_CldDot116GHzDynamicChannelAssignment_Object = MibScalar
cldDot116GHzDynamicChannelAssignment = _CldDot116GHzDynamicChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 3),
    _CldDot116GHzDynamicChannelAssignment_Type()
)
cldDot116GHzDynamicChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzDynamicChannelAssignment.setStatus("current")


class _CldDot116GHzDynamicChannelUpdateInterval_Type(Unsigned32):
    """Custom type cldDot116GHzDynamicChannelUpdateInterval based on Unsigned32"""
    defaultValue = 600


_CldDot116GHzDynamicChannelUpdateInterval_Type.__name__ = "Unsigned32"
_CldDot116GHzDynamicChannelUpdateInterval_Object = MibScalar
cldDot116GHzDynamicChannelUpdateInterval = _CldDot116GHzDynamicChannelUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 4),
    _CldDot116GHzDynamicChannelUpdateInterval_Type()
)
cldDot116GHzDynamicChannelUpdateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzDynamicChannelUpdateInterval.setStatus("current")


class _CldDot116GHzChannelUpdateCmdInvoke_Type(Integer32):
    """Custom type cldDot116GHzChannelUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_CldDot116GHzChannelUpdateCmdInvoke_Type.__name__ = "Integer32"
_CldDot116GHzChannelUpdateCmdInvoke_Object = MibScalar
cldDot116GHzChannelUpdateCmdInvoke = _CldDot116GHzChannelUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 5),
    _CldDot116GHzChannelUpdateCmdInvoke_Type()
)
cldDot116GHzChannelUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzChannelUpdateCmdInvoke.setStatus("current")
_CldDot116GHzChannelUpdateCmdStatus_Type = Unsigned32
_CldDot116GHzChannelUpdateCmdStatus_Object = MibScalar
cldDot116GHzChannelUpdateCmdStatus = _CldDot116GHzChannelUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 6),
    _CldDot116GHzChannelUpdateCmdStatus_Type()
)
cldDot116GHzChannelUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzChannelUpdateCmdStatus.setStatus("current")


class _CldDot116GHzDynamicTransmitPowerControl_Type(Integer32):
    """Custom type cldDot116GHzDynamicTransmitPowerControl based on Integer32"""
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
          ("runOnce", 2),
          ("static", 3))
    )


_CldDot116GHzDynamicTransmitPowerControl_Type.__name__ = "Integer32"
_CldDot116GHzDynamicTransmitPowerControl_Object = MibScalar
cldDot116GHzDynamicTransmitPowerControl = _CldDot116GHzDynamicTransmitPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 7),
    _CldDot116GHzDynamicTransmitPowerControl_Type()
)
cldDot116GHzDynamicTransmitPowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzDynamicTransmitPowerControl.setStatus("current")


class _CldDot116GHzCurrentTxPowerLevel_Type(Integer32):
    """Custom type cldDot116GHzCurrentTxPowerLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_CldDot116GHzCurrentTxPowerLevel_Type.__name__ = "Integer32"
_CldDot116GHzCurrentTxPowerLevel_Object = MibScalar
cldDot116GHzCurrentTxPowerLevel = _CldDot116GHzCurrentTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 8),
    _CldDot116GHzCurrentTxPowerLevel_Type()
)
cldDot116GHzCurrentTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzCurrentTxPowerLevel.setStatus("current")


class _CldDot116GHzPowerUpdateCmdInvoke_Type(Integer32):
    """Custom type cldDot116GHzPowerUpdateCmdInvoke based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("activate", 1))
    )


_CldDot116GHzPowerUpdateCmdInvoke_Type.__name__ = "Integer32"
_CldDot116GHzPowerUpdateCmdInvoke_Object = MibScalar
cldDot116GHzPowerUpdateCmdInvoke = _CldDot116GHzPowerUpdateCmdInvoke_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 9),
    _CldDot116GHzPowerUpdateCmdInvoke_Type()
)
cldDot116GHzPowerUpdateCmdInvoke.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzPowerUpdateCmdInvoke.setStatus("current")
_CldDot116GHzPowerUpdateCmdStatus_Type = Unsigned32
_CldDot116GHzPowerUpdateCmdStatus_Object = MibScalar
cldDot116GHzPowerUpdateCmdStatus = _CldDot116GHzPowerUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 10),
    _CldDot116GHzPowerUpdateCmdStatus_Type()
)
cldDot116GHzPowerUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldDot116GHzPowerUpdateCmdStatus.setStatus("current")


class _CldDot116GHz80211eMaxBandwidth_Type(Integer32):
    """Custom type cldDot116GHz80211eMaxBandwidth based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 85),
    )


_CldDot116GHz80211eMaxBandwidth_Type.__name__ = "Integer32"
_CldDot116GHz80211eMaxBandwidth_Object = MibScalar
cldDot116GHz80211eMaxBandwidth = _CldDot116GHz80211eMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 11),
    _CldDot116GHz80211eMaxBandwidth_Type()
)
cldDot116GHz80211eMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHz80211eMaxBandwidth.setStatus("current")


class _CldDot116GHzDTPCSupport_Type(TruthValue):
    """Custom type cldDot116GHzDTPCSupport based on TruthValue"""
    defaultValue = 1


_CldDot116GHzDTPCSupport_Type.__name__ = "TruthValue"
_CldDot116GHzDTPCSupport_Object = MibScalar
cldDot116GHzDTPCSupport = _CldDot116GHzDTPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 23, 12),
    _CldDot116GHzDTPCSupport_Type()
)
cldDot116GHzDTPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldDot116GHzDTPCSupport.setStatus("current")
_Cld11beMcsTable_Object = MibTable
cld11beMcsTable = _Cld11beMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 24)
)
if mibBuilder.loadTexts:
    cld11beMcsTable.setStatus("current")
_Cld11beMcsEntry_Object = MibTableRow
cld11beMcsEntry = _Cld11beMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 24, 1)
)
cld11beMcsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldDot11beBand"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11beMcsSpatialStreamIndex"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11beMcsDataRateIndex"),
)
if mibBuilder.loadTexts:
    cld11beMcsEntry.setStatus("current")
_CldDot11beBand_Type = CLDot11Band
_CldDot11beBand_Object = MibTableColumn
cldDot11beBand = _CldDot11beBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 24, 1, 1),
    _CldDot11beBand_Type()
)
cldDot11beBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldDot11beBand.setStatus("current")
_Cld11beMcsSpatialStreamIndex_Type = Unsigned32
_Cld11beMcsSpatialStreamIndex_Object = MibTableColumn
cld11beMcsSpatialStreamIndex = _Cld11beMcsSpatialStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 24, 1, 2),
    _Cld11beMcsSpatialStreamIndex_Type()
)
cld11beMcsSpatialStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11beMcsSpatialStreamIndex.setStatus("current")
_Cld11beMcsDataRateIndex_Type = Unsigned32
_Cld11beMcsDataRateIndex_Object = MibTableColumn
cld11beMcsDataRateIndex = _Cld11beMcsDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 24, 1, 3),
    _Cld11beMcsDataRateIndex_Type()
)
cld11beMcsDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11beMcsDataRateIndex.setStatus("current")


class _Cld11beMcsSupportEnable_Type(TruthValue):
    """Custom type cld11beMcsSupportEnable based on TruthValue"""
    defaultValue = 1


_Cld11beMcsSupportEnable_Type.__name__ = "TruthValue"
_Cld11beMcsSupportEnable_Object = MibTableColumn
cld11beMcsSupportEnable = _Cld11beMcsSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 24, 1, 4),
    _Cld11beMcsSupportEnable_Type()
)
cld11beMcsSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11beMcsSupportEnable.setStatus("current")
_CldStatus_ObjectIdentity = ObjectIdentity
cldStatus = _CldStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2)
)
_CldCountryTable_Object = MibTable
cldCountryTable = _CldCountryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cldCountryTable.setStatus("current")
_CldCountryEntry_Object = MibTableRow
cldCountryEntry = _CldCountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1)
)
cldCountryEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldCountryCode"),
)
if mibBuilder.loadTexts:
    cldCountryEntry.setStatus("current")


class _CldCountryCode_Type(SnmpAdminString):
    """Custom type cldCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CldCountryCode_Type.__name__ = "SnmpAdminString"
_CldCountryCode_Object = MibTableColumn
cldCountryCode = _CldCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 1),
    _CldCountryCode_Type()
)
cldCountryCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldCountryCode.setStatus("current")
_CldCountryName_Type = SnmpAdminString
_CldCountryName_Object = MibTableColumn
cldCountryName = _CldCountryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 2),
    _CldCountryName_Type()
)
cldCountryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryName.setStatus("current")
_CldCountryDot11aChannels_Type = SnmpAdminString
_CldCountryDot11aChannels_Object = MibTableColumn
cldCountryDot11aChannels = _CldCountryDot11aChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 3),
    _CldCountryDot11aChannels_Type()
)
cldCountryDot11aChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11aChannels.setStatus("current")
_CldCountryDot11bChannels_Type = SnmpAdminString
_CldCountryDot11bChannels_Object = MibTableColumn
cldCountryDot11bChannels = _CldCountryDot11bChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 4),
    _CldCountryDot11bChannels_Type()
)
cldCountryDot11bChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11bChannels.setStatus("current")
_CldCountryDot11aDcaChannels_Type = SnmpAdminString
_CldCountryDot11aDcaChannels_Object = MibTableColumn
cldCountryDot11aDcaChannels = _CldCountryDot11aDcaChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 5),
    _CldCountryDot11aDcaChannels_Type()
)
cldCountryDot11aDcaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11aDcaChannels.setStatus("current")
_CldCountryDot11bDcaChannels_Type = SnmpAdminString
_CldCountryDot11bDcaChannels_Object = MibTableColumn
cldCountryDot11bDcaChannels = _CldCountryDot11bDcaChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 6),
    _CldCountryDot11bDcaChannels_Type()
)
cldCountryDot11bDcaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11bDcaChannels.setStatus("current")
_CldCountryDot116GHzChannels_Type = SnmpAdminString
_CldCountryDot116GHzChannels_Object = MibTableColumn
cldCountryDot116GHzChannels = _CldCountryDot116GHzChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 7),
    _CldCountryDot116GHzChannels_Type()
)
cldCountryDot116GHzChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot116GHzChannels.setStatus("current")
_CldCountryDot116GHzDcaChannels_Type = SnmpAdminString
_CldCountryDot116GHzDcaChannels_Object = MibTableColumn
cldCountryDot116GHzDcaChannels = _CldCountryDot116GHzDcaChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 8),
    _CldCountryDot116GHzDcaChannels_Type()
)
cldCountryDot116GHzDcaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot116GHzDcaChannels.setStatus("current")
_CiscoLwappDot11MIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBConform = _CiscoLwappDot11MIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2)
)
_CiscoLwappDot11MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBCompliances = _CiscoLwappDot11MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 1)
)
_CiscoLwappDot11MIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBGroups = _CiscoLwappDot11MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2)
)

# Managed Objects groups

ciscoLwappDot11MIBMacOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 1)
)
ciscoLwappDot11MIBMacOperGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nChannelBandwidth"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nRifsEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nAmsduEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nAmpduEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nGuardIntervalEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBMacOperGroup.setStatus("current")

ciscoLwappDot11MIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 2)
)
ciscoLwappDot11MIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldMultipleCountryCode"),
        ("CISCO-LWAPP-DOT11-MIB", "cldRegulatoryDomain"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsDataRate"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsSupportEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryChangeNotifEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingWindowSize"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingDenialCount"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectCycleCount"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectCycleThreshold"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectAgeOutSuppression"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectAgeOutDualBand"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectClientRssi"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsChannelWidth"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsGuardInterval"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsModulation"),
        ("CISCO-LWAPP-DOT11-MIB", "cldVhtDot11acEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11acMcsSupportEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingTrafficThreshold"),
        ("CISCO-LWAPP-DOT11-MIB", "cldDot11axEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axMcsSupportEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axMbssidCap"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axBssColorState"),
        ("CISCO-LWAPP-DOT11-MIB", "cldConfiguredCountryCode"),
        ("CISCO-LWAPP-DOT11-MIB", "cldConfiguredCountryRowStatus"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axObssPdEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axNonSrgObssPdMax"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axSrgObssPdEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axSrgObssPdMin"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11axSrgObssPdMax"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBConfigGroup.setStatus("current")

ciscoLwappDot11MIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 4)
)
ciscoLwappDot11MIBStatusGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "cldCountryName"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11aChannels"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11bChannels"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11aDcaChannels"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11bDcaChannels"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBStatusGroup.setStatus("current")


# Notification objects

ciscoLwappDot11CountryChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 0, 1)
)
ciscoLwappDot11CountryChangeNotif.setObjects(
    ("CISCO-LWAPP-DOT11-MIB", "cldMultipleCountryCode")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11CountryChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappDot11MIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 3)
)
ciscoLwappDot11MIBNotifsGroup.setObjects(
    ("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11CountryChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappDot11MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 1, 1)
)
ciscoLwappDot11MIBCompliance.setObjects(
    ("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11MIBMacOperGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappDot11MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 1, 2)
)
ciscoLwappDot11MIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11MIBMacOperGroup"),
        ("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11MIBConfigGroup"),
        ("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11MIBNotifsGroup"),
        ("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11MIBStatusGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-MIB",
    **{"ciscoLwappDot11MIB": ciscoLwappDot11MIB,
       "ciscoLwappDot11MIBNotifs": ciscoLwappDot11MIBNotifs,
       "ciscoLwappDot11CountryChangeNotif": ciscoLwappDot11CountryChangeNotif,
       "ciscoLwappDot11MIBObjects": ciscoLwappDot11MIBObjects,
       "cldConfig": cldConfig,
       "cldHtMacOperationsTable": cldHtMacOperationsTable,
       "cldHtMacOperationsEntry": cldHtMacOperationsEntry,
       "cldHtDot11nBand": cldHtDot11nBand,
       "cldHtDot11nChannelBandwidth": cldHtDot11nChannelBandwidth,
       "cldHtDot11nRifsEnable": cldHtDot11nRifsEnable,
       "cldHtDot11nAmsduEnable": cldHtDot11nAmsduEnable,
       "cldHtDot11nAmpduEnable": cldHtDot11nAmpduEnable,
       "cldHtDot11nGuardIntervalEnable": cldHtDot11nGuardIntervalEnable,
       "cldHtDot11nEnable": cldHtDot11nEnable,
       "cldMultipleCountryCode": cldMultipleCountryCode,
       "cldRegulatoryDomain": cldRegulatoryDomain,
       "cld11nMcsTable": cld11nMcsTable,
       "cld11nMcsEntry": cld11nMcsEntry,
       "cld11nMcsBand": cld11nMcsBand,
       "cld11nMcsDataRateIndex": cld11nMcsDataRateIndex,
       "cld11nMcsDataRate": cld11nMcsDataRate,
       "cld11nMcsSupportEnable": cld11nMcsSupportEnable,
       "cld11nMcsChannelWidth": cld11nMcsChannelWidth,
       "cld11nMcsGuardInterval": cld11nMcsGuardInterval,
       "cld11nMcsModulation": cld11nMcsModulation,
       "cld11acConfig": cld11acConfig,
       "cldVhtDot11acEnable": cldVhtDot11acEnable,
       "cld11acMcsTable": cld11acMcsTable,
       "cld11acMcsEntry": cld11acMcsEntry,
       "cld11acMcsSpatialStreamIndex": cld11acMcsSpatialStreamIndex,
       "cld11acMcsDataRateIndex": cld11acMcsDataRateIndex,
       "cld11acMcsSupportEnable": cld11acMcsSupportEnable,
       "cldCountryChangeNotifEnable": cldCountryChangeNotifEnable,
       "cldLoadBalancing": cldLoadBalancing,
       "cldLoadBalancingEnable": cldLoadBalancingEnable,
       "cldLoadBalancingWindowSize": cldLoadBalancingWindowSize,
       "cldLoadBalancingDenialCount": cldLoadBalancingDenialCount,
       "cldLoadBalancingTrafficThreshold": cldLoadBalancingTrafficThreshold,
       "cldLoadBalancingDot11aWindowSize": cldLoadBalancingDot11aWindowSize,
       "cldLoadBalancingDot11aDenialCount": cldLoadBalancingDot11aDenialCount,
       "cldLoadBalancingDot11bWindowSize": cldLoadBalancingDot11bWindowSize,
       "cldLoadBalancingDot11bDenialCount": cldLoadBalancingDot11bDenialCount,
       "cldBandSelect": cldBandSelect,
       "cldBandSelectEnable": cldBandSelectEnable,
       "cldBandSelectCycleCount": cldBandSelectCycleCount,
       "cldBandSelectCycleThreshold": cldBandSelectCycleThreshold,
       "cldBandSelectAgeOutSuppression": cldBandSelectAgeOutSuppression,
       "cldBandSelectAgeOutDualBand": cldBandSelectAgeOutDualBand,
       "cldBandSelectClientRssi": cldBandSelectClientRssi,
       "cldBandSelectClientMidRssi": cldBandSelectClientMidRssi,
       "cld11axConfigTable": cld11axConfigTable,
       "cld11axConfigEntry": cld11axConfigEntry,
       "cldDot11axBandId": cldDot11axBandId,
       "cldDot11axEnable": cldDot11axEnable,
       "cld11axMcsTable": cld11axMcsTable,
       "cld11axMcsEntry": cld11axMcsEntry,
       "cldDot11axBand": cldDot11axBand,
       "cld11axMcsSpatialStreamIndex": cld11axMcsSpatialStreamIndex,
       "cld11axMcsDataRateIndex": cld11axMcsDataRateIndex,
       "cld11axMcsSupportEnable": cld11axMcsSupportEnable,
       "cldDot11axHeCapTable": cldDot11axHeCapTable,
       "cldDot11axHeCapEntry": cldDot11axHeCapEntry,
       "cldDot11IsHeCapable": cldDot11IsHeCapable,
       "cldDot11IsHeEnable": cldDot11IsHeEnable,
       "cldDot11HeSuBF": cldDot11HeSuBF,
       "cldDot11HeMuBF": cldDot11HeMuBF,
       "cldDot11HeStbcMode": cldDot11HeStbcMode,
       "cldDot11HeAmpduTidBmap": cldDot11HeAmpduTidBmap,
       "cldDot11HeCapTxRxMcsNss": cldDot11HeCapTxRxMcsNss,
       "cld11axMbssidTable": cld11axMbssidTable,
       "cld11axMbssidEntry": cld11axMbssidEntry,
       "cldBand": cldBand,
       "cld11axMbssidCap": cld11axMbssidCap,
       "cldDot11RxsopThreshold": cldDot11RxsopThreshold,
       "cldDot11bRxSopThresholdCustom": cldDot11bRxSopThresholdCustom,
       "cldDot11aRxSopThresholdCustom": cldDot11aRxSopThresholdCustom,
       "cld11axTargetWakeupTimeTable": cld11axTargetWakeupTimeTable,
       "cld11axTargetWakeupTimeEntry": cld11axTargetWakeupTimeEntry,
       "cld11axTargetWakeupTimeEnable": cld11axTargetWakeupTimeEnable,
       "cld11axTargetWakeupTimeBroadcastTable": cld11axTargetWakeupTimeBroadcastTable,
       "cld11axTargetWakeupTimeBroadcastEntry": cld11axTargetWakeupTimeBroadcastEntry,
       "cld11axTargetWakeupTimeBroadcastEnable": cld11axTargetWakeupTimeBroadcastEnable,
       "cld11axBssColorConfigTable": cld11axBssColorConfigTable,
       "cld11axBssColorConfigEntry": cld11axBssColorConfigEntry,
       "cld11axBssColorState": cld11axBssColorState,
       "cld11axBssColorRadioTable": cld11axBssColorRadioTable,
       "cld11axBssColorRadioEntry": cld11axBssColorRadioEntry,
       "cld11axIsBssColorCapable": cld11axIsBssColorCapable,
       "cld11axBssColor": cld11axBssColor,
       "cld11axBssColorConfigType": cld11axBssColorConfigType,
       "cldConfiguredCountryTable": cldConfiguredCountryTable,
       "cldConfiguredCountryEntry": cldConfiguredCountryEntry,
       "cldConfiguredCountryCode": cldConfiguredCountryCode,
       "cldConfiguredCountryRowStatus": cldConfiguredCountryRowStatus,
       "cld11axObssPdConfigTable": cld11axObssPdConfigTable,
       "cld11axObssPdConfigEntry": cld11axObssPdConfigEntry,
       "cld11axObssPdEnable": cld11axObssPdEnable,
       "cld11axNonSrgObssPdMax": cld11axNonSrgObssPdMax,
       "cld11axSrgObssPdEnable": cld11axSrgObssPdEnable,
       "cld11axSrgObssPdMin": cld11axSrgObssPdMin,
       "cld11axSrgObssPdMax": cld11axSrgObssPdMax,
       "cldDot11NdpMode": cldDot11NdpMode,
       "cldDot11bNdpMode": cldDot11bNdpMode,
       "cldDot11aNdpMode": cldDot11aNdpMode,
       "cldDot116GHzPhy": cldDot116GHzPhy,
       "cldDot116GHzMediumOccupancyLimit": cldDot116GHzMediumOccupancyLimit,
       "cldDot116GHzCFPPeriod": cldDot116GHzCFPPeriod,
       "cldDot116GHzCFPMaxDuration": cldDot116GHzCFPMaxDuration,
       "cldDot116GHzCFPollable": cldDot116GHzCFPollable,
       "cldDot116GHzCFPollRequest": cldDot116GHzCFPollRequest,
       "cldDot116GHzDTIMPeriod": cldDot116GHzDTIMPeriod,
       "cldDot116GHzRTSThreshold": cldDot116GHzRTSThreshold,
       "cldDot116GHzShortRetryLimit": cldDot116GHzShortRetryLimit,
       "cldDot116GHzLongRetryLimit": cldDot116GHzLongRetryLimit,
       "cldDot116GHzFragmentationThreshold": cldDot116GHzFragmentationThreshold,
       "cldDot116GHzMaxTransmitMSDULifetime": cldDot116GHzMaxTransmitMSDULifetime,
       "cldDot116GHzMaxReceiveLifetime": cldDot116GHzMaxReceiveLifetime,
       "cldDot116GHzChannelAgilityEnabled": cldDot116GHzChannelAgilityEnabled,
       "cldDot116GHzGlobalConfig": cldDot116GHzGlobalConfig,
       "cldDot116GHzNetworkStatus": cldDot116GHzNetworkStatus,
       "cldDot116GHzBeaconPeriod": cldDot116GHzBeaconPeriod,
       "cldDot116GHzDynamicChannelAssignment": cldDot116GHzDynamicChannelAssignment,
       "cldDot116GHzDynamicChannelUpdateInterval": cldDot116GHzDynamicChannelUpdateInterval,
       "cldDot116GHzChannelUpdateCmdInvoke": cldDot116GHzChannelUpdateCmdInvoke,
       "cldDot116GHzChannelUpdateCmdStatus": cldDot116GHzChannelUpdateCmdStatus,
       "cldDot116GHzDynamicTransmitPowerControl": cldDot116GHzDynamicTransmitPowerControl,
       "cldDot116GHzCurrentTxPowerLevel": cldDot116GHzCurrentTxPowerLevel,
       "cldDot116GHzPowerUpdateCmdInvoke": cldDot116GHzPowerUpdateCmdInvoke,
       "cldDot116GHzPowerUpdateCmdStatus": cldDot116GHzPowerUpdateCmdStatus,
       "cldDot116GHz80211eMaxBandwidth": cldDot116GHz80211eMaxBandwidth,
       "cldDot116GHzDTPCSupport": cldDot116GHzDTPCSupport,
       "cld11beMcsTable": cld11beMcsTable,
       "cld11beMcsEntry": cld11beMcsEntry,
       "cldDot11beBand": cldDot11beBand,
       "cld11beMcsSpatialStreamIndex": cld11beMcsSpatialStreamIndex,
       "cld11beMcsDataRateIndex": cld11beMcsDataRateIndex,
       "cld11beMcsSupportEnable": cld11beMcsSupportEnable,
       "cldStatus": cldStatus,
       "cldCountryTable": cldCountryTable,
       "cldCountryEntry": cldCountryEntry,
       "cldCountryCode": cldCountryCode,
       "cldCountryName": cldCountryName,
       "cldCountryDot11aChannels": cldCountryDot11aChannels,
       "cldCountryDot11bChannels": cldCountryDot11bChannels,
       "cldCountryDot11aDcaChannels": cldCountryDot11aDcaChannels,
       "cldCountryDot11bDcaChannels": cldCountryDot11bDcaChannels,
       "cldCountryDot116GHzChannels": cldCountryDot116GHzChannels,
       "cldCountryDot116GHzDcaChannels": cldCountryDot116GHzDcaChannels,
       "ciscoLwappDot11MIBConform": ciscoLwappDot11MIBConform,
       "ciscoLwappDot11MIBCompliances": ciscoLwappDot11MIBCompliances,
       "ciscoLwappDot11MIBCompliance": ciscoLwappDot11MIBCompliance,
       "ciscoLwappDot11MIBComplianceRev1": ciscoLwappDot11MIBComplianceRev1,
       "ciscoLwappDot11MIBGroups": ciscoLwappDot11MIBGroups,
       "ciscoLwappDot11MIBMacOperGroup": ciscoLwappDot11MIBMacOperGroup,
       "ciscoLwappDot11MIBConfigGroup": ciscoLwappDot11MIBConfigGroup,
       "ciscoLwappDot11MIBNotifsGroup": ciscoLwappDot11MIBNotifsGroup,
       "ciscoLwappDot11MIBStatusGroup": ciscoLwappDot11MIBStatusGroup}
)
