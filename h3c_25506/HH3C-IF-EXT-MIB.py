# SNMP MIB module (HH3C-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-IF-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:37:35 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

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

hh3cIfExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40)
)
if mibBuilder.loadTexts:
    hh3cIfExt.setRevisions(
        ("2014-11-20 08:00",
         "2009-05-06 19:36",
         "2004-11-13 19:36")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cIfExtScalarGroup_ObjectIdentity = ObjectIdentity
hh3cIfExtScalarGroup = _Hh3cIfExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1)
)
_Hh3cIfStatGlobalFlowInterval_Type = Integer32
_Hh3cIfStatGlobalFlowInterval_Object = MibScalar
hh3cIfStatGlobalFlowInterval = _Hh3cIfStatGlobalFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1, 1),
    _Hh3cIfStatGlobalFlowInterval_Type()
)
hh3cIfStatGlobalFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfStatGlobalFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfStatGlobalFlowInterval.setUnits("seconds")
_Hh3cIfShutDownInterval_Type = Integer32
_Hh3cIfShutDownInterval_Object = MibScalar
hh3cIfShutDownInterval = _Hh3cIfShutDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 1, 2),
    _Hh3cIfShutDownInterval_Type()
)
hh3cIfShutDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfShutDownInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfShutDownInterval.setUnits("seconds")
_Hh3cIfExtGroup_ObjectIdentity = ObjectIdentity
hh3cIfExtGroup = _Hh3cIfExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2)
)
_Hh3cIfStat_ObjectIdentity = ObjectIdentity
hh3cIfStat = _Hh3cIfStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1)
)
_Hh3cIfStatScalarGroup_ObjectIdentity = ObjectIdentity
hh3cIfStatScalarGroup = _Hh3cIfStatScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 1)
)
_Hh3cIfStatTable_ObjectIdentity = ObjectIdentity
hh3cIfStatTable = _Hh3cIfStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2)
)
_Hh3cIfFlowStatTable_Object = MibTable
hh3cIfFlowStatTable = _Hh3cIfFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIfFlowStatTable.setStatus("current")
_Hh3cIfFlowStatEntry_Object = MibTableRow
hh3cIfFlowStatEntry = _Hh3cIfFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1)
)
hh3cIfFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfFlowStatEntry.setStatus("current")
_Hh3cIfStatFlowInterval_Type = Integer32
_Hh3cIfStatFlowInterval_Object = MibTableColumn
hh3cIfStatFlowInterval = _Hh3cIfStatFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 1),
    _Hh3cIfStatFlowInterval_Type()
)
hh3cIfStatFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInterval.setUnits("seconds")
_Hh3cIfStatFlowInBits_Type = Unsigned32
_Hh3cIfStatFlowInBits_Object = MibTableColumn
hh3cIfStatFlowInBits = _Hh3cIfStatFlowInBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 2),
    _Hh3cIfStatFlowInBits_Type()
)
hh3cIfStatFlowInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInBits.setStatus("current")
_Hh3cIfStatFlowOutBits_Type = Unsigned32
_Hh3cIfStatFlowOutBits_Object = MibTableColumn
hh3cIfStatFlowOutBits = _Hh3cIfStatFlowOutBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 3),
    _Hh3cIfStatFlowOutBits_Type()
)
hh3cIfStatFlowOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowOutBits.setStatus("current")
_Hh3cIfStatFlowInPkts_Type = Unsigned32
_Hh3cIfStatFlowInPkts_Object = MibTableColumn
hh3cIfStatFlowInPkts = _Hh3cIfStatFlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 4),
    _Hh3cIfStatFlowInPkts_Type()
)
hh3cIfStatFlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInPkts.setStatus("current")
_Hh3cIfStatFlowOutPkts_Type = Unsigned32
_Hh3cIfStatFlowOutPkts_Object = MibTableColumn
hh3cIfStatFlowOutPkts = _Hh3cIfStatFlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 5),
    _Hh3cIfStatFlowOutPkts_Type()
)
hh3cIfStatFlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowOutPkts.setStatus("current")
_Hh3cIfStatFlowInBytes_Type = Unsigned32
_Hh3cIfStatFlowInBytes_Object = MibTableColumn
hh3cIfStatFlowInBytes = _Hh3cIfStatFlowInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 6),
    _Hh3cIfStatFlowInBytes_Type()
)
hh3cIfStatFlowInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowInBytes.setStatus("current")
_Hh3cIfStatFlowOutBytes_Type = Unsigned32
_Hh3cIfStatFlowOutBytes_Object = MibTableColumn
hh3cIfStatFlowOutBytes = _Hh3cIfStatFlowOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 1, 1, 7),
    _Hh3cIfStatFlowOutBytes_Type()
)
hh3cIfStatFlowOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowOutBytes.setStatus("current")
_Hh3cIfSpeedStatTable_Object = MibTable
hh3cIfSpeedStatTable = _Hh3cIfSpeedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cIfSpeedStatTable.setStatus("current")
_Hh3cIfSpeedStatEntry_Object = MibTableRow
hh3cIfSpeedStatEntry = _Hh3cIfSpeedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1)
)
hh3cIfSpeedStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfSpeedStatEntry.setStatus("current")
_Hh3cIfSpeedStatInterval_Type = Integer32
_Hh3cIfSpeedStatInterval_Object = MibTableColumn
hh3cIfSpeedStatInterval = _Hh3cIfSpeedStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 1),
    _Hh3cIfSpeedStatInterval_Type()
)
hh3cIfSpeedStatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInterval.setUnits("seconds")
_Hh3cIfSpeedStatInPkts_Type = Unsigned32
_Hh3cIfSpeedStatInPkts_Object = MibTableColumn
hh3cIfSpeedStatInPkts = _Hh3cIfSpeedStatInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 2),
    _Hh3cIfSpeedStatInPkts_Type()
)
hh3cIfSpeedStatInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInPkts.setStatus("current")
_Hh3cIfSpeedStatOutPkts_Type = Unsigned32
_Hh3cIfSpeedStatOutPkts_Object = MibTableColumn
hh3cIfSpeedStatOutPkts = _Hh3cIfSpeedStatOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 3),
    _Hh3cIfSpeedStatOutPkts_Type()
)
hh3cIfSpeedStatOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatOutPkts.setStatus("current")
_Hh3cIfSpeedStatInBytes_Type = Unsigned32
_Hh3cIfSpeedStatInBytes_Object = MibTableColumn
hh3cIfSpeedStatInBytes = _Hh3cIfSpeedStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 4),
    _Hh3cIfSpeedStatInBytes_Type()
)
hh3cIfSpeedStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatInBytes.setStatus("current")
_Hh3cIfSpeedStatOutBytes_Type = Unsigned32
_Hh3cIfSpeedStatOutBytes_Object = MibTableColumn
hh3cIfSpeedStatOutBytes = _Hh3cIfSpeedStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 2, 1, 5),
    _Hh3cIfSpeedStatOutBytes_Type()
)
hh3cIfSpeedStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfSpeedStatOutBytes.setStatus("current")
_Hh3cIfHCFlowStatTable_Object = MibTable
hh3cIfHCFlowStatTable = _Hh3cIfHCFlowStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cIfHCFlowStatTable.setStatus("current")
_Hh3cIfHCFlowStatEntry_Object = MibTableRow
hh3cIfHCFlowStatEntry = _Hh3cIfHCFlowStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1)
)
hh3cIfHCFlowStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfHCFlowStatEntry.setStatus("current")
_Hh3cIfStatFlowHCInBits_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCInBits_Object = MibTableColumn
hh3cIfStatFlowHCInBits = _Hh3cIfStatFlowHCInBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 1),
    _Hh3cIfStatFlowHCInBits_Type()
)
hh3cIfStatFlowHCInBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCInBits.setStatus("current")
_Hh3cIfStatFlowHCOutBits_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCOutBits_Object = MibTableColumn
hh3cIfStatFlowHCOutBits = _Hh3cIfStatFlowHCOutBits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 2),
    _Hh3cIfStatFlowHCOutBits_Type()
)
hh3cIfStatFlowHCOutBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCOutBits.setStatus("current")
_Hh3cIfStatFlowHCInPkts_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCInPkts_Object = MibTableColumn
hh3cIfStatFlowHCInPkts = _Hh3cIfStatFlowHCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 3),
    _Hh3cIfStatFlowHCInPkts_Type()
)
hh3cIfStatFlowHCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCInPkts.setStatus("current")
_Hh3cIfStatFlowHCOutPkts_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCOutPkts_Object = MibTableColumn
hh3cIfStatFlowHCOutPkts = _Hh3cIfStatFlowHCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 4),
    _Hh3cIfStatFlowHCOutPkts_Type()
)
hh3cIfStatFlowHCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCOutPkts.setStatus("current")
_Hh3cIfStatFlowHCInBytes_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCInBytes_Object = MibTableColumn
hh3cIfStatFlowHCInBytes = _Hh3cIfStatFlowHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 5),
    _Hh3cIfStatFlowHCInBytes_Type()
)
hh3cIfStatFlowHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCInBytes.setStatus("current")
_Hh3cIfStatFlowHCOutBytes_Type = CounterBasedGauge64
_Hh3cIfStatFlowHCOutBytes_Object = MibTableColumn
hh3cIfStatFlowHCOutBytes = _Hh3cIfStatFlowHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 1, 2, 3, 1, 6),
    _Hh3cIfStatFlowHCOutBytes_Type()
)
hh3cIfStatFlowHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatFlowHCOutBytes.setStatus("current")
_Hh3cIfControl_ObjectIdentity = ObjectIdentity
hh3cIfControl = _Hh3cIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2)
)
_Hh3cRTParentIfTable_Object = MibTable
hh3cRTParentIfTable = _Hh3cRTParentIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cRTParentIfTable.setStatus("current")
_Hh3cRTParentIfEntry_Object = MibTableRow
hh3cRTParentIfEntry = _Hh3cRTParentIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1)
)
hh3cRTParentIfEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cRTParentIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cRTParentIfEntry.setStatus("current")


