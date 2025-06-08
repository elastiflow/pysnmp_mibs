# SNMP MIB module (SYS4PACEMAKER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sys4_39996/SYS4PACEMAKER-MIB.mib
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(sys4SNMPExperimental,) = mibBuilder.importSymbols(
    "SYS4-MIB",
    "sys4SNMPExperimental")


# MODULE-IDENTITY

sys4Pacemaker = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4)
)
if mibBuilder.loadTexts:
    sys4Pacemaker.setRevisions(
        ("2013-12-27 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sys4PcmkClusterConfig_ObjectIdentity = ObjectIdentity
sys4PcmkClusterConfig = _Sys4PcmkClusterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 1)
)
if mibBuilder.loadTexts:
    sys4PcmkClusterConfig.setStatus("current")
_Sys4PcmkNodes_ObjectIdentity = ObjectIdentity
sys4PcmkNodes = _Sys4PcmkNodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2)
)
if mibBuilder.loadTexts:
    sys4PcmkNodes.setStatus("current")
_Sys4PcmkTotalNodes_Type = Integer32
_Sys4PcmkTotalNodes_Object = MibScalar
sys4PcmkTotalNodes = _Sys4PcmkTotalNodes_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 1),
    _Sys4PcmkTotalNodes_Type()
)
sys4PcmkTotalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkTotalNodes.setStatus("current")
_Sys4PcmkOnlineNodes_Type = Integer32
_Sys4PcmkOnlineNodes_Object = MibScalar
sys4PcmkOnlineNodes = _Sys4PcmkOnlineNodes_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 2),
    _Sys4PcmkOnlineNodes_Type()
)
sys4PcmkOnlineNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkOnlineNodes.setStatus("current")
_Sys4PcmkNodeTable_Object = MibTable
sys4PcmkNodeTable = _Sys4PcmkNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 3)
)
if mibBuilder.loadTexts:
    sys4PcmkNodeTable.setStatus("current")
_Sys4PcmkNodeEntry_Object = MibTableRow
sys4PcmkNodeEntry = _Sys4PcmkNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 3, 1)
)
sys4PcmkNodeEntry.setIndexNames(
    (0, "SYS4PACEMAKER-MIB", "sys4PcmkNodeIndex"),
)
if mibBuilder.loadTexts:
    sys4PcmkNodeEntry.setStatus("current")
_Sys4PcmkNodeIndex_Type = Integer32
_Sys4PcmkNodeIndex_Object = MibTableColumn
sys4PcmkNodeIndex = _Sys4PcmkNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 3, 1, 1),
    _Sys4PcmkNodeIndex_Type()
)
sys4PcmkNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodeIndex.setStatus("current")


