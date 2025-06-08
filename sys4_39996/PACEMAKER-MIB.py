# SNMP MIB module (PACEMAKER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sys4_39996/PACEMAKER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:57:44 2025
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

(sys4,) = mibBuilder.importSymbols(
    "CLUSTERLABS-MIB",
    "sys4")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

clusterLabsPacemaker = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1)
)
if mibBuilder.loadTexts:
    clusterLabsPacemaker.setRevisions(
        ("2016-11-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClusterLabsPcmkConfiguration_ObjectIdentity = ObjectIdentity
clusterLabsPcmkConfiguration = _ClusterLabsPcmkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 1)
)
_ClusterLabsPcmkClusterName_Type = DisplayString
_ClusterLabsPcmkClusterName_Object = MibScalar
clusterLabsPcmkClusterName = _ClusterLabsPcmkClusterName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 1, 1),
    _ClusterLabsPcmkClusterName_Type()
)
clusterLabsPcmkClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkClusterName.setStatus("current")
_ClusterLabsPcmkNodes_ObjectIdentity = ObjectIdentity
clusterLabsPcmkNodes = _ClusterLabsPcmkNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2)
)
_ClusterLabsPcmkTotalNodes_Type = Integer32
_ClusterLabsPcmkTotalNodes_Object = MibScalar
clusterLabsPcmkTotalNodes = _ClusterLabsPcmkTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 1),
    _ClusterLabsPcmkTotalNodes_Type()
)
clusterLabsPcmkTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkTotalNodes.setStatus("current")
_ClusterLabsPcmkOnlineNodes_Type = Integer32
_ClusterLabsPcmkOnlineNodes_Object = MibScalar
clusterLabsPcmkOnlineNodes = _ClusterLabsPcmkOnlineNodes_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 2),
    _ClusterLabsPcmkOnlineNodes_Type()
)
clusterLabsPcmkOnlineNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkOnlineNodes.setStatus("current")
_ClusterLabsPcmkNodesTable_Object = MibTable
clusterLabsPcmkNodesTable = _ClusterLabsPcmkNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3)
)
if mibBuilder.loadTexts:
    clusterLabsPcmkNodesTable.setStatus("current")
_ClusterLabsPcmkNodesEntry_Object = MibTableRow
clusterLabsPcmkNodesEntry = _ClusterLabsPcmkNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1)
)
clusterLabsPcmkNodesEntry.setIndexNames(
    (0, "PACEMAKER-MIB", "clusterLabsPcmkNodesIndex"),
)
if mibBuilder.loadTexts:
    clusterLabsPcmkNodesEntry.setStatus("current")