class _Hh3cRTParentIfIndex_Type(Integer32):
    """Custom type hh3cRTParentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cRTParentIfIndex_Type.__name__ = "Integer32"
_Hh3cRTParentIfIndex_Object = MibTableColumn
hh3cRTParentIfIndex = _Hh3cRTParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1, 1),
    _Hh3cRTParentIfIndex_Type()
)
hh3cRTParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTParentIfIndex.setStatus("current")
_Hh3cRTMinSubIfOrdinal_Type = Integer32
_Hh3cRTMinSubIfOrdinal_Object = MibTableColumn
hh3cRTMinSubIfOrdinal = _Hh3cRTMinSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1, 2),
    _Hh3cRTMinSubIfOrdinal_Type()
)
hh3cRTMinSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTMinSubIfOrdinal.setStatus("current")
_Hh3cRTMaxSubIfOrdinal_Type = Integer32
_Hh3cRTMaxSubIfOrdinal_Object = MibTableColumn
hh3cRTMaxSubIfOrdinal = _Hh3cRTMaxSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 1, 1, 3),
    _Hh3cRTMaxSubIfOrdinal_Type()
)
hh3cRTMaxSubIfOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTMaxSubIfOrdinal.setStatus("current")
_Hh3cRTSubIfTable_Object = MibTable
hh3cRTSubIfTable = _Hh3cRTSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cRTSubIfTable.setStatus("current")
_Hh3cRTSubIfEntry_Object = MibTableRow
hh3cRTSubIfEntry = _Hh3cRTSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1)
)
hh3cRTSubIfEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cRTSubIfParentIfIndex"),
    (0, "HH3C-IF-EXT-MIB", "hh3cRTSubIfOrdinal"),
)
if mibBuilder.loadTexts:
    hh3cRTSubIfEntry.setStatus("current")


class _Hh3cRTSubIfParentIfIndex_Type(Integer32):
    """Custom type hh3cRTSubIfParentIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cRTSubIfParentIfIndex_Type.__name__ = "Integer32"
