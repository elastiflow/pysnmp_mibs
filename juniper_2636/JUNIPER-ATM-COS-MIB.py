# SNMP MIB module (JUNIPER-ATM-COS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-ATM-COS-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:48:42 2025
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

(atmVclVci,
 atmVclVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(jnxCosFcId,) = mibBuilder.importSymbols(
    "JUNIPER-COS-MIB",
    "jnxCosFcId")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxAtmCos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21)
)
if mibBuilder.loadTexts:
    jnxAtmCos.setRevisions(
        ("2003-09-17 00:00",
         "2003-06-20 00:00",
         "2002-09-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxCosAtmVcTable_Object = MibTable
jnxCosAtmVcTable = _JnxCosAtmVcTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 1)
)
if mibBuilder.loadTexts:
    jnxCosAtmVcTable.setStatus("current")
_JnxCosAtmVcEntry_Object = MibTableRow
jnxCosAtmVcEntry = _JnxCosAtmVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 1, 1)
)
jnxCosAtmVcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    jnxCosAtmVcEntry.setStatus("current")


class _JnxCosAtmVcCosMode_Type(Integer32):
    """Custom type jnxCosAtmVcCosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strict", 0),
          ("alternate", 1))
    )


_JnxCosAtmVcCosMode_Type.__name__ = "Integer32"
_JnxCosAtmVcCosMode_Object = MibTableColumn
jnxCosAtmVcCosMode = _JnxCosAtmVcCosMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 1, 1, 1),
    _JnxCosAtmVcCosMode_Type()
)
jnxCosAtmVcCosMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcCosMode.setStatus("current")
_JnxCosAtmVcScTable_Object = MibTable
jnxCosAtmVcScTable = _JnxCosAtmVcScTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2)
)
if mibBuilder.loadTexts:
    jnxCosAtmVcScTable.setStatus("current")
_JnxCosAtmVcScEntry_Object = MibTableRow
jnxCosAtmVcScEntry = _JnxCosAtmVcScEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1)
)
jnxCosAtmVcScEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "JUNIPER-COS-MIB", "jnxCosFcId"),
)
if mibBuilder.loadTexts:
    jnxCosAtmVcScEntry.setStatus("current")


class _JnxCosAtmVcScPriority_Type(Integer32):
    """Custom type jnxCosAtmVcScPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_JnxCosAtmVcScPriority_Type.__name__ = "Integer32"
_JnxCosAtmVcScPriority_Object = MibTableColumn
jnxCosAtmVcScPriority = _JnxCosAtmVcScPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 1),
    _JnxCosAtmVcScPriority_Type()
)
jnxCosAtmVcScPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScPriority.setStatus("current")


class _JnxCosAtmVcScTxWeightType_Type(Integer32):
    """Custom type jnxCosAtmVcScTxWeightType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cells", 0),
          ("percent", 1))
    )


_JnxCosAtmVcScTxWeightType_Type.__name__ = "Integer32"
_JnxCosAtmVcScTxWeightType_Object = MibTableColumn
jnxCosAtmVcScTxWeightType = _JnxCosAtmVcScTxWeightType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 2),
    _JnxCosAtmVcScTxWeightType_Type()
)
jnxCosAtmVcScTxWeightType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScTxWeightType.setStatus("current")


class _JnxCosAtmVcScTxWeight_Type(Integer32):
    """Custom type jnxCosAtmVcScTxWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_JnxCosAtmVcScTxWeight_Type.__name__ = "Integer32"
_JnxCosAtmVcScTxWeight_Object = MibTableColumn
jnxCosAtmVcScTxWeight = _JnxCosAtmVcScTxWeight_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 3),
    _JnxCosAtmVcScTxWeight_Type()
)
jnxCosAtmVcScTxWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScTxWeight.setStatus("current")


class _JnxCosAtmVcScDpType_Type(Integer32):
    """Custom type jnxCosAtmVcScDpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linearRed", 0),
          ("epd", 1))
    )


_JnxCosAtmVcScDpType_Type.__name__ = "Integer32"
_JnxCosAtmVcScDpType_Object = MibTableColumn
jnxCosAtmVcScDpType = _JnxCosAtmVcScDpType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 4),
    _JnxCosAtmVcScDpType_Type()
)
jnxCosAtmVcScDpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScDpType.setStatus("current")


class _JnxCosAtmVcScLrdpQueueDepth_Type(Integer32):
    """Custom type jnxCosAtmVcScLrdpQueueDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_JnxCosAtmVcScLrdpQueueDepth_Type.__name__ = "Integer32"
_JnxCosAtmVcScLrdpQueueDepth_Object = MibTableColumn
jnxCosAtmVcScLrdpQueueDepth = _JnxCosAtmVcScLrdpQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 5),
    _JnxCosAtmVcScLrdpQueueDepth_Type()
)
jnxCosAtmVcScLrdpQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScLrdpQueueDepth.setStatus("current")