class _Sys4PcmkNodeName_Type(OctetString):
    """Custom type sys4PcmkNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Sys4PcmkNodeName_Type.__name__ = "OctetString"
_Sys4PcmkNodeName_Object = MibTableColumn
sys4PcmkNodeName = _Sys4PcmkNodeName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 3, 1, 2),
    _Sys4PcmkNodeName_Type()
)
sys4PcmkNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodeName.setStatus("current")
_Sys4PcmkNodeId_Type = Integer32
_Sys4PcmkNodeId_Object = MibTableColumn
sys4PcmkNodeId = _Sys4PcmkNodeId_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 3, 1, 3),
    _Sys4PcmkNodeId_Type()
)
sys4PcmkNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodeId.setStatus("current")


class _Sys4PcmkNodeStatus_Type(Integer32):
    """Custom type sys4PcmkNodeStatus based on Integer32"""
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


_Sys4PcmkNodeStatus_Type.__name__ = "Integer32"
_Sys4PcmkNodeStatus_Object = MibTableColumn
sys4PcmkNodeStatus = _Sys4PcmkNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 2, 3, 1, 4),
    _Sys4PcmkNodeStatus_Type()
)
sys4PcmkNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkNodeStatus.setStatus("current")
_Sys4PcmkResources_ObjectIdentity = ObjectIdentity
sys4PcmkResources = _Sys4PcmkResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3)
)
if mibBuilder.loadTexts:
    sys4PcmkResources.setStatus("current")
_Sys4PcmkResourcePrimitiveNumber_Type = Integer32
_Sys4PcmkResourcePrimitiveNumber_Object = MibScalar
sys4PcmkResourcePrimitiveNumber = _Sys4PcmkResourcePrimitiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 1),
    _Sys4PcmkResourcePrimitiveNumber_Type()
)
sys4PcmkResourcePrimitiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourcePrimitiveNumber.setStatus("current")
_Sys4PcmkResourceGroupNumber_Type = Integer32
_Sys4PcmkResourceGroupNumber_Object = MibScalar
sys4PcmkResourceGroupNumber = _Sys4PcmkResourceGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 2),
    _Sys4PcmkResourceGroupNumber_Type()
)
sys4PcmkResourceGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceGroupNumber.setStatus("current")
_Sys4PcmkResourceCloneNumber_Type = Integer32
_Sys4PcmkResourceCloneNumber_Object = MibScalar
sys4PcmkResourceCloneNumber = _Sys4PcmkResourceCloneNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 3),
    _Sys4PcmkResourceCloneNumber_Type()
)
sys4PcmkResourceCloneNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceCloneNumber.setStatus("current")
_Sys4PcmkResourceMasterNumber_Type = Integer32
_Sys4PcmkResourceMasterNumber_Object = MibScalar
sys4PcmkResourceMasterNumber = _Sys4PcmkResourceMasterNumber_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 4),
    _Sys4PcmkResourceMasterNumber_Type()
)
sys4PcmkResourceMasterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceMasterNumber.setStatus("current")
_Sys4PcmkResourceFailures_Type = Integer32
_Sys4PcmkResourceFailures_Object = MibScalar
sys4PcmkResourceFailures = _Sys4PcmkResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 5),
    _Sys4PcmkResourceFailures_Type()
)
sys4PcmkResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceFailures.setStatus("current")
_Sys4PcmkResourceTable_Object = MibTable
sys4PcmkResourceTable = _Sys4PcmkResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 6)
)
if mibBuilder.loadTexts:
    sys4PcmkResourceTable.setStatus("current")
_Sys4PcmkResourceEntry_Object = MibTableRow
sys4PcmkResourceEntry = _Sys4PcmkResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 6, 1)
)
sys4PcmkResourceEntry.setIndexNames(
    (0, "SYS4PACEMAKER-MIB", "sys4PcmkResourceIndex"),
)
if mibBuilder.loadTexts:
    sys4PcmkResourceEntry.setStatus("current")
_Sys4PcmkResourceIndex_Type = Integer32
_Sys4PcmkResourceIndex_Object = MibTableColumn
sys4PcmkResourceIndex = _Sys4PcmkResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 6, 1, 1),
    _Sys4PcmkResourceIndex_Type()
)
sys4PcmkResourceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceIndex.setStatus("current")
_Sys4PcmkResourceName_Type = OctetString
_Sys4PcmkResourceName_Object = MibTableColumn
sys4PcmkResourceName = _Sys4PcmkResourceName_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 6, 1, 2),
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
        *(("Stopped", 0),
          ("Started", 1),
          ("Master", 2),
          ("Unknown", 3))
    )


_Sys4PcmkResourceStatus_Type.__name__ = "Integer32"
_Sys4PcmkResourceStatus_Object = MibTableColumn
sys4PcmkResourceStatus = _Sys4PcmkResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 6, 1, 3),
    _Sys4PcmkResourceStatus_Type()
)
sys4PcmkResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceStatus.setStatus("current")
_Sys4PcmkResourceFailure_Type = Integer32
_Sys4PcmkResourceFailure_Object = MibTableColumn
sys4PcmkResourceFailure = _Sys4PcmkResourceFailure_Object(
    (1, 3, 6, 1, 4, 1, 39996, 161, 99, 4, 3, 6, 1, 4),
    _Sys4PcmkResourceFailure_Type()
)
sys4PcmkResourceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys4PcmkResourceFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYS4PACEMAKER-MIB",
    **{"sys4Pacemaker": sys4Pacemaker,
       "sys4PcmkClusterConfig": sys4PcmkClusterConfig,
       "sys4PcmkNodes": sys4PcmkNodes,
       "sys4PcmkTotalNodes": sys4PcmkTotalNodes,
       "sys4PcmkOnlineNodes": sys4PcmkOnlineNodes,
       "sys4PcmkNodeTable": sys4PcmkNodeTable,
       "sys4PcmkNodeEntry": sys4PcmkNodeEntry,
       "sys4PcmkNodeIndex": sys4PcmkNodeIndex,
       "sys4PcmkNodeName": sys4PcmkNodeName,
       "sys4PcmkNodeId": sys4PcmkNodeId,
       "sys4PcmkNodeStatus": sys4PcmkNodeStatus,
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
       "sys4PcmkResourceFailure": sys4PcmkResourceFailure}
)