_Hh3cRTSubIfParentIfIndex_Object = MibTableColumn
hh3cRTSubIfParentIfIndex = _Hh3cRTSubIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 1),
    _Hh3cRTSubIfParentIfIndex_Type()
)
hh3cRTSubIfParentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTSubIfParentIfIndex.setStatus("current")


class _Hh3cRTSubIfOrdinal_Type(Integer32):
    """Custom type hh3cRTSubIfOrdinal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cRTSubIfOrdinal_Type.__name__ = "Integer32"
_Hh3cRTSubIfOrdinal_Object = MibTableColumn
hh3cRTSubIfOrdinal = _Hh3cRTSubIfOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 2),
    _Hh3cRTSubIfOrdinal_Type()
)
hh3cRTSubIfOrdinal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRTSubIfOrdinal.setStatus("current")
_Hh3cRTSubIfSubIfIndex_Type = Integer32
_Hh3cRTSubIfSubIfIndex_Object = MibTableColumn
hh3cRTSubIfSubIfIndex = _Hh3cRTSubIfSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 3),
    _Hh3cRTSubIfSubIfIndex_Type()
)
hh3cRTSubIfSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTSubIfSubIfIndex.setStatus("current")


class _Hh3cRTSubIfSubIfDesc_Type(DisplayString):
    """Custom type hh3cRTSubIfSubIfDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cRTSubIfSubIfDesc_Type.__name__ = "DisplayString"
