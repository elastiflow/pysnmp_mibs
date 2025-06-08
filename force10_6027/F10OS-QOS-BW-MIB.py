# SNMP MIB module (F10OS-QOS-BW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/F10OS-QOS-BW-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:05 2025
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

(f10OSQOS,) = mibBuilder.importSymbols(
    "F10OS-QOS-MIB",
    "f10OSQOS")

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

f10OSQOSBandwidth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    f10OSQOSBandwidth.setRevisions(
        ("2005-01-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrafficClassGroup_ObjectIdentity = ObjectIdentity
trafficClassGroup = _TrafficClassGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1)
)


class _TrafficClassCreate_Type(DisplayString):
    """Custom type trafficClassCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TrafficClassCreate_Type.__name__ = "DisplayString"
_TrafficClassCreate_Object = MibScalar
trafficClassCreate = _TrafficClassCreate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 1),
    _TrafficClassCreate_Type()
)
trafficClassCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficClassCreate.setStatus("current")
_TrafficClassTable_Object = MibTable
trafficClassTable = _TrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    trafficClassTable.setStatus("current")
_TrafficClassEntry_Object = MibTableRow
trafficClassEntry = _TrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1)
)
trafficClassEntry.setIndexNames(
    (0, "F10OS-QOS-BW-MIB", "trafficClassIndex"),
)
if mibBuilder.loadTexts:
    trafficClassEntry.setStatus("current")
_TrafficClassIndex_Type = Integer32
_TrafficClassIndex_Object = MibTableColumn
trafficClassIndex = _TrafficClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 1),
    _TrafficClassIndex_Type()
)
trafficClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trafficClassIndex.setStatus("current")


class _TrafficClassName_Type(DisplayString):
    """Custom type trafficClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_TrafficClassName_Type.__name__ = "DisplayString"
_TrafficClassName_Object = MibTableColumn
trafficClassName = _TrafficClassName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 2),
    _TrafficClassName_Type()
)
trafficClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficClassName.setStatus("current")
_TrafficClassIfIndex_Type = Integer32
_TrafficClassIfIndex_Object = MibTableColumn
trafficClassIfIndex = _TrafficClassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 3),
    _TrafficClassIfIndex_Type()
)
trafficClassIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficClassIfIndex.setStatus("current")
_TrafficClassVlanId_Type = Integer32
_TrafficClassVlanId_Object = MibTableColumn
trafficClassVlanId = _TrafficClassVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 4),
    _TrafficClassVlanId_Type()
)
trafficClassVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficClassVlanId.setStatus("current")


class _TrafficClassWeight_Type(Integer32):
    """Custom type trafficClassWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_TrafficClassWeight_Type.__name__ = "Integer32"
_TrafficClassWeight_Object = MibTableColumn
trafficClassWeight = _TrafficClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 5),
    _TrafficClassWeight_Type()
)
trafficClassWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficClassWeight.setStatus("current")
_TrafficClassBandwidthAllocation_Type = Integer32
_TrafficClassBandwidthAllocation_Object = MibTableColumn
trafficClassBandwidthAllocation = _TrafficClassBandwidthAllocation_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 6),
    _TrafficClassBandwidthAllocation_Type()
)
trafficClassBandwidthAllocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficClassBandwidthAllocation.setStatus("current")
_TrafficClassAcceptByteCount_Type = Counter32
_TrafficClassAcceptByteCount_Object = MibTableColumn
trafficClassAcceptByteCount = _TrafficClassAcceptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 7),
    _TrafficClassAcceptByteCount_Type()
)
trafficClassAcceptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficClassAcceptByteCount.setStatus("current")
_TrafficClassStatus_Type = RowStatus
_TrafficClassStatus_Object = MibTableColumn
trafficClassStatus = _TrafficClassStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 1, 2, 1, 8),
    _TrafficClassStatus_Type()
)
trafficClassStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trafficClassStatus.setStatus("current")
_BandwidthAllocationGroup_ObjectIdentity = ObjectIdentity
bandwidthAllocationGroup = _BandwidthAllocationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2)
)


class _BandwidthAllocationCreate_Type(DisplayString):
    """Custom type bandwidthAllocationCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_BandwidthAllocationCreate_Type.__name__ = "DisplayString"