class _JnxCosAtmVcScLrdpLowPlpThresh_Type(Integer32):
    """Custom type jnxCosAtmVcScLrdpLowPlpThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_JnxCosAtmVcScLrdpLowPlpThresh_Type.__name__ = "Integer32"
_JnxCosAtmVcScLrdpLowPlpThresh_Object = MibTableColumn
jnxCosAtmVcScLrdpLowPlpThresh = _JnxCosAtmVcScLrdpLowPlpThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 6),
    _JnxCosAtmVcScLrdpLowPlpThresh_Type()
)
jnxCosAtmVcScLrdpLowPlpThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScLrdpLowPlpThresh.setStatus("current")


class _JnxCosAtmVcScLrdpHighPlpThresh_Type(Integer32):
    """Custom type jnxCosAtmVcScLrdpHighPlpThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_JnxCosAtmVcScLrdpHighPlpThresh_Type.__name__ = "Integer32"
_JnxCosAtmVcScLrdpHighPlpThresh_Object = MibTableColumn
jnxCosAtmVcScLrdpHighPlpThresh = _JnxCosAtmVcScLrdpHighPlpThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 7),
    _JnxCosAtmVcScLrdpHighPlpThresh_Type()
)
jnxCosAtmVcScLrdpHighPlpThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcScLrdpHighPlpThresh.setStatus("current")