_Hh3cRTSubIfSubIfDesc_Object = MibTableColumn
hh3cRTSubIfSubIfDesc = _Hh3cRTSubIfSubIfDesc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 4),
    _Hh3cRTSubIfSubIfDesc_Type()
)
hh3cRTSubIfSubIfDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRTSubIfSubIfDesc.setStatus("current")
_Hh3cRTSubIfRowStatus_Type = RowStatus
_Hh3cRTSubIfRowStatus_Object = MibTableColumn
hh3cRTSubIfRowStatus = _Hh3cRTSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 2, 1, 5),
    _Hh3cRTSubIfRowStatus_Type()
)
hh3cRTSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRTSubIfRowStatus.setStatus("current")
_Hh3cIfLinkModeTable_Object = MibTable
hh3cIfLinkModeTable = _Hh3cIfLinkModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cIfLinkModeTable.setStatus("current")
_Hh3cIfLinkModeEntry_Object = MibTableRow
hh3cIfLinkModeEntry = _Hh3cIfLinkModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1)
)
hh3cIfLinkModeEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cIfLinkModeIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfLinkModeEntry.setStatus("current")


class _Hh3cIfLinkModeIndex_Type(Integer32):
    """Custom type hh3cIfLinkModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIfLinkModeIndex_Type.__name__ = "Integer32"
_Hh3cIfLinkModeIndex_Object = MibTableColumn
hh3cIfLinkModeIndex = _Hh3cIfLinkModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1, 1),
    _Hh3cIfLinkModeIndex_Type()
)
hh3cIfLinkModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfLinkModeIndex.setStatus("current")


class _Hh3cIfLinkMode_Type(Integer32):
    """Custom type hh3cIfLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgeMode", 1),
          ("routeMode", 2))
    )


_Hh3cIfLinkMode_Type.__name__ = "Integer32"
_Hh3cIfLinkMode_Object = MibTableColumn
hh3cIfLinkMode = _Hh3cIfLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1, 2),
    _Hh3cIfLinkMode_Type()
)
hh3cIfLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfLinkMode.setStatus("current")
_Hh3cIfLinkModeSwitchSupport_Type = TruthValue
_Hh3cIfLinkModeSwitchSupport_Object = MibTableColumn
hh3cIfLinkModeSwitchSupport = _Hh3cIfLinkModeSwitchSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 3, 1, 3),
    _Hh3cIfLinkModeSwitchSupport_Type()
)
hh3cIfLinkModeSwitchSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfLinkModeSwitchSupport.setStatus("current")
_Hh3cIfPortTypeTable_Object = MibTable
hh3cIfPortTypeTable = _Hh3cIfPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cIfPortTypeTable.setStatus("current")
_Hh3cIfPortTypeEntry_Object = MibTableRow
hh3cIfPortTypeEntry = _Hh3cIfPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4, 1)
)
hh3cIfPortTypeEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cIfPortTypeIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfPortTypeEntry.setStatus("current")
_Hh3cIfPortTypeIndex_Type = InterfaceIndex
_Hh3cIfPortTypeIndex_Object = MibTableColumn
hh3cIfPortTypeIndex = _Hh3cIfPortTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4, 1, 1),
    _Hh3cIfPortTypeIndex_Type()
)
hh3cIfPortTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfPortTypeIndex.setStatus("current")


