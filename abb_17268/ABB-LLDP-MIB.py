# SNMP MIB module (ABB-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/abb_17268/ABB-LLDP-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:23:57 2025
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

(hmConfiguration,) = mibBuilder.importSymbols(
    "ABB-PRIVATE-MIB",
    "hmConfiguration")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hmLLDP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7)
)
if mibBuilder.loadTexts:
    hmLLDP.setRevisions(
        ("2004-11-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmLLDPConfig_ObjectIdentity = ObjectIdentity
hmLLDPConfig = _HmLLDPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1)
)


class _HmLLDPAdminStatus_Type(Integer32):
    """Custom type hmLLDPAdminStatus based on Integer32"""
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


_HmLLDPAdminStatus_Type.__name__ = "Integer32"
_HmLLDPAdminStatus_Object = MibScalar
hmLLDPAdminStatus = _HmLLDPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 1),
    _HmLLDPAdminStatus_Type()
)
hmLLDPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmLLDPAdminStatus.setStatus("current")
_HmLLDPInterfaceTable_Object = MibTable
hmLLDPInterfaceTable = _HmLLDPInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2)
)
if mibBuilder.loadTexts:
    hmLLDPInterfaceTable.setStatus("current")
_HmLLDPIfEntry_Object = MibTableRow
hmLLDPIfEntry = _HmLLDPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2, 1)
)
hmLLDPIfEntry.setIndexNames(
    (0, "ABB-LLDP-MIB", "hmLLDPIfaceGroupID"),
    (0, "ABB-LLDP-MIB", "hmLLDPIfaceID"),
)
if mibBuilder.loadTexts:
    hmLLDPIfEntry.setStatus("current")


class _HmLLDPIfaceGroupID_Type(Integer32):
    """Custom type hmLLDPIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmLLDPIfaceGroupID_Type.__name__ = "Integer32"
_HmLLDPIfaceGroupID_Object = MibTableColumn
hmLLDPIfaceGroupID = _HmLLDPIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2, 1, 1),
    _HmLLDPIfaceGroupID_Type()
)
hmLLDPIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPIfaceGroupID.setStatus("current")


class _HmLLDPIfaceID_Type(Integer32):
    """Custom type hmLLDPIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HmLLDPIfaceID_Type.__name__ = "Integer32"
_HmLLDPIfaceID_Object = MibTableColumn
hmLLDPIfaceID = _HmLLDPIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2, 1, 2),
    _HmLLDPIfaceID_Type()
)
hmLLDPIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPIfaceID.setStatus("current")


class _HmLLDPIfaceHirmaMode_Type(Integer32):
    """Custom type hmLLDPIfaceHirmaMode based on Integer32"""
    defaultValue = 3

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
        *(("txOnly", 1),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("disabled", 4))
    )


_HmLLDPIfaceHirmaMode_Type.__name__ = "Integer32"
_HmLLDPIfaceHirmaMode_Object = MibTableColumn
hmLLDPIfaceHirmaMode = _HmLLDPIfaceHirmaMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2, 1, 3),
    _HmLLDPIfaceHirmaMode_Type()
)
hmLLDPIfaceHirmaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmLLDPIfaceHirmaMode.setStatus("current")


class _HmLLDPIfaceFDBMode_Type(Integer32):
    """Custom type hmLLDPIfaceFDBMode based on Integer32"""
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
        *(("lldpOnly", 1),
          ("macOnly", 2),
          ("both", 3),
          ("autoDetect", 4))
    )


_HmLLDPIfaceFDBMode_Type.__name__ = "Integer32"
_HmLLDPIfaceFDBMode_Object = MibTableColumn
hmLLDPIfaceFDBMode = _HmLLDPIfaceFDBMode_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2, 1, 4),
    _HmLLDPIfaceFDBMode_Type()
)
hmLLDPIfaceFDBMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmLLDPIfaceFDBMode.setStatus("current")


class _HmLLDPIfaceMaxNeighbors_Type(Integer32):
    """Custom type hmLLDPIfaceMaxNeighbors based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_HmLLDPIfaceMaxNeighbors_Type.__name__ = "Integer32"
_HmLLDPIfaceMaxNeighbors_Object = MibTableColumn
hmLLDPIfaceMaxNeighbors = _HmLLDPIfaceMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 1, 2, 1, 5),
    _HmLLDPIfaceMaxNeighbors_Type()
)
hmLLDPIfaceMaxNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmLLDPIfaceMaxNeighbors.setStatus("current")
_HmLLDPStatistics_ObjectIdentity = ObjectIdentity
hmLLDPStatistics = _HmLLDPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2)
)
_HmLLDPStatsIfTable_Object = MibTable
hmLLDPStatsIfTable = _HmLLDPStatsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hmLLDPStatsIfTable.setStatus("current")
_HmLLDPStatsIfEntry_Object = MibTableRow
hmLLDPStatsIfEntry = _HmLLDPStatsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1)
)
hmLLDPStatsIfEntry.setIndexNames(
    (0, "ABB-LLDP-MIB", "hmLLDPStatsIfaceGroupID"),
    (0, "ABB-LLDP-MIB", "hmLLDPStatsIfaceID"),
)
if mibBuilder.loadTexts:
    hmLLDPStatsIfEntry.setStatus("current")


class _HmLLDPStatsIfaceGroupID_Type(Integer32):
    """Custom type hmLLDPStatsIfaceGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HmLLDPStatsIfaceGroupID_Type.__name__ = "Integer32"