class _ClusterLabsPcmkNodesIndex_Type(Integer32):
    """Custom type clusterLabsPcmkNodesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClusterLabsPcmkNodesIndex_Type.__name__ = "Integer32"
_ClusterLabsPcmkNodesIndex_Object = MibTableColumn
clusterLabsPcmkNodesIndex = _ClusterLabsPcmkNodesIndex_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 1),
    _ClusterLabsPcmkNodesIndex_Type()
)
clusterLabsPcmkNodesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterLabsPcmkNodesIndex.setStatus("current")
_ClusterLabsPcmkNodesName_Type = DisplayString
_ClusterLabsPcmkNodesName_Object = MibTableColumn
clusterLabsPcmkNodesName = _ClusterLabsPcmkNodesName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 2),
    _ClusterLabsPcmkNodesName_Type()
)
clusterLabsPcmkNodesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkNodesName.setStatus("current")
_ClusterLabsPcmkNodesId_Type = Integer32
_ClusterLabsPcmkNodesId_Object = MibTableColumn
clusterLabsPcmkNodesId = _ClusterLabsPcmkNodesId_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 3),
    _ClusterLabsPcmkNodesId_Type()
)
clusterLabsPcmkNodesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkNodesId.setStatus("current")


class _ClusterLabsPcmkNodesStatus_Type(Integer32):
    """Custom type clusterLabsPcmkNodesStatus based on Integer32"""
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
        *(("unknown", 0),
          ("online", 1),
          ("standby", 2),
          ("offline", 3),
          ("other", 4))
    )


_ClusterLabsPcmkNodesStatus_Type.__name__ = "Integer32"
_ClusterLabsPcmkNodesStatus_Object = MibTableColumn
clusterLabsPcmkNodesStatus = _ClusterLabsPcmkNodesStatus_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 4),
    _ClusterLabsPcmkNodesStatus_Type()
)
clusterLabsPcmkNodesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkNodesStatus.setStatus("current")
_ClusterLabsPcmkResources_ObjectIdentity = ObjectIdentity
clusterLabsPcmkResources = _ClusterLabsPcmkResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3)
)
_ClusterLabsPcmkResourcePrimitiveNumber_Type = Integer32
_ClusterLabsPcmkResourcePrimitiveNumber_Object = MibScalar
clusterLabsPcmkResourcePrimitiveNumber = _ClusterLabsPcmkResourcePrimitiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 1),
    _ClusterLabsPcmkResourcePrimitiveNumber_Type()
)
clusterLabsPcmkResourcePrimitiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourcePrimitiveNumber.setStatus("current")
_ClusterLabsPcmkResourceGroupNumber_Type = Integer32
_ClusterLabsPcmkResourceGroupNumber_Object = MibScalar
clusterLabsPcmkResourceGroupNumber = _ClusterLabsPcmkResourceGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 2),
    _ClusterLabsPcmkResourceGroupNumber_Type()
)
clusterLabsPcmkResourceGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceGroupNumber.setStatus("current")
_ClusterLabsPcmkResourceCloneNumber_Type = Integer32
_ClusterLabsPcmkResourceCloneNumber_Object = MibScalar
clusterLabsPcmkResourceCloneNumber = _ClusterLabsPcmkResourceCloneNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 3),
    _ClusterLabsPcmkResourceCloneNumber_Type()
)
clusterLabsPcmkResourceCloneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceCloneNumber.setStatus("current")
_ClusterLabsPcmkResourceMasterNumber_Type = Integer32
_ClusterLabsPcmkResourceMasterNumber_Object = MibScalar
clusterLabsPcmkResourceMasterNumber = _ClusterLabsPcmkResourceMasterNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 4),
    _ClusterLabsPcmkResourceMasterNumber_Type()
)
clusterLabsPcmkResourceMasterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceMasterNumber.setStatus("current")
_ClusterLabsPcmkResourceFailures_Type = Integer32
_ClusterLabsPcmkResourceFailures_Object = MibScalar
clusterLabsPcmkResourceFailures = _ClusterLabsPcmkResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 5),
    _ClusterLabsPcmkResourceFailures_Type()
)
clusterLabsPcmkResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceFailures.setStatus("current")
_ClusterLabsPcmkResourceTable_Object = MibTable
clusterLabsPcmkResourceTable = _ClusterLabsPcmkResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6)
)
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceTable.setStatus("current")
_ClusterLabsPcmkResourceEntry_Object = MibTableRow
clusterLabsPcmkResourceEntry = _ClusterLabsPcmkResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1)
)
clusterLabsPcmkResourceEntry.setIndexNames(
    (0, "PACEMAKER-MIB", "clusterLabsPcmkResourceIndex"),
)
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceEntry.setStatus("current")


class _ClusterLabsPcmkResourceIndex_Type(Integer32):
    """Custom type clusterLabsPcmkResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ClusterLabsPcmkResourceIndex_Type.__name__ = "Integer32"
_ClusterLabsPcmkResourceIndex_Object = MibTableColumn
clusterLabsPcmkResourceIndex = _ClusterLabsPcmkResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 1),
    _ClusterLabsPcmkResourceIndex_Type()
)
clusterLabsPcmkResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceIndex.setStatus("current")
_ClusterLabsPcmkResourceName_Type = DisplayString
_ClusterLabsPcmkResourceName_Object = MibTableColumn
clusterLabsPcmkResourceName = _ClusterLabsPcmkResourceName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 2),
    _ClusterLabsPcmkResourceName_Type()
)
clusterLabsPcmkResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceName.setStatus("current")


class _ClusterLabsPcmkResourceStatus_Type(Integer32):
    """Custom type clusterLabsPcmkResourceStatus based on Integer32"""
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
        *(("stopped", 0),
          ("started", 1),
          ("master", 2),
          ("unknown", 3))
    )