class _JnxCosAtmVcEpdThreshold_Type(Integer32):
    """Custom type jnxCosAtmVcEpdThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_JnxCosAtmVcEpdThreshold_Type.__name__ = "Integer32"
_JnxCosAtmVcEpdThreshold_Object = MibTableColumn
jnxCosAtmVcEpdThreshold = _JnxCosAtmVcEpdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 2, 1, 8),
    _JnxCosAtmVcEpdThreshold_Type()
)
jnxCosAtmVcEpdThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcEpdThreshold.setStatus("current")
_JnxCosAtmVcQstatsTable_Object = MibTable
jnxCosAtmVcQstatsTable = _JnxCosAtmVcQstatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3)
)
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsTable.setStatus("current")
_JnxCosAtmVcQstatsEntry_Object = MibTableRow
jnxCosAtmVcQstatsEntry = _JnxCosAtmVcQstatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1)
)
jnxCosAtmVcQstatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "JUNIPER-COS-MIB", "jnxCosFcId"),
)
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsEntry.setStatus("current")
_JnxCosAtmVcQstatsOutPackets_Type = Counter64
_JnxCosAtmVcQstatsOutPackets_Object = MibTableColumn
jnxCosAtmVcQstatsOutPackets = _JnxCosAtmVcQstatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 1),
    _JnxCosAtmVcQstatsOutPackets_Type()
)
jnxCosAtmVcQstatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutPackets.setStatus("current")
_JnxCosAtmVcQstatsOutBytes_Type = Counter64
_JnxCosAtmVcQstatsOutBytes_Object = MibTableColumn
jnxCosAtmVcQstatsOutBytes = _JnxCosAtmVcQstatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 2),
    _JnxCosAtmVcQstatsOutBytes_Type()
)
jnxCosAtmVcQstatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutBytes.setStatus("current")
_JnxCosAtmVcQstatsOutRedDropPkts_Type = Counter64
_JnxCosAtmVcQstatsOutRedDropPkts_Object = MibTableColumn
jnxCosAtmVcQstatsOutRedDropPkts = _JnxCosAtmVcQstatsOutRedDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 3),
    _JnxCosAtmVcQstatsOutRedDropPkts_Type()
)
jnxCosAtmVcQstatsOutRedDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutRedDropPkts.setStatus("current")
_JnxCosAtmVcQstatsOutNonRedDrops_Type = Counter64
_JnxCosAtmVcQstatsOutNonRedDrops_Object = MibTableColumn
jnxCosAtmVcQstatsOutNonRedDrops = _JnxCosAtmVcQstatsOutNonRedDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 4),
    _JnxCosAtmVcQstatsOutNonRedDrops_Type()
)
jnxCosAtmVcQstatsOutNonRedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutNonRedDrops.setStatus("current")
_JnxCosAtmVcQstatsOutLpBytes_Type = Counter64
_JnxCosAtmVcQstatsOutLpBytes_Object = MibTableColumn
jnxCosAtmVcQstatsOutLpBytes = _JnxCosAtmVcQstatsOutLpBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 5),
    _JnxCosAtmVcQstatsOutLpBytes_Type()
)
jnxCosAtmVcQstatsOutLpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutLpBytes.setStatus("current")
_JnxCosAtmVcQstatsOutLpPkts_Type = Counter64
_JnxCosAtmVcQstatsOutLpPkts_Object = MibTableColumn
jnxCosAtmVcQstatsOutLpPkts = _JnxCosAtmVcQstatsOutLpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 6),
    _JnxCosAtmVcQstatsOutLpPkts_Type()
)
jnxCosAtmVcQstatsOutLpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutLpPkts.setStatus("current")
_JnxCosAtmVcQstatsOutLpDropBytes_Type = Counter64
_JnxCosAtmVcQstatsOutLpDropBytes_Object = MibTableColumn
jnxCosAtmVcQstatsOutLpDropBytes = _JnxCosAtmVcQstatsOutLpDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 7),
    _JnxCosAtmVcQstatsOutLpDropBytes_Type()
)
jnxCosAtmVcQstatsOutLpDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutLpDropBytes.setStatus("current")
_JnxCosAtmVcQstatsOutHpDropBytes_Type = Counter64
_JnxCosAtmVcQstatsOutHpDropBytes_Object = MibTableColumn
jnxCosAtmVcQstatsOutHpDropBytes = _JnxCosAtmVcQstatsOutHpDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 8),
    _JnxCosAtmVcQstatsOutHpDropBytes_Type()
)
jnxCosAtmVcQstatsOutHpDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutHpDropBytes.setStatus("current")
_JnxCosAtmVcQstatsOutLpDropPkts_Type = Counter64
_JnxCosAtmVcQstatsOutLpDropPkts_Object = MibTableColumn
jnxCosAtmVcQstatsOutLpDropPkts = _JnxCosAtmVcQstatsOutLpDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 9),
    _JnxCosAtmVcQstatsOutLpDropPkts_Type()
)
jnxCosAtmVcQstatsOutLpDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutLpDropPkts.setStatus("current")
_JnxCosAtmVcQstatsOutHpDropPkts_Type = Counter64
_JnxCosAtmVcQstatsOutHpDropPkts_Object = MibTableColumn
jnxCosAtmVcQstatsOutHpDropPkts = _JnxCosAtmVcQstatsOutHpDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 21, 3, 1, 10),
    _JnxCosAtmVcQstatsOutHpDropPkts_Type()
)
jnxCosAtmVcQstatsOutHpDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxCosAtmVcQstatsOutHpDropPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-ATM-COS-MIB",
    **{"jnxAtmCos": jnxAtmCos,
       "jnxCosAtmVcTable": jnxCosAtmVcTable,
       "jnxCosAtmVcEntry": jnxCosAtmVcEntry,
       "jnxCosAtmVcCosMode": jnxCosAtmVcCosMode,
       "jnxCosAtmVcScTable": jnxCosAtmVcScTable,
       "jnxCosAtmVcScEntry": jnxCosAtmVcScEntry,
       "jnxCosAtmVcScPriority": jnxCosAtmVcScPriority,
       "jnxCosAtmVcScTxWeightType": jnxCosAtmVcScTxWeightType,
       "jnxCosAtmVcScTxWeight": jnxCosAtmVcScTxWeight,
       "jnxCosAtmVcScDpType": jnxCosAtmVcScDpType,
       "jnxCosAtmVcScLrdpQueueDepth": jnxCosAtmVcScLrdpQueueDepth,
       "jnxCosAtmVcScLrdpLowPlpThresh": jnxCosAtmVcScLrdpLowPlpThresh,
       "jnxCosAtmVcScLrdpHighPlpThresh": jnxCosAtmVcScLrdpHighPlpThresh,
       "jnxCosAtmVcEpdThreshold": jnxCosAtmVcEpdThreshold,
       "jnxCosAtmVcQstatsTable": jnxCosAtmVcQstatsTable,
       "jnxCosAtmVcQstatsEntry": jnxCosAtmVcQstatsEntry,
       "jnxCosAtmVcQstatsOutPackets": jnxCosAtmVcQstatsOutPackets,
       "jnxCosAtmVcQstatsOutBytes": jnxCosAtmVcQstatsOutBytes,
       "jnxCosAtmVcQstatsOutRedDropPkts": jnxCosAtmVcQstatsOutRedDropPkts,
       "jnxCosAtmVcQstatsOutNonRedDrops": jnxCosAtmVcQstatsOutNonRedDrops,
       "jnxCosAtmVcQstatsOutLpBytes": jnxCosAtmVcQstatsOutLpBytes,
       "jnxCosAtmVcQstatsOutLpPkts": jnxCosAtmVcQstatsOutLpPkts,
       "jnxCosAtmVcQstatsOutLpDropBytes": jnxCosAtmVcQstatsOutLpDropBytes,
       "jnxCosAtmVcQstatsOutHpDropBytes": jnxCosAtmVcQstatsOutHpDropBytes,
       "jnxCosAtmVcQstatsOutLpDropPkts": jnxCosAtmVcQstatsOutLpDropPkts,
       "jnxCosAtmVcQstatsOutHpDropPkts": jnxCosAtmVcQstatsOutHpDropPkts}
)
