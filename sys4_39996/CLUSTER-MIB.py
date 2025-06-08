# SNMP MIB module (CLUSTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sys4_39996/CLUSTER-MIB.mib
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

sys4Pacemaker = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1)
)
if mibBuilder.loadTexts:
    sys4Pacemaker.setRevisions(
        ("2013-12-27 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sys4PcmkConfiguration_ObjectIdentity = ObjectIdentity
sys4PcmkConfiguration = _Sys4PcmkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 1)
)
_Sys4PcmkClusterName_Type = DisplayString
_Sys4PcmkClusterName_Object = MibScalar
sys4PcmkClusterName = _Sys4PcmkClusterName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 1, 1),
    _Sys4PcmkClusterName_Type()
)
sys4PcmkClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkClusterName.setStatus("current")
_Sys4PcmkNodes_ObjectIdentity = ObjectIdentity
sys4PcmkNodes = _Sys4PcmkNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2)
)
_Sys4PcmkTotalNodes_Type = Integer32
_Sys4PcmkTotalNodes_Object = MibScalar
sys4PcmkTotalNodes = _Sys4PcmkTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 1),
    _Sys4PcmkTotalNodes_Type()
)
sys4PcmkTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkTotalNodes.setStatus("current")
_Sys4PcmkOnlineNodes_Type = Integer32
_Sys4PcmkOnlineNodes_Object = MibScalar
sys4PcmkOnlineNodes = _Sys4PcmkOnlineNodes_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 2),
    _Sys4PcmkOnlineNodes_Type()
)
sys4PcmkOnlineNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkOnlineNodes.setStatus("current")
_Sys4PcmkNodesTable_Object = MibTable
sys4PcmkNodesTable = _Sys4PcmkNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sys4PcmkNodesTable.setStatus("current")
_Sys4PcmkNodesEntry_Object = MibTableRow
sys4PcmkNodesEntry = _Sys4PcmkNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1)
)
sys4PcmkNodesEntry.setIndexNames(
    (0, "CLUSTER-MIB", "sys4PcmkNodesIndex"),
)
if mibBuilder.loadTexts:
    sys4PcmkNodesEntry.setStatus("current")