class _Hh3cIfPortType_Type(Integer32):
    """Custom type hh3cIfPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ethernet", 2),
          ("fc", 3))
    )


_Hh3cIfPortType_Type.__name__ = "Integer32"
_Hh3cIfPortType_Object = MibTableColumn
hh3cIfPortType = _Hh3cIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 2, 4, 1, 2),
    _Hh3cIfPortType_Type()
)
hh3cIfPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPortType.setStatus("current")
_Hh3cIfInterfaces_ObjectIdentity = ObjectIdentity
hh3cIfInterfaces = _Hh3cIfInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3)
)
_Hh3cIfPhysicalNumber_Type = Integer32
_Hh3cIfPhysicalNumber_Object = MibScalar
hh3cIfPhysicalNumber = _Hh3cIfPhysicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 1),
    _Hh3cIfPhysicalNumber_Type()
)
hh3cIfPhysicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfPhysicalNumber.setStatus("current")
_Hh3cIfTable_Object = MibTable
hh3cIfTable = _Hh3cIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cIfTable.setStatus("current")
_Hh3cIfEntry_Object = MibTableRow
hh3cIfEntry = _Hh3cIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1)
)
hh3cIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfEntry.setStatus("current")
_Hh3cIfUpDownTimes_Type = Integer32
_Hh3cIfUpDownTimes_Object = MibTableColumn
hh3cIfUpDownTimes = _Hh3cIfUpDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 1),
    _Hh3cIfUpDownTimes_Type()
)
hh3cIfUpDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfUpDownTimes.setStatus("current")
_Hh3cIfMtu_Type = Integer32
_Hh3cIfMtu_Object = MibTableColumn
hh3cIfMtu = _Hh3cIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 2),
    _Hh3cIfMtu_Type()
)
hh3cIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfMtu.setStatus("current")


class _Hh3cIfBandwidthRate_Type(Integer32):
    """Custom type hh3cIfBandwidthRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cIfBandwidthRate_Type.__name__ = "Integer32"
_Hh3cIfBandwidthRate_Object = MibTableColumn
hh3cIfBandwidthRate = _Hh3cIfBandwidthRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 3),
    _Hh3cIfBandwidthRate_Type()
)
hh3cIfBandwidthRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfBandwidthRate.setStatus("current")


class _Hh3cIfDiscardPktRate_Type(Integer32):
    """Custom type hh3cIfDiscardPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cIfDiscardPktRate_Type.__name__ = "Integer32"
_Hh3cIfDiscardPktRate_Object = MibTableColumn
hh3cIfDiscardPktRate = _Hh3cIfDiscardPktRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 4),
    _Hh3cIfDiscardPktRate_Type()
)
hh3cIfDiscardPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfDiscardPktRate.setStatus("current")
_Hh3cIfStatusKeepTime_Type = TimeTicks
_Hh3cIfStatusKeepTime_Object = MibTableColumn
hh3cIfStatusKeepTime = _Hh3cIfStatusKeepTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 5),
    _Hh3cIfStatusKeepTime_Type()
)
hh3cIfStatusKeepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfStatusKeepTime.setStatus("current")
_Hh3cIfInNUcastPkts_Type = Counter64
_Hh3cIfInNUcastPkts_Object = MibTableColumn
hh3cIfInNUcastPkts = _Hh3cIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 6),
    _Hh3cIfInNUcastPkts_Type()
)
hh3cIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfInNUcastPkts.setStatus("current")
_Hh3cIfOutNUcastPkts_Type = Counter64
_Hh3cIfOutNUcastPkts_Object = MibTableColumn
hh3cIfOutNUcastPkts = _Hh3cIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 7),
    _Hh3cIfOutNUcastPkts_Type()
)
hh3cIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfOutNUcastPkts.setStatus("current")
_Hh3cIfIsPoe_Type = TruthValue
_Hh3cIfIsPoe_Object = MibTableColumn
hh3cIfIsPoe = _Hh3cIfIsPoe_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 8),
    _Hh3cIfIsPoe_Type()
)
hh3cIfIsPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfIsPoe.setStatus("current")


class _Hh3cIfOperStatus_Type(Integer32):
    """Custom type hh3cIfOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("admindown", 4))
    )


_Hh3cIfOperStatus_Type.__name__ = "Integer32"
_Hh3cIfOperStatus_Object = MibTableColumn
hh3cIfOperStatus = _Hh3cIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 9),
    _Hh3cIfOperStatus_Type()
)
hh3cIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfOperStatus.setStatus("current")
_Hh3cIfDownTimes_Type = Integer32
_Hh3cIfDownTimes_Object = MibTableColumn
hh3cIfDownTimes = _Hh3cIfDownTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 10),
    _Hh3cIfDownTimes_Type()
)
hh3cIfDownTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfDownTimes.setStatus("current")


class _Hh3cIfPfcStatus_Type(Integer32):
    """Custom type hh3cIfPfcStatus based on Integer32"""
    defaultValue = 2

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
          ("auto", 3))
    )


_Hh3cIfPfcStatus_Type.__name__ = "Integer32"
_Hh3cIfPfcStatus_Object = MibTableColumn
hh3cIfPfcStatus = _Hh3cIfPfcStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 11),
    _Hh3cIfPfcStatus_Type()
)
hh3cIfPfcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPfcStatus.setStatus("current")


