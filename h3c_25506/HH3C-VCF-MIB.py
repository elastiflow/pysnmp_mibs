# SNMP MIB module (HH3C-VCF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-VCF-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:44:13 2025
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

(entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hh3cVcf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129)
)
if mibBuilder.loadTexts:
    hh3cVcf.setRevisions(
        ("2012-11-12 11:29",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVcfSpecInfo_ObjectIdentity = ObjectIdentity
hh3cVcfSpecInfo = _Hh3cVcfSpecInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1)
)
_Hh3cVcfPortMinId_Type = Integer32
_Hh3cVcfPortMinId_Object = MibScalar
hh3cVcfPortMinId = _Hh3cVcfPortMinId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 1),
    _Hh3cVcfPortMinId_Type()
)
hh3cVcfPortMinId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfPortMinId.setStatus("current")
_Hh3cVcfPortMaxId_Type = Integer32
_Hh3cVcfPortMaxId_Object = MibScalar
hh3cVcfPortMaxId = _Hh3cVcfPortMaxId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 2),
    _Hh3cVcfPortMaxId_Type()
)
hh3cVcfPortMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfPortMaxId.setStatus("current")
_Hh3cVcfMinVirtualSlot_Type = Integer32
_Hh3cVcfMinVirtualSlot_Object = MibScalar
hh3cVcfMinVirtualSlot = _Hh3cVcfMinVirtualSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 3),
    _Hh3cVcfMinVirtualSlot_Type()
)
hh3cVcfMinVirtualSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfMinVirtualSlot.setStatus("current")
_Hh3cVcfMaxVirtualSlot_Type = Integer32
_Hh3cVcfMaxVirtualSlot_Object = MibScalar
hh3cVcfMaxVirtualSlot = _Hh3cVcfMaxVirtualSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 4),
    _Hh3cVcfMaxVirtualSlot_Type()
)
hh3cVcfMaxVirtualSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfMaxVirtualSlot.setStatus("current")
_Hh3cVcfMaxPortPerVcfPort_Type = Integer32
_Hh3cVcfMaxPortPerVcfPort_Object = MibScalar
hh3cVcfMaxPortPerVcfPort = _Hh3cVcfMaxPortPerVcfPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 1, 5),
    _Hh3cVcfMaxPortPerVcfPort_Type()
)
hh3cVcfMaxPortPerVcfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfMaxPortPerVcfPort.setStatus("current")
_Hh3cVcfTable_ObjectIdentity = ObjectIdentity
hh3cVcfTable = _Hh3cVcfTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2)
)
_Hh3cVcfPortTable_Object = MibTable
hh3cVcfPortTable = _Hh3cVcfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cVcfPortTable.setStatus("current")
_Hh3cVcfPortEntry_Object = MibTableRow
hh3cVcfPortEntry = _Hh3cVcfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1)
)
hh3cVcfPortEntry.setIndexNames(
    (0, "HH3C-VCF-MIB", "hh3cVcfPortId"),
)
if mibBuilder.loadTexts:
    hh3cVcfPortEntry.setStatus("current")


class _Hh3cVcfPortId_Type(Integer32):
    """Custom type hh3cVcfPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cVcfPortId_Type.__name__ = "Integer32"
_Hh3cVcfPortId_Object = MibTableColumn
hh3cVcfPortId = _Hh3cVcfPortId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 1),
    _Hh3cVcfPortId_Type()
)
hh3cVcfPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVcfPortId.setStatus("current")


class _Hh3cVcfPortVirtualSlot_Type(Integer32):
    """Custom type hh3cVcfPortVirtualSlot based on Integer32"""
    defaultValue = 65535


_Hh3cVcfPortVirtualSlot_Type.__name__ = "Integer32"
_Hh3cVcfPortVirtualSlot_Object = MibTableColumn
hh3cVcfPortVirtualSlot = _Hh3cVcfPortVirtualSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 2),
    _Hh3cVcfPortVirtualSlot_Type()
)
hh3cVcfPortVirtualSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVcfPortVirtualSlot.setStatus("current")


class _Hh3cVcfPortEntPhysicalIndex_Type(Integer32):
    """Custom type hh3cVcfPortEntPhysicalIndex based on Integer32"""
    defaultValue = 0


_Hh3cVcfPortEntPhysicalIndex_Type.__name__ = "Integer32"
_Hh3cVcfPortEntPhysicalIndex_Object = MibTableColumn
hh3cVcfPortEntPhysicalIndex = _Hh3cVcfPortEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 3),
    _Hh3cVcfPortEntPhysicalIndex_Type()
)
hh3cVcfPortEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfPortEntPhysicalIndex.setStatus("current")


class _Hh3cVcfPortDescr_Type(DisplayString):
    """Custom type hh3cVcfPortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_Hh3cVcfPortDescr_Type.__name__ = "DisplayString"