class _Sys4PcmkNodesIndex_Type(Integer32):
    """Custom type sys4PcmkNodesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sys4PcmkNodesIndex_Type.__name__ = "Integer32"
_Sys4PcmkNodesIndex_Object = MibTableColumn
sys4PcmkNodesIndex = _Sys4PcmkNodesIndex_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 1),
    _Sys4PcmkNodesIndex_Type()
)
sys4PcmkNodesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sys4PcmkNodesIndex.setStatus("current")
_Sys4PcmkNodesName_Type = DisplayString
_Sys4PcmkNodesName_Object = MibTableColumn
sys4PcmkNodesName = _Sys4PcmkNodesName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 2),
    _Sys4PcmkNodesName_Type()
)
sys4PcmkNodesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodesName.setStatus("current")
_Sys4PcmkNodesId_Type = Integer32
_Sys4PcmkNodesId_Object = MibTableColumn
sys4PcmkNodesId = _Sys4PcmkNodesId_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 3),
    _Sys4PcmkNodesId_Type()
)
sys4PcmkNodesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodesId.setStatus("current")


class _Sys4PcmkNodesStatus_Type(Integer32):
    """Custom type sys4PcmkNodesStatus based on Integer32"""
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


_Sys4PcmkNodesStatus_Type.__name__ = "Integer32"
_Sys4PcmkNodesStatus_Object = MibTableColumn
sys4PcmkNodesStatus = _Sys4PcmkNodesStatus_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 2, 3, 1, 4),
    _Sys4PcmkNodesStatus_Type()
)
sys4PcmkNodesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodesStatus.setStatus("current")
_Sys4PcmkResources_ObjectIdentity = ObjectIdentity
sys4PcmkResources = _Sys4PcmkResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3)
)
_Sys4PcmkResourcePrimitiveNumber_Type = Integer32
_Sys4PcmkResourcePrimitiveNumber_Object = MibScalar
sys4PcmkResourcePrimitiveNumber = _Sys4PcmkResourcePrimitiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 1),
    _Sys4PcmkResourcePrimitiveNumber_Type()
)
sys4PcmkResourcePrimitiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourcePrimitiveNumber.setStatus("current")
_Sys4PcmkResourceGroupNumber_Type = Integer32
_Sys4PcmkResourceGroupNumber_Object = MibScalar
sys4PcmkResourceGroupNumber = _Sys4PcmkResourceGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 2),
    _Sys4PcmkResourceGroupNumber_Type()
)
sys4PcmkResourceGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceGroupNumber.setStatus("current")
_Sys4PcmkResourceCloneNumber_Type = Integer32
_Sys4PcmkResourceCloneNumber_Object = MibScalar
sys4PcmkResourceCloneNumber = _Sys4PcmkResourceCloneNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 3),
    _Sys4PcmkResourceCloneNumber_Type()
)
sys4PcmkResourceCloneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceCloneNumber.setStatus("current")
_Sys4PcmkResourceMasterNumber_Type = Integer32
_Sys4PcmkResourceMasterNumber_Object = MibScalar
sys4PcmkResourceMasterNumber = _Sys4PcmkResourceMasterNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 4),
    _Sys4PcmkResourceMasterNumber_Type()
)
sys4PcmkResourceMasterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceMasterNumber.setStatus("current")
_Sys4PcmkResourceFailures_Type = Integer32
_Sys4PcmkResourceFailures_Object = MibScalar
sys4PcmkResourceFailures = _Sys4PcmkResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 5),
    _Sys4PcmkResourceFailures_Type()
)
sys4PcmkResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceFailures.setStatus("current")
_Sys4PcmkResourceTable_Object = MibTable
sys4PcmkResourceTable = _Sys4PcmkResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6)
)
if mibBuilder.loadTexts:
    sys4PcmkResourceTable.setStatus("current")
_Sys4PcmkResourceEntry_Object = MibTableRow
sys4PcmkResourceEntry = _Sys4PcmkResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1)
)
sys4PcmkResourceEntry.setIndexNames(
    (0, "CLUSTER-MIB", "sys4PcmkResourceIndex"),
)
if mibBuilder.loadTexts:
    sys4PcmkResourceEntry.setStatus("current")


class _Sys4PcmkResourceIndex_Type(Integer32):
    """Custom type sys4PcmkResourceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Sys4PcmkResourceIndex_Type.__name__ = "Integer32"
_Sys4PcmkResourceIndex_Object = MibTableColumn
sys4PcmkResourceIndex = _Sys4PcmkResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 1),
    _Sys4PcmkResourceIndex_Type()
)
sys4PcmkResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sys4PcmkResourceIndex.setStatus("current")
_Sys4PcmkResourceName_Type = DisplayString
_Sys4PcmkResourceName_Object = MibTableColumn
sys4PcmkResourceName = _Sys4PcmkResourceName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 2),
    _Sys4PcmkResourceName_Type()
)
sys4PcmkResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceName.setStatus("current")


class _Sys4PcmkResourceStatus_Type(Integer32):
    """Custom type sys4PcmkResourceStatus based on Integer32"""
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


_Sys4PcmkResourceStatus_Type.__name__ = "Integer32"
_Sys4PcmkResourceStatus_Object = MibTableColumn
sys4PcmkResourceStatus = _Sys4PcmkResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 3),
    _Sys4PcmkResourceStatus_Type()
)
sys4PcmkResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceStatus.setStatus("current")
_Sys4PcmkResourceFailure_Type = Integer32
_Sys4PcmkResourceFailure_Object = MibTableColumn
sys4PcmkResourceFailure = _Sys4PcmkResourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 39996, 1, 3, 6, 1, 4),
    _Sys4PcmkResourceFailure_Type()
)
sys4PcmkResourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceFailure.setStatus("current")
_Sys4PcmkConformance_ObjectIdentity = ObjectIdentity
sys4PcmkConformance = _Sys4PcmkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4)
)
_Sys4PcmkCompliances_ObjectIdentity = ObjectIdentity
sys4PcmkCompliances = _Sys4PcmkCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 1)
)
_Sys4PcmkGroups_ObjectIdentity = ObjectIdentity
sys4PcmkGroups = _Sys4PcmkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 2)
)