_BandwidthAllocationCreate_Object = MibScalar
bandwidthAllocationCreate = _BandwidthAllocationCreate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 1),
    _BandwidthAllocationCreate_Type()
)
bandwidthAllocationCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocationCreate.setStatus("current")
_BandwidthAllocationTable_Object = MibTable
bandwidthAllocationTable = _BandwidthAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bandwidthAllocationTable.setStatus("current")
_BandwidthAllocationEntry_Object = MibTableRow
bandwidthAllocationEntry = _BandwidthAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2, 1)
)
bandwidthAllocationEntry.setIndexNames(
    (0, "F10OS-QOS-BW-MIB", "bandwidthAllocationIndex"),
)
if mibBuilder.loadTexts:
    bandwidthAllocationEntry.setStatus("current")
_BandwidthAllocationIndex_Type = Integer32
_BandwidthAllocationIndex_Object = MibTableColumn
bandwidthAllocationIndex = _BandwidthAllocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2, 1, 1),
    _BandwidthAllocationIndex_Type()
)
bandwidthAllocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bandwidthAllocationIndex.setStatus("current")


class _BandwidthAllocationName_Type(DisplayString):
    """Custom type bandwidthAllocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_BandwidthAllocationName_Type.__name__ = "DisplayString"
_BandwidthAllocationName_Object = MibTableColumn
bandwidthAllocationName = _BandwidthAllocationName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2, 1, 2),
    _BandwidthAllocationName_Type()
)
bandwidthAllocationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandwidthAllocationName.setStatus("current")
_BandwidthAllocationMinBandwidth_Type = Gauge32
_BandwidthAllocationMinBandwidth_Object = MibTableColumn
bandwidthAllocationMinBandwidth = _BandwidthAllocationMinBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2, 1, 3),
    _BandwidthAllocationMinBandwidth_Type()
)
bandwidthAllocationMinBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocationMinBandwidth.setStatus("current")
_BandwidthAllocationMaxBandwidth_Type = Gauge32
_BandwidthAllocationMaxBandwidth_Object = MibTableColumn
bandwidthAllocationMaxBandwidth = _BandwidthAllocationMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2, 1, 4),
    _BandwidthAllocationMaxBandwidth_Type()
)
bandwidthAllocationMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocationMaxBandwidth.setStatus("current")
_BandwidthAllocationStatus_Type = RowStatus
_BandwidthAllocationStatus_Object = MibTableColumn
bandwidthAllocationStatus = _BandwidthAllocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 3, 1, 2, 2, 1, 5),
    _BandwidthAllocationStatus_Type()
)
bandwidthAllocationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandwidthAllocationStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10OS-QOS-BW-MIB",
    **{"f10OSQOSBandwidth": f10OSQOSBandwidth,
       "trafficClassGroup": trafficClassGroup,
       "trafficClassCreate": trafficClassCreate,
       "trafficClassTable": trafficClassTable,
       "trafficClassEntry": trafficClassEntry,
       "trafficClassIndex": trafficClassIndex,
       "trafficClassName": trafficClassName,
       "trafficClassIfIndex": trafficClassIfIndex,
       "trafficClassVlanId": trafficClassVlanId,
       "trafficClassWeight": trafficClassWeight,
       "trafficClassBandwidthAllocation": trafficClassBandwidthAllocation,
       "trafficClassAcceptByteCount": trafficClassAcceptByteCount,
       "trafficClassStatus": trafficClassStatus,
       "bandwidthAllocationGroup": bandwidthAllocationGroup,
       "bandwidthAllocationCreate": bandwidthAllocationCreate,
       "bandwidthAllocationTable": bandwidthAllocationTable,
       "bandwidthAllocationEntry": bandwidthAllocationEntry,
       "bandwidthAllocationIndex": bandwidthAllocationIndex,
       "bandwidthAllocationName": bandwidthAllocationName,
       "bandwidthAllocationMinBandwidth": bandwidthAllocationMinBandwidth,
       "bandwidthAllocationMaxBandwidth": bandwidthAllocationMaxBandwidth,
       "bandwidthAllocationStatus": bandwidthAllocationStatus}
)