class _Hh3cIfPfcDot1pNoDrop_Type(Bits):
    """Custom type hh3cIfPfcDot1pNoDrop based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("pri0", 0),
          ("pri1", 1),
          ("pri2", 2),
          ("pri3", 3),
          ("pri4", 4),
          ("pri5", 5),
          ("pri6", 6),
          ("pri7", 7))
    )

_Hh3cIfPfcDot1pNoDrop_Type.__name__ = "Bits"
_Hh3cIfPfcDot1pNoDrop_Object = MibTableColumn
hh3cIfPfcDot1pNoDrop = _Hh3cIfPfcDot1pNoDrop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 2, 1, 12),
    _Hh3cIfPfcDot1pNoDrop_Type()
)
hh3cIfPfcDot1pNoDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfPfcDot1pNoDrop.setStatus("current")
_Hh3cIfUsingTable_Object = MibTable
hh3cIfUsingTable = _Hh3cIfUsingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cIfUsingTable.setStatus("current")
_Hh3cIfUsingEntry_Object = MibTableRow
hh3cIfUsingEntry = _Hh3cIfUsingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1)
)
hh3cIfUsingEntry.setIndexNames(
    (0, "HH3C-IF-EXT-MIB", "hh3cIfUsingIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfUsingEntry.setStatus("current")


class _Hh3cIfUsingIndex_Type(Integer32):
    """Custom type hh3cIfUsingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIfUsingIndex_Type.__name__ = "Integer32"
_Hh3cIfUsingIndex_Object = MibTableColumn
hh3cIfUsingIndex = _Hh3cIfUsingIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 1),
    _Hh3cIfUsingIndex_Type()
)
hh3cIfUsingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIfUsingIndex.setStatus("current")
_Hh3cIfUsingSupportType_Type = Integer32
_Hh3cIfUsingSupportType_Object = MibTableColumn
hh3cIfUsingSupportType = _Hh3cIfUsingSupportType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 2),
    _Hh3cIfUsingSupportType_Type()
)
hh3cIfUsingSupportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfUsingSupportType.setStatus("current")


class _Hh3cIfUsingType_Type(Integer32):
    """Custom type hh3cIfUsingType based on Integer32"""
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
        *(("noUsing", 0),
          ("using10GE", 1),
          ("using20GE", 2),
          ("using40GE", 3),
          ("using100GE", 4))
    )


_Hh3cIfUsingType_Type.__name__ = "Integer32"
_Hh3cIfUsingType_Object = MibTableColumn
hh3cIfUsingType = _Hh3cIfUsingType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 3),
    _Hh3cIfUsingType_Type()
)
hh3cIfUsingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfUsingType.setStatus("current")


class _Hh3cIfUsingStatus_Type(Integer32):
    """Custom type hh3cIfUsingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noUsing", 0),
          ("needReboot", 1))
    )


_Hh3cIfUsingStatus_Type.__name__ = "Integer32"
_Hh3cIfUsingStatus_Object = MibTableColumn
hh3cIfUsingStatus = _Hh3cIfUsingStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 2, 3, 3, 1, 4),
    _Hh3cIfUsingStatus_Type()
)
hh3cIfUsingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIfUsingStatus.setStatus("current")
_Hh3cIfExtTrap_ObjectIdentity = ObjectIdentity
hh3cIfExtTrap = _Hh3cIfExtTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3)
)
_Hh3cIfExtTrapPrex_ObjectIdentity = ObjectIdentity
hh3cIfExtTrapPrex = _Hh3cIfExtTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0)
)
_Hh3cIfExtTrapObject_ObjectIdentity = ObjectIdentity
hh3cIfExtTrapObject = _Hh3cIfExtTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1)
)
_Hh3cIfExtTrapCfgTable_Object = MibTable
hh3cIfExtTrapCfgTable = _Hh3cIfExtTrapCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cIfExtTrapCfgTable.setStatus("current")
_Hh3cIfExtTrapCfgEntry_Object = MibTableRow
hh3cIfExtTrapCfgEntry = _Hh3cIfExtTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1, 1)
)
hh3cIfExtTrapCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cIfExtTrapCfgEntry.setStatus("current")


class _Hh3cIfBandwidthUpperLimit_Type(Integer32):
    """Custom type hh3cIfBandwidthUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cIfBandwidthUpperLimit_Type.__name__ = "Integer32"
_Hh3cIfBandwidthUpperLimit_Object = MibTableColumn
hh3cIfBandwidthUpperLimit = _Hh3cIfBandwidthUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1, 1, 1),
    _Hh3cIfBandwidthUpperLimit_Type()
)
hh3cIfBandwidthUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfBandwidthUpperLimit.setStatus("current")


