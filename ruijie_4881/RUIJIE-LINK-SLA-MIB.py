# SNMP MIB module (RUIJIE-LINK-SLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-LINK-SLA-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ruijieSLAMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163)
)
if mibBuilder.loadTexts:
    ruijieSLAMonitor.setRevisions(
        ("2019-06-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieSLAObjects_ObjectIdentity = ObjectIdentity
ruijieSLAObjects = _RuijieSLAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1)
)
_RuijieSLATable_Object = MibTable
ruijieSLATable = _RuijieSLATable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieSLATable.setStatus("current")
_RuijieSLAEntry_Object = MibTableRow
ruijieSLAEntry = _RuijieSLAEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1)
)
ruijieSLAEntry.setIndexNames(
    (0, "RUIJIE-LINK-SLA-MIB", "ruijieSLARnsId"),
)
if mibBuilder.loadTexts:
    ruijieSLAEntry.setStatus("current")


class _RuijieSLARnsId_Type(Integer32):
    """Custom type ruijieSLARnsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_RuijieSLARnsId_Type.__name__ = "Integer32"
_RuijieSLARnsId_Object = MibTableColumn
ruijieSLARnsId = _RuijieSLARnsId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 1),
    _RuijieSLARnsId_Type()
)
ruijieSLARnsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLARnsId.setStatus("current")
_RuijieSLAIntfName_Type = DisplayString
_RuijieSLAIntfName_Object = MibTableColumn
ruijieSLAIntfName = _RuijieSLAIntfName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 2),
    _RuijieSLAIntfName_Type()
)
ruijieSLAIntfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLAIntfName.setStatus("current")
_RuijieSLAIPAddr_Type = IpAddress
_RuijieSLAIPAddr_Object = MibTableColumn
ruijieSLAIPAddr = _RuijieSLAIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 3),
    _RuijieSLAIPAddr_Type()
)
ruijieSLAIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLAIPAddr.setStatus("current")


class _RuijieSLALinkState_Type(Integer32):
    """Custom type ruijieSLALinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_RuijieSLALinkState_Type.__name__ = "Integer32"
_RuijieSLALinkState_Object = MibTableColumn
ruijieSLALinkState = _RuijieSLALinkState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 4),
    _RuijieSLALinkState_Type()
)
ruijieSLALinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLALinkState.setStatus("current")


class _RuijieSLALinkDelay_Type(Integer32):
    """Custom type ruijieSLALinkDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RuijieSLALinkDelay_Type.__name__ = "Integer32"
_RuijieSLALinkDelay_Object = MibTableColumn
ruijieSLALinkDelay = _RuijieSLALinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 5),
    _RuijieSLALinkDelay_Type()
)
ruijieSLALinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLALinkDelay.setStatus("current")


class _RuijieSLALinkDropRate_Type(Integer32):
    """Custom type ruijieSLALinkDropRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RuijieSLALinkDropRate_Type.__name__ = "Integer32"
_RuijieSLALinkDropRate_Object = MibTableColumn
ruijieSLALinkDropRate = _RuijieSLALinkDropRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 6),
    _RuijieSLALinkDropRate_Type()
)
ruijieSLALinkDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLALinkDropRate.setStatus("current")
_RuijieSLAIntfTxByteCount_Type = Counter64
_RuijieSLAIntfTxByteCount_Object = MibTableColumn
ruijieSLAIntfTxByteCount = _RuijieSLAIntfTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 7),
    _RuijieSLAIntfTxByteCount_Type()
)
ruijieSLAIntfTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLAIntfTxByteCount.setStatus("current")
_RuijieSLAIntfRxByteCount_Type = Counter64
_RuijieSLAIntfRxByteCount_Object = MibTableColumn
ruijieSLAIntfRxByteCount = _RuijieSLAIntfRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 8),
    _RuijieSLAIntfRxByteCount_Type()
)
ruijieSLAIntfRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLAIntfRxByteCount.setStatus("current")


class _RuijieSLALinkByteUsedRate_Type(Integer32):
    """Custom type ruijieSLALinkByteUsedRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RuijieSLALinkByteUsedRate_Type.__name__ = "Integer32"
_RuijieSLALinkByteUsedRate_Object = MibTableColumn
ruijieSLALinkByteUsedRate = _RuijieSLALinkByteUsedRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 1, 1, 9),
    _RuijieSLALinkByteUsedRate_Type()
)
ruijieSLALinkByteUsedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieSLALinkByteUsedRate.setStatus("current")
_RuijieSLATrap_ObjectIdentity = ObjectIdentity
ruijieSLATrap = _RuijieSLATrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 2)
)
_RuijieSLANotifications_ObjectIdentity = ObjectIdentity
ruijieSLANotifications = _RuijieSLANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 2, 1)
)

# Managed Objects groups


# Notification objects

ruijieSLASignalThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 163, 1, 2, 1, 1)
)
ruijieSLASignalThreshold.setObjects(
      *(("RUIJIE-LINK-SLA-MIB", "ruijieSLAIntfName"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLAIPAddr"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLALinkState"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLALinkDelay"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLALinkDropRate"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLAIntfTxByteCount"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLAIntfRxByteCount"),
        ("RUIJIE-LINK-SLA-MIB", "ruijieSLALinkByteUsedRate"))
)
if mibBuilder.loadTexts:
    ruijieSLASignalThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-LINK-SLA-MIB",
    **{"ruijieSLAMonitor": ruijieSLAMonitor,
       "ruijieSLAObjects": ruijieSLAObjects,
       "ruijieSLATable": ruijieSLATable,
       "ruijieSLAEntry": ruijieSLAEntry,
       "ruijieSLARnsId": ruijieSLARnsId,
       "ruijieSLAIntfName": ruijieSLAIntfName,
       "ruijieSLAIPAddr": ruijieSLAIPAddr,
       "ruijieSLALinkState": ruijieSLALinkState,
       "ruijieSLALinkDelay": ruijieSLALinkDelay,
       "ruijieSLALinkDropRate": ruijieSLALinkDropRate,
       "ruijieSLAIntfTxByteCount": ruijieSLAIntfTxByteCount,
       "ruijieSLAIntfRxByteCount": ruijieSLAIntfRxByteCount,
       "ruijieSLALinkByteUsedRate": ruijieSLALinkByteUsedRate,
       "ruijieSLATrap": ruijieSLATrap,
       "ruijieSLANotifications": ruijieSLANotifications,
       "ruijieSLASignalThreshold": ruijieSLASignalThreshold}
)
