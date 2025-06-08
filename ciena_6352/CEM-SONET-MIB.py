# SNMP MIB module (CEM-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-SONET-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

cnSonetModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnSonetTable_Object = MibTable
cnSonetTable = _CnSonetTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1)
)
if mibBuilder.loadTexts:
    cnSonetTable.setStatus("current")
_CnSonetEntry_Object = MibTableRow
cnSonetEntry = _CnSonetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1)
)
cnSonetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cnSonetEntry.setStatus("current")
_CnSonetLineStatus_Type = Integer32
_CnSonetLineStatus_Object = MibTableColumn
cnSonetLineStatus = _CnSonetLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 1),
    _CnSonetLineStatus_Type()
)
cnSonetLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnSonetLineStatus.setStatus("current")


class _CnSonetTxPathTraceId_Type(OctetString):
    """Custom type cnSonetTxPathTraceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnSonetTxPathTraceId_Type.__name__ = "OctetString"
_CnSonetTxPathTraceId_Object = MibTableColumn
cnSonetTxPathTraceId = _CnSonetTxPathTraceId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 2),
    _CnSonetTxPathTraceId_Type()
)
cnSonetTxPathTraceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSonetTxPathTraceId.setStatus("current")


class _CnSonetRxPathTraceId_Type(OctetString):
    """Custom type cnSonetRxPathTraceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnSonetRxPathTraceId_Type.__name__ = "OctetString"
_CnSonetRxPathTraceId_Object = MibTableColumn
cnSonetRxPathTraceId = _CnSonetRxPathTraceId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 3),
    _CnSonetRxPathTraceId_Type()
)
cnSonetRxPathTraceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnSonetRxPathTraceId.setStatus("current")


class _CnSonetExpectedPathTraceId_Type(OctetString):
    """Custom type cnSonetExpectedPathTraceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnSonetExpectedPathTraceId_Type.__name__ = "OctetString"
_CnSonetExpectedPathTraceId_Object = MibTableColumn
cnSonetExpectedPathTraceId = _CnSonetExpectedPathTraceId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 4),
    _CnSonetExpectedPathTraceId_Type()
)
cnSonetExpectedPathTraceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSonetExpectedPathTraceId.setStatus("current")
_CnSonetBipTestDuration_Type = Integer32
_CnSonetBipTestDuration_Object = MibTableColumn
cnSonetBipTestDuration = _CnSonetBipTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 5),
    _CnSonetBipTestDuration_Type()
)
cnSonetBipTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSonetBipTestDuration.setStatus("current")
_CnSonetTcaProfileId_Type = Integer32
_CnSonetTcaProfileId_Object = MibTableColumn
cnSonetTcaProfileId = _CnSonetTcaProfileId_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 6),
    _CnSonetTcaProfileId_Type()
)
cnSonetTcaProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSonetTcaProfileId.setStatus("current")


class _CnSonetRowStatus_Type(RowStatus):
    """Custom type cnSonetRowStatus based on RowStatus"""
    defaultValue = 1


_CnSonetRowStatus_Type.__name__ = "RowStatus"
_CnSonetRowStatus_Object = MibTableColumn
cnSonetRowStatus = _CnSonetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 18, 1, 1, 7),
    _CnSonetRowStatus_Type()
)
cnSonetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSonetRowStatus.setStatus("current")
_CnSonetModuleConformance_ObjectIdentity = ObjectIdentity
cnSonetModuleConformance = _CnSonetModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 18, 3)
)
_CnCnSonetGroups_ObjectIdentity = ObjectIdentity
cnCnSonetGroups = _CnCnSonetGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 18, 3, 1)
)

# Managed Objects groups

cnSonetCN1KObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 18, 3, 1, 1)
)
cnSonetCN1KObjectsGroup.setObjects(
      *(("CEM-SONET-MIB", "cnSonetLineStatus"),
        ("CEM-SONET-MIB", "cnSonetTxPathTraceId"),
        ("CEM-SONET-MIB", "cnSonetRxPathTraceId"),
        ("CEM-SONET-MIB", "cnSonetExpectedPathTraceId"),
        ("CEM-SONET-MIB", "cnSonetBipTestDuration"),
        ("CEM-SONET-MIB", "cnSonetTcaProfileId"),
        ("CEM-SONET-MIB", "cnSonetRowStatus"))
)
if mibBuilder.loadTexts:
    cnSonetCN1KObjectsGroup.setStatus("current")

cnSonetCNX5ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 18, 3, 1, 2)
)
cnSonetCNX5ObjectsGroup.setObjects(
      *(("CEM-SONET-MIB", "cnSonetLineStatus"),
        ("CEM-SONET-MIB", "cnSonetTxPathTraceId"),
        ("CEM-SONET-MIB", "cnSonetRxPathTraceId"),
        ("CEM-SONET-MIB", "cnSonetExpectedPathTraceId"),
        ("CEM-SONET-MIB", "cnSonetBipTestDuration"),
        ("CEM-SONET-MIB", "cnSonetTcaProfileId"),
        ("CEM-SONET-MIB", "cnSonetRowStatus"))
)
if mibBuilder.loadTexts:
    cnSonetCNX5ObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-SONET-MIB",
    **{"cnSonetModule": cnSonetModule,
       "cnSonetTable": cnSonetTable,
       "cnSonetEntry": cnSonetEntry,
       "cnSonetLineStatus": cnSonetLineStatus,
       "cnSonetTxPathTraceId": cnSonetTxPathTraceId,
       "cnSonetRxPathTraceId": cnSonetRxPathTraceId,
       "cnSonetExpectedPathTraceId": cnSonetExpectedPathTraceId,
       "cnSonetBipTestDuration": cnSonetBipTestDuration,
       "cnSonetTcaProfileId": cnSonetTcaProfileId,
       "cnSonetRowStatus": cnSonetRowStatus,
       "cnSonetModuleConformance": cnSonetModuleConformance,
       "cnCnSonetGroups": cnCnSonetGroups,
       "cnSonetCN1KObjectsGroup": cnSonetCN1KObjectsGroup,
       "cnSonetCNX5ObjectsGroup": cnSonetCNX5ObjectsGroup}
)
