# SNMP MIB module (RUIJIE-BGP-ACCOUNTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-BGP-ACCOUNTING-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:44 2025
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

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressType")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieBgpAccountingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166)
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingMIB.setRevisions(
        ("2020-10-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieBgpAccountingMIBObjects_ObjectIdentity = ObjectIdentity
ruijieBgpAccountingMIBObjects = _RuijieBgpAccountingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1)
)
_RuijieBgpAccountingStatisticsTable_Object = MibTable
ruijieBgpAccountingStatisticsTable = _RuijieBgpAccountingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingStatisticsTable.setStatus("current")
_RuijieBgpAccountingStatisticsEntry_Object = MibTableRow
ruijieBgpAccountingStatisticsEntry = _RuijieBgpAccountingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1)
)
ruijieBgpAccountingStatisticsEntry.setIndexNames(
    (0, "RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingAddrType"),
    (0, "RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingInterfaceIndex"),
    (0, "RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingDirection"),
    (0, "RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingTrafficIndex"),
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingStatisticsEntry.setStatus("current")
_BgpAccountingAddrType_Type = InetAddressType
_BgpAccountingAddrType_Object = MibTableColumn
bgpAccountingAddrType = _BgpAccountingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 1),
    _BgpAccountingAddrType_Type()
)
bgpAccountingAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingAddrType.setStatus("current")
_BgpAccountingInterfaceIndex_Type = IfIndex
_BgpAccountingInterfaceIndex_Object = MibTableColumn
bgpAccountingInterfaceIndex = _BgpAccountingInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 2),
    _BgpAccountingInterfaceIndex_Type()
)
bgpAccountingInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingInterfaceIndex.setStatus("current")


class _BgpAccountingDirection_Type(Integer32):
    """Custom type bgpAccountingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_BgpAccountingDirection_Type.__name__ = "Integer32"
_BgpAccountingDirection_Object = MibTableColumn
bgpAccountingDirection = _BgpAccountingDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 3),
    _BgpAccountingDirection_Type()
)
bgpAccountingDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingDirection.setStatus("current")


class _BgpAccountingTrafficIndex_Type(Integer32):
    """Custom type bgpAccountingTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BgpAccountingTrafficIndex_Type.__name__ = "Integer32"
_BgpAccountingTrafficIndex_Object = MibTableColumn
bgpAccountingTrafficIndex = _BgpAccountingTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 4),
    _BgpAccountingTrafficIndex_Type()
)
bgpAccountingTrafficIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingTrafficIndex.setStatus("current")
_BgpAccountingMatchedPackets_Type = Counter64
_BgpAccountingMatchedPackets_Object = MibTableColumn
bgpAccountingMatchedPackets = _BgpAccountingMatchedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 5),
    _BgpAccountingMatchedPackets_Type()
)
bgpAccountingMatchedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingMatchedPackets.setStatus("current")
_BgpAccountingMatchedBytes_Type = Counter64
_BgpAccountingMatchedBytes_Object = MibTableColumn
bgpAccountingMatchedBytes = _BgpAccountingMatchedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 6),
    _BgpAccountingMatchedBytes_Type()
)
bgpAccountingMatchedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingMatchedBytes.setStatus("current")
_BgpAccountingMatchedPacketsRate_Type = Counter64
_BgpAccountingMatchedPacketsRate_Object = MibTableColumn
bgpAccountingMatchedPacketsRate = _BgpAccountingMatchedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 7),
    _BgpAccountingMatchedPacketsRate_Type()
)
bgpAccountingMatchedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingMatchedPacketsRate.setStatus("current")
_BgpAccountingMatchedBitsRate_Type = Counter64
_BgpAccountingMatchedBitsRate_Object = MibTableColumn
bgpAccountingMatchedBitsRate = _BgpAccountingMatchedBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 1, 1, 8),
    _BgpAccountingMatchedBitsRate_Type()
)
bgpAccountingMatchedBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingMatchedBitsRate.setStatus("current")
_RuijieBgpAccountingStatisticsResetTable_Object = MibTable
ruijieBgpAccountingStatisticsResetTable = _RuijieBgpAccountingStatisticsResetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingStatisticsResetTable.setStatus("current")
_RuijieBgpAccountingStatisticsResetEntry_Object = MibTableRow
ruijieBgpAccountingStatisticsResetEntry = _RuijieBgpAccountingStatisticsResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 2, 1)
)
ruijieBgpAccountingStatisticsResetEntry.setIndexNames(
    (0, "RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingResetInterfaceIndex"),
    (0, "RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingResetDirection"),
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingStatisticsResetEntry.setStatus("current")
_BgpAccountingResetInterfaceIndex_Type = IfIndex
_BgpAccountingResetInterfaceIndex_Object = MibTableColumn
bgpAccountingResetInterfaceIndex = _BgpAccountingResetInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 2, 1, 1),
    _BgpAccountingResetInterfaceIndex_Type()
)
bgpAccountingResetInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingResetInterfaceIndex.setStatus("current")