_Hh3cVcfPortDescr_Object = MibTableColumn
hh3cVcfPortDescr = _Hh3cVcfPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 4),
    _Hh3cVcfPortDescr_Type()
)
hh3cVcfPortDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVcfPortDescr.setStatus("current")


class _Hh3cVcfPortStatus_Type(Integer32):
    """Custom type hh3cVcfPortStatus based on Integer32"""
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
        *(("offline", 1),
          ("loading", 2),
          ("online", 3))
    )


_Hh3cVcfPortStatus_Type.__name__ = "Integer32"
_Hh3cVcfPortStatus_Object = MibTableColumn
hh3cVcfPortStatus = _Hh3cVcfPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 5),
    _Hh3cVcfPortStatus_Type()
)
hh3cVcfPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfPortStatus.setStatus("current")
_Hh3cVcfPortRowStatus_Type = RowStatus
_Hh3cVcfPortRowStatus_Object = MibTableColumn
hh3cVcfPortRowStatus = _Hh3cVcfPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 1, 1, 6),
    _Hh3cVcfPortRowStatus_Type()
)
hh3cVcfPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVcfPortRowStatus.setStatus("current")
_Hh3cVcfPhyPortTable_Object = MibTable
hh3cVcfPhyPortTable = _Hh3cVcfPhyPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cVcfPhyPortTable.setStatus("current")
_Hh3cVcfPhyPortEntry_Object = MibTableRow
hh3cVcfPhyPortEntry = _Hh3cVcfPhyPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1)
)
hh3cVcfPhyPortEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hh3cVcfPhyPortEntry.setStatus("current")


class _Hh3cVcfPhyPortStatus_Type(Integer32):
    """Custom type hh3cVcfPhyPortStatus based on Integer32"""
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
        *(("unknown", 1),
          ("down", 2),
          ("blocked", 3),
          ("forwarding", 4))
    )


_Hh3cVcfPhyPortStatus_Type.__name__ = "Integer32"
_Hh3cVcfPhyPortStatus_Object = MibTableColumn
hh3cVcfPhyPortStatus = _Hh3cVcfPhyPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1, 1),
    _Hh3cVcfPhyPortStatus_Type()
)
hh3cVcfPhyPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfPhyPortStatus.setStatus("current")


class _Hh3cVcfPhyPortBelongToVcfPort_Type(Integer32):
    """Custom type hh3cVcfPhyPortBelongToVcfPort based on Integer32"""
    defaultValue = 0


_Hh3cVcfPhyPortBelongToVcfPort_Type.__name__ = "Integer32"
_Hh3cVcfPhyPortBelongToVcfPort_Object = MibTableColumn
hh3cVcfPhyPortBelongToVcfPort = _Hh3cVcfPhyPortBelongToVcfPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1, 2),
    _Hh3cVcfPhyPortBelongToVcfPort_Type()
)
hh3cVcfPhyPortBelongToVcfPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVcfPhyPortBelongToVcfPort.setStatus("current")
_Hh3cVcfPhyPortNeighborEntIndex_Type = Integer32
_Hh3cVcfPhyPortNeighborEntIndex_Object = MibTableColumn
hh3cVcfPhyPortNeighborEntIndex = _Hh3cVcfPhyPortNeighborEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 2, 2, 1, 3),
    _Hh3cVcfPhyPortNeighborEntIndex_Type()
)
hh3cVcfPhyPortNeighborEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVcfPhyPortNeighborEntIndex.setStatus("current")
_Hh3cVcfTraps_ObjectIdentity = ObjectIdentity
hh3cVcfTraps = _Hh3cVcfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3)
)
_Hh3cVcfTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cVcfTrapPrefix = _Hh3cVcfTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0)
)
_Hh3cVcfTrapObjects_ObjectIdentity = ObjectIdentity
hh3cVcfTrapObjects = _Hh3cVcfTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 4)
)
_Hh3cVcfEntPhysicalIndexBind_Type = Integer32
_Hh3cVcfEntPhysicalIndexBind_Object = MibScalar
hh3cVcfEntPhysicalIndexBind = _Hh3cVcfEntPhysicalIndexBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 4, 1),
    _Hh3cVcfEntPhysicalIndexBind_Type()
)
hh3cVcfEntPhysicalIndexBind.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVcfEntPhysicalIndexBind.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cVcfPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 1)
)
hh3cVcfPortOnline.setObjects(
      *(("HH3C-VCF-MIB", "hh3cVcfPortId"),
        ("HH3C-VCF-MIB", "hh3cVcfPortDescr"))
)
if mibBuilder.loadTexts:
    hh3cVcfPortOnline.setStatus(
        "current"
    )