class _Hh3cIfDiscardPktRateUpperLimit_Type(Integer32):
    """Custom type hh3cIfDiscardPktRateUpperLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cIfDiscardPktRateUpperLimit_Type.__name__ = "Integer32"
_Hh3cIfDiscardPktRateUpperLimit_Object = MibTableColumn
hh3cIfDiscardPktRateUpperLimit = _Hh3cIfDiscardPktRateUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 1, 1, 1, 2),
    _Hh3cIfDiscardPktRateUpperLimit_Type()
)
hh3cIfDiscardPktRateUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIfDiscardPktRateUpperLimit.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cIfBandwidthUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 1)
)
hh3cIfBandwidthUsageHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfBandwidthRate"),
        ("HH3C-IF-EXT-MIB", "hh3cIfBandwidthUpperLimit"))
)
if mibBuilder.loadTexts:
    hh3cIfBandwidthUsageHigh.setStatus(
        "current"
    )

hh3cIfDiscardPktRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 2)
)
hh3cIfDiscardPktRateHigh.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HH3C-IF-EXT-MIB", "hh3cIfDiscardPktRate"),
        ("HH3C-IF-EXT-MIB", "hh3cIfDiscardPktRateUpperLimit"))
)
if mibBuilder.loadTexts:
    hh3cIfDiscardPktRateHigh.setStatus(
        "current"
    )

hh3cIfDampeningSuppressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 3)
)
hh3cIfDampeningSuppressed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cIfDampeningSuppressed.setStatus(
        "current"
    )

hh3cIfDampeningNotSuppressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 40, 3, 0, 4)
)
hh3cIfDampeningNotSuppressed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cIfDampeningNotSuppressed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IF-EXT-MIB",
    **{"hh3cIfExt": hh3cIfExt,
       "hh3cIfExtScalarGroup": hh3cIfExtScalarGroup,
       "hh3cIfStatGlobalFlowInterval": hh3cIfStatGlobalFlowInterval,
       "hh3cIfShutDownInterval": hh3cIfShutDownInterval,
       "hh3cIfExtGroup": hh3cIfExtGroup,
       "hh3cIfStat": hh3cIfStat,
       "hh3cIfStatScalarGroup": hh3cIfStatScalarGroup,
       "hh3cIfStatTable": hh3cIfStatTable,
       "hh3cIfFlowStatTable": hh3cIfFlowStatTable,
       "hh3cIfFlowStatEntry": hh3cIfFlowStatEntry,
       "hh3cIfStatFlowInterval": hh3cIfStatFlowInterval,
       "hh3cIfStatFlowInBits": hh3cIfStatFlowInBits,
       "hh3cIfStatFlowOutBits": hh3cIfStatFlowOutBits,
       "hh3cIfStatFlowInPkts": hh3cIfStatFlowInPkts,
       "hh3cIfStatFlowOutPkts": hh3cIfStatFlowOutPkts,
       "hh3cIfStatFlowInBytes": hh3cIfStatFlowInBytes,
       "hh3cIfStatFlowOutBytes": hh3cIfStatFlowOutBytes,
       "hh3cIfSpeedStatTable": hh3cIfSpeedStatTable,
       "hh3cIfSpeedStatEntry": hh3cIfSpeedStatEntry,
       "hh3cIfSpeedStatInterval": hh3cIfSpeedStatInterval,
       "hh3cIfSpeedStatInPkts": hh3cIfSpeedStatInPkts,
       "hh3cIfSpeedStatOutPkts": hh3cIfSpeedStatOutPkts,
       "hh3cIfSpeedStatInBytes": hh3cIfSpeedStatInBytes,
       "hh3cIfSpeedStatOutBytes": hh3cIfSpeedStatOutBytes,
       "hh3cIfHCFlowStatTable": hh3cIfHCFlowStatTable,
       "hh3cIfHCFlowStatEntry": hh3cIfHCFlowStatEntry,
       "hh3cIfStatFlowHCInBits": hh3cIfStatFlowHCInBits,
       "hh3cIfStatFlowHCOutBits": hh3cIfStatFlowHCOutBits,
       "hh3cIfStatFlowHCInPkts": hh3cIfStatFlowHCInPkts,
       "hh3cIfStatFlowHCOutPkts": hh3cIfStatFlowHCOutPkts,
       "hh3cIfStatFlowHCInBytes": hh3cIfStatFlowHCInBytes,
       "hh3cIfStatFlowHCOutBytes": hh3cIfStatFlowHCOutBytes,
       "hh3cIfControl": hh3cIfControl,
       "hh3cRTParentIfTable": hh3cRTParentIfTable,
       "hh3cRTParentIfEntry": hh3cRTParentIfEntry,
       "hh3cRTParentIfIndex": hh3cRTParentIfIndex,
       "hh3cRTMinSubIfOrdinal": hh3cRTMinSubIfOrdinal,
       "hh3cRTMaxSubIfOrdinal": hh3cRTMaxSubIfOrdinal,
       "hh3cRTSubIfTable": hh3cRTSubIfTable,
       "hh3cRTSubIfEntry": hh3cRTSubIfEntry,
       "hh3cRTSubIfParentIfIndex": hh3cRTSubIfParentIfIndex,
       "hh3cRTSubIfOrdinal": hh3cRTSubIfOrdinal,
       "hh3cRTSubIfSubIfIndex": hh3cRTSubIfSubIfIndex,
       "hh3cRTSubIfSubIfDesc": hh3cRTSubIfSubIfDesc,
       "hh3cRTSubIfRowStatus": hh3cRTSubIfRowStatus,
       "hh3cIfLinkModeTable": hh3cIfLinkModeTable,
       "hh3cIfLinkModeEntry": hh3cIfLinkModeEntry,
       "hh3cIfLinkModeIndex": hh3cIfLinkModeIndex,
       "hh3cIfLinkMode": hh3cIfLinkMode,
       "hh3cIfLinkModeSwitchSupport": hh3cIfLinkModeSwitchSupport,
       "hh3cIfPortTypeTable": hh3cIfPortTypeTable,
       "hh3cIfPortTypeEntry": hh3cIfPortTypeEntry,
       "hh3cIfPortTypeIndex": hh3cIfPortTypeIndex,
       "hh3cIfPortType": hh3cIfPortType,
       "hh3cIfInterfaces": hh3cIfInterfaces,
       "hh3cIfPhysicalNumber": hh3cIfPhysicalNumber,
       "hh3cIfTable": hh3cIfTable,
       "hh3cIfEntry": hh3cIfEntry,
       "hh3cIfUpDownTimes": hh3cIfUpDownTimes,
       "hh3cIfMtu": hh3cIfMtu,
       "hh3cIfBandwidthRate": hh3cIfBandwidthRate,
       "hh3cIfDiscardPktRate": hh3cIfDiscardPktRate,
       "hh3cIfStatusKeepTime": hh3cIfStatusKeepTime,
       "hh3cIfInNUcastPkts": hh3cIfInNUcastPkts,
       "hh3cIfOutNUcastPkts": hh3cIfOutNUcastPkts,
       "hh3cIfIsPoe": hh3cIfIsPoe,
       "hh3cIfOperStatus": hh3cIfOperStatus,
       "hh3cIfDownTimes": hh3cIfDownTimes,
       "hh3cIfPfcStatus": hh3cIfPfcStatus,
       "hh3cIfPfcDot1pNoDrop": hh3cIfPfcDot1pNoDrop,
       "hh3cIfUsingTable": hh3cIfUsingTable,
       "hh3cIfUsingEntry": hh3cIfUsingEntry,
       "hh3cIfUsingIndex": hh3cIfUsingIndex,
       "hh3cIfUsingSupportType": hh3cIfUsingSupportType,
       "hh3cIfUsingType": hh3cIfUsingType,
       "hh3cIfUsingStatus": hh3cIfUsingStatus,
       "hh3cIfExtTrap": hh3cIfExtTrap,
       "hh3cIfExtTrapPrex": hh3cIfExtTrapPrex,
       "hh3cIfBandwidthUsageHigh": hh3cIfBandwidthUsageHigh,
       "hh3cIfDiscardPktRateHigh": hh3cIfDiscardPktRateHigh,
       "hh3cIfDampeningSuppressed": hh3cIfDampeningSuppressed,
       "hh3cIfDampeningNotSuppressed": hh3cIfDampeningNotSuppressed,
       "hh3cIfExtTrapObject": hh3cIfExtTrapObject,
       "hh3cIfExtTrapCfgTable": hh3cIfExtTrapCfgTable,
       "hh3cIfExtTrapCfgEntry": hh3cIfExtTrapCfgEntry,
       "hh3cIfBandwidthUpperLimit": hh3cIfBandwidthUpperLimit,
       "hh3cIfDiscardPktRateUpperLimit": hh3cIfDiscardPktRateUpperLimit}
)