_HmLLDPStatsIfaceGroupID_Object = MibTableColumn
hmLLDPStatsIfaceGroupID = _HmLLDPStatsIfaceGroupID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 1),
    _HmLLDPStatsIfaceGroupID_Type()
)
hmLLDPStatsIfaceGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceGroupID.setStatus("current")


class _HmLLDPStatsIfaceID_Type(Integer32):
    """Custom type hmLLDPStatsIfaceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HmLLDPStatsIfaceID_Type.__name__ = "Integer32"
_HmLLDPStatsIfaceID_Object = MibTableColumn
hmLLDPStatsIfaceID = _HmLLDPStatsIfaceID_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 2),
    _HmLLDPStatsIfaceID_Type()
)
hmLLDPStatsIfaceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceID.setStatus("current")
_HmLLDPStatsIfaceTotalFDBEntryCount_Type = Counter32
_HmLLDPStatsIfaceTotalFDBEntryCount_Object = MibTableColumn
hmLLDPStatsIfaceTotalFDBEntryCount = _HmLLDPStatsIfaceTotalFDBEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 3),
    _HmLLDPStatsIfaceTotalFDBEntryCount_Type()
)
hmLLDPStatsIfaceTotalFDBEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceTotalFDBEntryCount.setStatus("current")
_HmLLDPStatsIfaceTotalEntryCount_Type = Counter32
_HmLLDPStatsIfaceTotalEntryCount_Object = MibTableColumn
hmLLDPStatsIfaceTotalEntryCount = _HmLLDPStatsIfaceTotalEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 4),
    _HmLLDPStatsIfaceTotalEntryCount_Type()
)
hmLLDPStatsIfaceTotalEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceTotalEntryCount.setStatus("current")
_HmLLDPStatsIfaceIEEEEntryCount_Type = Counter32
_HmLLDPStatsIfaceIEEEEntryCount_Object = MibTableColumn
hmLLDPStatsIfaceIEEEEntryCount = _HmLLDPStatsIfaceIEEEEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 5),
    _HmLLDPStatsIfaceIEEEEntryCount_Type()
)
hmLLDPStatsIfaceIEEEEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceIEEEEntryCount.setStatus("current")
_HmLLDPStatsIfaceHirmaEntryCount_Type = Counter32
_HmLLDPStatsIfaceHirmaEntryCount_Object = MibTableColumn
hmLLDPStatsIfaceHirmaEntryCount = _HmLLDPStatsIfaceHirmaEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 6),
    _HmLLDPStatsIfaceHirmaEntryCount_Type()
)
hmLLDPStatsIfaceHirmaEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceHirmaEntryCount.setStatus("current")
_HmLLDPStatsIfaceFDBEntryCount_Type = Counter32
_HmLLDPStatsIfaceFDBEntryCount_Object = MibTableColumn
hmLLDPStatsIfaceFDBEntryCount = _HmLLDPStatsIfaceFDBEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 17268, 2818, 6, 14, 7, 2, 1, 1, 7),
    _HmLLDPStatsIfaceFDBEntryCount_Type()
)
hmLLDPStatsIfaceFDBEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmLLDPStatsIfaceFDBEntryCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ABB-LLDP-MIB",
    **{"hmLLDP": hmLLDP,
       "hmLLDPConfig": hmLLDPConfig,
       "hmLLDPAdminStatus": hmLLDPAdminStatus,
       "hmLLDPInterfaceTable": hmLLDPInterfaceTable,
       "hmLLDPIfEntry": hmLLDPIfEntry,
       "hmLLDPIfaceGroupID": hmLLDPIfaceGroupID,
       "hmLLDPIfaceID": hmLLDPIfaceID,
       "hmLLDPIfaceHirmaMode": hmLLDPIfaceHirmaMode,
       "hmLLDPIfaceFDBMode": hmLLDPIfaceFDBMode,
       "hmLLDPIfaceMaxNeighbors": hmLLDPIfaceMaxNeighbors,
       "hmLLDPStatistics": hmLLDPStatistics,
       "hmLLDPStatsIfTable": hmLLDPStatsIfTable,
       "hmLLDPStatsIfEntry": hmLLDPStatsIfEntry,
       "hmLLDPStatsIfaceGroupID": hmLLDPStatsIfaceGroupID,
       "hmLLDPStatsIfaceID": hmLLDPStatsIfaceID,
       "hmLLDPStatsIfaceTotalFDBEntryCount": hmLLDPStatsIfaceTotalFDBEntryCount,
       "hmLLDPStatsIfaceTotalEntryCount": hmLLDPStatsIfaceTotalEntryCount,
       "hmLLDPStatsIfaceIEEEEntryCount": hmLLDPStatsIfaceIEEEEntryCount,
       "hmLLDPStatsIfaceHirmaEntryCount": hmLLDPStatsIfaceHirmaEntryCount,
       "hmLLDPStatsIfaceFDBEntryCount": hmLLDPStatsIfaceFDBEntryCount}
)