hh3cVcfPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 2)
)
hh3cVcfPortOffline.setObjects(
      *(("HH3C-VCF-MIB", "hh3cVcfPortId"),
        ("HH3C-VCF-MIB", "hh3cVcfPortDescr"))
)
if mibBuilder.loadTexts:
    hh3cVcfPortOffline.setStatus(
        "current"
    )

hh3cVcfPhyPortForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 3)
)
hh3cVcfPhyPortForwarding.setObjects(
      *(("HH3C-VCF-MIB", "hh3cVcfEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    hh3cVcfPhyPortForwarding.setStatus(
        "current"
    )

hh3cVcfPhyPortBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 129, 3, 0, 4)
)
hh3cVcfPhyPortBlocked.setObjects(
      *(("HH3C-VCF-MIB", "hh3cVcfEntPhysicalIndexBind"),
        ("ENTITY-MIB", "entPhysicalDescr"))
)
if mibBuilder.loadTexts:
    hh3cVcfPhyPortBlocked.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VCF-MIB",
    **{"hh3cVcf": hh3cVcf,
       "hh3cVcfSpecInfo": hh3cVcfSpecInfo,
       "hh3cVcfPortMinId": hh3cVcfPortMinId,
       "hh3cVcfPortMaxId": hh3cVcfPortMaxId,
       "hh3cVcfMinVirtualSlot": hh3cVcfMinVirtualSlot,
       "hh3cVcfMaxVirtualSlot": hh3cVcfMaxVirtualSlot,
       "hh3cVcfMaxPortPerVcfPort": hh3cVcfMaxPortPerVcfPort,
       "hh3cVcfTable": hh3cVcfTable,
       "hh3cVcfPortTable": hh3cVcfPortTable,
       "hh3cVcfPortEntry": hh3cVcfPortEntry,
       "hh3cVcfPortId": hh3cVcfPortId,
       "hh3cVcfPortVirtualSlot": hh3cVcfPortVirtualSlot,
       "hh3cVcfPortEntPhysicalIndex": hh3cVcfPortEntPhysicalIndex,
       "hh3cVcfPortDescr": hh3cVcfPortDescr,
       "hh3cVcfPortStatus": hh3cVcfPortStatus,
       "hh3cVcfPortRowStatus": hh3cVcfPortRowStatus,
       "hh3cVcfPhyPortTable": hh3cVcfPhyPortTable,
       "hh3cVcfPhyPortEntry": hh3cVcfPhyPortEntry,
       "hh3cVcfPhyPortStatus": hh3cVcfPhyPortStatus,
       "hh3cVcfPhyPortBelongToVcfPort": hh3cVcfPhyPortBelongToVcfPort,
       "hh3cVcfPhyPortNeighborEntIndex": hh3cVcfPhyPortNeighborEntIndex,
       "hh3cVcfTraps": hh3cVcfTraps,
       "hh3cVcfTrapPrefix": hh3cVcfTrapPrefix,
       "hh3cVcfPortOnline": hh3cVcfPortOnline,
       "hh3cVcfPortOffline": hh3cVcfPortOffline,
       "hh3cVcfPhyPortForwarding": hh3cVcfPhyPortForwarding,
       "hh3cVcfPhyPortBlocked": hh3cVcfPhyPortBlocked,
       "hh3cVcfTrapObjects": hh3cVcfTrapObjects,
       "hh3cVcfEntPhysicalIndexBind": hh3cVcfEntPhysicalIndexBind}
)