class _BgpAccountingResetDirection_Type(Integer32):
    """Custom type bgpAccountingResetDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_BgpAccountingResetDirection_Type.__name__ = "Integer32"
_BgpAccountingResetDirection_Object = MibTableColumn
bgpAccountingResetDirection = _BgpAccountingResetDirection_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 2, 1, 2),
    _BgpAccountingResetDirection_Type()
)
bgpAccountingResetDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAccountingResetDirection.setStatus("current")


class _BgpAccountingStatisticsReset_Type(Integer32):
    """Custom type bgpAccountingStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_BgpAccountingStatisticsReset_Type.__name__ = "Integer32"
_BgpAccountingStatisticsReset_Object = MibTableColumn
bgpAccountingStatisticsReset = _BgpAccountingStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 1, 2, 1, 3),
    _BgpAccountingStatisticsReset_Type()
)
bgpAccountingStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bgpAccountingStatisticsReset.setStatus("current")
_RuijieBgpAccountingMIBConformance_ObjectIdentity = ObjectIdentity
ruijieBgpAccountingMIBConformance = _RuijieBgpAccountingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 3)
)
_RuijieBgpAccountingMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieBgpAccountingMIBCompliances = _RuijieBgpAccountingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 3, 1)
)
_RuijieBgpAccountingMIBGroups_ObjectIdentity = ObjectIdentity
ruijieBgpAccountingMIBGroups = _RuijieBgpAccountingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 3, 2)
)

# Managed Objects groups

ruijieBgpAccountingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 3, 2, 1)
)
ruijieBgpAccountingMIBGroup.setObjects(
      *(("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingInterfaceIndex"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingDirection"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingTrafficIndex"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingMatchedPackets"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingMatchedBytes"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingResetInterfaceIndex"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingResetDirection"),
        ("RUIJIE-BGP-ACCOUNTING-MIB", "bgpAccountingStatisticsReset"))
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieBgpAccountingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 166, 3, 1, 1)
)
ruijieBgpAccountingMIBCompliance.setObjects(
    ("RUIJIE-BGP-ACCOUNTING-MIB", "ruijieBgpAccountingMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieBgpAccountingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-BGP-ACCOUNTING-MIB",
    **{"ruijieBgpAccountingMIB": ruijieBgpAccountingMIB,
       "ruijieBgpAccountingMIBObjects": ruijieBgpAccountingMIBObjects,
       "ruijieBgpAccountingStatisticsTable": ruijieBgpAccountingStatisticsTable,
       "ruijieBgpAccountingStatisticsEntry": ruijieBgpAccountingStatisticsEntry,
       "bgpAccountingAddrType": bgpAccountingAddrType,
       "bgpAccountingInterfaceIndex": bgpAccountingInterfaceIndex,
       "bgpAccountingDirection": bgpAccountingDirection,
       "bgpAccountingTrafficIndex": bgpAccountingTrafficIndex,
       "bgpAccountingMatchedPackets": bgpAccountingMatchedPackets,
       "bgpAccountingMatchedBytes": bgpAccountingMatchedBytes,
       "bgpAccountingMatchedPacketsRate": bgpAccountingMatchedPacketsRate,
       "bgpAccountingMatchedBitsRate": bgpAccountingMatchedBitsRate,
       "ruijieBgpAccountingStatisticsResetTable": ruijieBgpAccountingStatisticsResetTable,
       "ruijieBgpAccountingStatisticsResetEntry": ruijieBgpAccountingStatisticsResetEntry,
       "bgpAccountingResetInterfaceIndex": bgpAccountingResetInterfaceIndex,
       "bgpAccountingResetDirection": bgpAccountingResetDirection,
       "bgpAccountingStatisticsReset": bgpAccountingStatisticsReset,
       "ruijieBgpAccountingMIBConformance": ruijieBgpAccountingMIBConformance,
       "ruijieBgpAccountingMIBCompliances": ruijieBgpAccountingMIBCompliances,
       "ruijieBgpAccountingMIBCompliance": ruijieBgpAccountingMIBCompliance,
       "ruijieBgpAccountingMIBGroups": ruijieBgpAccountingMIBGroups,
       "ruijieBgpAccountingMIBGroup": ruijieBgpAccountingMIBGroup}
)