_ClusterLabsPcmkResourceStatus_Type.__name__ = "Integer32"
_ClusterLabsPcmkResourceStatus_Object = MibTableColumn
clusterLabsPcmkResourceStatus = _ClusterLabsPcmkResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 3),
    _ClusterLabsPcmkResourceStatus_Type()
)
clusterLabsPcmkResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceStatus.setStatus("current")
_ClusterLabsPcmkResourceFailure_Type = Integer32
_ClusterLabsPcmkResourceFailure_Object = MibTableColumn
clusterLabsPcmkResourceFailure = _ClusterLabsPcmkResourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 4),
    _ClusterLabsPcmkResourceFailure_Type()
)
clusterLabsPcmkResourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLabsPcmkResourceFailure.setStatus("current")
_ClusterLabsPcmkConformance_ObjectIdentity = ObjectIdentity
clusterLabsPcmkConformance = _ClusterLabsPcmkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4)
)
_ClusterLabsPcmkCompliances_ObjectIdentity = ObjectIdentity
clusterLabsPcmkCompliances = _ClusterLabsPcmkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 1)
)
_ClusterLabsPcmkGroups_ObjectIdentity = ObjectIdentity
clusterLabsPcmkGroups = _ClusterLabsPcmkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 2)
)

# Managed Objects groups

libvirtGuestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 2, 1)
)
libvirtGuestGroup.setObjects(
      *(("PACEMAKER-MIB", "clusterLabsPcmkClusterName"),
        ("PACEMAKER-MIB", "clusterLabsPcmkTotalNodes"),
        ("PACEMAKER-MIB", "clusterLabsPcmkOnlineNodes"),
        ("PACEMAKER-MIB", "clusterLabsPcmkNodesName"),
        ("PACEMAKER-MIB", "clusterLabsPcmkNodesId"),
        ("PACEMAKER-MIB", "clusterLabsPcmkNodesStatus"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourcePrimitiveNumber"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceGroupNumber"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceCloneNumber"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceMasterNumber"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceFailures"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceName"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceStatus"),
        ("PACEMAKER-MIB", "clusterLabsPcmkResourceFailure"))
)
if mibBuilder.loadTexts:
    libvirtGuestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clusterLabsPcmkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 1, 1)
)
clusterLabsPcmkCompliance.setObjects(
    ("PACEMAKER-MIB", "libvirtGuestGroup")
)
if mibBuilder.loadTexts:
    clusterLabsPcmkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACEMAKER-MIB",
    **{"clusterLabsPacemaker": clusterLabsPacemaker,
       "clusterLabsPcmkConfiguration": clusterLabsPcmkConfiguration,
       "clusterLabsPcmkClusterName": clusterLabsPcmkClusterName,
       "clusterLabsPcmkNodes": clusterLabsPcmkNodes,
       "clusterLabsPcmkTotalNodes": clusterLabsPcmkTotalNodes,
       "clusterLabsPcmkOnlineNodes": clusterLabsPcmkOnlineNodes,
       "clusterLabsPcmkNodesTable": clusterLabsPcmkNodesTable,
       "clusterLabsPcmkNodesEntry": clusterLabsPcmkNodesEntry,
       "clusterLabsPcmkNodesIndex": clusterLabsPcmkNodesIndex,
       "clusterLabsPcmkNodesName": clusterLabsPcmkNodesName,
       "clusterLabsPcmkNodesId": clusterLabsPcmkNodesId,
       "clusterLabsPcmkNodesStatus": clusterLabsPcmkNodesStatus,
       "clusterLabsPcmkResources": clusterLabsPcmkResources,
       "clusterLabsPcmkResourcePrimitiveNumber": clusterLabsPcmkResourcePrimitiveNumber,
       "clusterLabsPcmkResourceGroupNumber": clusterLabsPcmkResourceGroupNumber,
       "clusterLabsPcmkResourceCloneNumber": clusterLabsPcmkResourceCloneNumber,
       "clusterLabsPcmkResourceMasterNumber": clusterLabsPcmkResourceMasterNumber,
       "clusterLabsPcmkResourceFailures": clusterLabsPcmkResourceFailures,
       "clusterLabsPcmkResourceTable": clusterLabsPcmkResourceTable,
       "clusterLabsPcmkResourceEntry": clusterLabsPcmkResourceEntry,
       "clusterLabsPcmkResourceIndex": clusterLabsPcmkResourceIndex,
       "clusterLabsPcmkResourceName": clusterLabsPcmkResourceName,
       "clusterLabsPcmkResourceStatus": clusterLabsPcmkResourceStatus,
       "clusterLabsPcmkResourceFailure": clusterLabsPcmkResourceFailure,
       "clusterLabsPcmkConformance": clusterLabsPcmkConformance,
       "clusterLabsPcmkCompliances": clusterLabsPcmkCompliances,
       "clusterLabsPcmkCompliance": clusterLabsPcmkCompliance,
       "clusterLabsPcmkGroups": clusterLabsPcmkGroups,
       "libvirtGuestGroup": libvirtGuestGroup}
)