# Managed Objects groups

libvirtGuestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 2, 1)
)
libvirtGuestGroup.setObjects(
      *(("CLUSTER-MIB", "sys4PcmkClusterName"),
        ("CLUSTER-MIB", "sys4PcmkTotalNodes"),
        ("CLUSTER-MIB", "sys4PcmkOnlineNodes"),
        ("CLUSTER-MIB", "sys4PcmkNodesName"),
        ("CLUSTER-MIB", "sys4PcmkNodesId"),
        ("CLUSTER-MIB", "sys4PcmkNodesStatus"),
        ("CLUSTER-MIB", "sys4PcmkResourcePrimitiveNumber"),
        ("CLUSTER-MIB", "sys4PcmkResourceGroupNumber"),
        ("CLUSTER-MIB", "sys4PcmkResourceCloneNumber"),
        ("CLUSTER-MIB", "sys4PcmkResourceMasterNumber"),
        ("CLUSTER-MIB", "sys4PcmkResourceFailures"),
        ("CLUSTER-MIB", "sys4PcmkResourceName"),
        ("CLUSTER-MIB", "sys4PcmkResourceStatus"),
        ("CLUSTER-MIB", "sys4PcmkResourceFailure"))
)
if mibBuilder.loadTexts:
    libvirtGuestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sys4PcmkCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 39996, 1, 4, 1, 1)
)
sys4PcmkCompliance.setObjects(
    ("CLUSTER-MIB", "libvirtGuestGroup")
)
if mibBuilder.loadTexts:
    sys4PcmkCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLUSTER-MIB",
    **{"sys4Pacemaker": sys4Pacemaker,
       "sys4PcmkConfiguration": sys4PcmkConfiguration,
       "sys4PcmkClusterName": sys4PcmkClusterName,
       "sys4PcmkNodes": sys4PcmkNodes,
       "sys4PcmkTotalNodes": sys4PcmkTotalNodes,
       "sys4PcmkOnlineNodes": sys4PcmkOnlineNodes,
       "sys4PcmkNodesTable": sys4PcmkNodesTable,
       "sys4PcmkNodesEntry": sys4PcmkNodesEntry,
       "sys4PcmkNodesIndex": sys4PcmkNodesIndex,
       "sys4PcmkNodesName": sys4PcmkNodesName,
       "sys4PcmkNodesId": sys4PcmkNodesId,
       "sys4PcmkNodesStatus": sys4PcmkNodesStatus,
       "sys4PcmkResources": sys4PcmkResources,
       "sys4PcmkResourcePrimitiveNumber": sys4PcmkResourcePrimitiveNumber,
       "sys4PcmkResourceGroupNumber": sys4PcmkResourceGroupNumber,
       "sys4PcmkResourceCloneNumber": sys4PcmkResourceCloneNumber,
       "sys4PcmkResourceMasterNumber": sys4PcmkResourceMasterNumber,
       "sys4PcmkResourceFailures": sys4PcmkResourceFailures,
       "sys4PcmkResourceTable": sys4PcmkResourceTable,
       "sys4PcmkResourceEntry": sys4PcmkResourceEntry,
       "sys4PcmkResourceIndex": sys4PcmkResourceIndex,
       "sys4PcmkResourceName": sys4PcmkResourceName,
       "sys4PcmkResourceStatus": sys4PcmkResourceStatus,
       "sys4PcmkResourceFailure": sys4PcmkResourceFailure,
       "sys4PcmkConformance": sys4PcmkConformance,
       "sys4PcmkCompliances": sys4PcmkCompliances,
       "sys4PcmkCompliance": sys4PcmkCompliance,
       "sys4PcmkGroups": sys4PcmkGroups,
       "libvirtGuestGroup": libvirtGuestGroup}
)
